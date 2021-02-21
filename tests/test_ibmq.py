from unittest import main as __ut_main__
from qbitkit.provider.ibmq import provider as __p__
from qbitkit.provider.ibmq.circuit import circuitry as __c__
from qiskit import Aer as __a__
from qiskit import BasicAer as __ba__
from tests.qktest import QKTestCase as __tc__


class TestAerSimulatorCreation(__tc__):
    def test_aer_creation(self):
        qiskit_aer_type = type(__a__.get_backend('qasm_simulator'))
        qbitkit_aer_type = type(__p__.Local.aer())
        self.assertEqual(qiskit_aer_type,
                         qbitkit_aer_type)
    def test_basicaer_creation(self):
        qiskit_basicaer_type = type(__ba__.get_backend('qasm_simulator'))
        qbitkit_basicaer_type = type(__p__.Local.basic_aer())
        self.assertEqual(qiskit_basicaer_type,
                         qbitkit_basicaer_type)
    def test_alt_aer_creation(self):
        qiskit_aer_type = type(__a__.get_backend('qasm_simulator'))
        qbitkit_aer_type = type(__p__.Local.sim(backend='aer'))
        self.assertEqual(qiskit_aer_type,
                         qbitkit_aer_type)
    def test_alt_basicaer_creation(self):
        qiskit_basicaer_type = type(__ba__.get_backend('qasm_simulator'))
        qbitkit_basicaer_type = type(__p__.Local.sim(backend='basic_aer'))
        self.assertEqual(qiskit_basicaer_type,
                         qbitkit_basicaer_type)


class TestTranslation(__tc__):
    def test_from_df(self):
        nshots = 1000
        nqubits = 8
        df = __tc__.example_frame(scale_qubit=nqubits)
        test_circ = __c__.Translate.df_circuit(df=df,
                                               q=nqubits,
                                               c=nqubits)
        test_dev = __p__.Local.sim()
        test = __p__.Job.get_job(circuit=test_circ,
                                 backend=test_dev,
                                 shots=nshots)
        test_results = test.result().get_counts()
        expected_result_str = '1' * nqubits
        expected_results = {expected_result_str: nshots}
        self.assertEqual(expected_results,
                         test_results)


if __name__ == '__main__':
    __ut_main__()
