<img src="https://gist.githubusercontent.com/brianlechthaler/8137558340cc322e2d3acc1a740540d6/raw/1da63bfff411b1647e277e9b265939346fc5c845/qbitkit.svg" alt="qbitkit Official Logo (you may need to enable JavaScript to see this!)">

#### The Truly Universal Quantum Toolkit for Humans

## Documentation
For the time being, documentation is hosted at:
* https://qbitkit-docs-temporary.neutralthreat.com

## Example
Here we make a Bell State and submit it to the SV1 Quantum Simulator on AWS Braket.
```python
from qbitkit.provider.braket.circuit import circuitry as c
from qbitkit.provider.braket import provider as p
from qbitkit.io.frame import frame as f

# Define circuit dataframe
bellFrame = f.get_frame(data={'gate' : ['h','cnot'], 
                              'targetA' : [0,0], 
			                  'targetB' : [None, 1], 
			                  'targetC' : [None, None],})

# Translate the dataframe into a circuit we can run on AWS Braket
bellCircuit = c.translate.df_circuit(df=bellFrame)

# Get the Amazon SV1 Quantum Simulator to test our circuit on (this constitutes free-tier usage, so don't worry about cost!)
device = p.quantum_device.get_device(
         p.quantum_device.get_sim_arn(device='sv1'))

# Send job to quantum processor (in this case a simulated one)
job = device.run(bellCircuit, shots=10000,
                    s3_destination_folder=p.connection.get_bucket(
                    bucket='Your_AWS_Braket_Bucket_Here-Check_Your_S3_Console_After_Onboarding'))
# Show probabilities (should come out as close to 50/50 because the qubit we are measuring is superpositioned between 1 and 0)
print(job.result().measurement_probabilities)
```

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
#### Pip (coming soon)
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
