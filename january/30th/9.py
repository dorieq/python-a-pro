class Point:
    
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def sum(self):
        print(self.x + self.y)

class P1(Point):

    def __init__(self, x, y) -> None:
        super().__init__(x, y)

    def sum(self, P):
        print(self.x + P.x)
        print(self.y + P.y)

p = Point(2, 3)
p.sum()
p1 = P1(4, 5)
p1.sum(p)