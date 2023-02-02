class Person:

    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def display(self):
        print(self.name)
        print(self.id)

class Employee(Person):
    def __init__(self, name, id, salary, post):
        super().__init__(name, id)
        self.salary = salary
        self.post = post
    
    def display(self):
        super().display()
        print(self.salary)
        print(self.post)

p = Employee('Dauren', 123, 600, 'Dev')
p.display()