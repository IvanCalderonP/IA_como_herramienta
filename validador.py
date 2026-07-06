import re
from datetime import datetime

SEVERIDADES_VALIDAS = {"INFO", "WARNING", "ERROR"}


def limpiar_texto(texto: str) -> str:
    return re.sub(r"\s+", " ", texto.strip())


def extraer_fecha(texto: str):
    coincidencia = re.search(r"\b(\d{4}-\d{2}-\d{2})\b", texto)
    return coincidencia.group(1) if coincidencia else None


def extraer_nivel(texto: str):
    coincidencia = re.search(r"\b(INFO|WARNING|ERROR)\b", texto, flags=re.IGNORECASE)
    return coincidencia.group(1).upper() if coincidencia else None


def extraer_mensaje(texto: str, fecha=None, nivel=None) -> str:
    mensaje = texto.strip()
    if fecha:
        mensaje = mensaje.replace(fecha, "", 1).strip()
    if nivel:
        mensaje = re.sub(rf"\b{re.escape(nivel)}\b", "", mensaje, count=1, flags=re.IGNORECASE).strip()
    return limpiar_texto(mensaje)


def validar_fecha(texto: str) -> bool:
    try:
        datetime.strptime(texto, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def evaluar_linea(linea: str) -> dict:
    linea_limpia = linea.strip()
    if not linea_limpia:
        return {
            "es_vacia": True,
            "fecha": None,
            "nivel": None,
            "mensaje": "",
            "fecha_valida": False,
            "es_mal_formada": False,
        }

    fecha = extraer_fecha(linea_limpia)
    nivel = extraer_nivel(linea_limpia)
    mensaje = extraer_mensaje(linea_limpia, fecha, nivel)
    fecha_valida = bool(fecha and validar_fecha(fecha))

    # Una línea se considera mal formada cuando falta información esencial o la fecha no es válida.
    es_mal_formada = (
        nivel is None
        or not mensaje
        or fecha is None
        or not fecha_valida
    )

    return {
        "es_vacia": False,
        "fecha": fecha,
        "nivel": nivel,
        "mensaje": mensaje,
        "fecha_valida": fecha_valida,
        "es_mal_formada": es_mal_formada,
    }
