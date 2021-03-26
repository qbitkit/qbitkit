The Quantum Stack
=================
The "Quantum Stack" refers to the combination of all of the different software
and hardware pieces necessary for building a quantum computer.

To explain the quantum stack, we'll go over each layer of the Quantum Stack
in order of lowest level (closest to the actual qubits used for a given quantum
computing task) to highest level (closest to the "end user"):

1) Qubits
2) Control Hardware
    * Typically an AWG for superconducting qubits
3) Pulse
4) Circuit
5) Algorithm
6) Application

Layers 4-6 describe most of qbitkit's functionality, with the majority of the library addressing layer 4.