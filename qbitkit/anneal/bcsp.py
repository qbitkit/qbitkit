import dwavebinarycsp as __dbc__
from qbitkit.anneal import embed as __embed__


def new(self='BINARY'):
    """Create an empty constraint satisfaction problem.

    Args:
        self(dimod.vartype): A string describing the variable type (either SPIN or BINARY) (default 'BINARY')
    Returns:
        dwavebinarycsp.ConstraintSatisfactionProblem: An empty constraint satisfaction problem."""
    dbc = __dbc__.ConstraintSatisfactionProblem(self)
    return dbc


class Convert:
    def to_bqm(self=None):
        """Stitch a given Constraint Solving Problem into a BQM.

        Args:
            self(dwavebinarycsp.ConstraintSatisfactionProblem): The Constraint Solving Problem to stitch into a BQM. (default None)
        Returns:
            dimod.binary_quadratic_model.BinaryQuadraticModel: BQM stitched together from the given Constraint Solving Problem.
"""
        bqm = __dbc__.stitch(self)
        return bqm

    def to_ising(self=None):
        """Convert a given Constraint Solving Problem to an Ising.

        Args:
            self(dwavebinarycsp.ConstraintSatisfactionProblem): The Constraint Solving Problem to convert to an Ising. (default None)
        Returns:
            tuple: the specified Constraint Solving Problem expressed as an Ising."""
        bqm = Convert.to_bqm(self)
        ising = bqm.to_ising()
        return ising

    def to_qubo(self=None):
        """Convert a given Constraint Solving Problem to a QUBO.

        Args:
            self(dwavebinarycsp.ConstraintSatisfactionProblem): The Constraint Solving Problem to convert to a QUBO. (default None)
        Returns:
            tuple: the specified CSP converted to a QUBO."""
        bqm = Convert.to_bqm(self)
        qubo = bqm.to_qubo()
        return qubo


class Solve:
    def solve(self=None,
              sampler=None,
              shots=int(1000)):
        """Solves a given Constraint Satisfaction Problem using a given D-Wave Sampler.

        Args:
            self(dwavebinarycsp.ConstraintSatisfactionProblem): The Constraint Satisfaction Problem to solve. (default None)
            sampler(dimod.meta.SamplerABCMeta): The D-Wave sampler to use when solving the given CSP. (default None)
            shots(int): A positive integer describing the number of shots. Can not be higher than 10000. (default 1000)
        Returns:
            dict: a dictionary containing the results from the sampler."""
        bqm = Convert.to_bqm(self)
        embedded_sampler = __embed__.bqm(sampler,
                                         bqm)
        result = embedded_sampler.sample(bqm,
                                         num_reads=shots)
        return result
