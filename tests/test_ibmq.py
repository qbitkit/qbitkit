import unittest as __ut__
from qbitkit.provider.ibmq import provider as __p__
from qiskit import Aer as __a__
from qiskit import BasicAer as __ba__


class TestAerSimulators(__ut__.TestCase):
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


if __name__ == '__main__':
    __ut__.main()
