class Matrix(object):
    def __init__(self, matrix_string):
        self._matrix = [list(map(int, r.split())) for r in matrix_string.split('\n')]

    @property
    def rows(self):
        return self._matrix[:]

    @property
    def columns(self):
        return list(map(list, zip(*self._matrix)))

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]
