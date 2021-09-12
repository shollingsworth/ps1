#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import sys
import argparse
from argparse import ArgumentParser
import ps1api

ME = Path(__file__)
BASE = Path(__file__).resolve().parent.parent
BINDIR = BASE.joinpath("bin")
README = BASE.joinpath("README.md")
MEDIA_DIR = BASE.joinpath("media")
EXAMPLES_DIR = BASE.joinpath("src/ps1api/examples")
sys.path.append(str(BINDIR.absolute()))

GITHUB_BASE = "https://github.com/shollingsworth/ps1"
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/shollingsworth/ps1"


def _iter_subpaser_helps(parser: ArgumentParser):
    sub_parser_actions = [
        action
        for action in parser._actions
        if isinstance(action, argparse._SubParsersAction)
    ]
    for action in sub_parser_actions:
        for choice, subparser in sorted(action.choices.items()):
            htxt = subparser.format_help()
            htxt = htxt.replace(ME.name, "ps1")
            yield choice, htxt


def _iter_examples(p: Path = None):
    if p is None:
        p = EXAMPLES_DIR
    for i in p.iterdir():
        if i.is_dir():
            yield from _iter_examples(i)
        else:
            mpath = MEDIA_DIR.joinpath("/".join(i.parts[-2:]) + ".png")
            if not mpath.exists():
                raise SystemExit(f"{mpath} does not exist")
            yield i, mpath


def _get_example_output():
    lines = []
    for srcfile, media in sorted(_iter_examples()):
        srclink = f"{GITHUB_BASE}/blob/main/{srcfile.relative_to(BASE)}"
        imglink = f"{GITHUB_RAW_BASE}/main/{media.relative_to(BASE)}"
        lines.append(f"### [{srcfile.name}]({srclink})")
        lines.append(f"![{srcfile.name}]({imglink})")
        lines.append("\n")
    return "\n".join(lines)


def _get_ps1_output(parser):
    lines = []
    for choice, content in _iter_subpaser_helps(parser):
        lines.append(f"### subcommand {choice}")
        lines.append("```")
        lines.append(content)
        lines.append("```")
        lines.append("\n")
    return "\n".join(lines)


def main():
    """Run main function."""
    mod = __import__("ps1")
    template_map = mod._gen_template(ps1api)
    parser = mod._get_parser(template_map, ps1api.Base)  # type: ArgumentParser

    with README.open("r+") as fileh:
        fmt = _get_ps1_output(parser)
        data = fileh.read()
        fileh.seek(0)
        data = data.replace("__PS1__", fmt)
        fileh.write(data)
        fileh.flush()

    with README.open("r+") as fileh:
        fmt = _get_example_output()
        data = fileh.read()
        fileh.seek(0)
        data = data.replace("__EXAMPLES__", fmt)
        fileh.write(data)
        fileh.flush()


if __name__ == "__main__":
    main()
