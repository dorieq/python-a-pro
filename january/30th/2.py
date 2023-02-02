class Dog:

    def __init__(self, age, breed):
        self.age = age
        self.breed = breed

dog = Dog(12, 'Ovcharka')
dog.age = 13
print(dog.age)
print(dog.breed)