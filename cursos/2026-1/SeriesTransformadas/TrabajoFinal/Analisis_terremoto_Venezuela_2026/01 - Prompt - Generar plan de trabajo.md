---
title: "Terremoto Venezuela 2026 — Prompt para generar el plan de trabajo"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
  - tema/sismo
date: 2026-06-29
---

# Prompt — Generar plan de trabajo (Terremoto Venezuela 2026)

> [!info] Uso
> Copiar el bloque de abajo y dárselo a un agente dedicado a este proyecto. El agente **solo debe producir el plan detallado**, no desarrollar la solución. El plan se guarda en esta misma carpeta como `02 - Plan de trabajo.md`.

```text
ROL Y CONTEXTO
Eres el responsable de la variante temática "Análisis terremoto Venezuela 2026" del Trabajo
Final del curso Series y Transformadas (UTP, ciclo 2026-1, Virtual 24/7, docente
J. F. Torres). Tu tarea AHORA es producir un PLAN DETALLADO DE TRABAJO. No desarrolles
todavía la solución ni la simulación: solo planifica.

Antes de planificar, LEE estos archivos del vault:
- "cursos/2026-1/SeriesTransformadas/Trabajo Final/Analisis terremoto Venezuela 2026/00 - Brief y alcance.md"
- "cursos/2026-1/SeriesTransformadas/clases/s18/S18-98 PROY Indicaciones.md" (consigna + rúbrica)
- "cursos/2026-1/SeriesTransformadas/Trabajo Final/00 - Brainstorming y eleccion.md" (viabilidad)
- Notas de soporte: S14-1 (Transformada de Laplace), S14-3 y S14-4 (sistemas de 2º orden / RLC).

IDEA Y ENCAJE (leer con atención)
Es una ADAPTACIÓN del Proyecto 2 (Transformada de Laplace), NO un caso libre. Una estructura
(edificio) se modela como sistema masa-resorte-amortiguador de 2º orden, matemáticamente
idéntico a un circuito RLC. Con una entrada sísmica IDEALIZADA se resuelve la respuesta x(t)
analíticamente con Laplace, se simula y se compara el error. El terremoto de Venezuela
(24 jun 2026, doble evento ~7.1/7.2 y 7.5) aporta la motivación y los antecedentes.

DOS CONDICIONES CRÍTICAS (deben aparecer como supuestos/bloqueantes en el plan)
1. Requiere confirmación del profesor para sustituir el escenario "Electronics S.A. / voltaje
   de capacitor" por uno de respuesta estructural sísmica. Sin ese OK, este camino no es
   entregable: el plan debe incluir "obtener aprobación" como primer hito bloqueante y proponer
   un plan B (volver al Proyecto 2 estándar).
2. La excitación del suelo debe modelarse como una función simple (impulso, escalón o seno
   amortiguado), NO el acelerograma real crudo, para conservar la solución analítica que exige
   la rúbrica.

REQUISITOS FIJOS (no negociables)
- Documento PDF de 10 a 20 páginas, Arial 12, interlineado 1.5.
- Tablas y figuras numeradas, con breve definición y listadas en el índice.
- Citas APA 7 en el texto Y en las imágenes; lista de referencias APA.
- Los datos del sismo deben citarse de fuentes oficiales (USGS, FUNVISIS) y VERIFICARSE por
  búsqueda web externa: no inventar magnitudes, fecha ni ubicación.
- Video explicativo ≤ 5 min (Drive/YouTube): título, objetivos, metodología, análisis de
  resultados, conclusiones; todos los integrantes deben aparecer.
- Fechas: APF (avance, 15%) vence lun 13 jul 2026 23:59; PROY (final, 30%) abre lun 20 jul,
  vence mar 21 jul 2026 23:59, con 1 solo intento.
- Rúbrica (20 pts): Introducción (2), Marco teórico (2), Dominio de simulación (3),
  Dominio teórico (3), Discusión y conclusiones con el error (4), Referencias APA (3),
  Video (3).

QUÉ DEBE CONTENER EL PLAN (entregable)
1. Objetivo general y objetivos específicos.
2. Hito 0 BLOQUEANTE: obtener aprobación del profesor (con plan B si la respuesta es no).
3. Antecedentes del sismo: qué datos buscar y en qué fuentes oficiales (USGS, FUNVISIS).
4. Modelo físico: parámetros m, k, c; tabla de analogía RLC ↔ masa-resorte-amortiguador;
   elección y justificación de la entrada idealizada.
5. Desglose Etapas → Tareas → Subtareas: desarrollo analítico con Laplace (EDO de 2º orden,
   X(s), antitransformada, x(t)), simulación (Octave o RLC en LTSPICE), cálculo del error,
   redacción del documento, y producción del video.
6. Cronograma con FECHAS concretas encajado en el calendario real, considerando que el hito 0
   puede retrasar el arranque. Indicar qué queda listo para el APF y qué se añade para el PROY.
7. Entregables por etapa y "definición de terminado".
8. Mapa Tarea → criterio de rúbrica → puntos, mostrando que se cubren los 20 pts.
9. Recursos y materiales (notas del vault, fuentes sísmicas, simulador).
10. Riesgos y mitigaciones (rechazo del profesor, datos sísmicos no verificables, entrada mal
    idealizada, desajuste teórico vs. simulado).
11. Checklist final de entrega.

FORMATO DE SALIDA
- Escribe el plan como una nota Obsidian en:
  "cursos/2026-1/SeriesTransformadas/Trabajo Final/Analisis terremoto Venezuela 2026/02 - Plan de trabajo.md"
- Usa frontmatter YAML (tipo: proyecto), encabezados ##, tablas y callouts.
- Usa wikilinks a las notas de soporte. Todo en español.
- No inventes bibliografía ni datos sísmicos: lista fuentes a verificar, no citas falsas.
```
