import reflex as rx

from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, TamañosTexto

modal =dict(
    position="fixed",
    top="50%",
    left="50%",
    transform="translate(-50%, -50%)",
    bg="rgba(10, 20, 50, 0.9)",  # Fondo semitransparente para la superposición
    width="100vw",
    height="100vh",
    display="flex",
    justify_content="center",
    align_items="center",
    z_index="1000",  # Asegura que el modal esté por encima de otros elementos
)

def modal_perdistes(EstadoJuego , estilos_boton ,modo = False ) -> rx.Component:
    "Modal que se muestra cuando el jugador ha perdido."

    if not modo :
        return rx.cond(
            EstadoJuego.var_mostrar_modal_perdistes,
            # Este es el contenido que se muestra si EstadoJuego.var_mostrar_modal es True
            rx.box(
                rx.box(
                    rx.heading("Has perdido",
                            font_size=TamañosTexto.TITULO.value,
                            color=Colores.TITULO.value),

                    rx.text("Te has quedado sin oportunidades, ¿qué te gustaría hacer?",
                            font_size = TamañosTexto.TEXTO.value,
                            color = Colores.TEXTO.value,
                            margin_y="10px"),

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
                    width="350px",
                    text_align="center"
                ),
                style = modal
            ),
        # Este es el contenido que se muestra si EstadoJuego.var_mostrar_modal es False (un box vacío)

        rx.box()
    )

def modal_ganastes(EstadoJuego , estilos_boton ,modo = False ) -> rx.Component:
    "Modal que se muestra cuando el jugador ha perdido."

    if not modo :
        return rx.cond(
            EstadoJuego.var_mostrar_modal_ganastes,
            # Este es el contenido que se muestra si EstadoJuego.var_mostrar_modal es True
            rx.box(
                rx.box(
                    rx.heading("Has ganado",
                            font_size=TamañosTexto.TITULO.value,
                            color=Colores.TITULO.value),

                    rx.text("Lo has logrado que vas hacer ahora",
                            font_size = TamañosTexto.TEXTO.value,
                            color = Colores.TEXTO.value,
                            margin_y="10px"),

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
                style=modal
            ),
        # Este es el contenido que se muestra si EstadoJuego.var_mostrar_modal es False (un box vacío)

        rx.box()
    )