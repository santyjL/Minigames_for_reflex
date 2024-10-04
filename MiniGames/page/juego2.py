import random

import reflex as rx

from MiniGames.Components.class_base import classBase
from MiniGames.Components.modal import modal_ganastes, modal_perdistes
from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, TamañosTexto, _hover_generico

textos_victoria: list[str]= [
    "¡Increíble jugada! Has vencido con una lógica imbatible.",
    "¡Tu mente afilada como tijeras ha cortado cualquier duda, victoria tuya!",
    "Papel envolvió la estrategia enemiga. ¡Qué movimiento maestro!",
    "Lagarto devora con astucia. ¡El trono es tuyo!",
    "Spock miraría con orgullo tu victoria lógica y aplastante.",
    "Tu piedra ha aplastado más que rivales, ¡ha cimentado tu triunfo!",
    "¡Es oficial, eres un estratega digno de leyenda!"
    ]

texto_derrota: list[str] = [
    "Hoy no fue tu día, pero los grandes vuelven más fuertes.",
    "Caíste, pero hasta Spock sabe que perder es aprender.",
    "Tu tijera fue desafilada... por esta vez.",
    "Lagarto fue aplastado, pero la próxima vez mordisquearás la victoria.",
    "El universo se inclinó ante Spock, pero tú te alzarás de nuevo.",
    "Piedra se quebró esta vez, pero hay muchas más en el camino.",
    "No fue suficiente, pero como dicen, ¡cada derrota es una lección!"
    ]


class EstadoJuego(classBase):
    jugada_npc:str= "?"
    jugada_jugador:str= "?"
    puntuacion_npc:int= 0
    puntuacion_jugador:int= 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def logica(self):
        if self.puntuacion_jugador < 4:
            match (self.jugada_jugador, self.jugada_npc):
                case (jugada, npc) if jugada == npc:
                    pass

                case ("🥌", "✂") | ("🥌", "🦎"):
                    self.puntuacion_jugador += 1

                case ("✂", "📋") | ("✂", "🦎"):
                    self.puntuacion_jugador += 1

                case ("📋", "🥌") | ("📋", "🖖"):
                    self.puntuacion_jugador += 1

                case ("🦎", "📋") | ("🦎", "🖖"):
                    self.puntuacion_jugador += 1

                case ("🖖", "🥌") | ("🖖", "✂"):
                    self.puntuacion_jugador += 1

                case _:
                    self.puntuacion_npc += 1
        else:
            self.puntuacion_jugador += 1
            self.mostrar_modal_ganastes = True

        if self.puntuacion_npc > 4 :
            self.mostrar_modal_perdistes = True


    def npc(self):
        self.jugada_npc = random.choice(["🥌","📋","✂","🦎","🖖"])

    def piedra(self):
        self.jugada_jugador = "🥌"
        self.npc()
        self.logica()

    def papel(self):
        self.jugada_jugador = "📋"
        self.npc()
        self.logica()

    def tijeras(self):
        self.jugada_jugador = "✂"
        self.npc()
        self.logica()

    def lagarto(self):
        self.jugada_jugador = "🦎"
        self.npc()
        self.logica()

    def spock(self):
        self.jugada_jugador = "🖖"
        self.npc()
        self.logica()

    def reiniciar_juego(self):
        self.jugada_npc:str= "?"
        self.jugada_jugador:str= "?"
        self.puntuacion_npc:int= 0
        self.puntuacion_jugador:int= 0
        self.mostrar_modal_perdistes= False
        self.mostrar_modal_ganastes= False

    @rx.var
    def var_jugada_npc(self) -> str:
        return self.jugada_npc

    @rx.var
    def var_jugada_jugador(self) -> str:
        return self.jugada_jugador

    @rx.var
    def var_puntuacion_jugador(self) -> int:
        return self.puntuacion_jugador

    @rx.var
    def var_puntuacion_npc(self) -> int:
        return self.puntuacion_npc

# Función para crear los botones con los emojis de las jugadas
def botones(emoji: str , event:EstadoJuego) -> rx.Component:
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
        on_click=event,
        _hover=_hover_generico
    )

# Función para mostrar la puntuación
def puntuacion(texto: str, valor:EstadoJuego) -> rx.Component:
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

    return rx.center(
            rx.box(
            # Iteramos sobre la lista de reglas para generar los textos
            *(rx.text(regla,
                    font_size=TamañosTexto.SUBTITULO.value,
                    color=Colores.TEXTO.value,
                    align="center") for regla in reglas),
            height="auto",
            width="20vw",
            bg=Colores.BG_COMPONENTES.value,
            margin=Tamaños.MARGIN_MEDIANO.value,
            padding= Tamaños.PADDING.value
        )
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
                        rx.text(EstadoJuego.jugada_npc, font_size=["80px", "100px", "120px"], color="white"),
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
                        rx.text(EstadoJuego.jugada_jugador, font_size=["80px", "100px", "120px"], color="white"),
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
                    botones("🥌", EstadoJuego.piedra),  # Botón Piedra
                    botones("📋", EstadoJuego.papel),  # Botón Papel
                    botones("✂️", EstadoJuego.tijeras),  # Botón Tijeras
                    botones("🦎", EstadoJuego.lagarto),  # Botón Lagarto
                    botones("🖖", EstadoJuego.spock),  # Botón Spock
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
    return rx.desktop_only(
        rx.hstack(
            rx.vstack(
                puntuacion("NPC", EstadoJuego.puntuacion_npc),
                puntuacion("Tú", EstadoJuego.puntuacion_jugador),
                margin_x=Tamaños.MARGIN_MEDIANO.value
            ),
            bloque_juego(),
            rx.center(
                sistema_de_victoria_text(),
            ),
            margin_y=25
        )
    )

def mobile_and_tablets_juegos() -> rx.Component:
    return rx.mobile_and_tablet(
        bloque_juego(),
        rx.hstack(
                puntuacion("NPC", EstadoJuego.puntuacion_npc),
                puntuacion("Tú", EstadoJuego.puntuacion_jugador),
                margin_x=Tamaños.MARGIN_MEDIANO.value,

        ),
        margin_y=25
    )

# Página del juego
@rx.page(route=routers.PIEDRA_PAPEL_TIJERAS.value)
def pantalla_juego2() -> rx.Component:
    """Página que contiene el juego 'Piedra, Papel, Tijeras, Lagarto, Spock'."""
    return rx.box(
        rx.vstack(
            navbar(),
            rx.box(
                desktop_juegos(),
                mobile_and_tablets_juegos(),
            ),
            modal_ganastes(EstadoJuego, random.choice(textos_victoria)),
            modal_perdistes(EstadoJuego, random.choice(texto_derrota)),
            align_items="stretch"
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height="100vh"
    )
