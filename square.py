class cal4:
    def setdata(self,no):
        self.num = no
    def display(self):
        answer = self.num * self.num
        print("Square of number: ",answer)
c1 = cal4()
c1.setdata(7)
c1.display()