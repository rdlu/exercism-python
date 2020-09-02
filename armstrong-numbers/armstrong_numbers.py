def is_armstrong_number(number: int) -> bool:
    digits = str(number)
    return sum(int(char) ** len(digits) for char in digits) == number
