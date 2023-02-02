class Dog:
    
    def __init__(self, age, breed):
        self.age = age
        self.breed = breed

    def voice(self):
        print('Gav')


# obj identity - название 
# obj state - переменные
# obj behaviour - методы

tuzik = Dog(10, 'Ovcharka')
tuzik.voice()