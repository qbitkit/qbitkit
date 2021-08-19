import dwavebinarycsp as __dbc__
from qbitkit.anneal import embed as __embed__


def new(self='BINARY'):
    """Create an empty constraint satisfaction problem.

    Args:
        self(dimod.vartype): A string describing the variable type (either SPIN or BINARY) (default 'BINARY')
    Returns:
        dwavebinarycsp.ConstraintSatisfactionProblem: An empty constraint satisfaction problem."""
    # Return an empty CSP.
    return __dbc__.ConstraintSatisfactionProblem(self)


class Convert:
    def to_bqm(self=None):
        """Stitch a given Constraint Solving Problem into a BQM.

        Args:
            self(dwavebinarycsp.ConstraintSatisfactionProblem): The Constraint Solving Problem to stitch into a BQM. (default None)
        Returns:
            dimod.binary_quadratic_model.BinaryQuadraticModel: BQM stitched together from the given Constraint Solving Problem.
"""
        # Return the BQM.
        return __dbc__.stitch(self)

    def to_ising(self=None):
        """Convert a given Constraint Solving Problem to an Ising.

        Args:
            self(dwavebinarycsp.ConstraintSatisfactionProblem): The Constraint Solving Problem to convert to an Ising. (default None)
        Returns:
            tuple: the specified Constraint Solving Problem expressed as an Ising."""
        # Return the Ising converted from given CSP.
        return Convert.to_bqm(self).to_ising()

    def to_qubo(self=None):
        """Convert a given Constraint Solving Problem to a QUBO.

        Args:
            self(dwavebinarycsp.ConstraintSatisfactionProblem): The Constraint Solving Problem to convert to a QUBO. (default None)
        Returns:
            tuple: the specified CSP converted to a QUBO."""
        # Return the QUBO converted from given CSP.
        return Convert.to_bqm(self).to_qubo()


class Solve:
    def sampler(self=None,
                sampler=None,
                shots=int(1000)):
        """Solves a given Constraint Satisfaction Problem using a given D-Wave Sampler.

        Args:
            self(dwavebinarycsp.ConstraintSatisfactionProblem): The Constraint Satisfaction Problem to solve. (default None)
            sampler(dimod.meta.SamplerABCMeta): The D-Wave sampler to use when solving the given CSP. (default None)
            shots(int): A positive integer describing the number of shots. Can not be higher than 10000. (default 1000)
        Returns:
            dict: a dictionary containing the results from the sampler."""
        # Return the result from sampling.
        return __embed__.bqm(
            sampler,
            sampler.Convert.to_bqm(self)
        ).sample(
            sampler.Convert.to_bqm(self),
            num_reads=shots)
