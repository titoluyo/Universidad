---
title: "Ejercicio 2 - Probar que u = e^(-x)(x sen y - y cos y) es armonica"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 4
orden: 3
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/funcion-armonica
  - tema/ecuacion-laplace
date: 2026-04-19
---

## Enunciado

Demostrar que la funcion:

$$u(x, y) = e^{-x}(x \operatorname{sen} y - y \cos y)$$

es una **funcion armonica**, es decir, que cumple con la ecuacion de Laplace:

$$\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$

## Paso 1: Primera derivada respecto a $x$

Aplicamos la regla del producto (tratando $x \operatorname{sen} y - y \cos y$ como un factor y $e^{-x}$ como otro):

$$\frac{\partial u}{\partial x} = \frac{\partial}{\partial x}\left[e^{-x}(x \operatorname{sen} y - y \cos y)\right]$$

$$= (-e^{-x})(x \operatorname{sen} y - y \cos y) + e^{-x}(\operatorname{sen} y)$$

Reagrupando:

$$\frac{\partial u}{\partial x} = e^{-x} \operatorname{sen} y - e^{-x} x \operatorname{sen} y + e^{-x} y \cos y$$

## Paso 2: Segunda derivada respecto a $x$

Derivamos cada termino de $u_x$ respecto a $x$:

- $\dfrac{\partial}{\partial x}(e^{-x}\operatorname{sen} y) = -e^{-x}\operatorname{sen} y$
- $\dfrac{\partial}{\partial x}(-e^{-x} x \operatorname{sen} y) = e^{-x}x \operatorname{sen} y - e^{-x}\operatorname{sen} y$
- $\dfrac{\partial}{\partial x}(e^{-x} y \cos y) = -e^{-x} y \cos y$

Sumando:

$$\frac{\partial^2 u}{\partial x^2} = -e^{-x}\operatorname{sen} y + e^{-x}x \operatorname{sen} y - e^{-x}\operatorname{sen} y - e^{-x} y \cos y$$

Agrupando:

$$\boxed{\frac{\partial^2 u}{\partial x^2} = -2e^{-x}\operatorname{sen} y + x e^{-x}\operatorname{sen} y - e^{-x} y \cos y \quad (1)}$$

## Paso 3: Primera derivada respecto a $y$

$$\frac{\partial u}{\partial y} = \frac{\partial}{\partial y}\left[e^{-x}(x \operatorname{sen} y - y \cos y)\right]$$

Como $e^{-x}$ no depende de $y$:

$$= e^{-x}\left[x \cos y - (\cos y - y \operatorname{sen} y)\right] = e^{-x}(x \cos y - \cos y + y \operatorname{sen} y)$$

## Paso 4: Segunda derivada respecto a $y$

$$\frac{\partial^2 u}{\partial y^2} = e^{-x}\frac{\partial}{\partial y}(x \cos y - \cos y + y \operatorname{sen} y)$$

$$= e^{-x}(-x \operatorname{sen} y + \operatorname{sen} y + \operatorname{sen} y + y \cos y)$$

$$= e^{-x}(-x \operatorname{sen} y + 2 \operatorname{sen} y + y \cos y)$$

Agrupando:

$$\boxed{\frac{\partial^2 u}{\partial y^2} = -x e^{-x}\operatorname{sen} y + 2 e^{-x}\operatorname{sen} y + e^{-x} y \cos y \quad (2)}$$

## Paso 5: Suma de (1) + (2)

$$\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}$$

Sustituyendo (1) y (2):

$$\nabla^2 u = \underbrace{\left(-2e^{-x}\operatorname{sen} y + x e^{-x}\operatorname{sen} y - e^{-x} y \cos y\right)}_{(1)} + \underbrace{\left(-x e^{-x}\operatorname{sen} y + 2 e^{-x}\operatorname{sen} y + e^{-x} y \cos y\right)}_{(2)}$$

Agrupando terminos semejantes:

- Terminos con $\operatorname{sen} y$ (sin $x$): $-2e^{-x}\operatorname{sen} y + 2e^{-x}\operatorname{sen} y = 0$
- Terminos con $x \operatorname{sen} y$: $xe^{-x}\operatorname{sen} y - xe^{-x}\operatorname{sen} y = 0$
- Terminos con $y \cos y$: $-e^{-x}y\cos y + e^{-x}y\cos y = 0$

Por tanto:

$$\nabla^2 u = 0 \checkmark$$

## Conclusion

$$\boxed{u(x, y) = e^{-x}(x \operatorname{sen} y - y \cos y) \text{ es una funcion armonica en } \mathbb{C}.}$$

> [!info] Nota
> Esta funcion es la parte real de $f(z) = -i z e^{-z}$ (o equivalente). Al ser armonica en todo el plano, existe una conjugada armonica $v(x, y)$ tal que $u + iv$ es analitica — ver [[S04-1 Tema 04 - Funciones analiticas, holomorfas y armonicas#Teorema de existencia|teorema de existencia]].

## Bibliografia

- Churchill, R., & Ward, J. (2004). *Variable Compleja y Aplicaciones* (7ma ed.). McGraw-Hill.
