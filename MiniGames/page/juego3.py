import random

import reflex as reflex
import reflex as rx

from MiniGames.Components.class_base import classBase
from MiniGames.Components.modal import modal_ganastes, modal_perdistes
from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, _hover_generico


def tablero() -> rx.Component:
    return rx.box(
        rx.grid(
            rx.button("❌",width="auto",height ="auto", bg="#0000", border="solid #FFFFFF"),
            rx.button("",width="auto",height ="auto", bg="#0000", border="solid #FFFFFF"),
            rx.button("⭕",width="auto",height ="auto", bg="#0000", border="solid #FFFFFF"),
            rx.button("",width="auto",height ="auto", bg="#0000", border="solid #FFFFFF"),
            rx.button("❌",width="auto",height ="auto", bg="#0000", border="solid #FFFFFF"),
            rx.button("",width="auto",height ="auto", bg="#0000", border="solid #FFFFFF"),
            rx.button("⭕",width="auto",height ="auto", bg="#0000", border="solid #FFFFFF"),
            rx.button("",width="auto",height ="auto", bg="#0000", border="solid #FFFFFF"),
            rx.button("❌",width="auto",height ="auto", bg="#0000", border="solid #FFFFFF"),
            columns="3",
            rows="3",
            margin=Tamaños.MARGIN_GRANDE.value,
            padding=Tamaños.PADDING.value,
            bg=Colores.BG_COMPONENTES.value,
            width = "40vw",
            height = "70vh"
        )
    )

def ronda() -> rx.Component:
    return rx.box(

    )

@rx.page(route=routers.TRES_EN_RAYA.value)
def pantalla_juego3() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            rx.hstack(
                tablero(),
            )
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height = "100vh",

    )