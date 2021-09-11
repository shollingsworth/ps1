#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup
from glob import glob
from itertools import chain

SCRIPTS = [
    i
    for i in chain(
        glob("bin/*.py"),
    )
]

setup(
    name="ps1",
    install_requires=[
        "colored>=1.4.2",
    ],
    scripts=SCRIPTS,
)
