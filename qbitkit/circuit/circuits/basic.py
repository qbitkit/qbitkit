from qbitkit.io import frame as f

def bell(append=None):
    """Make a 2-qubit Bell State Circuit using 1 Hadamard gate and 1 Controlled NOT gate.

    Args:
        append(pandas.DataFrame): an existing Pandas DataFrame to append the Bell State Circuit to.
    Returns:
        pandas.DataFrame: Pandas DataFrame containing the Bell State Circuit, or a DataFrame you specified with the Bell State Circuit appended to it."""
    bellFrame = f.get_frame(data={'gate': ['h', 'cnot'],
                                  'targetA': [0, 0],
                                  'targetB': [None, 1],
                                  'targetC': [None, None], })
    if append == None:
        return bellFrame
    elif append != None:
        bellFrameAppended = append.append(bellFrame)
        return bellFrameAppended
    else:
        bellFrameAppended = append.append(bellFrame)
        return bellFrameAppended