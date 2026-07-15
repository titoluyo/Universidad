---
title: "Proyecto 1 (Fourier) — Prompt para generar el plan de trabajo"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
date: 2026-06-29
---

# Prompt — Generar plan de trabajo (Proyecto 1)

> [!info] Uso
> Copiar el bloque de abajo y dárselo a un agente dedicado a este proyecto. El agente **solo debe producir el plan detallado**, no desarrollar la solución. El plan se guarda en esta misma carpeta como `02 - Plan de trabajo.md`.

```text
ROL Y CONTEXTO
Eres el responsable del "Proyecto 1" del Trabajo Final del curso Series y Transformadas
(UTP, ciclo 2026-1, modalidad Virtual 24/7, docente J. F. Torres). Tu tarea AHORA es
producir un PLAN DETALLADO DE TRABAJO. No desarrolles todavía la solución matemática ni
la simulación: solo planifica.

Antes de planificar, LEE estos archivos del vault:
- "cursos/2026-1/SeriesTransformadas/Trabajo Final/Proyecto 1/00 - Brief y alcance.md" (tu alcance)
- "cursos/2026-1/SeriesTransformadas/clases/s18/S18-98 PROY Indicaciones.md" (consigna + rúbrica)
- "cursos/2026-1/SeriesTransformadas/clases/s16/S16-98 APF Indicaciones.md" (avance)
- Notas de soporte: S11-2 (Series de Fourier), S12-0 (media onda), S12-3 (error cuadrático),
  S16-5 (Programa Octave).

CASO A RESOLVER
Serie de Fourier de una señal senoidal rectificada de MEDIA ONDA: hallarla analíticamente
Y aproximarla en GNU Octave, comparando teoría vs. simulación mostrando el error.

REQUISITOS FIJOS (no negociables)
- Documento PDF de 10 a 20 páginas, fuente Arial 12, interlineado 1.5.
- Tablas y figuras numeradas, con breve definición y listadas en el índice.
- Citas APA 7 en el texto Y en las imágenes; lista de referencias APA.
- Video explicativo ≤ 5 min (Drive/YouTube): título, objetivos, metodología, análisis de
  resultados, conclusiones; todos los integrantes deben aparecer.
- Fechas: APF (avance, 15%) vence lun 13 jul 2026 23:59; PROY (final, 30%) abre lun 20 jul,
  vence mar 21 jul 2026 23:59, con 1 solo intento.
- Rúbrica (20 pts): Introducción (2), Marco teórico (2), Dominio de simulación (3),
  Dominio teórico (3), Discusión y conclusiones con el error (4), Referencias APA (3),
  Video (3).

QUÉ DEBE CONTENER EL PLAN (entregable)
1. Objetivo general y objetivos específicos del proyecto.
2. Definición concreta del caso: proponer valores de amplitud A y periodo T de la señal,
   y justificar la elección.
3. Desglose Etapas → Tareas → Subtareas, cubriendo: desarrollo analítico (a0, an, bn,
   integrales, serie resultante), programa en Octave (reconstrucción con N términos y
   gráficas), cálculo del error, redacción del documento, y producción del video.
4. Cronograma con FECHAS concretas encajado en el calendario real (aprovechar sem 16 para
   el APF y sem 17-18 para el PROY). Indicar qué queda listo para el APF y qué se añade
   para el PROY.
5. Entregables por etapa y "definición de terminado" de cada uno.
6. Mapa Tarea → criterio de rúbrica → puntos, mostrando que se cubren los 20 pts.
7. Recursos y materiales (notas del vault, bibliografía a buscar, Octave).
8. Riesgos y mitigaciones (p. ej. definir mal el periodo, error numérico en Octave).
9. Checklist final de entrega (formato, APA, páginas, video subido y enlazado).

FORMATO DE SALIDA
- Escribe el plan como una nota Obsidian en:
  "cursos/2026-1/SeriesTransformadas/Trabajo Final/Proyecto 1/02 - Plan de trabajo.md"
- Usa frontmatter YAML (tipo: proyecto), encabezados ##, tablas y callouts.
- Usa wikilinks a las notas de soporte. Todo en español.
- No inventes bibliografía: lista fuentes candidatas a verificar, no citas falsas.
```
