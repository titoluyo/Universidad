---
title: "Ejercicio 2 — Transformada Z de (1/5)ⁿ·u(n−3) (desplazamiento)"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 16
orden: 3
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/transformada-z
  - tema/serie-geometrica
date: 2026-07-06
---

## Enunciado

> [!question] Problema
> Determinar la transformada Z de $x(n) = \left(\tfrac{1}{5}\right)^n u(n-3)$.

Fuente: [[T01-Ej2-Guion.pdf|Guion del video — Transformada Z de una función II]].

## Desarrollo

### Paso 1 — Aplicar la definición y el desplazamiento

$$X(z) = \sum_{n=-\infty}^{+\infty} \left(\tfrac{1}{5}\right)^n u(n-3)\,z^{-n}$$

El escalón **desplazado** $u(n-3)$ obliga a iniciar la sumatoria en $n=3$:

$$X(z) = \sum_{n=3}^{\infty} \left(\tfrac{1}{5}\right)^n z^{-n} = \sum_{n=3}^{\infty}\left(\tfrac{1}{5}z^{-1}\right)^n$$

### Paso 2 — Serie geométrica que empieza en $n=3$

Usando $\displaystyle\sum_{n=N_1}^{\infty} r^n = \frac{r^{N_1}}{1-r}$ con $r = \tfrac15 z^{-1}$ y $N_1 = 3$:

$$X(z) = \frac{\left(\tfrac15 z^{-1}\right)^3}{1 - \tfrac15 z^{-1}}$$

### Resultado

Como $\left(\tfrac15\right)^3 = \tfrac{1}{125}$:

> [!success] Resultado
> $$\boxed{\;X(z) = \frac{\frac{1}{125}\,z^{-3}}{1 - \frac{1}{5}z^{-1}}\;}$$
> con región de convergencia $|z| > \tfrac15$.

> [!tip] Efecto del desplazamiento
> Comparado con el [[S16-2 Tema 01 - Ejercicio 1 - Transformada Z de a elevado n por u(n)|Ej 1]], el desplazamiento $u(n-3)$ introduce el factor $z^{-3}$ (propiedad de **desplazamiento en el tiempo**) y cambia el inicio de la serie geométrica.

## Conceptos aplicados

- [[S16-1 Tema 01 - Transformada Z#3. Propiedades de la transformada Z|Propiedad de desplazamiento en el tiempo]].
- [[S16-1 Tema 01 - Transformada Z#2. Herramienta básica: serie geométrica|Serie geométrica (desde $N_1$)]].

## Bibliografía

- Mitra, S. K. (2007). *Procesamiento de Señales Digitales* (3.ª ed.). McGraw-Hill. México.
