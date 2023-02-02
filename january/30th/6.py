class Grandparent:
    def __init__(self, name):
        self.name = name

class Dad(Grandparent):
    def __init__(self, name, work):
        super().__init__(name)
        self.work = work

class Boy(Dad):
    def __init__(self, name, work, school):
        super().__init__(name, work)
        self.school = school

gp = Grandparent('Askar')
d = Dad('Almas', 'Principal')
b = Boy('Abzal', 'Student', 'AGU')
