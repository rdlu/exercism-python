def slices(series: str, length: int) -> list:
    """slices - a.k.a Grouped Slices -

    :param series: str:
    :param length: int:
    :returns: A list of grouped slices of n length from a string

    """
    if length not in range(1, len(series) + 1):
        raise ValueError(f'Length {length} not in range for this series')
    return [series[tailcut - length:tailcut] for tailcut in range(length, len(series) + 1)]
