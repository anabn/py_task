import math
from GeneralFigure import GeneralFigure

class Ellipse(GeneralFigure):
    def __init__(self, color, exalA, exalB):
        super().__init__(color)
        self.exalA = exalA
        self.exalB = exalB

    def area(self):
        return round(round(math.pi, 3) * self.exalA * self.exalB, 3)
    
    def perimeter(self):
        return round(
                round(math.pi, 3) * ( 3 * (self.exalA + self.exalB) - math.sqrt((3*self.exalA + self.exalB) * (self.exalA + 3*self.exalB))),
                3
            )
    
    def informationAboutFigure(self):
        super().informationAboutFigure()