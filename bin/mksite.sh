#!/bin/sh
# Print usage
echo "mkdocs.sh <make argument>"
# Change directory to where we have our docs to build
cd ../doc/sphinx
# Create a new virtual environment
virtualenv -p python3 venv
# Activate virtual environment
. venv/bin/activate
# Make sure pip is up-to-date
pip install -U pip
# Install dependencies for building documentation
pip install -Ur requirements.txt
# Go to repository root
cd ../..
# Install qbitkit dependencies
pip install -Ur requirements.txt
# Build qbitkit
python setup.py build
# Install qbitkit
python setup.py install
# Go back to the folder containing the documentation we're going to compile
cd doc/sphinx
# Build documentation
make $1
# Inject homepage
echo "Injecting homepage..."
mkdir -p homepage/docs
mv _build/html/* homepage/docs
rm -rf _build/html/*
mv homepage/* _build/html/