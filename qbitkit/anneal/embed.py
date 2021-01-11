from dwave.system.composites import EmbeddingComposite as _ec
def composite(sampler=None):
    EmbeddingCompositeSampler = _ec(sampler)
    return EmbeddingCompositeSampler