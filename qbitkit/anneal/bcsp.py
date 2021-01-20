import dwavebinarycsp as _dbc


def new(self='BINARY'):
    """Create an empty constraint satisfaction problem.

    Args:
        self(dimod.vartype): A string describing the variable type (either SPIN or BINARY) (default 'BINARY')
    Returns:
        dwavebinarycsp.ConstraintSatisfactionProblem: An empty constraint satisfaction problem."""
    dbc = _dbc.ConstraintSatisfactionProblem(self)
    return dbc


class Convert:
    def to_bqm(self):
        """Stitch a given Constraint Solving Problem into a BQM.

        Args:
            self(dwavebinarycsp.ConstraintSatisfactionProblem): The Constraint Solving Problem to stitch into a BQM.
        Returns:
            dimod.binary_quadratic_model.BinaryQuadraticModel: BQM stitched together from the given Constraint Solving Problem.
"""
        bqm = _dbc.stitch(self)
        return bqm

    def to_ising(self):
        """Convert a given Constraint Solving Problem to an Ising.

        Args:
            self(dwavebinarycsp.ConstraintSatisfactionProblem): The Constraint Solving Problem to convert to an Ising.
        Returns:
            tuple: the specified Constraint Solving Problem expressed as an Ising."""
        bqm = convert.to_bqm(self)
        ising = bqm.to_ising()
        return ising

    def to_qubo(self):
        """Convert a given Constraint Solving Problem to a QUBO.

        Args:
            self(dwavebinarycsp.ConstraintSatisfactionProblem): The Constraint Solving Problem to convert to a QUBO.
        Returns:
            tuple: the specified CSP converted to a QUBO."""
        bqm = convert.to_bqm(self)
        qubo = bqm.to_qubo()
        return qubo
