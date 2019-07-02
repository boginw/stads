class Grade:
    name = None
    grade = None
    ects = None
    when = None

    def __init__(self, name, grade, ects, when):
        self.name = name
        self.grade = grade
        self.ects = ects
        self.when = when
    
    def equals(self, grade):
        return (
            self.name == grade.name and
            self.grade == grade.grade and
            self.ects == grade.ects and
            self.when == grade.when
        )