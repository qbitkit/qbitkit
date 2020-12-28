from qbitkit.provider.braket.circuit import circuitry
from braket.aws import AwsDevice
from braket.devices import local_simulator as localsim
import boto3

class connection:
    def default_bucket(folder='results'):
        aws_account_id = boto3.client("sts").get_caller_identity()["Account"]
        s3_folder = (f"amazon-braket-{aws_account_id}",
                     "results")
        return s3_folder
    def get_bucket(bucket=None,
                   prefix=None):
        if prefix == None:
            my_prefix = "results"
        if bucket == None:
            bucket = connection.default_bucket(folder=my_prefix)
        s3 = (bucket,
                     prefix)
        return s3

class local:
    def sim(self):
        device = localsim("default")
        return device

class device:
    def get_qpu_arn(vendor=None,
                    device=None):
        status = 1
        if vendor == None:
            print('Warning: No quantum vendor specified')
            status = 0
        if device == None:
            print('Warning: No quantum device specified')
            status = 0
        arn = 'arn:aws:braket:::device/qpu/' + vendor + '/' + device
        return arn, status
    def get_sim_arn(vendor='amazon', device='sv1'):
        arn = 'arn:aws:braket:::device/quantum-simulator/' + vendor + '/' + device
        return arn
    def get_device(arn=get_sim_arn):
        device = AwsDevice(arn)
        return device
    def get_device_ops(device=None,
                       print_result=False):
        device_operations = device.properties.dict()['action']['braket.ir.jaqcd.program']['supportedOperations']
        if print_result == True:
            print('Quantum Gates supported by {}:\n {}'.format(device,
                                                               device_operations))
            return device_operations
        elif print_result == False:
            return device_operations
        else:
            return device_operations
class job:
    def get_job(device=device.get_device(arn=device.get_sim_arn(vendor='amazon',
                                          device='sv1')),
                circuit=circuitry.braket_circuit(),
                s3loc=connection.get_bucket(),
                shots=1000,
                disable_qubit_rewiring=False):
        my_task = device.run(circuit,
                             s3loc,
                             shots=shots,
                             disable_qubit_rewiring=disable_qubit_rewiring)
        return my_task