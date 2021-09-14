#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate PS1 images from examples."""
from pathlib import Path
import subprocess
import shlex
import argparse

BDIR = Path(__file__).parent.parent
EXAMPLE_DIR = BDIR.joinpath("src/ps1api/examples")
LIGHT_DIR = EXAMPLE_DIR.joinpath("light")
DARK_DIR = EXAMPLE_DIR.joinpath("dark")

DSTDIR = BDIR.joinpath("media")

KONS_GEO = "1400x400,0+0"
CAP_GEO = "1350x340+1920+60"


def konsole(rcfile: Path, profile=None):
    cmd = shlex.split(
        f"konsole --nofork --geometry {KONS_GEO} -e bash --rcfile {rcfile.resolve()}"
    )
    if profile:
        cmd.insert(1, "--profile")
        cmd.insert(2, profile)
    return subprocess.Popen(cmd, stderr=subprocess.PIPE)


def screencap(dstfile: Path):
    cmd = shlex.split(
        f"import -window root -pause 3 -crop {CAP_GEO} {dstfile.resolve()}"
    )
    return subprocess.Popen(cmd)


def _iter_media_files():
    light_path = DSTDIR.joinpath("light")
    light_path.exists() or light_path.mkdir()

    dark_path = DSTDIR.joinpath("dark")
    dark_path.exists() or dark_path.mkdir()

    for i in LIGHT_DIR.iterdir():
        if not i.name.endswith(".sh"):
            continue
        yield "light", i, light_path.joinpath(f"{i.name}.png")

    for i in DARK_DIR.iterdir():
        if not i.name.endswith(".sh"):
            continue
        yield "dark", i, dark_path.joinpath(f"{i.name}.png")


def clean():
    light_path = DSTDIR.joinpath("light")
    dark_path = DSTDIR.joinpath("dark")
    for file in light_path.iterdir():
        print(f"Deleting {file}")
        file.unlink()
    for file in dark_path.iterdir():
        print(f"Deleting {file}")
        file.unlink()


def check():
    noexist = []
    for _, srcfile, dfile in _iter_media_files():
        if not dfile.exists():
            noexist.append(srcfile.name)
    if noexist:
        out = ",".join(noexist)
        raise SystemExit(f"The following media files need to be created for: {out}")


def main(overwrite=False):
    """Run main function."""
    for profile, srcfile, dfile in _iter_media_files():
        if not overwrite and dfile.exists():
            continue
        print(f"Creating: {dfile}")
        kons = konsole(srcfile, profile)
        sc = screencap(dfile)
        sc.communicate()
        kons.kill()


create = lambda: main()
overwrite = lambda: main(True)


MAP = {
    "create": [create],
    "overwrite": [overwrite],
    "clean": [clean],
    "check": [check],
    "regen": [
        clean,
        main,
    ],
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__,
    )
    parser.add_argument(
        "command",
        choices=MAP.keys(),
        type=str,
    )
    # args = parser.parse_args(["regen"])
    args = parser.parse_args()
    for func in MAP[args.command]:
        func()
