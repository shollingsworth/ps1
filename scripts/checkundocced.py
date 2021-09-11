#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check to make sure pydoctor doesn't have any undocumented values."""
from bs4 import BeautifulSoup, Tag
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
UNDOC = BASE.joinpath("docs", "undoccedSummary.html")

xml = BeautifulSoup(UNDOC.read_bytes(), features="lxml")
ul = xml.find("ul", attrs={"id": "summaryTree"})  # type: Tag
undocs = []
for i in ul.findAll("li"):
    undocs.append(i.text.split(" - "))

for _type, place in undocs:
    print(f"{_type}\n\t{place}")

if undocs:
    raise SystemExit("Undocumented Values Found (see above)")
