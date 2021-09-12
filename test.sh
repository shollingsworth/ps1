#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

unset PYTHONPATH
rm -rfv venv/
virtualenv venv
vim setup.cfg
vim MANIFEST.in 
make pkg 
source venv/bin/activate
pip3 install ./dist/ps1-0.0.1.tar.gz
# python3 setup.py install
find venv/|grep ps1
