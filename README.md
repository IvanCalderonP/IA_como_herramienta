# Analizador de logs en Python

Este proyecto permite seleccionar un archivo de texto, leerlo línea por línea y generar un resumen de los eventos detectados. El programa identifica niveles de severidad, valida fechas y reporta líneas mal formadas.

## Requisitos

- Python 3.9 o superior
- Módulos estándar de Python, sin dependencias externas

## Ejecución

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta:
   ```bash
   python3.13.exe main.py
   ```
3. Selecciona un archivo de texto desde el explorador o proporciona la ruta como argumento:
   ```bash
   python main.py logs/log_bueno.txt
   ```

## Archivos de prueba

La carpeta logs contiene ejemplos de distintos casos:

- log_bueno.txt: archivo con eventos bien formados.
- log_fecha_invalida.txt: incluye una fecha inválida.
- log_sin_nivel.txt: muestra líneas sin un nivel de severidad válido.
- log_mixto.txt: combina eventos válidos, inválidos y líneas vacías.

## Evidencia de pruebas

Se realizaron pruebas básicas con los archivos de ejemplo para comprobar el comportamiento del programa.

- Archivo bien formado: log_bueno.txt
  - Resultado esperado: 4 eventos, 2 INFO, 1 WARNING, 1 ERROR, 0 fechas inválidas.
  - Resultado obtenido: coincidente con lo esperado.

- Archivo con errores: log_fecha_invalida.txt
  - Resultado esperado: 3 eventos, 1 fecha válida, 2 fechas inválidas y 2 líneas mal formadas.
  - Resultado obtenido: coincidente con lo esperado.

Para verificarlo, se ejecutó:

```bash
py -3 -m unittest discover -s tests -v
```

## Estructura del proyecto

- main.py: punto de entrada del programa.
- analizador.py: lógica para procesar y resumir el contenido del archivo.
- validador.py: funciones para validar fechas, niveles y formato de línea.
- tests/test_analizador.py: pruebas básicas del comportamiento del analizador.
