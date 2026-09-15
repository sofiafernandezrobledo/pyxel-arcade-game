import pyxel
import random
from Players.marioplayer import Marioplayer
from Fondos.tuberias import Tuberia
from Fondos.pow import Pow
from Fondos.niveles import Nivel, Pantalla



class Pantallainicio(Pantalla):

    def __init__(self, deadplayer, level, monedas, plataformas, tiempo):
        Pantalla.__init__(self, deadplayer, level, monedas, plataformas, tiempo)

    def update(self):
        if pyxel.btnp(pyxel.KEY_1):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0,10,1,51,6,48,30,0)
        pyxel.blt(218,210,1,11,18,32,18,0)
        pyxel.text(90, 140, "Press ENTER to play", 7)
        pyxel.blt(27, 50, 0, 16, 8, 216, 80, pyxel.frame_count % 25)
        pyxel.text(112,200,"CONTROLS", 7)
        pyxel.text(105,209,"Move - arrows",7)
        pyxel.text(97,218, "Jump - space key", 7)
        
class Pantallanivel1(Nivel):
    def __init__(self, framecount, deadplayer, level, enemigos, plataformas, monedas, color):

        Nivel.__init__(self, framecount, deadplayer, level, enemigos, plataformas, monedas, color)
        self.mario = Marioplayer()
        self.__pow = Pow()
        self.__tuberia = Tuberia()
        self.screenenemigos = []

    def update(self):

        if self.framecount == 0:
                self.framecount = 70
                if len(self.enemigos)>0:
                    a = random.randint(0, len(self.enemigos)-1)
                    self.screenenemigos.append(self.enemigos[a])
                    del(self.enemigos[a])
        else:
            self.framecount -= 1

        for i in range(len(self.screenenemigos)):
            self.screenenemigos[i].update(self.plataformas)
            self.screenenemigos[i].col_suelo(self.plataformas)

        if self.mario.vidas == 0:
            self.dead = True

        if self.mario.puntuacion >=10:
            self.level = True
        
        self.mario.colisionenemigos(self.screenenemigos)
        self.mario.arribaplataforma(self.plataformas)
        self.mario.colision_powmario(self.__pow, self.screenenemigos, self.plataformas)
        if self.__pow.num_col==3:
            self.__pow.disponible = False
        self.mario.colision_mariomoneda(self.monedas)
        self.mario.move(self.plataformas, self.__pow, self.enemigos)
        
    
            
    def draw(self):
        pyxel.cls(self.color)
        for i in range(len(self.plataformas)):
            self.plataformas[i].draw_plataforma()
        self.mario.abajoplataforma(self.plataformas, self.screenenemigos)

        for i in range(len(self.screenenemigos)):
            self.screenenemigos[i].draw()
        
        self.__pow.draw() 
        for x in range(len(self.monedas)):
            self.monedas[x].draw()

        self.__tuberia.draw() 

        for i in range(self.mario.vidas):
            pyxel.blt(55  + 10*i, 5, 2, 7, 153, 8, 6, 0)

        self.mario.draw_mario()
        pyxel.blt(0, 235, 1, 5, 53, 250, 15,0) #suelo 

        pyxel.blt(98,5, 0, 66, 137, 7, 7 , 0) #puntuación partida 
        pyxel.text(108, 6, str(self.mario.puntuacion), 7) #variable puntuación 
        pyxel.blt(130 ,5, 0, 77, 137, 20, 7, 0) #top puntuación 
        

