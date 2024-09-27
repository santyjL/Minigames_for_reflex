import reflex as rx

from MiniGames.Components.class_base import classBase
from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, TamañosTexto


@rx.page(route=routers.PIEDRA_PAPEL_TIJERAS.value)
def pantalla_juego2() -> rx.components:
    return rx.box(
        rx.vstack(
            navbar(),
            align_items="stretch",
            width="100%",
        ),
        bg=Colores.BG.value,
        background_size="cover",
        min_height="100vh",
    )