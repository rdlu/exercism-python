def is_valid(isbn: str) -> bool:
    # filter nums, convert to list of int
    l = [int(x) for x in filter(str.isnumeric, isbn)]
    # handle the edge case: X
    if isbn and isbn[-1] == 'X': l.append(10)
    # check len and sum the product of digits x position
    return len(l) == 10 and sum([l[10-i] * i for i in range(1,11)]) % 11 == 0
