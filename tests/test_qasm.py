# Unit test for qbitkit.qasm module
from unittest import main as __ut_main__
from os import linesep as __sep__
from qbitkit.qasm import generate as __g__
from numpy.random import randint as __rand__
from tests.qktest import QKTestCase as __tc__


# TestCase for QASM Generation (qbitkit.qasm.generate)
class TestGeneration(__tc__):
    def test_headers(self):
        # Set expectation of result when running test
        expected_headers = f"""OPENQASM 2.0;{__sep__}include "qelib1.inc";"""
        # Get actual value
        headers = __g__.headers()
        # Check if headers are what they should be
        correct_headers = __tc__.compare(expected_headers,
                                         headers)
        self.assertEqual(correct_headers, True)
    def test_measurements(self):
        # Initialize variables
        test_q = __rand__(0, 1024)
        test_c = __rand__(0, 1024)
        actual_expected_match = False
        # Set expected value
        expected_measurements = f"measure q[{test_q}] -> c[{test_c}];"
        # Get actual value
        actual_measurements = __g__.measurement(test_q,
                                                test_c)
        # Check if actual and expected values match as they should
        actual_expected_match = __tc__.compare(expected_measurements,
                                               actual_measurements)
        self.assertEqual(actual_expected_match, True)
    def test_single_qubit_gates(self):
        test_q = __rand__(0,1024)
        expected_value = f"h q[{test_q}];"
        actual_value = __g__.gate('h',
                                  targetA=test_q)
        actual_equals_expected = __tc__.compare(expected_value,
                                                actual_value)
        self.assertEqual(actual_equals_expected,True)

    def test_triple_qubit_gates(self):
        test_q0 = __rand__(0, 2048)
        test_q1 = __rand__(0, 2048)
        test_q2 = __rand__(0, 2048)
        test_gate = 'cx'
        test_targets = f'q[{test_q0}], q[{test_q1}], q[{test_q2}]'
        expected_value = f'{test_gate} {test_targets};'
        actual_value = __g__.gate(test_gate, # Gate Spec
                                  test_q0, # TargetA Spec
                                  test_q1, # TargetB Spec
                                  test_q2) # TargetC Spec
        expected_equals_actual = __tc__.compare(expected_value,
                                                actual_value)
        self.assertEqual(expected_equals_actual, True)
    def test_double_qubit_gates(self):
        test_q0 = __rand__(0, 2048)
        test_q1 = __rand__(0, 2048)
        test_gate = 'cx'
        test_targets = f'q[{test_q0}], q[{test_q1}]'
        expected_value = f'{test_gate} {test_targets};'
        actual_value = __g__.gate(test_gate, # Gate Spec
                                  test_q0, # TargetA Spec
                                  test_q1) # TargetB Spec
        expected_equals_actual = __tc__.compare(expected_value,
                                                actual_value)
        self.assertEqual(expected_equals_actual, True)


if __name__ == '__main__':
    __ut_main__()
