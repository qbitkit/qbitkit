#!/bin/sh
echo "Usage: ./update_docs.sh <make subcommand> <path to copy docs to>"
echo "Updating APT..."
sudo apt-get update > /dev/null
echo "Upgrading APT..."
sudo apt-get upgrade -y -qq > /dev/null
git pull
. ../doc/sphinx/venv/bin/activate
pip install -Ur ../requirements.txt
pip install -Ur ../doc/sphinx/requirements.txt
cd ..
python setup.py build
python setup.py install
cd doc/sphinx/
rm -rf _*
make -j $(nproc) $1
sudo /bin/sh ../../bin/copy_docs.sh _build/html $2 nginx