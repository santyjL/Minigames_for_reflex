import reflex as rx

from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, TamañosTexto, _hover_generico

# Definimos los valores por defecto de las jugadas
JUGADA_NPC = "?"
JUGADA_JUGADOR = "🖖"

# Función para crear los botones con los emojis de las jugadas
def botones(emoji: str) -> rx.Component:
    """Crea un botón con un emoji representando una jugada."""
    return rx.button(
        rx.text(
            emoji,
            font_size=TamañosTexto.SUBTITULO.value
        ),
        font_size=["16px", "18px", "20px"],
        bg=Colores.SECUNDARIO.value,
        border_radius=Tamaños.BORDER_RADIUS.value,
        padding=Tamaños.PADDING.value,
        border=Tamaños.BORDER.value,
        _hover=_hover_generico
    )

# Función para mostrar la puntuación
def puntuacion(texto: str, valor: int) -> rx.Component:
    """Muestra un cuadro con el texto (nombre del jugador/NPC) y su puntuación."""
    return rx.box(
        # Texto que muestra el nombre (NPC o Tú)
        rx.text(
            texto,
            font_size=TamañosTexto.TEXTO.value,
            color=Colores.TITULO.value,
            align="center"
        ),
        # Cuadro con la puntuación numérica
        rx.box(
            rx.text(
                valor,
                font_size=["80px", "100px", "120px"],
                color=Colores.TITULO.value,
                align="center",
                _hover=_hover_generico,
            ),
            bg=Colores.BG_COMPONENTES.value,
            border_radius=Tamaños.BORDER_RADIUS,
            border=Tamaños.BORDER.value,
            padding=Tamaños.PADDING.value,
            width="15vw"
        ),
        _hover=_hover_generico
    )

# Función para mostrar las reglas del juego
def sistema_de_victoria_text() -> rx.Component:
    """Muestra un cuadro con las reglas de quién gana a quién en el juego."""
    reglas = [
        "🥌  >>  ✂",  # Piedra aplasta Tijeras
        "🥌  >>  🦎",  # Piedra aplasta Lagarto
        "✂  >>  🦎",  # Tijeras decapitan Lagarto
        "✂  >>  📋",  # Tijeras cortan Papel
        "📋  >>  🥌",  # Papel envuelve Piedra
        "📋  >>  🖖",  # Papel refuta a Spock
        "🦎  >>  📋",  # Lagarto devora Papel
        "🦎  >>  🖖",  # Lagarto envenena a Spock
        "🖖  >>  🥌",  # Spock vaporiza Piedra
        "🖖  >>  ✂",  # Spock rompe Tijeras
    ]

    return rx.box(
        # Iteramos sobre la lista de reglas para generar los textos
        *(rx.text(regla, font_size=TamañosTexto.TITULO.value, color=Colores.TEXTO.value, align="center") for regla in reglas),
        height="80vh",
        bg=Colores.BG_COMPONENTES.value,
        width="20vw",
        margin_x=Tamaños.MARGIN_MEDIANO.value
    )

# Bloque principal del juego con las jugadas del NPC y del jugador, y los botones para elegir jugada
def bloque_juego() -> rx.Component:
    """Genera el bloque central del juego, incluyendo las jugadas y los botones."""
    return rx.center(
        rx.box(
            rx.hstack(
                # Flex para las jugadas del NPC y del jugador
                rx.flex(
                    # Jugada del NPC
                    rx.box(
                        rx.text(JUGADA_NPC, font_size=["80px", "100px", "120px"], color="white"),
                        bg=Colores.PRINCIPAL.value,
                        padding=Tamaños.PADDING.value,
                        border_radius=Tamaños.BORDER_RADIUS.value,
                        border=Tamaños.BORDER.value,
                        justify="center",
                        align_items="center",
                        text_align="center",
                        width="95%",
                        height="45%",
                        margin=Tamaños.MARGIN_PEQUEÑO.value
                    ),
                    # Jugada del Jugador
                    rx.box(
                        rx.text(JUGADA_JUGADOR, font_size=["80px", "100px", "120px"], color="white"),
                        bg=Colores.PRINCIPAL.value,
                        padding=Tamaños.PADDING.value,
                        border_radius=Tamaños.BORDER_RADIUS.value,
                        border=Tamaños.BORDER.value,
                        justify="center",
                        align_items="center",
                        text_align="center",
                        width="95%",
                        height="45%",
                        margin=Tamaños.MARGIN_PEQUEÑO.value
                    ),
                    direction="column",
                    justify="center",
                    align_items="center",
                    width="55%",
                    bg=Colores.SECUNDARIO.value,
                    border_radius=Tamaños.BORDER_RADIUS.value,
                    border=Tamaños.BORDER.value
                ),
                rx.separator(orientation="horizontal", size="3"),
                # Flex para los botones de jugadas
                rx.flex(
                    botones("🥌"),  # Botón Piedra
                    botones("📋"),  # Botón Papel
                    botones("✂️"),  # Botón Tijeras
                    botones("🦎"),  # Botón Lagarto
                    botones("🖖"),  # Botón Spock
                    direction="column",
                    justify="center",
                    align_items="center",
                    gap="10px",
                    width="25vw"
                ),
                width="100vw",
                height="100vh",
                justify_content="space-between",
                align_items="center"
            ),
            bg=Colores.BG_COMPONENTES.value,
            width="55vw",
            height="80vh",
            padding=Tamaños.PADDING.value,
            display="flex",
            justify="center",
            align_items="center"
        )
    )

# Componente que representa la disposición principal del juego en pantallas más grandes
def desktop_juegos() -> rx.Component:
    """Genera la vista principal de la pantalla del juego."""
    return rx.hstack(
        # Sección de puntuaciones para el NPC y el jugador
        rx.vstack(
            puntuacion("NPC", 0),
            puntuacion("Tú", 3),
            margin_x=Tamaños.MARGIN_MEDIANO.value
        ),
        bloque_juego(),
        sistema_de_victoria_text(),
        margin_y=25
    )

# Página del juego
@rx.page(route=routers.PIEDRA_PAPEL_TIJERAS.value)
def pantalla_juego2() -> rx.Component:
    """Página que contiene el juego 'Piedra, Papel, Tijeras, Lagarto, Spock'."""
    return rx.box(
        rx.vstack(
            navbar(),
            desktop_juegos(),
            align_items="stretch"
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height="100vh"
    )
