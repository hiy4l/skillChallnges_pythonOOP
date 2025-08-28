class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return f"deposited ${amount}"
        
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdraw amount must be positive.")
        self.balance -= amount
        return f"withdrew ${amount}"
        
    def __repr__(self):
        return f"A {self.__class__.__name__} with ${self.balance} in it."
        
class Savings(BankAccount):
    interest_rate = 0.0035
    
    def pay_interest(self):
        interest = self.balance * self.interest_rate
        return super().deposit(interest)
    
class HighInterest(Savings):
    interest_rate = 0.007
    
    def __init__(self, withdrawal_fee = 5):
        super().__init__()
        self.withdrawal_fee = withdrawal_fee
        
    def withdraw(self, amount):
        self.balance -= self.withdrawal_fee
        return super().withdraw(amount)

class LockedIn(HighInterest):
    interest_rate = 0.009
    
    def __init__(self, initial_balance=0):
        super().__init__()
        self.balance = initial_balance

    def withdraw(self, amount):
        raise ValueError("Withdrawals are not allowed from a LockedIn account.")