def score(x, y):
    radius = (x**2 + y**2) ** 0.5
    if radius <= 1:
        return 10

    if radius <= 5:
        return 5

    if radius <= 10:
        return 1

    return 0
