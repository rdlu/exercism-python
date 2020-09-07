from typing import List

def sum_of_multiples(limit: int, multiples: List[int]) -> int:
    return sum([i for m in multiples for i in range(limit) if i % m == 0])
