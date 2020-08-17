class Garden:
    _students = [
        'Alice', 'Bob', 'Charlie', 'David',
        'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]

    _plants_table = {
        'R': "Radishes", 'G': "Grass", 'C': "Clover", 'V': "Violets"
    }

    def __init__(self, diagram: str, students: list = _students):
        self.diagram = diagram.split()
        self._students = sorted(students)

    def plants(self, student: str) -> list:
        return [self._plants_table[initial] for initial in self._get_initials(student)]

    def _get_initials(self, student: str) -> list:
        idx = self._students.index(student) * 2
        return [initial for row in self.diagram for initial in row[idx:idx+2]]
