class first:
    def __init__(self , Name , Fname ):
        self.Name = Name
        self.Fname = Fname

class second(first):
    def __init__(self, Name , Fname , year):
        super().__init__(Name , Fname)
        self.Year_ofG = year

    def welcome(self):
        print(f"Hi {self.Name} {self.Fname} your graduation Year is {self.Year_ofG}")

p = second("Muzzamil" , "Khalid" , 2022)
p.welcome()
