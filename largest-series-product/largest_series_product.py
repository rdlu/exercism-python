from operator import mul
from functools import reduce


def largest_product(series: str, size: int) -> int:
    """Largest Product takes a series of digits
    and return the largest product within groups of size n"""
    series_slices = slices(series, size)
    return max(reduce(lambda acc, digit: mul(acc, int(digit)), subseries, 1)
               for subseries in series_slices)


def slices(series: str, length: int) -> list:
    """slices - a.k.a Grouped Slices -

    :param series: str:
    :param length: int:
    :returns: A list of grouped slices of n length from a string

    """
    if length not in range(len(series) + 1):
        raise ValueError(f'Length {length} not in range for this series')
    return [series[tailcut - length:tailcut] for tailcut in range(length, len(series) + 1)]
