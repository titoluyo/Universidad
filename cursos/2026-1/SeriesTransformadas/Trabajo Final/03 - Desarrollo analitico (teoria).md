---
title: "Etapa 3 — Desarrollo analítico (teoría)"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
date: 2026-06-29
---

# Etapa 3 — Desarrollo analítico (teoría)

Resolución **a mano, paso a paso** del proyecto elegido. Cubre el criterio **Dominio teórico (3 pts)** de la rúbrica. Mantener cada paso justificado (la nota de clase enlazada respalda cada propiedad usada).

> [!info] Completar según la elección de [[00 - Brainstorming y eleccion]]

## Si Proyecto 1 — Serie de Fourier (seno rectificado de media onda)

Pasos esperados:
1. Definir la señal $f(t)$ y su periodo $T$ (media onda del seno rectificado).
2. Plantear los coeficientes: $a_0$, $a_n$, $b_n$ (aprovechar simetrías).
3. Resolver las integrales analíticamente.
4. Escribir la serie de Fourier resultante.
5. Evaluar la aproximación con $N$ términos y preparar el **error** vs. la simulación.

$$f(t) = \dots$$

- Donde:
  - $T$ = periodo de la señal
  - $\omega_0 = 2\pi/T$ = frecuencia fundamental

Respaldo: [[S11-2 Tema 02 - Series de Fourier|coeficientes de Fourier]], [[S12-0 Tema 01 - Analisis de las series de Fourier|media onda]], [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|error cuadrático del seno rectificado]].

## Si Proyecto 2 — Transformada de Laplace ($V_o(t)$ de un circuito)

Pasos esperados:
1. Dibujar el circuito y definir R, L, C y la fuente.
2. Plantear la ecuación del circuito en el dominio del tiempo.
3. Aplicar la **transformada de Laplace** (condiciones iniciales incluidas).
4. Despejar $V_o(s)$.
5. Antitransformar (fracciones parciales) → $V_o(t)$ y graficar.

$$V_o(s) = \dots \qquad\Rightarrow\qquad V_o(t) = \dots$$

Respaldo: [[S14-1 Tema 01 - Transformadas de Laplace|Transformada de Laplace]], [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|circuito RLC resuelto]].

## Resultados teóricos (para comparar con la simulación)

| Magnitud | Valor teórico |
| -------- | ------------- |
| _…_ | _…_ |
