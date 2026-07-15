---
title: "Tema 01 Ej 1 — Periodo de $f(t) = \\cos\\frac{t}{3} + \\cos\\frac{t}{4}$"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 11
orden: 1
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/senales-periodicas
date: 2026-06-01
---

## Enunciado

Encontrar el **periodo** de la función:

$$f(t) = \cos\frac{t}{3} + \cos\frac{t}{4}$$

Fuente: [[T01-Ej1-Guion-periodo.pdf|Guion del video — Señales periódicas]].

## Idea: aplicar la definición de periodicidad a cada término

Por definición, $f$ es periódica de periodo $T$ si $f(t + T) = f(t)$. Como $f$ es **suma de dos cosenos**, el periodo total $T$ debe ser **simultáneamente** un periodo de cada sumando. Se usa que el coseno se repite al agregar un múltiplo entero de $2\pi$:

$$\cos(\theta + 2\pi m) = \cos\theta, \qquad m \in \mathbb{Z}$$

## Paso 1: condición para $\cos\frac{t}{3}$

Exigir $\cos\dfrac{t+T}{3} = \cos\dfrac{t}{3}$ equivale a que el incremento del argumento sea un múltiplo de $2\pi$:

$$\frac{T}{3} = 2\pi m \quad\Longrightarrow\quad T = 6\pi m, \qquad m \in \mathbb{Z}^+$$

## Paso 2: condición para $\cos\frac{t}{4}$

Análogamente, con un entero $n$:

$$\frac{T}{4} = 2\pi n \quad\Longrightarrow\quad T = 8\pi n, \qquad n \in \mathbb{Z}^+$$

## Paso 3: igualar ambos periodos

El periodo debe ser **el mismo** para los dos términos:

$$6\pi m = 8\pi n$$

Cancelando $\pi$ y simplificando (mitades $3$ y $4$):

$$3m = 4n$$

## Paso 4: menores enteros que cumplen la relación

Para que $3m = 4n$ con $m, n$ enteros positivos mínimos:

$$m = 4, \qquad n = 3$$

> [!note] Por qué estos valores
> $3m = 4n$ obliga a que $m$ sea múltiplo de $4$ y $n$ múltiplo de $3$. Los **menores** positivos son $m=4$, $n=3$ (dan $3\cdot4 = 4\cdot3 = 12$). Valores mayores darían periodos múltiplos, no el **mínimo**.

## Paso 5: calcular el periodo y verificar

$$T = 6\pi m = 6\pi(4) = 24\pi$$

Comprobación con el otro término:

$$T = 8\pi n = 8\pi(3) = 24\pi \quad\checkmark$$

> [!success] Resultado
> $$\boxed{\;T = 24\pi\;}$$

## Conclusión

Para hallar el periodo de una **suma de armónicos** se calcula el periodo de cada término y se busca el **mínimo común** mediante la relación entera entre ellos ($3m = 4n$). El periodo total es el menor $T$ que es múltiplo entero simultáneo de ambos periodos individuales.

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
- Material del curso: [[T01-Ej1-Guion-periodo.pdf|Guion del video — Señales periódicas]].
