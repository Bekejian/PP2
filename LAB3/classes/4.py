import math  

class Point:
    def _init_(self, x, y):
        self.x = x  
        self.y = y  

    def show(self):
        print(f"({self.x}, {self.y})")
    def move(self, dx, dy):
        self.x += dx  
        self.y += dy  

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) * 2 + (self.y - other_point.y) * 2)


p1 = Point(1, 2)  
p2 = Point(4, 6)  


print(p1.dist(p2))  