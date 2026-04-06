---
title: Ejercicio 3 - Continuidad por factorizacion
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 2
orden: 4
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/limites-complejos
  - tema/continuidad-complejas
  - tema/factorizacion
date: 2026-04-05
---

## Enunciado

Sea la funcion:

$$f(z) = \begin{cases} \dfrac{z^2 - 4}{x + 2}, & x \neq -2 \\ f(-2) = 10 \end{cases}$$

Diga si la funcion es continua o discontinua y determine su limite.

## Desarrollo

Para probar si la funcion es [[S02-1 Tema 02 - Limites y continuidad de funciones complejas#Definicion|continua]] debe cumplir las tres condiciones:

1. $\displaystyle\lim_{z \to z_0} f(z)$ existe
2. $f(z_0)$ existe
3. $\displaystyle\lim_{z \to z_0} f(z) = f(z_0)$

### Condiciones 1 y 2: Determinar el limite

Evaluamos directamente en $z = -2$:

$$f(-2) = \frac{(-2)^2 - 4}{-2 + 2} = \frac{0}{0}$$

Resolvemos por [[S02-1 Tema 02 - Limites y continuidad de funciones complejas#Metodos para resolver limites|factorizacion]], donde $z^2 - 4 = (z - 2)(z + 2)$:

$$\lim_{z \to -2} \frac{z^2 - 4}{z + 2} = \lim_{z \to -2} \frac{(z - 2)(z + 2)}{z + 2}$$

$$= \lim_{z \to -2} (z - 2) = -2 - 2 = -4$$

El limite existe y vale $-4$. Ademas, $f(-2) = 10$ esta definida.

### Condicion 3: Comparar limite con valor de la funcion

$$\lim_{z \to -2} f(z) = -4$$

$$f(-2) = 10$$

$$-4 \neq 10$$

> [!fail] Resultado
> No se cumple la tercera condicion de continuidad. Por lo tanto, $f(z)$ es **discontinua** en $z = -2$.
