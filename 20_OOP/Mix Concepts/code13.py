
"""give me complete code for this:Advanced Question: Flight Booking System
You are developing a flight booking system for an airline. Consider the following features:
Each flight has a flight number, departure city, destination city, and available seats.
Implement a decorator called SeatUpgrade that allows passengers to upgrade their seats (e.g., economy to business class).
Use abstraction to create an interface for payment gateways (e.g., credit card, PayPal).
Handle file I/O for storing flight details and passenger bookings.
Implement error handling for cases like overbooking, invalid seat selections, etc.
How would you ensure encapsulation while managing passenger bookings and payments?"""

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCard(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPal(PaymentGateway):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

def SeatUpgrade(func):
    def wrapper(*args, **kwargs):
        print("Seat upgrade successful!")
        return func(*args, **kwargs)
    return wrapper

class Flight:
    def __init__(self, flight_number, departure_city, destination_city, available_seats):
        self.flight_number = flight_number
        self.departure_city = departure_city
        self.destination_city = destination_city
        self.available_seats = available_seats

    @SeatUpgrade
    def upgrade_seat(self, passenger_name, current_seat):
        print(f"{passenger_name} upgraded seat from {current_seat} to Business Class")

    def book_flight(self, passenger_name, seat_type):
        if seat_type == "Business Class":
            if self.available_seats > 0:
                self.available_seats -= 1
                print(f"{passenger_name} booked a {seat_type} seat on flight {self.flight_number}")
            else:
                print("Sorry, the flight is fully booked.")
        else:
            print("Invalid seat selection.")

# File I/O for storing flight details and passenger bookings
def save_flight_details(flight):
    with open(f"flight_{flight.flight_number}.txt", "w") as file:
        file.write(f"Flight Number: {flight.flight_number}\nDeparture City: {flight.departure_city}\nDestination City: {flight.destination_city}\nAvailable Seats: {flight.available_seats}")

def save_passenger_booking(passenger_name, flight_number, seat_type):
    with open(f"booking_{passenger_name}.txt", "w") as file:
        file.write(f"Passenger Name: {passenger_name}\nFlight Number: {flight_number}\nSeat Type: {seat_type}")

# Error handling for overbooking and invalid seat selections
def handle_booking_errors(flight, passenger_name, seat_type):
    if seat_type != "Business Class":
        print("Invalid seat selection.")
    elif flight.available_seats == 0:
        print("Sorry, the flight is fully booked.")
    else:
        flight.book_flight(passenger_name, seat_type)

# Encapsulation for managing passenger bookings and payments
flight1 = Flight("F123", "New York", "London", 100)
credit_card = CreditCard()
paypal = PayPal()

handle_booking_errors(flight1, "Alice", "Business Class")
flight1.upgrade_seat("Alice", "Economy")
credit_card.process_payment(500)
paypal.process_payment(200)
save_flight_details(flight1)
save_passenger_booking("Alice", "F123", "Business Class")
