---
title: "Tema 01 Ej 1 — Serie de Fourier por expansión del coseno (medio rango)"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 12
orden: 1
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/series-de-fourier
  - tema/serie-de-medio-rango
date: 2026-06-08
---

## Enunciado

Dada la función definida en $(0, \pi)$:

$$f(t) = \begin{cases} 0, & 0 < t < \dfrac{\pi}{2} \\[4pt] 1, & \dfrac{\pi}{2} < t < \pi \end{cases}$$

Desarrollar $f(t)$ en una **serie de Fourier en términos del coseno** (expansión de medio rango par).

Fuente: [[T01-Ej1-Guion-expansion-cosenos.pdf|Guion del video — Serie de Fourier por expansión del coseno]].

## Paso 0: forma de la serie de cosenos

Al pedir la serie **en cosenos**, se extiende $f$ de forma **par**, lo que anula los senos ($b_n = 0$). Con el intervalo $(0, \tau)$ y $\tau = \pi$, la serie de medio rango tiene base $\cos\dfrac{n\pi t}{\tau} = \cos(nt)$:

$$f(t) = \frac{1}{2}a_0 + \sum_{n=1}^{\infty} a_n \cos(nt)$$

Solo falta determinar $a_0$ y $a_n$.

## Paso 1: coeficiente $a_n$

$$a_n = \frac{2}{\tau}\int_0^{\tau} f(t)\cos(nt)\,dt = \frac{2}{\pi}\left[\underbrace{\int_0^{\pi/2}(0)\cos(nt)\,dt}_{=\,0} + \int_{\pi/2}^{\pi}(1)\cos(nt)\,dt\right]$$

El primer tramo se anula ($f = 0$). Integrando el segundo ($\int\cos(nt)\,dt = \tfrac{\sin(nt)}{n}$):

$$a_n = \frac{2}{\pi}\cdot\frac{\sin(nt)}{n}\Big|_{\pi/2}^{\pi} = \frac{2}{n\pi}\left[\sin(n\pi) - \sin\frac{n\pi}{2}\right]$$

Como $\sin(n\pi) = 0$:

$$\boxed{a_n = -\frac{2}{n\pi}\sin\frac{n\pi}{2}}$$

## Paso 2: analizar el patrón $\sin\frac{n\pi}{2}$

| $n$ | $\sin\frac{n\pi}{2}$ | $a_n$ |
| --- | -------------------- | ----- |
| $1$ | $1$ | $-\dfrac{2}{\pi}$ |
| $2$ | $0$ | $0$ |
| $3$ | $-1$ | $+\dfrac{2}{3\pi}$ |
| $4$ | $0$ | $0$ |
| $5$ | $1$ | $-\dfrac{2}{5\pi}$ |

> [!tip] Solo armónicos impares, con signo alternante
> $a_n = 0$ para $n$ **par**; para $n$ **impar** vale $-\dfrac{2}{n\pi}(-1)^{(n-1)/2}$.

## Paso 3: término constante $a_0$

$$a_0 = \frac{2}{\tau}\int_0^{\tau} f(t)\,dt = \frac{2}{\pi}\int_{\pi/2}^{\pi}(1)\,dt = \frac{2}{\pi}\left(\pi - \frac{\pi}{2}\right) = \frac{2}{\pi}\cdot\frac{\pi}{2} = 1$$

Por tanto $\dfrac{1}{2}a_0 = \dfrac{1}{2}$ (el valor promedio de $f$ en el intervalo).

## Paso 4: escribir la serie

> [!success] Resultado
> $$\boxed{\;f(t) = \frac{1}{2} - \frac{2}{\pi}\left(\cos t - \frac{1}{3}\cos 3t + \frac{1}{5}\cos 5t - \cdots\right)\;}$$
>
> En forma compacta (solo $n$ impares):
> $$f(t) = \frac{1}{2} - \frac{2}{\pi}\sum_{k=1}^{\infty}\frac{(-1)^{k-1}}{2k-1}\cos\bigl((2k-1)t\bigr)$$

## Conclusión

La expansión de **medio rango en cosenos** representa una función definida solo en $(0,\pi)$ mediante su extensión par. El término $\tfrac{1}{2}a_0 = \tfrac12$ recoge el promedio y los armónicos impares (con signo alternante) construyen el escalón. Si en cambio se pidiera la serie **en senos**, se extendería de forma impar y se calcularía $b_n$ (ver teoría de [[S12-0 Tema 01 - Analisis de las series de Fourier|medio rango]]).

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
- Material del curso: [[T01-Ej1-Guion-expansion-cosenos.pdf|Guion del video — Serie de Fourier por expansión del coseno]].
