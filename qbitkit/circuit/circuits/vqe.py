from qbitkit.io import frame as __f__
import numpy as __np__


class UCCSD(self=float(0.)):
    """Create a UCCSD Ansatz.

    Args:
        self(float): Floating point describing the VQE parameter to be optimized. (default float(0.)
    Returns:
        pandas.DataFrame: Generated Ansatz circuit as a Pandas DataFrame."""
    def ansatz(a_theta=float(0.)):
        """Build a UCCSD ansatz circuit parametrized by a_theta per McArdle et al.

        Args:
            a_theta(float): A floating point describing the VQE parameter to be optimized.
        Returns:
            pandas.DataFrame: generated ansatz circuit as a Pandas DataFrame."""
        # Initialize Hartree-Fock State
        hartree_fock = __f__.Frame.get_frame(data={'gate': ['x', 'x'],
                                                   'targetA': [2, 3],
                                                   'targetB': [None, None],
                                                   'targetC': [None, None],
                                                   'phi': [None, None],
                                                   'theta': [None, None],
                                                   'angle': [None, None]})
        # Perform Initial Rotations to measure in Y & X bases
        initial_rots = __f__.Frame.get_frame(data={'gate': ['rx', 'h', 'h', 'h'],
                                                   'targetA': [3, 0, 1, 2],
                                                   'targetB': [None, None, None, None],
                                                   'targetC': [None, None, None, None],
                                                   'phi': [None, None, None, None],
                                                   'theta': [None, None, None, None],
                                                   'angle': [__np__.pi/2, None, None, None], })
        # Use Controlled NOTs to entangle all 4 qubits used in the ansatz
        entangle_with_cnots = __f__.Frame.get_frame(data={'gate': ['cnot', 'cnot', 'cnot'],
                                                          'targetA': [3, 2, 1],
                                                          'targetB': [2, 1, 0],
                                                          'targetC': [None, None, None],
                                                          'phi': [None, None, None],
                                                          'theta': [None, None, None],
                                                          'angle': [None, None, None]})
        # Perform the rotation in Z-basis
        rotation_in_z_basis = __f__.Frame.get_frame(data={'gate': 'rz',
                                                          'targetA': [0],
                                                          'targetB': [None],
                                                          'targetC': [None],
                                                          'phi': [None],
                                                          'theta': [a_theta],
                                                          'angle': [None]})
        # Uncompute rotations, step 1/3: using Controlled NOTs
        uncompute_rotations_with_cnots = __f__.Frame.get_frame(data={'gate': ['cnot', 'cnot', 'cnot'],
                                                                     'targetA': [3, 2, 1],
                                                                     'targetB': [2, 1, 0],
                                                                     'targetC': [None, None, None],
                                                                     'phi': [None, None, None],
                                                                     'theta': [None, None, None],
                                                                     'angle': [None, None, None]})
        # Uncompute rotations, step 2/3: using Hadamards
        uncompute_rotations_with_hadamards = __f__.Frame.get_frame(data={'gate': ['h', 'h', 'h'],
                                                                         'targetA': [3, 2, 1],
                                                                         'targetB': [None, None, None],
                                                                         'targetC': [None, None, None],
                                                                         'phi': [None, None, None],
                                                                         'theta': [None, None, None],
                                                                         'angle': [None, None, None]})
        # Uncompute rotations, step 3/3: by rotating around X-axis
        uncompute_rotations_with_rotation_in_x_basis = __f__.Frame.get_frame(data={'gate': 'rz',
                                                                                   'targetA': [0],
                                                                                   'targetB': [None],
                                                                                   'targetC': [None],
                                                                                   'phi': [None],
                                                                                   'theta': [-__np__.pi/2.],
                                                                                   'angle': [None]})
        # Put each piece of the circuit in a list we can iterate over
        pieces = [hartree_fock,
                  initial_rots,
                  entangle_with_cnots,
                  rotation_in_z_basis,
                  uncompute_rotations_with_cnots,
                  uncompute_rotations_with_hadamards,
                  uncompute_rotations_with_rotation_in_x_basis]
        # Iterate over list of DataFrames to assemble the circuit
        generated_ansatz = __f__.Frame.get_frame()
        for piece in pieces:
            generated_ansatz = generated_ansatz.append(piece)
        # Return the generated Ansatz
        return generated_ansatz
