def distance(strand_a, strand_b):
    counter = 0
    for idx, val in enumerate(strand_a):
        if val != strand_b[idx]:
            counter += 1
    return counter