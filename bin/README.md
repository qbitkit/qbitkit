# `qbitkit` Shell Scripts
## For End-Users:
### `install.sh`
* Description: Installs `qbitkit` into a new Python Virtual Environment.
* Pre-requisites: You need Python3.x with the latest version of `pip` and `virtualenv` installed.
### `install_without_venv.sh`
* Description: Installs `qbitkit`.
* Pre-requisites: You need Python3.x with the latest version of `pip` installed.
### `mkdocs.sh`
* Description: Builds Documentation in specified format. For example, to build HTML documentation, `./mkdocs.sh html`
* Pre-requisites: You need Python3.x with the latest version of `pip` and `virtualenv` installed.
## For Developers:
### `copy_docs.sh`
* Description: Copies compiled documentation to a specified folder, for example `/var/www/html`.
* Pre-requisites: You need Python3.x with the latest version of `pip` and `virtualenv` installed.
### `update_docs.sh <make subcommand> <copy docs to this path>`
* Description: Pulls new changes from `git`, wipes <copy docs to this path>, and copies documentation to it. Exactly like the syntax of `mkdocs.sh`, you **must** specify the type of docs to output, for example `html`: `./update_docs.sh html /var/www/html`
* Pre-requisites: You need Python3.x with the latest version of `pip` and `virtualenv` installed.
* Notes: Once you've verified running this script works, add a `cron` job to your system's `crontab` to make sure you're always hosting the latest version of `qbitkit`'s documentation.
### `update_site.sh <make subcommand> <copy site to this path>`
* Description: Pulls new changes from `git`, wipes <copy site to this path>, and copies documentation to it. Exactly like the syntax of `mkdocs.sh`, you **must** specify the type of docs to output, for example `html`: `./update_docs.sh html /var/www/html`
* Pre-requisites: You need Python3.x with the latest version of `pip` and `virtualenv` installed.
* Notes: Once you've verified running this script works, add a `cron` job to your system's `crontab` to make sure you're always hosting the latest version of `qbitkit`'s documentation.
### `mkrelease.sh`
* Description: Build a Python Release from the current repository
* Pre-requisites: You need Python3.x with the latest version of `pip` and `virtualenv` installed.
### `sign_release.sh`
* Description: Use the Qubes Split GPG to securely sign releases.
* Pre-requisites: You need Qubes OS installed and up-to-date with 
* Notes: You **must** take the highest precautions when building and signing releases. **Do not use GPG without a Smart Card!** Even if you have your keys in a separate VM and access them with Qubes Spit GPG, your key material is still stored on your system's disk. For the highest level of security, please make sure to use a Smart Card device such as a Smart Card with a USB Smart Card reader or a Yubikey. I use my personal Yubikey 4 in conjunction with the Qubes Split GPG to sign all `qbitkit` releases at the highest possible levels of security. As for building releases, new disposable machines are started to build a release, and destroyed immediately afterwards. This significantly decreases the amount of state the system holds, thus making it more difficult to compromise the building and signing process. 
### `bootstrap_host.sh`
* Description: Setup CloudFlare's Argo Tunnel to route traffic without exposing ports on the host. Compile docs as HTML. Finally, copy the compiled HTML to /var/www/html.
* Pre-requisites: None, this takes care of all of that for you. Just make sure you **run this script on Debian 10 ("Buster")**