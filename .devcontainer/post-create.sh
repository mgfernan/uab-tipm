#!/usr/bin/env bash

set -euo pipefail

python3 -m pip install --user --upgrade pip
python3 -m pip install --user jupyter matplotlib numpy pandas

quarto --version
python3 --version
jupyter --version