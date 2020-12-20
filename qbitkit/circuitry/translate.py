from ..provider.braket.circuit.circuitry import translate as translate_braket
from ..provider.braket.circuit.circuitry import braket_circuit as braket_circuit
class to_provider:
    def braket(op=None,
               input_circuit=braket_circuit(),
               targetA=None,
               targetB=None,
               targetC=None):
        translated = translate_braket.translate_instruction(op,
                                                            input_circuit,
                                                            targetA,
                                                            targetB,
                                                            targetC)
        return translated