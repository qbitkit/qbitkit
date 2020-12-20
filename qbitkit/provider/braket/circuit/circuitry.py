from braket.circuits import Circuit as braket_circuit
from braket.circuits import Gate as braket_gate
import numpy as np
import string


class info:
        def get_gates(self):
            gate_set = [attr for attr in dir(braket_gate) if attr[0] in string.ascii_uppercase]
            return gate_set
class translate:
    def translate_gate(op=None,
                              input_circuit=braket_circuit(),
                              targetA=0,
                              targetB=1,
                              targetC=2,
                              angle=0.15,
                              phi=0.15,
                              theta=0.15,
                              unitary_matrix=np.array([[0,1],
                                                       [1,0]]),
                              unitary_targets=[0]):
        if op == 'unitary':
            input_circuit = input_circuit.unitary(matrix=unitary_matrix,
                                                  targets=unitary_targets)
        if op == 'h':
            input_circuit = input_circuit.h(targetA)
        if op == 'x':
            input_circuit = input_circuit.x(targetA)
        if op == 'y':
            input_circuit = input_circuit.y(targetA)
        if op == 'z':
            input_circuit = input_circuit.z(targetA)
        if op == 's':
            input_circuit = input_circuit.s(targetA)
        if op == 't':
            input_circuit = input_circuit.t(targetA)
        if op == 'v':
            input_circuit = input_circuit.v(targetA)
        if op == 'vi':
            input_circuit = input_circuit.vi(targetA)
        if op == 'si':
            input_circuit = input_circuit.si(targetA)
        if op == 'ti':
            input_circuit = input_circuit.ti(targetA)
        if op == 'xx':
            input_circuit = input_circuit.xx(targetA,
                                             targetB,
                                             theta)
        if op == 'xy':
            input_circuit = input_circuit.xx(targetA,
                                             targetB,
                                             theta)
        if op == 'yy':
            input_circuit = input_circuit.yy(targetA,
                                             targetB,
                                             theta)
        if op == 'zz':
            input_circuit = input_circuit.zz(targetA,
                                             targetB,
                                             theta)
        if op == 'iswap':
            input_circuit = input_circuit.iswap(targetA,
                                                targetB)
        if op == 'phaseshift':
            input_circuit = input_circuit.phaseshift(targetA,
                                                     phi)
        if op == 'cy':
            input_circuit = input_circuit.cy(targetA,
                                             targetB)
        if op == 'cz':
            input_circuit = input_circuit.cz(targetA,
                                             targetB)
        if op == 'i':
            input_circuit = input_circuit.i(targetA)
        if op == 'rx':
            input_circuit = input_circuit.rx(targetA,
                                             angle)
        if op == 'ry':
            input_circuit = input_circuit.ry(targetA,
                                             angle)
        if op == 'rz':
            input_circuit = input_circuit.rz(targetA,
                                             angle)
        if op == 'swap':
            input_circuit = input_circuit.swap(targetA,
                                               targetB)
        if op == 'cnot':
            input_circuit = input_circuit.cnot(targetA,
                                               targetB)
        if op == 'ccnot':
            input_circuit = input_circuit.ccnot(targetA,
                                                targetB,
                                                targetC)
        if op == 'cphaseshift':
            input_circuit = input_circuit.cphaseshift(targetA,
                                                      targetB,
                                                      angle)
        if op == 'cphaseshift00':
            input_circuit = input_circuit.cphaseshift00(targetA,
                                                        targetB,
                                                        angle)
        if op == 'cphaseshift01':
            input_circuit = input_circuit.cphaseshift01(targetA,
                                                        targetB,
                                                        angle)
        if op == 'chphaseshift10':
            input_circuit = input_circuit.cphaseshift10(targetA,
                                                        targetB,
                                                        angle)
        if op == 'cswap':
            input_circuit = input_circuit.ccnot(targetA,
                                                targetB,
                                                targetC)
        if op == 'pswap':
            input_circuit = input_circuit.ccnot(targetA,
                                                targetB,
                                                phi)
        else:
            print(f'[ERROR]: Gate {op} not found. Returning an empty object with a value of None.')
            input_circuit = None
        return input_circuit