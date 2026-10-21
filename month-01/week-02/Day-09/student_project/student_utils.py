def validate_marks(marks: int) -> int:
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100")

    return marks


def get_highest_scorer(students: list[dict]) -> dict:
    if not students:
        raise ValueError("Student list cannot be empty")

    return max(students, key=lambda s: s["marks"])