from qbitkit.anneal import embed as __embed__


def from_bqm(bqm=None):
    """Convert a given BQM into an Ising.

    Args:
        bqm(dimod.binary_quadratic_model.BinaryQuadraticModel): A BQM to convert into an Ising. (default None)
    Returns:
        tuple: A tuple containing the Ising converted from the specified BQM."""
    # Convert the BQM to an Ising
    ising = bqm.to_ising()
    # Return Ising
    return ising


class Solve:
    def sampler(self=None,
                sampler=None,
                shots=int(1000),
                auto_embed=True):
        """Solves a given Ising using a given D-Wave Sampler.

        Args:
            self(tuple): The Ising to solve. (default None)
            sampler(dimod.meta.SamplerABCMeta): The D-Wave sampler to use when solving the given Ising. (default None)
            shots(int): A positive integer describing the number of shots. Can not be higher than 10000. (default 1000)
            auto_embed(bool): Whether or not to automatically embed the Ising to the given sampler. (default True)
        Returns:
            dict: a dictionary containing the results from the sampler."""
        # Check if auto-embedding is enabled.
        if auto_embed is True:
            # Embed the Ising on to the D-Wave QPU's topology.
            embedded_sampler = __embed__.ising(sampler,
                                               self)
            # Sample using the embedded sampler.
            result = embedded_sampler.sample_ising(self,
                                                   num_reads=shots)
        # Check if auto-embedding is disabled.
        elif auto_embed is False:
            # Sample the ising equation with the given sampler.
            result = sampler.sample_ising(self,
                                          num_reads=shots)
        # Return the result of sampling the Ising.
        return result
