import itertools
from itertools import combinations
from dwave.system.composites import EmbeddingComposite
from braket.ocean_plugin import BraketDWaveSampler
import time
from datetime import datetime as dt
import pandas as pd
import dimod
from math import log2, floor


# notebook specific config
dwave_qpu = 'Advantage_system1'
notebook_start_time = time.time()
#AWS specific config
# Please enter the S3 bucket you created during onboarding in the code below
def get_bucket(bucket=None, prefix=None):
    if bucket == None:
        bucket = None
    if prefix == None:
        my_prefix = "results" # the name of the folder in the bucket
    s3_folder = (bucket, prefix)
    return s3_folder

def get_qpu(vendor=None, device=None):
    status = 1
    if vendor == None:
        print('Warning: No quantum vendor specified')
        status = 0
    if device == None:
        print('Warning: No quantum device specified')
        status = 0
    arn = 'arn:aws:braket:::device/qpu/' + vendor + device
    return arn, status
def get_sim(vendor, device):
    arn = 'arn:aws:braket:::device/quantum-simulator/' + vendor + device