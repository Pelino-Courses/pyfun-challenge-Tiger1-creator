class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        student.addEnrollment(course)
        # course.enroll_student(self)
    def __str__(self):
        return (f"Student: {self.student.name}, Course enrlled is: {self.course.title}")