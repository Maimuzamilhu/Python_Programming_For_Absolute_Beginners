#Apply inheritance concept write a class polygon with a method that takes number of side as input and another method that displays it . create a subclass triangle which calls input and display methods from the parent class and contains a method to calculate the area of triangle. create object for trianglle and call method to take input . calculate area of a triangle and display the result and show the output

class Polygon:
    def __init__(self):
        self.n = 0

    def sides(self):
        self.a = float(input("Enter the Side 1 :"))
        self.b = float(input("Enter the Side 2 :"))
        self.c = float(input("Enter the Side 3 :"))

    def dis(self):
        print(f"{self.a} and {self.b} and {self.c}")
    
class Triangle(Polygon):
    def __init__(self):
        super().__init__()
        self.a = 0
        self.b = 0
        self.c = 0

    def sol(self):
        # calculate the semi-perimeter
        s = (self.a + self.b + self.c) / 2
        # calculate the area
        area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)



# creating object of subclass and calling methods
t = Triangle()
t.sides()
t.dis()
t.sol()
