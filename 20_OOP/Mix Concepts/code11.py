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
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(Account):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")

class CheckingAccount(Account):
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds!")

class TransactionLogger:
    def __init__(self, filename):
        self.filename = filename

    def log_transaction(self, account_number, transaction_type, amount):
        with open(self.filename, 'a') as file:
            file.write(f"Account {account_number}: {transaction_type} ${amount}\n")

    def log_account_transaction(self, account, transaction_type, amount):
        self.log_transaction(account.account_number, transaction_type, amount)

def TransactionLoggerDecorator(account):
    def wrapper(func):
        def decorated(*args, **kwargs):
            result = func(*args, **kwargs)
            logger = TransactionLogger("transaction_log.txt")
            logger.log_account_transaction(account, func.__name__, kwargs.get("amount", 0))
            return result
        return decorated
    return wrapper

# Example usage:
if __name__ == "__main__":
    savings = SavingsAccount("SA123", "Alice")
    savings.deposit(1000)
    savings.withdraw(200)
    print(f"Savings balance: ${savings.balance}")

    checking = CheckingAccount("CH456", "Bob")
    checking.deposit(1500)
    checking.withdraw(300)
    print(f"Checking balance: ${checking.balance}")

    # Apply TransactionLoggerDecorator to deposit and withdraw methods
    @TransactionLoggerDecorator(savings)
    def custom_deposit(account, amount):
        account.deposit(amount)

    custom_deposit(savings, amount=500)  # Log custom deposit

    logger = TransactionLogger("transaction_log.txt")
    logger.log_transaction(savings.account_number, "deposit", 1000)
    logger.log_transaction(checking.account_number, "withdrawal", 300)
