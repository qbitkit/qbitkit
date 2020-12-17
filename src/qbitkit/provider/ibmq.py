# Importing standard Qiskit libraries
from qiskit.tools.monitor import job_monitor
from qiskit.providers.ibmq import *
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from qiskit.extensions import Initialize
import numpy as np

# Loading your IBM Q account(s)
class ibmq_connect:
    def get_provider(self):
        provider = IBMQ.get_account()
        return provider
class ibmq_job:
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