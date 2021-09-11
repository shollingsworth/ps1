#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Version bumper on upload."""
import pathlib
import subprocess
import sys

BASE = pathlib.Path(__file__).resolve().parent.parent
VFILE = BASE.joinpath("VERSION")


def _run(cmd):
    output = subprocess.check_output(cmd, encoding="utf-8").strip()
    return " ".join(cmd), output


def _check_clean():
    _, out = _run(
        [
            "git",
            "status",
            "--short",
        ]
    )
    if not out.strip():
        return True
    return False


def bump():
    """Run main function."""
    if not _check_clean():
        raise SystemExit("Working directory is not clean, bailing")
    prev = VFILE.read_text().strip()
    major, minor, bugfix = map(int, VFILE.read_text().strip().split("."))
    bugfix += 1
    new = ".".join(map(str, [major, minor, bugfix]))
    sys.stderr.write(f"Bumping version from: {prev} to {new}\n")
    with open(str(VFILE), "w") as fileh:
        fileh.write(new)
        fileh.flush()


def main():
    bump()


if __name__ == "__main__":
    main()
