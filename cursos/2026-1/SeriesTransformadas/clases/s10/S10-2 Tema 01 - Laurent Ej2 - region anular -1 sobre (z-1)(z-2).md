---
title: "Laurent Ej 2 — Expansión de $\\dfrac{-1}{(z-1)(z-2)}$ en el anillo $1<|z|<2$"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 10
orden: 2
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/series-de-laurent
  - tema/fracciones-parciales
  - tema/serie-geometrica
date: 2026-05-25
---

## Enunciado

Hallar la **serie de Laurent** de la función:

$$f(z) = \frac{-1}{(z-1)(z-2)}$$

Fuente: [[Ej2-Laurent-Guion.pdf|Guion del video — Expansión de la serie de Laurent, Ejercicio 2]].

## Paso 1: puntos de singularidad y regiones

El denominador se anula en:

$$z - 1 = 0 \;\Rightarrow\; z = 1, \qquad z - 2 = 0 \;\Rightarrow\; z = 2$$

Trabajando centrados en $z_0 = 0$, los círculos $|z|=1$ y $|z|=2$ dividen el plano en tres regiones:

| Región | Condición | Tipo |
| ------ | --------- | ---- |
| A | $\|z\| < 1$ | disco interior |
| **B** | $1 < \|z\| < 2$ | **anillo (Laurent)** |
| C | $\|z\| > 2$ | exterior |

Como la serie de Laurent vive en el **anillo**, se trabaja en la **región B**: $1 < |z| < 2$.

## Paso 2: fracciones parciales

$$\frac{-1}{(z-1)(z-2)} = \frac{A}{z-1} + \frac{B}{z-2} \;\Rightarrow\; -1 = A(z-2) + B(z-1)$$

- $z = 1$: $-1 = A(-1) \Rightarrow A = 1$
- $z = 2$: $-1 = B(1) \Rightarrow B = -1$

$$f(z) = \frac{1}{z-1} - \frac{1}{z-2}$$

## Paso 3: expandir cada término según el anillo $1<|z|<2$

**Término $\dfrac{1}{z-1}$** (aquí $|z|>1$, así que $\left|\frac1z\right|<1$ — se factoriza $z$):

$$\frac{1}{z-1} = \frac{1}{z}\cdot\frac{1}{1 - \frac{1}{z}} = \frac{1}{z}\sum_{n=0}^{\infty}\frac{1}{z^n} = \frac{1}{z} + \frac{1}{z^2} + \frac{1}{z^3} + \cdots$$

Esta es la **parte principal** (potencias negativas).

**Término $-\dfrac{1}{z-2}$** (aquí $|z|<2$, así que $\left|\frac z2\right|<1$ — se factoriza la constante):

$$-\frac{1}{z-2} = \frac{1}{2-z} = \frac{1}{2}\cdot\frac{1}{1 - \frac{z}{2}} = \frac{1}{2}\sum_{n=0}^{\infty}\left(\frac{z}{2}\right)^n = \frac{1}{2} + \frac{z}{4} + \frac{z^2}{8} + \frac{z^3}{16} + \cdots$$

Esta es la **parte analítica** (potencias positivas).

## Resultado

> [!success] Serie de Laurent en $1 < |z| < 2$
> $$f(z) = \cdots + \frac{1}{z^3} + \frac{1}{z^2} + \frac{1}{z} \;+\; \frac{1}{2} + \frac{z}{4} + \frac{z^2}{8} + \frac{z^3}{16} + \cdots$$
> $$f(z) = \sum_{n=1}^{\infty}\frac{1}{z^n} \;+\; \sum_{n=0}^{\infty}\frac{z^n}{2^{n+1}}$$

> [!note] La doble naturaleza de Laurent
> La serie tiene **potencias negativas** (de $\frac{1}{z-1}$, válida para $|z|>1$) **y positivas** (de $\frac{1}{z-2}$, válida para $|z|<2$). La intersección de ambas condiciones es exactamente el anillo $1<|z|<2$. En las otras regiones (A o C) las expansiones cambian.

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — §66–68 (series de Laurent).
- Material del curso: [[Ej2-Laurent-Guion.pdf|Guion del video — Serie de Laurent Ej 2]].
