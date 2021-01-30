# Importing standard Qiskit libraries
from qiskit import execute
from qiskit import QuantumCircuit
from qiskit.providers.ibmq import IBMQ, least_busy
from qiskit.providers import aer as a
from qiskit.providers import basicaer as ba
from qiskit.visualization import plot_histogram
from qbitkit.error import error as qbitkit_error


def get_support_status():
    ibmq_support_status = 'experimental'
    resource_name = 'IBM Quantum Experience'

    additional_notes = f'For more information on forthcoming {resource_name} support, \
    see https://github.com/brianlechthaler/qbitkit/issues/2'
    qbitkit_error.Errors.support_status(feature_state=ibmq_support_status,
                                        resource_name=resource_name,
                                        additional_notes=additional_notes)
    return ibmq_support_status


get_support_status()

# Loading your IBM Q account(s)


class Connection:
    def get_provider(hub='ibm-q'):
        """Create an IBMQ provider with Qiskit to be used as a device in qbitkit

        Args:
            hub (str): The hub to pick IBM Q machines from. (default 'ibm-q')
        Returns:
            qiskit.providers.BaseProvider: the IBMQ provider"""
        provider = IBMQ.get_account(hub)
        return provider


class Local:
    def aer(simulator='qasm_simulator'):
        """Create an Aer simulator from Qiskit.

        Args:
            simulator(str): Name of the simulator to use (default 'qasm_simulator')
        Returns:
            qiskit.providers.BaseBackend: the Aer simulator from Qiskit"""
        a.get_backend(simulator)

    def basic_aer(simulator='qasm_simulator'):
        """Create a Basic Aer simulator from Qiskit.

        Args:
            simulator(str): Name of the simulator to use (default 'qasm_simulator')
        Returns:
            qiskit.providers.BaseBackend: the BasicAer simulator from Qiskit"""
        ba.get_backend(simulator)
    def sim(simulator='qasm_simulator',
            backend='basic_aer'):
        """Create an IBMQ Simulator.

        Args:
            simulator (str): the type of simulator to use (default 'qasm_simulator')
            backend (str): the backend to use. can be 'aer' or 'basic_aer'. (default 'basic_aer')
        Returns:
            qiskit.providers.BaseBackend: the simulator you chose"""
        if backend == 'basic_aer':
            device = Local.basic_aer(simulator=simulator)
            return device
        elif backend == 'aer':
            device = Local.aer(simulator=simulator)
            return device
        else:
            print(f"ERROR: Backend {backend} not found. Not returning anything.")
            device = None
            return device


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
        IBMQ.load_account()
        provider = IBMQ.get_provider(hub='ibm-q')
        filters = lambda b: b.configuration().n_qubits >= 3 and \
            not b.configuration().simulator and b.status().operational is True

        if qasm != str(""):
            circuit = QuantumCircuit.from_qasm_str(qasm)

        if backend is None:
            backend = least_busy(provider.backends(filters=filters))
        job = execute(circuit,
                      backend,
                      shots)
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
        result = job.result()
        if show_graph is False:
            return result
        elif show_graph is True:
            meas_result = result
            plot_histogram(meas_result)
            return result
        else:
            return result
