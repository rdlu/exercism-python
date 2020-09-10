from string import ascii_lowercase, ascii_uppercase, punctuation, whitespace

reverse_ci = ascii_lowercase[::-1]
trans_engine = str.maketrans(ascii_lowercase + ascii_uppercase,
                             reverse_ci + reverse_ci,   # + to handle uppercase
                             punctuation + whitespace)  # chars to remove


def encode(plain_text: str) -> str:
    """Encodes a text using Atbash Cipher"""
    return _chunk_text(_translate(plain_text))


def decode(ciphered_text: str) -> str:
    """Decodes a text using Atbash Cipher"""
    return _translate(ciphered_text)


def _translate(text: str) -> str:
    return text.translate(trans_engine)


def _chunk_text(text: str, size: int = 5) -> str:
    if len(text) <= size:
        return text
    return text[:size] + " " + _chunk_text(text[size:])
