class Payment:
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

class WalletPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Wallet.")


# Polymorphism
payments = [
    CreditCardPayment(),
    UPIPayment(),
    WalletPayment()
]

for payment in payments:
    payment.pay(1000)


