from secrets import choice


def private_key(p):
    return choice(range(2, p))


def public_key(p, g, our_private):
    # A = g**a mod p
    return pow(g, our_private, p)


def secret(p, their_public, our_private):
    # s = B**a mod p
    return pow(their_public, our_private, p)
