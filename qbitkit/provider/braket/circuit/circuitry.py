from braket.circuits import Circuit as braket_circuit
from braket.circuits import Gate as braket_gate
import string
class info:
        def get_gates(self):
            gate_set = [attr for attr in dir(braket_gate) if attr[0] in string.ascii_uppercase]
            return gate_set
class translate:
    def translate_instruction(op=None,
                              input_circuit=braket_circuit(),
                              targetA=0,
                              targetB=0,
                              targetC=0):
        if op == 'h':
            input_circuit = input_circuit.h(targetA)
        if op == 'cnot':
            input_circuit = input_circuit.cnot(targetA,
                                               targetB)
        if op == 'ccnot':
            input_circuit = input_circuit.ccnot(targetA,
                                                targetB,
                                                targetC)
        else:
            print(f'[ERROR]: Gate {op} not found. Returning an empty object.')
            input_circuit = None
        return input_circuit