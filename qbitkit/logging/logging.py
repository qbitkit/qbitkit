from qbitkit.logging import elasticsearch as es
from datetime import datetime as dt
class braket:
    class gate_model:
        def doc(job=None):
            """Create a dictionary object containing information from the results of a Braket task, then return it.

            Args:
                job (braket.tasks.quantum_task.QuantumTask): a job object returned from running a Braket task.
            Returns:
                dict: returns a dict containing measurement probabilities, measurement counts, measured qubits, and task metadata."""
            meas_probabilities = job.result().measurement_probabilities
            meas_counts = job.result().measurement_counts
            meas_qubits = job.result().measured_qubits
            metadata = job.result().task_metadata
            doc = {
                'measurement_probabilities': meas_probabilities,
                'measurement_counts': meas_counts,
                'measured_qubits': meas_qubits,
                'metadata': metadata,
            }
            return doc