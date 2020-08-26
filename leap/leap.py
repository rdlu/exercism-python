def leap_year(year: int) -> bool:
    # discarding majority of years right away (short circuit and)
    # then subject the candidate to the edge cases
    return year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0)

