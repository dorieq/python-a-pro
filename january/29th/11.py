class Base:
    def __init__(self):
        self.a = 2
        self.__b = 5
    
    def details(self):
        print(self.__b)

b = Base()
print(b.a)
print(vars(b))
b.details()