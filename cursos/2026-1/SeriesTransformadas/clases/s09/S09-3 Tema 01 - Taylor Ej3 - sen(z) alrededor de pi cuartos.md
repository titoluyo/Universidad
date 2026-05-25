---
title: "Taylor Ej 3 — Expansión de $\\sin z$ alrededor de $z_0 = \\pi/4$"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 9
orden: 3
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/series-de-taylor
  - tema/funciones-trigonometricas
date: 2026-05-18
---

## Enunciado

Desarrollar $f(z) = \sin z$ en una **serie de Taylor alrededor de $z_0 = \pi/4$**.

Fuente: [[T01-Ej3-Guion.pdf|Guion del video — Ejercicio 3]].

> [!note] Diferencia con la serie de Maclaurin estándar
> La serie de Maclaurin clásica de $\sin z$ (centrada en $z_0 = 0$) ya se vio en [[S08-2 Tema 01 - Convergencia Ej2 - serie del seno|S08-2]]. Aquí el centro es $z_0 = \pi/4$, por lo que los términos serán potencias de $(z - \pi/4)$.

## Paso 1: derivadas sucesivas de $\sin z$

| $n$ | $f^{(n)}(z)$ | $f^{(n)}(\pi/4)$ |
| --- | ------------ | ---------------- |
| $0$ | $\sin z$     | $\sin(\pi/4) = \dfrac{\sqrt{2}}{2}$  |
| $1$ | $\cos z$     | $\cos(\pi/4) = \dfrac{\sqrt{2}}{2}$  |
| $2$ | $-\sin z$    | $-\dfrac{\sqrt{2}}{2}$               |
| $3$ | $-\cos z$    | $-\dfrac{\sqrt{2}}{2}$               |
| $4$ | $\sin z$     | $\dfrac{\sqrt{2}}{2}$                |
| $5$ | $\cos z$     | $\dfrac{\sqrt{2}}{2}$                |

> [!tip] Patrón cíclico de período 4
> Las derivadas de $\sin z$ se repiten cada 4: $\sin, \cos, -\sin, -\cos, \sin, \cos, \ldots$ Evaluadas en $z_0 = \pi/4$, dan **el mismo valor absoluto $\sqrt{2}/2$** con signos $(+, +, -, -, +, +, -, -, \ldots)$.

## Paso 2: construir la serie

Sustituyendo en la fórmula de Taylor $\sum \dfrac{f^{(n)}(z_0)}{n!}\,(z - z_0)^n$ con $z_0 = \pi/4$:

$$\sin z = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2}\,\frac{(z - \pi/4)}{1!} - \frac{\sqrt{2}}{2}\,\frac{(z - \pi/4)^2}{2!} - \frac{\sqrt{2}}{2}\,\frac{(z - \pi/4)^3}{3!} + \frac{\sqrt{2}}{2}\,\frac{(z - \pi/4)^4}{4!} + \cdots$$

## Paso 3: factorizar el término común $\sqrt{2}/2$

> [!success] Resultado
> $$\sin z = \frac{\sqrt{2}}{2}\left[1 + (z - \tfrac{\pi}{4}) - \frac{(z - \pi/4)^2}{2!} - \frac{(z - \pi/4)^3}{3!} + \frac{(z - \pi/4)^4}{4!} + \frac{(z - \pi/4)^5}{5!} - \cdots\right]$$

## Paso 4: forma compacta

Definamos $w = z - \pi/4$. El patrón de signos sigue el ciclo $(+, +, -, -)$ con período 4, que se puede expresar como:

$$\text{signo}(n) = \begin{cases} +1 & \text{si } n \equiv 0 \text{ o } 1 \pmod 4 \\ -1 & \text{si } n \equiv 2 \text{ o } 3 \pmod 4 \end{cases}$$

Equivalentemente, separando términos pares (con derivada $\pm\sin z_0$) e impares (con derivada $\pm\cos z_0$), y observando que para $\sin z$ en $z_0 = \pi/4$ ambos valen $\sqrt{2}/2$:

$$\sin z = \frac{\sqrt{2}}{2}\sum_{n=0}^{\infty} \frac{(-1)^{\lfloor n/2 \rfloor}\,(z - \pi/4)^n}{n!}$$

Donde $\lfloor n/2 \rfloor = 0, 0, 1, 1, 2, 2, 3, 3, \ldots$ genera el patrón de signos $(+, +, -, -, +, +, -, -)$.

> [!info] Forma alternativa elegante
> Usando la identidad $\sin(a + b) = \sin a \cos b + \cos a \sin b$ con $a = \pi/4$ y $b = w$:
> $$\sin z = \sin(\pi/4 + w) = \frac{\sqrt{2}}{2}\,(\cos w + \sin w)$$
> Sustituyendo las series de Maclaurin de $\cos w$ y $\sin w$:
> $$\sin z = \frac{\sqrt{2}}{2}\left[\sum_{k=0}^\infty \frac{(-1)^k w^{2k}}{(2k)!} + \sum_{k=0}^\infty \frac{(-1)^k w^{2k+1}}{(2k+1)!}\right]$$
> que combinadas dan exactamente la serie obtenida arriba. Esta forma alternativa confirma el resultado y da una manera más rápida de obtenerlo sin calcular derivadas.

## Radio de convergencia

Como $\sin z$ es una **función entera** (analítica en todo $\mathbb{C}$, sin singularidades), su serie de Taylor centrada en **cualquier** punto $z_0$ tiene radio de convergencia $R = \infty$.

## Conclusión

Este ejercicio enseña dos puntos clave:

1. **Cualquier punto $z_0$** puede usarse como centro de la expansión, no solo $z_0 = 0$. Los términos serán potencias de $(z - z_0)$.
2. **Las funciones trigonométricas tienen derivadas cíclicas** que generan patrones de signos $(+, +, -, -)$. Esto permite escribir la serie compactamente.

Para funciones con suma trigonométrica conocida (como $\sin(a+b) = \sin a\cos b + \cos a\sin b$), conviene usar la **identidad algebraica** como atajo antes de calcular derivadas — especialmente útil cuando $z_0$ es un ángulo notable como $\pi/4$, $\pi/6$, $\pi/2$.

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — §63.
- Spiegel, M. R. (2009). *Variable compleja* (Schaum). McGraw-Hill — Cap. 6.
- Material del curso: [[T01-Ej3-Guion.pdf|Guion del video Serie de Taylor Ej 3]].
