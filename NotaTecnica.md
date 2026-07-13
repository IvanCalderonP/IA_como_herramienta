# Nota Técnica — Skill: Validación de scripts principales en Python para consola

## Descripción

Esta Skill automatiza la revisión de scripts principales de aplicaciones Python ejecutables desde consola, aplicando un conjunto de buenas prácticas relacionadas con la estructura del código, manejo de errores, validación de entradas y organización general.

Su propósito es facilitar la identificación de oportunidades de mejora sin modificar el archivo original, generando una versión mejorada del mismo.

---

## Objetivo

Revisar el punto de entrada de una aplicación Python y producir una versión optimizada que siga buenas prácticas de desarrollo, manteniendo el comportamiento original del programa.

---

## Alcance

La Skill está orientada a archivos como:

- `main.py`
- `app.py`
- `run.py`
- cualquier otro archivo que represente el punto de entrada de una aplicación de consola.

---

## Validaciones realizadas

Durante el análisis se verifican los siguientes aspectos:

### Estructura

- Existencia de una función `main()`.
- Uso de `if __name__ == "__main__":`.
- Separación entre la lógica del programa y el punto de entrada.

### Manejo de errores

- Uso adecuado de bloques `try/except`.
- Captura de excepciones comunes.
- Mensajes de error claros para el usuario.
- Evitar excepciones sin controlar.

### Validación de entradas

- Verificación de argumentos recibidos.
- Validación de archivos y rutas.
- Comprobación de recursos antes de utilizarlos.

### Buenas prácticas

- Uso de `argparse` cuando corresponda.
- Uso de `pathlib.Path`.
- Retorno de códigos de salida.
- Organización del código en funciones pequeñas.
- Nombres descriptivos para variables y funciones.

---

## Funcionamiento

La Skill sigue el siguiente flujo:

1. Identifica el archivo principal del proyecto.
2. Analiza el código utilizando el checklist definido.
3. Detecta problemas y oportunidades de mejora.
4. Conserva intacto el archivo original.
5. Genera un nuevo archivo con las mejoras aplicadas utilizando el sufijo `_mejorado.py`.

Ejemplo:

```
main.py
```

↓

```
main_mejorado.py
```

---

## Salida esperada

Al finalizar la ejecución la Skill proporciona:

- Resumen de los problemas encontrados.
- Descripción de las mejoras realizadas.
- Nuevo archivo Python listo para ejecutarse.
- Nombre del archivo generado.

---

## Restricciones

La Skill:

- No modifica el archivo original.
- No elimina funcionalidades existentes.
- No agrega funcionalidades nuevas que no estén relacionadas con las buenas prácticas revisadas.
- Mantiene el comportamiento original del programa siempre que sea posible.

---

## Casos de uso

Esta Skill es útil para:

- Revisiones de código.
- Refactorización de proyectos académicos.
- Preparación de código antes de realizar pruebas.
- Estandarización de proyectos Python.
- Aplicación de buenas prácticas de programación.

---

## Resultado esperado

Después de ejecutar la Skill, el proyecto contará con una versión mejorada del archivo principal, aplicando buenas prácticas de programación, mejorando la legibilidad, robustez y mantenibilidad del código sin alterar la lógica principal de la aplicación.