import re

def decode(data: str) -> str:
    # uses the length to "multiply" the char
    decompress = lambda match: str(int(match.groups(0)[0]) * match.groups(0)[1])
    # matches a digit-non_digit
    return re.sub(r"(\d+)([^0-9])", decompress, data)

def encode(data: str) -> str:
    # uses the position delta to determine the size
    compress = lambda match: f"{match.end() - match.start()}{match.groups(0)[0]}"
    # \1+ matches the same text as most recently matched THAT has more than 1
    # otherwise stays untouched
    return re.sub(r"(.)\1+", compress, data)
