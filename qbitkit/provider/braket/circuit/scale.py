def circuit(circuit=None):
    """Appends a circuit to itself.
    
    Args:
        circuit(braket.circuits.Circuit): a Braket circuit to append to itself. (default None)
    Returns:
        braket.circuits.Circuit: a scaled-up Braket circuit."""
    circuit = circuit.append(circuit)
    return circuit