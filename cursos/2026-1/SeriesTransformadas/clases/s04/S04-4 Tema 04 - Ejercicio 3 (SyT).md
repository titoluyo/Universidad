---
title: "Ejercicio 3 - Encontrar la conjugada armonica de u = x^2 - y^2 - y"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 4
orden: 4
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/funcion-armonica-conjugada
  - tema/cauchy-riemann
date: 2026-04-19
---

## Enunciado

Sea $u(x, y)$ una funcion armonica en todo el plano complejo. Encontrar una **funcion armonica conjugada** $v(x, y)$ de:

$$u(x, y) = x^2 - y^2 - y$$

## Referencia teorica

Ver [[S04-1 Tema 04 - Funciones analiticas, holomorfas y armonicas#5. Funcion armonica conjugada|definicion de conjugada armonica]] y el [[S04-1 Tema 04 - Funciones analiticas, holomorfas y armonicas#Metodo para encontrar la conjugada armonica|metodo de integracion sucesiva]]:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

## Paso 1: Verificar que $u$ es armonica

Calculamos las segundas derivadas parciales:

$$\frac{\partial u}{\partial x} = 2x \;\Rightarrow\; \frac{\partial^2 u}{\partial x^2} = 2$$

$$\frac{\partial u}{\partial y} = -2y - 1 \;\Rightarrow\; \frac{\partial^2 u}{\partial y^2} = -2$$

Aplicando la ecuacion de Laplace:

$$\nabla^2 u = 2 + (-2) = 0 \checkmark$$

Por tanto, $u$ es armonica en todo $\mathbb{C}$.

## Paso 2: Plantear las ecuaciones de Cauchy-Riemann

Queremos hallar $v(x, y)$ tal que:

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \;\Rightarrow\; \frac{\partial v}{\partial y} = 2x \quad (1)$$

$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x} \;\Rightarrow\; -\frac{\partial v}{\partial x} = -2y - 1 \;\Rightarrow\; \frac{\partial v}{\partial x} = 2y + 1 \quad (2)$$

## Paso 3: Integrar (1) respecto a $y$

De $\dfrac{\partial v}{\partial y} = 2x$, integrando respecto a $y$ (tratando $x$ como constante):

$$v(x, y) = \int 2x\, dy = 2xy + h(x) \quad (3)$$

donde $h(x)$ es una funcion arbitraria de $x$ a determinar.

## Paso 4: Derivar (3) respecto a $x$ y comparar con (2)

Derivando (3) respecto a $x$:

$$\frac{\partial v}{\partial x} = 2y + h'(x)$$

Comparando con la ecuacion (2):

$$2y + h'(x) = 2y + 1$$

$$\Rightarrow h'(x) = 1$$

## Paso 5: Integrar $h'(x)$

$$h(x) = \int 1\, dx = x + C$$

donde $C$ es una constante real arbitraria.

## Paso 6: Construir $v(x, y)$

Sustituyendo $h(x) = x + C$ en (3):

$$\boxed{v(x, y) = 2xy + x + C}$$

## Verificacion

Comprobamos que $v$ tambien es armonica:

$$v_x = 2y + 1, \quad v_y = 2x$$

$$v_{xx} = 0, \quad v_{yy} = 0$$

$$\nabla^2 v = 0 + 0 = 0 \checkmark$$

Y que se cumplen las ecuaciones de Cauchy-Riemann:

- $u_x = 2x = v_y$ ✓
- $u_y = -2y - 1 = -(2y + 1) = -v_x$ ✓

## Conclusion

La conjugada armonica de $u(x, y) = x^2 - y^2 - y$ es:

$$v(x, y) = 2xy + x + C$$

La funcion compleja analitica correspondiente es:

$$f(z) = u(x, y) + i\,v(x, y) = (x^2 - y^2 - y) + i(2xy + x + C)$$

Usando que $z^2 = (x^2 - y^2) + i(2xy)$ y $iz = -y + ix$:

$$f(z) = z^2 + iz + iC$$

> [!tip] Interpretacion
> Como $z^2$ y $iz$ son analiticas en todo $\mathbb{C}$, la funcion $f(z) = z^2 + iz + iC$ es analitica en todo el plano. La constante $C$ refleja la no-unicidad de la conjugada armonica: esta definida **salvo una constante real aditiva**.

## Bibliografia

- Churchill, R., & Ward, J. (2004). *Variable Compleja y Aplicaciones* (7ma ed.). McGraw-Hill.
