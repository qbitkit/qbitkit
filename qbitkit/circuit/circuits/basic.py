from qbitkit.io import frame as __f__
from qbitkit.io import list as __l__


def bell(append=None):
    """Make a 2-qubit Bell State Circuit using 1 Hadamard gate and 1 Controlled NOT gate.

    Args:
        append(pandas.DataFrame): an existing Pandas DataFrame to append the Bell State Circuit to. (default None)
    Returns:
        pandas.DataFrame: Pandas DataFrame containing the Bell State Circuit, or a DataFrame you specified with the Bell State Circuit appended to it."""
    bellFrame = __f__.Frame.get_frame(data={'gate': ['h', 'cnot'],
                                            'targetA': [0, 0],
                                            'targetB': [None, 1], })
    if append is None:
        return bellFrame
    elif append is not None:
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
    ghzFrame = __f__.Frame.get_frame(data={'gate': ['h', 'cnot', 'cnot'],
                                           'targetA': [0, 1, 2],
                                           'targetB': [None, 1, 2],
                                           'targetC': [None, None, None]})
    if append is None:
        return ghzFrame
    elif append is not None:
        ghzFrameAppended = append.append(ghzFrame)
        return ghzFrameAppended
    else:
        ghzFrameAppended = append.append(ghzFrame)
        return ghzFrameAppended

    def qrng(bits=int(5)):
        """Generate a simple quantum random number generator circuit.

        Args:
            bits(int): Number of qubits to use in generated circuit. (default int(5))
        Returns:
            pandas.DataFrame: DataFrame containing generated QRNG circuit."""
        if type(bits) != type(int(1)):
            bits = 5

        gate_spec = __l__.fill_range('h', bits)
        tgtA_spec = __l__.count_range(start=0,
                                      end=bits)

        rngdict = {'gate': gate_spec,
                   'targetA': tgtA_spec}
        rngframe = __f__.Frame.get_frame(data=rngdict)
        return rngframe
