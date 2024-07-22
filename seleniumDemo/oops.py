class calc:
    def __init__(self,*args):
        self.a = args
        # self.b = b
    def add(self):
        s=0
        for ele in self.a:
            s+=ele
        self.display(s)
    def display(self,inp):
        print(inp)
    # def mul(self):
    #     return self.a * self.b

c = calc(2,4,6)
c.add()
# print(c.mul())
