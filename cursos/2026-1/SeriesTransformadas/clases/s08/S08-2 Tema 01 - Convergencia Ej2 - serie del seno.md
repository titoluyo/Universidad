---
title: "Convergencia Ej 2 — Serie del $\\sin z$, $R = \\infty$"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 8
orden: 2
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/criterio-del-cociente
  - tema/serie-del-seno
date: 2026-05-11
---

## Enunciado

Hallar la **región de convergencia** de la serie:

$$\sum_{n=1}^{\infty} \frac{(-1)^{n-1}\,z^{2n-1}}{(2n - 1)!}$$

Fuente: [[T01-Ej2-Guion.pdf|Guion del video — Ejercicio 2]].

> [!note] Esta es la serie de Maclaurin del seno
> $$\sin z = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}\,z^{2n-1}}{(2n - 1)!} = z - \frac{z^3}{3!} + \frac{z^5}{5!} - \frac{z^7}{7!} + \cdots$$
> Sabemos *a priori* que $\sin z$ es **entera** (analítica en todo $\mathbb{C}$), por lo que su serie de potencias debe converger en todo el plano: $R = \infty$. Verifiquemos con el criterio del cociente.

## Paso 1: identificar $C_n$

$$C_n = \frac{(-1)^{n-1}\,z^{2n-1}}{(2n - 1)!}$$

## Paso 2: construir $C_{n+1}$

$$C_{n+1} = \frac{(-1)^{n}\,z^{2n+1}}{(2n + 1)!}$$

## Paso 3: aplicar el criterio del cociente

$$\lim_{n \to \infty}\left|\frac{C_{n+1}}{C_n}\right| = \lim_{n \to \infty}\left|\frac{(-1)^{n}\,z^{2n+1}}{(2n + 1)!} \cdot \frac{(2n - 1)!}{(-1)^{n-1}\,z^{2n-1}}\right|$$

## Paso 4: simplificar

- Signos: $\dfrac{(-1)^n}{(-1)^{n-1}} = -1$, y $|-1| = 1$.
- Potencias: $z^{2n+1 - (2n-1)} = z^{2}$.
- Factoriales: $\dfrac{(2n - 1)!}{(2n + 1)!} = \dfrac{1}{(2n)(2n + 1)}$ — al expandir $(2n+1)! = (2n+1)(2n)(2n-1)!$.

Sustituyendo:

$$\lim_{n \to \infty}\left|\frac{z^2}{(2n)(2n + 1)}\right| = |z|^2 \cdot \lim_{n \to \infty} \frac{1}{(2n)(2n+1)}$$

## Paso 5: calcular el límite

$$\lim_{n \to \infty} \frac{1}{(2n)(2n+1)} = \frac{1}{\infty} = 0$$

Por lo tanto:

$$\lambda = |z|^2 \cdot 0 = 0$$

## Paso 6: radio y región de convergencia

$$R = \frac{1}{\lambda} = \frac{1}{0} = \infty$$

> [!success] Resultado
> La serie converge absolutamente en **todo el plano complejo** $\mathbb{C}$, para cualquier valor de $z$. Esto confirma que $\sin z$ es una **función entera**.

## Identificación de la función

La serie corresponde exactamente a la serie de Maclaurin de $\sin z$:

$$\sin z = z - \frac{z^3}{3!} + \frac{z^5}{5!} - \frac{z^7}{7!} + \cdots = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}\,z^{2n-1}}{(2n-1)!}$$

(Esta serie fue desarrollada para variable real por Newton/Taylor y se extiende al plano complejo por analiticidad — la definición compleja $\sin z = \frac{e^{iz} - e^{-iz}}{2i}$ visto en [[S05-1 Tema 05 - Funciones complejas elementales]] es equivalente.)

## Conclusión

Cuando el término general contiene un **factorial creciente** en el denominador (como $(2n-1)!$, $n!$, $(2n)!$), el cociente $C_{n+1}/C_n$ tiende a 0 conforme $n \to \infty$, y por lo tanto $R = \infty$. Esto explica por qué $\sin z$, $\cos z$ y $e^z$ — todas con factoriales en sus series — son enteras.

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — §61 (Serie de Maclaurin del seno).
- Material del curso: [[T01-Ej2-Guion.pdf|Guion del video Comprobando la convergencia Ej 2]].
