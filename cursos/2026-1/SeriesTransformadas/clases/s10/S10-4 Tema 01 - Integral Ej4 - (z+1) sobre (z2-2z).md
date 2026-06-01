---
title: "Integral Ej 4 — $\\oint \\dfrac{z+1}{z^2-2z}\\,dz$ sobre $|z|=3$"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 10
orden: 4
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/series-de-laurent
  - tema/integral-de-contorno
  - tema/residuo
  - tema/fracciones-parciales
date: 2026-05-25
---

## Enunciado

Calcular la integral:

$$\oint_{C}\frac{z+1}{z^2 - 2z}\,dz, \qquad C:\ |z| = 3$$

> [!warning] Errata del material del portal
> El ejercicio interactivo de la semana 10 enuncia esta función $\dfrac{z+1}{z^2-2z}$, pero la "ayuda paso a paso" que muestra debajo desarrolla por error la función del [[S10-3 Tema 01 - Integral Ej3 - 5z-2 sobre z(z-1)|Ejercicio 3]] ($\frac{5z-2}{z(z-1)}$, resultado $10\pi i$). A continuación se resuelve el **enunciado correcto**.

## Paso 1: singularidades

$$z^2 - 2z = z(z - 2) = 0 \;\Rightarrow\; z = 0 \quad\text{y}\quad z = 2$$

Ambos están **dentro** de $|z| = 3$ (sus módulos $0$ y $2$ son menores que $3$).

![[ej4-regiones-singularidades.png]]

## Paso 2: fracciones parciales

$$\frac{z+1}{z(z-2)} = \frac{A}{z} + \frac{B}{z-2} \;\Rightarrow\; z + 1 = A(z-2) + Bz$$

- $z = 0$: $1 = A(-2) \Rightarrow A = -\dfrac{1}{2}$
- $z = 2$: $3 = B(2) \Rightarrow B = \dfrac{3}{2}$

$$f(z) = \frac{z+1}{z(z-2)} = \frac{-\tfrac{1}{2}}{z} + \frac{\tfrac{3}{2}}{z-2}$$

## Paso 3: coeficientes de potencia $-1$ (residuos) en cada singularidad

Como el contorno $|z|=3$ encierra a $z=0$ y $z=2$, se suma la contribución de ambos. El coeficiente de $(z-z_0)^{-1}$ en la serie de Laurent alrededor de cada polo es el **residuo** (ver [[S10-0 Tema 01 - Series de Maclaurin y Laurent#3. Conexión con integrales de contorno|teoría]]):

- En $z_0 = 0$: el término $\dfrac{-1/2}{z}$ ya está en forma de Laurent → $\operatorname{Res}_0 f = -\dfrac{1}{2}$.
- En $z_0 = 2$: el término $\dfrac{3/2}{z-2}$ ya está en forma de Laurent → $\operatorname{Res}_2 f = \dfrac{3}{2}$.

(Equivalentemente, $\operatorname{Res}_{z_0}f = \lim_{z\to z_0}(z-z_0)f(z)$: $\left.\tfrac{z+1}{z-2}\right|_{0} = -\tfrac12$ y $\left.\tfrac{z+1}{z}\right|_{2} = \tfrac32$.)

## Paso 4: aplicar la fórmula

$$\oint_C f(z)\,dz = 2\pi i\left(\operatorname{Res}_0 f + \operatorname{Res}_2 f\right) = 2\pi i\left(-\frac{1}{2} + \frac{3}{2}\right) = 2\pi i\,(1)$$

> [!success] Resultado
> $$\boxed{\;\oint_{|z|=3}\frac{z+1}{z^2-2z}\,dz = 2\pi i\;}$$

> [!note] Verificación con la fórmula integral de Cauchy
> Por la [[S07-0 Tema 01 - Relacion del teorema de Cauchy y una integral|fórmula integral de Cauchy]]: $\oint \frac{g(z)}{z-z_0}dz = 2\pi i\,g(z_0)$. Para $z=0$ con $g(z)=\frac{z+1}{z-2}$: $2\pi i\cdot(-\tfrac12) = -\pi i$. Para $z=2$ con $g(z)=\frac{z+1}{z}$: $2\pi i\cdot\tfrac32 = 3\pi i$. Suma $= 2\pi i$. ✓

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — §68–77 (Laurent y residuos).
- Material del curso: ejercicio interactivo de la semana 10 (contenido personalizado del portal).
