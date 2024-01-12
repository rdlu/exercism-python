def score(x, y):
    """Branchless version (avoiding if-then-else) of a scoring function for a darts game."""
    radius = (x**2 + y**2) ** 0.5

    return 5 * (radius <= 1) + 4 * (radius <= 5) + 1 * (radius <= 10)
