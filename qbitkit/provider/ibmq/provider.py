from qiskit import execute as __execute__
from qiskit import QuantumCircuit as __QuantumCircuit__
from qiskit.providers.ibmq import IBMQ as __IBMQ__
from qiskit.providers.ibmq import least_busy as __least_busy__
from qiskit import Aer as __a__
from qiskit import BasicAer as __ba__
from qiskit.visualization import plot_histogram as __plot_histogram__


class Local:
    def aer(simulator='qasm_simulator'):
        """Create an Aer simulator from Qiskit.

        Args:
            simulator(str): Name of the simulator to use (default 'qasm_simulator')
        Returns:
            qiskit.providers.BaseBackend: the Aer simulator from Qiskit"""
        backend = None
        backend = __a__.get_backend(simulator)
        return backend

    def basic_aer(simulator='qasm_simulator'):
        """Create a Basic Aer simulator from Qiskit.

        Args:
            simulator(str): Name of the simulator to use (default 'qasm_simulator')
        Returns:
            qiskit.providers.BaseBackend: the BasicAer simulator from Qiskit"""
        # Initialize variables
        backend = None
        # Get backend
        backend = __ba__.get_backend(simulator)
        # Return backend
        return backend
    def sim(simulator='qasm_simulator',
            backend='basic_aer'):
        """Create an IBMQ Simulator.

        Args:
            simulator (str): the type of simulator to use (default 'qasm_simulator')
            backend (str): the backend to use. can be 'aer' or 'basic_aer'. (default 'basic_aer')
        Returns:
            qiskit.providers.BaseBackend: the simulator you chose"""
        # Check if requested simulator is basic_aer
        if backend == 'basic_aer':
            # Create a basic_aer simulator
            device = Local.basic_aer(simulator=simulator)
            # Return basic_aer simulator
            return device
        # Check if requested simulator is aer
        elif backend == 'aer':
            # Create an aer simulator
            device = Local.aer(simulator=simulator)
            # Return aer simulator
            return device
        # In any other case
        else:
            # Throw a soft error
            print(f"ERROR: Backend {backend} not found. Not returning anything.")
            # Set device variable to None
            device = None
            # Return None
            return device


class Remote:
    def get_provider(hub='ibm-q'):
        """Create an IBMQ provider with Qiskit to be used as a device in qbitkit

        Args:
            hub (str): The hub to pick IBM Q machines from. (default 'ibm-q')
        Returns:
            qiskit.providers.BaseProvider: the IBMQ provider"""
        # Create a provider object from specified hub name.
        provider = __IBMQ__.load_account(hub)
        # Return new provider object.
        return provider
    def auto_backend(provider=None,
                     qubits=3,
                     simulator=False):
        """Automatically select a simulator from a provider based on keyword parameters.

        Args:
            provider(qiskit.providers.ibmq.accountprovider.AccountProvider): Qiskit AccountProvider object. (default None)
            qubits(int): Minimum qubit count necessary for a device to be selected. (default 3)
            simulator(bool): If set to True, allows automatic selection of classically simulated quantum devices. (defeault False)
        Returns:
            qiskit.providers.ibmq.ibmqbackend.IBMQBackend: Qiskit IBMQBackend object."""
        # Check whether or not we should include simulators in our search.
        if simulator == False:
            # Get least busy device, only looking for hardware devices.
            filters = lambda b: b.configuration().n_qubits >= qubits and \
                                not b.configuration().simulator and \
                                b.status().operational is True
        else:
            # Get least busy device, including simulators in search for devices.
            filters = lambda b: b.configuration().n_qubits >= qubits and \
                                b.configuration().simulator and \
                                b.status().operational is True
        # Get backend.
        backend = __least_busy__(
            provider.backends(
                filters=filters))
        # Return backend.
        return backend


class Job:
    def get_job(circuit=None,
                qasm=str(""),
                backend=None,
                shots=8192):
        """Create a job with the least busy provider capable of fulfilling our request, then return the job object.

        Args:
            circuit (qiskit.providers.ibmq.job.IBMQ): the circuit to run on the QPU. (default None)
            qasm (str): A string containing valid QASM 2.0 to run. Specifying this overrides circuit. (default str(""))
            backend (qiskit.providers.ibmq.IBMQBackend): the backend to use. (default None)
            shots (int): the number of shots or 'reads' to take when executing on QPU. (default 8192)"""

        # Check if qasm parameter is not it's default value
        if qasm != str(""):
            # Create circuit from QASM
            circuit = __QuantumCircuit__.from_qasm_str(qasm)

        # Get the number of qubits used in the specified QuantumCircuit
        num_qubits = circuit.num_qubits

        # Check if backend is specified
        if backend is None:
            # Automatically pick the least busy backend
            backend = Remote.auto_backend(qubits=num_qubits)

        # Run QuantumCircuit
        job = __execute__(experiments=circuit,
                          backend=backend,
                          shots=shots)
        return job

    def run_job(circuit=None,
                job=None,
                show_graph=False):
        """Run a specified job and return the results from the QPU.

        Args:
            circuit (braket.circuits.Circuit): the circuit to be run on the QPU. (default None)
            job (qiskit.providers.ibmq.job.IBMQJob): the job object to run on the QPU. (default None)
            show_graph (bool): whether or not to show a graph of the measurement probabilities. (default False)
        Returns:
            dict: the results from running the job"""
        # Read result into variable result.
        result = job.result()
        # Check if we should not display a graph of probabilities
        if show_graph is False:
            # Just return result
            return result
        # Check if we should display a graph of probabilities
        elif show_graph is True:
            # Plot a Histogram from Results
            __plot_histogram__(result)
            # Return results
            return result
        # In any other case
        else:
            # Just return result
            return result
