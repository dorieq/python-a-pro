class Animal:
    def __init__(self) -> None:
        pass
        
    def sound(self):
        print('Sound')

class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()
    
    def sound(self):
        print('Gav')

class Cat(Animal):
    def __init__(self) -> None:
        super().__init__()
    
    def sound(self): #Override
        print('Meow')

a = Animal()
tuzik = Dog()
cat = Cat()
a.sound()
tuzik.sound()
cat.sound()