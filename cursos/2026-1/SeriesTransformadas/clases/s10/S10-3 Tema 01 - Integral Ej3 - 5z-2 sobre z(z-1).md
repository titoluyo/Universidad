---
title: "Integral Ej 3 — $\\oint \\dfrac{5z-2}{z(z-1)}\\,dz$ mediante serie de Laurent"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 10
orden: 3
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/series-de-laurent
  - tema/integral-de-contorno
  - tema/residuo
date: 2026-05-25
---

## Enunciado

Calcular la integral de contorno:

$$\oint_{C}\frac{5z-2}{z(z-1)}\,dz, \qquad C:\ |z| = 1$$

Fuente: [[Ej3-Integral-Laurent-Guion.pdf|Guion del video — Resolución de integrales mediante series de Laurent]].

## Paso 1: singularidades

$$z = 0 \qquad\text{y}\qquad z - 1 = 0 \;\Rightarrow\; z = 1$$

Ambos puntos son interiores a la curva. Según la teoría de integración compleja (ver [[S06-6 Tema 06 - Teorema de extension de Cauchy|teorema de extensión de Cauchy]]), solo las singularidades **dentro** del contorno contribuyen; las de afuera dan integral nula. Aquí se expande la función en serie de Laurent alrededor de **cada** singularidad y se aísla el coeficiente de la potencia $-1$.

> [!note] Idea clave
> $\displaystyle\oint_C (z - z_0)^k\,dz = 0$ para todo entero $k \neq -1$, y $\displaystyle\oint_C \frac{dz}{z - z_0} = 2\pi i$. Por eso, al integrar la serie de Laurent **solo sobrevive el término** $(z-z_0)^{-1}$.

## Paso 2: contribución de $z_0 = 0$ (región $0<|z|<1$)

Se factoriza $z$ y se fuerza la serie geométrica $\dfrac{1}{1-z} = 1 + z + z^2 + \cdots$ (válida para $|z|<1$):

$$\frac{5z-2}{z(z-1)} = \frac{5z-2}{z}\left(\frac{1}{z-1}\right) = -\frac{5z-2}{z}\left(\frac{1}{1-z}\right)$$

$$= -\frac{5z-2}{z}\left(1 + z + z^2 + z^3 + \cdots\right) = -5\left(1 + z + z^2 + \cdots\right) + \frac{2}{z}\left(1 + z + z^2 + \cdots\right)$$

El único término con potencia $z^{-1}$ tiene coeficiente $\mathbf{2}$. Por tanto:

$$\oint_C \frac{5z-2}{z(z-1)}\,dz = 2\pi i\cdot 2 = 4\pi i \qquad\text{(contribución de } z=0\text{)}$$

## Paso 3: contribución de $z_0 = 1$ (región $0<|z-1|<1$)

Se reescribe pidiendo potencias de $(z-1)$. Usando $5z - 2 = 5(z-1) + 3$ y $\dfrac{1}{z} = \dfrac{1}{1+(z-1)}$:

$$\frac{5z-2}{z(z-1)} = \frac{5(z-1)+3}{z-1}\left(\frac{1}{1 + (z-1)}\right) = \frac{5(z-1)+3}{z-1}\Big(1 - (z-1) + (z-1)^2 - \cdots\Big)$$

$$= 5\Big(1 - (z-1) + \cdots\Big) - \frac{3}{z-1}\Big(1 - (z-1) + (z-1)^2 - \cdots\Big)$$

El único término con potencia $(z-1)^{-1}$ tiene coeficiente $\mathbf{3}$. Por tanto:

$$\oint_C \frac{5z-2}{z(z-1)}\,dz = 2\pi i\cdot 3 = 6\pi i \qquad\text{(contribución de } z=1\text{)}$$

## Paso 4: sumar contribuciones

> [!success] Resultado
> $$\boxed{\;\oint_{|z|=1}\frac{5z-2}{z(z-1)}\,dz = 4\pi i + 6\pi i = 10\pi i\;}$$

## Verificación por residuos

El coeficiente de $(z-z_0)^{-1}$ es exactamente el **residuo** de $f$ en $z_0$. Para polos simples, $\operatorname{Res}_{z_0} f = \lim_{z\to z_0}(z-z_0)f(z)$:

$$\operatorname{Res}_{0}f = \left.\frac{5z-2}{z-1}\right|_{z=0} = \frac{-2}{-1} = 2, \qquad \operatorname{Res}_{1}f = \left.\frac{5z-2}{z}\right|_{z=1} = \frac{3}{1} = 3$$

$$\oint_C f\,dz = 2\pi i\,(2 + 3) = 10\pi i \;\checkmark$$

> [!warning] Sutileza del contorno
> Estrictamente, $z=1$ está **sobre** la circunferencia $|z|=1$, no en su interior. El material del curso trata ambas singularidades como interiores (equivalente a tomar $C:\ |z| = 1{+}\varepsilon$). Se conserva el desarrollo del portal; el resultado $10\pi i$ corresponde a encerrar ambos polos.

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — §68–77 (Laurent y residuos).
- Material del curso: [[Ej3-Integral-Laurent-Guion.pdf|Guion del video — Integrales mediante series de Laurent]].
