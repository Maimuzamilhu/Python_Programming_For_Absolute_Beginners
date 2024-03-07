"""Bank Account Management System:
Design a BankAccount class with the following properties:
Account number (unique identifier)
Account holder name
Balance
Implement encapsulation by making the properties private and providing public getter and setter methods.
Create subclasses for different types of accounts (e.g., SavingsAccount, CheckingAccount).
Use inheritance to share common behavior (e.g., deposit, withdraw) between account types.
Implement abstraction by defining an abstract method for calculating interest.
Demonstrate polymorphism by overriding the interest calculation method in each account type."""
from abc import abstractclassmethod , ABC
class Bank:
    def __init__(self , accountnumber , HolderName) -> None:
        self.accountNumber = accountnumber
        self.holderName = HolderName
        self.__balance = 0
    
    def getaccountnum(self):
        return self.accountNumber
    
    def getholdername(self):
        return self.accountNumber
    
    def getbalance(self):
        return self.__balance
    
    @abstractclassmethod
    def calculateinterset(self):
        pass
    
class SavingsAccount(Bank):
    def calculate_interest(self):
        return self.get_balance() * 0.05

class CheckingAccount(Bank):
    def calculate_interest(self):
        return self.get_balance() * 0.02

