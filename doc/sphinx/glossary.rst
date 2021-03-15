Glossary
========
Every industry has its jargon, and quantum computing is by far no exception.
Here, we lay out terms we commonly use in qbitkit's documentation in hopes of
making our explanations of things more accessible.

0. Quantum Computing Jargon
===========================
0) Qubit
    * Short for QUantum BIT
    * Most basic unit of quantum computers, similar to classical computing bits.

1) Bra-Ket notation
    * Bra: :math:`\langle f |`
        * Denotes a linear form :math:`f: V \rightarrow \mathbb{C}`
            * e.g. a linear map mapping all of the vectors in :math:`V` to a number on complex plane :math:`\mathbb{C}`
    * Ket: :math:`| v \rangle`
        * Denotes a vector, :math:`v`, in a complex vector space :math:`V`.
        * Represents the state of a quantum system.
    * If you let the linear functional :math:`\langle f |` act on vector :math:`| v \rangle`, you would write this out as:
        * :math:`\langle f| v\rangle \in \mathbb{C}`
    * Bra-Ket: :math:`\langle x | y \rangle`
    * Also known as Dirac notation

1) Lazy Bra-Ket notation
    * Bra: `<f|`
        * Denotes a linear form `f` :math:`:V \rightarrow \mathbb{C}`
            * e.g. a linear map mapping all of the vectors in :math:`V` to a number on complex plane :math:`\mathbb{C}`
    * Ket: `|v>`
        * Denotes a vector, `v`, in a complex vector space :math:`V`.
        * Represents the state of a quantum system.
    * Bra-Ket: `<x|y>`
    * Also known as Lazy Dirac notation

2) Measurement
    * The action of reading the state of a quantum entity, thereby 'collapsing' the state of the qubit to a binary value (`|0>` or `|1>`)

3) Coherence
    * Quantum mechanics only happen in coherent systems, therefore a quantum computer only functions inside the computer's window of coherence time.
    * At present, one of the limitations present in NISQ-era hardware is short coherence times.
    * One analogy that comes to mind is coherence time is like having a maximum uptime on a classical computer after which the system shuts off.
    * Coherence time is low due to the high amount of environmental noise from external sources of radiation, interfering with the carefully emitted pulses of microwave radiation used to drive superconducting qubits.

4) Quantum Annealing
    * Quantum annealing exploits quantum tunnneling to traverse an energy landscape in order to find the global minimum.
    * By using precise magnetic forces to tune the strengths of Josephson junctions :math:`j` acting as couplers connecting qubits together in order to form what's called a chain.
    * Through the process of minor embedding, you can convert various problem spaces to :math:`j` coupler strengths and using superpositioned qubits to emit every possible answer (including incorrect answers) so that the couplers guide correct solutions iterated to lower energy states.
    * This allows you to formulate even the biggest problems you can imagine as long as you can express them as a QUBO, Ising Model, BQM or Graph problem.
    * Once the problem has been translated, and encoded by adjusting :math:`j` values to their desired strengths, the annealer pauses to wait for the dilution fridge to cool it back down as using ferromagnetism adds small amounts of heat that negatively affect the accuracy of the annealing process by adding noise.
        * This process of cooling the QPU back down after encoding is referred to as re-thermalization.
        * You can also re-thermalize after sampling the energy landscape with each read or 'shot' you take, reducing heat leading to noise introduced by the readout process.

5) Interferometry
    * One of the most important parts of any quantum computer is the ability to manipulate the qubit's spin.
    * Interferometry refers to a mechanism used to control the state of each qubit.
    * The implementation of interferometry depends on the architecture of the quantum computer in question.
        * See :doc:`computer_types` for a quick rundown of different quantum computing architectures.

1. Computer Science Jargon
==========================
1) Big O Notation
    * Common way to describe how much work there is to be done relative to the size of the problem space.
    * Where :math:`N` is the size of the problem space
        * For example, :math:`N` in the context of prime factorization of an 8-bit prime is equal to :math:`8`.
    * Linear Scaling Example: :math:`O(N)`
        * Example: Simple arithmetic such as addition
    * Logarithmic Scaling Example: :math:`O(\log(N))`
    * Exponential Scaling Example: :math:`O(2^{N})`
        * Example: Brute force prime factorization is :math:`2^{b}-1` where :math:`b` is the number of bits
    * Quadratic Scaling Example: :math:`O(\sqrt{N})`
        * Example: Grover's Algorithm

2. qbitkit-Specific Jargon
==========================
0) DataFrame
    * Object from the popular Python data science library Pandas
1) Circuit DataFrame
    * DataFrame describing a quantum circuit