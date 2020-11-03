import math
from GeneralFigure import GeneralFigure

# need method for check correspondence of the sides of the triangle

class Triangle(GeneralFigure):
    def __init__(self, color, a, b, c):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        return self.a + self.b + self.c 

    def area(self):
        halfP = self.perimeter()
        return round(math.sqrt(halfP * (halfP - self.a) * (halfP - self.b) * (halfP - self.c)), 3)
    
    def informationAboutFigure(self):
        super().informationAboutFigure()