def equilateral(sides):
    valid, unique_sides = is_valid(sides)
    if valid and unique_sides == 1:
        return True

    return False


def isosceles(sides):
    valid, unique_sides = is_valid(sides)
    if valid and unique_sides in [1, 2]:
        return True

    return False


def scalene(sides):
    valid, unique_sides = is_valid(sides)
    if valid and unique_sides == 3:
        return True

    return False


def is_valid(sides):
    if len(sides) != 3:
        return False, 0
    a, b, c = sides
    if a + b > c and a + c > b and b + c > a:
        return True, len(set(sides))

    return False, len(set(sides))
