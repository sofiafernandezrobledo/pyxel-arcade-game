import pyxel
import random
from pathlib import Path
from Fondos.pantallas import (
    Pantallainicio,
    Pantallanivel1,
    Pantallanivel2,
    Pantallanivel3,
    Pantallanivel4,
    Pantallawin,
    Pantalla_gameover,
    Pantalla_monedas,
)
from Fondos.plataformas import Plataforma
from Enemigos.tortugas import Tortuga
from Enemigos.cangrejos import Cangrejo
from Enemigos.moscas import Mosca
from Fondos.monedas import Moneda


class Fabrica:
    def __init__(self):
        # Screen configuration
        self.width = 250

        # Coin configuration
        self.coin_heights = [48, 116, 184, 83, 151]
        self.coin_left_min = -4
        self.coin_left_max = 76
        self.coin_right_min = 170
        self.coin_right_max = 246
        self.coin_center_min = 106
        self.coin_center_max = 144

        # Platform configuration
        self.platform_left_x = -2
        self.platform_right_x = 170
        self.platform_center_x = 102

        self.side_platform_width = 83
        self.center_platform_width = 46

        self.side_platform_start_y = 60
        self.center_platform_start_y = 95
        self.platform_spacing = 68

        # Enemy spawn configuration
        self.enemy_left_x = 20
        self.enemy_right_x = 185
        self.enemy_spawn_y = 8

        # Turtle configuration
        self.turtle_speed = 1
        self.turtle_width = 17
        self.turtle_height = 16
        self.turtle_score = 50

        # Crab configuration
        self.crab_speed = 1
        self.crab_width = 16
        self.crab_height = 13
        self.crab_score = 75

        # Fly configuration
        self.fly_speed = 0.5
        self.fly_width = 15
        self.fly_height = 14
        self.fly_score = 100

        # Common enemy configuration
        self.enemy_time = 50

    def fabrica_monedas(self, cantidad: int):
        monedas = []

        for _ in range(cantidad):
            pos_y = random.choice(self.coin_heights)

            if pos_y in (48, 116, 184):
                lado = random.randint(1, 2)

                if lado == 1:
                    pos_x = random.randint(
                        self.coin_left_min,
                        self.coin_left_max
                    )
                else:
                    pos_x = random.randint(
                        self.coin_right_min,
                        self.coin_right_max
                    )

            else:
                pos_x = random.randint(
                    self.coin_center_min,
                    self.coin_center_max
                )

            monedas.append(Moneda(pos_x, pos_y))

        return monedas

    def fabrica_plataformas(self, cantidad: int):
        plataformas = []

        # Left platforms
        y = self.side_platform_start_y

        for _ in range(cantidad):
            plataformas.append(
                Plataforma(
                    self.platform_left_x,
                    y,
                    self.side_platform_width
                )
            )
            y += self.platform_spacing

        # Right platforms
        y = self.side_platform_start_y

        for _ in range(cantidad):
            plataformas.append(
                Plataforma(
                    self.platform_right_x,
                    y,
                    self.side_platform_width
                )
            )
            y += self.platform_spacing

        # Center platforms
        y = self.center_platform_start_y

        for _ in range(cantidad - 1):
            plataformas.append(
                Plataforma(
                    self.platform_center_x,
                    y,
                    self.center_platform_width
                )
            )
            y += self.platform_spacing

        return plataformas

    def fabrica_enemigos(
        self,
        num_tortugas: int,
        num_cangrejos: int,
        num_moscas: int
    ):
        enemigos = []

        for i in range(num_tortugas):
            x = self.enemy_right_x if i % 2 == 0 else self.enemy_left_x

            enemigos.append(
                Tortuga(
                    x,
                    self.enemy_spawn_y,
                    self.turtle_speed,
                    self.turtle_width,
                    self.turtle_height,
                    i,
                    self.turtle_score,
                    True,
                    True,
                    self.enemy_time,
                    False
                )
            )

        for i in range(num_cangrejos):
            x = self.enemy_right_x if i % 2 == 0 else self.enemy_left_x

            enemigos.append(
                Cangrejo(
                    x,
                    self.enemy_spawn_y,
                    self.crab_speed,
                    self.crab_width,
                    self.crab_height,
                    i,
                    self.crab_score,
                    True,
                    True,
                    self.enemy_time,
                    False
                )
            )

        for i in range(num_moscas):
            x = self.enemy_right_x if i % 2 == 0 else self.enemy_left_x

            enemigos.append(
                Mosca(
                    x,
                    self.enemy_spawn_y,
                    self.fly_speed,
                    self.fly_width,
                    self.fly_height,
                    i,
                    self.fly_score,
                    True,
                    True,
                    self.enemy_time,
                    False
                )
            )

        return enemigos

