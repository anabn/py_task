import math
from GeneralFigure import GeneralFigure

class EquilateralTriangle(GeneralFigure):
    def __init__(self, color, a):
        super().__init__(color)
        self.a = a

    def area(self):
        return round(self.a**2 * math.sqrt(3) / 4, 3)
    
    def perimeter(self):
        return 3 * self.a
    
    def informationAboutFigure(self):
        super().informationAboutFigure()