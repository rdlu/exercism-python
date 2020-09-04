def slices(series: str, length: int) -> list:
    if length not in range(1, len(series)+1): raise ValueError('Value not in range')
    return [series[tailcut-length:tailcut] for tailcut in range(length, len(series)+1)]
