from typing import List

def sum_of_multiples(limit: int, multiples: List[int]) -> int:
    # set comprehension (not a list, to avoid repeated nums)
    return sum({ i for m in multiples if m != 0
        for i in range(m, limit, m) })
