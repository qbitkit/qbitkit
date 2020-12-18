from braket.aws import AwsDevice
class run:
    def circuit(circuit=None,
                device=None,
                shots=1000,
                disable_qubit_rewiring=True):
        task = device.run(circuit,
                          shots=shots,
                          disable_qubit_rewiring=disable_qubit_rewiring)
        return task