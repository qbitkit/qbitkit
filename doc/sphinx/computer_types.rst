Types of Quantum Computers
==========================
There are many different architectures of quantum computers, however unlike
the different architectures of classical computers (x86, Arm, RISC) the differences
between them are much more subtle than different instruction sets.

1. Superconducting Qubits
=========================
By far the most popular architecture of all, involving the use of cryogenic
hardware to unlock the superconductive properties of certain metals. Qubits
are driven using controlled pulses of microwave radiation emitted from an
Arbitrary Waveform Generator (AWG). For measurements, the same AWG is used
to read the qubit's state. Both the pulses used to drive the qubit as well
as the measurements being taken are carried along control lines, typically
one per qubit on current systems.

2. Ion Trapping Qubits
======================
Ion Trapping is rapidly growing in popularity as it continues to shatter records
for important metrics like Quantum Volume. By leveraging the precision of laser
beams, each qubit benefits from high fidelity rotations and long coherence times.
Additionally, ion trap quantum computers typically are fully connected, meaning
a 2 qubit gate can connect any pair of qubits -- without the need for swap gates
that would waste precious coherence time.

What happens every time a shot is taken on an ion trap quantum computer is summarized
as follows:
1) A laser is used to ionize an atom of Ytterbium.
2) An ion trap uses electromagnetic force to hold a chain of these ions in a linear array.
3) A laser is used to both set the spin of all qubits to up (|0> in lazy braket) and cool the qubits down using the doppler effect to the point where atoms nearly stop moving
4) One 'global' laser shining through all qubits sets the tempo like a drummer in a band, and each qubit has its own laser. When a qubit's own laser interferes with the global laser, the qubit's state is precisely altered to achieve the desired state
5) Once it's time to read out the state of the qubits, each qubit's laser shines on it's own qubit and the light of the laser is measured. The state of each qubit, be it |1> or |0> can be deduced based on whether or not the laser was able to shine through a given qubit.