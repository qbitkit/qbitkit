from qbitkit.io import frame as __f__


def circuit(circuit=None,
            iterations=1,
            provider=None):
    """Scale a circuit by appending a given circuit to itself for a specified number of times.

    Args:
        circuit(provider_specific_quantum_circuit): input circuit to scale up. (default None)
        iterations(int): number of times to append the circuit onto itself. (default 1)
        provider(qbitkit_provider): specify a provider from qbitkit to use when appending gates (default None)
    Returns:
        provider_specific_quantum_circuit: scaled up provider-specific quantum circuit"""
    # Iterate once for every item in the range.
    for x in range(iterations):
        # Append circuit to itself.
        circuit = provider.circuit.scale.append(circuit)
    # Return scaled-up circuit.
    return circuit


def frame(frame=__f__.Frame.get_frame(),
          iterations=1):
    """Scale a circuit Pandas DataFrame by appending a given Pandas DataFrame to iteself for a specified number of iterations

    Args:
        frame(pandas.DataFrame): the Pandas DataFrame to append to itself. (default qbitkit.io.frame.frame.get_frame())
        iterations(int): the number of times to append the Pandas DataFrame to itself. (default 1)
    Returns:
        pandas.DataFrame: scaled up Pandas DataFrame"""
    # Create a range based on the number of iterations, so we can iterate a set number of times.
    if type(iterations) == type(int(1)):
        iteration_range = range(int(iterations))
    else:
        iteration_range = [0]

    # Iterate once for every item in the range.
    for x in iteration_range:
        # Append the DataFrame to itself.
        frame = frame.append(frame)
    # Return the scaled-up DataFrame.
    return frame
