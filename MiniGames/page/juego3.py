import random

import reflex as reflex
import reflex as rx

from MiniGames.Components.class_base import classBase
from MiniGames.Components.modal import modal_ganastes, modal_perdistes
from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, TamañosTexto, _hover_generico


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

def ronda(ronda:int) -> rx.Component:
    return rx.center(
            rx.box(
            rx.text(
                "Ronda",
                font_size=TamañosTexto.SUBTITULO.value,
                color=Colores.TEXTO.value,
                align="center"
            ),
            rx.box(
                rx.text(
                    str(ronda),
                    font_size=TamañosTexto.TITULO.value,
                    color=Colores.TITULO.value,
                    align="center"
                ),
                bg=Colores.SECUNDARIO.value,
                width = "20vw",
                padding=Tamaños.PADDING.value,
                margin=Tamaños.MARGIN_MEDIANO.value
            ),
            margin_y=175
        )
    )

def puntuacion(nombre:str ,valor:str) ->rx.Component:
    return rx.box(
        # Texto que muestra el nombre (NPC o Tú)
        rx.text(
            nombre,
            font_size=TamañosTexto.TEXTO.value,
            color=Colores.TITULO.value,
            align="center"
        ),
        # Cuadro con la puntuación numérica
        rx.box(
            rx.text(
                valor,
                font_size=["80px", "100px", "120px"],
                color=Colores.TITULO.value,
                align="center",
                _hover=_hover_generico,
            ),
            rx.desktop_only(width="12vw"),
            rx.mobile_and_tablet(width="95%"),
            bg=Colores.BG_COMPONENTES.value,
            border_radius=Tamaños.BORDER_RADIUS,
            border=Tamaños.BORDER.value,
            padding=Tamaños.PADDING.value,
        ),
        rx.mobile_and_tablet(width="37vw"),
        margin_x=Tamaños.MARGIN_GRANDE.value,
        _hover=_hover_generico,
    )

@rx.page(route=routers.TRES_EN_RAYA.value)
def pantalla_juego3() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            rx.hstack(
                tablero(),
                ronda(16),
                rx.vstack(
                    puntuacion("TÚ", "9"),
                    puntuacion("NPC", "5")
                )
            )
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height = "100vh",

    )