---
title: "Convergencia Ej 4 — Serie polinomial $n(n+1)\\,z^n$, $R = 1$"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 8
orden: 4
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/criterio-del-cociente
date: 2026-05-11
---

## Enunciado

Calcular el **radio de convergencia** de la serie:

$$\sum_{n=1}^{\infty} n(n + 1)\,z^n$$

## Paso 1: identificar $C_n$

$$C_n = n(n + 1)\,z^n$$

Coeficiente $a_n = n(n+1)$. Centro $z_0 = 0$.

## Paso 2: construir $C_{n+1}$

$$C_{n+1} = (n+1)(n + 2)\,z^{n+1}$$

## Paso 3: aplicar el criterio del cociente

$$\lim_{n \to \infty}\left|\frac{C_{n+1}}{C_n}\right| = \lim_{n \to \infty}\left|\frac{(n+1)(n+2)\,z^{n+1}}{n(n+1)\,z^n}\right|$$

## Paso 4: simplificar

- Potencias: $z^{n+1 - n} = z$.
- Coeficientes: $\dfrac{(n+1)(n+2)}{n(n+1)} = \dfrac{n+2}{n}$.

Sacando $|z|$ fuera del límite:

$$|z| \cdot \lim_{n \to \infty}\left|\frac{n+2}{n}\right| = |z| \cdot \lim_{n \to \infty}\left(1 + \frac{2}{n}\right) = |z| \cdot 1 = |z|$$

## Paso 5: calcular $\lambda$

Por la convención del docente (extraer $|z|$ del límite y definir $\lambda$ solo como el límite de los coeficientes):

$$\lambda = \lim_{n \to \infty}\left|\frac{n+2}{n}\right| = 1$$

## Paso 6: radio y región de convergencia

$$R = \frac{1}{\lambda} = \frac{1}{1} = 1$$

> [!success] Resultado
> La serie converge absolutamente en el **disco unitario abierto**:
> $$|z| < 1$$
> Y diverge para $|z| > 1$.

## Análisis adicional — qué pasa en la frontera $|z| = 1$

Para $|z| = 1$, el término $|n(n+1) z^n| = n(n+1) \cdot 1^n = n(n+1) \to \infty$, así que el término general **no tiende a cero** y la serie diverge en toda la circunferencia $|z| = 1$.

Por lo tanto, la región de convergencia es **estrictamente** el disco abierto $|z| < 1$.

## Identificación de la función

La serie $\sum_{n=1}^\infty n(n+1)\,z^n$ está relacionada con la **derivada segunda** de la serie geométrica. Partiendo de $\sum_{n=0}^\infty z^n = \dfrac{1}{1-z}$ para $|z| < 1$:

$$\sum_{n=0}^\infty z^n = \frac{1}{1 - z}, \quad |z| < 1$$

Derivando una vez:

$$\sum_{n=1}^\infty n\,z^{n-1} = \frac{1}{(1 - z)^2}$$

Multiplicando por $z$:

$$\sum_{n=1}^\infty n\,z^{n} = \frac{z}{(1 - z)^2}$$

Derivando esta otra vez y multiplicando por $z$, se obtiene una expresión similar para $\sum n(n+1) z^n$. El resultado final es:

$$\sum_{n=1}^\infty n(n+1)\,z^n = \frac{2z}{(1-z)^3}, \quad |z| < 1$$

Esto confirma que el radio de convergencia es $1$ (la función tiene un polo de orden 3 en $z = 1$).

## Conclusión

Cuando el coeficiente $a_n$ es **polinomial en $n$** (sin factoriales ni potencias exponenciales), el cociente $\dfrac{a_{n+1}}{a_n}$ tiende a 1 conforme $n \to \infty$, y por lo tanto $R = 1$. La serie converge solo dentro del disco unitario centrado en $z_0$.

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — §59, §63.
- Apostol, T. M. (1980). *Análisis matemático* (2.ª ed.). Reverté — §9.3.
