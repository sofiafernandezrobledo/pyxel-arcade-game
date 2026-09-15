import pyxel

from Enemigos.enemigos import Enemigo

class Tortuga(Enemigo):

    def __init__(self, x, y, v, w, l, direccion, score, alive, moving, tiempo, revivir):

        Enemigo.__init__(self, x, y, v, w, l, direccion, score, alive, moving, tiempo, revivir)

    def update(self, plataformas):
        self.colisionarriba = self.col_suelo(plataformas)

        if self.alive:
            if self.moving:
                if self.point.y + self.dimensiones.l < self.arriba:
                    self.point.y -= self.dimensiones.v
                    self.dimensiones.v -= 1
                elif self.point.y + self.dimensiones.l >= self.arriba:
                    self.point.y = self.arriba - self.dimensiones.l

                if self.direccion %2==0:
                    if self.point.x <250:
                        self.point.x +=1
                    else:
                        self.point.x = 0
                    
                    if self.point.x > 200 and self.point.y + self.dimensiones.l > 235: 
                        self.point.y = 230
                    elif self.point.x > 214 and self.point.y + self.dimensiones.l >230:
                        self.point.x = 35
                        self.point.y = 8
                else: 
                    if self.point.x > 0:
                        self.point.x -=1
                    else:
                        self.point.x = 235
                    
                    if self.point.x < 50 and self.point.y + self.dimensiones.l > 235: 
                        self.point.y = 230
                    elif self.point.x+ self.dimensiones.w < 35 and self.point.y + self.dimensiones.l >230:
                        self.point.x = 235
                        self.point.y = 8

            else:
                if self.tiempo == 0:
                    self.tiempo = 50
                    self.moving = True
                    self.revivir = True

                else:
                    self.tiempo -= 1

    def draw(self):
        if self.alive:
            if self.moving:
                if self.direccion%2==0:
                    if self.point.x %3==0: 
                        pyxel.blt(self.point.x, self.point.y, 1, 6, 92, self.dimensiones.w, self.dimensiones.l, 0) #tortuga derecha enfadada
                    else:
                        pyxel.blt(self.point.x, self.point.y, 1, 54, 92, self.dimensiones.w, self.dimensiones.l, 0) #tortuga derecha contenta
                else:
                    if self.point.x %3==0: 
                        pyxel.blt(self.point.x, self.point.y, 1, 26, 92, self.dimensiones.w, self.dimensiones.l, 0) #tortuga izquierda enfadada
                    else:
                        pyxel.blt(self.point.x, self.point.y, 1, 74, 92, self.dimensiones.w, self.dimensiones.l, 0) #tortuga izquierda contenta

                if self.revivir:
                    if self.direccion%2==0:
                        if self.point.x %3==0: 
                            pyxel.blt(self.point.x, self.point.y, 1, 6, 116, self.dimensiones.w, self.dimensiones.l, 0) #tortuga derecha enfadada
                        else:
                            pyxel.blt(self.point.x, self.point.y, 1, 54, 116, self.dimensiones.w, self.dimensiones.l, 0) #tortuga derecha contenta
                    else: 
                        if self.point.x %3==0: 
                            pyxel.blt(self.point.x, self.point.y, 1, 26, 116, self.dimensiones.w, self.dimensiones.l, 0) #tortuga izquierda enfadada
                        else:
                            pyxel.blt(self.point.x, self.point.y, 1, 74, 116, self.dimensiones.w, self.dimensiones.l, 0) #tortuga izquierda contenta
            else: 
                pyxel.blt(self.point.x, self.point.y+4, 1, 234,97,12,11, 0) #se cambia a modo caparazón 

               


    def col_suelo(self, plataformas):
        for j in range(len(plataformas)):
            x = plataformas[j].point.x
            y = plataformas[j].point.y
            width = plataformas[j].dimensiones.w

            # si la tortuga toca la plataforma, el metodo devuelve true
            if ((self.point.x >= x and self.point.x <= x + width) or ((self.point.x + self.dimensiones.w) >= x and (self.point.x + self.dimensiones.w) <= x + width)) and (self.point.y + self.dimensiones.l >= y - 5 and self.point.y + self.dimensiones.l <= y + 5):
                self.point.y = y - 1 - self.dimensiones.l
                self.dimensiones.v = 0
                self.arriba = y
                return True
            
            elif j == len(plataformas) - 1:
                self.arriba = 235
                return False              
        
