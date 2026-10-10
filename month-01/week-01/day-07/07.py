students = [
    {"name": "Ali", "marks": 85},
    {"name": "Moosa", "marks": 92},
    {"name": "Nasir", "marks": 78},
    {"name": "Ahmed", "marks": 105},
    {"name": "Asad", "marks": -10}
]

def validate_marks(marks):
    if not isinstance(marks, (int, float)) or isinstance(marks, bool):
        raise ValueError("Marks must be numeric")

    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100")

    return marks

def student_report(students):
    valid_students = []
    invalid_students = []
    
    for student in students:
        try:
            # Agar marks valid nahi hain toh ValueError aayega
            validate_marks(student["marks"])
            valid_students.append(student)
        except ValueError:
            # Exception catch karke student ko invalid list mein bhejh diya
            invalid_students.append(student)
            
    # Valid students ka average aur highest scorer nikalna
    if valid_students:
        total_marks = sum(s["marks"] for s in valid_students)
        average_marks = total_marks / len(valid_students)
        highest_scorer = max(valid_students, key=lambda x: x["marks"])
    else:
        average_marks = 0
        highest_scorer = None
        
    return {
        "valid_students": valid_students,
        "invalid_students": invalid_students,
        "average_marks": average_marks,
        "highest_scorer": highest_scorer
    }

# Function call and output
result = student_report(students)
print(result)