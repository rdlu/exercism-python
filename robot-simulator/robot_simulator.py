EAST = lambda t: (t[0]+1, t[1])
NORTH = lambda t: (t[0], t[1]+1)
WEST = lambda t: (t[0]-1, t[1])
SOUTH = lambda t: (t[0], t[1]-1)


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.coordinates = (x, y)
        self.directions = [EAST, NORTH, WEST, SOUTH]

    def move(self, instructions: str) -> None:
        """Move the robot from a list of instructions"""
        for instruction in instructions:
            if instruction == 'A':
                self.coordinates = self.new_coordinates()
            else:
                self.direction = self.new_direction(instruction)

    def new_coordinates(self):
        """Executes the lambda associated with the direction
           Advancing the coordinates in that direction
        """
        return self.direction(self.coordinates)

    def new_direction(self, rotation: str):
        "Gives a new lambda associated with the rotation"
        if rotation == 'L': 
            return self.directions[(self.directions.index(self.direction) + 1) % 4]
        if rotation == 'R':
            return self.directions[(self.directions.index(self.direction) - 1) % 4]
        return self.direction