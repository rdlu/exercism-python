from typing import List

def flatten(iterable: List) -> List:
    flat = []
    for el in iterable:
        if isinstance(el, list):
            flat.extend(flatten(el))
        elif el is not None:
            flat.append(el)
    return flat
