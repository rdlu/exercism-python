def rotate(text: str, key: int) -> str:
    plain = 'abcdefghijklmnopqrstuvwxyz'
    rotated = rotate_left(plain, key)
    plain_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rotated_up = rotate_left(plain_up, key)
    return text.translate(str.maketrans(plain+plain_up, rotated+rotated_up))

def rotate_left(l: list, n: int):
    if not l: return l
    rotations = n % len(l)
    return l[rotations:] + l[:rotations]

# not used, just to keep in mind
def rotate_right(l: list, n: int):
    if not l: return l
    ### Optimization ###
    # if n > len(l), rotate only necessary with
    # module of the division
    rotations = n % len(l)
    return l[-rotations:] + l[:-rotations]
