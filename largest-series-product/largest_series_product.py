from math import prod


def largest_product(series: str, size: int) -> int:
    """Largest Series Product from strings

    :param series: str: takes a series of digits
    :param size: int: size of slices / groups / chunks
    :returns: int: the largest product within groups of n size

    """
    series_slices = slices(series, size)
    return max(prod(int(digit) for digit in subseries)
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
