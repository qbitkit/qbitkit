from dwave.plugins.qiskit import DWaveMinimumEigensolver as __dwmes__
from qbitkit.anneal.embed import composite as __ec__


class Solve:
    def sampler(self=None,
                sampler=None,
                shots=int(1000)):
        emb_samp = __ec__(sampler)
        sample = __dwmes__(self,
                           sampler=emb_samp,
                           num_reads=shots)
        return sample
