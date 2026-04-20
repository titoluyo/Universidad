---
title: "Ejercicio 1 - Probar que f(z) = (y^3 - 3x^2 y) + i(x^3 - 3xy^2 + 3) es armonica"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 4
orden: 2
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/funcion-armonica
  - tema/ecuacion-laplace
date: 2026-04-19
---

## Enunciado

Sea la funcion compleja:

$$f(z) = (y^3 - 3x^2y) + i(x^3 - 3xy^2 + 3)$$

Demostrar que es una **funcion armonica**, es decir, que sus componentes $u(x, y)$ y $v(x, y)$ satisfacen las ecuaciones de Laplace.

## Referencia teorica

Ver [[S04-1 Tema 04 - Funciones analiticas, holomorfas y armonicas#4. Funcion armonica|definicion de funcion armonica]]: una funcion $f(z) = u + iv$ es armonica si sus componentes satisfacen

$$\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0, \qquad \nabla^2 v = \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} = 0$$

## Paso 1: Identificar las componentes

Separando parte real e imaginaria:

$$u(x, y) = y^3 - 3x^2 y$$

$$v(x, y) = x^3 - 3xy^2 + 3$$

## Paso 2: Verificar que $u(x, y)$ es armonica

Calculamos las derivadas parciales de primer orden:

$$\frac{\partial u}{\partial x} = -6xy$$

$$\frac{\partial u}{\partial y} = 3y^2 - 3x^2$$

Derivadas parciales de segundo orden:

$$\frac{\partial^2 u}{\partial x^2} = -6y$$

$$\frac{\partial^2 u}{\partial y^2} = 6y$$

Aplicando la ecuacion de Laplace:

$$\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = -6y + 6y = 0 \checkmark$$

Por tanto, $u(x, y) = y^3 - 3x^2y$ es armonica en $\mathbb{C}$.

## Paso 3: Verificar que $v(x, y)$ es armonica

Calculamos las derivadas parciales de primer orden:

$$\frac{\partial v}{\partial x} = 3x^2 - 3y^2$$

$$\frac{\partial v}{\partial y} = -6xy$$

Derivadas parciales de segundo orden:

$$\frac{\partial^2 v}{\partial x^2} = 6x$$

$$\frac{\partial^2 v}{\partial y^2} = -6x$$

Aplicando la ecuacion de Laplace:

$$\nabla^2 v = \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} = 6x + (-6x) = 0 \checkmark$$

Por tanto, $v(x, y) = x^3 - 3xy^2 + 3$ es armonica en $\mathbb{C}$.

## Paso 4: Verificar las ecuaciones de Cauchy-Riemann

Ademas de ser ambas armonicas, verifiquemos si $u$ y $v$ satisfacen Cauchy-Riemann (para determinar si $f$ es analitica):

- $u_x = -6xy$ y $v_y = -6xy$ → $u_x = v_y$ ✓
- $u_y = 3y^2 - 3x^2$ y $-v_x = -(3x^2 - 3y^2) = 3y^2 - 3x^2$ → $u_y = -v_x$ ✓

Se cumplen las ecuaciones de Cauchy-Riemann y las derivadas son continuas, por lo que $f(z)$ tambien es **analitica** en todo $\mathbb{C}$.

## Conclusion

$$\boxed{f(z) = (y^3 - 3x^2y) + i(x^3 - 3xy^2 + 3) \text{ es una funcion armonica en } \mathbb{C}.}$$

Ademas, al cumplir las ecuaciones de Cauchy-Riemann con derivadas continuas, es **analitica en todo el plano complejo**, lo cual confirma que sus componentes deben ser armonicas (por el teorema fundamental de la seccion [[S04-1 Tema 04 - Funciones analiticas, holomorfas y armonicas#Teorema fundamental]]).

> [!info] Observacion
> La funcion $u + iv$ puede reescribirse como $f(z) = i(z^3 + 3)$. En efecto:
> $$i(z^3 + 3) = i[(x + iy)^3 + 3] = i[x^3 - 3xy^2 + i(3x^2y - y^3) + 3]$$
> $$= -(3x^2y - y^3) + i(x^3 - 3xy^2 + 3) = (y^3 - 3x^2y) + i(x^3 - 3xy^2 + 3)$$
> Como $z^3$ es analitica, multiplicarla por $i$ y sumar una constante preserva la analiticidad.

## Bibliografia

- Churchill, R., & Ward, J. (2004). *Variable Compleja y Aplicaciones* (7ma ed.). McGraw-Hill.
