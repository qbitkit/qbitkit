import dwavebinarycsp as _dbc
def new(vartype='BINARY'):
  dbc = _dbc.ConstraintSatisfactionProblem(vartype)
  return dbc
class convert:
    def to_qubo(self):
        qubo = self.to_qubo()
        return qubo