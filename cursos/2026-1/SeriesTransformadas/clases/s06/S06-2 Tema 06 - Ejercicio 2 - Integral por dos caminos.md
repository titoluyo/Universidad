---
title: "Ejercicio 2 - Integral de (conjugada de z) al cuadrado por dos caminos"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 6
orden: 2
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/integral-de-contorno
  - tema/integral-por-caminos
date: 2026-05-03
---

## Enunciado

Calcular la integral de contorno:

$$\int_{C} \overline{z}^{\,2}\,dz$$

desde el punto inicial $z_0 = i$ hasta el punto final $z_1 = 1 + 2i$, tomando como contorno $C$ la trayectoria formada por dos caminos rectos:

- **Camino 1:** desde $(0, 1)$ hasta $(1, 1)$ — varía $x \in [0, 1]$ con $y = 1$ fijo.
- **Camino 2:** desde $(1, 1)$ hasta $(1, 2)$ — varía $y \in [1, 2]$ con $x = 1$ fijo.

> [!info] Material original
> Video del docente + transcripción en [[T01-Ej2-Guion-integral-contorno.pdf|Guion del Ejercicio 2]].

## Referencia teorica

Ver [[S06-1 Tema 06 - Integral de contorno en funciones complejas|integral de contorno]]. En particular, si $f(z) = u + iv$ y $dz = dx + i\,dy$:

$$\int_{C} f(z)\,dz = \int_{C} (u + iv)(dx + i\,dy) = \int_{C}(u\,dx - v\,dy) + i\int_{C}(v\,dx + u\,dy)$$

## Paso 1: Identificar $u(x, y)$ y $v(x, y)$

Sea $z = x + iy$, su conjugada es $\overline{z} = x - iy$. Elevando al cuadrado:

$$\overline{z}^{\,2} = (x - iy)^2 = x^2 - 2ixy - y^2 = (x^2 - y^2) - i(2xy)$$

Es decir:

$$u(x, y) = x^2 - y^2, \qquad v(x, y) = -2xy$$

## Paso 2: Plantear la integral general

$$\int_{C} \overline{z}^{\,2}\,dz = \int_{C}\bigl[(x^2 - y^2) - i\,2xy\bigr](dx + i\,dy)$$

Distribuyendo:

$$= \int_{C}\bigl[(x^2 - y^2)\,dx + 2xy\,dy\bigr] + i\int_{C}\bigl[-2xy\,dx + (x^2 - y^2)\,dy\bigr]$$

## Paso 3: Camino 1 ($y = 1$, $dy = 0$, $x: 0 \to 1$)

Sustituyendo $y = 1$ y $dy = 0$:

$$I_1 = \int_{0}^{1}(x^2 - 1)\,dx + i\int_{0}^{1}(-2x)\,dx$$

Calculando cada parte:

$$\int_{0}^{1}(x^2 - 1)\,dx = \left[\frac{x^3}{3} - x\right]_0^1 = \frac{1}{3} - 1 = -\frac{2}{3}$$

$$\int_{0}^{1}(-2x)\,dx = -\left[x^2\right]_0^1 = -1$$

$$\boxed{I_1 = -\frac{2}{3} - i}$$

## Paso 4: Camino 2 ($x = 1$, $dx = 0$, $y: 1 \to 2$)

Sustituyendo $x = 1$ y $dx = 0$:

$$I_2 = \int_{1}^{2}(2 \cdot 1 \cdot y)\,dy + i\int_{1}^{2}(1 - y^2)\,dy$$

Calculando:

$$\int_{1}^{2} 2y\,dy = \left[y^2\right]_1^2 = 4 - 1 = 3$$

$$\int_{1}^{2}(1 - y^2)\,dy = \left[y - \frac{y^3}{3}\right]_1^2 = \left(2 - \frac{8}{3}\right) - \left(1 - \frac{1}{3}\right) = -\frac{2}{3} - \frac{2}{3} = -\frac{4}{3}$$

$$\boxed{I_2 = 3 - \frac{4}{3}\,i}$$

## Paso 5: Sumar las contribuciones

$$\int_{C} \overline{z}^{\,2}\,dz = I_1 + I_2 = \left(-\frac{2}{3} - i\right) + \left(3 - \frac{4}{3}\,i\right)$$

$$= \left(-\frac{2}{3} + 3\right) + \left(-1 - \frac{4}{3}\right)i = \frac{7}{3} - \frac{7}{3}\,i$$

> [!success] Resultado
> $$\boxed{\int_{C} \overline{z}^{\,2}\,dz = \frac{7}{3} - \frac{7}{3}\,i = \frac{7}{3}(1 - i)}$$
>
> El valor depende del **camino** porque $\overline{z}^{\,2}$ no es analítica (no satisface Cauchy-Riemann). Para funciones analíticas, el [[S06-3 Tema 06 - Teorema de Cauchy|Teorema de Cauchy]] garantiza que la integral en un contorno cerrado es 0 y, por extension, que la integral entre dos puntos es independiente del camino.
