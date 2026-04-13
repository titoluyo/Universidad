---
title: Ejercicio 1 - Derivada de cociente de funciones complejas
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 3
orden: 2
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/derivada-compleja
date: 2026-04-12
---

## Enunciado

Determinar la derivada de la siguiente funcion con respecto a $z$:

$$f(z) = \frac{\sqrt{z - 4} - 2i}{z}$$

![[video-ej1-enunciado.png]]

## Resolucion

### Paso 1: Identificar las funciones del cociente

Expresamos $f(z)$ como un cociente de dos funciones:

$$f(z) = \frac{h(z)}{g(z)}$$

Donde:
- $h(z) = \sqrt{z - 4} - 2i$
- $g(z) = z$

![[video-ej1-identificacion.png]]

### Paso 2: Aplicar la [[S03-1 Tema 03 - Derivada de una funcion compleja#Propiedad 4 Derivada del cociente|propiedad de la derivada del cociente]]

$$f'(z) = \frac{h'(z) \cdot g(z) - h(z) \cdot g'(z)}{[g(z)]^2}$$

### Paso 3: Calcular las derivadas individuales

**Derivada de $h(z)$:**

$$h(z) = (z - 4)^{1/2} - 2i$$

$$h'(z) = \frac{1}{2}(z - 4)^{1/2 - 1} \cdot 1 = \frac{1}{2}(z - 4)^{-1/2} = \frac{1}{2\sqrt{z - 4}}$$

> [!note] Nota
> La derivada de la constante $-2i$ es cero. La derivada del contenido interno $(z - 4)$ con respecto a $z$ es $1$.

**Derivada de $g(z)$:**

$$g'(z) = 1$$

![[video-ej1-derivada.png]]

### Paso 4: Sustituir en la formula del cociente

$$f'(z) = \frac{\dfrac{1}{2\sqrt{z-4}} \cdot z - (\sqrt{z-4} - 2i) \cdot 1}{z^2}$$

$$= \frac{\dfrac{z}{2\sqrt{z-4}} - \sqrt{z-4} + 2i}{z^2}$$

![[video-ej1-sustitucion.png]]

### Paso 5: Simplificar el numerador

Combinamos los terminos que contienen $\sqrt{z-4}$:

$$\frac{z}{2\sqrt{z-4}} - \sqrt{z-4} = \frac{z}{2\sqrt{z-4}} - \frac{2(z-4)}{2\sqrt{z-4}} = \frac{z - 2(z - 4)}{2\sqrt{z-4}}$$

$$= \frac{z - 2z + 8}{2\sqrt{z-4}} = \frac{-z + 8}{2\sqrt{z-4}}$$

### Resultado final

$$\boxed{f'(z) = \frac{-z + 8 + 4i\sqrt{z-4}}{2z^2\sqrt{z-4}}}$$

![[video-ej1-resultado.png]]
