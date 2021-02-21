# Unit test for qbitkit.qasm module
from unittest import main as __ut_main__
from os import linesep as __sep__
from qbitkit.qasm import generate as __g__
from qbitkit.qasm import translate as __t__
from qbitkit.provider.ibmq import provider as __p__
from qbitkit.provider.ibmq.circuit import circuitry as __c__
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
    def test_comments(self):
        expected_value = "// Hello, World!"
        actual_value = __g__.comment('Hello, World!')
        expected_equals_actual = False
        expected_equals_actual = __tc__.compare(expected_value,
                                                actual_value)
        self.assertEqual(expected_equals_actual, True)
    def test_if_statement(self):
        expected_value = 'if (c==0) x q[0];'
        actual_value = __g__.if_statement('c','==',0,'x',0)
        expected_equals_actual = __tc__.compare(expected_value,
                                                actual_value)
        self.assertEqual(expected_equals_actual, True)


class TestTranslation(__tc__):
    def test_df_to_ibmq(self):
        nshots = 1000
        testing_df = __tc__.example_frame(scale_qubit=5)
        testing_dev = __p__.Local.sim()
        testing_qasm = __t__.from_frame(testing_df)
        testing_circ = __c__.Translate.from_qasm(testing_qasm)
        test_run = __p__.Job.get_job(circuit=testing_circ,
                                     backend=testing_dev,
                                     shots=nshots)
        expected_counts = {'11111': nshots}
        test_counts = test_run.result().get_counts()
        self.assertEqual(expected_counts,
                         test_counts)



if __name__ == '__main__':
    __ut_main__()
