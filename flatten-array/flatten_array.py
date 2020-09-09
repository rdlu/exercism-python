from collections.abc import Iterable

def flatten(iterable: Iterable) -> Iterable:
    flat = []
    for el in iterable:
        if isinstance(el, Iterable):
            flat.extend(flatten(el))
        elif el is not None:
            flat.append(el)
    return flat
