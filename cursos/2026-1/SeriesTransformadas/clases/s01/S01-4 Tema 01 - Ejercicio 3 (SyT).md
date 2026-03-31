---
title: Ejercicio 3 - Raices cubicas de un numero complejo
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 1
orden: 4
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/numeros-complejos
  - tema/raices-n-esimas
date: 2026-03-29
---

## Enunciado

Encontrar las raices de $(-1 + i)^{\frac{1}{3}}$.

## Desarrollo

### Paso 1: Determinar modulo y argumento

Ubicamos el punto $z = -1 + i$ en el plano cartesiano para determinar el angulo principal y el modulo.

![[Pasted image 20260329222757.png]]

Del grafico verificamos que:
- $\theta = \dfrac{3\pi}{4}$ (segundo cuadrante)
- $|z| = \sqrt{(-1)^2 + 1^2} = \sqrt{2}$

### Paso 2: Aplicar la formula de raices n-esimas

Usando la formula de [[S01-1 Tema 01 - Funciones en el plano complejo#Raices n-esimas polar-exponencial|raices n-esimas]]:

$$z^{\frac{1}{n}} = |z|^{\frac{1}{n}} \left\{ \cos\left(\frac{\theta + 2k\pi}{n}\right) + i\,\text{sen}\left(\frac{\theta + 2k\pi}{n}\right) \right\}$$

### Paso 3: Sustituir los datos

Con $|z| = \sqrt{2}$, $\theta = \dfrac{3\pi}{4}$ y $n = 3$:

$$(-1 + i)^{\frac{1}{3}} = (\sqrt{2})^{\frac{1}{3}} \left\{ \cos\left(\frac{\frac{3\pi}{4} + 2k\pi}{3}\right) + i\,\text{sen}\left(\frac{\frac{3\pi}{4} + 2k\pi}{3}\right) \right\}$$

Donde $(\sqrt{2})^{1/3} = 2^{1/6} = \sqrt[6]{2}$.

### Paso 4: Calcular las 3 raices ($k = 0, 1, 2$)

**Para $k = 0$:**

$$w_0 = \sqrt[6]{2} \left\{ \cos\left(\frac{3\pi/4}{3}\right) + i\,\text{sen}\left(\frac{3\pi/4}{3}\right) \right\} = \sqrt[6]{2} \left\{ \cos\frac{\pi}{4} + i\,\text{sen}\frac{\pi}{4} \right\}$$

**Para $k = 1$:**

$$w_1 = \sqrt[6]{2} \left\{ \cos\left(\frac{3\pi/4 + 2\pi}{3}\right) + i\,\text{sen}\left(\frac{3\pi/4 + 2\pi}{3}\right) \right\} = \sqrt[6]{2} \left\{ \cos\frac{11\pi}{12} + i\,\text{sen}\frac{11\pi}{12} \right\}$$

**Para $k = 2$:**

$$w_2 = \sqrt[6]{2} \left\{ \cos\left(\frac{3\pi/4 + 4\pi}{3}\right) + i\,\text{sen}\left(\frac{3\pi/4 + 4\pi}{3}\right) \right\} = \sqrt[6]{2} \left\{ \cos\frac{19\pi}{12} + i\,\text{sen}\frac{19\pi}{12} \right\}$$

> [!tip] Verificacion
> Como $n = 3$, existen exactamente **3 raices** cubicas ($k = 0, 1, 2$). Las raices estan separadas por angulos de $\dfrac{2\pi}{3} = 120°$ entre si, equidistribuidas en un circulo de radio $\sqrt[6]{2}$.
