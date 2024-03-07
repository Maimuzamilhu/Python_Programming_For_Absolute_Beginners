"""Add an attribute called login_attempts to your User class from
Exercise 9-3 (page 162). Write a method called increment_login_attempts() that increments
the value of login_attempts by 1. Write another method called reset_login_attempts() that
resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times.
Print the value of login_attempts to make sure it was incremented properly, and then call
reset_login_attempts(). Print login_attempts again to make sure it was reset to 0."""


class User:
   
    def __init__(self, first_name, last_name, age, email, username , login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.username = username
        self.login_attempts = login_attempts 
    
    
    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Username: {self.username}")
    
   
    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome to our website.")
    
   
    def increment_login_attempts(self):
        self.login_attempts += 1
    
  
    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Alice", "Smith", 25, "alice@gmail.com", "alice123" ,0)


user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()


print(f"Login attempts: {user1.login_attempts}")


user1.reset_login_attempts()


print(f"Login attempts: {user1.login_attempts}")