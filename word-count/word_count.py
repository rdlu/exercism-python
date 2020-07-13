from collections import Counter
from string import punctuation

def count_words(sentence):
    # string.punctuation without single '
    trans_regex = r"""!"#$%&()*+,-./:;<=>?@[\]^_`{|}~"""
    trans_engine = str.maketrans(trans_regex, ' '*len(trans_regex))
    words = str.translate(sentence, trans_engine).lower().split()
    words = [word.strip('\'') for word in words]
    return dict(Counter(words))
