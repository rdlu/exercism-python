from functools import lru_cache
from math import gcd
from string import ascii_lowercase

alphabet = ascii_lowercase
m = len(alphabet)


def validate_a(a: int):
    if gcd(a, m) > 1:
        raise ValueError("a and m must be coprime.")


def ord_(char):
    return alphabet.index(char)


def chr_(num):
    return alphabet[num]


@lru_cache
def mmi(a: int) -> int:
    """Returns the result of a ** -1, using integers only"""
    for n in range(1, m):
        if (a * n) % m == 1:
            return n
    return 1


def encode(plain_text: str, a: int, b: int) -> str:
    """Encode the text using affine cipher"""
    validate_a(a)

    def cipher(char: str) -> str:
        if char in alphabet:
            return chr_((a * ord_(char) + b) % m)
        if char.isdigit():
            return char
        return ''

    return chunk_text(
        ''.join(cipher(char) for char in plain_text.lower().replace(' ', '')))


def chunk_text(text: str, size: int = 5) -> str:
    """Utility function to put spaces on strings at each size"""
    if len(text) <= size:
        return text
    return text[:size] + " " + chunk_text(text[size:])


def decode(ciphered_text: str, a: int, b: int):
    """Encode the text using affine cipher"""
    validate_a(a)

    def decipher(char: str) -> str:
        if char in alphabet:
            num = mmi(a) * (ord_(char) - b) % m
            return chr_(num)
        if char.isdigit():
            return char
        return ''

    return ''.join(decipher(char)
                   for char in ciphered_text.lower().replace(' ', ''))
