#!/bin/bash
# Update Pip
sudo -H python3 -m pip install -U pip
# Make Sure Setup Tools are installed
sudo -H python3 -m pip install -U setuptools
# Go to the parent directory where the root of the repo should be
cd ..
# Make sure pip and setuptools inside the virtualenv are up-to-date
sudo -H python3 -m pip install -U pip
# Install Dependencies
sudo -H python3 -m pip install -U -r requirements.txt
# Build python package
python3 setup.py build
# Install Python package
sudo -H python3 setup.py install