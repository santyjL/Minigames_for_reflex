import reflex as rx


class classBase(rx.State):
    """Clase base con funcionalidad de modales para juegos."""

    mostrar_modal_perdistes: bool = False  # Variable para manejar la visibilidad del modal de derrota
    mostrar_modal_ganastes: bool = False   # Variable para manejar la visibilidad del modal de victoria

    def reiniciar_juego(self):
        """Esta función debe ser capaz de regresar el juego a su estado original.
        Cada clase que herede de esta deberá implementar su propia versión."""
        pass

    # Variables reactivas para mostrar los modales
    @rx.var
    def var_mostrar_modal_perdistes(self) -> bool:
        return self.mostrar_modal_perdistes

    @rx.var
    def var_mostrar_modal_ganastes(self) -> bool:
        return self.mostrar_modal_ganastes
