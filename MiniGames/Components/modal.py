import reflex as rx

from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, TamañosTexto, botones

# Estilo base del modal
modal = dict(
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

# Modal para pantalla de escritorio
def modal_perdistes_desktop(EstadoJuego, otro_texto="") -> rx.Component:
    return rx.box(
        rx.box(
            rx.heading("Has perdido",
                       font_size=TamañosTexto.TITULO.value,
                       color=Colores.TITULO.value),

            rx.text("Te has quedado sin oportunidades, ¿qué te gustaría hacer?",
                    font_size=TamañosTexto.TEXTO.value,
                    color=Colores.TEXTO.value,
                    text_align="center",
                    margin="10px"),

            rx.text(otro_texto,
                    font_size=TamañosTexto.TEXTO.value,
                    color=Colores.TEXTO.value,
                    text_align="center",
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
                justify="center",
            ),
            padding=Tamaños.PADDING.value,
            bg=Colores.BG_COMPONENTES.value,
            border_radius=Tamaños.BORDER_RADIUS.value,
            box_shadow="0 0 10px rgba(0, 0, 0, 0.25)",
            width="30%",  # Ancho para escritorio
            text_align="center"
        ),
        style=modal
    )


# Modal para móvil y tablet
def modal_perdistes_mobile(EstadoJuego, otro_texto="") -> rx.Component:
    return rx.box(
        rx.box(
            rx.heading("Has perdido",
                       font_size=TamañosTexto.TITULO.value,
                       color=Colores.TITULO.value),

            rx.text("Te has quedado sin oportunidades, ¿qué te gustaría hacer?",
                    font_size=TamañosTexto.TEXTO.value,
                    color=Colores.TEXTO.value,
                    text_align="center",
                    margin="10px"),

            rx.text(otro_texto,
                    font_size=TamañosTexto.TEXTO.value,
                    color=Colores.TEXTO.value,
                    text_align="center",
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
                justify="center",
            ),
            padding=Tamaños.PADDING.value,
            bg=Colores.BG_COMPONENTES.value,
            border_radius=Tamaños.BORDER_RADIUS.value,
            box_shadow="0 0 10px rgba(0, 0, 0, 0.25)",
            width="80%",  # Ancho más pequeño para móvil/tablet
            text_align="center"
        ),
        style=modal
    )

# Función principal que selecciona el modal según el dispositivo
def modal_perdistes(EstadoJuego, otro_texto="") -> rx.Component:
    return rx.cond(
        EstadoJuego.var_mostrar_modal_perdistes,
        rx.box(
            rx.desktop_only(modal_perdistes_desktop(EstadoJuego, otro_texto)),
            rx.mobile_and_tablet(modal_perdistes_mobile(EstadoJuego, otro_texto)),
        ),
        rx.box()
    )

# Similar para el modal de ganar
def modal_ganastes_desktop(EstadoJuego, otro_texto="") -> rx.Component:
    return rx.box(
        rx.box(
            rx.heading("Has ganado",
                       font_size=TamañosTexto.TITULO.value,
                       color=Colores.TITULO.value),

            rx.text("Lo has logrado, ¿qué vas a hacer ahora?",
                    font_size=TamañosTexto.TEXTO.value,
                    color=Colores.TEXTO.value,
                    text_align="center",
                    margin="10px"),

            rx.text(otro_texto,
                    font_size=TamañosTexto.TEXTO.value,
                    color=Colores.TEXTO.value,
                    text_align="center",
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
                justify="center",
            ),
            padding=Tamaños.PADDING.value,
            bg=Colores.BG_COMPONENTES.value,
            border_radius=Tamaños.BORDER_RADIUS.value,
            box_shadow="0 0 10px rgba(0, 0, 0, 0.25)",
            width="30%",  # Ancho para escritorio
            text_align="center"
        ),
        style=modal
    )

def modal_ganastes_mobile(EstadoJuego, otro_texto="") -> rx.Component:
    return rx.box(
        rx.box(
            rx.heading("Has ganado",
                       font_size=TamañosTexto.TITULO.value,
                       color=Colores.TITULO.value),

            rx.text("Lo has logrado, ¿qué vas a hacer ahora?",
                    font_size=TamañosTexto.TEXTO.value,
                    color=Colores.TEXTO.value,
                    text_align="center",
                    margin="10px"),

            rx.text(otro_texto,
                    font_size=TamañosTexto.TEXTO.value,
                    color=Colores.TEXTO.value,
                    text_align="center",
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
                justify="center",
            ),
            padding=Tamaños.PADDING.value,
            bg=Colores.BG_COMPONENTES.value,
            border_radius=Tamaños.BORDER_RADIUS.value,
            box_shadow="0 0 10px rgba(0, 0, 0, 0.25)",
            width="80%",  # Ancho más pequeño para móvil/tablet
            text_align="center"
        ),
        style=modal
    )

def modal_ganastes(EstadoJuego, otro_texto="") -> rx.Component:
    return rx.cond(
        EstadoJuego.var_mostrar_modal_ganastes,
        rx.box(
            rx.desktop_only(modal_ganastes_desktop(EstadoJuego, otro_texto)),
            rx.mobile_and_tablet(modal_ganastes_mobile(EstadoJuego, otro_texto)),
        ),
        rx.box()
    )
