# combinations_with_replacement is greedy and order-stable, will use to generate candidates
# https://docs.python.org/3.8/library/itertools.html#itertools.combinations_with_replacement
from itertools import combinations_with_replacement as generate_candidate_list


def find_fewest_coins(coins: list, target: int) -> list:
    if target == 0:
        return []
    if target < min(coins):
        raise ValueError(f'Can\'t give change for #{target}')

    for i in range(1, target // min(coins) + 1):
        for candidate_list in generate_candidate_list(sorted(coins), i):
            if sum(candidate_list) == target:
                return list(candidate_list)

    raise ValueError('No change possible')
