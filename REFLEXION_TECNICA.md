# Reflexión técnica

## Tareas apoyadas por IA

La inteligencia artificial apoyó la generación inicial de la estructura del proyecto, la organización en módulos y la propuesta de funciones reutilizables para validar líneas, fechas y severidades. También ayudó a definir una distribución clara de responsabilidades entre main.py, analizador.py y validador.py.

## Decisiones tomadas por el desarrollador

El desarrollador definió la lógica de negocio principal, incluyendo qué condiciones convierten una línea en mal formada y cómo se deben contar los eventos. También se decidió que el programa permita seleccionar el archivo desde un explorador o recibirlo como argumento desde la consola, lo cual mejora la usabilidad y facilita las pruebas.

## Ejemplo concreto de mejora de una sugerencia de IA

Una sugerencia inicial de la IA proponía validar la fecha con una expresión regular y luego comprobarla. Esa propuesta era incompleta, porque no detectaba de forma fiable fechas imposibles como 2026-02-30. El estudiante identificó la limitación, corrigió la solución y decidió usar datetime.strptime, lo que permitió validar correctamente el formato y la coherencia de la fecha.

## Aprendizaje sobre el uso responsable de la IA

Este ejercicio mostró que la IA puede acelerar la creación de código y proponer buenas prácticas, pero no sustituye la revisión crítica. Es importante verificar que las recomendaciones sean correctas, adaptarlas al contexto del problema y conservar el control sobre las decisiones técnicas. La IA funcionó como apoyo para pensar y construir, pero la responsabilidad final del desarrollo siguió siendo del estudiante.
