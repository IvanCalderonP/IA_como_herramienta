from pathlib import Path

from validador import evaluar_linea


def analizar_archivo(ruta_archivo: str) -> dict:
    ruta = Path(ruta_archivo)
    if not ruta.exists():
        raise FileNotFoundError(f"El archivo no existe: {ruta}")
    if not ruta.is_file():
        raise ValueError("La ruta no apunta a un archivo válido.")

    resumen = {
        "ruta": str(ruta),
        "total_eventos": 0,
        "info": 0,
        "warning": 0,
        "error": 0,
        "lineas_fecha_valida": 0,
        "lineas_fecha_invalida": 0,
        "lineas_mal_formadas": 0,
        "archivo_vacio": False,
        "mensaje": "",
    }

    contenido = ruta.read_text(encoding="utf-8")
    if not contenido.strip():
        resumen["archivo_vacio"] = True
        resumen["mensaje"] = "El archivo está vacío."
        return resumen

    with ruta.open("r", encoding="utf-8") as archivo:
        for linea in archivo:
            # Cada línea se valida de forma independiente para contar eventos y detectar errores de formato.
            resultado = evaluar_linea(linea)
            if resultado["es_vacia"]:
                continue

            resumen["total_eventos"] += 1

            if resultado["fecha"] is not None:
                if resultado["fecha_valida"]:
                    resumen["lineas_fecha_valida"] += 1
                else:
                    resumen["lineas_fecha_invalida"] += 1

            if resultado["es_mal_formada"]:
                resumen["lineas_mal_formadas"] += 1
                continue

            nivel = resultado["nivel"].lower()
            if nivel in resumen:
                resumen[nivel] += 1

    return resumen


def mostrar_resumen(resumen: dict) -> None:
    print("\nResumen del archivo de logs")
    print(f"Ruta: {resumen['ruta']}")
    print(f"Total de eventos: {resumen['total_eventos']}")
    print(f"INFO: {resumen['info']}")
    print(f"WARNING: {resumen['warning']}")
    print(f"ERROR: {resumen['error']}")
    print(f"Líneas con fecha válida: {resumen['lineas_fecha_valida']}")
    print(f"Líneas con fecha inválida: {resumen['lineas_fecha_invalida']}")
    print(f"Líneas mal formadas: {resumen['lineas_mal_formadas']}")
    if resumen.get("mensaje"):
        print(resumen["mensaje"])
