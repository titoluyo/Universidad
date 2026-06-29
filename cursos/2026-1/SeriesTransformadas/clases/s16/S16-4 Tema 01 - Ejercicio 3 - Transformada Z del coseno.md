---
title: "Ejercicio 3 — Transformada Z de cos(ωt) (vía identidad de Euler)"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 16
orden: 4
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
> Calcular la transformada Z de $f(t) = \cos\omega t$.

## Desarrollo

### Paso 1 — Discretizar ($t = nT$)

Para obtener la versión discreta hacemos el cambio $t = nT$:

$$X(z) = \sum_{n=0}^{\infty} \cos(\omega nT)\,z^{-n} = 1 + \cos\omega T\,z^{-1} + \cos 2\omega T\,z^{-2} + \cos 3\omega T\,z^{-3} + \cdots$$

### Paso 2 — Identidad de Euler

$$\cos x = \frac{e^{ix} + e^{-ix}}{2}$$

### Paso 3 — Sustituir y aplicar linealidad

$$X(z) = \sum_{n=0}^{\infty} \left(\frac{e^{i\omega nT} + e^{-i\omega nT}}{2}\right)z^{-n} = \frac{1}{2}\sum_{n=0}^{\infty}\left(e^{i\omega T}z^{-1}\right)^n + \frac{1}{2}\sum_{n=0}^{\infty}\left(e^{-i\omega T}z^{-1}\right)^n$$

### Pasos 4–5 — Resolver cada serie geométrica

$$\frac{1}{2}\sum_{n=0}^{\infty}\left(e^{i\omega T}z^{-1}\right)^n = \frac{1}{2}\frac{z}{z - e^{i\omega T}};\qquad \frac{1}{2}\sum_{n=0}^{\infty}\left(e^{-i\omega T}z^{-1}\right)^n = \frac{1}{2}\frac{z}{z - e^{-i\omega T}}$$

### Paso 6 — Combinar y simplificar

$$X(z) = \frac{z}{2}\left[\frac{1}{z - e^{i\omega T}} + \frac{1}{z - e^{-i\omega T}}\right] = \frac{z}{2}\left[\frac{2z - \left(e^{i\omega T} + e^{-i\omega T}\right)}{z^2 - z\left(e^{i\omega T} + e^{-i\omega T}\right) + 1}\right]$$

Usando $e^{i\omega T} + e^{-i\omega T} = 2\cos\omega T$:

> [!success] Resultado
> $$\boxed{\;X(z) = \frac{z\,(z - \cos\omega T)}{z^2 - 2z\cos\omega T + 1}\;}$$

> [!note] Observación
> Es la transformada Z estándar del coseno discreto. El denominador $z^2 - 2z\cos\omega T + 1$ tiene polos en $e^{\pm i\omega T}$ (sobre el círculo unitario), lo que corresponde a una oscilación sostenida.

## Conceptos aplicados

- [[S16-1 Tema 01 - Transformada Z#1. Definición|Definición de la transformada Z]].
- [[S16-1 Tema 01 - Transformada Z#3. Propiedades de la transformada Z|Linealidad]] + [[S16-1 Tema 01 - Transformada Z#2. Herramienta básica: serie geométrica|serie geométrica]].

## Bibliografía

- Mitra, S. K. (2007). *Procesamiento de Señales Digitales* (3.ª ed.). McGraw-Hill. México.
