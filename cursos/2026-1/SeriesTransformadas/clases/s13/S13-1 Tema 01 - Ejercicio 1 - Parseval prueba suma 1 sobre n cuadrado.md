---
title: "Tema 01 Ej 1 — Parseval: probar $\\sum 1/n^2 = \\pi^2/6$"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 13
orden: 1
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/teorema-de-parseval
  - tema/series-de-fourier
date: 2026-06-15
---

## Enunciado

Sea la función $f(x) = x$ para $-\pi < x < \pi$ (con $f(\pm\pi) = 0$), de periodo $2\pi$. Probar que:

$$\sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6}$$

Fuente: [[T01-Ej1-Guion-parseval-demostracion.pdf|Guion del video — Parseval Ejercicio 1]].

## Paso 1: paridad y coeficientes

$f(x) = x$ es **impar** ($f(-x) = -x = -f(x)$), por lo tanto:

$$a_0 = 0, \qquad a_n = 0 \quad(\text{solo senos})$$

Periodo $T = 2\pi$, frecuencia $\omega_0 = \dfrac{2\pi}{T} = 1$.

## Paso 2: coeficiente $b_n$ (integración por partes)

$$b_n = \frac{2}{T}\int_{-\pi}^{\pi} t\sin(nt)\,dt = \frac{1}{\pi}\int_{-\pi}^{\pi} t\sin(nt)\,dt$$

Con $u = t$, $dv = \sin(nt)\,dt$ → $v = -\dfrac{\cos(nt)}{n}$:

$$b_n = \frac{1}{\pi}\left[-\frac{t\cos(nt)}{n}\Big|_{-\pi}^{\pi} + \frac{1}{n}\underbrace{\int_{-\pi}^{\pi}\cos(nt)\,dt}_{=\,0}\right] = \frac{1}{\pi}\cdot\left(-\frac{2\pi\cos n\pi}{n}\right) = -\frac{2\cos n\pi}{n}$$

Como $\cos n\pi = (-1)^n$:

$$b_n = -\frac{2(-1)^n}{n} = \frac{2(-1)^{n+1}}{n}$$

La serie de Fourier es $f(t) = \displaystyle\sum_{n=1}^{\infty}\frac{-2(-1)^n}{n}\sin(nt)$.

## Paso 3: aplicar la identidad de Parseval

> [!note] Identidad de Parseval
> $$\frac{1}{T}\int_{-T/2}^{T/2}\bigl[f(t)\bigr]^2 dt = \frac{a_0^2}{4} + \frac{1}{2}\sum_{n=1}^{\infty}\bigl(a_n^2 + b_n^2\bigr)$$

Como $a_0 = a_n = 0$, solo contribuye $b_n$. Con $f(t) = t$ y $T = 2\pi$:

$$\frac{1}{2\pi}\int_{-\pi}^{\pi} t^2\,dt = \frac{1}{2}\sum_{n=1}^{\infty} b_n^2 = \frac{1}{2}\sum_{n=1}^{\infty}\left(\frac{-2(-1)^n}{n}\right)^2$$

## Paso 4: evaluar cada lado

**Lado izquierdo** (potencia media):

$$\frac{1}{2\pi}\cdot\frac{t^3}{3}\Big|_{-\pi}^{\pi} = \frac{1}{2\pi}\left(\frac{\pi^3}{3} + \frac{\pi^3}{3}\right) = \frac{1}{2\pi}\cdot\frac{2\pi^3}{3} = \frac{\pi^2}{3}$$

**Lado derecho** (con $b_n^2 = \dfrac{4(-1)^{2n}}{n^2} = \dfrac{4}{n^2}$, pues $(-1)^{2n} = 1$):

$$\frac{1}{2}\sum_{n=1}^{\infty}\frac{4}{n^2} = 2\sum_{n=1}^{\infty}\frac{1}{n^2}$$

## Paso 5: despejar la serie

$$\frac{\pi^2}{3} = 2\sum_{n=1}^{\infty}\frac{1}{n^2} \quad\Longrightarrow\quad \sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6}$$

> [!success] Resultado
> $$\boxed{\;\sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6}\;}$$

## Conclusión

Este es el célebre **problema de Basilea**, resuelto aquí con la **identidad de Parseval**: se expande $f(x)=x$ en serie de senos (por ser impar), y al igualar la potencia media de la señal con la suma de potencias de los armónicos aparece directamente $\sum 1/n^2$. La paridad impar simplifica el cálculo al anular $a_0$ y $a_n$.

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
- Material del curso: [[T01-Ej1-Guion-parseval-demostracion.pdf|Guion del video — Parseval Ejercicio 1]], [[T01-Lectura-teorema-parseval.pdf|Lectura — Teorema de Parseval]].
