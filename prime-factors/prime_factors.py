from typing import List


def factors(value: int) -> List[int]:
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
