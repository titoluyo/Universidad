---
title: Ejercicio 2 - Derivada por regla de la cadena
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 3
orden: 3
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/derivada-compleja
  - tema/regla-de-la-cadena
date: 2026-04-12
---

## Enunciado

Derivar $\cos^2(2z + 3i)$ por la regla de la cadena.

![[video-ej2-enunciado.png]]

## Resolucion

### Paso 1: Definir la funcion y realizar sustituciones

Sea:

$$w = \cos^2(2z + 3i)$$

Para aplicar la regla de la cadena, introducimos variables intermedias:

1. Sea $\sigma = 2z + 3i$, entonces $w = \cos^2 \sigma$
2. Sea $t = \cos \sigma$, entonces $w = t^2$

![[video-ej2-cadena.png]]

### Paso 2: Plantear la regla de la cadena

Como $w$ depende de $t$, $t$ depende de $\sigma$, y $\sigma$ depende de $z$:

$$\frac{dw}{dz} = \frac{dw}{dt} \cdot \frac{dt}{d\sigma} \cdot \frac{d\sigma}{dz} \quad (1)$$

### Paso 3: Calcular cada derivada

**Derivada de $w$ con respecto a $t$:**

$$w = t^2 \implies \frac{dw}{dt} = 2t$$

**Derivada de $t$ con respecto a $\sigma$:**

$$t = \cos \sigma \implies \frac{dt}{d\sigma} = -\operatorname{sen} \sigma$$

**Derivada de $\sigma$ con respecto a $z$:**

$$\sigma = 2z + 3i \implies \frac{d\sigma}{dz} = 2$$

![[video-ej2-derivadas.png]]

### Paso 4: Sustituir en la ecuacion (1)

$$\frac{dw}{dz} = (2t) \cdot (-\operatorname{sen} \sigma) \cdot (2) = -4t \operatorname{sen} \sigma$$

Reemplazamos $t = \cos \sigma$ y $\sigma = 2z + 3i$:

$$\frac{dw}{dz} = -4 \cos(2z + 3i) \operatorname{sen}(2z + 3i)$$

### Paso 5: Simplificar con identidad trigonometrica

Usando la identidad del angulo doble $2 \operatorname{sen} \alpha \cos \alpha = \operatorname{sen}(2\alpha)$:

$$-4 \cos(2z+3i)\operatorname{sen}(2z+3i) = -2 \cdot 2\operatorname{sen}(2z+3i)\cos(2z+3i) = -2\operatorname{sen}(2(2z+3i))$$

### Resultado final

$$\boxed{\frac{d}{dz}\cos^2(2z + 3i) = -2\operatorname{sen}(4z + 6i)}$$

![[video-ej2-resultado.png]]
