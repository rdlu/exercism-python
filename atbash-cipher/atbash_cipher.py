plain_ci = 'abcdefghijklmnopqrstuvwxyz'
reverse_ci = ''.join(reversed(plain_ci))

def encode(plain_text: str) -> str:
    clean_plain = plain_text.lower().replace(" ", "")
    translated = clean_plain.translate(str.maketrans(plain_ci, reverse_ci))
    return translated


def decode(ciphered_text: str) -> str:
    clean_ciphered = ciphered_text.lower().replace(" ", "")
    translated = clean_ciphered.translate(str.maketrans(reverse_ci, plain_ci))
    return translated
