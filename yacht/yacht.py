# Score categories.
YACHT = lambda dice: 50 if len(set(dice)) == 1 else 0
ONES = lambda dice: sum(die for die in dice if die == 1)
TWOS = lambda dice: sum(die for die in dice if die == 2)
THREES = lambda dice: sum(die for die in dice if die == 3)
FOURS = lambda dice: sum(die for die in dice if die == 4)
FIVES = lambda dice: sum(die for die in dice if die == 5)
SIXES = lambda dice: sum(die for die in dice if die == 6)
FULL_HOUSE = lambda dice: sum(dice) if len(set(dice)) == 2 and any(dice.count(die) == 3 for die in set(dice)) else 0
FOUR_OF_A_KIND = lambda dice: sum(die * 4 for die in set(dice) if dice.count(die) > 3)
LITTLE_STRAIGHT = lambda dice: 30 if sum(dice) == 15 and len(set(dice)) == 5 else 0
BIG_STRAIGHT = lambda dice: 30 if sum(dice) == 20 and len(set(dice)) == 5 else 0
CHOICE = lambda dice: sum(dice)


def score(dice: list, category) -> int:
    if any(die not in range(0, 7) for die in dice):
        raise ValueError("Invalid die {}".format(dice))

    return category(dice)
