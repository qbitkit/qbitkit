def from_bqm(bqm=None):
    """Convert a given BQM into an Ising.

    Args:
        bqm(dimod.binary_quadratic_model.BinaryQuadraticModel): A BQM to convert into an Ising. (default None)
    Returns:
        tuple: A tuple containing the Ising converted from the specified BQM."""
    ising = bqm.to_ising()
    return ising