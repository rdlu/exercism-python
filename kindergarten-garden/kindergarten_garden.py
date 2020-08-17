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
        initials = self._get_initials(student)
        return [self._plants_table[initial] for rows in initials for initial in rows]

    def _get_initials(self, student: str) -> list:
        idx = self._students.index(student) * 2
        return [row[idx:idx+2] for row in self.diagram]
