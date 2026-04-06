---
title: Ejercicio 2 - Forma polar, potencias y ecuaciones complejas
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 1
orden: 3
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/numeros-complejos
  - tema/forma-polar
  - tema/de-moivre
date: 2026-03-29
---

## Video del ejercicio

![Ejercicio 2](https://www.youtube.com/watch?v=o7-74UB5gpw)

## Ejercicio 2a: Conversion a forma polar

Convertir $z = 1 + i$ a forma polar y exponencial.

### Desarrollo

$$r = |z| = \sqrt{1^2 + 1^2} = \sqrt{2}$$

$$\theta = \arctan\frac{1}{1} = \frac{\pi}{4}$$

**Forma polar:**

$$z = \sqrt{2}\left(\cos\frac{\pi}{4} + i\,\text{sen}\frac{\pi}{4}\right)$$

**Forma exponencial:**

$$z = \sqrt{2}\,e^{i\pi/4}$$

## Ejercicio 2b: Potencia con De Moivre

Calcular $(1 + i)^8$.

### Desarrollo

Usamos la [[S01-1 Tema 01 - Funciones en el plano complejo#Forma polar|forma polar]]: $1 + i = \sqrt{2}\,e^{i\pi/4}$

Aplicamos la [[S01-1 Tema 01 - Funciones en el plano complejo#Potencia polar-exponencial|formula de De Moivre]]:

$$(1 + i)^8 = (\sqrt{2})^8 \left(\cos\frac{8\pi}{4} + i\,\text{sen}\frac{8\pi}{4}\right) = 16(\cos 2\pi + i\,\text{sen}\,2\pi) = 16$$

## Ejercicio 2c: Raices cubicas de 8

Encontrar las raices cubicas de $z = 8$.

### Desarrollo

En forma polar: $z = 8 = 8\,e^{i \cdot 0}$ (modulo 8, argumento 0).

Las raices son $w_k = \sqrt[3]{8}\,e^{i(2k\pi/3)} = 2\,e^{i(2k\pi/3)}$ para $k = 0, 1, 2$:

**Para $k = 0$:**

$$w_0 = 2(\cos 0 + i\,\text{sen}\,0) = 2$$

**Para $k = 1$:**

$$w_1 = 2\left(\cos\frac{2\pi}{3} + i\,\text{sen}\frac{2\pi}{3}\right) = 2\left(-\frac{1}{2} + i\frac{\sqrt{3}}{2}\right) = -1 + \sqrt{3}\,i$$

**Para $k = 2$:**

$$w_2 = 2\left(\cos\frac{4\pi}{3} + i\,\text{sen}\frac{4\pi}{3}\right) = 2\left(-\frac{1}{2} - i\frac{\sqrt{3}}{2}\right) = -1 - \sqrt{3}\,i$$

> [!tip] Verificacion
> Las 3 raices estan equidistribuidas en un circulo de radio 2, separadas por angulos de $120°$.

## Ejercicio 2d: Ecuacion cuadratica compleja

Resolver $z^2 + 2z + 5 = 0$.

### Desarrollo

Usando la formula cuadratica:

$$z = \frac{-2 \pm \sqrt{4 - 20}}{2} = \frac{-2 \pm \sqrt{-16}}{2} = \frac{-2 \pm 4i}{2}$$

$$z_1 = -1 + 2i, \qquad z_2 = -1 - 2i$$

> [!tip] Nota
> Las soluciones son conjugadas entre si, como siempre ocurre en ecuaciones con coeficientes reales.

## Ejercicio 2e: Raices cuartas de la unidad

Encontrar todas las raices de $z^4 = 1$.

### Desarrollo

$z = 1 = e^{i \cdot 0}$, entonces:

$$w_k = e^{i(2k\pi/4)}, \quad k = 0, 1, 2, 3$$

| $k$ | Angulo | Raiz |
| --- | --- | --- |
| 0 | $0$ | $w_0 = 1$ |
| 1 | $\pi/2$ | $w_1 = i$ |
| 2 | $\pi$ | $w_2 = -1$ |
| 3 | $3\pi/2$ | $w_3 = -i$ |

## Ejercicio 2f: Funcion compleja

Sea $f(z) = z^2 + 1$. Evaluar $f(1 + i)$ e identificar $u$ y $v$.

### Desarrollo

$$f(1 + i) = (1 + i)^2 + 1 = (1 + 2i + i^2) + 1 = (1 + 2i - 1) + 1 = 1 + 2i$$

Identificamos partes:
- $u = \text{Re}(w) = 1$
- $v = \text{Im}(w) = 2$
