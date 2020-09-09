from typing import List

def find(search_list: List, value: int) -> int:
    l = 0
    r = len(search_list)
    while l <= r and r > 0:
        m = (l + r) // 2
        if search_list[m] < value:
            l = m + 1
        elif search_list[m] > value:
            r = m - 1
        else:
            return m
    raise ValueError('not found')
