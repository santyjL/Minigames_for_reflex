import random

import reflex as rx

from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores

numero_random : int = random.randint(1 , 101)

class numeroRandom(rx.state):
   numero:int = 0

   @rx.var
   def sumar10(self):
       if self.numero <= 90:
        return self.numero +10

   @rx.var
   def sumar5(self):
       if self.numero <=95:
        return self.numero +5

   @rx.var
   def sumar1(self):
       if self.numero <=99:
        return self.numero +1

   @rx.var
   def restar10(self):
       if self.numero >= 10:
        return self.numero -10

   @rx.var
   def restar5(self):
       if self.numero >= 5:
        return self.numero -5

   @rx.var
   def restar6(self):
       if self.numero >= 1:
        return self.numero -1

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