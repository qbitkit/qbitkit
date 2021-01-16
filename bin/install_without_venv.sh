#!/bin/bash
# Update Pip
python3 -m pip install -U --user pip
# Go to the parent directory where the root of the repo should be
cd ..
# Make sure pip and setuptools inside the virtualenv are up-to-date
python3 -m pip install -U pip
# Install Dependencies
python3 -m pip install -U -r requirements.txt
# Build python package
python3 setup.py build
# Install Python package
python3 setup.py install