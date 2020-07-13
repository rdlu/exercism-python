from collections import Counter
import string

def count_words(sentence):
    words = sentence.replace(',', ' ').replace('_', ' ').lower().split()
    words = [word.strip(string.punctuation) for word in words]
    return dict(Counter(words))
