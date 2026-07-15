---
title: "Tema 01 Ej 2 — Parseval: convergencia $\\sum 1/(2n-1)^4 = \\pi^4/96$"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 13
orden: 2
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/teorema-de-parseval
  - tema/series-de-fourier
date: 2026-06-15
---

## Enunciado

Sea la función $f(x) = 1 + |x|$ para $-1 < x < 1$, de periodo $2$. Determinar:

**(a)** su serie de Fourier, y
**(b)** la convergencia de $\displaystyle\sum_{n=1}^{\infty}\frac{1}{(2n-1)^4}$.

Fuente: [[T01-Ej2-Guion-parseval-convergencia.pdf|Guion del video — Parseval Ejercicio 2]].

## Parte (a): serie de Fourier

### Paso 1: paridad y datos

$f(x) = 1 + |x|$ es **par** ($|-x| = |x|$ absorbe el signo), por lo tanto $b_n = 0$ (solo cosenos). Periodo $T = 2$, frecuencia $\omega_0 = \dfrac{2\pi}{T} = \pi$. Por ser par, se integra en $(0,1)$ y se duplica.

### Paso 2: término constante $a_0$

$$a_0 = \frac{2}{T}\int_{-1}^{1}(1+|x|)\,dx = 2\int_0^1 (1+t)\,dt = 2\left[t + \frac{t^2}{2}\right]_0^1 = 2\left(1 + \frac{1}{2}\right) = 3$$

Por tanto $\dfrac{1}{2}a_0 = \dfrac{3}{2}$.

### Paso 3: coeficiente $a_n$ (integración por partes)

$$a_n = \frac{2}{T}\int_{-1}^{1}(1+|x|)\cos(n\pi x)\,dx = 2\int_0^1 (1+t)\cos(n\pi t)\,dt$$

La parte $\int_0^1 \cos(n\pi t)\,dt = \dfrac{\sin(n\pi)}{n\pi} = 0$. Para $\int_0^1 t\cos(n\pi t)\,dt$, por partes ($u=t$, $dv=\cos(n\pi t)dt$):

$$\int_0^1 t\cos(n\pi t)\,dt = \underbrace{\frac{t\sin(n\pi t)}{n\pi}\Big|_0^1}_{=\,0} - \int_0^1 \frac{\sin(n\pi t)}{n\pi}\,dt = \frac{\cos(n\pi t)}{(n\pi)^2}\Big|_0^1 = \frac{(-1)^n - 1}{(n\pi)^2}$$

Por tanto:

$$a_n = \frac{2\bigl[(-1)^n - 1\bigr]}{(n\pi)^2} = \begin{cases} 0, & n\ \text{par} \\[4pt] -\dfrac{4}{(n\pi)^2}, & n\ \text{impar} \end{cases}$$

### Paso 4: serie (solo armónicos impares, $n = 2n-1$)

> [!success] Serie de Fourier
> $$\boxed{\;f(t) = \frac{3}{2} - \frac{4}{\pi^2}\sum_{n=1}^{\infty}\frac{1}{(2n-1)^2}\cos\bigl((2n-1)\pi t\bigr)\;}$$

## Parte (b): convergencia vía Parseval

### Paso 5: aplicar la identidad de Parseval

$$\frac{1}{T}\int_{-T/2}^{T/2}\bigl[f(t)\bigr]^2 dt = \frac{a_0^2}{4} + \frac{1}{2}\sum_{n=1}^{\infty} a_n^2$$

**Lado izquierdo** (potencia media, usando paridad):

$$\frac{1}{2}\int_{-1}^{1}(1+|x|)^2\,dx = \int_0^1 (1+t)^2\,dt = \left[t + t^2 + \frac{t^3}{3}\right]_0^1 = 1 + 1 + \frac{1}{3} = \frac{7}{3}$$

**Lado derecho** ($\dfrac{a_0^2}{4} = \dfrac{9}{4}$ y $a_n^2 = \dfrac{16}{(2n-1)^4\pi^4}$):

$$\frac{9}{4} + \frac{1}{2}\sum_{n=1}^{\infty}\frac{16}{(2n-1)^4\pi^4} = \frac{9}{4} + \frac{8}{\pi^4}\sum_{n=1}^{\infty}\frac{1}{(2n-1)^4}$$

### Paso 6: despejar la serie

$$\frac{7}{3} = \frac{9}{4} + \frac{8}{\pi^4}\sum_{n=1}^{\infty}\frac{1}{(2n-1)^4}$$

$$\frac{7}{3} - \frac{9}{4} = \frac{28 - 27}{12} = \frac{1}{12} = \frac{8}{\pi^4}\sum_{n=1}^{\infty}\frac{1}{(2n-1)^4}$$

$$\sum_{n=1}^{\infty}\frac{1}{(2n-1)^4} = \frac{\pi^4}{12 \cdot 8} = \frac{\pi^4}{96}$$

> [!success] Resultado
> $$\boxed{\;\sum_{n=1}^{\infty}\frac{1}{(2n-1)^4} = \frac{\pi^4}{96}\;}$$

## Conclusión

Para una función **par** ($f(x)=1+|x|$) la serie de Fourier solo contiene cosenos de armónicos impares. Al aplicar Parseval, la potencia media (calculada por integral directa) se iguala con la suma de potencias, despejando la serie $\sum 1/(2n-1)^4 = \pi^4/96$. El método es idéntico al [[S13-1 Tema 01 - Ejercicio 1 - Parseval prueba suma 1 sobre n cuadrado|Ej 1]], pero aquí la potencia $4$ proviene de que los coeficientes $a_n \sim 1/n^2$ se elevan al cuadrado.

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
- Material del curso: [[T01-Ej2-Guion-parseval-convergencia.pdf|Guion del video — Parseval Ejercicio 2]], [[T01-Lectura-teorema-parseval.pdf|Lectura — Teorema de Parseval]].
