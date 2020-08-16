def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Different lengths on strands')
    counter = 0
    for l, r in zip(strand_a, strand_b):
        if l != r:
          counter += 1
    return counter