class App:
    def __init__(self):
        pyxel.init(250,250,"MarioBros", quit_key=pyxel.KEY_ESCAPE)
        assets_path = Path(__file__).resolve().parent / "Assets" / "marioassets.pyxres"

        if not assets_path.exists():
            raise FileNotFoundError(
                "Missing Assets/marioassets.pyxres. "
                "The original game assets are not included in this repository."
            )

        pyxel.load(str(assets_path))
        
        self.fabrica = Fabrica()  
        self.__fondo = Pantallainicio(False, False,self.fabrica.fabrica_monedas(0),  self.fabrica.fabrica_plataformas(0), 50)
        self.__escena = 0
        pyxel.run(self.update, self.draw)
        
    def update(self):
        if self.__fondo.dead == True:
            self.__fondo = Pantalla_gameover(
                False,
                False,
                self.fabrica.fabrica_monedas(0),
                self.fabrica.fabrica_plataformas(0),
                50
            )
            self.__escena = 5

        if self.__escena == 5 and pyxel.btn(pyxel.KEY_ALT):
            self.__fondo = Pantallainicio(
                False,
                False,
                self.fabrica.fabrica_monedas(0),
                self.fabrica.fabrica_plataformas(0),
                50
            )
            self.__escena = 0

        if self.__escena == 6 and pyxel.btn(pyxel.KEY_ALT):
            self.__fondo = Pantallainicio(
                False,
                False,
                self.fabrica.fabrica_monedas(0),
                self.fabrica.fabrica_plataformas(0),
                50
            )
            self.__escena = 0

        if pyxel.btn(pyxel.KEY_RETURN) and self.__escena == 0:
            self.__fondo = Pantallanivel1(
                70,
                False,
                False,
                self.fabrica.fabrica_enemigos(10, 0, 0),
                self.fabrica.fabrica_plataformas(3),
                self.fabrica.fabrica_monedas(10),
                6
            )
            self.__escena = 1

        elif self.__escena == 1 and self.__fondo.level:
            self.__fondo = Pantallanivel2(
                65,
                False,
                False,
                self.fabrica.fabrica_enemigos(12, 3, 0),
                self.fabrica.fabrica_plataformas(3),
                self.fabrica.fabrica_monedas(20),
                12
            )
            self.__escena = 2

        elif self.__escena == 2 and self.__fondo.level:
            self.__fondo = Pantallanivel3(
                60,
                False,
                False,
                self.fabrica.fabrica_enemigos(12, 5, 3),
                self.fabrica.fabrica_plataformas(3),
                self.fabrica.fabrica_monedas(25),
                5
            )
            self.__escena = 3

        elif self.__escena == 3 and self.__fondo.level:
            self.__fondo = Pantallanivel4(
                55,
                False,
                False,
                self.fabrica.fabrica_enemigos(13, 7, 5),
                self.fabrica.fabrica_plataformas(3),
                self.fabrica.fabrica_monedas(30),
                1
            )
            self.__escena = 4

        elif self.__escena == 7 and self.__fondo.level:
            self.__fondo = Pantallawin(
                False,
                False,
                self.fabrica.fabrica_monedas(0),
                self.fabrica.fabrica_plataformas(0),
                50
            )
            self.__escena = 6

        elif self.__fondo.level and self.__escena == 4:
            self.__fondo = Pantalla_monedas(
                False,
                False,
                self.fabrica.fabrica_monedas(50),
                self.fabrica.fabrica_plataformas(3),
                150
            )
            self.__escena = 7

        self.__fondo.update()
            
    def draw(self):
        self.__fondo.draw()
        
        
if __name__ == "__main__":
    App()