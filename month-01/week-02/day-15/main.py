from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, name : str, student_id : int, marks : int):
        self.name = name
        self.student_id = student_id

        if not(0 <= marks <= 100):
            raise ValueError ("marks must between 0 and 100")

        self .__marks = marks

    @abstractmethod

    def show_details(self)->None:
        pass

    def get_marks(self)->int:
        return self.__marks

    def update_marks(self, new_marks : int)->None:
        if not(0 <= new_marks <= 100):
            raise ValueError("new_marks must be between 0 to 100")

        self.__marks = new_marks    

class RegularStudent(Student):
    def show_details(self)->None:
        print(f"Name : {self.name}, ID : {self.student_id}, Marks : {self.get_marks()}, Type : Regular")

class ScholarshipStudent(Student):

    def show_details(self) -> None:
        print(
            f"Name: {self.name}, ID: {self.student_id}, Marks: {self.get_marks()}, Type: Scholarship Student"
        )        


#=======================================
# Testing Requirements
# ======================================
if __name__ == "__main__":
    print("--- Testing Start ---")
# Marks = 85 (accept)
    try:
        s1 = RegularStudent("Ali", 1, 85)
        print(f"Marks = 85: Success, Marks = {s1.get_marks()}")
    except ValueError as e:
        print(f"Marks = 85: failed with error: {e}")

# Marks = 0 (accept) 
    try:
        s2 = RegularStudent("Sahar", 2, 0)  
        print(f"Marks = 0 Success, Marks = {s2.get_marks()}")
    except ValueError as e:
        print(f"Marks = 0: failed with error: {e}")

# Marks = 100 (accept)
    try:
        s3 = RegularStudent("Moosa", 3, 100)  
        print(f"Marks = 100 Success, Marks = {s3.get_marks()}")
    except ValueError as e:
        print(f"Marks = 100: failed with error: {e}")                 

# 4. Marks = -5 (ValueError expected)
    try:
        s4 = RegularStudent("Zain", 4, -5)
    except ValueError as e:
        print(f"Marks = -5: ValueError caught successfully! ({e})")

    # 5. Marks = 105 (ValueError expected)
    try:
        s5 = RegularStudent("Fatima", 5, 105)
    except ValueError as e:
        print(f"Marks = 105: ValueError caught successfully! ({e})")

    # 6. Existing marks 85 (s1), update to 95 -> Updated marks = 95
    try:
        print(f"Before update: {s1.get_marks()}")
        s1.update_marks(95)
        print(
            f"Existing marks 85, update to 95 -> Updated marks = {s1.get_marks()}"
        )
    except ValueError as e:
        print(f"Update failed: {e}")

    print("--- Testing End ---")


# ==========================================
# Testing Requirements & Polymorphism
# ==========================================
if __name__ == "__main__":
    print("--- Students Details ---")

    students_list = [
        RegularStudent("Ali", 1, 85),
        ScholarshipStudent("Moosa", 3, 100),
        RegularStudent("Sahat", 2, 92)
    ]

    for student in students_list:
        student.show_details()
# Test 1
ali = students_list[0]
print("Test 1: Valid Update")
print(f"Before update: {ali.get_marks()}")
ali.update_marks(95)
print("Marks updated successfully.")
print(f"After update: {ali.get_marks()}")

# Test 2 & 3

print("\nTest 2 & 3: Invalid Update & Data Integrity Verification")
try:
    ali.update_marks(105)
except ValueError as e:
    print(f"Error: {e}")
    print(f"Current marks: {ali.get_marks()}")

empty_students = []   