---
title: "Conclusiones semana 11 — Series de Fourier"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 11
orden: 5
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/series-de-fourier
  - tema/senales-periodicas
date: 2026-06-01
---

## Cierre

La semana 11 abre el bloque de **series de Fourier**: la representación de una función **periódica** como suma infinita de senos y cosenos. Primero se caracterizan las señales por su **periodicidad** y **paridad** (semana clave porque la paridad anula la mitad de los coeficientes), y luego se construyen los coeficientes usando la **ortogonalidad** de las funciones trigonométricas.

## Resumen de la semana

> [!summary] Serie trigonométrica de Fourier
> $$f(t) = \frac{1}{2}a_0 + \sum_{n=1}^{\infty}\bigl(a_n\cos n\omega t + b_n\sin n\omega t\bigr), \qquad \omega = \frac{2\pi}{T}$$

> [!summary] Coeficientes (vía ortogonalidad)
> $$a_0 = \frac{2}{T}\int_{-T/2}^{T/2} f(t)\,dt, \quad a_n = \frac{2}{T}\int_{-T/2}^{T/2} f(t)\cos n\omega t\,dt, \quad b_n = \frac{2}{T}\int_{-T/2}^{T/2} f(t)\sin n\omega t\,dt$$

> [!tip] La paridad ahorra trabajo
> - $f$ **par** → $b_n = 0$ (serie de **cosenos**).
> - $f$ **impar** → $a_0 = a_n = 0$ (serie de **senos**).

## Técnicas aprendidas

| Técnica | Ejemplo | Nota |
| ------- | ------- | ---- |
| Periodo de una suma de armónicos (mínimo común) | $\cos\tfrac{t}{3} + \cos\tfrac{t}{4} \Rightarrow T = 24\pi$ | [[S11-1 Tema 01 - Ejercicio 1 - periodo de cos(t3) + cos(t4)\|Ej 1]] |
| Paridad impar $\Rightarrow$ solo senos | onda cuadrada y triangular | [[S11-3 Tema 02 - Series de Fourier Ejercicio 1 - onda cuadrada\|Ej 1]], [[S11-4 Tema 02 - Series de Fourier Ejercicio 2 - onda triangular\|Ej 2]] |
| Patrón $1 - (-1)^n$ $\Rightarrow$ solo armónicos impares | onda cuadrada $\to b_n = \tfrac{4}{n\pi}$ | [[S11-3 Tema 02 - Series de Fourier Ejercicio 1 - onda cuadrada\|Ej 1]] |
| Integración por partes + cancelación de tramos | onda triangular $\to b_n = \tfrac{8k}{(n\pi)^2}\sin\tfrac{n\pi}{2}$ | [[S11-4 Tema 02 - Series de Fourier Ejercicio 2 - onda triangular\|Ej 2]] |
| Decaimiento de amplitudes según suavidad ($1/n$ vs $1/n^2$) | cuadrada vs triangular | [[S11-4 Tema 02 - Series de Fourier Ejercicio 2 - onda triangular\|Ej 2]] |

## Notas de la semana

- [[S11-0 Tema 01 - Senales periodicas, pares e impares|Teoría — Señales periódicas, pares e impares]]
- [[S11-1 Tema 01 - Ejercicio 1 - periodo de cos(t3) + cos(t4)|Ej 1 — Periodo de $\cos\tfrac{t}{3}+\cos\tfrac{t}{4} = 24\pi$]]
- [[S11-2 Tema 02 - Series de Fourier|Teoría — Series de Fourier, ortogonalidad y coeficientes]]
- [[S11-3 Tema 02 - Series de Fourier Ejercicio 1 - onda cuadrada|Ej 1 — Onda cuadrada $\to \tfrac{4}{n\pi}\sin n\omega t$ (impares)]]
- [[S11-4 Tema 02 - Series de Fourier Ejercicio 2 - onda triangular|Ej 2 — Onda triangular $\to \tfrac{8k}{(n\pi)^2}\sin\tfrac{n\pi}{2}$]]

## Evaluación de la semana

> [!info] Evaluación no calificada (cuestionario)
> Cuestionario sobre series de Fourier. Plazo: lunes **1 junio** → domingo **7 junio 2026** 23:59. Ver [[S11-99 Evaluacion sem 11|metadatos]].

## Próxima semana

La semana 12 continúa con **series de Fourier de medio rango**, las **aproximaciones finitas** (sumas parciales), el **fenómeno de Gibbs** (el sobreimpulso cerca de las discontinuidades, visible justamente en la onda cuadrada del Ej 1) y el **error cuadrático medio**.
