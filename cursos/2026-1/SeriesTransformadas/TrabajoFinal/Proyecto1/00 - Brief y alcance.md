---
title: "Proyecto 1 (Fourier) — Brief y alcance"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
date: 2026-06-29
---

# Proyecto 1 — Serie de Fourier · Brief y alcance

> [!info] Estado
> Carpeta de trabajo para el **Proyecto 1** del Trabajo Final. **Aún no desarrollar**: este documento solo fija la línea de lo que debe hacerse. El desarrollo lo hará un agente dedicado.

## Caso a resolver (definido por la consigna)

La empresa *Electronics S.A.* necesita una **señal senoidal rectificada de media onda**. Se usa la teoría de **Series de Fourier** para analizarla y un programa en **Octave** para aproximarla.

- **Entregable técnico central:** hallar **analíticamente** la serie de Fourier de la señal senoidal rectificada de media onda, **por teoría y por simulación**, y comparar mostrando el error.

## Línea de trabajo (qué debe producir el agente)

1. **Definir la señal** $f(t)$: seno rectificado de media onda, amplitud $A$, periodo $T$, $\omega_0 = 2\pi/T$. Graficarla.
2. **Solución teórica (analítica):**
   - Calcular $a_0$, $a_n$, $b_n$ aprovechando simetrías.
   - Resolver las integrales paso a paso.
   - Escribir la serie de Fourier resultante.
3. **Simulación en Octave:**
   - Script que reconstruye la señal con $N$ términos.
   - Graficar la aproximación vs. la señal original para varios $N$.
4. **Comparación y error:** error cuadrático con $N$ términos (teórico vs. simulado). Reutilizar el método de [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|S12-3]].
5. **Discusión y conclusiones** acordes a los objetivos.
6. **Documento PDF** (10–20 pág, Arial 12, interlineado 1.5, APA) con la estructura de [[05 - Documento final (esqueleto)|esqueleto]].
7. **Video** ≤ 5 min (ver [[06 - Guion del video|guion]]).

## Rúbrica que debe cubrir (20 pts)

| Criterio | pts | Dónde se cubre |
| -------- | --- | -------------- |
| Introducción | 2 | doc § Introducción |
| Marco teórico | 2 | def. Series de Fourier + propiedades + simulador + ecuaciones |
| Dominio de simulación | 3 | script Octave + resultados |
| Dominio teórico | 3 | cálculo analítico de la serie |
| Discusión y conclusiones | 4 | comparación con **error** + conclusiones |
| Referencias APA | 3 | citas en texto e imágenes |
| Video | 3 | título, objetivos, metodología, análisis, conclusiones |

## Material de soporte

- Teoría: [[S11-2 Tema 02 - Series de Fourier|Series de Fourier]], [[S12-0 Tema 01 - Analisis de las series de Fourier|media onda y medio rango]].
- Error: [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|error cuadrático del seno rectificado]].
- Octave: [[S16-5 Tema 02 - Programa Octave|cómo usar Octave]].
- Consigna y rúbrica completas: [[S18-98 PROY Indicaciones]] · [[S16-98 APF Indicaciones|versión APF]].

## Notas / decisiones abiertas

- Definir valores concretos de $A$ y $T$.
- Modalidad individual o grupal (ver [[Trabajo Final - SyT MOC|hub]]).
