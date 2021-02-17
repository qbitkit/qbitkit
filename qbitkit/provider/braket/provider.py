from braket.aws import AwsDevice as __AWS_Device__
from braket.devices import LocalSimulator as __local_simulator__
from braket.ocean_plugin import BraketDWaveSampler as __bdwsamp__
from braket.ocean_plugin import BraketSampler as __bsamp__


class Connection:
    def get_bucket(bucket=None,
                   prefix=None):
        """Get bucket from specified keyword arguments.

        Args:
            bucket (str): name of the AWS S3 bucket you want to save/read results with (default None)
            prefix (str): name of the folder inside the bucket to save/read results with(default None)
        Returns:
            str: S3 bucket for communicating with Braket"""
        # Check if prefix is set to its default value.
        if prefix is None:
            # Set prefix value to "results".
            prefix = "results"
        # Create tuple from specified values.
        s3 = (bucket,
              prefix)
        # Return generated tuple.
        return s3


class Local:
    def sim(self):
        """Create a local simulator for AWS braket and return it.

        Args:
            self(None): An unused argument.
        Returns:
            braket.devices.local_simulator: the local simulator device for Braket"""
        # Create a local simulator.
        device = __local_simulator__
        # Return the local simulator.
        return device


class QuantumDevice:
    def get_qpu_arn(vendor='ionq',
                    device='ionQdevice'):
        """Get ARN for a QPU based on specified vendor and device and return the ARN.

        Args:
            vendor (str): the vendor you would like to choose a QPU from. (default 'ionq')
            device (str): the device you would like to choose as your QPU (default 'ionQdevice')
        Returns:
            str: selected QPU ARN"""
        # Check if vendor is set to its default value.
        if vendor is None:
            # Throw a warning about not having a vendor specified.
            print('Warning: No quantum vendor specified')
        # Check if device is set to its default value.
        if device is None:
            # Throw a warning about not having a vendor specified.
            print('Warning: No quantum device specified')
        # Build ARN.
        arn = 'arn:aws:braket:::device/qpu/' + vendor + '/' + device
        # Return generated ARN.
        return arn

    def get_sim_arn(vendor='amazon',
                    device='sv1'):
        """Get ARN for a simulator from the specified vendor and device and return it.

        Args:
            vendor (str): the name of the vendor from which you wish to choose a simulator from (default 'amazon')
            device (str): the name of the simulator you wish to use as your (simulated) QPU (default 'sv1')
        Returns:
            str: ARN of selected simulator."""
        # Build ARN from specified values.
        arn = 'arn:aws:braket:::device/quantum-simulator/' + vendor + '/' + device
        # Return ARN.
        return arn

    def get_device(arn=get_sim_arn()):
        """Get device from specified ARN and return it as an AwsDevice().

        Args:
            arn (str): the ARN of the device you would like to use (default get_sim_arn())
        Returns:
            braket.aws.AwsDevice: AWS Quantum Device from specified ARN."""
        # Get device from specified ARN.
        device = __AWS_Device__(arn)
        # Return new device.
        return device
    def get_device_ops(device=None,
                       print_result=False):
        # Get the device's properties dictionary, extract values we need.
        device_operations = device.properties.dict()['action']['braket.ir.jaqcd.program']['supportedOperations']
        # Check if print_result is enabled.
        if print_result is True:
            # Print the quantum gates.
            print('Quantum Gates supported by {}:\n {}'.format(device,
                                                               device_operations))
            # Return the quantum gates.
            return device_operations
        # Check if print_result is disabled.
        elif print_result is False:
            # Return the quantum gates.
            return device_operations
        # Check if any other value is speccified for print_result.
        else:
            # Return the quantum gates.
            return device_operations


class Job:
    def get_job(device=None,
                circuit=None,
                s3loc=None,
                shots=1000,
                disable_qubit_rewiring=False):
        """Create Job from specified keyword arguments.

        Args:
            device (str): the AwsDevice() of the QPU or simulated QPU of your choice. (default None)
            circuit (braket.circuits.Circuit): the braket_circuit() of the translated circuit you wish to run on the QPU or simulated QPU. (default None)
            shots (int): the number of shots, or reads that will be taken while executing the Job on the QPU or simulated QPU (default 1000)
            s3loc (str): the bucket and result folder you wish to save/read results with (default None)
            disable_qubit_rewiring (bool): whether or not to disable qubit rewiring. You probably will not need to worry about using this argument in most cases. (default False)
        Returns:
            braket.aws.AwsQuantumTask: an AWS quantum task object"""
        # Create a Quantum Task from the specified values.
        my_task = device.run(task_specification=circuit,
                             s3_destination_folder=s3loc,
                             shots=shots,
                             disable_qubit_rewiring=disable_qubit_rewiring)
        # Return the new Quantum Task.
        return my_task


class Annealing:
    def get_sampler(sampler_type='BraketDWaveSampler',
                    bucket=None,
                    dwave_qpu="Advantage_system1"):
        """Create a new D-Wave Sampler for Braket based on a specified D-Wave QPU.

        Args:
            sampler_type(str): a D-Wave Sampler from the Braket Ocean SDK plugin. (default 'BraketDWaveSampler')
            bucket (str): the s3 bucket you wish to use for communication with the D-Wave QPU (default None)
            dwave_qpu (str): the D-Wave QPU model you wish to use for Quantum Annealing (default 'Advantage_system1')
        Returns:
            braket.ocean_plugin.braket_dwave_sampler.BraketDWaveSampler: An AWS Braket D-Wave Ocean SDK Plugin Sampler"""
        # Check if specified sampler is the BraketDWaveSampler.
        if sampler_type == 'BraketDWaveSampler':
            sampler = __bdwsamp__
        # Check if specified sampler is the BraketSampler.
        elif sampler_type == 'BraketSampler':
            sampler = __bsamp__
        # Throw an error if something invalid was specified.
        else:
            # Assemble first part of message.
            first = str(f"[Error] Invalid Sampler Type Specified: {str(sampler_type)}.")
            # Assemble second part of message.
            last = str(f"Try specifying 'BraketDWaveSampler' or 'BraketSampler' instead. Default is BraketDWaveSampler")
            # Assemble final message.
            message = str(first) + str(last)
            # Print final message.
            print(message)
            # Return nothing.
            return None

        # Create a new D-Wave sampler based on the specified values.
        new_sampler = sampler(s3_destination_folder=bucket,
                              device_arn=f"arn:aws:braket:::device/qpu/d-wave/{dwave_qpu}")
        # Return the new D-Wave sampler.
        return new_sampler
