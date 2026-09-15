import pyxel
from Constantes.point import Point 
from Constantes.dimensiones import Dimension 
from Fondos.plataformas import Plataforma
from Enemigos.cangrejos import Cangrejo


class Marioplayer():
    
    def __init__(self):
           
        self.point = Point(115, 210)
        self.dimensiones = Dimension(0, 15, 22)
        self.__saltando = False
        self.__is_alive = True
        self.vidas = 3
        self.__lado = 1
        self.__revivir = False
        self.puntuacion = 0
        self.bajando = False
        self.__plataforma = Plataforma (0,0,0)
            
    def move(self, plataformas, pow, enemigos):
        self.arribaplataforma(plataformas)
        self.abajoplataforma(plataformas, enemigos)
        self.colision_powmario(pow, enemigos, plataformas)

        if pyxel.btnp(pyxel.KEY_SPACE) and not self.__saltando:
            self.dimensiones.v = 8
            self.point.y -= 10  
            self.__saltando = True

        if self.__revivir:
            self.point.y -= 0.000001 

        if self.point.y + self.dimensiones.l < self.arriba:
            self.point.y -= self.dimensiones.v
            self.dimensiones.v -= 1
        elif self.point.y + self.dimensiones.l >= self.arriba:
            self.point.y = self.arriba - self.dimensiones.l
            self.__saltando = False
        elif self.point.y > self.abajo:
            self.point.y -= self.dimensiones.v
            self.dimensiones.v -= 1
        
        if pyxel.btn(pyxel.KEY_LEFT):
            self.__lado = 1
            if self.point.x <-13:
                self.point.x =245
            self.point.x -= 3
        
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.__lado=2
            if self.point.x >245:
                self.point.x = -13
            self.point.x +=3

            
    def draw_mario(self):
        if self.__is_alive == True:
            if self.__revivir == True:
                pyxel.blt(self.point.x-1, self.point.y+self.dimensiones.l, 0, 120, 138, 15, 5, 0)

            if self.__lado %2 ==0 and self.__saltando == True: #movimiento derecha
                pyxel.blt(self.point.x, self.point.y, 2, 112, 163, self.dimensiones.w, self.dimensiones.l, 0)
            elif self.__lado %2 ==1 and self.__saltando == True: #movimiento izquierda          
                pyxel.blt(self.point.x, self.point.y, 2, 93, 163, self.dimensiones.w, self.dimensiones.l,0)
            elif self.__lado %2 == 0 and self.__saltando == False: #derecha
                self.dimensiones.l = 21
                if self.point.x %2 ==0: #movimiento correr derecha
                    self.dimensiones.w = 14
                    pyxel.blt(self.point.x, self.point.y, 2, 71, 164,self.dimensiones.w, self.dimensiones.l, 0)
                else:
                    self.dimensiones.w = 16
                    pyxel.blt (self.point.x, self.point.y,2, 22, 164, self.dimensiones.w, self.dimensiones.l, 0)
            elif self.__lado %2 == 1 and self.__saltando == False: #izquierda
                self.dimensiones.l = 21
                if self.point.x %2 ==0: #movimiento de correr izquierda
                    self.dimensiones.w = 14
                    pyxel.blt(self.point.x, self.point.y,2, 54, 164, self.dimensiones.w, self.dimensiones.l, 0)
                else:
                    self.dimensiones.w = 16
                    pyxel.blt (self.point.x, self.point.y, 2, 3, 164, self.dimensiones.w, self.dimensiones.l,0)
            elif self.__saltando == False:
                self.dimensiones.w, self.dimensiones.l = 16, 21
                pyxel.blt (self.point.x, self.point.y, 2, 3, 164, self.dimensiones.w, self.dimensiones.l,0)
        

    def arribaplataforma(self,plataformas):
        for j in range(len(plataformas)):
            x = plataformas[j].point.x
            y = plataformas[j].point.y
            width = plataformas[j].dimensiones.w

            if ((self.point.x >= x and self.point.x <= x + width) or ((self.point.x + self.dimensiones.w) >= x and (self.point.x + self.dimensiones.w) <= x + width)) and (self.point.y + self.dimensiones.l >= y - 5 and self.point.y + self.dimensiones.l <= y + 5):
                self.point.y = y - 1 - self.dimensiones.l
                self.dimensiones.v = 0
                self.__saltando = False
                self.__revivir = False
                self.arriba = y
                return True
            
            elif j == len(plataformas) - 1:
                self.arriba = 235
                return False
            
    def abajoplataforma(self, plataformas, enemigos):
            for j in range(len(plataformas)):
                x = plataformas[j].point.x
                y = plataformas[j].point.y
                width = plataformas[j].dimensiones.w
                length = plataformas[j].dimensiones.l

                if ((self.point.x >= x and self.point.x <= x + width) or ((self.point.x + self.dimensiones.w) >= x and (self.point.x + self.dimensiones.w) <= x + width)) and (self.point.y >= y - 5 and self.point.y <= y + 5):
                    self.point.y = y + length
                    self.dimensiones.v = 0
                    self.abajo = y + length
                    self.col_enemigosuelomario(plataformas, enemigos)
                    self.__plataforma.draw_colision(y, self.point.x, x, width)
                    return True
                
                elif j == len(plataformas) - 1:
                    self.abajo = 235
                    return False
    
    
    def colisionenemigos(self, enemigos):
        i = 0
        while i < len(enemigos):
            x = enemigos[i].point.x
            y = enemigos[i].point.y
            w = enemigos[i].dimensiones.w
            l = enemigos[i].dimensiones.l
            if ((x + w > self.point.x and x < self.point.x + self.dimensiones.w) or (x < self.point.x and x > self.point.x + self.dimensiones.w)) and (y > self.point.y and y < self.point.y + self.dimensiones.l) and enemigos[i].moving:
                self.__revivir = True
                self.point.x = 110
                self.point.y = 0
                
                if self.vidas>1:
                    self.vidas -=1
                elif self.vidas == 1:
                    self.vidas -=1
                    self.__is_alive = False

                    with open("score.txt", "r") as file:
                        high_score = int(file.read().strip() or 0)

                    if self.puntuacion > high_score:
                        with open("score.txt", "w") as file:
                            file.write(str(self.puntuacion))

            if ((x + 17 > self.point.x and x + 17 < self.point.x + 15) or
                (x < self.point.x and x > self.point.x + 15)) and \
                    (y > self.point.y and y < self.point.y + 22) and \
                    enemigos[i].moving == False:

                self.puntuacion += enemigos[i].score
                del enemigos[i]

            else:
                i += 1

    def col_enemigosuelomario(self, plataformas, enemigos):
        for i in range(len(enemigos)):
            x = enemigos[i].point.x
            y = enemigos[i].point.y
            w = enemigos[i].dimensiones.w
            l = enemigos[i].dimensiones.l
            if enemigos[i].col_suelo(plataformas)==True and ((x + w > self.point.x and x  < self.point.x + self.dimensiones.w) or (x < self.point.x and x > self.point.x + self.dimensiones.w)) and (y + l >= self.point.y - 10):
                if enemigos[i].moving == True:
                    if isinstance(enemigos[i], Cangrejo):
                        enemigos[i].ungolpe = True
                    else:
                        enemigos[i].moving = False
                elif isinstance(enemigos[i], Cangrejo):
                    if enemigos[i].ungolpe:
                        enemigos[i].ungolpe = False
                        enemigos[i].moving = False
                else:
                    enemigos[i].moving = True

    def colision_powmario(self, pow, enemigos, plataformas):
        xpow = pow.point.x
        ypow = pow.point.y
        lpow = pow.dimensiones.l
        wpow = pow.dimensiones.w
        if pow.disponible==True:
            if ((self.point.x >= xpow and self.point.x <= xpow + wpow) or ((self.point.x + self.dimensiones.w) >= xpow and (self.point.x + self.dimensiones.w) <= xpow + wpow)) and (self.point.y >= ypow - 5 and self.point.y <= ypow + 5):
                self.point.y = ypow + lpow
                self.dimensiones.v = 0
                self.abajo = ypow + lpow
                pow.num_col +=1   
                for i in range(len(enemigos)):
                    if enemigos[i].col_suelo(plataformas)==True:
                        enemigos[i].moving = False

    def colision_mariomoneda(self, monedas):
        for m in range(len(monedas)):
            x = monedas[m].point.x
            y = monedas[m].point.y
            if (self.point.x+15>x and self.point.x<x+8 and self.point.y<=y+11 and self.point.y+22>y):
                if monedas[m].disponible == True:
                    self.puntuacion +=10
                    monedas[m].disponible = False
                