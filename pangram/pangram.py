def is_pangram(sentence: str) -> bool:
    filtered_sentence = filter(str.isalpha, sentence.lower())
    return len(set(filtered_sentence)) == 26
