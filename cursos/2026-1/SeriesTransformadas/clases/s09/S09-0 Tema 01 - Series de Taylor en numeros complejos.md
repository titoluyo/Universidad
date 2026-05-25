---
title: "Series de Taylor en números complejos — definición y procedimiento"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 9
orden: 0
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/series-de-taylor
  - tema/series-de-maclaurin
date: 2026-05-18
---

## Idea central

Una **serie de Taylor** representa una función analítica como una **suma infinita de potencias** centradas en un punto $z_0$, donde los coeficientes se obtienen a partir de las **derivadas sucesivas** de la función evaluadas en ese punto.

Es la generalización al plano complejo del teorema de Taylor para funciones reales, y se enmarca dentro del estudio de [[S08-0 Tema 01 - Series de potencias en complejos|series de potencias]] (semana 8).

## Definición

> [!summary] Serie de Taylor de $f(z)$ alrededor de $z_0$
> Si $f(z)$ es analítica en un disco $|z - z_0| < R$, entonces:
> $$f(z) = f(z_0) + \frac{f'(z_0)}{1!}(z - z_0) + \frac{f''(z_0)}{2!}(z - z_0)^2 + \cdots$$
> $$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(z_0)}{n!}(z - z_0)^n$$

Donde:
- $f^{(n)}(z_0)$ es la $n$-ésima derivada de $f$ evaluada en $z_0$.
- $z_0$ es el **centro** de la expansión.
- $(z - z_0)^n$ es la potencia $n$-ésima del desplazamiento desde $z_0$.

### Caso particular: $z_0 = 0$ (serie de Maclaurin)

$$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}\,z^n$$

## Procedimiento operativo

1. **Identificar la función** $f(z)$ y el **centro** $z_0$ de la expansión.
2. **Calcular las derivadas sucesivas** $f(z), f'(z), f''(z), \ldots, f^{(n)}(z)$.
3. **Evaluar cada derivada en $z_0$**: $f(z_0), f'(z_0), f''(z_0), \ldots$
4. **Construir los coeficientes Taylor**: $a_n = \dfrac{f^{(n)}(z_0)}{n!}$.
5. **Escribir la serie**: $\sum_{n=0}^\infty a_n (z - z_0)^n$.
6. **Identificar el patrón** (si existe) y expresar en forma compacta con sumatoria.

## Conexión con series de potencias

Una serie de Taylor es un **caso particular de serie de potencias**: aquella cuyos coeficientes son $a_n = \dfrac{f^{(n)}(z_0)}{n!}$. Por lo tanto, todo lo aprendido la semana 8 sobre [[S08-0 Tema 01 - Series de potencias en complejos#Criterio del cociente (test de D'Alembert)|criterio del cociente]] y [[S08-0 Tema 01 - Series de potencias en complejos#Radio de convergencia|radio de convergencia]] aplica.

> [!info] Teorema de Taylor (existencia)
> Si $f$ es analítica en un disco $|z - z_0| < R$, su serie de Taylor centrada en $z_0$ **converge a $f(z)$** dentro de ese disco. El radio $R$ es la distancia desde $z_0$ a la **singularidad más cercana** de $f$.

## Series de Maclaurin notables

| Función | Serie de Maclaurin | Radio $R$ |
| ------- | ------------------ | --------- |
| $e^z$ | $\sum_{n=0}^\infty \dfrac{z^n}{n!}$ | $\infty$ |
| $\sin z$ | $\sum_{n=1}^\infty \dfrac{(-1)^{n-1}\,z^{2n-1}}{(2n-1)!}$ | $\infty$ |
| $\cos z$ | $\sum_{n=0}^\infty \dfrac{(-1)^n\,z^{2n}}{(2n)!}$ | $\infty$ |
| $\dfrac{1}{1-z}$ | $\sum_{n=0}^\infty z^n$ | $1$ |
| $\ln(1+z)$ | $\sum_{n=1}^\infty \dfrac{(-1)^{n-1}\,z^n}{n}$ | $1$ |
| $\ln\!\left(\dfrac{1+z}{1-z}\right)$ | $2\sum_{n=1}^\infty \dfrac{z^{2n-1}}{2n-1}$ | $1$ |

Las tres primeras tienen radio infinito porque son funciones enteras; las tres últimas tienen $R=1$ porque $z = 1$ (o $z = -1$) son singularidades.

## Ejercicios resueltos en la semana

| # | Función | Centro $z_0$ | Resultado |
| - | ------- | ------------ | --------- |
| [[S09-1 Tema 01 - Taylor Ej1 - logaritmo neperiano de (1+z)\|Ej 1]] | $\ln(1 + z)$ | $0$ | $\sum_{n=1}^\infty \dfrac{(-1)^{n-1}\,z^n}{n}$ |
| [[S09-2 Tema 01 - Taylor Ej2 - logaritmo de (1+z)/(1-z)\|Ej 2]] | $\ln\!\left(\dfrac{1+z}{1-z}\right)$ | $0$ | $2\sum_{n=1}^\infty \dfrac{z^{2n-1}}{2n-1}$ |
| [[S09-3 Tema 01 - Taylor Ej3 - sen(z) alrededor de pi cuartos\|Ej 3]] | $\sin z$ | $\pi/4$ | Patrón cíclico con $\sqrt{2}/2$ |

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — Capítulo 5 (Series de Taylor y Laurent).
- Spiegel, M. R. (2009). *Variable compleja* (Schaum). McGraw-Hill — Capítulo 6.
- Apostol, T. M. (1980). *Análisis matemático* (2.ª ed.). Reverté — §9.5 (Series de Taylor).
