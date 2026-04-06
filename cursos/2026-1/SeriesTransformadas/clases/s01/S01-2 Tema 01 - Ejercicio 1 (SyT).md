---
title: Ejercicio 1 - Operaciones con numeros complejos
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 1
orden: 2
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/numeros-complejos
  - tema/operaciones-complejas
date: 2026-03-29
---

## Video del ejercicio

![Ejercicio 1](https://www.youtube.com/watch?v=IT68dfhXJts)

## Ejercicio 1a: Operaciones basicas

Sean $z_1 = 3 + 4i$ y $z_2 = 1 - 2i$. Calcular suma, resta, multiplicacion y division.

### Desarrollo

**a) Suma:**

$$z_1 + z_2 = (3 + 1) + (4 - 2)i = 4 + 2i$$

**b) Resta:**

$$z_1 - z_2 = (3 - 1) + (4 - (-2))i = 2 + 6i$$

**c) Multiplicacion:**

$$z_1 \cdot z_2 = (3)(1) - (4)(-2) + [(3)(-2) + (4)(1)]i = 3 + 8 + (-6 + 4)i = 11 - 2i$$

**d) Division** (multiplicando por la [[S01-1 Tema 01 - Funciones en el plano complejo#Propiedades del conjugado|conjugada]]):

$$\frac{z_1}{z_2} = \frac{(3 + 4i)(1 + 2i)}{|z_2|^2} = \frac{3 + 6i + 4i + 8i^2}{1 + 4} = \frac{-5 + 10i}{5} = -1 + 2i$$

## Ejercicio 1b: Conjugado y modulo

Para $z = 3 - 4i$, encontrar $\bar{z}$, $|z|$ y $z \cdot \bar{z}$.

### Desarrollo

$$\bar{z} = 3 + 4i$$

$$|z| = \sqrt{3^2 + (-4)^2} = \sqrt{9 + 16} = 5$$

$$z \cdot \bar{z} = (3 - 4i)(3 + 4i) = 9 + 16 = 25 = |z|^2$$

> [!tip] Verificacion
> Se cumple la propiedad $z \cdot \bar{z} = |z|^2 = 25$.

## Ejercicio 1c: Determinar los valores de $(-1)^{1/2}$

### Desarrollo

#### Paso 1: Forma polar de $z = -1$

- $|z| = 1$
- $\theta_0 = \pi$ (eje real negativo)

#### Paso 2: Aplicar [[S01-1 Tema 01 - Funciones en el plano complejo#Raíces n-esimas polar-exponencial|raices n-esimas]] con $m = 2$

$$w_k = |z|^{1/2} \left\{ \cos\left(\frac{\pi + 2k\pi}{2}\right) + i\,\text{sen}\left(\frac{\pi + 2k\pi}{2}\right) \right\}$$

#### Paso 3: Calcular las 2 raices

**Para $k = 0$:**

$$w_0 = \cos\frac{\pi}{2} + i\,\text{sen}\frac{\pi}{2} = i$$

**Para $k = 1$:**

$$w_1 = \cos\frac{3\pi}{2} + i\,\text{sen}\frac{3\pi}{2} = -i$$

> [!success] Resultado
> Las raices cuadradas de $-1$ son $w_0 = i$ y $w_1 = -i$, ubicadas sobre el circulo unitario en angulos $\frac{\pi}{2}$ y $\frac{3\pi}{2}$.

## Ejercicio 1d: Expresar $2x + y = 5$ en funcion de $z$ y $\bar{z}$

### Desarrollo

Sabemos que $z = x + iy$ y $\bar{z} = x - iy$. Despejamos $x$ e $y$:

$$x = \frac{z + \bar{z}}{2}, \qquad y = \frac{z - \bar{z}}{2i}$$

Sustituimos en $2x + y = 5$:

$$2\left(\frac{z + \bar{z}}{2}\right) + \frac{z - \bar{z}}{2i} = 5$$

$$(z + \bar{z}) + \frac{z - \bar{z}}{2i} = 5$$

Multiplicamos por $2i$:

$$2i(z + \bar{z}) + (z - \bar{z}) = 10i$$

$$z(2i + 1) + \bar{z}(2i - 1) = 10i$$

> [!tip] Nota
> Esta tecnica de expresar ecuaciones reales en terminos de $z$ y $\bar{z}$ es util en el estudio de curvas y regiones en el plano complejo.
