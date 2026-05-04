---
title: "Cauchy Ejercicio 1 - Comprobar Teorema de Cauchy en contorno triangular"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 6
orden: 4
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/teorema-de-cauchy
  - tema/integral-por-caminos
date: 2026-05-03
---

## Enunciado

Comprobar el **Teorema de Cauchy** para:

$$\oint_{C} z\,dz = 0$$

donde $C$ es el contorno triangular formado por:

- **Camino 1:** $(0, 0) \to (1, 0)$ — sobre el eje $x$
- **Camino 2:** $(1, 0) \to (1, 1)$ — sobre la vertical $x = 1$
- **Camino 3:** $(1, 1) \to (0, 0)$ — diagonal de regreso al origen

> [!info] Material original
> Video del docente + transcripción en [[T02-Ej1-Guion-Cauchy.pdf|Guion del Ejercicio 1]].

## Referencia teorica

Ver [[S06-3 Tema 06 - Teorema de Cauchy|Teorema de Cauchy]]. Como $f(z) = z$ es analítica en todo $\mathbb{C}$ (entera), debe cumplirse $\oint_C z\,dz = 0$. Aquí lo verificamos por cálculo directo en cada camino.

Sea $z = x + iy$ y $dz = dx + i\,dy$.

## Camino 1: $y = 0$, $dy = 0$, $x: 0 \to 1$

Aquí $z = x$ y $dz = dx$:

$$I_1 = \int_{0}^{1} x\,dx = \left[\frac{x^2}{2}\right]_0^1 = \frac{1}{2}$$

## Camino 2: $x = 1$, $dx = 0$, $y: 0 \to 1$

Aquí $z = 1 + iy$ y $dz = i\,dy$:

$$I_2 = \int_{0}^{1}(1 + iy)(i\,dy) = i\int_{0}^{1} dy + i^2 \int_{0}^{1} y\,dy = i - \frac{1}{2}$$

## Camino 3: $y = x$, $x: 1 \to 0$ (diagonal de regreso)

Como $y = x$, entonces $dy = dx$, y $z = x + ix = x(1 + i)$, $dz = (1 + i)\,dx$:

$$I_3 = \int_{1}^{0} x(1+i) \cdot (1+i)\,dx = (1+i)^2 \int_{1}^{0} x\,dx = (1+i)^2 \left[\frac{x^2}{2}\right]_1^0$$

Calculando $(1+i)^2 = 1 + 2i + i^2 = 2i$:

$$I_3 = 2i \cdot \left(0 - \frac{1}{2}\right) = -i$$

## Suma de los tres caminos

$$\oint_{C} z\,dz = I_1 + I_2 + I_3 = \frac{1}{2} + \left(i - \frac{1}{2}\right) + (-i)$$

$$= \left(\frac{1}{2} - \frac{1}{2}\right) + (i - i) = 0 + 0 = 0 \checkmark$$

> [!success] Resultado
> $$\boxed{\oint_{C} z\,dz = 0}$$
>
> Se cumple el [[S06-3 Tema 06 - Teorema de Cauchy|Teorema de Cauchy]]: como $f(z) = z$ es analítica en todo $\mathbb{C}$, su integral sobre cualquier contorno cerrado simple es cero.
