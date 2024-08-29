from enum import Enum


class TamañosTexto(Enum):
    TITULO = "2.5em"
    SUBTITULO = "2em"
    TEXTO = "1.5em"

class Colores(Enum):
    BG = "linear-gradient(#7A0C0C , #8B89E7)"
    BG_COMPONENTES = "#FFFFFF22"
    PRINCIPAL = "#DE1010"
    SECUNDARIO = "#211F6A"

    TEXTO = "#C1C1C1"
    SUBTITULO = "#FFFFFF"
    TITULO = "#000000"

class Tamaños (Enum):
    MARGIN_PEQUEÑO = "0.5em"
    MARGIN_MEDIANO = "1em"
    MARGIN_GRANDE = "2em"

    PADDING = "1.5em"

    BORDER_RADIUS = "2em"

    BORDER = "solid #000000"

_hover_generico={
    "transform": "scale(1.05)",
    "transition": "all 0.5s ease-in-out",
    "filter": "drop-shadow(0 0 30px rgba(150, 255, 50, 1.5))",
    },

juegos_movil_y_tableta = dict(
    padding = Tamaños.PADDING.value,
    margin = Tamaños.MARGIN_PEQUEÑO.value,
    bg = Colores.PRINCIPAL.value,
    width = "65vw",
    border_radius = Tamaños.BORDER_RADIUS.value,
    border = Tamaños.BORDER.value,
    align = "center",
    _hover = _hover_generico
    )
