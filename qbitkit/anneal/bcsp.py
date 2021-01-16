import dwavebinarycsp as _dbc

def new(vartype='BINARY'):
  dbc = _dbc.ConstraintSatisfactionProblem(vartype)
  return dbc
class convert:
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