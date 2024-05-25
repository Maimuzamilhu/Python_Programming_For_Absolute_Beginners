""" Make a class called Restaurant. The __init__() method for Restaurant
should store two attributes: a restaurant_name and a cuisine_type. Make a method called
describe_restaurant() that prints these two pieces of information, and a method called
open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually,
and then call both methods."""

class Restaurant:
    def __init__(self , restaurant_name , cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Hi Welcome to the {self.restaurant_name},I hoped you liked!")
        print(f"Please dont play the {self.cuisine_type},Czn its not allowed!")

    def open_restaurant(self):
        print(f"Hi happy to tell that {self.restaurant_name} is opened at the moment!")

obj = Restaurant("The Royal" , "Swatch")
obj.describe_restaurant()
obj.open_restaurant()
