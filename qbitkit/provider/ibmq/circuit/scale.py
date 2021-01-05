def circuit(circuit=None):
    """Appends a circuit to itself.
    Args:
        circuit(braket.circuits.Circuit): a Qiskit circuit to append to itself.
    Returns:
        qiskit.QuantumCircuit: a scaled-up Qiskit QuantumCircuit."""
    circuit = circuit.append(circuit)
    return circuit