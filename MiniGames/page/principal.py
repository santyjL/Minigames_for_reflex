import reflex as rx

from MiniGames.Components.navbar import navbar
from MiniGames.styles import Colores


def pantalla_principal() -> rx.Component:
    return rx.box(
        navbar(),
        bg= Colores.BG.value
    )