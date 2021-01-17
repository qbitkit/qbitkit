# Importing standard Qiskit libraries
from qiskit import execute, IBMQ
from qiskit.providers.ibmq import *
from qiskit.providers import aer as a
from qiskit.providers import basicaer as ba
from qiskit.visualization import *
from qbitkit.error import error as qbitkit_error

def get_support_status():
    ibmq_support_status = 'experimental'
    resource_name = 'IBM Quantum Experience'
    qbitkit_error.errors.support_status(feature_state=ibmq_support_status,
                                        resource_name=resource_name,
                                        additional_notes=f'For more information on forthcoming {resource_name} support, see https://github.com/brianlechthaler/qbitkit/issues/2')
    return ibmq_support_status

get_support_status()

# Loading your IBM Q account(s)
class connection:
    def get_provider(hub='ibm-q'):
        """Create an IBMQ provider with Qiskit to be used as a device in qbitkit

        Args:
            hub (str): The hub to pick IBM Q machines from. (default 'ibm-q')
        Returns:
            qiskit.providers.BaseProvider: the IBMQ provider"""
        provider = IBMQ.get_account(hub)
        return provider
class local:
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
            device = local.basic_aer(simulator=simulator)
            return device
        elif backend == 'aer':
            device = local.aer(simulator=simulator)
            return device
        else:
            print(f"ERROR: Backend {backend} not found. Not returning anything.")
            device = None
            return device
class job:
    def get_job(circuit=None,
                backend=None,
                shots=8192):
        """Create a job with the least busy provider capable of fulfilling our request, then return the job object.

        Args:
            circuit (qiskit.providers.ibmq.job.IBMQ): the circuit to run on the QPU. (default None)
            backend (qiskit.providers.ibmq.IBMQBackend): the backend to use. (default None)
            shots (int): the number of shots or 'reads' to take when executing on QPU. (default 8192)"""
        IBMQ.load_account()
        provider = IBMQ.get_provider(hub='ibm-q')
        if backend == None:
            backend = least_busy(provider.backends(filters=lambda b: b.configuration().n_qubits >= 3 and
                                                                     not b.configuration().simulator and b.status().operational == True))
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
        if show_graph == False:
            return result
        elif show_graph == True:
            meas_result = result
            plot_histogram(meas_result)
            return result
        else:
            return result