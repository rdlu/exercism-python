from typing import List


def slices(series: str, length: int) -> List[List[str]]:
    """Return all substrings of `size`, given a string `s`.
    If `size` is greater than the length of `s`, or less than 1, return an empty list

    :param series: str:
    :param length: int:
    :returns: A list of grouped slices of n length from a string

    """
    if length < 1:
        return []
    return [series[tailcut - length:tailcut] for tailcut in range(length, len(series) + 1)]
