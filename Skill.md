# Skill: Validación de scripts principales en Python para consola

## Propósito

Esta skill sirve para revisar scripts principales de proyectos Python ejecutables desde consola y verificar que sigan buenas prácticas de programación, incluyendo manejo de errores con try/except, validación de entradas, uso de argumentos y claridad en la salida.

## Cuándo usarla

Usa esta skill cuando quieras revisar o mejorar un archivo como `main.py`, `app.py` o cualquier punto de entrada que:

- se ejecute desde la terminal;
- lea argumentos o archivos del usuario;
- interactúe con archivos, entradas de consola o interfaces gráficas;
- deba devolver un código de salida claro.

## Modo de trabajo

Al aplicar esta skill:

- Analiza el archivo principal del proyecto.
- Identifica los problemas según el checklist de esta skill.
- **No modifiques el archivo original.**
- **Genera un nuevo archivo Python con todas las mejoras aplicadas.**
- Conserva el comportamiento original del programa siempre que sea posible.
- Mantén una estructura clara y legible.
- Generame un archivo "Cambios.md" donde se expliquen todas las obsersioaciones y mejoras realizadas.

## Nombre del archivo generado

El archivo generado debe conservar el nombre original agregando el sufijo `_mejorado`.

Ejemplos:

- `main.py` → `main_mejorado.py`
- `app.py` → `app_mejorado.py`
- `programa.py` → `programa_mejorado.py`

## Checklist de revisión

### 1. Estructura del punto de entrada

- Debe tener una función `main()`.
- Debe incluir `if __name__ == "__main__":`.
- La lógica debe estar separada de la ejecución directa.

### 2. Manejo de errores

- Debe usar `try/except` para capturar errores esperables como:
  - `FileNotFoundError`
  - `ValueError`
  - `OSError`
  - `UnicodeError`
- Los mensajes deben ser claros y orientados al usuario.
- No deben existir excepciones sin controlar.

### 3. Validación de argumentos y entradas

- Validar los argumentos recibidos.
- Informar claramente cuando falten parámetros obligatorios.
- Verificar la existencia de archivos o recursos antes de utilizarlos.

### 4. Buenas prácticas de consola

- Retornar `0` cuando la ejecución sea correcta.
- Retornar un código distinto de `0` cuando ocurra un error.
- Mostrar mensajes útiles para el usuario.
- Evitar depender de interfaces gráficas.

### 5. Calidad del código

- Utilizar nombres descriptivos.
- Evitar duplicación de código.
- Dividir la lógica en funciones pequeñas.
- Facilitar la creación de pruebas unitarias.

## Recomendaciones

Siempre que sea apropiado:

- usar `argparse`;
- usar `pathlib.Path`;
- encapsular operaciones críticas dentro de `try/except`;
- evitar `except:` genéricos;
- devolver códigos de salida desde `main()`.

## Forma de entrega

Al finalizar:

1. Explica brevemente los problemas encontrados.
2. Indica las mejoras realizadas.
3. Genera el nuevo archivo Python con todos los cambios aplicados.
4. No modifiques el archivo original.
5. El nuevo archivo debe estar listo para ejecutarse sin cambios adicionales.

## Aplicación en este proyecto

Durante la revisión:

- Analiza únicamente el archivo principal del proyecto.
- Mantén la funcionalidad original siempre que sea posible.
- Aplica únicamente las mejoras necesarias para cumplir con el checklist.
- Guarda el resultado en un nuevo archivo con el sufijo `_mejorado.py`.