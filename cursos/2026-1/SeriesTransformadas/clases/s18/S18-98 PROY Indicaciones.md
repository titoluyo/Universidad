---
title: "Proyecto Final (PROY) — consigna y rúbrica"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 18
orden: 98
tipo: evaluacion
subtipo: pc
tags:
  - curso/series-transformadas
  - tipo/evaluacion
  - tema/proyecto-final
  - tema/octave
date: 2026-07-20
---

> [!info] Evaluación flexible
> Puede realizarse de forma **individual o grupal**. Entrega por la plataforma virtual (Canvas). Vale el **30%** de la nota final. **1 intento permitido.**

> [!abstract] Relación con el Avance (APF)
> El PROY es la **versión completa** del proyecto cuyo avance se entregó en la semana 16. Mismo enunciado y mismos dos proyectos del [[S16-98 APF Indicaciones|APF]]; aquí se añaden **discusión del error simulado vs. teórico**, **conclusiones** y un **video explicativo (≤ 5 min)**.

## Logro a evaluar

Al finalizar la unidad, el estudiante **resuelve ejercicios de aplicación mediante las transformadas**.

## Contexto

En la empresa **Electronics S.A.** se presentan dos situaciones. El estudiante **escoge UNO** de los dos proyectos para desarrollar y luego lo explica mediante un **video**. La empresa optó por estas dos técnicas por ser eficientes y económicas.

### Proyecto 1 — Serie de Fourier
La señal de onda deseada para una aplicación específica debe ser una **señal senoidal rectificada cuadrática**. Se usa la teoría de **Series de Fourier** para el análisis y un programa en **Octave** para aproximar la señal requerida.

### Proyecto 2 — Transformada de Laplace
Se necesita determinar el **voltaje de un capacitor** para un circuito específico, usando un programa de **simulación** y la teoría de las **Transformadas de Laplace**.

> [!important] El cruce Proyecto 1/2 es INTENCIONAL (aclarado por el docente, 16 jul 2026)
> En las "Indicaciones específicas" del PROY, bajo *"Si eligieron el proyecto 1"* se pide $V_o(t)$ con **Laplace** y bajo *"Si eligieron el proyecto 2"* la **serie de Fourier**. No es una errata: el diseño es que **todos trabajen ambos proyectos** — quien desarrolló el Proyecto 1 (Fourier) en el [[S16-98 APF Indicaciones|APF]] desarrolla el Proyecto 2 (Laplace) en el Proyecto Final, y viceversa.
> En nuestro caso: APF = Fourier → **PROY = Laplace**, entregado desde [[00 - Decision y alcance v2|Proyecto2-v2]].

## Contenido exigido del documento

| Proyecto 1 (Fourier) | Proyecto 2 (Laplace) |
| -------------------- | -------------------- |
| Introducción | Introducción |
| Marco teórico | Marco teórico |
| Hallar **analíticamente** la serie de Fourier de la señal senoidal rectificada de **media onda** — por simulación y por teoría | Hallar **analíticamente** $V_o$ y graficar $V_o(t)$ del circuito aplicando la **transformada de Laplace** — por simulación y por teoría |
| Referencias bibliográficas | Referencias bibliográficas |

**Independientemente del proyecto elegido**, se debe incluir además:
- **Comparación** de los datos obtenidos de forma simulada y teórica, **mostrando el error**.
- **Conclusiones** acordes a los objetivos, indicando los datos obtenidos.
- **Video explicativo** (ver abajo).

- **Simulador:** GNU **Octave** o **LTSPICE**.

## Video explicativo

- Duración **máxima 5 minutos**.
- Subir a **Drive o YouTube** (no adjuntar pesado) y enlazarlo.
- Debe especificar: **Título · Objetivos · Metodología · Análisis de resultados · Conclusiones**.
- **Todos los integrantes** deben aparecer explicando su parte del proyecto.

## Indicaciones de formato

- Citas bibliográficas en texto y en imágenes (**formato APA**).
- Fuente **Arial 12**, interlineado **1.5**.
- Tablas y figuras **enumeradas** con breve definición y listadas en el índice.
- Entrega del documento en **PDF** por la plataforma.
- Extensión: **mínimo 10 y máximo 20 páginas**.
- Tipos de archivo admitidos en la entrega: PDF, PPT, Word, Excel, JPG, mp3, mp4, zip o rar. Tamaño total máximo **500 MB**.

## Rúbrica de evaluación (20 pts)

Código de rúbrica: `I18N-PROY-2026M`. Cada criterio se califica: **Estándar esperado · En proceso 2 · En proceso 1 · Inicial · No cumple**.

| # | Criterio | Estándar esperado (pts máx) | Qué evalúa |
| - | -------- | --------------------------- | ---------- |
| 1 | **Introducción** | 2 | Redactado en prosa · antecedentes generales y específicos · objetivo principal |
| 2 | **Marco teórico** | 2 | Definición/conceptos (Fourier o Laplace) · propiedades usadas · define el simulador · plantea las ecuaciones aplicadas |
| 3 | **Dominio de simulación** | 3 | Muestra el desarrollo del programa/simulación · presenta resultados · analiza resultados del simulador |
| 4 | **Dominio teórico** | 3 | Muestra la solución teórica (Laplace en el circuito / Fourier de la función) · presenta resultados · analiza resultados teóricos |
| 5 | **Discusión y conclusiones** | 4 | Discusión simulado vs. teórico **incluyendo el error** · conclusión de resultados simulados · conclusión de resultados teóricos · conclusión de la discusión con su error |
| 6 | **Referencias bibliográficas** | 3 | Cita en texto · cita de imágenes · formato APA |
| 7 | **Dominio del tema (video)** | 3 | Video con: título · objetivos · metodología · análisis de resultados · conclusiones · ≤ 5 min |

Escala por criterio (puntajes intermedios): para los de 2 pts → 2 / 1.5 / 1 / 0.5 / 0; para los de 3 pts → 3 / 2 / 1 / 0.5 / 0; para el de 4 pts → 4 / 3 / 2 / 1 / 0.

> [!danger] Integridad académica
> Todo acto de copiar, intentar copiar o dejar copiar está normado en el Reglamento de Estudios y el Reglamento de Disciplina del Estudiante.

## Material de soporte

- Proyecto 1 (Fourier): [[S11-2 Tema 02 - Series de Fourier|Series de Fourier]], [[S12-0 Tema 01 - Analisis de las series de Fourier|medio rango y media onda]], [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|error cuadrático del seno rectificado]].
- Proyecto 2 (Laplace): [[S14-1 Tema 01 - Transformadas de Laplace|Transformada de Laplace]], [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|circuito RLC]].
- Simulación: [[S16-5 Tema 02 - Programa Octave|Programa Octave]].
- Avance previo: [[S16-98 APF Indicaciones|APF — consigna y rúbrica]].
- Metadatos y fechas: [[S18-99 PROY sem 18]].
- Espacio de trabajo: [[Trabajo Final - SyT MOC|Trabajo Final — hub de etapas]].
