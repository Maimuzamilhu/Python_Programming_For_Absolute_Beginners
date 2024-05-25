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

ob2 = Restaurant("Worst" , "SCOCH")
ob2.describe_restaurant()

ob3 = Restaurant("Bahria" , "French")
ob3.describe_restaurant()
