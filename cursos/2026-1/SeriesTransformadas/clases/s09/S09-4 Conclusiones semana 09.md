---
title: "Conclusiones semana 09 — Series de Taylor"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 9
orden: 4
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/series-de-taylor
date: 2026-05-24
---

## Cierre

La semana 9 desarrolla las **series de Taylor** como caso particular de las [[S08-0 Tema 01 - Series de potencias en complejos|series de potencias]] vistas en la semana 8 — donde los coeficientes se obtienen de las derivadas sucesivas de una función analítica evaluadas en un punto $z_0$.

## Resumen de la semana

> [!summary] Fórmula de Taylor
> $$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(z_0)}{n!}(z - z_0)^n$$

> [!summary] Caso particular: serie de Maclaurin ($z_0 = 0$)
> $$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}\,z^n$$

> [!summary] Procedimiento operativo
> 1. Identificar $f$ y centro $z_0$.
> 2. Calcular varias derivadas sucesivas.
> 3. Evaluar cada una en $z_0$.
> 4. Construir $a_n = f^{(n)}(z_0)/n!$ y simplificar.
> 5. Identificar patrón y escribir en forma de sumatoria.
> 6. Verificar radio de convergencia (distancia desde $z_0$ a la singularidad más cercana).

## Técnicas adicionales aprendidas

| Técnica | Ejemplo | Nota |
| ------- | ------- | ---- |
| Patrón de signos $(-1)^{n-1}$ con factoriales que se simplifican | $\ln(1+z)$ | [[S09-1 Tema 01 - Taylor Ej1 - logaritmo neperiano de (1+z)\|Ej 1]] |
| Reducir una función compuesta a partes conocidas con propiedades algebraicas | $\ln\!\left(\dfrac{1+z}{1-z}\right) = \ln(1+z) - \ln(1-z)$ | [[S09-2 Tema 01 - Taylor Ej2 - logaritmo de (1+z) sobre (1-z)\|Ej 2]] |
| Sustitución $z \mapsto g(z)$ en una serie conocida | $\ln(1-z)$ a partir de $\ln(1+z)$ | [[S09-2 Tema 01 - Taylor Ej2 - logaritmo de (1+z) sobre (1-z)\|Ej 2]] |
| Centro no nulo $z_0 \neq 0$ con patrón cíclico de derivadas | $\sin z$ alrededor de $\pi/4$ | [[S09-3 Tema 01 - Taylor Ej3 - sen(z) alrededor de pi cuartos\|Ej 3]] |
| Identidad trigonométrica como atajo a derivadas | $\sin(a+b)$ | [[S09-3 Tema 01 - Taylor Ej3 - sen(z) alrededor de pi cuartos\|Ej 3]] |

## Notas de la semana

- [[S09-0 Tema 01 - Series de Taylor en numeros complejos|Teoría — Series de Taylor y procedimiento]]
- [[S09-1 Tema 01 - Taylor Ej1 - logaritmo neperiano de (1+z)|Ej 1 — $\ln(1+z)$ en $z_0 = 0$ → $\sum (-1)^{n-1} z^n / n$]]
- [[S09-2 Tema 01 - Taylor Ej2 - logaritmo de (1+z) sobre (1-z)|Ej 2 — $\ln\!\left(\dfrac{1+z}{1-z}\right)$ → $2 \sum z^{2n-1}/(2n-1)$]]
- [[S09-3 Tema 01 - Taylor Ej3 - sen(z) alrededor de pi cuartos|Ej 3 — $\sin z$ alrededor de $\pi/4$]]

## Evaluación de la semana

> [!info] Evaluación no calificada (cuestionario)
> Cuestionario sobre series de Taylor. Plazo: lunes **18 mayo** → domingo **24 mayo 2026** 23:59. Ver [[S09-99 Evaluacion sem 09|metadatos]].

## Próxima semana

La semana 10 introduce las **series de Maclaurin** (caso particular del Taylor con $z_0 = 0$) y las **series de Laurent** — extensión natural que admite potencias negativas $(z - z_0)^{-n}$ y permite expandir funciones alrededor de **singularidades** (no solo de puntos regulares).
