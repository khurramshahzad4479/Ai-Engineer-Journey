students = [
    {"name": "Ali", "marks": 85},
    {"name": "Moosa", "marks": 92},
    {"name": "Nasir", "marks": 78},
    {"name": "Ahmed", "marks": 105},
    {"name": "Asad", "marks": -10}
]

def student_report(students):
    valid_students = []
    invalid_students = []
    
    # Marks 0 se 100 ke darmiyan hone chahiye valid hone ke liye
    for student in students:
        if 0 <= student["marks"] <= 100:
            valid_students.append(student)
        else:
            invalid_students.append(student)
            
    # Valid students ka average aur highest scorer nikalna
    if valid_students:
        total_marks = sum(s["marks"] for s in valid_students)
        average_marks = total_marks / len(valid_students)
        highest_scorer = max(valid_students, key=lambda x: x["marks"])
    else:
        average_marks = 0
        highest_scorer = None
        
    report = {
        "valid_students": valid_students,
        "invalid_students": invalid_students,
        "average_marks": average_marks,
        "highest_scorer": highest_scorer
    }
    
    return report

# Function call and output
result = student_report(students)
print(result)