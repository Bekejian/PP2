class Shape:
    def _init_(self):
        pass  

class Rectangle(Shape):
    def _init_(self, length, width):
        super()._init()  
        self.length = length  
        self.width = width 
    def area(self):
        return self.length * self.width  


rect = Rectangle(4, 5)


print(rect.area())  