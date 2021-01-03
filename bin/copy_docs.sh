#!/bin/sh
echo "Usage: ./copy_docs.sh <input directory> <output directory> <webserver>"
export input=$1
export output=$2
export webserver=$3
rm -rf $output/*
cp -r $input/* $output
sudo service $webserver restart