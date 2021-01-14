import dwavebinarycsp as _dbc

def new(vartype='BINARY'):
  dbc = _dbc.ConstraintSatisfactionProblem(vartype)
  return dbc
class convert:
    def to_qubo(self):
        """Convert a given Constraint Solving Problem to a QUBO.

        Args:
            self(dwavebinarycsp.ConstraintSatisfactionProblem): The Constraint Solving Problem to convert to a QUBO.
        Returns:
            tuple: the specified CSP converted to a QUBO."""
        qubo = self.to_qubo()
        return qubo
    def to_bqm(self):
        bqm = _dbc.stitch(self)
        return bqm
    def to_ising(self):
        ising = self.to_ising()
        return ising