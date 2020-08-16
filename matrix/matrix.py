class Matrix:
    def __init__(self, matrix_string):
        list_of_rows_str = matrix_string.split('\n')
        self.list_of_rows = []
        for row in list_of_rows_str:
            self.list_of_rows.append([int(value) for value in row.split(' ')])

    def row(self, index):
        return self.list_of_rows[index-1]

    def column(self, index):
        col = []
        for row in self.list_of_rows:
            col.append(row[index-1])
        return col
