"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from MiniGames.page.juego1 import pantalla_juego1
from MiniGames.page.principal import pantalla_principal
from MiniGames.routers import routers

app = rx.App()
app.add_page(pantalla_principal , route=routers.PRINCIPAL.value)
app.add_page(pantalla_juego1 , route=routers.ENCUENTRA_EL_NUMERO.value)
