# research: https://iq.opengenus.org/difference-between-square-of-sum-and-sum-of-squares/
def square_of_sum(n: int) -> int:
    return (n * (n+1) // 2) ** 2

def sum_of_squares(n: int) -> int:
    return n * (n+1) * (2*n+1) // 6

def difference_of_squares(n: int) -> int:
    return square_of_sum(n) - sum_of_squares(n)
