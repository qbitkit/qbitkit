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
def frame(frame=f.frame.get_frame(),
          iterations=1):
    """Scale a circuit Pandas DataFrame by appending a given Pandas DataFrame to iteself for a specified number of iterations

    Args:
        frame(pandas.DataFrame): the Pandas DataFrame to append to itself.
        iterations(int): the number of times to append the Pandas DataFrame to itself.
    Returns:
        pd.DataFrame: scaled up Pandas DataFrame"""
    for x in range(iterations):
        frame = frame.append(frame)
    return frame