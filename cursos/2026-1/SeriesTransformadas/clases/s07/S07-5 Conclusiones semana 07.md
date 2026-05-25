---
title: "Conclusiones semana 07 — Aplicación del teorema de Cauchy"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 7
orden: 5
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/cierre-de-unidad
date: 2026-05-10
---

## Cierre

La semana 7 cierra la **Unidad 1 — Funciones de variable compleja** del curso. Se aplicó el [[S06-3 Tema 06 - Teorema de Cauchy|teorema de Cauchy]] y su [[S06-6 Tema 06 - Teorema de extension de Cauchy|teorema de extensión]] (semana 6) a través de la **fórmula integral de Cauchy** y su generalización para derivadas, herramientas que permiten evaluar integrales de contorno con singularidades interiores sin parametrizar la curva.

## Ideas a retener

> [!summary] Fórmula integral de Cauchy (singularidad simple)
> $$\oint_C \frac{f(z)}{z - z_0}\,dz = 2\pi i\,f(z_0)$$
> Válida cuando $f$ es analítica dentro y sobre $C$, y $z_0$ es interior a $C$.

> [!summary] Fórmula integral generalizada (singularidad de orden $n+1$)
> $$\oint_C \frac{f(z)}{(z - z_0)^{n+1}}\,dz = \frac{2\pi i}{n!}\,f^{(n)}(z_0)$$
> Para $n = 0$ se recupera la fórmula simple.

> [!summary] Procedimiento
> 1. Identificar las **singularidades** ($h(z) = 0$).
> 2. Determinar **cuáles están dentro** del contorno.
> 3. Aislar el factor $(z - z_0)^{n+1}$ → leer $f(z)$ y el orden $n$.
> 4. Calcular $f^{(n)}(z_0)$ y sumar contribuciones de cada singularidad interior.

## Notas de la semana

- [[S07-0 Tema 01 - Relacion del teorema de Cauchy y una integral|Lectura base — Relación del teorema de Cauchy con una integral]]
- [[S07-1 Tema 01 - Aplicacion Caso 1 - integral con factor lineal|Caso 1 — dos singularidades simples + factor lineal con coeficiente]]
- [[S07-2 Tema 01 - Aplicacion Caso 2 - formula generalizada (derivadas)|Caso 2 — derivación de la fórmula generalizada (polo de orden 2)]]
- [[S07-3 Tema 01 - Aplicacion Caso 3 - fracciones parciales|Caso 3 — fracciones parciales con dos singularidades]]
- [[S07-4 Tema 01 - Aplicacion Caso 4 - formula generalizada e2z|Caso 4 — fórmula generalizada con $e^{2z}$ y polo de orden 4]]

## Evaluación de la semana

> [!warning] Práctica Calificada 1 (PC01)
> Esta semana cierra la unidad con la **PC01**, que evalúa los temas de las semanas 1–7. Plazo: viernes **8 mayo** → domingo **10 mayo 2026** a las 23:59. Ver [[S07-99 PC1 sem 07|consigna y metadatos]].

## Próxima unidad

La Unidad 2 (semana 8 en adelante) inicia con **series de potencias en variable compleja** — extensión natural a series infinitas de los conceptos vistos en esta primera unidad sobre funciones complejas y sus integrales.
