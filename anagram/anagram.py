def find_anagrams(word: str, candidates: list) -> list:
    return [candidate for candidate in candidates
        if sorted(candidate.lower()) == sorted(word.lower()) and candidate.lower() != word.lower()]
