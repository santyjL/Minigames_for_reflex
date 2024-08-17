import reflex as rx

from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores


class stateTexto(rx.State):
    pass

class stateColor(rx.State):
    pass

def texto_enunciado() -> rx.Component:
    pass

def juego() -> rx.Component:
    pass

@rx.page(route=routers.ENCUENTRA_EL_NUMERO.value)
def pantalla_juego1() -> rx.Component:
    rx.box(
        rx.vstack(
        navbar(),
        align_items="stretch",
        width="100%"
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height="100vh"
    )