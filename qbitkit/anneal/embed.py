from dwave.system.composites import EmbeddingComposite as _ec
import minorminer as _mm
from dwave.embedding import embed_qubo
from dwave.embedding import embed_ising as __embed_ising__

def composite(sampler=None):
    """Returns EmbeddingComposite based on specified sampler.

    Args:
        sampler (dwave.system.samplers): Any Sampler compatible with the D-Wave Ocean SDK. (default None)
    Returns:
        dwave.system.composites.EmbeddingComposite: An EmbeddingComposite based on the specified sampler."""
    EmbeddingCompositeSampler = _ec(sampler)
    return EmbeddingCompositeSampler
def qubo(sampler=None,
         qubo=None):
    """Create embedding for a specified sampler from a specified QUBO.

    Args:
        sampler(dimod.meta.SamplerABCMeta): A D-Wave Ocean SDK Sampler.
        qubo(tuple): A tuple containing the QUBO to map onto the given sampler's QPU topology.
    Returns:
        dict: The given QUBO mapped to the given sampler's QPU topology."""
    _, target_edgelist, target_adjacency = sampler.structure
    embedding = _mm.find_embedding(qubo,
                                   target_edgelist)
    qubo_embedded = embed_qubo(qubo,
                               embedding,
                               target_adjacency)
    return qubo_embedded


def ising(sampler=None,
          ising=None):
    """Create embedding for a specified sampler from a specified Ising.

    Args:
        sampler(dimod.meta.SamplerABCMeta): A D-Wave Ocean SDK Sampler.
        ising(tuple): A tuple containing the Ising to map onto the given sampler's QPU topology.
    Returns:
        dict: The given Ising mapped to the given sampler's QPU topology."""
    _, target_edgelist, target_adjacency = sampler.structure
    embedding = _mm.find_embedding(ising,
                                   target_edgelist)
    ising_embedded = __embed_ising__(ising,
                                     embedding,
                                     target_adjacency)
    return ising_embedded
