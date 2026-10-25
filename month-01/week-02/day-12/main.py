class Person:
    def __init__(self, name: str):
        self.name =  name

    def show_name(self):
        print("Name:", self.name)

class Student(Person):
    def __init__(self, name: str, course: str, marks: int):
        super().__init__(name)
        self.course = course
        self.marks = marks

    def show_details(self):
        self.show_name()
        print("Course:", self.course)
        print("Marks:", self.marks)  

student1 = Student("Moosa", "Python", 91)
#student1.show_details() 



class BankAccount:
    def __init__(self, balance: float):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.__balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance +=amount

    def get_balance(self):
        return self.__balance

try:
    account = BankAccount(200)
    deposit_amount = 500
    account.deposit(deposit_amount)
    print(f"Success:{deposit_amount}, successfully deposited")


except ValueError as error:
    #if deposit is invalid except error
    print("Error:", error)

print("Current Balance:", account.get_balance())
