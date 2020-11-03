# 1. Создать базовый клас который описывает геометрическую фигуру (можно абстрактный). 
# Так же нужно создать класы которые описывают эллипс, круг, треугольник, 
# равнобедренный треугольник, равносторонний треугольник, прямоугольник, квадрат. 
# Все классы должны иметь методы вычисления площади и периметра.
from Circle import Circle
# from GeneralFigure import GeneralFigure
from Ellipse import Ellipse
from Triangle import Triangle
from IsoscelesTriangle import IsoscelesTriangle
from EquilateralTriangle import EquilateralTriangle
from Square import Square
from Rectangle import Rectangle

class CreateObjects:
    if __name__ == '__main__':
        figure1 = Circle("red", 12)
        figure2 = Ellipse("pink", 9, 15)
        figure3 = Triangle("black", 4, 7, 10)
        figure4 = IsoscelesTriangle("none", 6, 10)
        figure5 = EquilateralTriangle("millitary", 7)
        figure6 = Square("red", 6)
        figure7 = Rectangle("green", 6, 12)
    
        listFigures = [figure1, figure2, figure3, figure3, figure4, figure5, figure6, figure7]
        for shape in listFigures:
            print ("========= Number : " + str(listFigures.index(shape) + 1) + " ============")
            shape.informationAboutFigure()

        # print("======     first figure     =======")
        # figure1.informationAboutFigure()
        # print("======     second figure     =======")
        # figure2.informationAboutFigure()
      
