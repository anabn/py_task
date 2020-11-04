import math
from GeneralFigure import GeneralFigure

class Square(GeneralFigure):
    def __init__(self, color, a):
        GeneralFigure.__init__(self, color)
        self.a = a

    def area(self):
        return self.a**2
    
    def perimeter(self):
        return 4 * self.a
    
    def informationAboutFigure(self):
        super().informationAboutFigure()