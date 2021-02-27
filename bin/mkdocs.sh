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
# Just in case we're running on a system without Bash installed, let's create an empty file at ~/.bashrc so that the next command won't cause the image build to fail.
touch ~/.bashrc
# Reset shell to deactivate the virtual environment we are in
source ~/.bashrc