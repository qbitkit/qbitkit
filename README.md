<img src="https://gist.githubusercontent.com/brianlechthaler/8137558340cc322e2d3acc1a740540d6/raw/1da63bfff411b1647e277e9b265939346fc5c845/qbitkit.svg" alt="qbitkit Official Logo (you may need to enable JavaScript to see this!)">



# ⚛ `qbitkit` [Docs](https://qbitkit-docs-temporary.neutralthreat.com/index.html) ![CodeQL](https://github.com/qbitkit/qbitkit/workflows/CodeQL/badge.svg) 

#### Quantum Computing, for Humans.
`qbitkit` is a set of high-level abstractions to make writing software for quantum computers easier. 
Gates are defined using a Pandas DataFrame that can be automatically translated to your platform of choice.
Once you've translated a DataFrame to your platform of choice, for example AWS Braket or IBMQ, all you have to do is run it and check the results.
All of this, in just 3 lines of code (not counting import statements, comments, whitespace lines, or printing results.) 

### Example
Here we make a Bell State and submit it to the SV1 Quantum Simulator on AWS Braket.
```python
# Import relevant qbitkit Libraries
from qbitkit.provider.braket.circuit import circuitry as c
from qbitkit.provider.braket import provider as p
from qbitkit.io.frame import frame as f

# Define your DataFrame as a circuit, then translate it to your platform of choice.
circuit = c.translate.df_circuit(df=f.get_frame(
    data={'gate' : ['h','cnot'], 
          'targetA' : [0,0], 
          'targetB' : [None, 1], 
          'targetC' : [None, None],}))
# Run the circuit on the Rigetti Aspen-8 hosted on AWS Braket
job = p.job.get_job(device=p.quantum_device.get_device(
                        p.quantum_device.get_qpu_arn(
                            # Pick the Aspen-8 Quantum Computer by Rigetti as our QPU
                            vendor='rigetti', device='Aspen-8')),
                    circuit=circuit,
                    s3loc=p.connection.get_bucket(
                      #Use the name of the bucket created at Braket onboarding.
                      # You can always check your S3 Console to find this info.
                      bucket='amazon-braket-YourID'), 
                    # Warning: Running this will cost a little under $4.
                    shots=10000 )
# Show all of the results
```

## Documentation
For the time being, documentation is hosted at:
* https://qbitkit-docs-temporary.neutralthreat.com



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
#### Pip (coming soon)
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
#### Installer Script (recommended)
1) Change directory into qbitkit/bin
* `cd bin`
2) Run script
* `/bin/sh install.sh`
#### Pip (coming soon)
1) Make sure `pip` is up-to-date, then install `qbitkit`:
* with root, system install: `sudo -H pip install -U qbitkit`
* without root, user install: `pip install --user -U qbitkit`
#### Python Virtual Environment
1) Clone `qbitkit` locally, then `cd` to the directory you just cloned:
* `git clone https://github.com/qbitkit/qbitkit.git`
* `cd qbitkit`
2) Create a virtual environment, then activate it: 
* `virtualenv --python=python3 venv && . venv/bin/activate`
3) Install requirements, then use `setup.py` to build `qbitkit` then install `qbitkit` into the virtualenv: 
* `pip install -r requirements.txt && python setup.py build && python setup.py install`

## Features of `qbitkit`
* With such a diverse range of quantum hardware and cloud services providing that hardware to end users, having to rewrite the same circuits 2-3 times is not uncommon. With `qbitkit`, hardware and cloud providers are abstracted and made as simple to use as possible. Stop re-inventing the wheel, and start actually innovating with the ease of use and flexibility of `qbitkit`.
* Define your circuit using a Pandas DataFrame, translate it to your quantum provider of choice, and run it -- in just a few lines of code.
* Running quantum circuits often requires costly hardware access and long wait times. It is therefore beneficial to keep track of your results so you don't have to re-run experiments to reproduce the results. For this reason, we included support for **logging** to Elasticsearch, with support for other ways to log your data coming soon.
* Check the *Issues* tab at the top of this repository's page to see features we're working on now and the status of implementing those features into `qbitkit`

## Project Lifecycle
* Visibility: 
    * Public
    * Released: January 1st, 2021
* Status:
    * Active development as of December 16th
* Health:
    * Green (healthy)
    * Preparing for v1.0.0 (stable)
    * Code examples needed  
    * Extensive testing will still be necessary prior to public release
