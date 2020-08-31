from itertools import groupby

def decode(data):
    decoded = ''
    count = ''
    for char, _group in groupby(data):
        if char.isnumeric():
            count += str(char)
        elif not count:
            decoded = str(char)
        else:
            decoded += str(int(count) * char)
            count = ''
    return decoded

def encode(data: str) -> str:
    encoded = ''

    for char, group in groupby(data):
        section_qty = sum(1 for _ in group)
        if section_qty > 1:
            encoded += f"{section_qty}{char}"
        else:
            encoded += char
    return encoded
