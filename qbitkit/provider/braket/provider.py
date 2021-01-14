from qbitkit.provider.braket.circuit import circuitry
from braket.aws import AwsDevice
from braket.devices import local_simulator as localsim
import boto3

class connection:
    def default_bucket(folder='results'):
        """Get the default AWS S3 Bucket using boto3.

        Warning: This function is experimental and may cause unexpected errors or not even be functional. Use with caution.

        Args:
            folder (str): folder within S3 bucket to save results to and read results from (default 'results')
        Returns:
            str: S3 bucket for communicating with Braket"""
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

        Args:
            bucket (str): name of the AWS S3 bucket you want to save/read results with (default None)
            prefix (str): name of the folder inside the bucket to save/read results with(default None)
            default_bucket (str): try to use the default bucket. Experimental feature, don't switch to True unless you're ok with things being likely to break and know what you're doing. (default False)
        Returns:
            str: S3 bucket for communicating with Braket"""
        if prefix == None:
            prefix = "results"
        if default_bucket == True:
            bucket = connection.default_bucket(folder=prefix)
        s3 = (bucket,
              prefix)
        return s3

class local:
    def sim(self):
        """Create a local simulator for AWS braket and return it.

        Args:
            self(None): An unused argument.
        Returns:
            braket.devices.localsim: the local simulator device for Braket"""
        device = localsim
        return device

class quantum_device:
    def get_qpu_arn(vendor='ionq',
                    device='ionQdevice'):
        """Get ARN for a QPU based on specified vendor and device and return the ARN.

        Args:
            vendor (str) the vendor you would like to choose a QPU from. (default 'ionq')
            device (str) the device you would like to choose as your QPU (default 'ionQdevice')
        Returns:
            str: selected QPU ARN"""
        if vendor == None:
            print('Warning: No quantum vendor specified')
        if device == None:
            print('Warning: No quantum device specified')
        arn = 'arn:aws:braket:::device/qpu/' + vendor + '/' + device
        return arn
    def get_sim_arn(vendor='amazon',
                    device='sv1'):
        """Get ARN for a simulator from the specified vendor and device and return it.

        Args:
            vendor (str) the name of the vendor from which you wish to choose a simulator from (default 'amazon')
            device (str) the name of the simulator you wish to use as your (simulated) QPU (default 'sv1')
        Returns:
            str: ARN of selected simulator."""
        arn = 'arn:aws:braket:::device/quantum-simulator/' + vendor + '/' + device
        return arn
    def get_device(arn=get_sim_arn()):
        """Get device from specified ARN and return it as an AwsDevice().

        Args:
            arn (str) the ARN of the device you would like to use (default get_sim_arn())
        Returns:
            braket.aws.AwsDevice: AWS Quantum Device from specified ARN
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

        Args:
            device (str): the AwsDevice() of the QPU or simulated QPU of your choice. (default device.get_device(arn=device.get_sim_arn()))
            circuit (braket.circuits.Circuit): the braket_circuit() of the translated circuit you wish to run on the QPU or simulated QPU. (default braket_circuit())
            shots (int): the number of shots, or reads that will be taken while executing the job on the QPU or simulated QPU (default 1000)
            s3loc (str): the bucket and result folder you wish to save/read results with (default connection.get_bucket())
            disable_qubit_rewiring (bool): whether or not to disable qubit rewiring. You probably will not need to worry about using this argument in most cases. (default False)
        Returns:
            braket.aws.AwsQuantumTask"""
        my_task = device.run(circuit,
                             s3loc,
                             shots=shots,
                             disable_qubit_rewiring=disable_qubit_rewiring)
        return my_task
class annealing:
    def get_sampler(sampler=None,
                    bucket=None,
                    dwave_qpu="Advantage_system1"):
        """Create a new D-Wave Sampler for Braket based on a specified D-Wave QPU.

        Args:
            sampler(braket.ocean_plugin.BraketDWaveSampler): a D-Wave Sampler from the Braket Ocean SDK plugin.
            bucket (str): the s3 bucket you wish to use for communication with the D-Wave QPU
            dwave_qpu (str): the D-Wave QPU model you wish to use for Quantum Annealing (default 'Advantage_system1')"""
        new_sampler = sampler(s3_destination_folder=bucket,
                              arn=f"arn:aws:braket:::device/qpu/d-wave/{dwave_qpu}")
        return new_sampler