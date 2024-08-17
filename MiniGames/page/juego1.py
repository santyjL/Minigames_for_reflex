import random

import reflex as rx

from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores

numero_random : int = random.randint(1 , 101)

class numeroRandom(rx.State):
    numero:int = 0

    def sumar10(self):
       if self.numero <= 90:
            self.numero +10

    def sumar5(self):
       if self.numero <=95:
            self.numero +5

    def sumar1(self):
       if self.numero <=99:
            self.numero +1

    def restar10(self):
       if self.numero >= 10:
            self.numero -10

    def restar5(self):
       if self.numero >= 5:
            self.numero -5

    def restar6(self):
       if self.numero >= 1:
            self.numero -1

    @rx.var
    def var_numero(self) -> int :
        return self.numero

class stateTexto(rx.State):
    pass

class stateColor(rx.State):
    pass

def texto_enunciado() -> rx.Component:
    return rx.box(
        rx.text("")
    )

def juego() -> rx.Component:
    pass

@rx.page(route=routers.ENCUENTRA_EL_NUMERO.value)
def pantalla_juego1() -> rx.Component:
    return rx.box(
        rx.vstack(
        navbar(),
        align_items="stretch",
        width="100%"
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height="100vh"
    )