---
title: "Ejercicio 2 - Calcular todos los factores logaritmicos de z = 4i"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 5
orden: 3
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/funcion-logaritmica-compleja
  - tema/multivaluacion
date: 2026-04-26
---

## Enunciado

Calcular **todos los factores logaritmicos** de:

$$z = 4i$$

Es decir, evaluar $\ln z$ teniendo en cuenta que es una funcion multivaluada.

## Referencia teorica

Ver [[S05-1 Tema 05 - Funciones complejas elementales#2. Funcion logaritmica|funcion logaritmica compleja]]:

$$\ln z = \ln|z| + i(\arg(z) + 2k\pi), \quad k = 0, \pm 1, \pm 2, \ldots$$

Cada valor de $k$ produce un valor distinto de $\ln z$ (corresponde a una vuelta adicional en el plano).

## Paso 1: Ubicar $z = 4i$ en el plano

- Parte real: $a = 0$
- Parte imaginaria: $b = 4$

El punto se encuentra sobre el **eje imaginario positivo**, justo en el limite entre el 1er y 2do cuadrante.

## Paso 2: Calcular el argumento

Por estar sobre el eje imaginario positivo:

$$\theta = \arg(z) = \frac{\pi}{2}$$

## Paso 3: Calcular el modulo

$$|z| = \sqrt{0^2 + 4^2} = \sqrt{16} = 4$$

## Paso 4: Aplicar la definicion del logaritmo complejo

Sustituyendo en la formula:

$$\ln(4i) = \ln|4i| + i\left(\frac{\pi}{2} + 2k\pi\right)$$

$$\boxed{\ln(4i) = \ln 4 + i\left(\frac{\pi}{2} + 2k\pi\right), \quad k = 0, \pm 1, \pm 2, \ldots}$$

## Valores explicitos

| $k$ | $\ln(4i)$                              |
| --- | -------------------------------------- |
| $0$ | $\ln 4 + i\,\pi/2$ (rama principal)    |
| $1$ | $\ln 4 + i\,5\pi/2$                    |
| $-1$| $\ln 4 - i\,3\pi/2$                    |
| $2$ | $\ln 4 + i\,9\pi/2$                    |

> [!info] Periodicidad logaritmica
> Cada valor sucesivo se obtiene sumando $i\,2\pi$ al anterior. Esto refleja la periodicidad de $e^z$ con periodo $2\pi i$: si $w$ es solucion de $e^w = z$, entonces $w + 2\pi i k$ tambien lo es.
