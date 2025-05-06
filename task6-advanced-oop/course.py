from typing import List
from enrollment import Enrollment

class Course:
    code: str
    title: str

    def __init__(self, code: str, title: str, capacity: int):
        self.code = code
        self.title = title
        self.capacity = capacity
        self.enrollments: List[Enrollment] = []
    def addEnrollment(self, enrollment: Enrollment):
        if len(self.enrollments) >= self.capacity:
            raise ValueError("Course is full")
        self.enrollments.append(enrollment)
    def __iter__(self):
        return iter(self.enrollments)
    def __add__(self, other: 'Course') -> List[str]:
       return list(set([e.student.name for e in self.enrollments + other.enrollments]))
    @classmethod
    def create_Lab_Course(cls, code: str, title: str):   
        return cls(code, title + "Lab",30)