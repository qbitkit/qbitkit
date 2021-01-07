def bell(iterations=1,
         append=None):
    """Make a 2-qubit Bell State Circuit using 1 Hadamard gate and 1 Controlled NOT gate.

    Args:
        iterations(int): number of times to repeat the circuit (default 1)
        append(pandas.DataFrame): an existing Pandas DataFrame to append the Bell State Circuit to."""