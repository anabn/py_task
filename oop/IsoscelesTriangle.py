import math
from GeneralFigure import GeneralFigure

# need method for check correspondence of the sides of the triangle

class IsoscelesTriangle(GeneralFigure):
    def __init__(self, color, a, b):
        GeneralFigure.__init__(self, color)
        self.a = a
        self.b = b
    
    def perimeter(self):
        return self.a + 2 * self.b

    def area(self):
        halfP = self.perimeter()
        return round(math.sqrt(halfP * (halfP - self.a) * 2 * (halfP - self.b)), 3)
    
    def informationAboutFigure(self):
        super().informationAboutFigure()