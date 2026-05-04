---
title: "Ejercicio 1 - Transformar z = 1 - i a su forma exponencial"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 5
orden: 2
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/funcion-exponencial-compleja
  - tema/forma-exponencial
date: 2026-04-26
---

## Enunciado

Dado el numero complejo:

$$z = 1 - i$$

Transformar $z$ a su **forma exponencial**.

## Referencia teorica

Ver [[S05-1 Tema 05 - Funciones complejas elementales#1. Funcion exponencial|funcion exponencial]] y la formula de Euler. La forma exponencial es:

$$z = |z|\,e^{i\theta}$$

donde $|z|$ es el modulo y $\theta$ el argumento (en radianes).

## Paso 1: Ubicar $z$ en el plano

Identificamos parte real e imaginaria:

- Parte real: $a = 1$
- Parte imaginaria: $b = -1$

Como $a > 0$ y $b < 0$, el punto $z$ se ubica en el **cuarto cuadrante** del plano complejo.

## Paso 2: Calcular el argumento $\theta$

En el cuarto cuadrante el angulo se mide en sentido **horario** (negativo):

$$\tan\theta = \frac{|b|}{|a|} = \frac{1}{1} = 1$$

$$\theta = -\frac{\pi}{4} \quad (\text{equivalente a } -45°)$$

> [!info] Regla de signos del argumento
> - Si el angulo esta en el **1er o 2do cuadrante**: se mide antihorario (positivo).
> - Si esta en el **3er o 4to cuadrante**: se mide horario (negativo).

## Paso 3: Calcular el modulo $|z|$

$$|z| = \sqrt{a^2 + b^2} = \sqrt{1^2 + (-1)^2} = \sqrt{2}$$

## Paso 4: Forma exponencial

Sustituyendo en $z = |z|\,e^{i\theta}$:

$$\boxed{z = \sqrt{2}\,e^{-i\pi/4}}$$

## Verificacion

Aplicando la formula de Euler:

$$\sqrt{2}\,e^{-i\pi/4} = \sqrt{2}\left[\cos\left(-\tfrac{\pi}{4}\right) + i\,\text{sen}\left(-\tfrac{\pi}{4}\right)\right] = \sqrt{2}\left[\tfrac{\sqrt{2}}{2} - i\,\tfrac{\sqrt{2}}{2}\right] = 1 - i \checkmark$$
