---
title: "Convergencia Ej 1 — Serie centrada en $z_0 = -2$, $R = 4$"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 8
orden: 1
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/criterio-del-cociente
  - tema/radio-de-convergencia
date: 2026-05-11
---

## Enunciado

Hallar la **región de convergencia** de la serie:

$$\sum_{n=1}^{\infty} \frac{(z + 2)^{n-1}}{(n + 1)^3 \cdot 4^n}$$

Fuente: [[T01-Ej1-Guion.pdf|Guion del video — Ejercicio 1]].

## Paso 1: identificar el término general $C_n$

$$C_n = \frac{(z + 2)^{n-1}}{(n + 1)^3 \cdot 4^n}$$

> [!note] Centro de la serie
> La serie está centrada en $z_0 = -2$ (aparece el factor $(z - z_0)^{k} = (z + 2)^{k}$). El resultado dará un disco de convergencia centrado en $z = -2$.

## Paso 2: construir $C_{n+1}$

Sustituyendo $n \mapsto n + 1$:

$$C_{n+1} = \frac{(z + 2)^{n}}{(n + 2)^3 \cdot 4^{n+1}}$$

## Paso 3: aplicar el criterio del cociente

$$\lim_{n \to \infty}\left|\frac{C_{n+1}}{C_n}\right| = \lim_{n \to \infty}\left|\frac{(z + 2)^{n}}{(n + 2)^3 \cdot 4^{n+1}} \cdot \frac{(n + 1)^3 \cdot 4^n}{(z + 2)^{n-1}}\right|$$

Agrupando:

$$= \lim_{n \to \infty}\left|(z + 2)^{n - (n-1)} \cdot \frac{(n+1)^3}{(n+2)^3} \cdot 4^{n - (n+1)}\right|$$

## Paso 4: simplificar exponentes

- $(z + 2)^{n - (n-1)} = (z + 2)^1$
- $4^{n - (n+1)} = 4^{-1} = \dfrac{1}{4}$
- $\dfrac{(n+1)^3}{(n+2)^3} = \left(\dfrac{n+1}{n+2}\right)^3$

Sacando $|z + 2|$ fuera del límite (no depende de $n$):

$$\left|z + 2\right|\,\lim_{n \to \infty} \frac{1}{4}\,\left(\frac{n+1}{n+2}\right)^3$$

## Paso 5: calcular el límite

$$\lim_{n \to \infty}\left(\frac{n+1}{n+2}\right)^3 = \left(\lim_{n \to \infty}\frac{1 + 1/n}{1 + 2/n}\right)^3 = 1^3 = 1$$

Por lo tanto:

$$\lambda = \frac{1}{4} \cdot 1 = \frac{1}{4}$$

## Paso 6: radio y región de convergencia

$$R = \frac{1}{\lambda} = \frac{1}{1/4} = 4$$

> [!success] Resultado
> La serie converge absolutamente en el **disco abierto**
> $$|z + 2| < 4$$
> Es decir, dentro de la circunferencia de radio $4$ centrada en $z_0 = -2$.

## Verificación rápida

La condición $|z + 2|\,\lambda < 1$ se traduce en $|z + 2| < 1/\lambda = 4$, consistente con $R = 4$.

## Conclusión

El procedimiento estándar para hallar el radio de convergencia es: identificar $C_n$, formar el cociente con $C_{n+1}$, sacar el factor $|z - z_0|^k$ fuera del límite (porque no depende de $n$), calcular el límite de los coeficientes ($\lambda$) y reportar $R = 1/\lambda$.

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — §59 (Convergencia de series de potencias).
- Material del curso: [[T01-Ej1-Guion.pdf|Guion del video Comprobando la convergencia Ej 1]].
