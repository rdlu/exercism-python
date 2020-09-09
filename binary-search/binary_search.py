from typing import List

def find(search_list: List[int], value: int) -> int:
    l = 0
    r = len(search_list) - 1
    while l <= r:
        m = (l + r) // 2
        if search_list[m] < value:
            l = m + 1
        elif search_list[m] > value:
            r = m - 1
        else:
            return m
    raise ValueError(f"{value} not found in {search_list}")
