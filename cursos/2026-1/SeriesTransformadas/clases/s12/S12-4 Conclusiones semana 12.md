---
title: "Conclusiones semana 12 — Análisis de las series de Fourier"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 12
orden: 4
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/series-de-fourier
  - tema/error-cuadratico-medio
  - tema/fenomeno-de-gibbs
date: 2026-06-08
---

## Cierre

La semana 12 profundiza en las [[S11-2 Tema 02 - Series de Fourier|series de Fourier]] con tres herramientas de análisis: las **series de medio rango** (para funciones definidas en un intervalo finito), las **aproximaciones finitas** con su **error cuadrático medio**, y el **fenómeno de Gibbs** (sobreoscilación en discontinuidades).

## Resumen de la semana

> [!summary] Series de medio rango (intervalo $(0,\tau)$, $T = 2\tau$)
> - **Cosenos** (extensión par): $f(t) = \tfrac{1}{2}a_0 + \sum a_n\cos\tfrac{n\pi t}{\tau}$, con $a_n = \tfrac{2}{\tau}\int_0^{\tau} f\cos\tfrac{n\pi t}{\tau}\,dt$.
> - **Senos** (extensión impar): $f(t) = \sum b_n\sin\tfrac{n\pi t}{\tau}$, con $b_n = \tfrac{2}{\tau}\int_0^{\tau} f\sin\tfrac{n\pi t}{\tau}\,dt$.

> [!summary] Error cuadrático medio (aproximación a $k$ términos)
> $$E_k = \frac{1}{T}\int_{-T/2}^{T/2}\bigl[f(t)\bigr]^2 dt - \frac{a_0^2}{4} - \frac{1}{2}\sum_{n=1}^{k}\bigl(a_n^2 + b_n^2\bigr)$$

> [!tip] Suavidad ⇒ convergencia rápida
> El error cuadrático decae más rápido cuanto **más suave** es la señal: discontinua → lento (Gibbs); continua → muy rápido.

## Técnicas aprendidas

| Técnica | Ejemplo | Nota |
| ------- | ------- | ---- |
| Expansión de medio rango en cosenos (extensión par) | escalón $0/1$ en $(0,\pi)$ | [[S12-1 Tema 01 - Ejercicio 1 - serie por expansion del coseno\|Ej 1]] |
| Paridad para anular coeficientes + por partes | $f(t)=t \Rightarrow b_n = \tfrac{2(-1)^{n+1}}{n}$ | [[S12-2 Tema 01 - Ejercicio 2 - error cuadratico de f(t) = t\|Ej 2]] |
| Error cuadrático medio vía Parseval truncada | $f(t)=t \Rightarrow E_5 \approx 0.363$ | [[S12-2 Tema 01 - Ejercicio 2 - error cuadratico de f(t) = t\|Ej 2]] |
| Integración por partes doble (recursión en $a_n$) | $A\lvert\sin\omega_0 t\rvert$ | [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado\|Ej 3]] |
| Comparación de convergencia según suavidad | $E_5$: $0.363$ vs $1.22\times10^{-4}A^2$ | [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado\|Ej 3]] |

## Notas de la semana

- [[S12-0 Tema 01 - Analisis de las series de Fourier|Teoría — Medio rango, error cuadrático y Gibbs]]
- [[S12-1 Tema 01 - Ejercicio 1 - serie por expansion del coseno|Ej 1 — Serie en cosenos (medio rango) del escalón $0/1$]]
- [[S12-2 Tema 01 - Ejercicio 2 - error cuadratico de f(t) = t|Ej 2 — Error cuadrático de $f(t)=t$ a 5 términos ($E_5\approx0.363$)]]
- [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|Ej 3 — Error cuadrático del seno rectificado ($E_5\approx1.22\times10^{-4}A^2$)]]

## Evaluación de la semana

> [!info] Sin evaluación calificada en el portal
> La semana 12 **no tiene cuestionario ni evaluación** en el portal (verificado en el tab Evaluaciones: "No tienes evaluaciones"). Solo incluye una **actividad interactiva (Storyline)** de autoevaluación de conceptos, sin nota.

## Próxima semana

La semana 13 cierra la Unidad 2 y trae la **Práctica Calificada 2 (PC02)** 🔴 — actividad calificada programada del **viernes 19** al **domingo 21 de junio de 2026** (23:59).
