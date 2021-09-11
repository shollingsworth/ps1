#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a ps1 prompt."""
import ps1api
import argparse

Base = ps1api.Base

TEMPLATE_MAP = {}
for i in dir(ps1api):
    if i.startswith("_"):
        continue
    attr = getattr(ps1api, i)
    if not isinstance(attr, type):
        continue
    if not issubclass(attr, ps1api.Base):
        continue
    TEMPLATE_MAP[i.lower()] = attr


FUNC_MAP = {Base.add_custom.__name__: {}}


parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=__doc__,
)

parser.add_argument(
    "-t",
    "--template",
    type=str,
    required=False,
    choices=TEMPLATE_MAP.keys(),
    default="base",
)


def main(args):
    """Run main function."""
    obj = TEMPLATE_MAP[args.template]()  # type: ps1api.Base
    print(obj.output())
    # obj = ps1api.PromptBase()
    # obj.add_working_directory()
    # print(obj.output())


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
