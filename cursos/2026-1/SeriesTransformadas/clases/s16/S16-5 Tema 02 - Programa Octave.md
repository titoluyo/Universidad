---
title: "Tema 02 — Programa Octave (instalación y uso)"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 16
orden: 5
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/octave
  - tema/simulacion
date: 2026-07-06
---

## ¿Qué es Octave?

**GNU Octave** es un software de cálculo numérico (una "calculadora avanzada") para matemáticas y ciencias: resuelve ecuaciones, grafica datos y realiza análisis numérico. Es de código abierto y compatible en gran medida con el lenguaje de MATLAB. En este curso se usa para la **simulación** del proyecto final (ver [[S16-98 APF Indicaciones|APF]]).

> [!info] Material en video
> Los dos contenidos de este tema son **videos tutoriales** (con guion en PDF descargable):
> - **Cómo descargar el programa Octave** → [[T02-Octave-Descargar-Guion.pdf|Guion — descarga e instalación]].
> - **Cómo se usa el programa Octave** (funciones básicas) → [[T02-Octave-Usar-Guion.pdf|Guion — uso básico]].

## Descarga e instalación

- Descargar desde el sitio oficial **[octave.org](https://octave.org/download)** (versión para Windows).
- Ejecutar el instalador y seguir los pasos estándar.

## Uso básico (orientado al proyecto)

Octave permite definir variables, vectores y matrices, evaluar funciones, y **graficar** señales —útil para aproximar una serie de Fourier o simular la respuesta de un circuito. Funciones de uso frecuente en el proyecto:

- Definir vectores de tiempo: `t = 0:0.01:10;`
- Funciones elementales: `sin`, `cos`, `exp`, `abs`.
- Graficar: `plot(t, y)`, `xlabel`, `ylabel`, `title`, `grid on`.
- Sumatorias para aproximar series de Fourier mediante bucles `for`.

> [!tip] Alternativa
> Para el **Proyecto 2** (circuito con transformada de Laplace) también se admite el simulador **LTSPICE** (ver consigna del [[S16-98 APF Indicaciones|APF]]).

## Aplicación

El manejo de Octave se evalúa indirectamente en el **Avance de Proyecto Final**: se exige mostrar el **desarrollo del programa (simulación)**, presentar resultados y analizarlos. Ver criterios en [[S16-98 APF Indicaciones|la rúbrica del APF]].
