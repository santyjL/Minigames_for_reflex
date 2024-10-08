import random

import reflex as reflex
import reflex as rx

from MiniGames.Components.class_base import classBase
from MiniGames.Components.modal import modal_ganastes, modal_perdistes
from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, _hover_generico


@rx.page(route=routers.TRES_EN_RAYA.value)
def pantalla_juego3() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar()
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height = "100vh",

    )