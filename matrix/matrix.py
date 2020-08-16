class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(value) for value in row_string.split()] 
            for row_string in matrix_string.split("\n")]
 
    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]