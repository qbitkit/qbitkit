from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qbitkit.error import error as qbitkit_error
from qbitkit.io.frame import Frame as fr


def get_support_status():
    ibmq_support_status = 'experimental'
    resource_name = 'IBM Quantum Experience'
    issue_url = 'https://github.com/qbitkit/qbitkit/issues/2'
    additional_notes = 'For more information on forthcoming '
    additional_notes = additional_notes + resource_name + ' '
    additional_notes = additional_notes + 'support, see '
    additional_notes = additional_notes + issue_url + ' .'
    qbitkit_error.Errors.support_status(feature_state=ibmq_support_status,
                                        resource_name=resource_name,
                                        additional_notes=additional_notes)
    return ibmq_support_status


get_support_status()


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
        qreg = QuantumRegister(nqreg, 'qreg')
        ancl = QuantumRegister(nancl, 'ancl')
        creg = ClassicalRegister(ncreg, 'creg')
        qcir = QuantumCircuit(qreg, creg, ancl)
        return qcir


class Translate:
    def translate_gate(op='h',
                       input_circuit=Circuit.new(2, 2, 1),
                       targetA=0,
                       targetB=1,
                       targetC=2,
                       angle=0.15,
                       theta=0.15):
        """Translate individual circuit elements (gates) from a qbitkit Circuit DataFrame.

        Args:
            input_circuit (qiskit.QuantumCircuit): A Qiskit QuantumCircuit() to optionally append the translated gate to. (default qbitkit.provider.ibmq.circuit.circuitry.circuit.new(2,2,1))
            op (str): The instruction to translate into a gate. Default is a Hadamard gate represented as 'h'. (default 'h')
            targetA (int): the first qubit to target in a 1,2 or 3 qubit gate. (default 0)
            targetB (int): the second qubit to target in a 2 or 3 qubit gate. (default 1)
            targetC (int): the third qubit to target in a 3 qubit gate. (default 2)
            angle (float): the angle to set for the gate specified as a float. (default 0.15)
            theta (float): the theta to set for the gate specified as a float. (default 0.15)
        Returns:
            qiskit.QuantumCircuit: Qiskit circuit with translated gate appended to it"""
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
        if op == 'crz':
            input_circuit = input_circuit.crz(control_qubit=targetA,
                                              target_qubit=targetB,
                                              theta=theta)
        if op == 'ch':
            input_circuit = input_circuit.ch(control_qubit=targetA,
                                             target_qubit=targetB)
            return input_circuit
        if op == 'i':
            input_circuit = input_circuit.id(targetA)
            return input_circuit
        if op == 'si':
            input_circuit = input_circuit.sdg(targetA)
            return input_circuit
        if op == 'ti':
            input_circuit = input_circuit.tdg(targetA)
            return input_circuit
        else:
            print(f'[ERROR]: Gate {op} not found. Returning an empty object with a value of None.')
            input_circuit = None
        return input_circuit

    def df_circuit(df=fr.get_frame(),
                   input_circuit=Circuit.new()):
        """Converts a Circuit DataFrame into a Qiskit QuantumCircuit by iterating over the DataFrame and turning each row of the dataframe into a gate or set of gates.

        Args:
            df (pandas.DataFrame): specify a Circuit DataFrame to convert to a Qiskit QuantumCircuit. (default qbitkit.io.frame.get_frame())
            input_circuit (qiskit.QuantumCircuit): specify a circuit to append the translated circuit's contents to. (default ())
        Returns:
            qiskit.QuantumCircuit: Qiskit QuantumCircuit translated from specified DataFrame"""
        for index, row in df.iterrows():
            qcgates = str(row['gate'])
            targetA = row['targetA']
            targetB = row['targetB']
            targetC = row['targetC']
            circuit = Translate.translate_gate(input_circuit=input_circuit,
                                               op=qcgates,
                                               targetA=targetA,
                                               targetB=targetB,
                                               targetC=targetC)
        return circuit
