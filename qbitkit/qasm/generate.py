from os import linesep as __linesep__


def headers(qasm_version=float(2.0),
            includes=list(['qelib1.inc'])):
    """Generate QASM 2.0 formatted headers.

    Args:
        qasm_version(float): a floating point value describing the version number. (default float(2.0))
        includes(list): a list of strings describing what to import. (default list(['qelib1.inc']))
    Returns:
        str: the generated headers to be placed at the top of a QASM string"""
    nincludes = int(0)
    niterations = int(0)
    ver_float_to_str = str(qasm_version)
    dq = '"'
    include_formatted = ''
    all_includes = ''
    qasm_ver = f"OPENQASM {ver_float_to_str};"
    for include in includes:
        nincludes + 1
    for include in includes:
        niterations = niterations + 1
        include_formatted = f"include {dq}{include}{dq};"
        if niterations == 1:
            all_includes = include_formatted
        elif niterations > 1:
            all_includes = all_includes + include_formatted
        else:
            all_includes = str("")
    headers = f"{qasm_ver}{__linesep__}{all_includes}"
    return headers


def registers(c=2,
              q=2):
    """Generate a QASM String containing the specified number of classical and quantum registers.

    Args:
        c(int): The number of Classic registers. (default 2)
        q(int): The number of Quantum registers, in other words the number of logical Qubits. (default 2)
    Returns:
        str: A string object containing the generated QASM."""
    qreg_str = f"qreg q[{str(q)}];"
    creg_str = f"creg c[{str(c)}];"
    reg_str = qreg_str + __linesep__ + creg_str + __linesep__
    return reg_str


def gate(self=str('h'),
         targets=list([int(0)])):
    """Generate a gate from it's name as a string passed to self, and a list of targets passed to targets.

    Args:
        self(str): The name used to represent the gate in QASM. For example, a Hadamard Gate is 'h'. (default str('h'))
        targets(list): A list of positive integers that will be used as a list of target qubits to apply the gate to. (default list([int(0)]))
    Returns:
        str: A string object containing the specified gate as QASM."""
    ntargets = 0
    ngenerated_targets = 0
    target_str = ''
    all_targets = ''
    for target in targets:
        ntargets = ntargets + 1
    for target in targets:
        ngenerated_targets = ngenerated_targets + 1
        if ngenerated_targets == 1:
            target_str = str(f' q[{str(target)}],')
        if ngenerated_targets == ntargets:
            target_str = str(f'q[{str(target)}];')
        elif ngenerated_targets < ntargets:
            target_str = str(f'q[{str(target)}],')
        else:
            target_str = str('')
        all_targets = all_targets + target_str
    compiled_gate = self + ' ' + all_targets
    return compiled_gate


def measurement(qreg=int(0),
                creg=int(0)):
    """Generate QASM that takes a measurement from a qubit and stores it in a classical register.

    Args:
        qreg(int): Number of the Qubit to measure. (default 0)
        creg(int): Number of the Classical Register to store the measurement to. (default 1)
    Returns:
        str: Generated QASM containing measurement instruction."""
    meas_str = f'measure q[{str(qreg)}] -> c[{str(creg)}];'
    return meas_str
