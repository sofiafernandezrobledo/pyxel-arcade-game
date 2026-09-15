import pyxel
import random
from Constantes.dimensiones import Dimension
from Constantes.point import Point

class Moneda:
    def __init__(self, x, y):
        self.point = Point(x,y)
        self.dimensiones = Dimension(0, 8, 11)
        self.__lado = 1
        self.disponible = True


    def draw(self):
        if self.disponible:
            self.__lado+= random.randint(0,1)
            if self.__lado%5==0:
                pyxel.blt(self.point.x, self.point.y, 0, 166, 138, self.dimensiones.w, self.dimensiones.l, 0)
            elif self.__lado%3==0:
                self.dimensiones.w = 4
                pyxel.blt(self.point.x+2, self.point.y, 0, 157, 138, self.dimensiones.w, self.dimensiones.l, 0)
            elif self.__lado%2==0:
                self.dimensiones.w = 1
                pyxel.blt(self.point.x+4, self.point.y, 0, 151, 138, self.dimensiones.w, self.dimensiones.l, 0)
            else:
                self.dimensiones.w = 8
                pyxel.blt(self.point.x, self.point.y, 0, 166, 138, self.dimensiones.w, self.dimensiones.l, 0)