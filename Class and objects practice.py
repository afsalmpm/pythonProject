class Student:  # Defining a a class named Student
    def __init__(self, name, age, grade):  # Initialisation function
        self.name = name  # Initialisation function is to add attributes variable in a  class is called attribute
        self.age = age  # So whenever you assign a Student class, you should always provide name age and grade
        self.grade = grade

    def get_grade(self):
        return self.grade

    def get_details(self):
        print(f"Name is {self.name}")
        print(f"{self.name}'s grade is {self.grade}")
        print(f"{self.name}'s age is {self.age}")


class Course:  # Defining a class named Course
    def __init__(self, name, max_students):
        self.name = name  # Providing the following attributes
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
        else:
            print("Seats filled already")

    def get_course_participants(self):
        print(self.students)

    def average(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        print(f"Average is {value / len(self.students)}")


S1 = Student("Navin", 19, 95)
S2 = Student("Shaheen", 20, 100)
S3 = Student("Faheem", 20, 99)
S4 = Student("Shajeem", 20, 99)

S1.get_details()
S2.get_details()
S3.get_details()
Course1 = Course(Student, 3)
Course1.add_student(S1)
Course1.get_course_participants()
Course1.add_student(S2)
Course1.get_course_participants()
Course1.add_student(S3)
Course1.get_course_participants()
Course1.add_student(S4)
Course1.get_course_participants()
Course1.average()
