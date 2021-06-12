class cal2:
    def setdata(self,r):
        self.radius=r

    def display(self):
        return self.radius**2*3.14
c1=cal2()
c1.setdata(5)
print(c1.display())


