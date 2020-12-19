from braket.circuits import Circuit, Gate
import string
class info:
        def get_gates(self):
            gate_set = [attr for attr in dir(Gate) if attr[0] in string.ascii_uppercase]
            return gate_set
class translate:
    def translate_instruction(op=None,
                              input_circuit=Circuit(),
                              targetA=0,
                              targetB=0,
                              targetC=0):
        if op == 'toffoli':
            input_circuit = input_circuit.ccnot()
        return input_circuit