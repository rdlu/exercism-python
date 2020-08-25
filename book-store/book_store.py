# just rewrote this: https://exercism.io/tracks/python/exercises/book-store/solutions/736ace5096a74f079343773f0d13ad57
# and made some comments for clarification
# basically we need to simulate different sizes of bundles
# BUT in this case the edge case [3, 5] is known
# so this solution hardcodes that

from collections import Counter

bundle_cost = [0, 800, 1520, 2160, 2560, 3000]

def total(basket: list) -> int:
    books = Counter(basket)
    bundles = []

    while bundle_size := len(books):
        bundles.append(bundle_size)
        books.subtract(books.keys())
        books += Counter() # trick to remove zeroed items

    # edge case for bundle (4,4) is cheaper than bundle (3,5)
    # non scalable: if we add a bundle of 6, for instance, we will have new edge cases
    while 3 in bundles and 5 in bundles:
        bundles.remove(3)
        bundles.remove(5)
        bundles += [4, 4]

    return sum([bundle_cost[size] for size in bundles])