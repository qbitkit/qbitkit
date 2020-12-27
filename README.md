<img src="https://raw.githubusercontent.com/brianlechthaler/qbitkit/origin/doc/assets/qbitkit-logo-rasterized.svg?token=AAP7F43SB4JJGFMPT2AMRXK747USU">

Universal Quantum Toolkit for Humans

## Installing `qbitkit`
### Anaconda3 (Windows/Mac/Linux)
1) Download Anaconda3:
* Click [this link](https://www.anaconda.com/products/individual) to download Anaconda3 from the official page for Anaconda Individual Edition
2) After downloading and installing, open `Anaconda Prompt` and type:
* `conda create -n qbitkit` (hit enter)
* `conda activate qbitkit` (hit enter)
* `conda install -y pip` (hit enter)
3) If you are using Mac or Linux, skip this step. If you are using Windows, install Git for Windows:
* Download Git for Windows from git-scm.org using [this link](https://git-scm.com/download/win)
* Open the installer, complete the installation.
* Reminder: paths listed below, for example `venv/bin/activate` work for Mac and Linux, but on Windows you must change any `/` to `\` before running a command *unless* that `/` is in a URL, in which case leave it alone. Consider installing Debian alongside or in place of Windows if this bothers you.
#### Pip (available at launch)
1) Make sure `pip` is up-to-date, then install using `pip`: 
* `pip install -U pip`
* `pip install -U qbitkit`
#### Virtual Environment
1) Locally clone `qbitkit`, `cd` into the directory we just cloned it into:
* `git clone https://github.com/brianlechthaler/qbitkit.git`
* `cd qbitkit`
2) Update `pip`, install `virtualenv`, create a virtual environment, then activate it:
* `pip install -U pip`
* `pip install -U virtualenv`
* Mac and Linux: `. venv/bin/activate`
* Using Windows: `. venv\bin\activate`
3) Install Dependencies:
* `pip install -Ur requirements.txt`
4) Build and Install with `setup.py`:
* `python setup.py build`
* `python setup.py install`
### Linux
1) Make sure you have `pip` and `virtualenv` installed, for example on Debian-based systems you can use `apt-get` and `pip` as root: 
* `sudo apt-get install -qq -y python3-pip && sudo -H pip3 install -U pip && sudo -H pip3 install -U virtualenv`
2) To make sure you're using the right `pip` from the right `python`, you should **run this command before running subsequent commands**:
* `alias 'pip=python3 -m pip'`
3) You may need `git` if it isn't yet installed, for example on Debian-based systems:
* `sudo apt-get install -qq -y git`
#### Pip (available at launch)
1) Make sure `pip` is up-to-date, then install `qbitkit`:
* with root, system install: `sudo -H pip install -U qbitkit`
* without root, user install: `pip install --user -U qbitkit`
#### Python Virtual Environment (recommended)
1) Clone `qbitkit` locally, then `cd` to the directory you just cloned:
* `git clone https://github.com/brianlechthaler/qbitkit.git`
* `cd qbitkit`
2) Create a virtual environment, then activate it: 
* `virtualenv --python=python3 venv && . venv/bin/activate`
3) Install requirements, then use `setup.py` to build `qbitkit` then install `qbitkit` into the virtualenv: 
* `pip install -r requirements.txt && python setup.py build && python setup.py install`

## Project Lifecycle
* Minimum Viable Product Target Deadline:
    * January 1-15th, 2021
* Visibility: 
    * Contents considered confidential until publicly released
    * Private
    * Release ETA: Q1 2021
* Status:
    * Active development as of December 16th
* Health:
    * Yellow (unhealthy)
    * nearing minimum viable product stage
    * while there's theoretically enough of `qbitkit` working at this point, core features are still missing or underdeveloped.
    * extensive testing will still be necessary prior to public release
