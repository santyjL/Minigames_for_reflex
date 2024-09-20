import reflex as rx

from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, TamañosTexto, _hover_generico


def tarjetas() -> rx.Component:
    return rx.box(
        rx.center(
            rx.accordion.root(
                rx.accordion.item(
                    header="Con que se desarrollo esta web",
                    content="Esta web fue totalmente desarrollada con python utilizando el framework de reflex full-stack",
                    font_size = TamañosTexto.TEXTO.value,
                    _hover = _hover_generico,
                    value="item_1",
                    padding= Tamaños.PADDING.value,
                ),
                rx.accordion.item(
                    header="Con que se desarrollo esta web",
                    content="Esta web fue totalmente desarrollada con python utilizando el framework de reflex full-stack",
                    font_size = TamañosTexto.TEXTO.value,
                    _hover = _hover_generico,
                    value="item_2",
                    padding= Tamaños.PADDING.value
                ),
                rx.accordion.item(
                    header="Con que se desarrollo esta web",
                    content="Esta web fue totalmente desarrollada con python utilizando el framework de reflex full-stack",
                    font_size = TamañosTexto.TEXTO.value,
                    _hover = _hover_generico,
                    value="item_3",
                    padding= Tamaños.PADDING.value
                ),
                rx.accordion.item(
                    header="Con que se desarrollo esta web",
                    content="Esta web fue totalmente desarrollada con python utilizando el framework de reflex full-stack",
                    font_size = TamañosTexto.TEXTO.value,
                    _hover = _hover_generico,
                    value="item_4",
                    padding= Tamaños.PADDING.value
                ),
                rx.accordion.item(
                    header="Con que se desarrollo esta web",
                    content="Esta web fue totalmente desarrollada con python utilizando el framework de reflex full-stack",
                    font_size = TamañosTexto.TEXTO.value,
                    _hover = _hover_generico,
                    value="item_5",
                    padding= Tamaños.PADDING.value
                ),
                width="98%",
                variant="ghost",
                collapsible=True,
                text_align="left",
                style={
                    "background_color": "transparent",
                },
            ),
        ),
        width= "95%",
        height = "90%",
        bg=Colores.BG_COMPONENTES.value,
        text_aling= "center",
        border_radius=Tamaños.BORDER_RADIUS.value,
        margin = "1em"
    )

@rx.page(route=routers.FQA.value)
def FQA_pantalla () -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
        tarjetas(),
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height="100vh",
    )