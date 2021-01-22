from qbitkit.qasm import generate as __gen__
from qbitkit.io.frame import Frame as __fr__
from os import linesep as __sep__


def gate(op=None,
         targetA=None,
         targetB=None,
         targetC=None):
    """Translate a single gate to QASM.

    op(str): QASM2 gate to use.
    targetA(int): index of first target qubit to apply gate to. (default None)
    targetB(int): index of second target qubit to apply gate to for 2 and 3 qubit gates. (default None)
    targetB(int): index of the third target qubit to apply gate to for 3 qubit gates. (default None)"""
    targets = [targetA, targetB, targetC]
    print(targets)
    cleaned_targets = []
    for target in targets:
        if target is not None:
            cleaned_targets.append(target)
    qasm = __gen__.gate(op, cleaned_targets)
    return qasm


def from_frame(self=None,
               qregs=5,
               cregs=5,
               fill_nan=True,
               fill_nan_value=-1):
    """Convert a DataFrame to a QASM2 string.

    Args:
        self(pandas.DataFrame): a Pandas DataFrame to translate to QASM2.
        qregs(int): Positive integer describing number of Qubits to use in the circuit, AKA the number of Quantum Registers. (default 5)
        cregs(int): Positive integer describing number of classical registers to use in the circuit (default 5)
        fill_nan(bool): whether or not to replace NaN values with a specified value. (default True)
        fill_nan_value(int): a value to replace NaN values with if fill_nan is set to True. (default -1)
    Returns:
        str: Generated QASM2"""

    if fill_nan is True:
        df = __fr__.fill_nan(self,
                             fill_nan_value)

    gates = list()
    for index, row in self.iterrows():

        qcgates = row['gate']
        targetA = row['targetA']

        if 'targetB' in df.columns:
            targetB = row['targetB']
        else:
            targetB = None

        if 'targetC' in df.columns:
            targetC = row['targetC']
        else:
            targetC = None

        if qcgates == 'measure':
            dfgate = __gen__.measurement(qreg=targetA,
                                         creg=targetB)
        elif qcgates == 'cnot':
            dfgate = 'cx'
        elif qcgates == 'ccnot':
            dfgate = 'ccx'
        elif qcgates == 'i':
            dfgate = 'id'
        elif qcgates == 'si':
            dfgate = 'sdg'
        elif qcgates == 'ti':
            dfgate = 'tdg'
        else:
            dfgate = qcgates

        targetlist = list([targetA])

        if targetB != None:
            targetlist = targetlist.append(targetB)

        if targetC != None:
            targetlist = targetlist.append(targetC)

        qasmgate = __gen__.gate(dfgate, targetlist)

        gates = gates.append(qasmgate)

    formatted_gates=str(__sep__)
    for gate in gates:
        qasm_formatted_gate = __gen__.gate(gate)
        formatted_gates = f"{formatted_gates}{qasm_formatted_gate}{__sep__}"

    formatted_qasm = f"{__gen__.headers()}{__sep__}{formatted_gates}"

    return formatted_qasm
