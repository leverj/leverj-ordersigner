#!/usr/bin/env bash

# ensure a python3 virtual env exists in `.venv`, i.e.: `python3 -m venv .venv`
source .venv/bin/activate
pip install --upgrade pip
pip install .

# for development
pip install -e .[dev]
