---
title: "Ejercicio 2 — Transformada Z inversa por integral de inversión compleja"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 17
orden: 3
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/transformada-z-inversa
  - tema/residuos
date: 2026-07-13
---

## Enunciado

> [!question] Problema
> Evaluar la transformada Z inversa de $X(z) = \dfrac{1}{1 - a z^{-1}}$ utilizando la **integral de inversión compleja** (método de residuos).

Fuente: [[T01-InversionIntegral-Guion.pdf|Guion del video — Inversión de la transformada Z]].

## Desarrollo

### Paso 1 — Llevar a la forma con polo

Multiplicando numerador y denominador por $z$:

$$X(z) = \frac{1}{1 - a z^{-1}} = \frac{z}{z - a}$$

El **punto de singularidad** (polo) es $z_0 = a$.

### Paso 2 — Aplicar la integral de inversión

$$x(n) = \frac{1}{2\pi i}\oint_C X(z)\,z^{n-1}\,dz = \frac{1}{2\pi i}\oint_C \frac{z\cdot z^{n-1}}{z - a}\,dz = \frac{1}{2\pi i}\oint_C \frac{z^{n}}{z - a}\,dz$$

### Paso 3 — Residuo en $z_0 = a$ (para $n \ge 0$)

Por el teorema de Cauchy, con $f(z) = z^n$:

$$x(n) = f(a) = a^n \qquad (n \ge 0)$$

Para $n < 0$ aparece un polo adicional en $z = 0$; al evaluar los residuos, la contribución se **cancela** y $x(n) = 0$.

### Resultado

> [!success] Resultado
> $$\boxed{\;x(n) = a^n\,u(n)\;}$$

> [!note] Coherencia con la tabla
> Coincide con la transformada conocida $\mathcal{Z}\{a^n u(n)\} = \dfrac{z}{z-a}$ (ver [[S16-2 Tema 01 - Ejercicio 1 - Transformada Z de a elevado n por u(n)|S16 Ej 1]]). El método de residuos es la vía formal para invertir cuando no se reconoce la forma directamente.

## Conceptos aplicados

- [[S17-1 Tema 01 - Transformada Z Parte 2#3. Método de la integral de inversión (residuos)|Integral de inversión (residuos)]].

## Bibliografía

- Mitra, S. K. (2007). *Procesamiento de Señales Digitales* (3.ª ed.). McGraw-Hill. México.
