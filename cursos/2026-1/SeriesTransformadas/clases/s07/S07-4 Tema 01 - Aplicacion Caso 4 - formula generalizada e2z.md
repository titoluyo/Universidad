---
title: "Aplicación del teorema de Cauchy — Caso 4: fórmula generalizada con e^{2z}"
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 7
orden: 4
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

$$\oint_C \frac{e^{2z}}{(z + 1)^4}\,dz$$

donde $C: |z| = 3$.

## Paso 1: identificar el punto de singularidad

Resolvemos $(z + 1)^4 = 0$:

$$z_0 = -1$$

Es una singularidad de **orden 4** (polo de orden 4).

Verificamos que esté dentro de $C: |z| = 3$ → $|-1| = 1 < 3$ ✓.

![[T01-Caso4-Curva.png]]

## Paso 2: aplicar la fórmula generalizada

Como el denominador tiene exponente $4$ debemos usar la **fórmula integral generalizada de Cauchy**:

$$\oint_C \frac{f(z)}{(z - z_0)^{n+1}}\,dz = \frac{2\pi i}{n!}\,f^{(n)}(z_0)$$

(Derivación detallada en [[S07-2 Tema 01 - Aplicacion Caso 2 - formula generalizada (derivadas)|Caso 2]].)

## Paso 3: determinar el orden $n$ de la derivada

Comparando $(z - z_0)^{n+1}$ con $(z + 1)^4$:

$$n + 1 = 4 \;\Longrightarrow\; n = 3$$

Debemos calcular la **tercera derivada** de $f$.

## Paso 4: derivar $f(z) = e^{2z}$ tres veces

Usando la regla $\dfrac{d}{dz}e^{az} = a\,e^{az}$:

$$f(z) = e^{2z}$$

$$f'(z) = 2\,e^{2z}$$

$$f''(z) = 4\,e^{2z}$$

$$f'''(z) = 8\,e^{2z}$$

> [!tip] Atajo
> Cada derivada multiplica por $2$ (la constante del exponente). Para la derivada $n$-ésima: $f^{(n)}(z) = 2^n\,e^{2z}$. Así, $f^{(3)}(z) = 2^3\,e^{2z} = 8\,e^{2z}$.

## Paso 5: evaluar en $z_0 = -1$

$$f^{(3)}(-1) = 8\,e^{2(-1)} = 8\,e^{-2}$$

## Paso 6: sustituir en la fórmula

$$\oint_C \frac{e^{2z}}{(z + 1)^4}\,dz = \frac{2\pi i}{3!}\cdot 8\,e^{-2} = \frac{2\pi i}{6}\cdot 8\,e^{-2} = \frac{16\pi i\,e^{-2}}{6} = \frac{8\pi i\,e^{-2}}{3}$$

> [!success] Resultado
> $$\oint_C \frac{e^{2z}}{(z + 1)^4}\,dz = \frac{8\pi i}{3\,e^{2}}$$

## Conclusión

Este ejercicio ilustra el caso de un **polo de orden alto** combinado con una función trascendente sencilla. La estrategia es:

1. Identificar el orden del polo en el denominador → fija $n$.
2. Reconocer $f(z)$ como lo que queda en el numerador.
3. Calcular la $n$-ésima derivada (aquí explotamos que $e^{az}$ tiene derivada cerrada $a^n e^{az}$).
4. Evaluar en $z_0$ y aplicar $\dfrac{2\pi i}{n!}\,f^{(n)}(z_0)$.

Para integrandos donde $f(z)$ es polinómica o tiene derivadas más complicadas, el procedimiento es idéntico — solo el cálculo de $f^{(n)}(z_0)$ se vuelve más laborioso (ver [[S07-2 Tema 01 - Aplicacion Caso 2 - formula generalizada (derivadas)|Caso 2]] con $f(z) = z^2 - 3z$).

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — §53.
- Apostol, T. M. (1980). *Análisis matemático* (2.ª ed.). Reverté — Cap. 16 (Funciones analíticas).
