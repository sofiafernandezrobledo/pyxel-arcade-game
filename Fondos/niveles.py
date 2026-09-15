class Nivel:

    def __init__(self, framecount, deadplayer, level, enemigos, plataformas, monedas, color):
        self.framecount = framecount
        self.dead = deadplayer
        self.level = level
        self.enemigos = enemigos
        self.monedas = monedas
        self.plataformas = plataformas
        self.color = color
class Pantalla:
    def __init__(self, deadplayer, level, monedas, plataformas, tiempo):
        self.dead = deadplayer
        self.level = level
        self.monedas = monedas
        self.plataformas = plataformas
        self.tiempo = tiempo
