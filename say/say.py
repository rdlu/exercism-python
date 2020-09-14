spelling = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

ranges = [
    (1e9, "billion"),
    (1e6, "million"),
    (1e3, "thousand"),
    (1e2, "hundred"),
]


def say(number: int) -> str:
    if number < 0 or number >= 1e12:
        raise ValueError('invalid number')

    # direct conversion cases
    if number < 20 or (number < 100 and number % 10 == 0):
        return spelling[number]

    # decimals, almost close
    if number < 100:
        return say_range(number, 10, say(number % 10), '-')

    for r in ranges:
        if number >= r[0]:
            return say_range(number, r[0], r[1])


def say_range(n: int, limit: int, word: str, separator: str = ' ') -> str:
    if n % limit == 0:
        return f"{say(n // limit)}{separator}{word}"
    else:
        return f"{say(n // limit * limit)}{separator}{say(n % limit)}"
