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
    # Create an EmbeddingComposite from the specified sampler.
    EmbeddingCompositeSampler = _ec(sampler)
    # Return the embedded sampler.
    return EmbeddingCompositeSampler


def qubo(sampler=None,
         qubo=None):
    """Create embedding for a specified sampler from a specified QUBO.

    Args:
        sampler(dimod.meta.SamplerABCMeta): A D-Wave Ocean SDK Sampler. (default None)
        qubo(tuple): A tuple containing the QUBO to map onto the given sampler's QPU topology. (default None)
    Returns:
        dict: The given QUBO mapped to the given sampler's QPU topology."""
    # Get the topology data of the D-Wave QPU for the given sampler.
    _, target_edgelist, target_adjacency = sampler.structure
    # Find the embedding based on the given QUBO and the target edges from the topology data..
    embedding = _mm.find_embedding(qubo,
                                   target_edgelist)
    # Create embedding from the QUBO.
    qubo_embedded = embed_qubo(qubo,
                               embedding,
                               target_adjacency)
    # Return the generated embedding.
    return qubo_embedded


def ising(sampler=None,
          ising=None):
    """Create embedding for a specified sampler from a specified Ising.

    Args:
        sampler(dimod.meta.SamplerABCMeta): A D-Wave Ocean SDK Sampler. (default None)
        ising(tuple): A tuple containing the Ising to map onto the given sampler's QPU topology. (default None)
    Returns:
        dict: The given Ising mapped to the given sampler's QPU topology."""
    # Get the topology data of the D-Wave QPU from the given sampler.
    _, target_edgelist, target_adjacency = sampler.structure
    # Find the embedding based on the given Ising and target edges from the topology data.
    embedding = _mm.find_embedding(ising,
                                   target_edgelist)
    # Create embedding from the Ising.
    ising_embedded = __embed_ising__(ising,
                                     embedding,
                                     target_adjacency)
    # Return the generated embedding.
    return ising_embedded


def bqm(sampler=None,
        bqm=None):
    """Create embedding for a specified sampler from a specified BQM.

    Args:
        sampler(dimod.meta.SamplerABCMeta): A D-Wave Ocean SDK Sampler. (default None)
        bqm(dimod.binary_quadratic_model.BinaryQuadraticModel): A tuple containing the BQM to map onto the given sampler's QPU topology. (default None)
    Returns:
        dict: The given BQM mapped to the given sampler's QPU topology."""
    # Get the topology data of the D-Wave QPU from the given sampler.
    _, target_edgelist, target_adjacency = sampler.structure
    # Find the embedding based on the given BQM and target edges from the topology data.
    embedding = _mm.find_embedding(bqm,
                                   target_edgelist)
    # Create embedding from the BQM.
    bqm_embedded = __embed_ising__(bqm,
                                   embedding,
                                   target_adjacency)
    # Return the generated embedding.
    return bqm_embedded
