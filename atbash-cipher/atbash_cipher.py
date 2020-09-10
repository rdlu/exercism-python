from string import ascii_lowercase, punctuation, whitespace

reverse_ci = ascii_lowercase[::-1]
trans_engine = str.maketrans(ascii_lowercase, reverse_ci, punctuation+whitespace)

def encode(plain_text: str) -> str:
    return _chunk_text(_translate(plain_text))


def decode(ciphered_text: str) -> str:
    return _translate(ciphered_text)

def _translate(text: str) -> str:
    return text.lower().translate(trans_engine)

def _chunk_text(text: str, size: int = 5) -> str:
    if len(text) <= size:
        return text
    return text[:size] + " " + _chunk_text(text[size:])
