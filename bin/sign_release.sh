#!/bin/sh
# This is supposed to be run in a DispVM with no network access, and takes advantage of the Qubes GPG proxy to ensure the highest level of security.
# More important than anything else is MAKING SURE TO USE SMART CARDS as this is the only way to effectively defend against malware stealing your private key(s)
export filename=$1.sig.asc

echo "Signing file $1 with $gpgBinary and saving to $filename"
cat $1 | qubes-gpg-client --sign --armor > $filename

echo "Detached Signature for file $1:"
cat $filename