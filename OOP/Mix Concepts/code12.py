"""Advanced Question: Restaurant Reservation System
You are building a reservation system for a fine dining restaurant. Consider the following requirements:
Each reservation has a date, time, party size, and customer details.
Implement a decorator called SpecialOccasion that allows customers to mark their reservation as a special occasion (e.g., anniversary, birthday).
Use polymorphism to handle different types of tables (e.g., window view, private booth).
Ensure proper encapsulation by protecting customer privacy (e.g., only authorized staff can view reservation details).
Implement error handling for cases like fully booked time slots or invalid party sizes.
How would you handle inheritance for different types of customers (e.g., regular, VIP)?"""

from abc import ABC, abstractmethod

# Base class for reservations
class Reservation(ABC):
    def __init__(self, date, time, party_size, customer_name):
        self.date = date
        self.time = time
        self.party_size = party_size
        self.customer_name = customer_name

    @abstractmethod
    def confirm(self):
        pass

# Concrete class for regular reservations
class RegularReservation(Reservation):
    def confirm(self):
        print(f"Regular reservation for {self.party_size} guests on {self.date} at {self.time} by {self.customer_name}")

# Concrete class for VIP reservations
class VIPReservation(Reservation):
    def confirm(self):
        print(f"VIP reservation for {self.party_size} guests on {self.date} at {self.time} by {self.customer_name}")

# Decorator for special occasions
def SpecialOccasion(reservation_type):
    def wrapper(cls):
        class SpecialReservation(cls):
            def __init__(self, *args, occasion=None, **kwargs):
                super().__init__(*args, **kwargs)
                self.occasion = occasion

            def confirm(self):
                if self.occasion:
                    print(f"{self.occasion} special occasion reservation for {self.party_size} guests on {self.date} at {self.time} by {self.customer_name}")
                else:
                    super().confirm()

        return SpecialReservation

    return wrapper

# Example usage:
if __name__ == "__main__":
    # Create regular reservation
    regular = RegularReservation(date="2023-05-20", time="19:00", party_size=4, customer_name="Alice")
    regular.confirm()

    # Create VIP reservation with special occasion
    @SpecialOccasion(reservation_type=VIPReservation)
    class AnniversaryReservation:
        def __init__(self, *args, **kwargs):
            pass

    anniversary = AnniversaryReservation(date="2023-06-10", time="20:30", party_size=2, customer_name="Bob", occasion="Anniversary")
    anniversary.confirm()
