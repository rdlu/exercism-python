# not used
def square_of_sum(n: int) -> int:
    return sum(range(1, n+1)) ** 2

# not used
def sum_of_squares(n: int) -> int:
    return sum(i**2 for i in range(1, n+1))

# research: https://iq.opengenus.org/difference-between-square-of-sum-and-sum-of-squares/
def difference_of_squares(n: int) -> int:
    sum_1 = n * (n+1) // 2
    sum_2 = n * (n+1) * (2*n+1) // 6
    return sum_1 * sum_1 - sum_2
