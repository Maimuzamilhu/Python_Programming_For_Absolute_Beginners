"""Make a class called User. Create two attributes called first_name and last_name,
and then create several other attributes that are typically stored in a user profile. Make a
method called describe_user() that prints a summary of the user’s information. Make another
method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user."""


class User:
   
    def __init__(self, first_name, last_name, age, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.username = username
    
   
    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Username: {self.username}")
    
    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome to our website.")

user1 = User("Alice", "Smith", 25, "alice@gmail.com", "alice123")
user2 = User("Bob", "Jones", 30, "bob@yahoo.com", "bob456")
user3 = User("Charlie", "Brown", 35, "charlie@outlook.com", "charlie789")


user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
