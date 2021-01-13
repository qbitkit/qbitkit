def from_bqm(bqm=None):
    ising = bqm.to_ising()
    return ising