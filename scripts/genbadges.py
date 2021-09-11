#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import configparser
import pathlib

ME = pathlib.Path(__file__)
BASE = pathlib.Path(__file__).resolve().parent.parent
README = BASE.joinpath("README.md")
CFG = BASE.joinpath("setup.cfg")
STYLE = "plastic"

keymap = {
    "github-stars": "stargazers",
    "github-forks": "network/members",
    "github-issues": "issues",
}


def githubs(github):
    user, ext = github.split("/")
    urls = [
        f"https://img.shields.io/github/issues/{github}",
        f"https://img.shields.io/github/languages/code-size/{github}",
        f"https://img.shields.io/github/stars/{github}",
        f"https://img.shields.io/github/forks/{github}",
    ]
    for i in urls:
        arr = i.split("/")
        key = "-".join(i for i in arr[3:6] if i != user)
        if key in keymap:
            url = f"https://github.com/{github}/{keymap[key]}"
        else:
            url = f"https://github.com/{github}"
        yield f'[![{key}]({i}?style={STYLE} "{key}")]({url}) '


def pypis(pkgname):
    urls = [
        f"https://img.shields.io/pypi/v/{pkgname}",  # latest version
        f"https://img.shields.io/pypi/status/{pkgname}",  # stable / dev
        f"https://img.shields.io/pypi/l/{pkgname}",  # license
        f"https://img.shields.io/pypi/dm/{pkgname}",  # downloads / month
        f"https://img.shields.io/pypi/pyversions/{pkgname}",  # python versions
        f"https://img.shields.io/pypi/implementation/{pkgname}",  # implimentation
    ]
    for i in urls:
        arr = i.split("/")
        key = "-".join(arr[3:5])
        url = f"https://pypi.org/project/{pkgname}"
        yield f'[![{key}]({i}?style={STYLE} "{key}")]({url}) '


def get_badges():
    config = configparser.ConfigParser()
    config.read(CFG)
    pkgname = config.get("metadata", "name").replace("_", "-")
    github = "/".join(pathlib.Path(config.get("metadata", "url")).parts[-2:])
    b_github = "".join(githubs(github))
    b_pypi = "".join(pypis(pkgname))
    return "\n\n".join([b_github, b_pypi])


def main():
    """Run main function."""
    content = get_badges()
    with README.open("r+") as fileh:
        data = fileh.read()
        fileh.seek(0)
        data = content + "\n\n" + data
        fileh.write(data)
        fileh.flush()


if __name__ == "__main__":
    main()
