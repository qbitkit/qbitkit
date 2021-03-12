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

3. Photonic Qubits
==================
When you think about the future of quantum computing, what comes to mind is a smaller
form factor. Cryogenics is a massive pain to set up and maintain over time, adding
a significant amount of bulk and cost to quantum hardware endeavors. So, just like
how classical computers started out as large hotel room sized device, perhaps
the next logical evolution of quantum is making a computer small enough to fit in
a standard rack-mountable enclosure.

Well, quite interestingly, there is a company that has already pulled off this feat
of reducing the size of a quantum computer down to something that can fit on a server
rack. This company is Xanadu, and they managed to accomplish this impressive feat of
engineering in large part thanks to choosing to use photonic qubits as their medium.

Each shot starts with a single photon emitter on each qubit, well, emitting a single
photon. These photons travel down optical channels that in spots have been doped to
allow programmable control of the state of the photon as it passes through its channel.
Once it's time to read out the state of the photon, a single photon counter is used
to measure whether the photon made it all the way through its channel (making its value |1>),
or if it instead did not make it (thus making its value |0>).
