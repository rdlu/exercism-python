from collections import Counter

def is_pangram(sentence: str) -> bool:
    filtered_sentence = filter(str.isalpha, sentence.lower())
    return len(Counter(filtered_sentence).keys()) == 26
