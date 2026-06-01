---
title: "Conclusiones semana 10 — Series de Maclaurin y Laurent"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 10
orden: 5
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/series-de-maclaurin
  - tema/series-de-laurent
date: 2026-05-31
---

## Cierre

La semana 10 completa el bloque de series: la **serie de Maclaurin** (caso $z_0=0$ de [[S09-0 Tema 01 - Series de Taylor en numeros complejos|Taylor]], para funciones analíticas en el origen) y la **serie de Laurent** (para funciones con singularidades, válida en un **anillo** y con potencias negativas). Lo más importante: la serie de Laurent **conecta con las integrales de contorno** — el coeficiente de $(z-z_0)^{-1}$ es el residuo, y $\oint_C f\,dz = 2\pi i\,c_{-1}$.

## Resumen de la semana

> [!summary] Serie de Maclaurin
> $$f(z) = \sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}z^n \qquad (|z| < R_0)$$

> [!summary] Serie de Laurent (anillo $R_1<|z-z_0|<R_2$)
> $$f(z) = \sum_{n=-\infty}^{\infty} c_n(z-z_0)^n, \qquad c_n = \frac{1}{2\pi i}\oint_C\frac{f(z)\,dz}{(z-z_0)^{n+1}}$$
> Parte analítica ($n\geq 0$) + parte principal ($n<0$, delata la singularidad).

> [!summary] Integral por Laurent
> $$\oint_C f(z)\,dz = 2\pi i\,c_{-1} = 2\pi i\sum_{\text{polos interiores}}\operatorname{Res}_{z_k} f$$

## Técnicas aprendidas

| Técnica | Ejemplo | Nota |
| ------- | ------- | ---- |
| Maclaurin por serie geométrica (más rápido que derivar) | $\dfrac{z}{z+9}$ | [[S10-1 Tema 01 - Maclaurin Ej1 - z sobre (z+9)\|Ej 1]] |
| Elegir el anillo y forzar $\frac{1}{1-w}$ según $\|z\|\gtrless r$ | $\dfrac{-1}{(z-1)(z-2)}$ | [[S10-2 Tema 01 - Laurent Ej2 - region anular -1 sobre (z-1)(z-2)\|Ej 2]] |
| Fracciones parciales para separar singularidades | $\dfrac{-1}{(z-1)(z-2)}$, $\dfrac{z+1}{z(z-2)}$ | [[S10-2 Tema 01 - Laurent Ej2 - region anular -1 sobre (z-1)(z-2)\|Ej 2]], [[S10-4 Tema 01 - Integral Ej4 - (z+1) sobre (z2-2z)\|Ej 4]] |
| Aislar el coeficiente de $(z-z_0)^{-1}$ para integrar | $\oint\frac{5z-2}{z(z-1)}dz$ | [[S10-3 Tema 01 - Integral Ej3 - 5z-2 sobre z(z-1)\|Ej 3]] |
| Sumar contribuciones de varias singularidades interiores | $\oint_{\|z\|=3}\frac{z+1}{z^2-2z}dz$ | [[S10-4 Tema 01 - Integral Ej4 - (z+1) sobre (z2-2z)\|Ej 4]] |

## Notas de la semana

- [[S10-0 Tema 01 - Series de Maclaurin y Laurent|Teoría — Maclaurin, Laurent y conexión con integrales]]
- [[S10-1 Tema 01 - Maclaurin Ej1 - z sobre (z+9)|Ej 1 — Maclaurin de $\frac{z}{z+9}$ → $\sum (-1)^{n-1}z^n/9^n$]]
- [[S10-2 Tema 01 - Laurent Ej2 - region anular -1 sobre (z-1)(z-2)|Ej 2 — Laurent de $\frac{-1}{(z-1)(z-2)}$ en $1<|z|<2$]]
- [[S10-3 Tema 01 - Integral Ej3 - 5z-2 sobre z(z-1)|Ej 3 — $\oint\frac{5z-2}{z(z-1)}dz = 10\pi i$]]
- [[S10-4 Tema 01 - Integral Ej4 - (z+1) sobre (z2-2z)|Ej 4 — $\oint_{|z|=3}\frac{z+1}{z^2-2z}dz = 2\pi i$]]

## Evaluación de la semana

> [!danger] Actividad calificada — PA04 (vence hoy)
> 🔴 (AC-S10) **Participación Académica 4 (PA04)** — calificada. Subir un PDF con 5 ejercicios (Taylor, Laurent, Laurent, Taylor, Maclaurin). Plazo: lunes **25 mayo** → domingo **31 mayo 2026, 23:59**. Enunciados y desarrollo completo en [[S10-98 PA04 Enunciados y desarrollo]]; metadatos en [[S10-99 PA04 sem 10]].

## Próxima semana

La semana 11 continúa con la **Unidad 3** del curso, aplicando residuos y abriendo el bloque de **transformadas** (Fourier / Laplace), donde las series complejas se usan como herramienta de representación y resolución.
