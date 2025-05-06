from person import Person
class Student(Person):
    def __init__(self, name, ID):
        super().__init__(name, ID)
        self.enrollment = []

    def role(self) -> str:
        return "Student"
    def addEnrollment(self, course):
        self.enrollment.append(course)
    def get_courses(self):
       return self.enrollment

    def __iter__(self):
        return iter(self.enrollment) 