def leap_year(year: int) -> bool:
    # discarding majority of years right away
    if not year % 4 == 0:
        return False
    # now subject the candidate to the edge cases
    if year % 100 == 0 and not year % 400 == 0:
        return False
    return True

