import reflex as rx

from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, TamañosTexto, _hover_generico

# Definimos los valores por defecto de las jugadas
JUGADA_NPC = "?"
JUGADA_JUGADOR = "🖖"

def botones (emoji : str):
    return rx.button(
        rx.text(
            emoji,
            font_size = TamañosTexto.SUBTITULO.value
        ),
        font_size = ["16px", "18px", "20px"],
        bg = Colores.SECUNDARIO.value,
        border_radius = Tamaños.BORDER_RADIUS.value,
        padding = Tamaños.PADDING.value,
        border = Tamaños.BORDER.value,
        _hover = _hover_generico

    )
#Bloque principal del juego
def bloque_juego() -> rx.Component:
    return rx.center(
        rx.box(
            # Grid principal que contiene dos flex: uno para las jugadas y otro para los botones
            rx.hstack(
                # Flex para la jugada del NPC (arriba) y la del jugador (abajo)
                rx.flex(
                    rx.box(
                        rx.text(JUGADA_NPC, font_size=["80px", "100px", "120px"], color="white"),
                        bg=Colores.PRINCIPAL.value,
                        padding=Tamaños.PADDING.value,
                        border_radius=Tamaños.BORDER_RADIUS.value,
                        justify="center",
                        align_items="center",
                        text_align="center",
                        width="80%",
                        height="45%",
                        margin = Tamaños.MARGIN_PEQUEÑO.value
                    ),
                    rx.box(
                        rx.text(JUGADA_JUGADOR, font_size=["80px", "100px", "120px"], color="white"),
                        bg=Colores.PRINCIPAL.value,
                        padding=Tamaños.PADDING.value,
                        border_radius=Tamaños.BORDER_RADIUS.value,
                        justify="center",
                        align_items="center",
                        text_align="center",
                        width="80%",
                        height="45%",
                        margin = Tamaños.MARGIN_PEQUEÑO.value
                    ),
                    direction="column",  # Organiza las jugadas en columna
                    justify="center",
                    align_items="center",
                    width="55%",  # Ancho del flex de jugadas
                    bg = Colores.SECUNDARIO.value,
                    border_radius=Tamaños.BORDER_RADIUS.value,
                ),
                rx.separator(orientation="horizontal" ,size="3"),
                # Flex para los cinco botones de las opciones de jugada
                rx.flex(
                    botones("🥌"),
                    botones("📋"),
                    botones("✂️"),
                    botones("🦎"),
                    botones("🖖"),
                    direction="column",  # Organiza los botones en columna
                    justify="center",
                    align_items="center",
                    gap="10px",  # Espacio entre los botones
                    width="25%"  # Ancho del flex de botones
                ),
                width="95%",  # Ajusta el ancho total del grid
                height="95%",  # Altura del bloque de juego
                justify_content="center",
                align_items="center"
            ),
            bg=Colores.BG_COMPONENTES.value,
            width="60%",
            height="95%",  # Altura total del contenedor
            padding=Tamaños.PADDING.value,
            display="flex",
            justify="center",
            align_items="center",
        )
    )

@rx.page(route=routers.PIEDRA_PAPEL_TIJERAS.value)
def pantalla_juego2() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            bloque_juego(),
            align_items="stretch",
            width="100%",
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height="100vh",
    )
