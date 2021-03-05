#!/bin/sh
echo "Usage: ./mkdocs.sh <make cmd> <storage bucket optionally including prefix>"
echo "Building $1 Site + Docs ..."
time /bin/sh ./mksite.sh "$1"
echo "Removing venv directory used to build documentation ..."
time rm -rf ../docs/venv/
echo "Uploading $1 docs to $2 with gsutil ..."
time gsutil -m rsync -r ../doc/sphinx/_build/html/ "gs://$2"