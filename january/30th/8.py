class Animal:
    def __init__(self) -> None:
        pass

    def sound(self):
        print('Sound')

class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()
    
    def sound(self):
        print('gav') # override

class Cat(Animal):
    def __init__(self) -> None:
        super().__init__()

    def sound(self):
        print('Meow')

barsik = Cat()
tuzik = Dog()
barsik.sound()
tuzik.sound()