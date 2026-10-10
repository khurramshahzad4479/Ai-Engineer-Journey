students = [
    {"name": "Moosa", "marks": 92},
    {"name": "Ali", "marks": 85},
    {"name": "Nasir", "marks": 78},
    {"name": "Ahmed", "marks": 105},
    {"name": "Asad", "marks": -10}
]


def validate_marks(marks):
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

    return marks


def process_students(students):
    for student in students:
        name = student["name"]
        marks = student["marks"]

        try:
            valid_marks = validate_marks(marks)
            print(f"Name: {name} | Marks: {valid_marks}")

        except ValueError as e:
            print(f"Error for {name}: {e}")


def calculate_valid_average(students):
    valid_marks_list = []

    for student in students:
        try:
            valid_marks = validate_marks(student["marks"])
            valid_marks_list.append(valid_marks)

        except ValueError:
            continue

    if valid_marks_list:
        return sum(valid_marks_list) / len(valid_marks_list)

    return 0.0


process_students(students)

average = calculate_valid_average(students)
print(f"Valid Average: {average}")