---
title: "Conclusiones semana 08 — Series de potencias y criterio del cociente"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 8
orden: 5
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/series-de-potencias
  - tema/criterio-del-cociente
date: 2026-05-17
---

## Cierre

La semana 8 abre la **Unidad 2 — Series complejas** del curso. Se introducen las **series de potencias** en variable compleja y se aprende a determinar su **radio de convergencia** mediante el **criterio del cociente** (test de D'Alembert).

Fuente: [[Cierre-sem08-Guion.pdf|Guion del video — Conclusiones]].

## Resumen de la semana

> [!summary] Serie de potencias
> $$y = \sum_{n=0}^{\infty} a_n\,(z - z_0)^n$$
> Con coeficientes $a_n \in \mathbb{C}$ y centro $z_0$.

> [!summary] Convergencia absoluta
> Si $\sum |u_n|$ converge → $\sum u_n$ converge (la implicación inversa no se cumple en general).

> [!summary] Criterio del cociente
> $$L = \lim_{n \to \infty}\left|\frac{u_{n+1}}{u_n}\right|$$
> - $L < 1$ → converge absolutamente
> - $L > 1$ → diverge
> - $L = 1$ → no decide

> [!summary] Radio de convergencia
> Para $\sum a_n (z - z_0)^n$, separando $|z - z_0|$ del límite:
> $$\lambda = \lim_{n \to \infty}\left|\frac{a_{n+1}}{a_n}\right| \qquad \Longrightarrow \qquad R = \frac{1}{\lambda}$$
> Converge en el disco abierto $|z - z_0| < R$.

## Casos típicos vistos

| Tipo de coeficiente | Comportamiento de $\lambda$ | $R$ | Ejemplo |
| ------------------- | --------------------------- | --- | ------- |
| Polinomial en $n$ — $a_n = n(n+1)$ | $\to 1$ | $1$ | [[S08-4 Tema 01 - Convergencia Ej4 - polinomial n(n+1)\|Ej 4]] |
| Factorial creciente — $1/n!$, $1/(2n-1)!$ | $\to 0$ | $\infty$ | [[S08-2 Tema 01 - Convergencia Ej2 - serie del seno\|Ej 2]], [[S08-3 Tema 01 - Convergencia Ej3 - exponencial alternante\|Ej 3]] |
| Exponencial — $1/c^n$ | $\to 1/c$ | $c$ | [[S08-1 Tema 01 - Convergencia Ej1 - serie geometrica con (z+2)\|Ej 1]] (con factor extra $1/4^n$ y $1/(n+1)^3$) |

## Notas de la semana

- [[S08-0 Tema 01 - Series de potencias en complejos|Series de potencias en complejos — teoría]]
- [[S08-1 Tema 01 - Convergencia Ej1 - serie geometrica con (z+2)|Ej 1 — $R = 4$, centro $z_0 = -2$]]
- [[S08-2 Tema 01 - Convergencia Ej2 - serie del seno|Ej 2 — $R = \infty$, serie del $\sin z$]]
- [[S08-3 Tema 01 - Convergencia Ej3 - exponencial alternante|Ej 3 — $R = \infty$, tipo exponencial $1 - e^{-z^3}$]]
- [[S08-4 Tema 01 - Convergencia Ej4 - polinomial n(n+1)|Ej 4 — $R = 1$, polinomial $n(n+1)$]]

## Evaluación de la semana

> [!info] Evaluación no calificada (cuestionario)
> Cuestionario sobre series de potencias. Plazo: lunes **11 mayo** → domingo **17 mayo 2026** 23:59. Ver [[S08-99 Evaluacion sem 08|metadatos]].

## Próxima semana

La semana 9 desarrolla **series de Taylor en números complejos** — caso particular en que los coeficientes $a_n = \dfrac{f^{(n)}(z_0)}{n!}$ se derivan de una función analítica, conectando series de potencias con el cálculo diferencial complejo visto en la Unidad 1.
