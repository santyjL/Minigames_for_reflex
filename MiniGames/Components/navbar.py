import reflex as rx

from MiniGames.routers import routers
from MiniGames.styles import Colores, TamañosTexto


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(
            text,
            font_size=TamañosTexto.SUBTITULO.value,
            weight="medium",
            color = Colores.TEXTO.value
            ),
        href=url,
        text_decoration="none"

    )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/favicon.ico",
                        width="2.75em",
                        height="auto",
                        border_radius="25%",
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("JUEGOS", routers.PRINCIPAL.value),
                    navbar_link("FQA", routers.FQA.value),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/favicon.ico",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu",
                                font_size= TamañosTexto.SUBTITULO.value ,
                                color = Colores.TEXTO.value)
                    ),
                    rx.menu.content(
                        rx.menu.item(navbar_link("JUEGOS" ,routers.PRINCIPAL.value) , color = Colores.TEXTO.value),
                        rx.menu.item(navbar_link("FQA" , routers.FQA.value) , color = Colores.TEXTO.value),
                        bg=Colores.SECUNDARIO.value,
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=Colores.SECUNDARIO.value,
        padding="0.3em",
        padding_x = "1em",
        #position="fixed",
        #top="0px",
        #z_index="5",
        width="100%",
    )