from calculator import add, subtract, multiply,divide

print(add(10,5)) #output 15
print(subtract(10,5)) #output 5
print(multiply(10,5)) #output 50
print(divide(10,5)) #output 2.0

#Two ways to import modules in python 
# import & from ..import
#import calculator
#print(calculator.add(10,5)) output 15
#from calculator import add
#print(add(10,5)) # now we can call "add" directly

from student_utils import validate_marks, get_highest_scorer

students = [
    {"name": "Ali", "marks": 85},
    {"name": "Moosa", "marks": 92},
    {"name": "Nasir", "marks": 78},
]

try:
    for student in students:
        validate_marks(student["marks"])

    highest = get_highest_scorer(students)
    print("Highest scorer:", highest["name"])
    print("Marks:", highest["marks"])

except ValueError as error:
    print("Error:", error)
