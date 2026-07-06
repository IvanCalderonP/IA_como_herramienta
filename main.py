import sys
from tkinter import Tk, filedialog

from analizador import analizar_archivo, mostrar_resumen


def seleccionar_archivo():
    try:
        # Se usa una ventana de selección para permitir elegir el archivo sin escribir la ruta manualmente.
        ventana = Tk()
        ventana.withdraw()
        ruta = filedialog.askopenfilename(
            title="Selecciona un archivo de log",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
        )
        ventana.destroy()
        return ruta or None
    except Exception:
        try:
            return input("Introduce la ruta del archivo: ").strip() or None
        except EOFError:
            return None


def main() -> int:
    print("Analizador de logs")
    try:
        ruta = sys.argv[1] if len(sys.argv) > 1 else seleccionar_archivo()
        if not ruta:
            print("No se seleccionó ningún archivo o se canceló la operación.")
            return 1

        resumen = analizar_archivo(ruta)
        mostrar_resumen(resumen)
        return 0
    except FileNotFoundError as error:
        print(error)
        return 1
    except ValueError as error:
        print(error)
        return 1
    except Exception as error:
        print(f"Error inesperado: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
