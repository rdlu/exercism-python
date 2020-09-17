import string

alphabet = string.ascii_lowercase


def encode(plain_text: str, a: int, b: int) -> str:
    """Encode the text using affine cipher"""
    return chunk_text(
        ''.join(affine_encode(char, a, b)
                for char in plain_text.lower().replace(' ', '')))


def affine_encode(char: str, a: int, b: int) -> str:
    """Encodes a single char using affine encode formula
        Formula: E(x) = (ax + b) mod m
    """
    if char in alphabet:
        return alphabet[(a * alphabet.index(char) + b) % len(alphabet)]
    if char in string.digits:
        return char
    return ''


def chunk_text(text: str, size: int = 5) -> str:
    if len(text) <= size:
        return text
    return text[:size] + " " + chunk_text(text[size:])


def decode(ciphered_text: str, a: int, b: int):
    return ''.join(affine_decode(char, a, b)
                   for char in ciphered_text.lower().replace(' ', ''))


def affine_decode(char: str, a: int, b: int) -> str:
    """Decodes a single char using affine decode formula
        D(y) = a^-1(y - b) mod m
    """
    if char in alphabet:
        num = int(((a ** -1) * (alphabet.index(char) - b)) % len(alphabet))
        return alphabet[num]
    if char in string.digits:
        return char
    return ''
