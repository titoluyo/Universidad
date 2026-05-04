---
title: "Ejercicio 3 - Parte real de i^(ln(1+i))"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 5
orden: 4
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/funcion-logaritmica-compleja
  - tema/funcion-exponente-complejo
  - tema/funcion-potencia-compleja
date: 2026-04-26
---

## Enunciado

Calcular la **parte real** de:

$$i^{\ln(1+i)}$$

usando la rama principal del logaritmo.

## Referencia teorica

Combinamos [[S05-1 Tema 05 - Funciones complejas elementales#2. Funcion logaritmica|logaritmo complejo]] con [[S05-1 Tema 05 - Funciones complejas elementales#3. Funcion exponente complejo|exponente complejo]]:

$$\beta^z = e^{z\,\ln\beta}$$

## Paso 1: Calcular $\ln(1 + i)$ (rama principal)

Sea $w_1 = 1 + i$:

- Modulo: $|w_1| = \sqrt{1^2 + 1^2} = \sqrt{2}$
- Argumento: como $a = b = 1$ (1er cuadrante), $\theta = \pi/4$

$$\ln(1+i) = \ln\sqrt{2} + i\,\frac{\pi}{4} = \frac{1}{2}\ln 2 + i\,\frac{\pi}{4}$$

## Paso 2: Expresar $i$ en forma exponencial

Por inspeccion, $i$ esta sobre el eje imaginario positivo con $|i| = 1$ y $\arg(i) = \pi/2$:

$$i = e^{i\pi/2}$$

> [!note] Verificacion
> $e^{i\pi/2} = \cos(\pi/2) + i\,\text{sen}(\pi/2) = 0 + i \cdot 1 = i \checkmark$

Equivalentemente, $\ln i = i\,\pi/2$ (rama principal).

## Paso 3: Aplicar la definicion de exponente complejo

$$i^{\ln(1+i)} = e^{\ln(1+i)\,\cdot\,\ln i} = e^{\left(\tfrac{1}{2}\ln 2 + i\,\tfrac{\pi}{4}\right)\left(i\,\tfrac{\pi}{2}\right)}$$

## Paso 4: Multiplicar el exponente

$$\left(\tfrac{1}{2}\ln 2 + i\,\tfrac{\pi}{4}\right)\left(i\,\tfrac{\pi}{2}\right) = i\,\tfrac{\pi}{4}\ln 2 + i^2\,\tfrac{\pi^2}{8} = -\tfrac{\pi^2}{8} + i\,\tfrac{\pi\ln 2}{4}$$

Por tanto:

$$i^{\ln(1+i)} = e^{-\pi^2/8 + i(\pi\ln 2)/4} = e^{-\pi^2/8}\left[\cos\left(\tfrac{\pi\ln 2}{4}\right) + i\,\text{sen}\left(\tfrac{\pi\ln 2}{4}\right)\right]$$

## Paso 5: Extraer la parte real

$$\boxed{\Re\!\left[i^{\ln(1+i)}\right] = e^{-\pi^2/8}\cos\!\left(\frac{\pi\ln 2}{4}\right)}$$

> [!warning] Discrepancia con el video del curso
> El video del docente presenta como respuesta $e^{-\pi^2/8}$ omitiendo el factor $\cos(\pi\ln 2 / 4)$. Esto es **incorrecto**: el resultado completo de la multiplicacion deja una parte imaginaria no nula que debe distribuirse como parte real (cos) y parte imaginaria (sen). Numericamente $\cos(\pi\ln 2/4) \approx 0.853$, asi que el video aproxima por exceso aprox un 17%.

## Valor numerico aproximado

$$e^{-\pi^2/8} \approx 0.2910, \quad \cos(\pi\ln 2 / 4) \approx 0.8530$$

$$\Re\!\left[i^{\ln(1+i)}\right] \approx 0.2483$$
