Intro to Qubits
===============

Qubits are the most fundamental unit of any quantum computer,
in much the same way bits are the most fundamental unit of any classical computer.

1. Classical Binary
===================
Before we get too deep into talking about quantum bits, lets first try to understand
their classical counterpart. One bit can represent one of two states,
just like a light switch can be either ON or OFF at any given point in time.
These two states in binary are represented as follows:

* 1 is ON
* 0 is OFF

Because large amounts of data can't be represented as just 1 or 0, bits are chained together.
For example, with two bits you can store these 4 values:

* 00
* 10
* 01
* 11

Each bit you add exponentially increases the total number of possible values that
can be stored. Mathematically speaking, the number of values that can be expressed
with :math:`n` bits is equal to exactly :math:`2^{n}`.