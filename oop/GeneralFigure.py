from abc import ABC, abstractmethod
class GeneralFigure(ABC):
    color = ""
    @abstractmethod
    def __init__(self, color):
        self.color = color
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

    def informationAboutFigure(self):
        print(" <---- General Information -----> ")
        print(" Figure : \t\t" + self.__class__.__name__)
        print(" color of figure : \t" + str(self.color))
        print(" area of figure : \t" + str(self.area()))
        print(" area of perimeter : \t" + str(self.perimeter()))