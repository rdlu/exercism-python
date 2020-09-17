from typing import List


from itertools import cycle


def factors(number: int) -> List[int]:
    # stole from: https://exercism.io/tracks/python/exercises/prime-factors/solutions/f524e783960d5b1b1fddb271
    """Factors returns all clean divisors of a number"""
    return list(generate_prime_factors(number))


def generate_prime_factors(number: int):
    for factor in generate_factor_candidates():
        if factor ** 2 > number:
            if number != 1:
                yield number
            return
        while not number % factor:
            yield factor
            number /= factor


def generate_factor_candidates():
    yield 2
    yield 3
    yield 5
    candidate = 1
    for jump in cycle([6, 4, 2, 4, 2, 4, 6, 2]):
        candidate += jump
        yield candidate


def naive_factors(value: int) -> List[int]:
    """Factors returns all clean divisors of a number"""
    factors = []
    divisor = 2
    current_value = value
    while current_value > 1:
        remainder, quotient = divmod(current_value, divisor)
        if quotient == 0:
            factors.append(divisor)
            current_value = remainder
        else:
            divisor += 1
    return factors