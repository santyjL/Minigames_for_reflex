import random

import reflex as rx

from MiniGames.Components.class_base import classBase
from MiniGames.Components.modal import modal_ganastes, modal_perdistes
from MiniGames.Components.navbar import navbar
from MiniGames.routers import routers
from MiniGames.styles import Colores, Tamaños, TamañosTexto, _hover_generico

mensajes_victoria:list = [
    "¡Ganaste como un verdadero estratega! 🎉",
    "¡Toma eso, tablero! ¡Victoria absoluta! 😎",
    "¡Ja! ¡Ganaste! ¡Este tablero nunca tuvo oportunidad! 😜",
    "¡Triunfo asegurado! ¡La suerte no tuvo nada que ver! 👊",
    "¡Victoria! ¡Los dioses del 3 en raya están contigo! 😇",
    "¡Ganaste! ¡Demasiado fácil para un maestro del 3 en raya como tú! 🧠",
    "¡Líneas completas, enemigo derrotado! ¡Eres imparable! 🥳"
]

mensajes_derrota:list = [
    "¡Perdiste! Pero, hey, siempre hay revancha. 😅",
    "¡Vaya! Esta vez el tablero te venció... ¿Intentas de nuevo? 🙃",
    "¡Lo siento, esta no fue la tuya! ¿Sigues jugando? 😜",
    "¡Oh no! Caíste en una trampa perfecta. Mejor suerte la próxima vez. 🤓",
    "¡Perdiste, pero el tablero quiere otro desafío! 😈",
    "¡Ups! ¡Derrota aplastante! Pero seguro que puedes mejorar. 🤔",
    "¡Game over! El 3 en raya es implacable a veces... 😬"
]

