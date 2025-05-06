from student import Student
from instructor import Instructor
from course import Course
from enrollment import Enrollment
from teachingAssistant import TeachingAssistant

def main():
    s1=Student("Olivier NIYONGABO", 1)
    s2=Student("Gaspa NSENGIYUMVA", 2)

    I1=Instructor("prof. Olivis T", 100)

    c1=Course("CS101", "Information Technology", 1)
    c2=Course("CS102", "Software Engineering", 2)
    

    Enrollment(s1, c1)
    Enrollment(s2, c2)

    I1.addCourse(c1)

    TA=TeachingAssistant("Mr Pellino", 11111)
    TA.addCourse(c1)
    

    print("Student:",s1)
    for course in s1.get_courses():
        print("_", course.title)

    print("enrollment:", c1.title)
    for e in c1:
        print("_", e)
    print(" T.A information:", TA)
    print("TA teaches: ",[course.title for course in TA.courses])
if __name__ == "__main__":
  main()