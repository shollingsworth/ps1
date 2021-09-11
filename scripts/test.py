#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Testing README work."""
from freeplane_tools.github import MindMap2GithubMarkdown
from freeplane_tools.bitbucket import MindMap2BitBucket
from freeplane_tools.data import get_template
import pathlib
import tempfile


def banner(msg):
    print("*" * 50)
    print("*" * 50)
    print(msg)


def main():
    """Run main function."""
    with tempfile.TemporaryDirectory() as tmpdir:
        path = pathlib.Path(tmpdir).resolve()
        gen = path.joinpath("template.mm")
        gen.write_bytes(get_template())

        github_file = path.joinpath("github.md")
        bb_file = path.joinpath("bitbucket.md")

        banner(f"Generated: {gen}")
        banner(f"Contents: {gen.read_text()}")

        github = MindMap2GithubMarkdown(gen)
        banner(f"Writing: {github_file}")
        github.write_document(github_file)
        banner(f"Contents: {github_file.read_text()}")

        bitbucket = MindMap2BitBucket(gen)
        banner(f"Writing: {bb_file}")
        bitbucket.write_document(bb_file)
        banner(f"Contents: {bb_file.read_text()}")


if __name__ == "__main__":
    main()
