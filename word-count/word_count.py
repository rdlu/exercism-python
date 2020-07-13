from collections import Counter
from string import punctuation

def count_words(sentence):
    words = sentence.replace(',', ' ').replace('_', ' ').lower().split()
    words = [word.strip(punctuation) for word in words]
    return dict(Counter(words))
