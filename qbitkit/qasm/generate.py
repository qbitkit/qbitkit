from os import linesep as __linesep__


def comment(self=str('')):
    """Generate a single-line QASM 2.0 comment from a string.

    Args:
        self(str): String to add as a comment in QASM 2.0 (default str(''))
    Returns:
        str: Generated QASM 2.0 comment."""
    # Generate QASM 2.0 comment from self parameter.
    qasm_comment = f'// {str(self)}'
    # Return generated QASM 2.0.
    return qasm_comment


def headers(qasm_version=float(2.0),
            includes=list(['qelib1.inc'])):
    """Generate QASM 2.0 formatted headers.

    Args:
        qasm_version(float): a floating point value describing the version number. (default float(2.0))
        includes(list): a list of strings describing what to import. (default list(['qelib1.inc']))
    Returns:
        str: the generated headers to be placed at the top of a QASM string"""
    # Initialize Variables
    # Counter for include statements
    nincludes = int(0)
    # Counter for iterations
    niterations = int(0)
    # Convert QASM version float to a string
    ver_float_to_str = str(qasm_version)
    # Double Quote
    dq = '"'
    # Formatted include statement
    include_formatted = ''
    # All include statements concatenated into one string
    all_includes = ''
    # QASM version statement
    qasm_ver = f"OPENQASM {ver_float_to_str};"
    # Count number of include statements we need to make
    for include in includes:
        nincludes + 1
    # Iterate over include statements, formatting each statement accordingly.
    for include in includes:
        niterations = niterations + 1
        include_formatted = f"include {dq}{include}{dq};"
        if niterations == 1:
            all_includes = include_formatted
        elif niterations > 1:
            all_includes = all_includes + include_formatted
        else:
            all_includes = str("")
    # Concatenate all headers into one string
    headers = f"{qasm_ver}{__linesep__}{all_includes}"
    # Return generated headers
    return headers


def registers(c=None,
              q=None):
    """Generate a QASM String containing the specified number of classical and quantum registers.

    Args:
        c(int): The number of Classic registers. (default None)
        q(int): The number of Quantum registers, in other words the number of logical Qubits. (default None)
    Returns:
        str: A string object containing the generated QASM."""

    # Check if qregs have been specified.
    if q is not None:
        # Create qregs string.
        qreg_str = f"qreg q[{str(q)}];"
    # Check if qregs are set to None.
    elif q is None:
        # Set qregs string to an empty string.
        qreg_str = ''

    # Check if cregs have been specified.
    if c is not None:
        # Create cregs string.
        creg_str = f"creg c[{str(c)}];"
    # Check if cregs is set to None.
    elif c is None:
        # Set cregs string to an empty string.
        creg_str = ''

    # Assemble full string containing classical and quantum registers separated by the OS's line separator.
    reg_str = qreg_str + __linesep__ + creg_str + __linesep__

    # Return generated QASM registers.
    return reg_str


def gate(self=str('h'),
         targetA=None,
         targetB=None,
         targetC=None,
         angle=None,
         Utheta=None,
         Uphi=None,
         Ulambda=None,
         custom_name=None,
         custom_params=None):
    """Generate a gate from it's name as a string passed to self, and a list of targets passed to targets.

    Args:
        self(str): The name used to represent the gate in QASM. For example, a Hadamard Gate is 'h'. (default str('h'))
        targetA(int): First target qubit. (default None)
        targetB(int): Second target qubit. (default None)
        targetC(int): Third target qubit. (default None)
        angle(float): Angle to specify in Radians for rotation gates like RX, RY, RZ. (default None)
        Utheta(str): Theta value for U-gates. (default None)
        Uphi(str): Phi value for U-gates. (default None)
        Ulambda(str): Lambda value for U-gates. (default None)
        custom_name(str): Name for user-defined opaque gate declarations, unitary gate declarations, and user-defined unitary gates. (default None)
        custom_params(str): Parameters for user-defined opaque gate declarations, unitary gate declarations, and user-defined unitary gates. (default None)
    Returns:
        str: A string object containing the specified gate as QASM."""
    angle_gates = ['rx', 'ry', 'rz',
                   'crx', 'cry', 'crz']
    # Ensure Integer Variables Have Correct Types
    if targetA is not None:
        targetA = int(targetA)

    if targetB is not None:
        targetB = int(targetB)

    if targetC is not None:
        targetC = int(targetC)

    # Check if a U gate was specified.
    if self == 'U':
        # Compile a U gate.
        compiled_gate = f'U({Utheta},{Uphi},{Ulambda}) q[{targetA}];'
        # Return compiled U gate.
        return compiled_gate
    # Create an empty string for variable 'targets'
    targets = ''
    # Check if targetA is not a default value.
    # Generate first target qubit.
    targetA_qasm = f'q[{int(targetA)}]'
    # Add translated target to 'targets'.
    targets = targets + targetA_qasm
    # Check if targetB is not a default value.
    if targetB is not None and targetB > 0:
        # Generate second target qubit.
        targetB_qasm = f', q[{int(targetB)}]'
        # Add translated target to 'targets'.
        targets = targets + targetB_qasm
    # Check if targetC is not a default value.
    if targetC is not None and targetC > 0:
        # Generate third target qubit.
        targetC_qasm = f', q[{int(targetC)}]'
        # Add translated instruction to 'targets'.
        targets = targets + targetC_qasm

    # Compile gate instruction by combining the gate name with the target specification(s).
    compiled_gate = f'{self} ' + f'{targets};'

    # Check if specified gate is a unitary gate.
    if self == 'unitary':
        # Compile unitary gate.
        compiled_gate = f'{custom_name}({custom_params}) {targets};'
    # Check if gate is declaring a unitary gate.
    elif self == 'gate':
        # Compile unitary gate declaration.
        compiled_gate = f'gate {custom_name}({custom_params}) {targets};'
    # Check if gate is declaring an opaque gate.
    elif self == 'opaque':
        # Compile opaque gate declaration.
        compiled_gate = f'opaque {custom_name}({custom_params}) {targets};'
    elif self in angle_gates:
        compiled_gate = f'{self} ({angle}) {targets};'

    # Return compiled gate.
    return compiled_gate


