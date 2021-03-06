from qbitkit.anneal import embed as __embed__


def from_bqm(bqm=None):
    """Convert a given BQM into a QUBO.

    Args:
        bqm(dimod.binary_quadratic_model.BinaryQuadraticModel): A BQM to convert into a QUBO. (default None)
    Returns:
        tuple: A tuple containing the QUBO converted from the specified BQM.
        offset: calculated offset"""
    # Convert the BQM to a QUBO and an offset.
    qubo, offset = bqm.to_qubo()
    # Return both the QUBO and the offset.
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
        # Check if auto-embedding is enabled.
        if auto_embed is True:
            # Embed the QUBO to the given sampler
            embedded_sampler = __embed__.qubo(sampler,
                                              self)
            # Sample using the embedded sampler.
            result = embedded_sampler.sample_qubo(self,
                                                  num_reads=shots)
        # Check if auto-embedding is disabled.
        elif auto_embed is False:
            # Sample using the given sampler.
            result = sampler.sample_qubo(self,
                                         num_reads=shots)
        # Return results from sampling.
        return result
