from student import Student
from instructor import Instructor

class TeachingAssistant(Instructor,Student):
    def __init__(self, name, ID):
        Student.__init__(self, name, ID)
        Instructor.__init__(self, name, ID)
    def role(self) -> str:
        return "teaching assistant"