---
title: "Tema 02 Ej 2 — Serie de Fourier de una onda triangular"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 11
orden: 4
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/series-de-fourier
  - tema/coeficientes-de-fourier
  - tema/onda-triangular
date: 2026-06-01
---

## Enunciado

Encontrar la serie de Fourier de la función $f(t)$ que se muestra en la figura (onda triangular que sube de $0$ a $k$ en $t = \tfrac{L}{2}$ y baja de $k$ a $0$ en $t = L$):

![[T02-Ej2-fig-onda-triangular.png]]

$$f(t) = \begin{cases} \dfrac{2k}{L}\,t, & 0 < t < \dfrac{1}{2}L \\[6pt] \dfrac{2k}{L}\,(L - t), & \dfrac{1}{2}L < t < L \end{cases}$$

> [!info] Ejercicio propuesto con ayudas
> Este es un ejercicio para resolver de forma autónoma; el portal incluye la guía paso a paso que se desarrolla a continuación. Se trabaja como **expansión de medio rango en senos** (periodo $2L$, integral sobre $[0, L]$).

Fuente: contenido HTML del portal — Semana 11, Tema 02: Series de Fourier (Ejercicio 2).

## Paso 1: evaluar paridad

Por definición:

- $f(-t) = -f(t)$ → **impar**
- $f(-t) = f(t)$ → **par**

Extendida de forma impar, la onda triangular cumple:

$$f(t) = \frac{2k}{L}t \;\Longrightarrow\; \frac{2k}{L}(-t) = -\frac{2k}{L}t$$

es decir, **es impar**.

## Paso 2: coeficientes de cosenos

Por ser impar (ver [[S11-0 Tema 01 - Senales periodicas, pares e impares|paridad]]):

$$a_n = 0, \qquad n = 0, 1, 2, \ldots$$

Solo habrá términos en **seno**.

## Paso 3: planteo de $b_n$

$$b_n = \frac{2}{L}\int_0^L f(t)\sin\!\left(\frac{n\pi}{L}t\right)dt$$

Separando en los dos tramos de la definición:

$$b_n = \frac{2}{L}\left[\frac{2k}{L}\int_0^{L/2} t\sin\!\left(\frac{n\pi}{L}t\right)dt + \frac{2k}{L}\int_{L/2}^{L}(L - t)\sin\!\left(\frac{n\pi}{L}t\right)dt\right]$$

## Paso 4: primera integral (por partes)

$$\int_0^{L/2} t\sin\!\left(\frac{n\pi}{L}t\right)dt = -\frac{Lt}{n\pi}\cos\frac{n\pi}{L}t\,\Big|_0^{L/2} + \frac{L}{n\pi}\int_0^{L/2}\cos\!\left(\frac{n\pi}{L}t\right)dt$$

$$= -\frac{L^2}{2n\pi}\cos\frac{n\pi}{2} + \frac{L^2}{(n\pi)^2}\sin\frac{n\pi}{2}$$

## Paso 5: segunda integral (análoga)

$$\int_{L/2}^{L}(L - t)\sin\!\left(\frac{n\pi}{L}t\right)dt = \frac{L^2}{2n\pi}\cos\frac{n\pi}{2} + \frac{L^2}{(n\pi)^2}\sin\frac{n\pi}{2}$$

## Paso 6: combinar y simplificar

Al sumar ambas integrales los términos $\pm\dfrac{L^2}{2n\pi}\cos\dfrac{n\pi}{2}$ **se cancelan** y los términos en $\sin\dfrac{n\pi}{2}$ se duplican. Sustituyendo en $b_n$ (con el factor $\tfrac{2}{L}\cdot\tfrac{2k}{L}$):

> [!success] Coeficiente $b_n$
> $$b_n = \frac{8k}{(n\pi)^2}\sin\frac{n\pi}{2}$$

El factor $\sin\dfrac{n\pi}{2}$ se anula para $n$ **par** y vale $\pm 1$ para $n$ **impar** ($+1, -1, +1, \ldots$).

## Paso 7: escribir la serie

> [!success] Resultado
> $$\boxed{\;f(t) = \frac{8k}{\pi^2}\left(\sin\frac{\pi}{L}t - \frac{1}{3^2}\sin\frac{3\pi}{L}t + \frac{1}{5^2}\sin\frac{5\pi}{L}t - \cdots\right)\;}$$
>
> En forma compacta (solo $n$ impares):
> $$f(t) = \frac{8k}{\pi^2}\sum_{\substack{n=1\\ n\ \text{impar}}}^{\infty}\frac{(-1)^{(n-1)/2}}{n^2}\,\sin\frac{n\pi}{L}t$$

## Conclusión

La onda triangular impar produce una serie de **solo senos de armónicos impares**, con amplitudes que decaen como $1/n^2$ — mucho más rápido que la [[S11-3 Tema 02 - Series de Fourier Ejercicio 1 - onda cuadrada|onda cuadrada]] ($1/n$), lo que refleja que la señal triangular es **más suave** (continua) que la cuadrada (discontinua). El truco clave fue reconocer la paridad impar ($a_n = 0$) y notar la cancelación de los términos en coseno al sumar los dos tramos.

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
- Material del curso: [[T02-Lectura-series-fourier.pdf|Lectura — Series de Fourier]].
