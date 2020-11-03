# 1. Создать базовый клас который описывает геометрическую фигуру (можно абстрактный). 
# Так же нужно создать класы которые описывают эллипс, круг, треугольник, 
# равнобедренный треугольник, равносторонний треугольник, прямоугольник, квадрат. 
# Все классы должны иметь методы вычисления площади и периметра.
from Circle import Circle
# from GeneralFigure import GeneralFigure
from Ellipse import Ellipse
from Triangle import Triangle
from IsoscelesTriangle import IsoscelesTriangle

class CreateObjects:
    if __name__ == '__main__':
        figure1 = Circle("red", 12)
        figure2 = Ellipse("pink", 9, 15)
        figure3 = Triangle("black", 4, 7, 10)
        figure4 = IsoscelesTriangle("none", 6, 10)
        print("======     first figure     =======")
        figure1.informationAboutFigure()
        print("======     second figure     =======")
        figure2.informationAboutFigure()
        print("======     third figure     =======")
        figure3.informationAboutFigure()
        print("======     forth figure     =======")
        figure4.informationAboutFigure()
