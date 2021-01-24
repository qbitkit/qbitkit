from braket.circuits import Circuit as __braket_circuit__
from braket.circuits import Gate as __braket_gate__
from qbitkit.io.frame import Frame as __fr__
import numpy as __np__
import string as __str__


class Info:
    def get_gates(self=None): # Parameter `self` does nothing.
        """Return all usable gates from the Braket SDK. Takes no keyword arguments.

        Args:
            self(None): Unused parameter, has no effect.
        Returns:
            list: a list of all quantum logic gates in the Braket Python SDK."""
        # Get a list of all the gates by using a Comprehension to extract values from the SDK.
        gate_set = [attr for attr in dir(__braket_gate__) if attr[0] in __str__.ascii_uppercase]
        # Return the list of gates
        return gate_set


class Translate:
    def translate_gate(op='h', # The Name of the gate to translate. Default is 'h' for Hadamard.
                       input_circuit=__braket_circuit__(), # Input circuit to append generated circuit to.
                       targetA=0, # First qubit target, required.
                       targetB=1, # Second target qubit, required for 2 or 3 qubit gates.
                       targetC=2, # Third target qubit, required for 3 qubit gates.
                       angle=0.15, # An angle to set for the gate, if the gate supports such a setting.
                       phi=0.15, # A phi value to set for the gate, if the gate supports such a setting.
                       theta=0.15, # A theta value to set for the gate, if the gate supports such a setting.
                       unitary_matrix=__np__.array([[0, 1], # A numpy matrix to use for the gate,
                                                    [1,0]]),# # if the gate supports such a setting.
                       unitary_targets=[0] # Targets to use for the unitary gate.
                       ):
        """Translate individual circuit elements from a Circuit DataFrame into a Braket Circuit, returns a Braket Circuit.

        Args:
            op (str): The instruction to translate into a gate. Default is a Hadamard gate represented as 'h'. (default 'h')
            input_circuit (braket.circuits.Circuit): specify a circuit to append the translated circuit to. (default braket_circuit())
            targetA (int): specify the first target qubit. Can be a positive integer or an array for specifying multiple targets. (default 0)
            targetB (int): specify the second target qubit for a two-qubit or three-qubit gate. Can be a positive integer or an array for specifying multiple targets. (default 1)
            targetC (int): specify the third target qubit for a three-qubit gate. Can be a positive integer or an array for specifying multiple targets. (default 2)
            angle (float): specify the angle for a gate. (default 0.15)
            phi (float): specify the phi for a gate. (default 0.15)
            theta (float): specify the theta for a gate. (default 0.15)
            unitary_matrix (np.array): specify a NumPy array with values for the unitary matrix. (default np.array([[0,1],[1,0]]))
            unitary_targets (list): a list of targets for the unitary. (default [0])
        Returns:
            braket.circuits.Circuit: Quantum circuit for Braket with gate we translated appended to it"""
        # Unitary Gate
        if op == 'unitary':
            input_circuit = input_circuit.unitary(matrix=unitary_matrix,
                                                  targets=unitary_targets)
            return input_circuit
        # Hadamard Gate
        if op == 'h':
            input_circuit = input_circuit.h(targetA)
            return input_circuit
        # X Gate
        if op == 'x':
            input_circuit = input_circuit.x(targetA)
            return input_circuit
        # Y Gate
        if op == 'y':
            input_circuit = input_circuit.y(targetA)
            return input_circuit
        # Z Gate
        if op == 'z':
            input_circuit = input_circuit.z(targetA)
            return input_circuit
        # S Gate
        if op == 's':
            input_circuit = input_circuit.s(targetA)
            return input_circuit
        # T Gate
        if op == 't':
            input_circuit = input_circuit.t(targetA)
            return input_circuit
        # Square Root Gate
        if op == 'v':
            input_circuit = input_circuit.v(targetA)
            return input_circuit
        # Square Root (inverted)
        if op == 'vi':
            input_circuit = input_circuit.vi(targetA)
            return input_circuit
        # S (inverted)
        if op == 'si':
            input_circuit = input_circuit.si(targetA)
            return input_circuit
        # T (inverted)
        if op == 'ti':
            input_circuit = input_circuit.ti(targetA)
            return input_circuit
        # XX Gate
        if op == 'xx':
            input_circuit = input_circuit.xx(targetA,
                                             targetB,
                                             theta)
            return input_circuit
        # XY Gate
        if op == 'xy':
            input_circuit = input_circuit.xx(targetA,
                                             targetB,
                                             theta)
            return input_circuit
        # YY Gate
        if op == 'yy':
            input_circuit = input_circuit.yy(targetA,
                                             targetB,
                                             theta)
            return input_circuit
        # ZZ Gate
        if op == 'zz':
            input_circuit = input_circuit.zz(targetA,
                                             targetB,
                                             theta)
            return input_circuit
        # Identity SWAP Gate
        if op == 'iswap':
            input_circuit = input_circuit.iswap(targetA,
                                                targetB)
            return input_circuit
        # Phase Shift Gate
        if op == 'phaseshift':
            input_circuit = input_circuit.phaseshift(targetA,
                                                     phi)
            return input_circuit
        # Controlled Y
        if op == 'cy':
            input_circuit = input_circuit.cy(targetA,
                                             targetB)
            return input_circuit
        # Controlled Z
        if op == 'cz':
            input_circuit = input_circuit.cz(targetA,
                                             targetB)
            return input_circuit
        # Identity
        if op == 'i':
            input_circuit = input_circuit.i(targetA)
            return input_circuit
        # Rotate around X axis
        if op == 'rx':
            input_circuit = input_circuit.rx(targetA,
                                             angle)
            return input_circuit
        # Rotate around Y axis
        if op == 'ry':
            input_circuit = input_circuit.ry(targetA,
                                             angle)
            return input_circuit
        # Rotate around Z axis
        if op == 'rz':
            input_circuit = input_circuit.rz(targetA,
                                             angle)
            return input_circuit
        # SWAP Gate
        if op == 'swap':
            input_circuit = input_circuit.swap(targetA,
                                               targetB)
            return input_circuit
        # Controlled NOT
        if op == 'cnot':
            input_circuit = input_circuit.cnot(targetA,
                                               targetB)
            return input_circuit
        # Double Controlled NOT (aka Toffoli Gate)
        if op == 'ccnot':
            input_circuit = input_circuit.ccnot(targetA,
                                                targetB,
                                                targetC)
            return input_circuit
        # Controlled Phase Shift Gate
        if op == 'cphaseshift':
            input_circuit = input_circuit.cphaseshift(targetA,
                                                      targetB,
                                                      angle)
            return input_circuit
        # Controlled Phase Shift Gate that phases the |00> state
        if op == 'cphaseshift00':
            input_circuit = input_circuit.cphaseshift00(targetA,
                                                        targetB,
                                                        angle)
            return input_circuit
        # Controlled Phase Shift Gate that phases the |01> state
        if op == 'cphaseshift01':
            input_circuit = input_circuit.cphaseshift01(targetA,
                                                        targetB,
                                                        angle)
            return input_circuit
        # Controlled Phase Shift Gate that phases the |10> state
        if op == 'cphaseshift10':
            input_circuit = input_circuit.cphaseshift10(targetA,
                                                        targetB,
                                                        angle)
            return input_circuit
        # Controlled SWAP (aka Fredkin Gate)
        if op == 'cswap':
            input_circuit = input_circuit.cswap(targetA,
                                                targetB,
                                                targetC)
            return input_circuit
        # Parametrized SWAP Gate
        if op == 'pswap':
            input_circuit = input_circuit.pswap(targetA,
                                                targetB,
                                                phi)
            return input_circuit
        # Print an error in case something goes wrong.
        else:
            print(f"[ERROR]: Gate {op} not found. Returning an empty object with a value of None.")
            # Return a None if we can't translate the gate.
            input_circuit = None
            return input_circuit
    def df_circuit(df=__fr__.get_frame(), # Specify a DataFrame to translate.
                   input_circuit=__braket_circuit__(), # Specify a circuit to append translated circuit to.
                   fill_nan=True, # Fill NaN values in DataFrame if True.
                   fill_nan_value=int(-1)): # If fill_nan=True, fill NaN values in the dataframe with this value.
        """Converts a Circuit DataFrame into a Braket Circuit by iterating over the DataFrame and turning each row of the dataframe into a gate or set of gates.

        Args:
            df (pandas.DataFrame): specify a Circuit DataFrame to convert to a Braket Circuit. (default fr.get_frame())
            input_circuit (braket.circuits.Circuit): specify a circuit to append the translated circuit's contents to. (default braket_circuit())
            fill_nan (bool): whether or not to replace NaN values with a specified value. (default True)
            fill_nan_value (int): a value to replace NaN values with. (default int(-1))
        Returns:
            braket.circuits.Circuit: Braket Circuit translated from specified DataFrame"""

        # Replace NaN/None values in the DataFrame. This prevents errors when iterating over the DataFrame.
        if fill_nan is True:
            df = __fr__.fill_nan(
                                 df, # the dataframe to operate on
                                 fill_nan_value) # the value to replace NaN values with.

        # Iterate over each row in the DataFrame, so we can process each line one-by-one.
        for index, row in df.iterrows():
            # Extract the name of the gate in the row and store it in a variable `qcgates`.
            qcgates = str(row['gate'])
            # Extract first qubit target in the row, store it in `targetA`.
            # # This is a required fieldm so we will skip checking if it exists.
            targetA = row['targetA']

            # Check if the second qubit target is specified...
            if 'targetB' in df.columns:
                # ... if it is, store it's value in targetB...
                targetB = row['targetB']
            else:
                # ... otherwise just set targetB to None.
                targetB = None

            # Check if the third qubit target is specified...
            if 'targetC' in df.columns:
                # ... if it is, store it's value in targetC...
                targetC = row['targetC']
            else:
                # ... otherwise just set targetC to None.
                targetC = None

            # Check if the gate's angle parameter is set...
            if 'angle' in df.columns:
                # ... if it is, store it's value in angle...
                angle = row['angle']
            else:
                # ... otherwise just set angle to None.
                angle = None

            # Check if the gate's phi parameter is set...
            if 'phi' in df.columns:
                # ... if it is, store it's value in phi...
                phi = row['phi']
            else:
                # ... otherwise just set phi to None.
                phi = None

            # Check if the gate's theta parameter is specified...
            if 'theta' in df.columns:
                # ... if it is, store it's value in theta...
                theta = row['theta']
            else:
                # ... otherwise just set theta to None.
                theta = None

            # Translate this row's values we just extracted into a quantum circuit
            # # This also appends the circuit to the previous iteration(s) if there's >1 rows in the DataFrame.
            circuit = Translate.translate_gate(input_circuit=input_circuit,
                                               op=qcgates,
                                               targetA=targetA,
                                               targetB=targetB,
                                               targetC=targetC,
                                               angle=angle,
                                               phi=phi,
                                               theta=theta)
        # Finally, return the completed circuit. Not too complex, eh?
        return circuit
