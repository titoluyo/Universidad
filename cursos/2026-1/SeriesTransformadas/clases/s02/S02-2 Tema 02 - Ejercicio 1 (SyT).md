---
title: Ejercicio 1 - Limite por racionalizacion
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 2
orden: 2
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/limites-complejos
  - tema/racionalizacion
date: 2026-04-05
---

## Enunciado

Determinar el limite de la funcion $f(z) = \dfrac{\sqrt{z - 4} - 2i}{z}$, cuando $z \to 0$.

## Desarrollo

### Verificar la indeterminacion

Evaluamos directamente en $z = 0$:

$$f(0) = \frac{\sqrt{0 - 4} - 2i}{0} = \nexists$$

El denominador se anula, por lo que la evaluacion directa no es posible.

### Resolver por racionalizacion

Multiplicamos numerador y denominador por el [[S02-1 Tema 02 - Limites y continuidad de funciones complejas#Metodos para resolver limites|conjugado]] del numerador $\sqrt{z - 4} + 2i$:

$$\lim_{z \to 0} \frac{(\sqrt{z - 4} - 2i)(\sqrt{z - 4} + 2i)}{z(\sqrt{z - 4} + 2i)}$$

Aplicamos diferencia de cuadrados en el numerador:

$$\lim_{z \to 0} \frac{(\sqrt{z - 4})^2 - (2i)^2}{z(\sqrt{z - 4} + 2i)}$$

$$\lim_{z \to 0} \frac{z - 4 - (-4)}{z(\sqrt{z - 4} + 2i)} = \lim_{z \to 0} \frac{z}{z(\sqrt{z - 4} + 2i)}$$

Simplificamos $z$:

$$\lim_{z \to 0} \frac{1}{\sqrt{z - 4} + 2i}$$

### Evaluar el limite

$$\frac{1}{\sqrt{-4} + 2i} = \frac{1}{2i + 2i} = \frac{1}{4i}$$

Racionalizamos multiplicando por $\dfrac{-4i}{-4i}$:

$$\frac{1}{4i} \cdot \frac{-4i}{-4i} = \frac{-i}{4}$$

> [!success] Resultado
> $$\lim_{z \to 0} \frac{\sqrt{z - 4} - 2i}{z} = -\frac{i}{4}$$
