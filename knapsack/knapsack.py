# from https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem
from typing import List, Dict


def maximum_value(maximum_weight: int, items: List[Dict]) -> int:
    memo = [[0 for _ in range(maximum_weight + 1)] for _ in range(0, len(items) + 1)]

    for n in range(1, len(items) + 1):
        for w in range(1, maximum_weight + 1):
            memo[n][w] = calculate_value(n, w, items, memo)

    return memo[len(items)][maximum_weight]


def calculate_value(n: int, w: int, items: List[Dict], memo: List[List[int]]) -> int:
    wi = items[n - 1]['weight']
    vi = items[n - 1]['value']
    return max(vi + memo[n - 1][w - wi], memo[n - 1][w]) \
        if wi <= w else memo[n - 1][w]
