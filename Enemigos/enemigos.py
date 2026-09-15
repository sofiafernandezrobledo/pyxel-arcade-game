from Constantes.point import Point
from Constantes.dimensiones import Dimension


class Enemigo:
    def __init__(
        self,
        x,
        y,
        v,
        w,
        l,
        direccion,
        score,
        alive,
        moving,
        tiempo,
        revivir
    ):
        self.point = Point(x, y)
        self.dimensiones = Dimension(v, w, l)
        self.direccion = direccion
        self.score = score
        self.alive = alive
        self.moving = moving
        self.tiempo = tiempo
        self.revivir = revivir

    