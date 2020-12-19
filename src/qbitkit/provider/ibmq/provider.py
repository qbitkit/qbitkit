# Importing standard Qiskit libraries
from qiskit import execute, IBMQ
from qiskit.providers.ibmq import *
from qiskit.visualization import *


# Loading your IBM Q account(s)
class connect:
    def get_provider(self):
        provider = IBMQ.get_account()
        return provider
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