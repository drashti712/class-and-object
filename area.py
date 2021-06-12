class cal6:
    def setdata(self):
        n1 = int(input("Enter length :"))
        self.n1 = n1
    def area(self):
        square = self.n1 * self.n1
        self.square = square
    def display(self):
        print("Area of the square=" + str(self.square))

c1 = cal6()
c1.setdata()
c1.area()
c1.display()