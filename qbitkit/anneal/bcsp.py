import dwavebinarycsp as _dbc
def new(vartype='BINARY'):
  dbc = _dbc.ConstraintSatisfactionProblem(vartype)
  return dbc
class convert:
    def to_qubo(self):
        qubo = self.to_qubo()
        return qubo
    def to_bqm(self):
        bqm = _dbc.stitch(self)
        return bqm
    def to_ising(self):
        ising = self.to_ising()
        return ising