# region: Estado del Juego
class EstadoJuego(classBase):
    """Clase para gestionar el estado del juego de 3 en raya."""
    # Variables de estado del juego
    tablero: list = [""] * 9
    jugador_actual: str = "❌"
    ronda: int = 1
    puntaje_jugador: int = 0
    puntaje_ia: int = 0
    juego_terminado: bool = False


    # region: Métodos de reinicio
    def reiniciar_partido(self):
        """Reinicia el tablero a su estado inicial para una nueva ronda."""
        self.tablero = [""] * 9
        self.jugador_actual = "❌"
        self.juego_terminado = False

    def reiniciar_juego(self):
        """Reinicia el juego completo, incluyendo puntajes y rondas."""
        self.reiniciar_partido()
        self.ronda = 1
        self.puntaje_jugador = 0
        self.puntaje_ia = 0
        self.mostrar_modal_perdistes = False
        self.mostrar_modal_ganastes = False
    # endregion

    # region: Métodos de verificación
    def verificar_ganador(self, tablero):
        """Verifica si hay un ganador en el tablero."""
        combinaciones = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combo in combinaciones:
            if tablero[combo[0]] == tablero[combo[1]] == tablero[combo[2]] != "":
                return tablero[combo[0]]
        return None

    def verificar_empate(self, tablero):
        """Verifica si el tablero está lleno y no hay ganador."""
        return all(celda != "" for celda in tablero)
    # endregion

    # region: Métodos de puntaje y rondas
    def actualizar_puntajes(self, ganador):
        """Actualiza los puntajes según el ganador de la ronda."""
        if ganador == "❌":
            self.puntaje_jugador += 1
        elif ganador == "⭕":
            self.puntaje_ia += 1

    def siguiente_ronda(self, ganador=None):
        """Avanza a la siguiente ronda o declara el ganador general."""
        if ganador:
            self.actualizar_puntajes(ganador)

        # Verificar si se alcanza la condición de victoria
        if self.ronda < 20 and max(self.puntaje_jugador, self.puntaje_ia) < 10:
            self.ronda += 1
            self.reiniciar_partido()
        else:
            self.mostrar_modal_perdistes = True
            self.mostrar_modal_ganastes = self.puntaje_jugador > self.puntaje_ia
            self.mostrar_modal_perdistes = self.puntaje_ia >= self.puntaje_jugador
    # endregion

    # region: Lógica de movimientos
    def realizar_movimiento(self, posicion):
        """Permite al jugador realizar una jugada en la posición especificada."""
        if self.tablero[posicion] == "" and not self.juego_terminado:
            self.tablero[posicion] = self.jugador_actual
            ganador = self.verificar_ganador(self.tablero)
            if ganador:
                self.juego_terminado = True
                self.siguiente_ronda(ganador=ganador)
            elif self.verificar_empate(self.tablero):
                self.juego_terminado = True
                self.siguiente_ronda()
            else:
                self.jugador_actual = "⭕" if self.jugador_actual == "❌" else "❌"
                if self.jugador_actual == "⭕":
                    self.movimiento_ia()

    def minimax(self, tablero, es_maximizador):
        """Implementa el algoritmo Minimax para decidir el mejor movimiento de la IA."""
        ganador = self.verificar_ganador(tablero)
        if ganador == "⭕":
            return 1  # Si la IA gana
        elif ganador == "❌":
            return -1  # Si el jugador gana
        elif self.verificar_empate(tablero):
            return 0  # Empate

        if es_maximizador:
            mejor_puntaje = -float('inf')
            for i in range(9):
                if tablero[i] == "":
                    tablero[i] = "⭕"
                    puntaje = self.minimax(tablero, False)
                    tablero[i] = ""
                    mejor_puntaje = max(mejor_puntaje, puntaje)
            return mejor_puntaje
        else:
            mejor_puntaje = float('inf')
            for i in range(9):
                if tablero[i] == "":
                    tablero[i] = "❌"
                    puntaje = self.minimax(tablero, True)
                    tablero[i] = ""
                    mejor_puntaje = min(mejor_puntaje, puntaje)
            return mejor_puntaje

    def movimiento_ia(self):
        """La IA realiza un movimiento: el primer movimiento de cada ronda es aleatorio, el resto usa Minimax."""
        # Verificar si es el primer movimiento de la IA en la ronda actual
        if self.tablero.count("") == 9 or (self.jugador_actual == "⭕" and self.tablero.count("❌") == 1):
            # Primer movimiento aleatorio en cada ronda
            posiciones_libres = [i for i, v in enumerate(self.tablero) if v == ""]
            if posiciones_libres:
                posicion = random.choice(posiciones_libres)
                self.realizar_movimiento(posicion)
        else:
            # Movimientos posteriores: usa el algoritmo Minimax
            mejor_puntaje = -float('inf')
            mejor_movimiento = None
            for i in range(9):
                if self.tablero[i] == "":
                    self.tablero[i] = "⭕"
                    puntaje = self.minimax(self.tablero, False)
                    self.tablero[i] = ""
                    if puntaje > mejor_puntaje:
                        mejor_puntaje = puntaje
                        mejor_movimiento = i
            if mejor_movimiento is not None:
                self.realizar_movimiento(mejor_movimiento)


    # endregion

    # region: Variables Reactivas
    @rx.var
    def var_ronda_actual(self) -> int:
        return self.ronda

    @rx.var
    def var_puntaje_jugador(self) -> int:
        return self.puntaje_jugador

    @rx.var
    def var_puntaje_ia(self) -> int:
        return self.puntaje_ia
    # endregion
# endregion

# region: Componentes UI
def tablero(ancho, alto, ancho_boton) -> rx.Component:
    return rx.box(
        rx.grid(
            *[
                rx.button(
                    rx.cond(
                        EstadoJuego.tablero[i] != "",
                        EstadoJuego.tablero[i],
                        " "
                    ),
                    width=ancho_boton,  # Ajustes para móvil (30vw) y escritorio (10vw)
                    height=alto,  # Ajustes para móvil (30vw) y escritorio (10vw)
                    bg="#0000", border="solid #FFFFFF",
                    on_click=lambda i=i: EstadoJuego.realizar_movimiento(i),
                ) for i in range(9)
            ],
            rx.mobile_and_tablet(width="90%", height="90%", margin=Tamaños.MARGIN_PEQUEÑO.value),
            columns="3", rows="3",
            margin=Tamaños.MARGIN_GRANDE.value,
            padding=Tamaños.PADDING.value,
            bg=Colores.BG_COMPONENTES.value,
            width=ancho,  # Tamaño para móvil y escritorio
            height=["85vw", "70vh"], # Tamaño para móvil y escritorio,
            border_radius=Tamaños.BORDER_RADIUS.value,
            border=Tamaños.BORDER.value
        ),
        display="flex",
        justify_content="center",
        align_items="center"
    )

