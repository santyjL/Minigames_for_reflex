import random

import reflex as rx

from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, TamañosTexto

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
    lista_textos:list[str] = ["Encuentra el numero random del 1 al 100 tienes 7 oportunidades para encontrarlos",
                        "El numero que buscas esta muy lejos",
                        "El numero que buscas esta algo cerca",
                        "El numero que buscas esta a solo a 20 o menos numeros de distancia",
                        "El numero que buscas esta a tan solo 10 o menos numeros de distancia",
                        "El numero que buscas esta muy cerca"]

    index: str = 0

    def modificar_texto(self):
        if (numeroRandom.numero * -numero_random) <= 5 :
            self.index = 5

        elif (numeroRandom.numero * -numero_random) <= 10 :
            self.index = 4

        elif (numeroRandom.numero * -numero_random) <= 20 :
            self.index = 3

        elif (numeroRandom.numero * -numero_random) <= 30 :
            self.index = 2

        elif (numeroRandom.numero * -numero_random) > 30 :
            self.index = 1

    @rx.var
    def get_texto(self) -> str:
        return self.lista_textos[self.index]


class stateColor(rx.State):
    pass

def texto_enunciado() -> rx.Component:
    return rx.center(
        rx.box(
            rx.text(
                stateTexto.get_texto,
                font_size=TamañosTexto.TEXTO.value,
                color = Colores.TEXTO.value,
                align="center"
                    ),
            width ="50vw",
            margin=50,
        )
    )

def juego() -> rx.Component:
    pass

@rx.page(route=routers.ENCUENTRA_EL_NUMERO.value)
def pantalla_juego1() -> rx.Component:
    return rx.box(
        rx.vstack(
        navbar(),
        texto_enunciado(),
        align_items="stretch",
        width="100%"
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height="100vh"
    )