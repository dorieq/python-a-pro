class Dog:
    age = 0
    breed = ''

    def __init__(self, age, breed):
        self.age = age
        self.breed = breed

    def voice(self):
        print('Gav')
    
## object identity - название объекта
## object state - переменные объекта
## object behariour - методы объекта

tuzik = Dog(4, 'Labrador')
tuzik.voice()