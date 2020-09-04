"""slices 

A.k.a - Grouped Slices -

Returns:
    A list of grouped slices of n length from a string
"""
def slices(series: str, length: int) -> list:
    if length not in range(1, len(series)+1): 
        raise ValueError(f'Length {length} not in range for this series')
    return [series[tailcut-length:tailcut] for tailcut in range(length, len(series)+1)]
