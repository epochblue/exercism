def distance(strand_a, strand_b):
    """Calculate the Hamming difference between two DNA strands."""
    pairs = zip(strand_a, strand_b)
    return len(filter(lambda p: p[0] != p[1], pairs))

