# Challenge 1

marks = [390,409,376,283,321]
print(marks[0], marks[4])
marks.append(344)

# Challenge 2

student = {"name" : "moosa",
           "age" : 17,
           "marks" : 391}
student.update({"marks":400})
print(student)

# challenge 3 
students = [{"name" : "ahmed", "marks" : 290},
            {"name" : "asad", "marks" : 330},
            {"name" : "arif", "marks" : 345},
            {"name" : "sohail", "marks" : 398}]
def highest_marks(student : list[dict]):
    if not student:
        raise ValueError("student cannot be empty")

    top_student =  max(student, key=lambda student: student["marks"])
    return top_student["name"]



top_name = highest_marks(students)
print("Top_student :", top_name)

