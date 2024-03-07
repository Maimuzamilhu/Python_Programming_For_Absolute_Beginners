"""Abstraction and Polymorphism:
Imagine you are designing a vehicle management system. Create an abstract base class called Vehicle with common properties like make, model, and year. Implement two concrete classes: Car and Motorcycle, both inheriting from Vehicle. Override the start_engine() method in each class to provide vehicle-specific behavior. How would you use polymorphism to handle a list of different vehicles in your system?"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return f"{self.make} {self.model} car engine started."

class Motorcycle(Vehicle):
    def start_engine(self):
        return f"{self.make} {self.model} motorcycle engine started."

# Example usage
def main():
    car1 = Car("Toyota", "Camry", 2022)
    motorcycle1 = Motorcycle("Harley-Davidson", "Sportster", 2021)

    vehicles = [car1, motorcycle1]

    for vehicle in vehicles:
        print(vehicle.start_engine())

if __name__ == "__main__":
    main()
