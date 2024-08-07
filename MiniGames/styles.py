from enum import Enum


class TamañosTexto(Enum):
    TITULO = "2.5em"
    SUBTITULO = "2em"
    TEXTO = "1.5em"

class Colores(Enum):
    BG = "linear-gradient(#7A0C0C , #8B89E7)"
    PRINCIPAL = "#DE1010"
    SECUNDARIO = "#0A0897"

    TEXTO = "#C1C1C1"
    SUBTITULO = "#FFFFFF"
    TITULO = "#000000"

class Tamaños (Enum):
    MARGIN_PEQUEÑO = "0.5em"
    MARGIN_MEDIANO = "1em"
    MARGIN_GRANDE = "2em"

    PADDING = "1em"

    BORDER_RADIUS = "2em"

    BORDER = "solid #000000"

juegos_movil_y_tableta = dict(
    padding = Tamaños.PADDING.value,
    margin = Tamaños.MARGIN_MEDIANO.value,
    bg = Colores.PRINCIPAL.value,
    width = "100wv",
    border_radius = Tamaños.BORDER_RADIUS.value,
    border = Tamaños.BORDER.value,
    align = "left"
    )