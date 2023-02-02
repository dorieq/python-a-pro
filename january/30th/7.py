class P1:
    def __init__(self):
        self.a = 1
        print(self.a)

class P2:
    def __init__(self):
        self.b = 2
        print(self.b)

class P3(P1, P2):
    def __init__(self):
        P1.__init__(self)
        P2.__init__(self)

p = P3()
print(vars(p))