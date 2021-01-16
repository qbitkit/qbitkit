# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version     | Supported          |
| ----------- | ------------------ |
| origin      | :white_check_mark: |
| 1.0.0       | :white_check_mark: |
| 1.0.0-beta  | :x:  *Archival*    |
| 1.0.0-alpha | :x:  *Archival*    |

## Reporting a Vulnerability

Immediately report all your findings in as much detail as possible in a report to the project maintainer, brianlechthaler (at) protonmail (dot) ch

We strongly encourage you to encrypt your message using the key located in `doc/official_gpg_key.asc` to make sure the only people who are aware of the vulnerability you are reporting are only you and the project maintainer. This isn't a requirement, but we emplore you to do this.

## Release Integrity
We take security very seriously, and employ various procedures to ensure all releases are built in the most secure way possible, and securely digitally signed with hardware keys.
### Overview
* All releases are cryptographically signed using the project maintainer's personal Yubikey 4. You can find this GPG key that's used to sign all releases under the doc/ directory.
* All steps are exclusively performed on Qubes OS on a system with Intel AMT neutralized and disabled at the factory, as well as bootloader tamper evidence with PureBoot.
### Release Building Process
1) Start new Disposable Virtual Machine.
2) Clone `qbitkit`: `git clone https://github.com/qbitkit/qbitkit.git`.
3) Start Build Script: `cd bin ; /bin/sh mkrelease.sh`.
4) Create new offline disposable virtual machine.
5) Use `qvm-copy` to copy the whole repository over to the Disposable VM.
6) Run the signing script as `cd qbitkit/bin ; /bin/sh sign_release.sh <path_to_built_release>`.
7) Use `qvm-copy` to copy the releases along with the signatures to another Disposable VM with your favorite browser running and logged into GitHub.
