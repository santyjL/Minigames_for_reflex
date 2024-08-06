"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from MiniGames.page.principal import pantalla_principal

app = rx.App()
app.add_page(pantalla_principal , route="/")
