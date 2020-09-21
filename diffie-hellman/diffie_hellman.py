from secrets import choice


def private_key(p: int) -> int:
    return choice(range(2, p))


def public_key(p: int, g: int, our_private: int) -> int:
    # A = g**a mod p
    return pow(g, our_private, p)


def secret(p: int, their_public: int, our_private: int) -> int:
    # s = B**a mod p
    return pow(their_public, our_private, p)
