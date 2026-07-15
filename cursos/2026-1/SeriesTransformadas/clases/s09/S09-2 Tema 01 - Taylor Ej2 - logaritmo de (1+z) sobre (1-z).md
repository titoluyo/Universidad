---
title: "Taylor Ej 2 — Expansión de $\\ln\\!\\left(\\dfrac{1+z}{1-z}\\right)$ alrededor de $z_0 = 0$"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 9
orden: 2
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/series-de-taylor
  - tema/series-de-maclaurin
  - tema/logaritmo-complejo
  - tema/arctangente-hiperbolica
date: 2026-05-18
---

## Enunciado

Desarrollar $f(z) = \ln\!\left(\dfrac{1 + z}{1 - z}\right)$ en una **serie de Taylor alrededor de $z_0 = 0$**.

Fuente: [[T01-Ej2-Guion.pdf|Guion del video — Ejercicio 2]].

## Estrategia: aplicar propiedad de logaritmos

> [!info] Propiedad
> $$\ln\!\left(\frac{a}{b}\right) = \ln a - \ln b$$

Aplicada al integrando:

$$\ln\!\left(\frac{1 + z}{1 - z}\right) = \ln(1 + z) \;-\; \ln(1 - z)$$

Esto reduce el problema a obtener las series de Taylor de **dos** logaritmos por separado.

## Paso 1: serie de $\ln(1 + z)$

Ya calculada en [[S09-1 Tema 01 - Taylor Ej1 - logaritmo neperiano de (1+z)|Ejercicio 1]]:

$$\ln(1 + z) = z - \frac{z^2}{2} + \frac{z^3}{3} - \frac{z^4}{4} + \frac{z^5}{5} - \cdots = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}\,z^n}{n}$$

## Paso 2: serie de $\ln(1 - z)$

Aplicando el mismo procedimiento (derivadas sucesivas en $z_0 = 0$):

| $n$ | $f^{(n)}(z)$              | $f^{(n)}(0)$        |
| --- | ------------------------- | ------------------- |
| $0$ | $\ln(1-z)$                | $0$                 |
| $1$ | $\dfrac{-1}{1-z}$         | $-1$                |
| $2$ | $\dfrac{-1}{(1-z)^2}$     | $-1$                |
| $3$ | $\dfrac{-2}{(1-z)^3}$     | $-2 = -2!$          |
| $4$ | $\dfrac{-6}{(1-z)^4}$     | $-6 = -3!$          |

> [!note] Atajo
> Como $\ln(1-z) = \ln(1 + (-z))$, basta sustituir $z \mapsto -z$ en la serie de $\ln(1+z)$:
> $$\ln(1 - z) = \sum_{n=1}^\infty \frac{(-1)^{n-1}(-z)^n}{n} = \sum_{n=1}^\infty \frac{(-1)^{n-1}(-1)^n z^n}{n} = -\sum_{n=1}^\infty \frac{z^n}{n}$$
> Es decir, todos los signos son negativos:

$$\ln(1 - z) = -z - \frac{z^2}{2} - \frac{z^3}{3} - \frac{z^4}{4} - \frac{z^5}{5} - \cdots = -\sum_{n=1}^{\infty} \frac{z^n}{n}$$

## Paso 3: restar las series término a término

$$\ln(1+z) - \ln(1-z) = \sum_{n=1}^{\infty}\frac{(-1)^{n-1}\,z^n}{n} \;+\; \sum_{n=1}^{\infty}\frac{z^n}{n}$$

Sumando término a término:

| $n$ | $\ln(1+z)$ | $-\ln(1-z)$ | Resta total |
| --- | ---------- | ----------- | ----------- |
| $1$ | $+z$       | $+z$        | $+2z$       |
| $2$ | $-z^2/2$   | $+z^2/2$    | $0$         |
| $3$ | $+z^3/3$   | $+z^3/3$    | $+2z^3/3$   |
| $4$ | $-z^4/4$   | $+z^4/4$    | $0$         |
| $5$ | $+z^5/5$   | $+z^5/5$    | $+2z^5/5$   |

> [!success] Observación
> Los términos con **$n$ par se cancelan**, y los términos con **$n$ impar se duplican**.

Por lo tanto:

$$\ln\!\left(\frac{1 + z}{1 - z}\right) = 2\left(z + \frac{z^3}{3} + \frac{z^5}{5} + \frac{z^7}{7} + \cdots\right)$$

## Paso 4: forma compacta

Reindexando los exponentes impares como $2n - 1$ con $n = 1, 2, 3, \ldots$:

> [!success] Resultado
> $$\boxed{\;\ln\!\left(\frac{1 + z}{1 - z}\right) = 2\sum_{n=1}^{\infty} \frac{z^{2n-1}}{2n - 1}\;}$$

## Identificación: arcotangente hiperbólica

Esta serie está relacionada con la **arcotangente hiperbólica**:

$$\text{arctanh}(z) = \frac{1}{2}\ln\!\left(\frac{1 + z}{1 - z}\right) = \sum_{n=1}^{\infty}\frac{z^{2n-1}}{2n - 1}, \quad |z| < 1$$

Por lo tanto, lo que se desarrolló es $2\,\text{arctanh}(z)$.

## Radio de convergencia

Ambas series originales convergen en $|z| < 1$ (singularidades en $z = -1$ y $z = +1$), por lo que la diferencia converge en la **intersección**: $|z| < 1$. Es consistente con el hecho de que $\dfrac{1+z}{1-z}$ tiene polo en $z = 1$ y cero en $z = -1$, ambos a distancia 1 del centro $z_0 = 0$.

$$R = 1$$

## Conclusión

Este ejercicio muestra dos técnicas potentes:

1. **Reducir un problema complejo a partes conocidas** usando propiedades algebraicas/logarítmicas, en vez de calcular derivadas desde cero.
2. **Sumar/restar series término a término**, lo cual es válido dentro del intervalo de convergencia común.

El procedimiento de **sustitución $z \mapsto g(z)$** en una serie conocida es una herramienta general que ahorra cálculos de derivadas — útil para Taylor de $\sin(z^2)$, $e^{-z^2}$, etc.

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — §63, §64.
- Apostol, T. M. (1980). *Análisis matemático* (2.ª ed.). Reverté — §9.5 (Manipulación de series de Taylor).
- Material del curso: [[T01-Ej2-Guion.pdf|Guion del video Serie de Taylor Ej 2]].
