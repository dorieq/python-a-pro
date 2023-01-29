class Dog:
    name = ''
    breed = ''

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

d = Dog('Tuzik', 'Ovcharka')
d.name = 'Sharik'
print(d.name)
print(d.breed)