class Pantallanivel2(Nivel):
    def __init__(self, framecount, deadplayer, level, enemigos, plataformas, monedas, color):

        Nivel.__init__(self, framecount, deadplayer, level, enemigos, plataformas, monedas, color)
        self.mario = Marioplayer()
        self.__pow = Pow()
        self.__tuberia = Tuberia()
        self.screenenemigos = []
        self.color = color

    def update(self):

        if self.framecount == 0:
                self.framecount = 100
                if len(self.enemigos)>0:
                    a = random.randint(0, len(self.enemigos)-1)
                    self.screenenemigos.append(self.enemigos[a])
                    del(self.enemigos[a])
        else:
            self.framecount -= 1

        for i in range(len(self.screenenemigos)):
            self.screenenemigos[i].update(self.plataformas)
            self.screenenemigos[i].col_suelo(self.plataformas)

        if self.mario.vidas == 0:
            self.dead = True

        if self.mario.puntuacion >=20:
            self.level = True

        self.mario.colisionenemigos(self.screenenemigos)
        self.mario.arribaplataforma(self.plataformas)
        self.mario.colision_powmario(self.__pow, self.screenenemigos, self.plataformas)
        if self.__pow.num_col==3:
            self.__pow.disponible = False
        self.mario.colision_mariomoneda(self.monedas)
        self.mario.move(self.plataformas, self.__pow, self.enemigos)
        
    
            
    def draw(self):
        pyxel.cls(self.color)
        for i in range(len(self.plataformas)):
            self.plataformas[i].draw_plataforma()
        self.mario.abajoplataforma(self.plataformas, self.screenenemigos)

        for i in range(len(self.screenenemigos)):
            self.screenenemigos[i].draw()
        
        self.__pow.draw() 
        for x in range(len(self.monedas)):
            self.monedas[x].draw()

        self.__tuberia.draw() 

        for i in range(self.mario.vidas):
            pyxel.blt(55  + 10*i, 5, 2, 7, 153, 8, 6, 0)

        self.mario.draw_mario()
        pyxel.blt(0, 235, 1, 5, 53, 250, 15,0) 

        pyxel.blt(98,5, 0, 66, 137, 7, 7 , 0) #puntuación partida 
        pyxel.text(108, 6, str(self.mario.puntuacion), 7) #variable puntuación 
        pyxel.blt(130 ,5, 0, 77, 137, 20, 7, 0) 


class Pantallanivel3(Nivel):
    def __init__(self, framecount, deadplayer, level, enemigos, plataformas, monedas, color):

        Nivel.__init__(self, framecount, deadplayer, level, enemigos, plataformas, monedas, color)
        self.mario = Marioplayer()
        self.__pow = Pow()
        self.__tuberia = Tuberia()
        self.screenenemigos = []

    def update(self):

        if self.framecount == 0:
                self.framecount = 100
                if len(self.enemigos)>0:
                    a = random.randint(0, len(self.enemigos)-1)
                    self.screenenemigos.append(self.enemigos[a])
                    del(self.enemigos[a])
        else:
            self.framecount -= 1

        for i in range(len(self.screenenemigos)):
            self.screenenemigos[i].update(self.plataformas)
            self.screenenemigos[i].col_suelo(self.plataformas)

        if self.mario.vidas == 0:
            self.dead = True

        if self.mario.puntuacion >=40:
            self.level = True

        self.mario.colisionenemigos(self.screenenemigos)
        self.mario.arribaplataforma(self.plataformas)
        self.mario.colision_powmario(self.__pow, self.screenenemigos, self.plataformas)
        if self.__pow.num_col==3:
            self.__pow.disponible = False
        self.mario.colision_mariomoneda(self.monedas)
        self.mario.move(self.plataformas, self.__pow, self.enemigos)
        
    
            
    def draw(self):
        pyxel.cls(self.color)
        for i in range(len(self.plataformas)):
            self.plataformas[i].draw_plataforma()
        self.mario.abajoplataforma(self.plataformas, self.screenenemigos)

        for i in range(len(self.screenenemigos)):
            self.screenenemigos[i].draw()
        
        self.__pow.draw() 
        for x in range(len(self.monedas)):
            self.monedas[x].draw()

        self.__tuberia.draw() 

        for i in range(self.mario.vidas):
            pyxel.blt(55  + 10*i, 5, 2, 7, 153, 8, 6, 0)

        self.mario.draw_mario()
        pyxel.blt(0, 235, 1, 5, 53, 250, 15,0) #suelo 

        pyxel.blt(98,5, 0, 66, 137, 7, 7 , 0) #puntuación partida 
        pyxel.text(108, 6, str(self.mario.puntuacion), 7) #variable puntuación 
        pyxel.blt(130 ,5, 0, 77, 137, 20, 7, 0) #top puntuación 

