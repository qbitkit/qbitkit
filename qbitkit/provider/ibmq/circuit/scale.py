class Circuit:
    def append(circuit=None):
        """Appends a circuit to itself.
        Args:
            circuit(qiskit.QuantumCircuit): a Qiskit circuit to append to itself. (default None)
        Returns:
            qiskit.QuantumCircuit: a scaled-up Qiskit QuantumCircuit."""
        # Append given circuit to the right hand side of the given circuit
        circuit = circuit.extend(circuit)
        # Return Appended Circuit
        return circuit
