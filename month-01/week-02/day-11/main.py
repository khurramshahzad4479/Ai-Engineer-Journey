class Student:
    def __init__(self, name: str, course: str, marks: int):
        self.name = name
        self.course = course
        self.marks = marks

    def show_details(self):
        print("name:", self.name)
        print("course:", self.course)
        print("marks:", self.marks)

    def update_marks(self, new_marks: int):
        if new_marks < 0 or new_marks > 100:
            raise ValueError("marks must be between 0 and 100")
        self.marks = new_marks
                

student1 = Student("Moosa", "Html", 100)
student2 = Student("Sahar", "Java", 91)
student3 = Student("Ali", "Python", 79)


student1.show_details()
print()
student2.show_details()
print()
student3.show_details()

student1.update_marks(97)
print(student1.marks)
student2.update_marks(104)
print(student2.marks)
student3.update_marks(-10)
print(student3.marks)

students = [
    (student1, 104),
    (student2, -10),
    (student3, 97),
]

for student, new_marks in students:
    try:
        student.update_marks(new_marks)
        print(f"{student.name}: Marks updated successfully")
    except ValueError as error:
        print(f"{student.name}: Error - {error}")

    print("Current marks:", student.marks)
    print()




