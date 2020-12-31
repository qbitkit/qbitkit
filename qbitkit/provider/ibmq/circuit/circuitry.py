from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
import numpy as np
import string

class info:
        def get_gates(self):
            """Get all usable gates. Not yet implemented (see https://github.com/qbitkit/qbitkit/issues/2)."""
            gate_set = print('Error: Function Not Yet Implemented')
            return gate_set
class circuit:
    def new(nqreg=int(2),
            ncreg=int(2),
            nancl=None):
        """Create a new quantum circuit from a specified number of quantum, classical, and ancilla registers.

        Keyword arguments:
        nqreg -- a positive integer describing the number of Qubits that will be used in the new quantum circuit. Also known as the number of quantum registers. (default 2)
        ncreg -- a positive integer describing the number of classical bits that will be used in the new quantum circuit. Also known as the number of classical registers. (default 2)
        nancl -- a positive integer describing the number of ancilla registers that will be used in the new quantum circuit. (default None)"""
        qreg = QuantumRegister(nqreg, 'qreg')
        ancl = QuantumRegister(nancl, 'ancl')
        creg = ClassicalRegister(ncreg, 'creg')
        qcir = QuantumCircuit(qreg, creg, ancl)
        return qcir
class translate:
    def translate_gate(op=None,
                              input_circuit=circuit.new(2,2,None),
                              targetA=0,
                              targetB=1,
                              targetC=2,
                              angle=0.15,
                              phi=0.15,
                              theta=0.15,
                              unitary_matrix=np.array([[0,1],
                                                       [1,0]]),
                              unitary_targets=[0]):
        """Translate individual circuit elements (gates) from a qbitkit Circuit DataFrame.

        Keyword arguments:
        targetA -- the first qubit to target in a 1,2 or 3 qubit gate. (default 0)
        targetB -- the second qubit to target in a 2 or 3 qubit gate. (default 1)
        targetC -- the third qubit to target in a 3 qubit gate. (default 2)
        angle -- the angle to set for the gate specified as a float. (default 0.15)
        phi -- the phi to set for the gate specified as a float. (default 0.15)
        theta -- the theta to set for the gate specified as a float. (default 0.15)
        unitary_matrix -- a numpy array defining the matrix to use for a unitary gate. (default np.array([[0,1]],[1,0]]))
        unitary_targets -- a list defining the targets to use for a unitary gate. (default [0])"""
        if op == 'h':
            input_circuit = input_circuit.h(targetA)
            return input_circuit
        if op == 'x':
            input_circuit = input_circuit.x(targetA)
            return input_circuit
        if op == 'y':
            input_circuit = input_circuit.y(targetA)
            return input_circuit
        if op == 'z':
            input_circuit = input_circuit.z(targetA)
            return input_circuit
        if op == 's':
            input_circuit = input_circuit.s(targetA)
            return input_circuit
        if op == 't':
            input_circuit = input_circuit.t(targetA)
            return input_circuit

        if op == 'iswap':
            input_circuit = input_circuit.iswap(targetA,
                                                targetB)
            return input_circuit
        if op == 'cy':
            input_circuit = input_circuit.cy(targetA,
                                             targetB)
            return input_circuit
        if op == 'cz':
            input_circuit = input_circuit.cz(targetA,
                                             targetB)
            return input_circuit
        if op == 'i':
            input_circuit = input_circuit.i(targetA)
            return input_circuit
        if op == 'rx':
            input_circuit = input_circuit.rx(targetA,
                                             angle)
            return input_circuit
        if op == 'ry':
            input_circuit = input_circuit.ry(targetA,
                                             angle)
            return input_circuit
        if op == 'rz':
            input_circuit = input_circuit.rz(targetA,
                                             angle)
            return input_circuit
        if op == 'swap':
            input_circuit = input_circuit.swap(targetA,
                                               targetB)
            return input_circuit
        if op == 'cnot':
            input_circuit = input_circuit.cnot(targetA,
                                               targetB)
            return input_circuit
        if op == 'ccnot':
            input_circuit = input_circuit.toffoli(targetA,
                                                targetB,
                                                targetC)
            return input_circuit
        else:
            print(f'[ERROR]: Gate {op} not found. Returning an empty object with a value of None.')
            input_circuit = None
        return input_circuit