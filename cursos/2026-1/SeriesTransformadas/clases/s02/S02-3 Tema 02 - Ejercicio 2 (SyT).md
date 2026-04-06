---
title: Ejercicio 2 - Limite por regla de L'Hospital
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 2
orden: 3
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/limites-complejos
  - tema/l-hospital
date: 2026-04-05
---

## Enunciado

Evaluar:

$$\lim_{z \to 2i} \frac{z^2 + 4}{z^2 - 3iz - 2}$$

## Desarrollo

### Verificar la indeterminacion

Evaluamos directamente en $z = 2i$:

$$f(2i) = \frac{(2i)^2 + 4}{(2i)^2 - 3i(2i) - 2} = \frac{-4 + 4}{-4 + 6 - 2} = \frac{0}{0}$$

Obtenemos la [[S02-1 Tema 02 - Limites y continuidad de funciones complejas#Metodos para resolver limites|indeterminacion]] $\frac{0}{0}$.

### Aplicar la regla de L'Hospital

Derivamos numerador y denominador por separado:

$$\frac{(z^2 + 4)'}{(z^2 - 3iz - 2)'} = \frac{2z}{2z - 3i}$$

### Evaluar el limite

$$\lim_{z \to 2i} \frac{2z}{2z - 3i} = \frac{2(2i)}{2(2i) - 3i} = \frac{4i}{4i - 3i} = \frac{4i}{i} = 4$$

> [!success] Resultado
> $$\lim_{z \to 2i} \frac{z^2 + 4}{z^2 - 3iz - 2} = 4$$
