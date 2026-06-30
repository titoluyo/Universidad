---
title: "Proyecto 2 (Laplace) — Brief y alcance"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
date: 2026-06-29
---

# Proyecto 2 — Transformada de Laplace · Brief y alcance

> [!info] Estado
> Carpeta de trabajo para el **Proyecto 2** del Trabajo Final. **Aún no desarrollar**: este documento solo fija la línea de lo que debe hacerse. El desarrollo lo hará un agente dedicado.

## Caso a resolver (definido por la consigna)

La empresa *Electronics S.A.* necesita determinar el **voltaje de un capacitor** $V_o(t)$ en un circuito específico, usando un **simulador** y la teoría de la **Transformada de Laplace**.

- **Entregable técnico central:** hallar **analíticamente** $V_o$ y graficar $V_o(t)$ del circuito aplicando la transformada de Laplace, **por teoría y por simulación**, y comparar mostrando el error.

## Línea de trabajo (qué debe producir el agente)

1. **Definir el circuito:** topología y valores de R, L, C y la fuente (escalón, sinusoidal, etc.). Dibujarlo.
2. **Planteamiento:** ecuación del circuito en el dominio del tiempo (con condiciones iniciales).
3. **Solución teórica (analítica):**
   - Aplicar la transformada de Laplace.
   - Despejar $V_o(s)$.
   - Antitransformar (fracciones parciales) → $V_o(t)$.
   - Graficar $V_o(t)$.
4. **Simulación:** **LTSPICE** (o Octave) del mismo circuito; obtener $V_o(t)$ simulado.
5. **Comparación y error:** teórico vs. simulado punto a punto, mostrando el error.
6. **Discusión y conclusiones** acordes a los objetivos.
7. **Documento PDF** (10–20 pág, Arial 12, interlineado 1.5, APA) con la estructura de [[05 - Documento final (esqueleto)|esqueleto]].
8. **Video** ≤ 5 min (ver [[06 - Guion del video|guion]]).

## Rúbrica que debe cubrir (20 pts)

| Criterio | pts | Dónde se cubre |
| -------- | --- | -------------- |
| Introducción | 2 | doc § Introducción |
| Marco teórico | 2 | def. Transformada de Laplace + propiedades + simulador + ecuaciones |
| Dominio de simulación | 3 | modelo LTSPICE/Octave + resultados |
| Dominio teórico | 3 | desarrollo analítico de $V_o(t)$ |
| Discusión y conclusiones | 4 | comparación con **error** + conclusiones |
| Referencias APA | 3 | citas en texto e imágenes |
| Video | 3 | título, objetivos, metodología, análisis, conclusiones |

## Material de soporte

- Teoría: [[S14-1 Tema 01 - Transformadas de Laplace|Transformada de Laplace]].
- Circuitos resueltos: [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|RLC carga y corriente]], [[S14-4 Tema 01 - Ejercicio 3 - Circuito RLC II|RLC II]].
- Consigna y rúbrica completas: [[S18-98 PROY Indicaciones]] · [[S16-98 APF Indicaciones|versión APF]].

## Notas / decisiones abiertas

- Definir el circuito y los valores concretos de R, L, C y la fuente.
- ¿LTSPICE u Octave para la simulación? (LTSPICE requiere instalación).
- Modalidad individual o grupal (ver [[Trabajo Final - SyT MOC|hub]]).
