#Apply inheritance concept write a class polygon with a method that takes number of side as input and another method that displays it . create a subclass triangle which calls input and display methods from the parent class and contains a method to calculate the area of triangle. create object for trianglle and call method to take input . calculate area of a triangle and display the result and show the output

class polygon:
    def __init__(self):
        self.n = int(input("Enter the Side :"))

    def display(self):
        print(f"Display the Input {self.n}")
    
class triangle(polygon):
    def __init__(self):
        super().__init__(self)
        self.a = 0
        self.b = 0
        self.c = 0

    def input_side(self):
        self.a = float(input("Enter the Side a :"))
        self.b = float(input("Enter the Side b :"))
        self.c = float(input("Enter the Side c :"))

    def area(self):
        s = (self.a + self.b + self.c) / 2
        # calculate the area
        return s
   
t = triangle()
t.input_side()

        