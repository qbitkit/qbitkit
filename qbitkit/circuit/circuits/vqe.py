from qbitkit.io import frame as __f__
import numpy as __np__


class UCCSD:
    def ansatz(a_theta=float(0.)):
        """Build a UCCSD ansatz circuit parametrized by a_theta per McArdle et al.

        Args:
            a_theta(float): A floating point describing the VQE parameter to be optimized.
        Returns:
            pandas.DataFrame: generated ansatz circuit as a Pandas DataFrame."""
        # Initialize Hartree fock state by using X (NOT) gates to set the state of qubits 1 and 2 to |1⟩
        hartree_fock = {'gate': ['x', 'x'],
                        'targetA': [0, 1]}

        # Initial rotation around the X-axis
        initial_rotation = {'gate': ['rx'],
                            'targetA': [0],
                            'angle': [__np__.pi / 2]}

        # Put qubits 2-4 in a superposition with equal probabilities of 1 and 0, or in bra ket notation: |ψ⟩
        initial_hadamard = {'gate': ['h', 'h', 'h'],
                            'targetA': [1, 2, 3]}

        # Entangle qubits 1-5 with a series of cascading Controlled NOT gates.
        initial_entangle = {'gate': ['cnot', 'cnot', 'cnot', 'cnot'],
                            'targetA': [0, 1, 2, 3],
                            'targetB': [1, 2, 3, 4]}

        # Rotate around the Z-axis according to the a_theta parameter.
        parametrized_rz = {'gate': ['rz'],
                           'targetA': [4],
                           'theta': [a_theta]}

        # Use a series of cascading Controlled NOT gates to take qubits out of a state of entanglement
        revert_entanglement = {'gate': ['cnot', 'cnot', 'cnot', 'cnot'],
                               'targetA': [3, 2, 1, 0],
                               'targetB': [4, 3, 2, 1]}

        # Use Hadamard gates to take qubits out of a state of superposition
        revert_superposition = {'gate': ['h', 'h', 'h'],
                                'targetA': [1, 2, 3]}

        # Revert initial rotaion on X-axis
        revert_rotation = {'gate': ['rx'],
                           'targetA': [0],
                           'angle': [-__np__.pi/2]}

        # Put each piece of the circuit in a list we can iterate over
        pieces = [hartree_fock,
                  initial_rotation,
                  initial_hadamard,
                  initial_entangle,
                  parametrized_rz,
                  revert_entanglement,
                  revert_superposition,
                  revert_rotation]
        # Iterate over list of DataFrames to assemble the circuit
        generated_ansatz = __f__.Frame.get_frame()
        for piece in pieces:
            piece_frame = __f__.Frame.get_frame(piece)
            generated_ansatz = generated_ansatz.append(piece_frame)
        # Return the generated Ansatz
        return generated_ansatz
