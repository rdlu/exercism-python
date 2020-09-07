from typing import List

def sum_of_multiples(limit: int, factors: List[int]) -> int:
    """Sum of Multiples

	Args:
        limit: the limit
	    factors: a list of numbers to find multiples of

	Returns: 
        the sum of all multiples of the factors up to, but not including the limit
	"""
    # set comprehension (not a list, to avoid repeated nums)
    return sum({ i for m in factors if m != 0
        for i in range(m, limit, m) })
