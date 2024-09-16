import reflex as rx

from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, TamañosTexto, botones

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

def modal_perdistes(EstadoJuego, otro_texto="" ) -> rx.Component:
    "Modal que se muestra cuando el jugador ha perdido."


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
                        text_align = "center",
                        margin="10px"),

                rx.text(otro_texto,
                        font_size = TamañosTexto.TEXTO.value,
                        color = Colores.TEXTO.value,
                        text_align = "center",
                        margin="10px"),

                rx.hstack(
                    rx.button(
                        "Volver a jugar",
                        on_click=EstadoJuego.reiniciar_juego,
                        style=botones,
                    ),
                    rx.spacer(),
                    rx.button(
                        "Menú Principal",
                        on_click=rx.redirect(routers.PRINCIPAL.value),
                        style=botones,
                    ),
                    justify="space-around",
                ),
                padding=Tamaños.PADDING.value,
                bg=Colores.BG_COMPONENTES.value,
                border_radius=Tamaños.BORDER_RADIUS.value,
                box_shadow="0 0 10px rgba(0, 0, 0, 0.25)",
                width="30%",
                text_align="center"
            ),
            style = modal
        ),
        # Este es el contenido que se muestra si EstadoJuego.var_mostrar_modal es False (un box vacío)
        rx.box()
    )

def modal_ganastes(EstadoJuego,otro_texto="" ) -> rx.Component:
    "Modal que se muestra cuando el jugador ha perdido."

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
                        text_align = "left",
                        margin="10px"
                        ),

                rx.text(otro_texto,
                        font_size = TamañosTexto.TEXTO.value,
                        color = Colores.TEXTO.value,
                        text_align = "center",
                        margin="10px"),

                rx.hstack(
                    rx.button(
                        "Volver a jugar",
                        on_click=EstadoJuego.reiniciar_juego,
                        style=botones,

                    ),
                    rx.spacer(),
                    rx.button(
                        "Menú Principal",
                        on_click=rx.redirect(routers.PRINCIPAL.value),
                        style=botones,
                    ),
                    justify="space-around",
                ),
                padding=Tamaños.PADDING.value,
                bg=Colores.BG_COMPONENTES.value,
                border_radius=Tamaños.BORDER_RADIUS.value,
                box_shadow="0 0 10px rgba(0, 0, 0, 0.25)",
                width="30%",
                text_align="center"
            ),
            style=modal
        ),
        # Este es el contenido que se muestra si EstadoJuego.var_mostrar_modal es False (un box vacío)
        rx.box()
    )