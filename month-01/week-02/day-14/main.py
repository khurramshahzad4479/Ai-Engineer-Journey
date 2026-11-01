#abstract class method
from abc import ABC, abstractmethod

class Payment(ABC):

    def validate_amount(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Payment amount must be positive")

    @abstractmethod
    def process_payment(self, amount : int)-> None:
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount : int)->int:
        self.validate_amount(amount)
        print(f"Payment of {amount} processed using Credit Card")

class PayPalPayment(Payment):
    def process_payment(self, amount : int)->int:
        self.validate_amount(amount)
        print(f"Payment of {amount} processed using Credit Card")


payment_method = [CreditCardPayment(), PayPalPayment()]
test_amounts = [1200, 0, -50]
for payment in payment_method:
    print(f"\n--- Testing {payment.__class__.__name__} ---")
    for amount in test_amounts:
        try:
             payment.process_payment(amount)
        except ValueError as e:
             print(f"Error Caught: {e}")
             





    