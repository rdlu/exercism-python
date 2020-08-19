from collections import defaultdict

class School:
    def __init__(self):
        self._students = defaultdict(set)

    def add_student(self, name: str, grade: int) -> None:
        self._students[grade].add(name)

    def roster(self) -> list:
        return [student \
            for grade_num in sorted(self._students.keys()) \
            for student in self.grade(grade_num)]

    def grade(self, grade_number: int) -> list:
        return sorted(self._students[grade_number])
