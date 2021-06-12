class cal1:
    def setdata(self,n1,n2,n3):
        self.num1 = n1
        self.num2 = n2
        self.num3 = n3
    def display(self):
        sum= self.num1+self.num2+self.num3
        print(sum)

c1=cal1()
c1.setdata(10,20,30)
c1.display()
