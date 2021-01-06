#!/bin/sh
echo "Usage: ./bootstrap_host.sh <RELEASE>"
sudo apt update
sudo apt upgrade -y
sudo apt install -y build-essential git python3-pip nginx
sudo -H pip3 install -U pip
sudo -H pip3 install -U virtualenv
curl -C - https://pkg.cloudflare.com/pubkey.gpg | sudo apt-key add -
echo 'deb http://pkg.cloudflare.com/ $1 main' | sudo tee /etc/apt/sources.list.d/cloudflare-main.list
sudo apt update
sudo apt install -y cloudflared
/bin/sh ./mkdocs.sh
/bin/sh ./update_docs.sh
cloudflared tunnel login