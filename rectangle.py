class cal5():
    def __init__(self,breadth,length):
        self.breadth = breadth
        self.length = length
    def display(self):
        return self.breadth*self.length

a = int(input("Enter length: "))
b = int(input("Enter breadth: "))
obj = cal5(a,b)
print("Area of rectangle:",obj.display())
print()