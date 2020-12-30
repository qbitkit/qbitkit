#!/bin/sh
# Print usage
echo "mkdocs.sh <make argument>"
# Change directory to where we have our docs to build
cd ..
cd doc
cd sphinx
# Create a new virtual environment
virtualenv -p python3 venv
# Activate virtual environment
. venv/bin/activate
# Make sure pip is up-to-date
pip install -U pip
# Install dependencies for building documentation
pip install -Ur requirements.txt
# Set default AWS region
aws configure set region us-east-1
# Build documentation
make $1
# Reset shell to deactivate the virtual environment we are in
source ~/.bashrc