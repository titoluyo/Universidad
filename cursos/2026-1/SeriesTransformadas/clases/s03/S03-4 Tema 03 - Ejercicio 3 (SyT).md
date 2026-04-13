---
title: Ejercicio 3 - Verificar existencia de derivada con Cauchy-Riemann
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 3
orden: 4
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/derivada-compleja
  - tema/cauchy-riemann
date: 2026-04-12
---

## Enunciado

Verificar que la derivada de la funcion $f(z) = z^2 + 5iz + 3 - i$ existe.

![[video-ej3-enunciado.png]]

## Resolucion

Para verificar la existencia de la derivada aplicamos las [[S03-1 Tema 03 - Derivada de una funcion compleja#Ecuacion de Cauchy-Riemann|ecuaciones de Cauchy-Riemann]].

### Paso 1: Sustituir $z = x + iy$

$$f(z) = (x + iy)^2 + 5i(x + iy) + 3 - i$$

Expandimos cada termino:

$$(x + iy)^2 = x^2 + 2ixy + i^2y^2 = x^2 + 2ixy - y^2$$

$$5i(x + iy) = 5ix + 5i^2y = 5ix - 5y$$

Entonces:

$$f(z) = x^2 + 2ixy - y^2 + 5ix - 5y + 3 - i$$

### Paso 2: Separar parte real e imaginaria

Agrupamos:

$$f(z) = \underbrace{(x^2 - y^2 - 5y + 3)}_{u(x,y)} + i\underbrace{(2xy + 5x - 1)}_{v(x,y)}$$

Donde:
- $u(x,y) = x^2 - y^2 - 5y + 3$
- $v(x,y) = 2xy + 5x - 1$

![[video-ej3-uv.png]]

### Paso 3: Verificar ecuacion (1) de Cauchy-Riemann

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$

Calculamos:

$$\frac{\partial u}{\partial x} = 2x$$

$$\frac{\partial v}{\partial y} = 2x$$

$$2x = 2x \quad \checkmark$$

![[video-ej3-ecuacion1.png]]

### Paso 4: Verificar ecuacion (2) de Cauchy-Riemann

$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

Calculamos:

$$\frac{\partial u}{\partial y} = -2y - 5$$

$$-\frac{\partial v}{\partial x} = -(2y + 5) = -2y - 5$$

$$-2y - 5 = -2y - 5 \quad \checkmark$$

### Conclusion

Como ambas ecuaciones de Cauchy-Riemann se satisfacen, la derivada $f'(z)$ **existe**.

![[video-ej3-resultado.png]]
