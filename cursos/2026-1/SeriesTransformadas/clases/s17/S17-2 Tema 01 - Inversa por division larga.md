---
title: "Ejercicio 1 — Transformada Z inversa por división larga (Fibonacci)"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 17
orden: 2
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/transformada-z-inversa
  - tema/division-larga
date: 2026-07-13
---

## Enunciado

> [!question] Problema
> Sea la ecuación de la **sucesión de Fibonacci** $y_{n+2} = y_{n+1} + y_n$, con $y_0 = 1$ y $y_1 = 1$. Encontrar una expresión para $y_n$ aplicando la transformada Z y su inversa, usando el **método de la división larga**.

Fuente: [[T01-DivisionLarga-Guion.pdf|Guion del video — Métodos de transformada inversa]].

## Desarrollo

### Paso 1 — Aplicar la transformada Z (con condiciones iniciales)

Usando la propiedad de adelanto unilateral:
$$\mathcal{Z}\{y_{n+2}\} = z^2 Y(z) - z^2 y_0 - z\,y_1,\qquad \mathcal{Z}\{y_{n+1}\} = zY(z) - z\,y_0$$

Sustituyendo $y_0 = 1$, $y_1 = 1$:

$$z^2 Y(z) - z^2 - z = \bigl(zY(z) - z\bigr) + Y(z)$$

### Paso 2 — Despejar $Y(z)$

$$z^2 Y - zY - Y = z^2 + z - z = z^2$$
$$Y(z)\,(z^2 - z - 1) = z^2 \qquad\Longrightarrow\qquad Y(z) = \frac{z^2}{z^2 - z - 1}$$

### Paso 3 — División larga

Dividiendo (en potencias de $z^{-1}$) $\dfrac{1}{1 - z^{-1} - z^{-2}}$:

$$Y(z) = 1 + z^{-1} + 2z^{-2} + 3z^{-3} + 5z^{-4} + 8z^{-5} + \cdots$$

### Resultado

Los coeficientes de $z^{-n}$ son los valores $y_n$:

> [!success] Resultado
> $$\boxed{\;y_n = \{\,1,\ 1,\ 2,\ 3,\ 5,\ 8,\ 13,\ \ldots\,\}\;}$$
> es decir, la **sucesión de Fibonacci** (cada término es la suma de los dos anteriores).

> [!note] Sobre el método
> La división larga entrega los $y_n$ **uno a uno** (no una fórmula cerrada). Es útil para obtener los primeros términos rápidamente; para la forma cerrada conviene fracciones parciales (los polos $z = \frac{1\pm\sqrt5}{2}$ dan la fórmula de Binet).

## Conceptos aplicados

- [[S17-1 Tema 01 - Transformada Z Parte 2#2. Transformada Z inversa|Método de división larga]].
- [[S16-1 Tema 01 - Transformada Z#3. Propiedades de la transformada Z|Propiedad de desplazamiento (adelanto)]].

## Bibliografía

- Mitra, S. K. (2007). *Procesamiento de Señales Digitales* (3.ª ed.). McGraw-Hill. México.
