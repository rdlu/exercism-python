def abbreviate(sentence):
    # string.punctuation without single '
    trans_regex = r"""!"#$%&()*+,-./:;<=>?@[\]^_`{|}~"""
    # compiling a translating engine for faster replace
    trans_engine = str.maketrans(trans_regex, ' '*len(trans_regex))
    words = str.translate(sentence, trans_engine).lower().split()
    words = [word.strip('\'') for word in words]
    return ''.join([word[0].upper() for word in words])