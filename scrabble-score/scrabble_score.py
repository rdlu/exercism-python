scores_dict = {
        1: 'AEIOULNRST',
        2: 'DG',
        3: 'BCMP',
        4: 'FHVWY',
        5: 'K',
        8: 'JX',
        10: 'QZ'
    }

scores = { letter: score
            for (score, letters) in scores_dict.items()
            for letter in letters }

def score(word: str) -> int:
    return sum(scores[letter] for letter in word.upper())
