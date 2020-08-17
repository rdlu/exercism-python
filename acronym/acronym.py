import re

def abbreviate(sentence):
    words = re.findall(r"[a-zA-Z0-9]+\'{0,1}[a-zA-Z0-9]*", sentence)
    return ''.join([word[0].upper() for word in words])