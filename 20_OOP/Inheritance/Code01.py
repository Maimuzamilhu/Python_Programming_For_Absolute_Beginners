
class Pso:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
        
    def info_pso(self):
        print("__________________________________________________________________________________________________________________")
        print(f"\n{self.name}'s Info:")
        print(f"\nName: {self.name}______Salary: {self.salary}______Age: {self.age}.")
        print(f"{self.name} works in PSO company and his salary is {self.salary} while his age is {self.age}.")
        print(f"PSO company is amazed by {self.name}'s work and decided to increase salary from {self.salary} to 10lacs/month.")


class PsoSteelmills(Pso):

    def info_pso_steelmills(self):
        
        self.info_pso()
        print(f"\n{self.name} also works in steelmills.")
        print(f"{self.name} is a hard worker there.")
        

a = PsoSteelmills("Rayyan Ahmed", "500000", "18")
b = PsoSteelmills("Muzammil", "450000", "19")
c = Pso("Wajahat", "370000", "19")
d = Pso("Hamza", "360000", "20")
e = PsoSteelmills("Sami", "460000", "20")


a.info_pso_steelmills()
b.info_pso_steelmills()
c.info_pso()
d.info_pso()
e.info_pso_steelmills()
# Print the method resolution order of the Pso class
print(Pso.mro())
