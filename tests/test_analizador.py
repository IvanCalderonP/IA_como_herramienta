import tempfile
import unittest
from pathlib import Path

from analizador import analizar_archivo


class AnalizadorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base_dir = Path(__file__).resolve().parents[1]
        self.logs_dir = self.base_dir / "logs"

    def test_log_bueno(self) -> None:
        resumen = analizar_archivo(self.logs_dir / "log_bueno.txt")

        self.assertEqual(resumen["total_eventos"], 4)
        self.assertEqual(resumen["info"], 2)
        self.assertEqual(resumen["warning"], 1)
        self.assertEqual(resumen["error"], 1)
        self.assertEqual(resumen["lineas_fecha_valida"], 4)
        self.assertEqual(resumen["lineas_fecha_invalida"], 0)
        self.assertEqual(resumen["lineas_mal_formadas"], 0)

    def test_log_fecha_invalida(self) -> None:
        resumen = analizar_archivo(self.logs_dir / "log_fecha_invalida.txt")

        self.assertEqual(resumen["total_eventos"], 3)
        self.assertEqual(resumen["lineas_fecha_valida"], 1)
        self.assertEqual(resumen["lineas_fecha_invalida"], 2)
        self.assertEqual(resumen["lineas_mal_formadas"], 2)

    def test_archivo_vacio(self) -> None:
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as archivo:
            archivo.write("")
            ruta = archivo.name

        try:
            resumen = analizar_archivo(ruta)
            self.assertTrue(resumen["archivo_vacio"])
            self.assertEqual(resumen["total_eventos"], 0)
        finally:
            Path(ruta).unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
