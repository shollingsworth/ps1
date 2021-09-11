#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pathlib
import os
import sys
from argparse import ArgumentParser

ME = pathlib.Path(__file__)
BASE = pathlib.Path(__file__).resolve().parent.parent
BINDIR = BASE.joinpath("bin")
README = BASE.joinpath("README.md")

sys.path.append(str(BINDIR.absolute()))


def get_parser(mod) -> ArgumentParser:
    return mod.parser


def _iterhelps():
    for script in BINDIR.glob("*"):
        if any(
            [
                script.is_dir(),
                not os.access(script, os.X_OK),
            ]
        ):
            continue
        mod_name = script.name.replace(".py", "")
        parser = get_parser(__import__(mod_name))
        out = parser.format_help().replace(ME.name, script.name)
        yield script.name, out


def main():
    """Run main function."""
    txt = []
    for name, help_diag in sorted(_iterhelps()):
        txt.append(f"*{name}*")
        txt.append("```")
        txt.append(help_diag)
        txt.append("```")
        txt.append("---")
    fmt = "\n".join(txt)
    with README.open("r+") as fileh:
        data = fileh.read()
        fileh.seek(0)
        data = data.replace("__CLI_COMMANDS__", fmt)
        fileh.write(data)
        fileh.flush()


if __name__ == "__main__":
    main()
