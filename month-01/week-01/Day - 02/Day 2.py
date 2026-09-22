banner = """ ===============
               DAY = 2
             =============== """   

def count_words(text: str)->int:
    return len(text.split())

def count_characters(text: str)->int:
    return len(text)

def clean_text(text: str)->str:
    return text.strip().lower()

def analyse_text(text: str)->dict:
     return {"words" : count_words(text),
             "charaters" : count_characters(text),
             "upercase" : text.upper()}
result=analyse_text("python is very powerfull")
print(result)

def square_no(number: int)->int:
    return number*number
number = square_no(5)
number1 = square_no(9)
print(number)
print(number1)

def calculate_average(*args: float)->float:
        if len(args) == 0:
             raise ValueError("Atleast one number is required")
             
        return sum(args)/len(args)
Total = calculate_average(2,4,6,8)
print(Total)

