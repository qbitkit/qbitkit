from qbitkit.io import frame as f

def bell(append=None):
    """Make a 2-qubit Bell State Circuit using 1 Hadamard gate and 1 Controlled NOT gate.

    Args:
        append(pandas.DataFrame): an existing Pandas DataFrame to append the Bell State Circuit to. (default None)
    Returns:
        pandas.DataFrame: Pandas DataFrame containing the Bell State Circuit, or a DataFrame you specified with the Bell State Circuit appended to it."""
    bellFrame = f.Frame.get_frame(data={'gate': ['h', 'cnot'],
                                        'targetA': [0, 0],
                                        'targetB': [None, 1],})
    if append == None:
        return bellFrame
    elif append != None:
        bellFrameAppended = append.append(bellFrame)
        return bellFrameAppended
    else:
        bellFrameAppended = append.append(bellFrame)
        return bellFrameAppended
def ghz(append=None):
    """Make a 2-qubit Greenberger-Horne-Zeilinger (GHZ) State Circuit using 1 Hadamard gate and 2 Controlled NOT gates.

        Args:
            append(pandas.DataFrame): an existing Pandas DataFrame to append the GHZ State Circuit to. (default None)
        Returns:
            pandas.DataFrame: Pandas DataFrame containing the GHZ State Circuit, or a DataFrame you specified with the GHZ State Circuit appended to it."""
    ghzFrame = f.Frame.get_frame(data={'gate':['h', 'cnot', 'cnot'],
                                       'targetA':[0,1,2],
                                       'targetB':[None,1,2],
                                       'targetC':[None,None,None]})
    if append == None:
        return ghzFrame
    elif append != None:
        ghzFrameAppended = append.append(ghzFrame)
        return ghzFrameAppended
    else:
        ghzFrameAppended = append.append(ghzFrame)
        return ghzFrameAppended