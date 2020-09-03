"""Allergies

Returns allergies info using a bitmask 'score'

Each allergen is a bit on the mask 'score', 
"""
class Allergies:
    allergens = ["eggs", "peanuts", "shellfish", "strawberries",
        "tomatoes", "chocolate", "pollen", "cats"]

    def __init__(self, score: int):
        self.score = score

    def allergic_to(self, item: str) -> bool:
        """Compares an candidate item for allergy check against the bitmask score
        
        How it works:
            when you receive a score decimal 10 you have binary 110
            10 bitwise-and 110 == 2 -> True - for shellfish
            100 bitwise-and 110 == 8 -> True - for strawberries
            1000 bitwise-and 110 == 0 -> False for tomatoes"""
        return bool(self.score & 2**self.allergens.index(item))

    @property
    def lst(self) -> list:
        return [item for item in self.allergens if self.allergic_to(item)]
