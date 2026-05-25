---
title: "Convergencia Ej 3 — Serie tipo exponencial con $z^{3n}$, $R = \\infty$"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 8
orden: 3
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/criterio-del-cociente
date: 2026-05-11
---

## Enunciado

Calcular el **radio de convergencia** de la serie:

$$\sum_{n=1}^{\infty} \frac{(-1)^{n+1}\,z^{3n}}{n!}$$

## Paso 1: identificar $C_n$

$$C_n = \frac{(-1)^{n+1}\,z^{3n}}{n!}$$

## Paso 2: construir $C_{n+1}$

$$C_{n+1} = \frac{(-1)^{n+2}\,z^{3(n+1)}}{(n+1)!} = \frac{(-1)^{n+2}\,z^{3n+3}}{(n+1)!}$$

## Paso 3: aplicar el criterio del cociente

$$\lim_{n \to \infty}\left|\frac{C_{n+1}}{C_n}\right| = \lim_{n \to \infty}\left|\frac{(-1)^{n+2}\,z^{3n+3}}{(n+1)!} \cdot \frac{n!}{(-1)^{n+1}\,z^{3n}}\right|$$

## Paso 4: simplificar

- Signos: $\dfrac{(-1)^{n+2}}{(-1)^{n+1}} = -1$, y $|-1| = 1$.
- Potencias: $z^{3n+3 - 3n} = z^3$.
- Factoriales: $\dfrac{n!}{(n+1)!} = \dfrac{1}{n+1}$ — porque $(n+1)! = (n+1) \cdot n!$.

Sustituyendo y sacando $|z|^3$ fuera del límite:

$$|z|^3 \cdot \lim_{n \to \infty} \frac{1}{n+1}$$

## Paso 5: calcular el límite

$$\lim_{n \to \infty} \frac{1}{n+1} = 0$$

Por lo tanto:

$$\lambda = |z|^3 \cdot 0 = 0$$

## Paso 6: radio y región de convergencia

$$R = \frac{1}{\lambda} = \frac{1}{0} = \infty$$

> [!success] Resultado
> La serie converge absolutamente en **todo el plano complejo** $\mathbb{C}$.

## Identificación de la función

Esta serie está relacionada con la exponencial. Sustituyendo $w = -z^3$:

$$\sum_{n=1}^{\infty} \frac{(-1)^{n+1}\,z^{3n}}{n!} = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}\,(z^3)^n}{n!} = -\sum_{n=1}^{\infty} \frac{(-z^3)^{n}}{n!}$$

Recordando $e^w = \sum_{n=0}^\infty \frac{w^n}{n!} = 1 + \sum_{n=1}^\infty \frac{w^n}{n!}$:

$$\sum_{n=1}^{\infty} \frac{(-z^3)^{n}}{n!} = e^{-z^3} - 1$$

Por lo tanto:

$$\sum_{n=1}^{\infty} \frac{(-1)^{n+1}\,z^{3n}}{n!} = -(e^{-z^3} - 1) = 1 - e^{-z^3}$$

(Esta identificación no era requerida por el enunciado; la suma vista con el cambio de variable confirma que la serie representa una función entera y por tanto $R = \infty$.)

## Conclusión

Cualquier serie del tipo $\sum \dfrac{P(z)^n}{n!}$, con $P(z)$ polinomial en $z$, tiene radio de convergencia infinito en el sentido de que para cualquier $z$ fijo, el factor $|z|^k$ es constante mientras que $1/n! \to 0$ más rápido que cualquier polinomio en $n$. Estas series convergen siempre en todo el plano.

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — §59.
- Spiegel, M. R. (2009). *Variable compleja* (Schaum). McGraw-Hill — Cap. 6.
