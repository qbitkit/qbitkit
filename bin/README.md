# `qbitkit` Shell Scripts
## For End-Users:
### ![install.sh](https://github.com/qbitkit/qbitkit/workflows/Test%20Install%20Script/badge.svg) `install.sh`
* Description: Installs `qbitkit` into a new Python Virtual Environment.
* Pre-requisites: You need Python3.x with the latest version of `pip` and `virtualenv` installed.
### ![install_without_venv.sh](https://github.com/qbitkit/qbitkit/workflows/Test%20Install%20(no%20venv)%20Script/badge.svg) `install_without_venv.sh`
* Description: Installs `qbitkit`.
* Pre-requisites: You need Python3.x with the latest version of `pip` installed.
### ![mkdocs.sh](https://github.com/qbitkit/qbitkit/workflows/mkdocs.sh/badge.svg) `mkdocs.sh`
* Description: Builds Documentation in specified format. For example, to build HTML documentation, `./mkdocs.sh html`
* Pre-requisites: You need Python3.x with the latest version of `pip` and `virtualenv` installed.
## For Developers:
### *tested in scripts `update_docs.sh` and `update_site.sh`* `copy_docs.sh`
* Description: Copies compiled documentation to a specified folder, for example `/var/www/html`.
* Pre-requisites: You need Python3.x with the latest version of `pip` and `virtualenv` installed.
### `update_docs.sh <make subcommand> <copy docs to this path>`
#### ![update_docs.sh](https://github.com/qbitkit/qbitkit/workflows/update_docs.sh/badge.svg) 
* Description: Pulls new changes from `git`, wipes <copy docs to this path>, and copies documentation to it. Exactly like the syntax of `mkdocs.sh`, you **must** specify the type of docs to output, for example `html`: `./update_docs.sh html /var/www/html`
* Pre-requisites: You need Python3.x with the latest version of `pip` and `virtualenv` installed.
* Notes: Once you've verified running this script works, add a `cron` job to your system's `crontab` to make sure you're always hosting the latest version of `qbitkit`'s documentation.
### `update_site.sh <make subcommand> <copy site to this path>`
#### ![update_site.sh](https://github.com/qbitkit/qbitkit/workflows/update_site.sh/badge.svg)
* Description: Pulls new changes from `git`, wipes <copy site to this path>, and copies documentation and site to it. Exactly like the syntax of `mkdocs.sh` and `update_docs.sh`, you **must** specify the type of docs to output, for example `html`: `./update_docs.sh html /var/www/html`
* Pre-requisites: You need Python3.x with the latest version of `pip` and `virtualenv` installed.
* Notes: Once you've verified running this script works, add a `cron` job to your system's `crontab` to make sure you're always hosting the latest version of `qbitkit`'s documentation.
### `mkrelease.sh`
#### ![mkrelease.sh](https://github.com/qbitkit/qbitkit/workflows/mkrelease.sh/badge.svg) 
* Description: Build a Python Release from the current repository
* Pre-requisites: You need Python3.x with the latest version of `pip` and `virtualenv` installed.
### `new_branch.sh`
##### ![new_branch.sh](https://github.com/qbitkit/qbitkit/workflows/new_branch.sh/badge.svg)
* Description: Switch branch from `origin` (old branch name) to `main` (new branch name.)
* Pre-Requisites: `git`, though it's quite likely you already have this ready to go if you are reading this README.
### `sign_release.sh`
* Description: Use Qubes Split GPG to securely sign releases.
* Pre-requisites: You need Qubes OS installed and up-to-date with 
* Notes: You **must** take the highest possible precautions when building and signing new releases. **Do not use GPG without a Smart Card!** Even if you have your keys in a separate VM and access them with Qubes Spit GPG, your key material is still stored on your system's disk. For the highest level of security, please make sure to use a Smart Card device such as a Smart Card with a USB Smart Card reader or a Yubikey. I use my personal Yubikey 4 in conjunction with Qubes Split GPG to sign all `qbitkit` releases with the highest possible levels of security. To build new releases, new disposable machines are started to build a release, and destroyed immediately afterwards. This significantly decreases the amount of state the system holds, thus making it more difficult for an adversary to compromise the building and signing process. 
### `mksite.sh`
##### [![mksite.sh](https://github.com/qbitkit/qbitkit/actions/workflows/test_mksite.yml/badge.svg)](https://github.com/qbitkit/qbitkit/actions/workflows/test_mksite.yml)
