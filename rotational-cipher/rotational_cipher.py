def rotate(text: str, key: int) -> str:
    plain = 'abcdefghijklmnopqrstuvwxyz'
    rotated = rotate_left(plain, key)
    return text.translate(str.maketrans(plain+plain.upper(), rotated+rotated.upper()))

def rotate_left(l: list, n: int) -> list:
    if not l: return l
    rotations = n % len(l)
    return l[rotations:] + l[:rotations]

# not used, just to keep in mind
def rotate_right(l: list, n: int) -> list:
    if not l: return l
    ### Optimization ###
    # if n > len(l), rotate only necessary with
    # module of the division
    rotations = n % len(l)
    return l[-rotations:] + l[:-rotations]
