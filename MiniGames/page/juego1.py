import random

import reflex as rx

from MiniGames.Components.class_base import classBase
from MiniGames.Components.modal import modal_ganastes, modal_perdistes
from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, TamañosTexto, _hover_generico

# Estilos comunes
estilos_boton = {
    "border": Tamaños.BORDER.value,
    "border_radius": Tamaños.BORDER_RADIUS.value,
    "padding": Tamaños.PADDING.value,
    "width": "80px",
    "margin_y": Tamaños.MARGIN_PEQUEÑO.value,
    "margin_x": Tamaños.MARGIN_MEDIANO.value,
    "_hover"  : _hover_generico
}

#back - end

class EstadoJuego(classBase):
    """Clase que maneja el estado del número a adivinar y los intentos del jugador."""

    # Variables específicas del juego
    numero_random: int = random.randint(1, 100)  # Número aleatorio a adivinar
    numero: int = 1  # Número actual del jugador
    intentos: int = 7  # Número de intentos restantes
    texto: str = "Encuentra el número random del 1 al 100, tienes 7 oportunidades para encontrarlo"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Llamar al constructor de la clase base

    def actualizar_numero(self, valor: int):
        """Actualiza el número actual del jugador dentro del rango permitido."""
        self.numero = max(1, min(100, self.numero + valor))

    def actualizar_texto(self):
        """Actualiza el mensaje de texto basado en cuán cerca está el jugador del número aleatorio."""
        valor: int = abs(self.numero - self.numero_random)

        if self.intentos > 0:
            if valor == 0:
                self.texto = "¡Felicidades! Has encontrado el número."
                self.mostrar_modal_ganastes = True  # Muestra el modal de victoria
            elif valor < 5:
                self.texto = "El número que buscas está muy cerca"
            elif valor < 10:
                self.texto = "El número que buscas está a tan solo 10 o menos números de distancia"
            elif valor < 20:
                self.texto = "El número que buscas está a solo 20 o menos números de distancia"
            elif valor < 30:
                self.texto = "El número que buscas está algo cerca"
            else:
                self.texto = "El número que buscas está muy lejos"

            self.intentos -= 1
        else:
            self.texto = "Te has quedado sin oportunidades, has perdido"
            self.mostrar_modal_perdistes = True  # Muestra el modal de derrota cuando se queden sin intentos

    def reiniciar_juego(self):
        """Reinicia el juego al estado inicial."""
        self.numero_random = random.randint(1, 100)
        self.numero = 1
        self.intentos = 7
        self.texto = "Encuentra el número random del 1 al 100, tienes 7 oportunidades para encontrarlo"
        self.mostrar_modal_perdistes = False  # Oculta el modal de derrota
        self.mostrar_modal_ganastes = False   # Oculta el modal de victoria

    # Variables reactivas para el número actual y el texto del juego
    @rx.var
    def var_numero(self) -> int:
        """Variable reactiva que devuelve el número actual."""
        return self.numero

    @rx.var
    def var_texto(self) -> str:
        """Variable reactiva que devuelve el texto actual del juego."""
        return self.texto

#front - end
def boton_numero(valor: int, color: str) -> rx.Component:
    "Componente reutilizable para los botones de incremento/decremento."
    return rx.button(
        rx.text(
            f"{'+' if valor > 0 else ''}{valor}",
            font_size=TamañosTexto.TITULO.value,
            color=Colores.SUBTITULO.value
        ),
        style={**estilos_boton, "bg": color},
        on_click=lambda: EstadoJuego.actualizar_numero(valor)  # Cambiado a lambda para evitar llamar directamente
    )

def texto_enunciado() -> rx.Component:
    return rx.center(
        rx.box(
            rx.text(
                EstadoJuego.var_texto,
                font_size=TamañosTexto.TEXTO.value,
                color=Colores.TEXTO.value,
                align="center",
            ),
            padding=Tamaños.PADDING.value,
            width="60vw",
            margin=50,
            border_radius=Tamaños.BORDER_RADIUS.value,
            bg="linear-gradient(45deg ,#67a6a6bb , #8867a6bb)",
            background_size="400% 400%",
            animation="gradientAnimation 3s infinite alternate",
            _style={
                "@keyframes gradientAnimation": {
                    "0%": {"background-position": "0% 50%"},
                    "50%": {"background-position": "100% 50%"},
                    "100%": {"background-position": "0% 50%"}
                }
            }
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
                            EstadoJuego.var_numero,
                            font_size=150,
                            color=Colores.TITULO.value,
                            _hover=_hover_generico
                        ),
                        rx.button(
                            rx.text("confirma✅",
                                    font_size=TamañosTexto.TEXTO.value,
                                    color=Colores.TEXTO.value),
                            bg=Colores.BG.value,
                            border_radius="50em",
                            border=Tamaños.BORDER.value,
                            width="130px",
                            height="130px",
                            _hover=_hover_generico,
                            on_click=lambda: EstadoJuego.actualizar_texto()  # Cambiado a lambda
                        ),
                        rx.text(
                            f"Intentos : [{EstadoJuego.intentos}]",
                            font_size=TamañosTexto.TITULO.value,
                            color=Colores.TITULO.value
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
            width="60vw",
            margin=Tamaños.MARGIN_GRANDE.value,
            border_radius=Tamaños.BORDER_RADIUS.value,
            bg=Colores.BG_COMPONENTES.value
        )
    )

@rx.page(route=routers.ENCUENTRA_EL_NUMERO.value)
def pantalla_juego1() -> rx.Component:
    "Página principal del juego."
    return rx.box(
        rx.vstack(
            navbar(),
            texto_enunciado(),
            juego(),
            modal_perdistes(EstadoJuego, f"El numero correcto era {EstadoJuego.numero_random}"),
            modal_ganastes(EstadoJuego, f"El numero correcto siempre fue {EstadoJuego.numero_random}"),
            align_items="stretch",
            width="100%"
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height="100vh"
    )