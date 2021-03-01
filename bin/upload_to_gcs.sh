#!/bin/sh
echo "Usage: ./mkdocs.sh <make cmd> <storage bucket optionally including prefix>"
echo "Building $1 Site + Docs ..."
/bin/sh ./mksite.sh "$1"
echo "Uploading $1 docs to $2 with gsutil ..."
gsutil -m cp -r ../doc/sphinx/_build/html "gs://$2"