#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate pypy Markdown without broken links."""
import pathlib
import configparser
import re

BASE = pathlib.Path(__file__).resolve().parent.parent
CFG = BASE.joinpath("setup.cfg")
README = BASE.joinpath("README.md")
DESTFILE = BASE.joinpath(".pypyreadme")


def main():
    """Run main function."""
    config = configparser.ConfigParser()
    config.read(CFG)
    vals = [
        list(map(str.strip, i.strip().split("=")))
        for i in config.get("metadata", "project_urls").splitlines()
        if i.strip()
    ]
    urls = {i[0]: i[1] for i in vals}
    url = urls["Source Code"]
    pattern = re.compile(r"\]\(([.A-Za-z0-9].*?)\)")

    def _sub_func(match: re.Match):
        full = match.group(0)
        possible_path = match.group(1)
        path = BASE.joinpath(possible_path)
        ext = str(path).replace(str(BASE) + "/", "")
        if path.exists():
            ntxt = f"{url}/blob/main/{ext}"
            return full.replace(possible_path, ntxt)
        return match.group(0)

    content = re.sub(pattern, _sub_func, README.read_text())
    DESTFILE.write_text(content)


if __name__ == "__main__":
    main()
