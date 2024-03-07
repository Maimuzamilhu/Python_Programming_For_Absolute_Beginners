class table:
    def __init__(self , number):
        self.number = number

    def myfun(self):
        for i in range(1, 11):
            print(f"{self.number} * {i} = {self.number * i}")

num  = int(input("Enter the Number :"))

p1 = table(num)
p1.myfun()
