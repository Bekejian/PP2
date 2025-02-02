class Shape:
    def _init_(self):
        self.area_value = 0

    def area(self):
        return self.area_value

class Square(Shape):
    def _init_(self, length):
        super()._init_()
        self.length = length

    def area(self):
        return self.length ** 2

sq = Square(5)
print(sq.area())  