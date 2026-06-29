---
title: "Ejercicio 5 — Ecuación en diferencias homogénea (raíces reales)"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 17
orden: 6
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/transformada-z-inversa
  - tema/ecuaciones-en-diferencias
  - tema/fracciones-parciales
date: 2026-07-13
---

## Enunciado

> [!question] Problema
> Evaluar con la transformada Z la ecuación en diferencias
> $$2y[n+2] - 5y[n+1] - 3y[n] = 0$$
> con condiciones iniciales $y[0] = 3$ y $y[1] = 2$.

## Desarrollo

### Paso 1 — Aplicar la transformada Z (adelanto con condiciones iniciales)

$$2\bigl(z^2 Y - y_0 z^2 - y_1 z\bigr) - 5\bigl(zY - y_0 z\bigr) - 3Y = 0$$

Sustituyendo $y_0 = 3$, $y_1 = 2$:

$$2\bigl(z^2 Y - 3z^2 - 2z\bigr) - 5\bigl(zY - 3z\bigr) - 3Y = 0$$
$$\bigl(2z^2 Y - 6z^2 - 4z\bigr) - \bigl(5zY - 15z\bigr) - 3Y = 0$$

### Paso 2 — Despejar $Y(z)$

$$Y(z)\,(2z^2 - 5z - 3) = 6z^2 - 11z$$
$$Y(z) = \frac{6z^2 - 11z}{2z^2 - 5z - 3}$$

Factorizando el denominador $2z^2 - 5z - 3 = (z-3)(2z+1)$ y dividiendo entre $z$:

$$\frac{Y(z)}{z} = \frac{6z - 11}{(z-3)(2z+1)}$$

### Paso 3 — Fracciones parciales (por residuos)

$$\frac{Y(z)}{z} = \frac{A}{z-3} + \frac{B}{2z+1}$$

$$A = \lim_{z\to 3}(z-3)\frac{6z-11}{(z-3)(2z+1)} = \frac{6(3)-11}{2(3)+1} = \frac{7}{7} = 1$$

$$B = \lim_{z\to -\frac12}\left(z+\tfrac12\right)\frac{6z-11}{(z-3)\left(z+\frac12\right)} = \frac{6\left(-\frac12\right)-11}{-\frac12-3} = \frac{-14}{-\frac72} = 4$$

Multiplicando por $z$:

$$Y(z) = \frac{z}{z-3} + \frac{4z}{2z+1} = \frac{z}{z-3} + \frac{2z}{z+\frac12}$$

### Paso 4 — Transformada inversa

Usando $\mathcal{Z}^{-1}\left\{\dfrac{z}{z-a}\right\} = a^k$:

> [!success] Resultado
> $$\boxed{\;y[n] = 3^{\,k} + 2\left(-\tfrac{1}{2}\right)^{k}\;}$$

### Verificación

- $y[0] = 3^0 + 2(-\tfrac12)^0 = 1 + 2 = 3$. ✓
- $y[1] = 3^1 + 2(-\tfrac12)^1 = 3 - 1 = 2$. ✓

> [!tip] Contraste con el Ej 4
> Aquí las raíces $z=3$ y $z=-\tfrac12$ son **reales** → solución suma de exponenciales $3^k$ y $(-\tfrac12)^k$. Cuando las raíces son **complejas conjugadas** (como en [[S17-5 Tema 01 - Ecuacion en diferencias con entrada|Ej 4]]) la solución es una **sinusoide amortiguada**.

## Conceptos aplicados

- [[S17-1 Tema 01 - Transformada Z Parte 2#4. Transformada Z unilateral|Desplazamiento unilateral (condiciones iniciales)]].
- [[S17-1 Tema 01 - Transformada Z Parte 2#2. Transformada Z inversa|Fracciones parciales]] + tabla.

## Bibliografía

- Mitra, S. K. (2007). *Procesamiento de Señales Digitales* (3.ª ed.). McGraw-Hill. México.
