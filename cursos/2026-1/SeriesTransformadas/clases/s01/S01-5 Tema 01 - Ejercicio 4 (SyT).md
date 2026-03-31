---
title: Ejercicio 4 - Raices cubicas de un imaginario puro
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 1
orden: 5
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/numeros-complejos
  - tema/raices-n-esimas
date: 2026-03-29
---

## Enunciado

Hallar los valores de $(-8i)^{\frac{1}{3}}$.

## Desarrollo

### Paso 1: Determinar modulo y argumento

Graficamos $z = -8i$ en el plano complejo para determinar su angulo principal y su modulo.

![[Pasted image 20260329223826.png]]

Del grafico verificamos que:
- $|z| = 8$
- $\theta = -\dfrac{\pi}{2}$ (eje imaginario negativo)

### Paso 2: Aplicar la formula de raices n-esimas

Usando la formula de [[S01-1 Tema 01 - Funciones en el plano complejo#Raices n-esimas polar-exponencial|raices n-esimas]]:

$$z^{\frac{1}{n}} = |z|^{\frac{1}{n}} \left\{ \cos\left(\frac{\theta + 2k\pi}{n}\right) + i\,\text{sen}\left(\frac{\theta + 2k\pi}{n}\right) \right\}$$

### Paso 3: Sustituir los datos

Con $|z| = 8$, $\theta = -\dfrac{\pi}{2}$ y $n = 3$:

$$(-8i)^{\frac{1}{3}} = 8^{\frac{1}{3}} \left\{ \cos\left(\frac{-\frac{\pi}{2} + 2k\pi}{3}\right) + i\,\text{sen}\left(\frac{-\frac{\pi}{2} + 2k\pi}{3}\right) \right\}$$

$$= 2 \left\{ \cos\left(\frac{-\frac{\pi}{2} + 2k\pi}{3}\right) + i\,\text{sen}\left(\frac{-\frac{\pi}{2} + 2k\pi}{3}\right) \right\}$$

### Paso 4: Calcular las 3 raices ($k = 0, 1, 2$)

**Para $k = 0$:**

$$w_0 = 2 \left\{ \cos\left(-\frac{\pi}{6}\right) + i\,\text{sen}\left(-\frac{\pi}{6}\right) \right\} = 2 \left\{ \cos\frac{\pi}{6} - i\,\text{sen}\frac{\pi}{6} \right\} = \sqrt{3} - i$$

**Para $k = 1$:**

$$w_1 = 2 \left\{ \cos\frac{\pi}{2} + i\,\text{sen}\frac{\pi}{2} \right\} = 2i$$

**Para $k = 2$:**

$$w_2 = 2 \left\{ \cos\frac{7\pi}{6} + i\,\text{sen}\frac{7\pi}{6} \right\} = -\sqrt{3} - i$$

> [!tip] Verificacion
> Las 3 raices estan separadas por angulos de $\dfrac{2\pi}{3} = 120°$, equidistribuidas en un circulo de radio $2$. Se puede verificar que $-\dfrac{\pi}{6} + \dfrac{2\pi}{3} = \dfrac{\pi}{2}$ y $\dfrac{\pi}{2} + \dfrac{2\pi}{3} = \dfrac{7\pi}{6}$.
