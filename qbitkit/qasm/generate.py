def registers(c=2,
              q=2):
    """Generate a QASM String containing the specified number of classical and quantum registers.

    Args:
        c(int): The number of Classic registers. (default 2)
        q(int): The number of Quantum registers, in other words the number of logical Qubits. (default 2)
    Returns:
        str: A string object containing the generated QASM."""
    reg_str = f"""qreg q[{str(q)}];
    creg c[{str(c)}];"""
    return reg_str
