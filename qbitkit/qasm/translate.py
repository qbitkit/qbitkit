from qbitkit.qasm import generate as __gen__
from qbitkit.io.frame import Frame as __fr__
from os import linesep as __sep__


def from_frame(df=__fr__.get_frame(),
               qreg=5,
               creg=5,
               fill_nan=True,
               fill_nan_value=int(-1)):
    """Converts a Circuit DataFrame into a QASM string by iterating over the DataFrame and turning each row of the dataframe into a gate or set of gates.

    Args:
        df (pandas.DataFrame): specify a Circuit DataFrame to convert to a QASM string. (default fr.get_frame())
        qreg(int): Positive integer describing number of Qubits to use in the circuit, AKA the number of Quantum Registers. (default 5)
        creg(int): Positive integer describing number of classical registers to use in the circuit (default 5)            fill_nan (bool): whether or not to replace NaN values with a specified value. (default True)
        fill_nan_value (int): a value to replace NaN values with. (default int(-1))
    Returns:
        str: QASM string translated from specified DataFrame"""

    if fill_nan is True:
        df = __fr__.fill_nan(df,
                         fill_nan_value)
    circuit = str("")
    for index, row in df.iterrows():
        qcgates = str(row['gate'])
        targetA = row['targetA']
        if 'targetB' in df.columns:
            targetB = row['targetB']
        else:
            targetB = None

        if 'targetC' in df.columns:
            targetC = row['targetC']
        else:
            targetC = None

        if 'angle' in df.columns:
            angle = row['angle']
        else:
            angle = None

        if 'phi' in df.columns:
            phi = row['phi']
        else:
            phi = None

        if 'theta' in df.columns:
            theta = row['theta']
        else:
            theta = None

        if 'params' in df.columns:
            params = row['params']
        else:
            params = None

        if qcgates == 'cnot':
            qcgates = 'cx'
        elif qcgates == 'ccnot':
            qcgates = 'ccx'
        else:
            qcgates = qcgates

        if qcgates == 'if':
            qasmstr = __gen__.if_statement(creg_name=targetA,
                                           operator=targetB,
                                           creg_val=targetC)
        elif qcgates == 'm':
            qasmstr = __gen__.measurement(creg=targetB,
                                          qreg=targetA)
        elif params is not None:
            qasmstr = __gen__.gate(targetA=targetA,
                                   targetB=targetB,
                                   targetC=targetC,
                                   custom_name=qcgates,
                                   custom_params=params)
        else:
            qasmstr = __gen__.gate(qcgates,
                                   targetA=targetA,
                                   targetB=targetB,
                                   targetC=targetC,)

        circuit = circuit + __sep__ + qasmstr
    s = __sep__ + __sep__
    full_circuit = f"{__gen__.headers()}{s}{__gen__.registers(c=creg, q=qreg)}{s}{circuit}"
    return full_circuit
