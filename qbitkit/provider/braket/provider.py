from qbitkit.provider.braket.circuit import circuitry
from braket.aws import AwsDevice
from braket.devices import local_simulator as localsim
import boto3

class connection:
    def default_bucket(folder='results'):
        """Get the default AWS S3 Bucket using boto3.

        Warning: This function is experimental and may cause unexpected errors or not even be functional. Use with caution.

        Keyword arguments:
        - folder -- folder within S3 bucket to save results to and read results from (default 'results')"""
        warning = 'WARNING: This function is experimental and may cause unexpected errors or not even be functional. Use with caution.'
        print(warning)
        aws_account_id = boto3.client("sts").get_caller_identity()["Account"]
        s3_folder = (f"amazon-braket-{aws_account_id}",
                     "results")
        return s3_folder
    def get_bucket(bucket=None,
                   prefix=None,
                   default_bucket=False):
        """Get bucket from specified keyword arguments.

        Keyword arguments:
        - bucket -- name of the AWS S3 bucket you want to save/read results with (default None)
        - results -- name of the folder inside the bucket to save/read results with(default None)
        - default_bucket -- try to use the default bucket. Experimental feature, don't switch to True unless you're ok with things being likely to break and know what you're doing. (default False)"""
        if prefix == None:
            prefix = "results"
        if default_bucket == True:
            bucket = connection.default_bucket(folder=prefix)
        s3 = (bucket,
              prefix)
        return s3

class local:
    def sim():
        """Create a local simulator for AWS braket and return it."""
        device = localsim
        return device

class quantum_device:
    def get_qpu_arn(vendor='ionq',
                    device='ionQdevice'):
        """Get ARN for a QPU based on specified vendor and device and return the ARN.

        Keyword arguments:
        - vendor -- the vendor you would like to choose a QPU from. (default 'ionq')
        - device -- the device you would like to choose as your QPU (default 'ionQdevice')"""
        if vendor == None:
            print('Warning: No quantum vendor specified')
        if device == None:
            print('Warning: No quantum device specified')
        arn = 'arn:aws:braket:::device/qpu/' + vendor + '/' + device
        return arn
    def get_sim_arn(vendor='amazon',
                    device='sv1'):
        """Get ARN for a simulator from the specified vendor and device and return it.

        Keyword arguments:
        - vendor -- the name of the vendor from which you wish to choose a simulator from (default 'amazon')
        - device -- the name of the simulator you wish to use as your (simulated) QPU (default 'sv1')"""
        arn = 'arn:aws:braket:::device/quantum-simulator/' + vendor + '/' + device
        return arn
    def get_device(arn=get_sim_arn()):
        """Get device from specified ARN and return it as an AwsDevice().

        Keyword arguments:
        - arn -- the ARN of the device you would like to use (default get_sim_arn())
        """
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
    def get_job(device=quantum_device.get_device(arn=quantum_device.get_sim_arn(vendor='amazon',
                                                                                device='sv1')),
                circuit=circuitry.braket_circuit(),
                s3loc=connection.get_bucket(),
                shots=1000,
                disable_qubit_rewiring=False):
        """Create job from specified keyword arguments.

        Keyword arguments:
        - device -- the AwsDevice() of the QPU or simulated QPU of your choice. (default device.get_device(arn=device.get_sim_arn()))
        - circuit -- the braket_circuit() of the translated circuit you wish to run on the QPU or simulated QPU. (default braket_circuit())
        - shots -- the number of shots, or reads that will be taken while executing the job on the QPU or simulated QPU (default 1000)
        - s3loc -- the bucket and result folder you wish to save/read results with (default connection.get_bucket())
        - disable_qubit_rewiring -- whether or not to disable qubit rewiring. You probably will not need to worry about using this argument in most cases. (default False)"""
        my_task = device.run(circuit,
                             s3loc,
                             shots=shots,
                             disable_qubit_rewiring=disable_qubit_rewiring)
        return my_task