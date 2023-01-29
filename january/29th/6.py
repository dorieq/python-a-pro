class Base1:
    def __init__(self):
        self.str1 = 'AB'
        print(self.str1)

class Base2:
    def __init__(self):
        self.str1 = 'BC'
        print(self.str1)

class Derived(Base1, Base2):
    def __init__(self):
        Base2.__init__(self)
        Base1.__init__(self)
        print(self.str1)
        print('ABC')

d = Derived()