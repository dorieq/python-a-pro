class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        print(self.x + self.y)

class Point2(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def add(self, p):
        print(self.x + p.x)
        print(self.y + p.y)

P = Point(2, 4)
P2 = Point2(3, 3)
P2.add(P)