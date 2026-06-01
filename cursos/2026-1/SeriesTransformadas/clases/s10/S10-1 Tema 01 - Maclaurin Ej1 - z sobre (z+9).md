---
title: "Maclaurin Ej 1 — Expansión de $\\dfrac{z}{z+9}$ alrededor de $z_0 = 0$"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 10
orden: 1
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/series-de-maclaurin
  - tema/serie-geometrica
date: 2026-05-25
---

## Enunciado

Hallar la **serie de Maclaurin** de la función:

$$f(z) = \frac{z}{z + 9}$$

## Paso 1: recordar la serie de Maclaurin

La serie de Maclaurin es una serie de Taylor con $z_0 = 0$:

$$f(z) = f(0) + \frac{f'(0)}{1!}z + \frac{f''(0)}{2!}z^2 + \cdots + \frac{f^{(n)}(0)}{n!}z^n$$

## Paso 2: derivadas sucesivas evaluadas en $z_0 = 0$

| $n$ | $f^{(n)}(z)$                         | $f^{(n)}(0)$                          |
| --- | ------------------------------------ | ------------------------------------- |
| $0$ | $\dfrac{z}{z+9}$                     | $0$                                   |
| $1$ | $\dfrac{9}{(z+9)^2}$                 | $\dfrac{9}{9^2} = \dfrac{1}{9}$       |
| $2$ | $\dfrac{-18}{(z+9)^3}$               | $\dfrac{-18}{9^3} = -\dfrac{2}{9^2}$  |
| $3$ | $\dfrac{18\cdot 3}{(z+9)^4}$         | $\dfrac{2\cdot 3}{9^3}$               |
| $4$ | $\dfrac{18\cdot 3\cdot 4}{(z+9)^5}$  | $\dfrac{2\cdot 3\cdot 4}{9^4}$        |

La primera derivada usa la regla del cociente: $f'(z) = \dfrac{1\cdot(z+9) - z\cdot 1}{(z+9)^2} = \dfrac{9}{(z+9)^2}$.

## Paso 3: construir los coeficientes y sustituir

$$f(z) = 0 + \frac{1}{9}z - \frac{1}{9^2}z^2 + \frac{1}{9^3}z^3 - \frac{1}{9^4}z^4 + \cdots$$

donde cada coeficiente es $a_n = \dfrac{f^{(n)}(0)}{n!}$ y los factoriales se cancelan con el numerador (p. ej. $a_3 = \dfrac{2\cdot 3/9^3}{3!} = \dfrac{6/9^3}{6} = \dfrac{1}{9^3}$).

> [!success] Resultado
> $$\boxed{\;f(z) = \frac{z}{z+9} = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}\,z^n}{9^n}\;}$$

## Verificación por serie geométrica

Es más rápido reescribir $f$ como serie geométrica (ver [[S10-0 Tema 01 - Series de Maclaurin y Laurent#1. Serie de Maclaurin|teoría]]):

$$\frac{z}{z+9} = \frac{z}{9}\cdot\frac{1}{1 + \frac{z}{9}} = \frac{z}{9}\sum_{k=0}^{\infty}\left(-\frac{z}{9}\right)^k = \sum_{k=0}^{\infty}(-1)^k\frac{z^{k+1}}{9^{k+1}}$$

Con $n = k+1$ se recupera $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}z^n}{9^n}$. ✓

## Radio de convergencia

La serie geométrica exige $\left|\frac{z}{9}\right| < 1$, es decir $|z| < 9$. La singularidad de $f$ está en $z = -9$, a distancia $9$ del origen — coincide con $R_0 = 9$.

> [!note] Erratas del material original
> El guion del portal escribía la cuarta derivada con denominador $(z+1)^5$ (debía ser $(z+9)^5$) y usaba $\times$ como signo de multiplicación. Aquí se corrigieron; el resultado final no cambia.

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — §62 (serie de Maclaurin).
- Material del curso: ejercicio interactivo de la semana 10 (contenido personalizado del portal).