class Pantallanivel4(Nivel):
    def __init__(self, framecount, deadplayer, level, enemigos, plataformas, monedas, color):

        Nivel.__init__(self, framecount, deadplayer, level, enemigos, plataformas, monedas, color)
        self.mario = Marioplayer()
        self.__pow = Pow()
        self.__tuberia = Tuberia()
        self.screenenemigos = []

    def update(self):

        if self.framecount == 0:
                self.framecount = 100
                if len(self.enemigos)>0:
                    a = random.randint(0, len(self.enemigos)-1)
                    self.screenenemigos.append(self.enemigos[a])
                    del(self.enemigos[a])
        else:
            self.framecount -= 1

        for i in range(len(self.screenenemigos)):
            self.screenenemigos[i].update(self.plataformas)
            self.screenenemigos[i].col_suelo(self.plataformas)

        if self.mario.vidas == 0:
            self.dead = True

        if self.mario.puntuacion >=60:
            self.level = True


        self.mario.colisionenemigos(self.screenenemigos)
        self.mario.arribaplataforma(self.plataformas)
        self.mario.colision_powmario(self.__pow, self.screenenemigos, self.plataformas)
        if self.__pow.num_col==3:
            self.__pow.disponible = False
        self.mario.colision_mariomoneda(self.monedas)
        self.mario.move(self.plataformas, self.__pow, self.enemigos)
        
    
            
    def draw(self):
        pyxel.cls(self.color)
        for i in range(len(self.plataformas)):
            self.plataformas[i].draw_plataforma()
        self.mario.abajoplataforma(self.plataformas, self.screenenemigos)

        for i in range(len(self.screenenemigos)):
            self.screenenemigos[i].draw()
        
        self.__pow.draw() 
        for x in range(len(self.monedas)):
            self.monedas[x].draw()

        self.__tuberia.draw() 

        for i in range(self.mario.vidas):
            pyxel.blt(55  + 10*i, 5, 2, 7, 153, 8, 6, 0)

        self.mario.draw_mario()
        pyxel.blt(0, 235, 1, 5, 53, 250, 15,0) #suelo 

        pyxel.blt(98,5, 0, 66, 137, 7, 7 , 0) #puntuación partida 
        pyxel.text(108, 6, str(self.mario.puntuacion), 7) #variable puntuación 
        pyxel.blt(130 ,5, 0, 77, 137, 20, 7, 0) #top puntuación 

class Pantallawin(Pantalla):

    def __init__(self, deadplayer, level, monedas, plataformas, tiempo):
        Pantalla.__init__(self, deadplayer, level, monedas, plataformas, tiempo)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
                pyxel.quit()
    def draw(self):
        pyxel.cls(4)
        pyxel.text(120, 120, "WIN", 0) 
        with open("score.txt", "r") as file:
            high_score = file.read().strip()

        pyxel.text(100, 145, f"BEST SCORE {high_score}", 0)

class Pantalla_gameover(Pantalla):

    def __init__(self, deadplayer, level, monedas, plataformas, tiempo):
        Pantalla.__init__(self, deadplayer, level, monedas, plataformas, tiempo)
        self.mario = Marioplayer()

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
                pyxel.quit()
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(90, 120,0, 65, 151, 71, 7) 
        with open("score.txt", "r") as file:
            high_score = file.read().strip()

        pyxel.text(100, 145, f"BEST SCORE {high_score}", 7)

class Pantalla_monedas(Pantalla):
    def __init__(self, deadplayer, level, monedas, plataformas, tiempo):

        Pantalla.__init__(self, deadplayer, level, monedas, plataformas, tiempo)
        self.__mario = Marioplayer()
        self.__pow = Pow()
        self.enemigos = []

    def update(self):
        self.__mario.move(self.plataformas, self.__pow, self.enemigos)
        self.__mario.colision_mariomoneda(self.monedas)
        if self.tiempo == 0:
            self.level = True      
        else:
            self.tiempo -= 1


    def draw(self):
        pyxel.cls(0)
        pyxel.blt(0, 235, 1, 5, 53, 250, 15,0)
        self.__mario.draw_mario()
        for i in range(len(self.plataformas)):
            self.plataformas[i].draw_plataforma_bonif()
        for x in range(len(self.monedas)):
            self.monedas[x].draw()
        pyxel.blt(98,5, 0, 66, 137, 7, 7 , 0) #puntuación partida
        pyxel.text(108, 6, str(self.__mario.puntuacion), 7) #variable puntuación
        if self.tiempo<50:
            if pyxel.frame_count%2 == 0:
                pyxel.text(90, 120, "TIME IS RUNNING OUT" , 7) #variable puntuación