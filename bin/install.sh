#!/bin/bash
# Set runtime variables
export install_project=qbitkit
export venv_name=venv
# Update Pip
python3 -m pip install -U --user pip
# Install virtualenv
python3 -m pip install -U --user virtualenv
# Go to the parent directory where the root of the repo should be
cd ..
# Create a virtual environment
python3 -m virtualenv --python python3 $venv_name
# Activate the virtual environment
. venv/bin/activate
# Make sure pip and setuptools inside the virtualenv are up-to-date
python3 -m pip install -U pip
# Install Dependencies
python3 -m pip install -U -r requirements.txt
# Build python package
python3 setup.py build
# Install Python package
python3 setup.py install
# Save current directory as env var, and use it to get the full path of our venv that we created
export dir=$(pwd)
export venv_dir=$dir/$venv_name
export activate_path=$venv_dir/bin/activate
# Give user some helpful information
echo "Install complete." 
echo "To access the virtual environment with $install_project installed in it, run this command or put it in your shell's configuration (example: .bashrc):"
echo ". $activate_path"