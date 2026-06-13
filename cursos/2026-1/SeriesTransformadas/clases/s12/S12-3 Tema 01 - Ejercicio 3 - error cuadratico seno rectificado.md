---
title: "Tema 01 Ej 3 — Error cuadrático del seno rectificado $A\\lvert\\sin\\omega_0 t\\rvert$"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 12
orden: 3
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/series-de-fourier
  - tema/error-cuadratico-medio
  - tema/seno-rectificado
date: 2026-06-08
---

## Enunciado

Encontrar la serie de Fourier de la función $f(t) = A\lvert\sin\omega_0 t\rvert$ (seno rectificado de onda completa) y determinar el **error cuadrático a cinco términos**.

![[T01-Ej3-fig-seno-rectificado.png]]

> [!info] Ejercicio propuesto con ayudas
> El portal incluye la guía paso a paso que se desarrolla a continuación.

Fuente: contenido HTML del portal — Semana 12, Tema 01: Teoría del error cuadrático (Ejercicio).

## Paso 1: paridad

El seno rectificado es **par**: $f(-t) = A\lvert\sin(-\omega_0 t)\rvert = A\lvert\sin\omega_0 t\rvert = f(t)$. Por tanto:

$$b_n = 0, \qquad n = 0, 1, 2, \ldots \quad(\text{solo cosenos})$$

## Paso 2: datos

El periodo del seno rectificado es $T = \pi$ (con $\omega_0 = 1$, $\lvert\sin t\rvert$ se repite cada $\pi$). Se integra sobre $(0, \pi)$ aprovechando la paridad.

## Paso 3: término constante $a_0$

$$a_0 = \frac{4}{2\pi}\int_0^{\pi} A\lvert\sin t\rvert\,dt = \frac{2A}{\pi}\bigl[-\cos t\bigr]_0^{\pi} = \frac{2A}{\pi}\bigl(-(-1) - (-1)\bigr) = \frac{4A}{\pi}$$

Es decir $\dfrac{1}{2}a_0 = \dfrac{2A}{\pi}$ (valor promedio del seno rectificado).

## Paso 4: coeficiente $a_n$ (integración por partes doble)

$$a_n = \frac{2}{\pi}\int_0^{\pi} A\sin t\cos(nt)\,dt$$

Integrando **por partes dos veces** (primero $u=\sin t$, $dv=\cos nt\,dt$; luego $u=\cos t$, $dv=\sin nt\,dt$), aparece de nuevo $a_n$ en el lado derecho:

$$a_n = \frac{2A}{\pi n^2}\bigl[\cos t\cos nt\bigr]_0^{\pi} + \frac{1}{n^2}a_n$$

Despejando:

$$a_n\left(1 - \frac{1}{n^2}\right) = \frac{2A}{\pi n^2}\bigl[(-1)\cos n\pi - 1\bigr] = -\frac{2A}{\pi n^2}\bigl[(-1)^n + 1\bigr]$$

$$\boxed{a_n = -\frac{2A}{\pi(n^2 - 1)}\bigl[(-1)^n + 1\bigr]}$$

## Paso 5: analizar el patrón

El factor $(-1)^n + 1$ vale $0$ si $n$ es impar y $2$ si $n$ es par:

$$a_n = \begin{cases} 0, & n\ \text{impar} \\[4pt] \dfrac{4A}{\pi(1 - n^2)}, & n\ \text{par} \end{cases}$$

## Paso 6: serie de Fourier

Reindexando los términos pares como $n \to 2n$:

> [!success] Serie del seno rectificado
> $$\boxed{\;f(t) = \frac{2A}{\pi} + \sum_{n=1}^{\infty}\frac{4A}{\pi\bigl(1 - (2n)^2\bigr)}\cos(2nt)\;}$$
>
> Equivalentemente: $\;f(t) = \dfrac{2A}{\pi} - \dfrac{4A}{\pi}\left(\dfrac{\cos 2t}{3} + \dfrac{\cos 4t}{15} + \dfrac{\cos 6t}{35} + \cdots\right)$.

## Paso 7: error cuadrático a cinco términos

> [!note] Fórmula
> $$E_k = \frac{1}{T}\int_{-T/2}^{T/2}\bigl[f(t)\bigr]^2 dt - \frac{a_0^2}{4} - \frac{1}{2}\sum_{n=1}^{k}\bigl(a_n^2 + b_n^2\bigr)$$

**Potencia media** ($\sin^2 t = \tfrac{1-\cos 2t}{2}$, cuya integral en $[0,\pi]$ es $\tfrac{\pi}{2}$):

$$\frac{1}{T}\int_{-T/2}^{T/2}\bigl[f(t)\bigr]^2 dt = \frac{A^2}{\pi}\int_0^{\pi}\sin^2 t\,dt = \frac{A^2}{\pi}\cdot\frac{\pi}{2} = \frac{A^2}{2}$$

**Término constante:** $\dfrac{a_0^2}{4} = \dfrac{1}{4}\left(\dfrac{4A}{\pi}\right)^2 = \dfrac{4A^2}{\pi^2}$.

**Suma de los coeficientes** (denominadores $(2n)^2 - 1 = 3, 15, 35, 63, 99$ para $n=1..5$):

$$\frac{1}{2}\sum_{n=1}^{5} a_n^2 = \frac{8A^2}{\pi^2}\sum_{n=1}^{5}\frac{1}{\bigl((2n)^2-1\bigr)^2} = \frac{8A^2}{\pi^2}\left(\frac{1}{3^2}+\frac{1}{15^2}+\frac{1}{35^2}+\frac{1}{63^2}+\frac{1}{99^2}\right)$$

$$= \frac{8A^2}{\pi^2}(0.1167)$$

Reuniendo:

$$E_5 = A^2\left(\frac{1}{2} - \frac{1}{\pi^2}\bigl(4 + 8(0.1167)\bigr)\right) = A^2\bigl(0.5 - 0.499878\bigr)$$

> [!success] Resultado
> $$\boxed{\;E_5 \approx 1.22\times 10^{-4}\,A^2\;}$$

## Conclusión

El seno rectificado es una señal **continua**, por lo que su serie de Fourier converge muy rápido: con solo 5 términos el error cuadrático medio es del orden de $10^{-4}A^2$ — más de **mil veces menor** que el de la función discontinua [[S12-2 Tema 01 - Ejercicio 2 - error cuadratico de f(t) = t|$f(t)=t$]] ($E_5 \approx 0.363$). Esto ilustra la regla general: a mayor **suavidad** de la señal (sin discontinuidades, sin [[S12-0 Tema 01 - Analisis de las series de Fourier#3. Fenómeno de Gibbs|Gibbs]]), más rápido decae el error de la aproximación finita.

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
- Material del curso: [[T01-Lectura-analisis-series-fourier.pdf|Lectura — Análisis de las series de Fourier]].
