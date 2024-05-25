class Vehicle:
    def _init_(self):
        self.color = 'black'
        self.seats = '4'
        self.weight = '50kg'
    def EngineSpec(self):
        self.number = 20
        self.avg = '5ltr'

class Bike(Vehicle):
    def _init_(self):
        super()._init_()
        self.ownername = 'Hamza'
        print(f'{self.seats}')
    def EngineSpec(self):
        super().EngineSpec()  # Call the parent class's EngineSpec() method
        self.life = '2years'
    def ShowOutput(self):
        print(f'Number: {self.number}\nAverage: {self.avg}\ncolor = {self.color}  ')

HamzaBike = Bike()
HamzaBike.EngineSpec() 
HamzaBike.ShowOutput()
print(HamzaBike.number)
