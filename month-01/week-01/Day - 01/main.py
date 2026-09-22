banner = """"
==========================================
        AI ENGINEER JOURNEY
 ==========================================
 """
print(banner)
name = "Khurram Shahzad"
current_role = "Developer"
learning = "AI + ML"

print(f"My name is : {name}, My Current Role : {current_role}, learning : {learning}")

Day = 1
Status = "Started"
print(f"Today is my day : {Day}, {Status}")

Goal = "Build Real AI-Powerd Product"
print(f"My goal is {Goal}")

def count_text(text: str)->int:
    words = text.split()
    return len(words)
text = "Python is powerfull"
result = count_text(text)
print(result)

