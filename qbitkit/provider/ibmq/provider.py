# Importing standard Qiskit libraries
from qiskit import execute, IBMQ
from qiskit.providers.ibmq import *
from qiskit.providers import aer as a
from qiskit.providers import basicaer as ba
from qiskit.visualization import *


# Loading your IBM Q account(s)
class quantum_device:
    def get_device(self):
        provider = IBMQ.get_account()
        return provider
class local:
    def aer(simulator='qasm_simulator'):
        a.get_backend(simulator)
    def basic_aer(simulator='qasm_simulator'):
        ba.get_backend(simulator)
    def sim(simulator='qasm_simulator',
            backend='basic_aer'):
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
        result = job.result()
        if show_graph == False:
            return result
        elif show_graph == True:
            meas_result = result
            plot_histogram(meas_result)
            return result
        else:
            return result