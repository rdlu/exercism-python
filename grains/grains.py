def square(number: int) -> int:
    # not in range(1, 65) is a possibility
    if not 1 <= number <= 64:
        raise ValueError(f'Number {number} outside of the valid range (1-64)')
    # return 2 ** (number - 1) using bitshift
    return 1 << number - 1


def total() -> int:
    # it faster to just to hardcode  the 2 ** 64 - 1 number
    return sum(square(i) for i in range(1, 65))
