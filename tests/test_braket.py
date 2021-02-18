import unittest.main as __ut_main__
from unittest import TestCase as __tc__
from qbitkit.provider.braket import provider as __p__
from braket.circuits import Circuit as __c__


def state_prep(self=None):
    # Create New Circuit
    test_circ = __c__()
    # Set All Qubits to |1>
    for i in range(16):
        test_circ = test_circ.x(i)
    # Set all Qubits to |0>
    for i in range(16):
        test_circ = test_circ.x(i)
    # First Byte 01110001 q
    test_circ = test_circ.x(1).x(2).x(3).x(7)
    # Second Byte 01101011 k
    test_circ = test_circ.x(9).x(10).x(12).x(14).x(15)
    return test_circ

class TestOfflineSimulator(__tc__):
    def test_local_sim(self):
        test_circ = state_prep()
        # Create Local Simulator
        lsim = __p__.Local.sim()
        ls = lsim('default')
        # Run Circuit on Local Simulator
        result = ls.run(test_circ,
                        shots=10000)
        # Set Expected Result
        expected_probabilities = {'0111000101101011': 1.0}
        # Get Actual Result
        actual_probabilities = result.result().measurement_probabilities
        self.assertEqual(expected_probabilities,
                         actual_probabilities)

if __name__ == '__main__':
    __ut_main__()
