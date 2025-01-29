"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from .page.FAQ import FAQ_pantalla
from .page.juego1 import pantalla_juego1
from .page.juego2 import pantalla_juego2
from .page.juego3 import pantalla_juego3
from .page.principal import pantalla_principal
from .routers import routers

app = rx.App()


