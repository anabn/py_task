import math
from GeneralFigure import GeneralFigure

class Rectangle(GeneralFigure):
    def __init__(self, color, a, b):
        super().__init__(color)
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b
    
    def perimeter(self):
        return 2 * (self.a + self.b)
    
    def informationAboutFigure(self):
        super().informationAboutFigure()