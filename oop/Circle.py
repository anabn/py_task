import math
from GeneralFigure import GeneralFigure

class Circle(GeneralFigure):
    def __init__(self, color, radius):
        GeneralFigure.__init__(self, color)
        self.radius = radius

    def area(self):
        return round(math.pi, 3) * self.radius**2
    
    def perimeter(self):
        return 2 * self.radius * round(math.pi, 3)
    
    def informationAboutFigure(self):
        super().informationAboutFigure()