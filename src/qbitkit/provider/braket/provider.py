import itertools
from itertools import combinations
from dwave.system.composites import EmbeddingComposite
from braket.ocean_plugin import BraketDWaveSampler
from datetime import datetime as dt
import pandas as pd
import dimod
from math import log2, floor
from circuit import circuitry

from braket.aws import AwsDevice


# notebook specific config
dwave_qpu = 'Advantage_system1'
notebook_start_time = time.time()
#AWS specific config
# Please enter the S3 bucket you created during onboarding in the code below
class connection:
    def get_bucket(bucket=None, prefix=None):
        if bucket == None:
            bucket = None
        if prefix == None:
            my_prefix = "results" # the name of the folder in the bucket
        s3_folder = (bucket, prefix)
        return s3_folder
class device:
    def get_qpu_arn(vendor=None, device=None):
        status = 1
        if vendor == None:
            print('Warning: No quantum vendor specified')
            status = 0
        if device == None:
            print('Warning: No quantum device specified')
            status = 0
        arn = 'arn:aws:braket:::device/qpu/' + vendor + device
        return arn, status
    def get_sim_arn(vendor='amazon', device='sv1'):
        arn = 'arn:aws:braket:::device/quantum-simulator/' + vendor + device
        return arn
    def get_device(arn=get_sim_arn):
        device = AwsDevice(arn)
        return device
    def get_device_ops(device=qbitkit.braket.provider.device.get_device(),
                       print_result=False):
        device_operations = device.properties.dict()['action']['braket.ir.jaqcd.program']['supportedOperations']
        if print_result == True:
            print('Quantum Gates supported by {}:\n {}'.format(device_name,
                                                               device_operations))
            return device_operations
        elif print_result == False:
            return device_operations
        else:
            return device_operations
class job():
    def get_job(circuit=circuitry.Circuit,
                s3loc=connection.get_bucket(),
                shots=1000, qubit_reqiring=False):
        my_task = device.run(circuit, s3loc, shots=shots, disable_qubit_rewiring=True)
        return my_task