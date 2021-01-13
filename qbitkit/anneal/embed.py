from dwave.system.composites import EmbeddingComposite as _ec
import minorminer as _mm
from dwave.embedding import embed_qubo

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
    _, target_edgelist, target_adjacency = sampler.structure
    embedding = _mm.find_embedding(qubo,
                                          target_edgelist)
    qubo_embedded = embed_qubo(qubo,
                               embedding,
                               target_adjacency)
    return qubo_embedded