from qbitkit.provider.braket.circuit.circuitry import translate as translate_braket
from qbitkit.provider.braket.circuit.circuitry import braket_circuit as braket_circuit
class to_provider:
    def braket(op=None,
               input_circuit=braket_circuit(),
               targetA=None,
               targetB=None,
               targetC=None):
        translated = translate_braket.translate_gate(op=None,
                                                     input_circuit=braket_circuit(),
                                                     targetA=0,
                                                     targetB=1,
                                                     targetC=2,
                                                     angle=0.15,
                                                     phi=0.15,
                                                     theta=0.15,
                                                     unitary_matrix=np.array([[0,1],
                                                                              [1,0]]),
                                                     unitary_targets=[0])
        return translated