def measurement(qreg=int(0),
                creg=int(0)):
    """Generate QASM that takes a measurement from a qubit and stores it in a classical register.

    Args:
        qreg(int): Number of the Qubit to measure. (default 0)
        creg(int): Number of the Classical Register to store the measurement to. (default 1)
    Returns:
        str: Generated QASM containing measurement instruction."""
    # Ensure Integer Variables Have Correct Types
    if qreg is not None:
        qreg = int(qreg)

    if creg is not None:
        creg = int(creg)

    # Generate a measurement argument for QASM 2.0.
    meas_str = f'measure q[{str(qreg)}] -> c[{str(creg)}];'
    # Return generated measurement argument.
    return meas_str


def if_statement(creg_name=str('c'),
                 operator=str('=='),
                 creg_val=int(0),
                 gate_name=str('x'),
                 targetA=None,
                 targetB=None,
                 targetC=None,
                 Utheta=None,
                 Uphi=None,
                 Ulambda=None,
                 custom_name=None,
                 custom_params=None):
    """Generate a gate controlled by a classical if statement as a QASM string from specified parameters.

        Args:
            creg_name(str): Classical register to run if statement against. (default 'c')
            operator(str): Operator to compare values with. (default str('=='))
            creg_val(int): Value to compare with creg_name. (default int(0))
            gate_name(str): The name used to represent the gate in QASM. For example, a Hadamard Gate is 'h'. (default str('h'))
            targetA(int): First target qubit. (default None)
            targetB(int): Second target qubit. (default None)
            targetC(int): Third target qubit. (default None)
            Utheta(float): Theta value for U-gates. (default None)
            Uphi(float): Phi value for U-gates. (default None)
            Ulambda(float): Lambda value for U-gates. (default None)
            custom_name(str): Name for user-defined opaque gate declarations, unitary gate declarations, and user-defined unitary gates. (default None)
            custom_params(str): Parameters for user-defined opaque gate declarations, unitary gate declarations, and user-defined unitary gates. (default None)
        Returns:
            str: A string object containing the specified gate as QASM."""

    # Ensure Variables Have Correct Types
    creg_name = str(creg_name)
    operator = str(operator)
    creg_val = str(int(creg_val))
    gate_name = str(gate_name)
    if targetA is not None:
        targetA = str(int(targetA))
    if targetB is not None:
        targetB = str(int(targetB))
    if targetC is not None:
        targetC = str(int(targetC))
    if Utheta is not None:
        Utheta = str(float(Utheta))
    if Uphi is not None:
        Uphi = str(float(Uphi))
    if Ulambda is not None:
        Ulambda = str(float(Ulambda))
    if custom_name is not None:
        custom_name = str(custom_name)
    if custom_params is not None:
        custom_params = str(custom_params)

    # Compile gate to apply if statement is fulfilled
    compiled_gate = gate(gate_name, targetA, targetB,
                         targetC, Utheta, Uphi, Ulambda,
                         custom_name, custom_params)
    # Compile if statement
    if_str = f'if ({creg_name}{operator}{creg_val}) {compiled_gate}'
    # Return compiled if statement
    return if_str
