#!/bin/sh
cd bin
apt-get update
apt-get upgrade -y
apt-get install -y python3-pip python3-virtualenv
/bin/sh ./upload_to_gcs.sh "$1" "$2"