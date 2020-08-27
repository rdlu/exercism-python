class Queen:
    def __init__(self, row: int, column: int):
        if row not in range(0, 8) or column not in range(0, 8):
            raise ValueError("Must be between 0 and 7") 
        self.i = row
        self.j = column

    def can_attack(self, another_queen: 'Queen') -> bool:
        if self.i == another_queen.i and self.j == another_queen.j:
            raise ValueError(f"Cannot be the same initial position [{self.i},{self.j}]")
        # same row, column or diff 
        return self.i == another_queen.i or self.j == another_queen.j \
            or abs(another_queen.i - self.i) == abs(another_queen.j - self.j)
