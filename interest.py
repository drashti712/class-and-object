class cal3:
    def callinterest(self,p,r,n):
        self.pri = p
        self.rate = r
        self.num = n
    def display(self):
        SI = (self.pri * self.num * self.rate)/100
        print("Interest: {} ".format(SI))
C1=cal3()
C1.callinterest(10,20,30)
C1.display()