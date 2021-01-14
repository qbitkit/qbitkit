import dwavebinarycsp as _dbc

def new(vartype='BINARY'):
  dbc = _dbc.ConstraintSatisfactionProblem(vartype)
  return dbc
class convert:
    def to_bqm(self):
        bqm = _dbc.stitch(self)
        return bqm
    def to_ising(self):
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