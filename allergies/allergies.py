class Allergies:
    allergens = ["eggs", "peanuts", "shellfish", "strawberries",
        "tomatoes", "chocolate", "pollen", "cats"]

    def __init__(self, score: int):
        self.score = score

    def allergic_to(self, item: str) -> bool:
        return bool(self.score & 2**self.allergens.index(item))

    @property
    def lst(self) -> list:
        return [item for item in self.allergens if self.allergic_to(item)]
