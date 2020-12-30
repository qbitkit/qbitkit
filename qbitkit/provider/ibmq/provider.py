# Importing standard Qiskit libraries
from qiskit import execute, IBMQ
from qiskit.providers.ibmq import *
from qiskit.providers import aer as a
from qiskit.providers import basicaer as ba
from qiskit.visualization import *


# Loading your IBM Q account(s)
class quantum_device:
    def get_device(self):
        """Create an IBMQ provider with Qiskit to be used as a device in qbitkit"""
        provider = IBMQ.get_account()
        return provider
class local:
    def aer(simulator='qasm_simulator'):
        """Create an Aer simulator from Qiskit."""
        a.get_backend(simulator)
    def basic_aer(simulator='qasm_simulator'):
        """Create a Basic Aer simulator from Qiskit."""
        ba.get_backend(simulator)
    def sim(simulator='qasm_simulator',
            backend='basic_aer'):
        """Create an IBMQ Simulator.

        Keyword arguments:
        simulator -- the type of simulator to use (default 'qasm_simulator')
        backend -- the backend to use. can be 'aer' or 'basic_aer'. (default 'basic_aer')"""
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

        Keyword arguments:
        circuit -- the circuit to run on the QPU. (default None)
        backend -- the backend to use. (default None)
        shots -- the number of shots or 'reads' to take when executing on QPU. (default 8192)"""
        IBMQ.load_account()
        provider = IBMQ.get_provider(hub='ibm-q')
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

        Keyword arguments:
        circuit -- the circuit to be run on the QPU. (default None)
        job -- the job object to run on the QPU. (default None)
        show_graph -- whether or not to show a graph of the measurement probabilities. (default False)"""
        result = job.result()
        if show_graph == False:
            return result
        elif show_graph == True:
            meas_result = result
            plot_histogram(meas_result)
            return result
        else:
            return result