from qbitkit.anneal import embed as __embed__


def from_bqm(bqm=None):
    """Convert a given BQM into a QUBO.

    Args:
        bqm(dimod.binary_quadratic_model.BinaryQuadraticModel): A BQM to convert into a QUBO. (default None)
    Returns:
        tuple: A tuple containing the QUBO converted from the specified BQM.
        offset: calculated offset"""
    qubo, offset = bqm.to_qubo()
    return qubo, offset


class Solve:
    def sampler(self=None,
                sampler=None,
                shots=int(1000),
                auto_embed=True):
        """Solves a given QUBO using a given D-Wave Sampler.

        Args:
            self(tuple): The QUBO to solve. (default None)
            sampler(dimod.meta.SamplerABCMeta): The D-Wave sampler to use when solving the given QUBO. (default None)
            shots(int): A positive integer describing the number of shots. Can not be higher than 10000. (default 1000)
            auto_embed(bool): Whether or not to automatically embed the QUBO to the given sampler. (default True)
        Returns:
            dict: a dictionary containing the results from the sampler."""


        embedded_sampler = __embed__.qubo(sampler,
                                          self)
        result = embedded_sampler.sample(self,
                                         num_reads=shots)
        return result
