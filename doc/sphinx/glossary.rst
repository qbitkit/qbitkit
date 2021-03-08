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
        * Denotes a linear form :math:`f:V \rightarrow \mathbb{C}`
            * e.g. a linear map mapping all of the vectors in :math:`\left V` to a number on complex plane :math:`\mathbb{C}`
    * Ket: :math:`| v \rangle`
        * Denotes a vector, :math:`\left v`, in a complex vector space :math:`\left V`.
        * Represents the state of a quantum system.
    * If you let the linear functional :math:`\langle f |` act on vector :math:`| v \rangle`, you would write this out as:
        * :math:`\langle f| v\rangle \in \mathbb{C}`
    * Bra-Ket: :math:`\langle x \middle| y \rangle`
    * Also known as Dirac notation

1) Lazy Bra-Ket notation
    * Bra: `<f|`
        * Denotes a linear form `f` :math:`:V \rightarrow \mathbb{C}`
            * e.g. a linear map mapping all of the vectors in :math:`\left V` to a number on complex plane :math:`\mathbb{C}`
    * Ket: `|v>`
        * Denotes a vector, `v`, in a complex vector space :math:`V`.
        * Represents the state of a quantum system.
    * Bra-Ket: `<x|y>`
    * Also known as Lazy Dirac notation

3) Measurement
    * The action of reading the state of a quantum entity, thereby 'collapsing' the state of the qubit to a binary value (`|0>` or `|1>`)

1. qbitkit-Specific Jargon
==========================
0) DataFrame
    * Object from the popular Python data science library Pandas
1) Circuit DataFrame
    * DataFrame describing a quantum circuit