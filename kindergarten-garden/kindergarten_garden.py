class Garden:
    _students = [
        'Alice', 'Bob', 'Charlie', 'David',
        'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]

    _plants_table = {
        'R': "Radishes", 'G': "Grass", 'C': "Clover", 'V': "Violets"
    }

    def __init__(self, diagram: str, students: list = None):
        self.diagram = diagram.split()
        if students:
            self._students = sorted(students)

    def plants(self, student: str) -> list:
        initials = self._get_initials(student)
        return [self._plants_table[initial] for rows in initials for initial in rows]

    def _calculate_position(self, student: str) -> int:
        idx = self._students.index(student)
        return idx * 2

    def _get_initials(self, student: str) -> list:
        col = self._calculate_position(student)
        return [row[col:col+2] for row in self.diagram]
