from typing import List
from math import sqrt

def primes(n: int) -> List[int]:
    """Return a list of primes using the Sieve of Eratosthenes"""
    numbers = list(range(n+1))    # using the list of nums to track primes
    last = int(sqrt(n))           # opt: you dont need to look all nums
    for number in numbers[2:last+1]:
        if number == 0:
            continue
        multiple = number * 2     # first multiple
        while multiple <= n:      # iterate multiples
            numbers[multiple] = 0 # mark as non-prime
            multiple += number    # next multiples
    return [x for x in numbers[2:] if x != 0]
