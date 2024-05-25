"""ecorator, Abstraction, and Polymorphism:
You are developing a web application that needs to authenticate users. Implement a decorator called AuthenticateUser that checks if a user is logged in before allowing access to certain routes. Use an abstract base class called UserController with methods like login(), logout(), and get_user_info(). Create concrete classes for different authentication methods (e.g., OAuth, username/password). How would you apply the decorator to specific routes and handle different authentication mechanisms?"""

from abc import abstractmethod, ABC

class UserController(ABC):
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    @abstractmethod
    def login(self, username):
        pass

    @abstractmethod
    def logout(self, username):
        pass

def authentications(func):
    def wrapper(self, *args, **kwargs):
        # Add authentication logic here
        print("Authentication logic here")
        return func(self, *args, **kwargs)
    return wrapper

class Main(UserController):
    def __init__(self, username, password, email):
        super().__init__(username, password, email)

    def login(self, username):
        print("User is logged in")

    def logout(self, username):
        print("User is logged out")

    @authentications
    def authentication(self):
        print("Access granted")

# Example usage
user = Main("john_doe", "password123", "john.doe@example.com")
user.authentication()
