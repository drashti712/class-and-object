class arith:
    def init(self,a,b):
        self.a = a
        self.b = b
    def _add_(self):
        print(f"Add operation on {self.a} and {self.b}")
        return self.a+self.b
    def _sub_(self):
        print(f"Sub operation on {self.a} and {self.b}")
        return self.a-self.b
    def _mul_(self):
        print(f"Multi operation on {self.a} and {self.b}")
        return self.a*self.b

a1= arith()
a1.init(10,20)
a1._add_()
a1._sub_()
a1._mul_()