import argparse
import sys
from pathlib import Path
from typing import Optional, Sequence

from analizador import analizar_archivo, mostrar_resumen


def seleccionar_archivo() -> Optional[str]:
    """Intenta abrir un selector gráfico de archivos; si no es posible, devuelve None."""
    try:
        import tkinter as tk
        from tkinter import filedialog
    except Exception:
        return None

    try:
        ventana = tk.Tk()
        ventana.withdraw()
        ruta = filedialog.askopenfilename(
            title="Selecciona un archivo de log",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
        )
        ventana.destroy()
        return ruta or None
    except Exception:
        return None


def construir_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analiza un archivo de log y muestra un resumen")
    parser.add_argument("ruta", nargs="?", help="Ruta del archivo de log a analizar")
    return parser


def obtener_ruta(ruta_arg: Optional[str]) -> Optional[str]:
    if ruta_arg:
        return ruta_arg

    if sys.stdin.isatty():
        try:
            return input("Introduce la ruta del archivo: ").strip() or None
        except EOFError:
            return None

    return seleccionar_archivo()


def ejecutar_analisis(ruta: str) -> int:
    ruta_archivo = Path(ruta)
    if not ruta_archivo.exists():
        raise FileNotFoundError(f"El archivo no existe: {ruta_archivo}")
    if not ruta_archivo.is_file():
        raise ValueError("La ruta no apunta a un archivo válido.")

    resumen = analizar_archivo(str(ruta_archivo))
    mostrar_resumen(resumen)
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    print("Analizador de logs")
    parser = construir_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)

    try:
        ruta = obtener_ruta(args.ruta)
        if not ruta:
            print("No se seleccionó ningún archivo o se canceló la operación.")
            return 1

        return ejecutar_analisis(ruta)
    except FileNotFoundError as error:
        print(f"Error: {error}")
        return 1
    except ValueError as error:
        print(f"Error: {error}")
        return 1
    except OSError as error:
        print(f"Error de acceso al archivo: {error}")
        return 1
    except UnicodeError as error:
        print(f"Error al leer el archivo: {error}")
        return 1
    except Exception as error:
        print(f"Error inesperado: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
