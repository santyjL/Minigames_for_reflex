import reflex as rx

from MiniGames.Components.navbar import navbar
from MiniGames.styles import Colores, Tamaños, TamañosTexto


def juegos() -> rx.components:
    return rx.box(
        rx.center(
            rx.desktop_only(
                rx.vstack(
                    rx.center(
                        rx.box(
                            rx.heading(
                                "Qué Quieres Jugar?",
                                color = Colores.TITULO.value,
                                font_size = TamañosTexto.TITULO.value,
                                align = "center"
                            ),
                            padding = Tamaños.PADDING.value,
                            margin = Tamaños.MARGIN_GRANDE.value,
                            bg = Colores.PRINCIPAL.value,
                            border_radius = Tamaños.BORDER_RADIUS.value,
                            border = Tamaños.BORDER.value,
                            align = "center",
                            width = "50wv"
                        ),
                        justify_content="center",
                        align_items="center",
                        width="100%"
                    ),
                    rx.box(
                        rx.heading(
                            "Piedra🥌 , Papel📋 , Tijeras✂ , Lagarto🦎 , Spock 🖖",
                            color = Colores.SUBTITULO.value,
                            font_size = TamañosTexto.SUBTITULO.value,
                            align = "left"
                        ),
                        rx.text(
                            "El clasico juego de pieda papel o tijeras  lo conocemos todo el mundo pero no todos conocen el juego de piedra, papel, tijeras, lagarto, spock",
                            color = Colores.TEXTO.value,
                            font_size = TamañosTexto.TEXTO.value,
                            align = "left"
                        ),
                        padding = Tamaños.PADDING.value,
                        margin = Tamaños.MARGIN_MEDIANO.value,
                        bg = Colores.PRINCIPAL.value,
                        border_radius = Tamaños.BORDER_RADIUS.value,
                        border = Tamaños.BORDER.value,
                        width = "100wv"
                    ),
                    rx.hstack(
                        rx.box(
                            rx.heading(
                                "Encuentra el numero 🎲",
                                color = Colores.SUBTITULO.value,
                                font_size = TamañosTexto.SUBTITULO.value,
                                align = "left"
                            ),
                            rx.text(
                                "del 1 al 100 se a perdido un numero pero cual sera, hay que entcontrarlo",
                                color = Colores.TEXTO.value,
                                font_size = TamañosTexto.TEXTO.value,
                                align = "left"
                            ),
                            padding = Tamaños.PADDING.value,
                            margin_x = Tamaños.MARGIN_MEDIANO.value,
                            bg = Colores.PRINCIPAL.value,
                            width = "45wv",
                            border_radius = Tamaños.BORDER_RADIUS.value,
                            border = Tamaños.BORDER.value,
                            align = "left"
                        ),
                        rx.box(
                            rx.heading(
                                "Tres en raya ❌ || ⭕  ",
                                color = Colores.SUBTITULO.value,
                                font_size = TamañosTexto.SUBTITULO.value,
                                align = "left"
                            ),
                            rx.text(
                                'El clasico "Tres en raya" no podia faltar  un juego mitico que todos conocemos',
                                color = Colores.TEXTO.value,
                                font_size = TamañosTexto.TEXTO.value,
                                align = "left"
                            ),
                            padding = Tamaños.PADDING.value,
                            margin_x = Tamaños.MARGIN_MEDIANO.value,
                            bg = Colores.PRINCIPAL.value,
                            width = "45wv",
                            border_radius = Tamaños.BORDER_RADIUS.value,
                            border = Tamaños.BORDER.value,
                            align = "right"
                        )
                    )
                )
            ),
            rx.mobile_and_tablet(
                rx.vstack(
                    rx.center(
                        rx.box(
                            rx.heading(
                                "Qué Quieres Jugar?",
                                color = Colores.TITULO.value,
                                font_size = TamañosTexto.TITULO.value,
                                align = "center"
                            ),
                            padding = Tamaños.PADDING.value,
                            margin = Tamaños.MARGIN_MEDIANO.value,
                            bg = Colores.PRINCIPAL.value,
                            width = "100wv",
                            border_radius = Tamaños.BORDER_RADIUS.value,
                            border = Tamaños.BORDER.value,
                            align = "center"
                        ),
                        justify_content="center",
                        align_items="center",
                        width="100%"
                    ),
                    rx.box(
                        rx.heading(
                            "Piedra🥌 , Papel📋 , Tijeras✂ , Lagarto🦎 , Spock 🖖",
                            color = Colores.SUBTITULO.value,
                            font_size = TamañosTexto.SUBTITULO.value,
                            align = "left"
                        ),
                        rx.text(
                            "El clasico juego de pieda papel o tijeras  lo conocemos todo el mundo pero no todos conocen el juego de piedra, papel, tijeras, lagarto, spock",
                            color = Colores.TEXTO.value,
                            font_size = TamañosTexto.TEXTO.value,
                            align = "center"
                        ),
                        padding = Tamaños.PADDING.value,
                        margin = Tamaños.MARGIN_MEDIANO.value,
                        bg = Colores.PRINCIPAL.value,
                        width = "100wv",
                        border_radius = Tamaños.BORDER_RADIUS.value,
                        border = Tamaños.BORDER.value,
                        align = "center"
                    ),
                    rx.box(
                        rx.heading(
                            "Encuentra el numero 🎲",
                            color = Colores.SUBTITULO.value,
                            font_size = TamañosTexto.SUBTITULO.value,
                            align = "left"
                        ),
                        rx.text(
                            "del 1 al 100 se a perdido un numero pero cual sera, hay que entcontrarlo",
                            color = Colores.TEXTO.value,
                            font_size = TamañosTexto.TEXTO.value,
                            align = "center"
                        ),
                        padding = Tamaños.PADDING.value,
                        margin = Tamaños.MARGIN_MEDIANO.value,
                        bg = Colores.PRINCIPAL.value,
                        width = "100wv",
                        border_radius = Tamaños.BORDER_RADIUS.value,
                        border = Tamaños.BORDER.value,
                        align = "center"
                    ),
                    rx.box(
                        rx.heading(
                            "Tres en raya ❌ || ⭕  ",
                            color = Colores.SUBTITULO.value,
                            font_size = TamañosTexto.SUBTITULO.value,
                            align = "left"
                        ),
                        rx.text(
                            'El clasico "Tres en raya" no podia faltar  un juego mitico que todos conocemos',
                            color = Colores.TEXTO.value,
                            font_size = TamañosTexto.TEXTO.value,
                            align = "center"
                        ),
                        padding = Tamaños.PADDING.value,
                        margin = Tamaños.MARGIN_MEDIANO.value,
                        bg = Colores.PRINCIPAL.value,
                        width = "100wv",
                        border_radius = Tamaños.BORDER_RADIUS.value,
                        border = Tamaños.BORDER.value,
                        align = "center"
                    )
                )
            )
        ),
        margin = Tamaños.MARGIN_GRANDE.value
    )


def pantalla_principal() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            juegos(),
            align_items="stretch",
            width="100%"
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height="100vh"
    )