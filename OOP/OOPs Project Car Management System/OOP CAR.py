
"""
 Prepared BY : Muzzamil Khalid
 Roll Number : 22F-BSAI-29
 Department : Artificial Intelligence 
 Section  : A1
 Submitted To : Sir Talha 
"""

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def getBrand(self):
        return self.brand

    def getModel(self):
        return self.model


class Car(Vehicle):
    def __init__(self, carId, brand, model, basePricePerDay):
        super().__init__(brand, model)
        self.carId = carId
        self.basePricePerDay = basePricePerDay
        self.available = True      # Car rent k liye available hai jb car rent pr chli jaegi to yh false ho jega

    def getCarId(self):
        return self.carId

    def calculatePrice(self, rentalDays):
        return self.basePricePerDay * rentalDays

    def isAvailable(self):
        return self.available

    def rent(self):
        self.available = False #Car rent ho chuki hai is liye false ayega

    def returnCar(self):
        self.available = True #jb car return krny ayega to car true ho jaegi iska mtlb ab car hai 


class Customer:
    def __init__(self, customerId, name):
        self.customerId = customerId
        self.name = name

    def getCustomerId(self):
        return self.customerId

    def getName(self):
        return self.name


class Rental:
    def __init__(self, vehicle, customer, days):
        self.vehicle = vehicle
        self.customer = customer
        self.days = days

    def getVehicle(self):
        return self.vehicle

    def getCustomer(self):
        return self.customer

    def getDays(self):
        return self.days


class CarRentalSystem:
    def __init__(self):
        self.vehicles = []
        self.customers = []
        self.rentals = []

    def addVehicle(self, vehicle):
        if isinstance(vehicle, Vehicle) and vehicle not in self.vehicles: #obj and type
            self.vehicles.append(vehicle)
            print("Vehicle added successfully.")
        else:
            print("Invalid vehicle or vehicle already exists.")

    def addCustomer(self, customer):
        if isinstance(customer, Customer) and customer not in self.customers:
            self.customers.append(customer)
            print("Customer added successfully.")
        else:
            print("Invalid customer or customer already exists.")

    def rentVehicle(self, vehicle, customer, days):
        if isinstance(vehicle, Vehicle) and isinstance(customer, Customer):
            if vehicle.isAvailable():
                vehicle.rent()
                self.rentals.append(Rental(vehicle, customer, days))
                print("Vehicle rented successfully.")
            else:
                print("Vehicle is not available for rent.")
        else:
            print("Invalid vehicle or customer.")

    def returnVehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            if not vehicle.isAvailable(): #yahn pr car dkhy ga hai yan nhi
                vehicle.returnCar()
                rentalToRemove = None
                for rental in self.rentals:
                    if rental.getVehicle() == vehicle:
                        rentalToRemove = rental
                        break
                if rentalToRemove is not None: #agr car mil gai to tu usy return kryga  
                    self.rentals.remove(rentalToRemove)
                    print("Vehicle returned successfully.")
                else:
                    print("Vehicle was not rented.")
            else:
                print("Vehicle is not rented.")
        else:
            print("Invalid vehicle.")

    def menu(self):
        while True:
            print("===== Vehicle Rental System =====")
            print("1. Rent a Vehicle")
            print("2. Return a Vehicle")
            print("3. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print("\n== Rent a Vehicle ==\n")
                customerName = input("Enter your name: ")

                print("\nAvailable Vehicles:")
                for vehicle in self.vehicles:
                    if vehicle.isAvailable(): #loop in array list
                        if isinstance(vehicle, Car):
                            print(
                                f"{vehicle.getCarId()} - {vehicle.getBrand()} {vehicle.getModel()}"
                            )
                        # Add more vehicle types here if needed

                vehicleId = input("\nEnter the vehicle ID you want to rent: ")
                rentalDays = int(input("Enter the number of days for rental: "))

                newCustomer = Customer("CUS" + str(len(self.customers) + 1), customerName)
                self.addCustomer(newCustomer)

                selectedVehicle = None
                for vehicle in self.vehicles:
                    if isinstance(vehicle, Car) and vehicle.getCarId() == vehicleId and vehicle.isAvailable():
                        selectedVehicle = vehicle
                        break
                    # Add more conditions for other vehicle types here if needed

                if selectedVehicle is not None: #available
                    totalPrice = selectedVehicle.calculatePrice(rentalDays)
                    print("\n== Rental Information ==\n")
                    print("Customer ID: " + newCustomer.getCustomerId())
                    print("Customer Name: " + newCustomer.getName())
                    print("Vehicle: " + selectedVehicle.getBrand() + " " + selectedVehicle.getModel())
                    print("Rental Days: " + str(rentalDays))
                    print("Total Price: $%.2f" % totalPrice)

                    confirm = input("\nConfirm rental (Y/N): ")
                    if confirm.upper() == "Y":
                        self.rentVehicle(selectedVehicle, newCustomer, rentalDays)
                        print("\nVehicle rented successfully.")
                    else:
                        print("\nRental canceled.")
                else:
                    print("\nInvalid vehicle selection or vehicle not available for rent.")
            elif choice == 2:
                print("\n== Return a Vehicle ==\n")
                vehicleId = input("Enter the vehicle ID you want to return: ")

                vehicleToReturn = None
                for vehicle in self.vehicles:
                    if isinstance(vehicle, Car) and vehicle.getCarId() == vehicleId and not vehicle.isAvailable():
                        vehicleToReturn = vehicle
                        break
                    
                if vehicleToReturn is not None: #available
                    customer = None
                    for rental in self.rentals:
                        if rental.getVehicle() == vehicleToReturn:
                            customer = rental.getCustomer()
                            break

                    if customer is not None:
                        self.returnVehicle(vehicleToReturn)
                        print("Vehicle returned successfully by " + customer.getName())
                    else:
                        print("Vehicle was not rented or rental information is missing.")
                else:
                    print("Invalid vehicle ID or vehicle is not rented.")
            elif choice == 3:
                break
            else:
                print("Invalid choice. Please enter a valid option.")

        print("\nThank you for using the Vehicle Rental System!")


rentalSystem = CarRentalSystem()

car1 = Car("C001", "Toyota", "Camry", 60.0)
car2 = Car("C002", "Honda", "Accord", 70.0)
car3 = Car("C003", "Tesla", "T45", 150.0)
rentalSystem.addVehicle(car1)
rentalSystem.addVehicle(car2)
rentalSystem.addVehicle(car3)

rentalSystem.menu()