#!/bin/sh
echo "Usage: ./update_site.sh <make subcommand> <path to copy site to>"
echo "Pulling latest updates from git..."
git pull
. ../doc/sphinx/venv/bin/activate
echo "Ensuring dependencies are up-to-date..."
pip install -Ur ../requirements.txt > /dev/null
pip install -Ur ../doc/sphinx/requirements.txt > /dev/null
cd ..
echo "Re-building qbitkit..."
python setup.py build > /dev/null
echo "Re-installing qbitkit..."
python setup.py install > /dev/null
cd doc/sphinx/
rm -rf _*
echo "Compiling documentation..."
make -j $(nproc) $1
echo "Injecting homepage..."
mkdir -p homepage/docs
mv _build/html/* homepage/docs
rm -rf _build/html/*
mv homepage/* _build/html/
echo "Copying compiled docs to specified directory..."
sudo /bin/sh ../../bin/copy_docs.sh _build/html $2 nginx