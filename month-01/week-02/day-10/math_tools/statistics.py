def calculate_average(numbers : list[float])->float:
    if numbers == 0:
        raise ValueError("numbers cannot be empty")
    return sum(numbers) / len(numbers)

