# Polymorphism & Method overriding
# Polymorphism (same interface, different behaviour)
# In other words, the same method name can exist in different classes, but each class can implement that method in its own way
# Like sound in this example sound() for dog "woof" & for cat "Meow"

class Animal:
    def sound(self):
        print("animals make a sound")

class Dog:
    def sound(self):
        print("Dog says: Woof!")

class Cat:
    def sound(self):
        print("Cat says: Meow")

animal = Animal()
dog = Dog()
cat = Cat()
#animal.sound()
#dog.sound()
#cat.sound()   

animals = [animal, dog, cat]
for object in animals:
    object.sound()

# In this loop, for each object, the code will call the appropriate `sound()` method for that specific object. This is a practical example of polymorphism.    

#-----Method Overriding-----

# Method overriding occurs when a child class replaces an existing method of the parent class with its own implementation.

class Animal:
    def sound(self):
        print("animals make a sound")


class Dog(Animal):
    def sound(self):
        print("Dog says: woof")

class Cat(Animal):
    def sound(self):
        print("Cat says Meow")

animal = Animal()
dog = Dog()
cat = Cat()
animal.sound()
dog.sound()
cat.sound()

# Dog inherits from Animal. But Dog defines its own sound() method, so Dog. Sound() prints the message of the dog, not the parent message.

# This is what is called method overriding
# Method Overriding with super()

class Animal:
    def sound(self):
        print("animals make a sound")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog says: woof")

dog = Dog()
dog.sound()

# It calls the `sound()` method of the parent class. Afterward, the child class prints its own message        
# Remember: Calling `super()` is not a requirement for overriding. This step is useful when you also want to retain the behavior of the parent method.

#-----Student Grading system Project------

class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def show_result(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

    def get_grade(self):
        pass        

class RegularStudents(Student):
    def show_result(self):
        print(f"Name: {self.name}, Marks: {self.marks} | Status : Regular Student")

    def get_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "F"      

class ScholarshipStudents(Student):
    def show_result(self):
        print(f"Name: {self.name}, Marks: {self.marks} | Status: Scholarship Student")

    def get_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        else:
            return "Needs Improvement (C)"
            

reg_student = RegularStudents("Ali", 78)
#reg_student.show_result()
scho_student = ScholarshipStudents("Moosa", 90)
#scho_student.show_result()

print("--- Students Result & Grades ---")
students_list = [reg_student, scho_student]
for student in students_list:
    student.show_result()
    print(f"Grade: {student.get_grade()}")                          
