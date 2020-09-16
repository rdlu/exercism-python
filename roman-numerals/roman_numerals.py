# found original using C# at http://www.blackwasp.co.uk/NumberToRoman.aspx
def roman(number: int) -> str:
    """Converts a integer Number to a string Roman Numeral"""
    if number < 0 or number > 3999:
        raise ValueError("Value must be in the range 0 - 3999")
    if number == 0:
        return "N"
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = []
    for i in range(13):
        while number >= values[i]:
            number -= values[i]
            result.append(numerals[i])
    return ''.join(result)
