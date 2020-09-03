"""Anagram utilities"""

def find_anagrams(word: str, candidates: list) -> list:
    """Detect anagrams on a list against a reference word
    
    Args:
        word: the reference word
        candidates: the list of words to be compared

    Returns:
        A new list with the anagrams found.
    """
    low_word = sorted(word.lower())
    return [candidate for candidate in candidates if is_anagram(low_word, candidate)]

def is_anagram(low_sort_word: str, candidate: str) -> bool:
    """Determine whether two words are anagrams of each other.

    Args:
        low_sort_words: the original word, sorted and lowered.
        candidate: the word to be compared

    Returns:
        A boolean True if the two words have the same letters in different order."""
    return sorted(candidate.lower()) == low_sort_word and candidate.lower() != low_sort_word