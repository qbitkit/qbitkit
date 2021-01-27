from qbitkit.io.list import remove_value as __rmval__
from qbitkit.qasm import generate as __gen__
from qbitkit.io.frame import Frame as __fr__
from os import linesep as __sep__
from qbitkit.error.error import Error as __err__


def get_support_status():
    fileIO_support_status = 'experimental'
    __err__.support_status(feature_state=fileIO_support_status,
                           resource_name='QASM2 Generation')
    return fileIO_support_status


get_support_status()


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
    cleaned_targets = __rmval__(targets, None)
    qasm = __gen__.gate(op, cleaned_targets)
    return qasm


def from_frame(df=__fr__.get_frame(),
               qreg=5,
               creg=5,
               fill_nan=True,
               fill_nan_value=int(-1)):
        """Converts a Circuit DataFrame into a Braket Circuit by iterating over the DataFrame and turning each row of the dataframe into a gate or set of gates.

        Args:
            df (pandas.DataFrame): specify a Circuit DataFrame to convert to a Braket Circuit. (default fr.get_frame())
            qregs(int): Positive integer describing number of Qubits to use in the circuit, AKA the number of Quantum Registers. (default 5)
            cregs(int): Positive integer describing number of classical registers to use in the circuit (default 5)            fill_nan (bool): whether or not to replace NaN values with a specified value. (default True)
            fill_nan_value (int): a value to replace NaN values with. (default int(-1))
        Returns:
            braket.circuits.Circuit: Braket Circuit translated from specified DataFrame"""

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

            qasmstr = gate(op=qcgates,
                           targetA=targetA,
                           targetB=targetB,
                           targetC=targetC,)
            circuit = circuit + __sep__ + qasmstr
        s = __sep__ + __sep__
        full_circuit = f"{__gen__.headers()}{s}{__gen__.registers(c=creg, q=qreg)}{s}{circuit}"
        return full_circuit