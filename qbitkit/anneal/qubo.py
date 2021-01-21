def from_bqm(bqm=None):
    """Convert a given BQM into a QUBO.

    Args:
        bqm(dimod.binary_quadratic_model.BinaryQuadraticModel): A BQM to convert into a QUBO. (default None)
    Returns:
        tuple: A tuple containing the QUBO converted from the specified BQM.
        offset: calculated offset"""
    qubo, offset = bqm.to_qubo()
    return qubo, offset