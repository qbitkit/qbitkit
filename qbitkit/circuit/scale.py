from qbitkit.io import frame as f

def circuit(circuit=None,
            iterations=1,
            provider=None):
    """Scale a circuit by appending a given circuit to itself for a specified number of times.

    Args:
        circuit(provider_specific_quantum_circuit): input circuit to scale up. (default None)
        iterations(int): number of times to append the circuit onto itself. (default 1)
        provider(qbitkit_provider): specify a provider from qbitkit to use when appending gates
    Returns:
        provider_specific_quantum_circuit: scaled up provider-specific quantum circuit"""
    for x in range(iterations):
        circuit = provider.circuit.scale.append(circuit)
    return circuit