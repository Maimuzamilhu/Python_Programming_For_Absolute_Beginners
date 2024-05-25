"""Decorator and Encapsulation:
You are building a logging system for a large e-commerce application. Implement a decorator called LogToFile that logs method calls to a file. The decorator should encapsulate the logging logic, allowing you to apply it selectively to specific methods (e.g., order processing, inventory updates). How would you use this decorator to log method calls in your application?"""

def logfile(func):
    def wrap(*args , **kwargs):
        print("Ths....")
        with open (logfile   , "r") as file:
            file.write(" EXtra")
        return func(*args , **kwargs)
    return logfile

class ecomerce:

    def __init__(self , customerName , Orderid) -> None:
        self.customerName = customerName
        self.Orderid = Orderid

    @logfile
    def process_order(self , customerName):
        print("THe order id of .....")


