import pyxel
from Constantes.point import Point
from Constantes.dimensiones import Dimension

class Pow:
    def __init__(self):
        self.point = Point(120, 180)
        self.dimensiones = Dimension(0, 16, 16)
        self.num_col=0
        self.disponible = True

    def draw(self):
        if self.disponible == True:
            pyxel.blt(self.point.x, self.point.y, 1, 133, 3, self.dimensiones.w, self.dimensiones.l, 0)