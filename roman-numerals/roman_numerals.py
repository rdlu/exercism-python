numerals_map = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I"
}


def roman(number: int) -> str:
    """Converts a integer Number to a string Roman Numeral"""
    if number < 0 or number > 3999:
        raise ValueError("Value must be in the range 0 - 3999")
    result = ''
    for value, numeral in numerals_map.items():
        while number >= value:
            number -= value
            result += numeral
    return result
