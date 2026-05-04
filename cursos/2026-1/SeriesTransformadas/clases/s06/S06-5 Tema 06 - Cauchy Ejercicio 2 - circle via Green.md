---
title: "Cauchy Ejercicio 2 - Comprobar Cauchy con f(z)=z en |z|=1 via Green"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 6
orden: 5
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/teorema-de-cauchy
  - tema/teorema-de-green
date: 2026-05-03
---

## Enunciado

Comprobar el **Teorema de Cauchy** para el contorno $C: |z| = 1$ (en cualquier orientación) usando la formulación a partir del **Teorema de Green**, con la función:

$$f(z) = z$$

## Referencia teorica

Ver [[S06-3 Tema 06 - Teorema de Cauchy|Teorema de Cauchy]]. La derivación del teorema usa:

$$\int f(z)\,dz = \iint\left(-\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right)dx\,dy + i\iint\left(\frac{\partial u}{\partial x} - \frac{\partial v}{\partial y}\right)dx\,dy$$

donde $f(z) = u(x,y) + i\,v(x,y)$.

## Paso 1: Expresar $z$ y $dz$

$$z = x + iy, \qquad dz = dx + i\,dy$$

## Paso 2: Sustituir en $f(z) = z$

$$f(z) = (x + iy)$$

Por lo tanto:

$$u(x, y) = x, \qquad v(x, y) = y$$

## Paso 3: Calcular las derivadas parciales

$$\frac{\partial u}{\partial x} = 1, \qquad \frac{\partial u}{\partial y} = 0$$

$$\frac{\partial v}{\partial x} = 0, \qquad \frac{\partial v}{\partial y} = 1$$

> [!warning] Verificacion de Cauchy-Riemann
> $\dfrac{\partial u}{\partial x} = 1 = \dfrac{\partial v}{\partial y}$ ✓ y $\dfrac{\partial u}{\partial y} = 0 = -\dfrac{\partial v}{\partial x}$ ✓
>
> Se satisfacen las ecuaciones de Cauchy-Riemann, por lo que $f(z) = z$ es analítica (en todo $\mathbb{C}$).

## Paso 4: Sustituir en la integral via Green

Parte real del integrando:

$$-\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} = -0 - 0 = 0$$

Parte imaginaria del integrando:

$$\frac{\partial u}{\partial x} - \frac{\partial v}{\partial y} = 1 - 1 = 0$$

Como ambos integrandos son cero en toda la región interior al círculo $|z| \le 1$:

$$\int f(z)\,dz = \iint 0\,dx\,dy + i\iint 0\,dx\,dy = 0$$

> [!success] Resultado
> $$\boxed{\oint_{|z|=1} z\,dz = 0}$$
>
> El **Teorema de Cauchy** se cumple para esta función analítica (consistente con el [[S06-4 Tema 06 - Cauchy Ejercicio 1 - contorno triangular|Ejercicio 1]] que también dio cero por cálculo directo en un contorno triangular).

## Interpretacion

Este ejercicio muestra el **mecanismo interno** del Teorema de Cauchy: las ecuaciones de Cauchy-Riemann hacen que los integrandos del Teorema de Green se anulen punto a punto en toda la región. Es decir, **la analiticidad** de $f$ es lo que fuerza a la integral a ser cero, no algún cálculo casual.

Esto contrasta con [[S06-2 Tema 06 - Ejercicio 2 - Integral por dos caminos|el ejercicio de $\overline{z}^{\,2}$]]: ahí $f$ no es analítica (no satisface Cauchy-Riemann), por lo que la integral depende del camino y no es cero.