def ronda(ancho, margen) -> rx.Component:
    return rx.center(
        rx.box(
            rx.text(
                "Ronda",
                font_size=["20px", TamañosTexto.SUBTITULO.value],
                color=Colores.TEXTO.value,
                align="center"
            ),
            rx.box(
                rx.text(
                    EstadoJuego.var_ronda_actual,
                    font_size=["30px","20px", TamañosTexto.TITULO.value],
                    color=Colores.TITULO.value,
                    align="center"
                ),
                bg=Colores.SECUNDARIO.value,
                width=ancho,  # Ajuste del tamaño para móvil (90vw) y escritorio (20vw)
                height="auto",
                padding=Tamaños.PADDING.value,
                margin=Tamaños.MARGIN_MEDIANO.value,
                display="flex",
                justify_content="center",
                align_text="center",
                border_radius=Tamaños.BORDER_RADIUS.value,
                border=Tamaños.BORDER.value
            ),
            # Márgenes específicos para cada tipo de dispositivo
            margin_y = margen
        ),
        width="100%",  # Aseguramos que el centro ocupe todo el ancho
        height="100%", # Aseguramos que el centro ocupe toda la altura
        display="flex",
        direction="column",
        justify="center",
        align_items="center",
    )

def puntuacion(nombre: str, valor: rx.Var[int]) -> rx.Component:
    return rx.box(
        rx.text(nombre, font_size=["20px", TamañosTexto.TEXTO.value], color=Colores.TITULO.value, align="center"),
        rx.box(
            rx.text(valor, font_size=["40px", "60px", "80px", "100px", "120px"], color=Colores.TITULO.value, align="center", _hover=_hover_generico),
            rx.desktop_only(width="12vw"),
            rx.mobile_and_tablet(width="15vw"),  # Tamaño ajustado para móvil
            bg=Colores.BG_COMPONENTES.value, border_radius=Tamaños.BORDER_RADIUS.value,
            border=Tamaños.BORDER.value, padding=Tamaños.PADDING.value,
            align_text="center"
        ),
        rx.mobile_and_tablet(width="35vw",margin_x="0px",),
        margin=Tamaños.MARGIN_PEQUEÑO.value,
        _hover=_hover_generico,
        align_text= "center"
    )

# Configuración de la pantalla de juego ajustada
@rx.page(route=routers.TRES_EN_RAYA.value)
def pantalla_juego3() -> rx.Component:
    return rx.box(
        rx.vstack(
            navbar(),
            # Configuración de escritorio
            rx.desktop_only(
                rx.hstack(
                    tablero("40vw", "auto" , "auto"),
                    ronda("20vw" , 175),
                    rx.vstack(
                        puntuacion("TÚ", EstadoJuego.var_puntaje_jugador),
                        puntuacion("NPC", EstadoJuego.var_puntaje_ia)
                    ),
                    spacing="4"
                )
            ),
            # Configuración móvil y tablet: centrado verticalmente
                rx.mobile_and_tablet(
                    rx.center(
                        rx.box(
                            rx.center(
                                ronda("35vw" , 5),
                            ),
                            tablero("80vw" , "auto", "23vw"),
                            rx.center(
                                rx.box(
                                    rx.hstack(
                                        puntuacion("NPC", EstadoJuego.var_puntaje_ia),
                                        puntuacion("JUGADOR", EstadoJuego.var_puntaje_jugador),
                                        bg=Colores.BG_COMPONENTES.value,
                                        border_radius=Tamaños.BORDER_RADIUS.value,
                                        border=Tamaños.BORDER.value,
                                        margin_y=Tamaños.MARGIN_PEQUEÑO.value
                                    ),
                                ),
                            ),
                            min_height="100vh",  # Altura mínima de la pantalla completa para centrar verticalmente
                            min_width="100vw"
                    )
                )
            ),
            modal_ganastes(EstadoJuego, random.choice(mensajes_victoria)),
            modal_perdistes(EstadoJuego, random.choice(mensajes_derrota)),
            bg=Colores.BG.value,
            background_size="cover",
            min_height="100vh",
            min_width="100vw"
        )
    )