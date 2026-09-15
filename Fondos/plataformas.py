
import pyxel
from Constantes.point import Point
from Constantes.dimensiones import Dimension

class Plataforma:
    def __init__(self,x, y, w):
        self.point = Point(x, y)
        self.dimensiones = Dimension(0, w,8)

    def draw_plataforma(self):
        pyxel.blt(self.point.x, self.point.y, 2, 9, 236, self.dimensiones.w, self.dimensiones.l, 0)

    def draw_colision(self, y, x, xplat, width):
        self.point.x = xplat
        self.dimensiones.w = 38
        self.dimensiones.l = 15
        self.empieza = 8

        if (x-12) < self.point.x:
            self.empieza += self.point.x - (x-12)
            self.dimensiones.w -= self.empieza - 8
            pyxel.blt(self.point.x, y-7, 2, self.empieza, 216, self.dimensiones.w, self.dimensiones.l, 0)

        elif (x + 26) > self.point.x + width:
            self.dimensiones.w -= (x + 26) - (self.point.x + width)
            pyxel.blt(x - 12, y-7, 2, self.empieza, 216, self.dimensiones.w, self.dimensiones.l, 0)

        else:
            pyxel.blt(x- 12, y- 7, 2, self.empieza, 216, self.dimensiones.w, self.dimensiones.l, 0)

    def draw_plataforma_bonif(self):
        pyxel.blt(self.point.x, self.point.y, 1, 133, 26, self.dimensiones.w, self.dimensiones.l)