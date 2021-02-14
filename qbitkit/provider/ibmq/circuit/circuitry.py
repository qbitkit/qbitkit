from qiskit import QuantumCircuit as __Quantum_Circuit__
from qiskit import QuantumRegister as __Quantum_Register__
from qiskit import ClassicalRegister as __Classical_Register__
from qbitkit.io.frame import Frame as __fr__
from qbitkit.qasm import translate as __qasm_t__


class Circuit:
    def new(nqreg=int(2),
            ncreg=int(2),
            nancl=int(2)):
        """Create a new quantum circuit from a specified number of quantum, classical, and ancilla registers.

        Args:
            nqreg (int): a positive integer describing the number of Qubits that will be used in the new quantum circuit. Also known as the number of quantum registers. (default 2)
            ncreg (int): -- a positive integer describing the number of classical bits that will be used in the new quantum circuit. Also known as the number of classical registers. (default 2)
            nancl (int): a positive integer describing the number of ancilla registers that will be used in the new quantum circuit. (default None)
        Returns:
            qiskit.QuantumCircuit: an empty Qiskit quantum circuit"""
        qreg = __Quantum_Register__(nqreg, 'qreg')
        ancl = __Quantum_Register__(nancl, 'ancl')
        creg = __Classical_Register__(ncreg, 'creg')
        qcir = __Quantum_Circuit__(qreg, creg, ancl)
        return qcir


class Translate:
    def from_qasm(
            qasm=str('')):
        """Create a new Qiskit QuantumCircuit from a QASM 2.0 string.

        Args:
            qasm(str): String containing valid QASM 2.0. (default str(''))
        Returns:
            qiskit.circuit.QuantumCircuit: Circuit created from specified QASM 2.0."""
        # Create a new QuantumCircuit from specified QASM string.
        circuit = __Quantum_Circuit__.from_qasm_str(
            qasm_str=str(qasm))
        # Return new QuantumCircuit translated from a QASM string.
        return circuit
    def df_circuit(df=__fr__.get_frame(),
                   q=5,
                   c=5):
        """Converts a Circuit DataFrame into a Qiskit QuantumCircuit by iterating over the DataFrame and turning each row of the dataframe into a gate or set of gates.

        Args:
            df (pandas.DataFrame): specify a Circuit DataFrame to convert to a Qiskit QuantumCircuit. (default qbitkit.io.frame.get_frame())
            q (int): Number of Quantum registers to initialize (in other words, the number of qubits to use.) (default 5)
            c (int): Number of Classical registers to initialize. (default 5)
        Returns:
            qiskit.QuantumCircuit: Qiskit QuantumCircuit translated from specified DataFrame"""
        qasm_circ = __qasm_t__.from_frame(df,
                                          qreg=q,
                                          creg=c)
        circuit = __Quantum_Circuit__.from_qasm_str(qasm_circ)
        return circuit
