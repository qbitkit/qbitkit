from braket.circuits import Circuit as braket_circuit
from braket.circuits import Gate as braket_gate
from qbitkit.io.frame import frame as fr
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
            return input_circuit
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
        if op == 'v':
            input_circuit = input_circuit.v(targetA)
            return input_circuit
        if op == 'vi':
            input_circuit = input_circuit.vi(targetA)
            return input_circuit
        if op == 'si':
            input_circuit = input_circuit.si(targetA)
            return input_circuit
        if op == 'ti':
            input_circuit = input_circuit.ti(targetA)
            return input_circuit
        if op == 'xx':
            input_circuit = input_circuit.xx(targetA,
                                             targetB,
                                             theta)
            return input_circuit
        if op == 'xy':
            input_circuit = input_circuit.xx(targetA,
                                             targetB,
                                             theta)
            return input_circuit
        if op == 'yy':
            input_circuit = input_circuit.yy(targetA,
                                             targetB,
                                             theta)
            return input_circuit
        if op == 'zz':
            input_circuit = input_circuit.zz(targetA,
                                             targetB,
                                             theta)
            return input_circuit
        if op == 'iswap':
            input_circuit = input_circuit.iswap(targetA,
                                                targetB)
            return input_circuit
        if op == 'phaseshift':
            input_circuit = input_circuit.phaseshift(targetA,
                                                     phi)
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
            input_circuit = input_circuit.ccnot(targetA,
                                                targetB,
                                                targetC)
            return input_circuit
        if op == 'cphaseshift':
            input_circuit = input_circuit.cphaseshift(targetA,
                                                      targetB,
                                                      angle)
            return input_circuit
        if op == 'cphaseshift00':
            input_circuit = input_circuit.cphaseshift00(targetA,
                                                        targetB,
                                                        angle)
            return input_circuit
        if op == 'cphaseshift01':
            input_circuit = input_circuit.cphaseshift01(targetA,
                                                        targetB,
                                                        angle)
            return input_circuit
        if op == 'cphaseshift10':
            input_circuit = input_circuit.cphaseshift10(targetA,
                                                        targetB,
                                                        angle)
            return input_circuit
        if op == 'cswap':
            input_circuit = input_circuit.cswap(targetA,
                                                targetB,
                                                targetC)
            return input_circuit
        if op == 'pswap':
            input_circuit = input_circuit.pswap(targetA,
                                                targetB,
                                                phi)
            return input_circuit
        else:
            print(f'[ERROR]: Gate {op} not found. Returning an empty object with a value of None.')
            input_circuit = None
        return input_circuit
    def df_circuit(df=fr.get_frame(),
                   input_circuit=braket_circuit()):
        for index, row in df.iterrows():
            qcgates = str(row['gate'])
            targetA = row['targetA']
            targetB = row['targetB']
            targetC = row['targetC']
            circuit = translate.translate_gate(input_cir=input_circuit,
                                               op=qcgates,
                                               targetA=targetA,
                                               targetB=targetB,
                                               targetC=targetC)
            return circuit