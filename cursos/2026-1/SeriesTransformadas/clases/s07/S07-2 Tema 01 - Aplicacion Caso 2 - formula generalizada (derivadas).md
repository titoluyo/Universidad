---
title: "Aplicación del teorema de Cauchy — Caso 2: fórmula generalizada (singularidad de orden 2)"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 7
orden: 2
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/formula-integral-de-cauchy
  - tema/derivadas-de-funciones-analiticas
date: 2026-05-04
---

## Enunciado

Calcular:

$$\oint \frac{z^2 - 3z}{(z + 1)^2}\,dz$$

donde el contorno $C$ encierra al punto singular (curva no especificada explícitamente; basta con que $z = -1$ esté en el interior).

Fuente: [[T01-Caso2-Guion.pdf|Guion del video del docente — Caso 2]].

## Observación inicial

Aparece un **exponente $2$ en el denominador** sobre el factor $(z + 1)$. Cuando esto sucede, la fórmula integral de Cauchy "simple" $\oint f(z)/(z - z_0)\,dz = 2\pi i\,f(z_0)$ **no aplica directamente**: hay que usar su **generalización para derivadas**.

## Derivación de la fórmula generalizada

Partimos de la fórmula integral de Cauchy:

$$f(z_0) = \frac{1}{2\pi i}\oint_C \frac{f(z)}{z - z_0}\,dz \tag{1}$$

Derivando respecto de $z_0$:

$$f'(z_0) = \frac{1}{2\pi i}\oint_C \frac{f(z)}{(z - z_0)^2}\,dz$$

Volviendo a derivar:

$$f''(z_0) = \frac{2!}{2\pi i}\oint_C \frac{f(z)}{(z - z_0)^3}\,dz$$

Iterando hasta la $n$-ésima derivada:

$$f^{(n)}(z_0) = \frac{n!}{2\pi i}\oint_C \frac{f(z)}{(z - z_0)^{n+1}}\,dz$$

Reordenando, se obtiene la **fórmula integral generalizada de Cauchy**:

$$\boxed{\;\oint_C \frac{f(z)}{(z - z_0)^{n+1}}\,dz = \frac{2\pi i}{n!}\,f^{(n)}(z_0)\;}$$

> [!note] Propiedad de las funciones analíticas
> Si $f(z)$ es analítica en un punto, admite **derivadas de todos los órdenes** allí, y todas ellas son a su vez analíticas. Esta es una diferencia fundamental con las funciones reales diferenciables, donde la existencia de la primera derivada no garantiza la segunda.

## Paso 1: identificar el punto de singularidad

Resolvemos $(z + 1)^2 = 0$:

$$z_0 = -1$$

> [!success] Singularidad de orden 2
> El punto $z_0 = -1$ es un polo de orden 2 (el exponente del denominador).

## Paso 2: determinar $n$

Comparando $(z - z_0)^{n+1}$ con $(z + 1)^2$:

$$n + 1 = 2 \;\Longrightarrow\; n = 1$$

Es decir, debemos calcular la **primera derivada** ($n = 1$).

## Paso 3: identificar $f(z)$

$$f(z) = z^2 - 3z$$

## Paso 4: derivar y evaluar en $z_0$

$$f'(z) = 2z - 3$$

$$f'(-1) = 2(-1) - 3 = -5$$

## Paso 5: aplicar la fórmula generalizada

$$\oint \frac{z^2 - 3z}{(z + 1)^2}\,dz = \frac{2\pi i}{1!}\cdot f'(-1) = 2\pi i \cdot (-5)$$

> [!success] Resultado
> $$\oint \frac{z^2 - 3z}{(z + 1)^2}\,dz = -10\pi i$$

## Conclusión

La **fórmula generalizada** extiende la utilidad del teorema de Cauchy a integrandos con singularidades de orden superior. La receta es:

1. Identificar el factor $(z - z_0)^{n+1}$ del denominador.
2. Deducir el orden de la derivada: $n = \text{exponente} - 1$.
3. Aislar $f(z)$ con el resto del integrando (el numerador "limpio").
4. Calcular $f^{(n)}(z_0)$ y aplicar $\dfrac{2\pi i}{n!}\,f^{(n)}(z_0)$.

Esto se aplica también en el [[S07-4 Tema 01 - Aplicacion Caso 4 - formula generalizada e2z|Caso 4]] con $n = 3$ (denominador $(z+1)^4$).

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — §53 (Derivadas de funciones analíticas).
- Material del curso: [[T01-Caso2-Guion.pdf|Guion del video Aplicación del teorema de Cauchy 2]].
