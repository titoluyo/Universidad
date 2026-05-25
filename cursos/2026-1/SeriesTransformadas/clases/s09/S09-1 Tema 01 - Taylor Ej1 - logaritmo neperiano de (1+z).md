---
title: "Taylor Ej 1 — Expansión de $\\ln(1+z)$ alrededor de $z_0 = 0$"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 9
orden: 1
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/series-de-taylor
  - tema/series-de-maclaurin
  - tema/logaritmo-complejo
date: 2026-05-18
---

## Enunciado

Sea la función $f(z) = \ln(1 + z)$, con la convención $f(0) = 0$.

Desarrollar $f(z)$ en una **serie de Taylor alrededor de $z_0 = 0$** (es decir, una serie de Maclaurin).

Fuente: [[T01-Ej1-Guion.pdf|Guion del video — Ejercicio 1]].

## Paso 1: derivadas sucesivas de $f(z) = \ln(1+z)$

| $n$ | $f^{(n)}(z)$                  | $f^{(n)}(0)$ |
| --- | ----------------------------- | ------------ |
| $0$ | $\ln(1+z)$                    | $\ln 1 = 0$  |
| $1$ | $\dfrac{1}{1+z}$              | $1$          |
| $2$ | $\dfrac{-1}{(1+z)^2}$         | $-1$         |
| $3$ | $\dfrac{2}{(1+z)^3}$          | $2 = 2!$     |
| $4$ | $\dfrac{-6}{(1+z)^4}$         | $-6 = -3!$   |
| $5$ | $\dfrac{24}{(1+z)^5}$         | $24 = 4!$    |

> [!tip] Patrón observado
> $f^{(n)}(0) = (-1)^{n-1}\,(n - 1)!$ para $n \geq 1$.

## Paso 2: construir los coeficientes Taylor $a_n = f^{(n)}(0)/n!$

| $n$ | $a_n = f^{(n)}(0)/n!$            | Simplificación |
| --- | -------------------------------- | -------------- |
| $0$ | $0/0! = 0$                       | $0$            |
| $1$ | $1/1!$                           | $1$            |
| $2$ | $-1/2!$                          | $-1/2$         |
| $3$ | $2!/3! = 2!/(3 \cdot 2!)$        | $1/3$          |
| $4$ | $-3!/4! = -3!/(4 \cdot 3!)$      | $-1/4$         |
| $5$ | $4!/5! = 4!/(5 \cdot 4!)$        | $1/5$          |

Aquí se usó que $n! = n \cdot (n-1)!$ para cancelar el factorial del numerador con el del denominador.

> [!success] Patrón compacto
> $$a_n = \frac{(-1)^{n-1}}{n}, \quad n \geq 1$$

## Paso 3: escribir la serie completa

Como $z_0 = 0$, los términos son $a_n\,z^n$:

$$f(z) = 0 + z - \frac{z^2}{2} + \frac{z^3}{3} - \frac{z^4}{4} + \frac{z^5}{5} - \cdots$$

## Paso 4: forma compacta

> [!success] Resultado
> $$\boxed{\;\ln(1 + z) = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}\,z^n}{n}\;}$$

## Verificación del signo con valores pequeños de $n$

- $n = 1$: $(-1)^{0} = 1$ → $+z$ ✓
- $n = 2$: $(-1)^{1} = -1$ → $-z^2/2$ ✓
- $n = 3$: $(-1)^{2} = 1$ → $+z^3/3$ ✓
- $n = 4$: $(-1)^{3} = -1$ → $-z^4/4$ ✓

## Radio de convergencia

Aplicando el criterio del cociente con $a_n = (-1)^{n-1}/n$:

$$\lambda = \lim_{n \to \infty}\left|\frac{a_{n+1}}{a_n}\right| = \lim_{n \to \infty}\frac{n}{n+1} = 1$$

$$R = \frac{1}{\lambda} = 1$$

> [!note] Singularidad en $z = -1$
> La función $\ln(1 + z)$ tiene una **singularidad logarítmica en $z = -1$** (el argumento del logaritmo se anula). La distancia desde $z_0 = 0$ hasta $z = -1$ es $1$, lo cual coincide con el radio de convergencia. La serie converge en el disco abierto $|z| < 1$.

## Conclusión

Este ejercicio ilustra el procedimiento clásico de Taylor:

1. Calcular varias derivadas sucesivas y evaluarlas en $z_0$.
2. Identificar el patrón de signos y factoriales.
3. Construir los coeficientes $a_n = f^{(n)}(z_0)/n!$ y simplificar.
4. Reconocer una **forma compacta** con sumatoria.

Esta serie es **fundamental** porque aparece como bloque base de otras expansiones (ver [[S09-2 Tema 01 - Taylor Ej2 - logaritmo de (1+z)/(1-z)|Ej 2]] que la reutiliza).

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — §63 (Serie de Maclaurin).
- Spiegel, M. R. (2009). *Variable compleja* (Schaum). McGraw-Hill — Cap. 6, ej. resueltos.
- Material del curso: [[T01-Ej1-Guion.pdf|Guion del video Serie de Taylor Ej 1]].
