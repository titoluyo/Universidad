---
title: "Conclusiones semana 13 — Teorema de Parseval"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 13
orden: 3
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/teorema-de-parseval
  - tema/series-de-fourier
date: 2026-06-15
---

## Cierre

La semana 13 cierra la **Unidad 2** con el **teorema de Parseval**: la energía (potencia promedio) de una señal periódica es igual a la suma de las energías de sus componentes armónicas. Además de su valor conceptual (conexión tiempo–frecuencia), es una herramienta poderosa para **sumar series numéricas** que de otro modo serían difíciles de evaluar.

## Resumen de la semana

> [!summary] Identidad de Parseval
> $$\frac{1}{T}\int_{-T/2}^{T/2}\bigl[f(t)\bigr]^2 dt = \frac{a_0^2}{4} + \frac{1}{2}\sum_{n=1}^{\infty}\bigl(a_n^2 + b_n^2\bigr)$$
> Potencia media de la señal = suma de potencias del término DC y de cada armónico.

> [!tip] Estrategia para sumar series
> 1. Expandir $f(t)$ en serie de Fourier (usar paridad para anular coeficientes).
> 2. Aplicar Parseval.
> 3. Calcular $\frac{1}{T}\int[f]^2 dt$ por integral directa y despejar la serie.

## Técnicas aprendidas

| Técnica | Ejemplo | Nota |
| ------- | ------- | ---- |
| Demostración de Parseval desde el error cuadrático | sucesión $E_k$ no creciente $\to 0$ | [[S13-0 Tema 01 - Teorema de Parseval\|Teoría]] |
| Parseval con función impar (solo senos) | $f(x)=x \Rightarrow \sum\tfrac{1}{n^2}=\tfrac{\pi^2}{6}$ | [[S13-1 Tema 01 - Ejercicio 1 - Parseval prueba suma 1 sobre n cuadrado\|Ej 1]] |
| Parseval con función par (solo cosenos impares) | $f(x)=1+\lvert x\rvert \Rightarrow \sum\tfrac{1}{(2n-1)^4}=\tfrac{\pi^4}{96}$ | [[S13-2 Tema 01 - Ejercicio 2 - Parseval convergencia 1 sobre (2n-1) cuarta\|Ej 2]] |

## Notas de la semana

- [[S13-0 Tema 01 - Teorema de Parseval|Teoría — Identidad de Parseval y demostración]]
- [[S13-1 Tema 01 - Ejercicio 1 - Parseval prueba suma 1 sobre n cuadrado|Ej 1 — $\sum 1/n^2 = \pi^2/6$ (problema de Basilea)]]
- [[S13-2 Tema 01 - Ejercicio 2 - Parseval convergencia 1 sobre (2n-1) cuarta|Ej 2 — $\sum 1/(2n-1)^4 = \pi^4/96$]]

## Evaluación de la semana

> [!danger] Práctica Calificada 2 (PC02) — calificada
> Actividad **calificada** 🔴, programada del **viernes 19** al **domingo 21 de junio de 2026** (23:59). 1 intento, ~60 min, vigesimal. Cubre **toda la Unidad 2**: convergencia, serie de Laurent, determinación/expansión de serie de Fourier, y aproximación finita + error cuadrático. Ver [[S13-99 PC02 sem 13|indicaciones y metadatos]].

## Próxima semana

La semana 14 abre la **Unidad 3 — Transformadas**, comenzando con la **Transformada de Laplace**.
