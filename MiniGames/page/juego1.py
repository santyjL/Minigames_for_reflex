import random

import reflex as rx

from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, TamañosTexto

numero_random: int = random.randint(1, 100)

# Estilos comunes
estilos_boton = {
    "border": Tamaños.BORDER.value,
    "border_radius": Tamaños.BORDER_RADIUS.value,
    "padding": Tamaños.PADDING.value,
    "width": "80px",
    "margin_y": Tamaños.MARGIN_GRANDE.value,
    "margin_x": Tamaños.MARGIN_MEDIANO.value
}

class NumeroRandom(rx.State):
    """
    Clase que maneja el estado del número a adivinar y los intentos del jugador.
    """
    numero: int = 1
    intentos: int = 7

    def actualizar_numero(self, valor: int):
        """
        Actualiza el número actual y los intentos restantes.
        """
        self.numero = max(1, min(100, self.numero + valor))
        self.intentos -= 1
        StateTexto.modificar_texto(self.numero, numero_random)

    @rx.var
    def var_numero(self) -> int:
        return self.numero

class StateTexto(rx.State):
    """
    Clase que maneja el estado del texto de pistas para el jugador.
    """
    texto: str = "Encuentra el numero random del 1 al 100 tienes 7 oportunidades para encontrarlos"

    def modificar_texto(self, numero_actual: int, numero_random: int):
        """
        Modifica el texto de pista basado en la diferencia entre el número actual y el número a adivinar.
        """

        diferencia = abs(numero_actual - numero_random)

        self.texto = rx.cond(

            numero_actual == numero_random, "¡Felicidades! Has encontrado el número.",

            rx.cond(diferencia <= 5, "El numero que buscas esta muy cerca",

            rx.cond(diferencia <= 10, "El numero que buscas esta a tan solo 10 o menos numeros de distancia",

            rx.cond(diferencia <= 20, "El numero que buscas esta a solo a 20 o menos numeros de distancia",

            rx.cond(diferencia <= 30, "El numero que buscas esta algo cerca",

            "El numero que buscas esta muy lejos")))))

        if NumeroRandom.intentos == 0 and numero_actual != numero_random:
            self.texto = "Encuentra el numero random del 1 al 100 tienes 7 oportunidades para encontrarlos"

    @rx.var
    def get_texto(self) -> str:
        return self.texto

def boton_numero(valor: int, color: str) -> rx.Component:
    """
    Componente reutilizable para los botones de incremento/decremento.
    """
    return rx.button(
        rx.text(
            f"{'+' if valor > 0 else ''}{valor}",
            font_size=TamañosTexto.TITULO.value,
            color=Colores.SUBTITULO.value
        ),
        style={**estilos_boton, "bg": color},
        on_click=NumeroRandom.actualizar_numero(valor)
    )

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
                    boton_numero(10, Colores.SECUNDARIO.value),
                    boton_numero(5, Colores.SECUNDARIO.value),
                    boton_numero(1, Colores.SECUNDARIO.value),
                ),
                rx.spacer(),
                rx.center(
                    rx.vstack(
                        rx.text(
                            NumeroRandom.var_numero,
                            font_size=150,
                            color=Colores.TITULO.value,
                        ),
                            rx.button(
                                bg=Colores.BG.value,
                                border_radius="50em",
                                width="100px",
                                height="100px",
                                on_click=StateTexto.get_texto

                        ),
                        align_items="center",
                    )
                ),
                rx.spacer(),
                rx.vstack(
                    boton_numero(-10, Colores.PRINCIPAL.value),
                    boton_numero(-5, Colores.PRINCIPAL.value),
                    boton_numero(-1, Colores.PRINCIPAL.value),
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
    """
    Página principal del juego.
    """
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