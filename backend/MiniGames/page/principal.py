import reflex as rx

from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import (Colores, Tamaños, TamañosTexto, _hover_generico,
                              juegos_movil_y_tableta)


def desktop_juegos() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.box(
                rx.heading(
                    "Qué Quieres Jugar?",
                    color=Colores.TITULO.value,
                    font_size=TamañosTexto.TITULO.value,
                    text_align="center"
                ),
                padding=Tamaños.PADDING.value,
                margin=Tamaños.MARGIN_GRANDE.value,
                bg=Colores.PRINCIPAL.value,
                border_radius=Tamaños.BORDER_RADIUS.value,
                border=Tamaños.BORDER.value,
            ),
            justify_content="center",
            align_items="center",
            width="100%"
        ),

        rx.center(
            rx.link(
                rx.box(
                    rx.heading(
                        "Piedra🥌 , Papel📋 , Tijeras✂ , Lagarto🦎 , Spock 🖖",
                        color=Colores.SUBTITULO.value,
                        font_size=TamañosTexto.SUBTITULO.value,
                        text_align="left"
                    ),
                    rx.text(
                        "El clásico juego de piedra papel o tijeras lo conocemos todos, pero no todos conocen el juego de piedra, papel, tijeras, lagarto, spock.",
                        color=Colores.TEXTO.value,
                        font_size=TamañosTexto.TEXTO.value,
                        text_align="left"
                    ),
                    padding=Tamaños.PADDING.value,
                    margin=Tamaños.MARGIN_MEDIANO.value,
                    bg=Colores.PRINCIPAL.value,
                    border_radius=Tamaños.BORDER_RADIUS.value,
                    border=Tamaños.BORDER.value,
                    width="85vw",
                    _hover = _hover_generico
                ),
                href=routers.PIEDRA_PAPEL_TIJERAS.value,
                text_decoration="none"
            ),
        ),

        rx.center(
            rx.hstack(
                rx.link(
                    rx.box(
                        rx.heading(
                            "Encuentra el número 🎲",
                            color=Colores.SUBTITULO.value,
                            font_size=TamañosTexto.SUBTITULO.value,
                            text_align="left"
                        ),
                        rx.text(
                            "Del 1 al 100 se ha perdido un número, ¿pero cuál será? Hay que encontrarlo.",
                            color=Colores.TEXTO.value,
                            font_size=TamañosTexto.TEXTO.value,
                            text_align="left"
                        ),
                        padding=Tamaños.PADDING.value,
                        margin_x=Tamaños.MARGIN_MEDIANO.value,
                        bg=Colores.PRINCIPAL.value,
                        width="41vw",
                        border_radius=Tamaños.BORDER_RADIUS.value,
                        border=Tamaños.BORDER.value,
                        _hover = _hover_generico
                    ),
                    href=routers.ENCUENTRA_EL_NUMERO.value,
                    text_decoration="none"
                ),

                rx.link(
                    rx.box(
                        rx.heading(
                            "Tres en raya ❌ || ⭕",
                            color=Colores.SUBTITULO.value,
                            font_size=TamañosTexto.SUBTITULO.value,
                            text_align="left"
                        ),
                        rx.text(
                            'El clásico "Tres en raya" no podía faltar, un juego mítico que todos conocemos.',
                            color=Colores.TEXTO.value,
                            font_size=TamañosTexto.TEXTO.value,
                            text_align="left"
                        ),
                        padding=Tamaños.PADDING.value,
                        margin_x=Tamaños.MARGIN_MEDIANO.value,
                        bg=Colores.PRINCIPAL.value,
                        width="41vw",
                        border_radius=Tamaños.BORDER_RADIUS.value,
                        border=Tamaños.BORDER.value,
                        _hover = _hover_generico
                    ),
                    href=routers.TRES_EN_RAYA.value,
                    text_decoration="none"
                )
            )
        )
    )

def mobile_juegos() -> rx.Component:
    return rx.vstack(
        rx.center(
            rx.box(
                rx.heading(
                    "Qué Quieres Jugar?",
                    color=Colores.TITULO.value,
                    font_size=TamañosTexto.SUBTITULO.value,
                    text_align="center"
                ),
                padding=Tamaños.PADDING.value,
                margin=Tamaños.MARGIN_MEDIANO.value,
                bg=Colores.PRINCIPAL.value,
                width="48vw",
                border_radius=Tamaños.BORDER_RADIUS.value,
                border=Tamaños.BORDER.value,
                text_align="center"
            ),
            justify_content="center",
            align_items="center",
            width="100%"
        ),
        rx.link(
            rx.box(
                rx.heading(
                    "Piedra🥌 , Papel📋 , Tijeras✂ , Lagarto🦎 , Spock 🖖",
                    color=Colores.SUBTITULO.value,
                    font_size=TamañosTexto.SUBTITULO.value,
                    text_align="left"
                ),
                rx.text(
                    "El clásico juego de piedra papel o tijeras lo conocemos todos, pero no todos conocen el juego de piedra, papel, tijeras, lagarto, spock.",
                    color=Colores.TEXTO.value,
                    font_size=TamañosTexto.TEXTO.value,
                    text_align="left"
                ),
                style=juegos_movil_y_tableta
            ),
            href=routers.PIEDRA_PAPEL_TIJERAS.value,
            text_decoration="none"
        ),
        rx.link(
            rx.box(
                rx.heading(
                    "Encuentra el número 🎲",
                    color=Colores.SUBTITULO.value,
                    font_size=TamañosTexto.SUBTITULO.value,
                    text_align="left"
                ),
                rx.text(
                    "Del 1 al 100 se ha perdido un número, ¿pero cuál será? Hay que encontrarlo.",
                    color=Colores.TEXTO.value,
                    font_size=TamañosTexto.TEXTO.value,
                    text_align="left"
                ),
                style=juegos_movil_y_tableta
            ),
            href=routers.ENCUENTRA_EL_NUMERO.value,
            text_decoration="none"
        ),
        rx.link(
            rx.box(
                rx.heading(
                    "Tres en raya ❌ || ⭕",
                    color=Colores.SUBTITULO.value,
                    font_size=TamañosTexto.SUBTITULO.value,
                    text_align="left"
                ),
                rx.text(
                    'El clásico "Tres en raya" no podía faltar, un juego mítico que todos conocemos.',
                    color=Colores.TEXTO.value,
                    font_size=TamañosTexto.TEXTO.value,
                    text_align="left"
                ),
                style=juegos_movil_y_tableta
            ),
            href=routers.TRES_EN_RAYA.value,
            text_decoration="none"
        )
    )

def juegos() -> rx.Component:
    return rx.box(
        rx.center(
            rx.desktop_only(
                desktop_juegos(),
                margin=50
            ),
            rx.mobile_and_tablet(
                mobile_juegos(),
                margin=50
            )
        ),
        min_height="100vh"
    )

@rx.page(route=routers.PRINCIPAL.value)
def pantalla_principal() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            rx.center(
                juegos(),
            ),
            align_items="stretch",
            width="100%"
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height="100vh"
    )
