class Braket:
    class GateModel:
        def doc(job=None):
            """Create a dictionary object containing information from the results of a Braket task, then return it.

            Args:
                job (braket.tasks.quantum_task.QuantumTask): a job object returned from running a Braket task. (default None)
            Returns:
                dict: returns a dict containing measurement probabilities, measurement counts, measured qubits, and task metadata."""
            # Extract Counts of Each Bit Measured.
            meas_counts = job.result().measurement_counts
            # Extract Measured Qubits.
            meas_qubits = job.result().measured_qubits
            # Extract Task Metadata.
            metadata = job.metadata()
            # Create Elasticsearch document using the 3 things we just collected.
            doc = {
                'measurement_counts': meas_counts,
                'measured_qubits': meas_qubits,
                'metadata': metadata,
            }
            # Return the generated Elasticsearch document.
            return doc
