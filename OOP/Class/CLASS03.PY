"""Start with your program from CLASS01.PY. Add an attribute
called number_served with a default value of 0. Create an instance called restaurant from this
class. Print the number of customers the restaurant has served, and then change this value and
print it again.
Add a method called set_number_served() that lets you set the number of customers that
have been served. Call this method with a new number and print the value again.
Add a method called increment_number_served() that lets you increment the number of
customers who’ve been served. Call this method with any number you like that could represent
how many customers were served in, say, a day of business."""


# Define the Restaurant class
class Restaurant:
    # Initialize the attributes
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # Add an attribute for number of customers served
    
    # Print the restaurant information
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")
    
    # Print a message that the restaurant is open
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now.")
    
    # Set the number of customers served
    def set_number_served(self, number):
        self.number_served = number
    
    # Increment the number of customers served
    def increment_number_served(self, number):
        self.number_served += number

# Create an instance of the Restaurant class
restaurant = Restaurant("Pizza Hut", "Italian")

# Print the number of customers served
print(f"{restaurant.restaurant_name} has served {restaurant.number_served} customers.")

# Change the number of customers served and print it again
restaurant.number_served = 10
print(f"{restaurant.restaurant_name} has served {restaurant.number_served} customers.")

# Use the set_number_served method and print the value again
restaurant.set_number_served(20)
print(f"{restaurant.restaurant_name} has served {restaurant.number_served} customers.")

# Use the increment_number_served method and print the value again
restaurant.increment_number_served(5)
print(f"{restaurant.restaurant_name} has served {restaurant.number_served} customers.")
