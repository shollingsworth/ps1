#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="ps1",
    install_requires=[
        "colored>=1.4.2",
    ],
    scripts=[
        "bin/ps1",
    ],
)
