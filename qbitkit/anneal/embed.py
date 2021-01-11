from dwave.system.composites import EmbeddingComposite as _ec
def composite(sampler=None):
    """Returns EmbeddingComposite based on specified sampler.

    Args:
        sampler (dwave.system.samplers): Any Sampler compatible with the D-Wave Ocean SDK. (default None)
    Returns:
        dwave.system.composites.EmbeddingComposite: An EmbeddingComposite based on the specified sampler."""
    EmbeddingCompositeSampler = _ec(sampler)
    return EmbeddingCompositeSampler