import reflex as rx

from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, TamañosTexto, _hover_generico


def tarjetas() -> rx.Component:
    return rx.box(
        rx.center(
            rx.accordion.root(
                rx.accordion.item(
                    header=rx.markdown("# ¿Cómo se juega Piedra, Papel, Tijeras, Lagarto, Spock?"),
                    content=rx.markdown("""
                Este juego es una versión ampliada del clásico Piedra, Papel, Tijeras.
                Las reglas son las siguientes:

                - Piedra aplasta a Tijeras.
                - Tijeras cortan Papel.
                - Papel cubre a Piedra.
                - Piedra aplasta a Lagarto.
                - Lagarto envenena a Spock.
                - Spock destruye Tijeras.
                - Tijeras decapitan a Lagarto.
                - Lagarto se come Papel.
                - Papel desautoriza a Spock.
                - Spock vaporiza a Piedra.

                El objetivo es elegir un símbolo que derrote al de tu oponente.
                """,),
                    font_size=TamañosTexto.TEXTO.value,
                    _hover=_hover_generico,
                    border_radius=Tamaños.BORDER_RADIUS.value,
                    value="item_1",
                    padding=Tamaños.PADDING.value,
                ),
                rx.accordion.item(
                    header=rx.markdown("# ¿Es posible jugar en dispositivos móviles?"),
                    content=rx.markdown("""
                    Sí, la página está optimizada para dispositivos móviles, así que puedes disfrutar de los juegos en
                    cualquier lugar.
                    """
                    ),
                    font_size=TamañosTexto.TEXTO.value,
                    _hover=_hover_generico,
                    border_radius=Tamaños.BORDER_RADIUS.value,
                    value="item_2",
                    padding=Tamaños.PADDING.value
                ),
                rx.accordion.item(
                    header=rx.markdown("# ¿Cómo funciona el juego Encuentra el Número?"),
                    content=rx.markdown("""
                    En este juego, debes adivinar un número del 1 al 100. Después de cada intento, recibirás pistas que te ayudarán
                    a acercarte al número correcto. Intenta adivinar antes de que se te acaben las oportunidades.
                    """
                    ),
                    font_size=TamañosTexto.TEXTO.value,
                    _hover=_hover_generico,
                    border_radius=Tamaños.BORDER_RADIUS.value,
                    value="item_3",
                    padding=Tamaños.PADDING.value
                ),
                rx.accordion.item(
                    header=rx.markdown("# Con que se desarrollo esta web"),
                    content=rx.markdown("Este sitio web fue completamente desarrollado en Python, utilizando el framework Reflex Full-Stack para ofrecer una experiencia dinámica y eficiente"),
                    font_size=TamañosTexto.TEXTO.value,
                    _hover=_hover_generico,
                    border_radius=Tamaños.BORDER_RADIUS.value,
                    value="item_4",
                    padding=Tamaños.PADDING.value
                ),
                # ... (repite para los demás items)
                width="98%",
                variant="ghost",
                collapsible=True,
                text_align="left",
                style={
                    "background_color": "transparent",
                },
            ),
        ),
        width="95%",
        height="90%",
        bg=Colores.BG_COMPONENTES.value,
        text_aling="center",
        border_radius=Tamaños.BORDER_RADIUS.value,
        margin="0.5em"
    )

@rx.page(route=routers.FQA.value)
def FAQ_pantalla () -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
        tarjetas(),
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height="100vh",
    )