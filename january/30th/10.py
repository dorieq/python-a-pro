class Base:

    def __init__(self) -> None:
        self.__a = 2

    def details(self):
        print(self.__a)
    
    def set(self, a):
        self.__a = a

b = Base()
b.set(10)
b.details()
## sql.execute('SELECT * FROM')