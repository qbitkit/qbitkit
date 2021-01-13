def from_bqm(bqm=None):
    qubo, offset = bqm.to_qubo()
    return qubo, offset