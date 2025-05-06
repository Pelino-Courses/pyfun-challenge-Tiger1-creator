from person import Person
class Instructor(Person):
    def __init__(self, name, ID):
        super().__init__(name, ID)
        self.courses = []

    def role(self) -> str:
        return "Instructor"
    def addCourse(self, course):
        self.courses.append(course) 