---
title: "Ejercicio 4 - Demostrar que f(z) = xy + iy no es analitica en ningun punto"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 4
orden: 5
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/funcion-analitica
  - tema/cauchy-riemann
date: 2026-04-19
---

## Enunciado

Demostrar que la funcion:

$$f(z) = xy + i\,y$$

**no es analitica en ningun punto** del plano complejo.

## Referencia teorica

Ver [[S04-1 Tema 04 - Funciones analiticas, holomorfas y armonicas#Condicion necesaria: Cauchy-Riemann|condicion de analiticidad]]: si las ecuaciones de Cauchy-Riemann no se satisfacen en todos los puntos de alguna vecindad de $z_0$, entonces $f$ no es analitica en $z_0$.

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

## Paso 1: Identificar las componentes real e imaginaria

La funcion se expresa como $f(z) = u(x, y) + i\,v(x, y)$ donde:

$$u(x, y) = xy$$

$$v(x, y) = y$$

## Paso 2: Calcular las derivadas parciales

Para $u(x, y) = xy$:

$$\frac{\partial u}{\partial x} = y, \qquad \frac{\partial u}{\partial y} = x$$

Para $v(x, y) = y$:

$$\frac{\partial v}{\partial x} = 0, \qquad \frac{\partial v}{\partial y} = 1$$

## Paso 3: Plantear las ecuaciones de Cauchy-Riemann

**Primera ecuacion:** $\dfrac{\partial u}{\partial x} = \dfrac{\partial v}{\partial y}$

$$y = 1 \quad (1)$$

**Segunda ecuacion:** $\dfrac{\partial u}{\partial y} = -\dfrac{\partial v}{\partial x}$

$$x = 0 \quad (2)$$

## Paso 4: Analizar las soluciones

Las ecuaciones (1) y (2) se cumplen **simultaneamente** solo si:

$$x = 0 \quad \text{y} \quad y = 1$$

Es decir, unicamente en el punto $z_0 = 0 + i \cdot 1 = i$.

> [!warning] Analiticidad requiere vecindad
> Aunque C-R se cumple en el punto aislado $z = i$, la funcion **no es analitica** ahi: para ser analitica en $z_0$, la derivada debe existir en todo punto de alguna vecindad de $z_0$. Como las ecuaciones de C-R fallan en cualquier punto cercano a $i$ (distinto de $i$), $f$ **no es derivable en ninguna vecindad** de $i$.

## Conclusion

Las ecuaciones de Cauchy-Riemann **no se cumplen simultaneamente en ningun abierto del plano complejo**. Por tanto:

$$\boxed{f(z) = xy + i\,y \text{ no es analitica en ningun punto del plano complejo.}}$$

A lo sumo, la derivada compleja $f'(z)$ podria existir en el punto aislado $z = i$, pero al no existir en una vecindad de dicho punto, $f$ no es analitica alli tampoco.

## Bibliografia

- Churchill, R., & Ward, J. (2004). *Variable Compleja y Aplicaciones* (7ma ed.). McGraw-Hill.
