---
title: Formulario - Series y Transformadas
curso: "[[SeriesTransformadas MOC]]"
tipo: formulario
tags:
  - curso/series-transformadas
  - tipo/formulario
date: 2026-03-29
---

## Numeros complejos

Fuente: [[S01-1 Tema 01 - Funciones en el plano complejo]]

### Representacion

| Forma | Expresion |
| ----- | --------- |
| Binomica | $z = a + bi$ |
| Polar | $z = \|z\|(\cos\theta + i\,\text{sen}\,\theta)$ |
| Exponencial (Euler) | $z = \|z\|\,e^{i\theta}$ |

### Modulo y conjugado

$$|z| = \sqrt{a^2 + b^2}$$

$$\bar{z} = a - ib$$

### Formula de Euler

$$e^{i\theta} = \cos\theta + i\,\text{sen}\,\theta$$

### Argumento

$$\arg(z) = \{\theta_0 + 2k\pi,\ k \in \mathbb{Z}\}$$

Donde $\theta_0$ es el argumento principal con $-\pi < \theta_0 < \pi$.

### Operaciones en forma binomica

Sean $z_1 = (a_1, b_1)$ y $z_2 = (a_2, b_2)$:

$$z_1 + z_2 = (a_1 + a_2,\ b_1 + b_2)$$

$$z_1 \cdot z_2 = (a_1 a_2 - b_1 b_2,\ b_1 a_2 + a_1 b_2)$$

$$\frac{z_1}{z_2} = \left(\frac{a_1 a_2 + b_1 b_2}{a_2^2 + b_2^2},\ \frac{b_1 a_2 - a_1 b_2}{a_2^2 + b_2^2}\right), \quad z_2 \neq 0$$

### Operaciones en forma polar-exponencial

Sean $z_1 = |z_1|\,e^{i\theta_1}$ y $z_2 = |z_2|\,e^{i\theta_2}$:

$$z_1 \cdot z_2 = |z_1|\,|z_2|\,e^{i(\theta_1 + \theta_2)}$$

$$\frac{z_1}{z_2} = \frac{|z_1|}{|z_2|}\,e^{i(\theta_1 - \theta_2)}$$

$$z^n = |z|^n\,e^{in\theta}$$

### Raices n-esimas

$$w_k = \sqrt[m]{|z|}\,e^{i\left(\frac{\theta_0 + 2k\pi}{m}\right)}, \quad k = 0, 1, \ldots, m-1$$

### Funciones de variable compleja

$$w = f(z) = u(x, y) + iv(x, y)$$

Donde:
- $u(x, y)$ = parte real de $f(z)$
- $v(x, y)$ = parte imaginaria de $f(z)$
