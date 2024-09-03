import random

import reflex as rx

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
class EstadoJuego(rx.State):
    "Clase que maneja el estado del número a adivinar y los intentos del jugador."

    numero_random: int = random.randint(1, 100)
    numero: int = 1
    intentos: int = 7
    texto: str = "Encuentra el numero random del 1 al 100 tienes 7 oportunidades para encontrarlos"
    mostrar_modal: bool = False  # Variable para manejar la visibilidad del modal

    def actualizar_numero(self, valor: int):
        "Actualiza el número actual y los intentos restantes."
        self.numero = max(1, min(100, self.numero + valor))

    def actualizar_texto(self):
        valor: int = abs(self.numero - self.numero_random)

        if self.intentos > 0:
            match valor:
                case _ if valor == 0:
                    self.texto = "¡Felicidades! Has encontrado el número."
                    self.mostrar_modal = True

                case _ if valor < 5:
                    self.texto = "El número que buscas está muy cerca"
                case _ if valor < 10:
                    self.texto = "El número que buscas está a tan solo 10 o menos números de distancia"
                case _ if valor < 20:
                    self.texto = "El número que buscas está a solo a 20 o menos números de distancia"
                case _ if valor < 30:
                    self.texto = "El número que buscas está algo cerca"
                case _:
                    self.texto = "El número que buscas está muy lejos"

            self.intentos -= 1
        else:
            self.texto = "Te has quedado sin oportunidades, has perdido"
            self.mostrar_modal = True  # Muestra el modal cuando se queden sin intentos

    def reiniciar_juego(self):
        "Reinicia el juego."
        self.numero_random = random.randint(1, 100)
        self.numero = 1
        self.intentos = 7
        self.texto = "Encuentra el número random del 1 al 100, tienes 7 oportunidades para encontrarlo"
        self.mostrar_modal = False  # Oculta el modal

    @rx.var
    def var_numero(self) -> int:
        return self.numero

    @rx.var
    def var_texto(self) -> str:
        return self.texto

    @rx.var
    def var_mostrar_modal(self) -> bool:
        return self.mostrar_modal


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
        on_click=EstadoJuego.actualizar_numero(valor)
    )

def texto_enunciado() -> rx.Component:
    return rx.center(
        rx.box(
            rx.text(
                EstadoJuego.var_texto,
                font_size=TamañosTexto.TEXTO.value,
                color=Colores.TEXTO.value,
                align="center"
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
                "0%": {
                    "background-position": "0% 50%"
                },
                "50%": {
                    "background-position": "100% 50%"
                },
                "100%": {
                    "background-position": "0% 50%"
                }
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
                            _hover = _hover_generico
                        ),
                            rx.button(
                                rx.text(EstadoJuego.intentos ,
                                        font_size = TamañosTexto.TEXTO.value ,
                                        color = Colores.TEXTO.value),
                                bg=Colores.BG.value,
                                border_radius="50em",
                                border =Tamaños.BORDER.value,
                                width="100px",
                                height="100px",
                                _hover = _hover_generico,
                                on_click=EstadoJuego.actualizar_texto()
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

def modal_perdida() -> rx.Component:
    "Modal que se muestra cuando el jugador ha perdido."

    return rx.cond(
        EstadoJuego.var_mostrar_modal,
        # Este es el contenido que se muestra si EstadoJuego.var_mostrar_modal es True
        rx.box(
            rx.box(
                rx.text("Has perdido", font_size=TamañosTexto.TITULO.value, color=Colores.TITULO.value),
                rx.text("Te has quedado sin oportunidades, ¿qué te gustaría hacer?", margin_y="10px"),
                rx.hstack(
                    rx.button(
                        "Volver a jugar",
                        on_click=EstadoJuego.reiniciar_juego,
                        style=estilos_boton
                    ),
                    rx.button(
                        "Menú Principal",
                        on_click=rx.redirect(routers.PRINCIPAL.value),
                        style=estilos_boton
                    ),
                    justify="space-around",
                ),
                padding=Tamaños.PADDING.value,
                bg=Colores.BG_COMPONENTES.value,
                border_radius=Tamaños.BORDER_RADIUS.value,
                box_shadow="0 0 10px rgba(0, 0, 0, 0.25)",
                width="300px",
                text_align="center"
            ),
            position="fixed",
            top="50%",
            left="50%",
            transform="translate(-50%, -50%)",
            bg="rgba(0, 0, 0, 0.8)",  # Fondo semitransparente para la superposición
            width="100vw",
            height="100vh",
            display="flex",
            justify_content="center",
            align_items="center",
            z_index="1000",  # Asegura que el modal esté por encima de otros elementos
        ),
        # Este es el contenido que se muestra si EstadoJuego.var_mostrar_modal es False (un box vacío)
        rx.box()
    )




@rx.page(route=routers.ENCUENTRA_EL_NUMERO.value)
def pantalla_juego1() -> rx.Component:
    "Página principal del juego."

    return rx.box(
        rx.vstack(
            navbar(),
            texto_enunciado(),
            juego(),
            modal_perdida(),  # Aquí integramos el modal en la página
            align_items="stretch",
            width="100%"
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height="100vh"
    )
