---
title: "Ejercicio 3 — Transformada Z inversa por residuos (dos polos simples)"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 17
orden: 4
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/transformada-z-inversa
  - tema/residuos
date: 2026-07-13
---

## Enunciado

> [!question] Problema
> Calcular la transformada Z inversa, usando la **integral de inversión (residuos)**, de:
> $$F(z) = \frac{z}{(z-1)(z-0.8)}$$

## Desarrollo

### Paso 1 — Identificar los polos

Igualando el denominador a cero, hay **dos polos simples**: $z_0 = 1$ y $z_0 = 0.8$. La solución es la suma de los residuos:

$$f(k) = R_1\big|_{z=1} + R_2\big|_{z=0.8}$$

### Paso 2 — Fórmula del residuo

$$\text{Residuo} = \lim_{z\to z_0} (z - z_0)\,F(z)\,z^{k-1}$$

### Paso 3 — Calcular cada residuo

$$R_1 = \lim_{z\to 1}(z-1)\frac{z\cdot z^{k-1}}{(z-1)(z-0.8)} = \frac{1^{k}}{1-0.8} = \frac{1}{0.2} = 5$$

$$R_2 = \lim_{z\to 0.8}(z-0.8)\frac{z\cdot z^{k-1}}{(z-1)(z-0.8)} = \frac{0.8^{k}}{0.8-1} = \frac{0.8^{k}}{-0.2} = -5\,(0.8)^{k}$$

### Resultado

$$f(k) = R_1 + R_2 = 5 - 5\,(0.8)^k$$

> [!success] Resultado
> $$\boxed{\;f(k) = 5\,\bigl(1 - 0.8^{\,k}\bigr)\;}$$

> [!note] Verificación
> $f(0) = 5(1-1) = 0$ y $f(\infty) \to 5$ (el polo en $z=1$ aporta el régimen permanente; el polo en $z=0.8<1$ aporta el transitorio que decae). Coincide con el resultado del portal.

## Conceptos aplicados

- [[S17-1 Tema 01 - Transformada Z Parte 2#3. Método de la integral de inversión (residuos)|Integral de inversión (residuos)]].

## Bibliografía

- Mitra, S. K. (2007). *Procesamiento de Señales Digitales* (3.ª ed.). McGraw-Hill. México.
