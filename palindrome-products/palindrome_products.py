def smallest(min_factor, max_factor):
    return extreme(min_factor, max_factor)


def largest(min_factor, max_factor):
    return extreme(min_factor, max_factor, step=-1)


def extreme(min_factor, max_factor, step=1):
    if max_factor < min_factor:
        raise ValueError("unordered factors")
    # palindrome can only be in the range of min_factor^2 and max_factor^2
    for total in range(2 * min_factor, 2 * max_factor + 1)[::step]:
        start, stop = ((total + 1) // 2, max_factor) if step < 0 else (min_factor, total // 2)
        for a in range(start, stop + 1):
            number = a * (total - a)
            if is_palindrome(number):
                a, b = (a, total - a)[::step]
                factors = [[k, number // k] for k in range(a, b + 1) if number % k == 0]
                return number, factors
    return None, []


def is_palindrome(number):
    stg = str(number)
    return stg == stg[::-1]