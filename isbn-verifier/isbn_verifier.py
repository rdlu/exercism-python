def is_valid(isbn: str) -> bool:
    l = [int(x) for x in filter(str.isnumeric, isbn)]
    if isbn and isbn[-1] == 'X': l.append(10)
    return len(l) == 10 and sum([l[10-i] * i for i in range(1,11)]) % 11 == 0
