#!/bin/sh
# Set runtime variables
export venv_pkg=setuptools
export python_cmd=python3
export install_project=qbitkit
export venv_name=venv
# Set aliases
alias py=$python_cmd
# Update Pip
py -m pip install -U --user pip
# Install virtualenv
py -m pip install -U --user virtualenv
# Save current directory as env var
export origin_dir=$(pwd)
# Go to the parent directory where the root of the repo should be
cd ..
# Create a virtual environment
py -m virtualenv --python $python_cmd $venv_name
# Activate the virtual environment
. venv/bin/activate
# Install Dependencies
py -m pip install -U -r $venv_pkg
py -m pip install -U -r requirements.txt
# Build python package
py setup.py build
# Install Python package
py setup.py install
# Save current directory as env var, and use it to get the full path of our venv that we created
export dir=$(pwd)
export venv_dir=$dir/$venv_name
export activate_path=$venv_dir/bin/activate
# Go back to the directory we were invoked from
cd $origin_dir
# Reset bash (de-activate the environment we created)
source ~/.bashrc
# Give user some helpful information
echo "Install complete."
echo "To access the virtual environment with $install_project installed in it, run this command or put it in your shell's configuration (example: .bashrc):"
echo ". $activate_path"