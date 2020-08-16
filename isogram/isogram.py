from collections import Counter

def is_isogram(word: str) -> bool:
    counter = Counter(word.lower())
    del counter['-']
    del counter[' ']
    return all([i < 2 for i in counter.values()])
