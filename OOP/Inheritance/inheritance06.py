class A:
    def __init__(self , n = "Muzzamil"):
        self.name = n

class B(A):
    def __init__(self, roll ):
        self.roll = roll
obj = B(23)
print(obj.name)