---
title: "Ejercicio 1 — Transformada Z de aⁿ·u(n) (secuencia exponencial)"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 16
orden: 2
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
> Determinar la transformada Z de $x(n) = a^n\,u(n)$, donde $u(n)$ es la función escalón unitario discreto.

Fuente: [[T01-Ej1-Guion.pdf|Guion del video — Transformada Z de una función I]].

## Desarrollo

### Paso 1 — Aplicar la definición

$$X(z) = \sum_{n=-\infty}^{+\infty} x(n)\,z^{-n} = \sum_{n=-\infty}^{+\infty} a^n\,u(n)\,z^{-n}$$

El escalón $u(n)$ indica **desde dónde** arranca la sumatoria: como $u(n)=1$ para $n\ge 0$, el límite inferior pasa a ser $n=0$ y $u(n)$ deja de escribirse:

$$X(z) = \sum_{n=0}^{\infty} a^n\,z^{-n}$$

### Paso 2 — Factorizar y reconocer la serie geométrica

$$X(z) = \sum_{n=0}^{\infty} \left(a\,z^{-1}\right)^n$$

Es una **serie geométrica** de razón $r = a z^{-1}$. Usando $\displaystyle\sum_{n=0}^{\infty} r^n = \frac{1}{1-r}$ (válido para $|r|<1$):

> [!success] Resultado
> $$\boxed{\;X(z) = \frac{1}{1 - a\,z^{-1}} = \frac{z}{z - a}\;}$$
> con **región de convergencia** $|z| > |a|$.

> [!note] Idea clave
> Calcular una transformada Z consiste en **partir de la sumatoria** de la definición y llevarla a una **forma geométrica cerrada**, aplicando la propiedad de desplazamiento (el escalón fija el inicio de la suma).

## Conceptos aplicados

- [[S16-1 Tema 01 - Transformada Z#1. Definición|Definición de la transformada Z]].
- [[S16-1 Tema 01 - Transformada Z#2. Herramienta básica: serie geométrica|Serie geométrica]].

## Bibliografía

- Mitra, S. K. (2007). *Procesamiento de Señales Digitales* (3.ª ed.). McGraw-Hill. México.
