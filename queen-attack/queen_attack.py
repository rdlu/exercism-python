class Queen:
    def __init__(self, row: int, column: int):
        if not 0 <= row < 8 or not 0 <= column < 8:
            raise ValueError("Must be between 0 and 7") 
        self.i = row
        self.j = column

    def can_attack(self, another_queen: 'Queen') -> bool:
        # law of physics
        if self.i == another_queen.i and self.j == another_queen.j:
            raise ValueError(f"Cannot be the same initial position [{self.i},{self.j}]")
        # same row or same column
        if self.i == another_queen.i or self.j == another_queen.j:
            return True
        # todo: diagonals
        if self.i == self.j and another_queen.i == another_queen.j:
            return True
        return False
