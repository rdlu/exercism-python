from typing import List

def flatten(iterable: List) -> List:
    flat = []
    while iterable:
        el = iterable.pop()
        if type(el) == list:
            iterable.extend(el)
        else:
            flat.append(el)
    return sorted(flat)
