# Unit test for qbitkit.qasm module
import unittest as __ut__
from os import linesep as __sep__
from qbitkit.qasm import generate as __g__
from numpy.random import randint as __rand__


# TestCase for QASM Generation (qbitkit.qasm.generate)
class TestGeneration(__ut__.TestCase):
    def test_headers(self):
        # Set expectation of result when running test
        expected_headers = f"""OPENQASM 2.0;{__sep__}include "qelib1.inc";"""
        # Initialize variables
        correct_headers = False
        headers = __g__.headers()
        # Check if headers are what they should be
        if headers == expected_headers:
            correct_headers = True
        else:
            print(f"--> Headers generated are invalid. {__sep__}",
                  f"--> Here's what they should be: {__sep__}'{expected_headers}'",
                  f"--> Here's what we got: {__sep__}'{headers}'")
            correct_headers = False
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
        if actual_measurements == expected_measurements:
            actual_expected_match = True
        else:
            print("--> Actual and Expected Values Differ.",
                  __sep__,
                  f"---> Expected Value: '{str(expected_measurements)}'",
                  __sep__,
                  f"---> Actual Value: '{str(actual_measurements)}'")
            actual_expected_match = False
        self.assertEqual(actual_expected_match, True)
    def test_single_qubit_gates(self):
        test_q = __rand__(0,1024)
        expected_value = f"h q[{test_q}];"
        actual_value = __g__.gate('h',
                                  targetA=test_q)
        actual_equals_expected = False
        if actual_value == expected_value:
            actual_equals_expected = True
        else:
            print("-->Actual output does not match expected output.",
                  __sep__,
                  f"---> Expected Output: '{expected_value}'",
                  __sep__,
                  f"---> Actual Output: '{actual_value}'")
            actual_equals_expected = False
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
        expected_equals_actual = False
        if actual_value == expected_value:
            print(f"--> Success! {__sep__}",
                  f"---> Expected value: '{expected_value}'",
                  f"= Actual Value: {actual_value}")
            expected_equals_actual = True
        else:
            print("--> Actual Output Did not Match Expected Output.",
                  f"{__sep__}---> Expected Output: '{expected_value}'",
                  f"{__sep__}---> Actual Value: '{actual_value}'")
            expected_equals_actual = False
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
        expected_equals_actual = False
        if actual_value == expected_value:
            print(f"--> Success! {__sep__}",
                  f"---> Expected value: '{expected_value}'",
                  f"= Actual Value: {actual_value}")
            expected_equals_actual = True
        else:
            print("--> Actual Output Did not Match Expected Output.",
                  f"{__sep__}---> Expected Output: '{expected_value}'",
                  f"{__sep__}---> Actual Value: '{actual_value}'")
            expected_equals_actual = False
        self.assertEqual(expected_equals_actual, True)


if __name__ == '__main__':
    __ut__.main()
