"""Advanced Question: Online Banking System
You are tasked with designing an online banking system. Consider the following features:
Each account has an account number, balance, and account holder information.
Implement a decorator called TransactionLogger that logs account transactions (e.g., deposits, withdrawals) to a file.
Use abstraction to create an interface for different types of accounts (e.g., savings, checking).
Handle file I/O for storing account details and transaction history.
Implement error handling for cases like insufficient funds, invalid account numbers, etc.
How would you ensure encapsulation while allowing account holders to access their balances securely?"""

from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(Account):
    def __init__(self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

class CheckingAccount(Account):
    def __init__(self, account_number, balance, account_holder):
        self.account_number = account_number
        self.balance = balance
        self.account_holder = account_holder

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds")

def TransactionLogger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("transaction_log.txt", "a") as file:
            file.write(f"Transaction: {func.__name__} - Amount: {args[1]}\n")
        return result
    return wrapper
