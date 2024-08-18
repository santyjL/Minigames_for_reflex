import random

import reflex as rx

from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, TamañosTexto

numero_random: int = random.randint(1, 100)

class NumeroRandom(rx.State):
    numero: int = 1
    intentos: int = 7

    def actualizar_numero(self, valor: int):
        nuevo_numero = self.numero + valor
        # Asegurarse de que el número esté entre 1 y 100
        if nuevo_numero < 1:
            self.numero = 1
        elif nuevo_numero > 100:
            self.numero = 100
        else:
            self.numero = nuevo_numero

        self.intentos -= 1
        # Actualizar el texto después de cambiar el número
        StateTexto.modificar_texto(self.numero, numero_random)

    @rx.var
    def var_numero(self) -> int:
        return self.numero

class StateTexto(rx.State):
    texto : str = "Encuentra el numero random del 1 al 100 tienes 7 oportunidades para encontrarlos"

    def modificar_texto(self, numero_actual: int, numero_random: int):
        diferencia = abs(numero_actual - numero_random)

        if numero_actual == numero_random:
            self.texto = "¡Felicidades! Has encontrado el número."
        elif diferencia <= 5:
            self.texto = "El numero que buscas esta muy cerca"
        elif diferencia <= 10:
            self.texto = "El numero que buscas esta a tan solo 10 o menos numeros de distancia",
        elif diferencia <= 20:
            self.texto = "El numero que buscas esta a solo a 20 o menos numeros de distancia"
        elif diferencia <= 30:
            self.texto = "El numero que buscas esta algo cerca"
        else:
            self.texto = "El numero que buscas esta muy lejos"

        if NumeroRandom.intentos == 0 and numero_actual != numero_random:
            self.texto = "Encuentra el numero random del 1 al 100 tienes 7 oportunidades para encontrarlos"

    @rx.var
    def get_texto(self) -> str:
        return self.texto

def texto_enunciado() -> rx.Component:
    return rx.center(
        rx.box(
            rx.text(
                StateTexto.get_texto,
                font_size=TamañosTexto.TEXTO.value,
                color=Colores.TEXTO.value,
                align="center"
            ),
            padding=Tamaños.PADDING.value,
            width="60vw",
            margin=50,
            border_radius=Tamaños.BORDER_RADIUS.value,
            bg=Colores.BG_COMPONENTES.value
        )
    )

def juego() -> rx.Component:
    return rx.center(
        rx.box(
            rx.hstack(
                rx.vstack(
                    rx.button(
                        rx.text(
                            "+10",
                            font_size=TamañosTexto.TITULO.value,
                            color=Colores.SUBTITULO.value
                        ),
                        on_click=lambda: NumeroRandom.actualizar_numero(10),
                        bg=Colores.SECUNDARIO.value,
                        border=Tamaños.BORDER.value,
                        border_radius=Tamaños.BORDER_RADIUS.value,
                        padding=Tamaños.PADDING.value,
                        width="80px",
                        margin=Tamaños.MARGIN_PEQUEÑO.value
                    ),
                    rx.button(
                        rx.text(
                            "+5",
                            font_size=TamañosTexto.TITULO.value,
                            color=Colores.SUBTITULO.value
                        ),
                        on_click=lambda: NumeroRandom.actualizar_numero(5),
                        bg=Colores.SECUNDARIO.value,
                        border=Tamaños.BORDER.value,
                        border_radius=Tamaños.BORDER_RADIUS.value,
                        padding=Tamaños.PADDING.value,
                        width="80px",
                        margin=Tamaños.MARGIN_PEQUEÑO.value
                    ),
                    rx.button(
                        rx.text(
                            "+1",
                            font_size=TamañosTexto.TITULO.value,
                            color=Colores.SUBTITULO.value
                        ),
                        on_click=lambda: NumeroRandom.actualizar_numero(1),
                        bg=Colores.SECUNDARIO.value,
                        border=Tamaños.BORDER.value,
                        border_radius=Tamaños.BORDER_RADIUS.value,
                        padding=Tamaños.PADDING.value,
                        width="80px",
                        margin=Tamaños.MARGIN_PEQUEÑO.value
                    ),
                ),

                rx.center(
                    rx.vstack(
                        rx.text(
                            NumeroRandom.var_numero,
                            font_size=150,
                            color=Colores.TITULO.value,
                        ),
                        rx.box(
                            bg=Colores.BG.value,
                            border_radius="50em",
                            width="100px",
                            height="100px"
                        )
                    )
                ),
                rx.vstack(
                    rx.button(
                        rx.text(
                            "-10",
                            font_size=TamañosTexto.TITULO.value,
                            color=Colores.SUBTITULO.value
                        ),
                        on_click=lambda: NumeroRandom.actualizar_numero(-10),
                        bg=Colores.PRINCIPAL.value,
                        border=Tamaños.BORDER.value,
                        border_radius=Tamaños.BORDER_RADIUS.value,
                        padding=Tamaños.PADDING.value,
                        width="80px",
                        margin=Tamaños.MARGIN_PEQUEÑO.value
                    ),
                    rx.button(
                        rx.text(
                            "-5",
                            font_size=TamañosTexto.TITULO.value,
                            color=Colores.SUBTITULO.value
                        ),
                        on_click=lambda: NumeroRandom.actualizar_numero(-5),
                        bg=Colores.PRINCIPAL.value,
                        border=Tamaños.BORDER.value,
                        border_radius=Tamaños.BORDER_RADIUS.value,
                        padding=Tamaños.PADDING.value,
                        width="80px",
                        margin=Tamaños.MARGIN_PEQUEÑO.value
                    ),
                    rx.button(
                        rx.text(
                            "-1",
                            font_size=TamañosTexto.TITULO.value,
                            color=Colores.SUBTITULO.value
                        ),
                        on_click=lambda: NumeroRandom.actualizar_numero(-1),
                        bg=Colores.PRINCIPAL.value,
                        border=Tamaños.BORDER.value,
                        border_radius=Tamaños.BORDER_RADIUS.value,
                        padding=Tamaños.PADDING.value,
                        width="80px",
                        margin=Tamaños.MARGIN_PEQUEÑO.value
                    ),
                )
            ),
            padding=Tamaños.PADDING.value,
            width="75vw",
            margin=Tamaños.MARGIN_GRANDE.value,
            border_radius=Tamaños.BORDER_RADIUS.value,
            bg=Colores.BG_COMPONENTES.value
        )
    )

@rx.page(route=routers.ENCUENTRA_EL_NUMERO.value)
def pantalla_juego1() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            texto_enunciado(),
            juego(),
            align_items="stretch",
            width="100%"
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height="100vh"
    )
