# from https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem
from typing import List, Dict


def maximum_value(maximum_weight: int, items: List[Dict]) -> int:
    memo = [[0 for j in range(maximum_weight + 1)] for i in range(0, len(items) + 1)]

    for n in range(1, len(items) + 1):
        for w in range(1, maximum_weight + 1):
            calculate_max(n, w, items, memo)

    return memo[len(items)][maximum_weight]


def calculate_max(n: int, w: int, items: List[Dict], memo: List[List[int]]) -> int:
    if n == 0 or w == 0:
        memo[n][w] = 0

    wi = items[n - 1]['weight']
    vi = items[n - 1]['value']
    if wi <= w:
        memo[n][w] = max(vi + memo[n - 1][w - wi], memo[n - 1][w])
    else:
        memo[n][w] = memo[n - 1][w]

    return memo[n][w]
