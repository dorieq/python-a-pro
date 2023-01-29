class Person:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name)
        print(self.id)

class Employee(Person):
    
    def __init__(self, salary, post, name, id):
        self.salary = salary
        self.post = post
        super().__init__(name, id)

    def display(self):
        print(self.salary)
        print(self.post)
        super().display()

a = Employee(600, 'Dev', 'Dauren', 123)
a.display()