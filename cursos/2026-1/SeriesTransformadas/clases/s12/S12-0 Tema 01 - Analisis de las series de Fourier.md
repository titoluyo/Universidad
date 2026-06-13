---
title: "Análisis de las series de Fourier — medio rango, error cuadrático y Gibbs"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 12
orden: 0
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/series-de-fourier
  - tema/serie-de-medio-rango
  - tema/error-cuadratico-medio
  - tema/fenomeno-de-gibbs
date: 2026-06-08
---

## Idea central

La semana 12 profundiza en las [[S11-2 Tema 02 - Series de Fourier|series de Fourier]] con tres herramientas de análisis:

1. **Series de medio rango** — cómo desarrollar en Fourier una función definida solo en un **intervalo finito** $(0, \tau)$, extendiéndola de forma par (cosenos) o impar (senos).
2. **Aproximaciones finitas y error cuadrático medio** — qué tan bien aproxima la **suma parcial** de $k$ términos a la función, medido por el error $E_k$.
3. **Fenómeno de Gibbs** — la sobreoscilación persistente cerca de las discontinuidades.

Fuente: [[T01-Lectura-analisis-series-fourier.pdf|Lectura — Análisis de las series de Fourier]].

## 1. Serie de Fourier de medio rango

En muchas situaciones físicas se tienen funciones **no periódicas**, definidas en un intervalo finito. Es útil **extender** la función no periódica a una periódica antes de calcular su serie de Fourier.

> [!summary] Serie de medio rango
> Una función $f(t)$ definida en un intervalo finito $(0, \tau)$ puede desarrollarse en una serie de Fourier válida **únicamente** en $(0, \tau)$, usando **solo senos** o **solo cosenos** (según la extensión elegida). Se toma periodo $T = 2\tau$.

### Extensión par → serie de cosenos

Si se extiende $f$ de forma **par**:

$$f(t) = \frac{1}{2}a_0 + \sum_{n=1}^{\infty} a_n \cos\frac{n\pi t}{\tau}, \qquad a_n = \frac{2}{\tau}\int_0^{\tau} f(t)\cos\frac{n\pi t}{\tau}\,dt$$

### Extensión impar → serie de senos

Si se extiende $f$ de forma **impar**:

$$f(t) = \sum_{n=1}^{\infty} b_n \sin\frac{n\pi t}{\tau}, \qquad b_n = \frac{2}{\tau}\int_0^{\tau} f(t)\sin\frac{n\pi t}{\tau}\,dt$$

Ambas se denominan **expansión de medio rango**. Aplicación resuelta: [[S12-1 Tema 01 - Ejercicio 1 - serie por expansion del coseno|expansión en cosenos]].

## 2. Aproximaciones finitas y error cuadrático medio

### Suma parcial $S_k$

> [!note] Suma parcial de $(2k+1)$ términos
> $$S_k = \frac{1}{2}a_0 + \sum_{n=1}^{k}\bigl(a_n\cos n\omega t + b_n\sin n\omega t\bigr)$$
> Es la aproximación de $f(t)$ con los primeros $k$ armónicos.

### Error y error cuadrático medio

La diferencia entre la función y su aproximación es el **error**:

$$\varepsilon_k(t) = f(t) - S_k(t)$$

El **error cuadrático medio** $E_k$ promedia el cuadrado de ese error sobre un periodo:

$$E_k = \frac{1}{T}\int_{-T/2}^{T/2}\bigl[\varepsilon_k(t)\bigr]^2 dt = \frac{1}{T}\int_{-T/2}^{T/2}\bigl[f(t) - S_k(t)\bigr]^2 dt$$

> [!success] Fórmula reducida del error cuadrático
> Desarrollando el cuadrado y usando la ortogonalidad, $E_k$ se reduce a:
> $$\boxed{\;E_k = \frac{1}{T}\int_{-T/2}^{T/2}\bigl[f(t)\bigr]^2 dt - \frac{a_0^2}{4} - \frac{1}{2}\sum_{n=1}^{k}\bigl(a_n^2 + b_n^2\bigr)\;}$$

- $\frac{1}{T}\int [f(t)]^2 dt$ = potencia media (valor cuadrático medio) de la señal.
- $\frac{a_0^2}{4} + \frac{1}{2}\sum(a_n^2+b_n^2)$ = potencia capturada por los $k$ armónicos (relación de Parseval truncada).

> [!tip] Interpretación
> $E_k$ es la **potencia residual** no representada por los primeros $k$ términos. A mayor $k$, menor $E_k$. Ejemplos: [[S12-2 Tema 01 - Ejercicio 2 - error cuadratico de f(t) = t|$f(t)=t$]] ($E_5 \approx 0.363$) y [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|$f(t)=A\lvert\sin\omega_0 t\rvert$]] ($E_5 \approx 1.22\times10^{-4}A^2$, muchísimo menor por ser una señal continua).

## 3. Fenómeno de Gibbs

> [!warning] Sobreoscilación en las discontinuidades
> Al aproximar una función con una **suma parcial** de Fourier, se produce un error considerable (un sobreimpulso) en la cercanía de una **discontinuidad**, **sin importar cuántos términos** se usen. Este efecto se llama **fenómeno de Gibbs**.

A medida que aumenta el número de términos, la sobreoscilación **se comprime hacia la discontinuidad**, pero su **altura se mantiene** prácticamente constante (≈ 9 % del salto). Sin embargo, la **energía** asociada a esas sobreoscilaciones (el error cuadrático medio) **tiende a cero**, por lo que su presencia carece de importancia práctica en términos de potencia.

> [!note] Dónde aparece
> Es visible en la [[S11-3 Tema 02 - Series de Fourier Ejercicio 1 - onda cuadrada|onda cuadrada]] (señal discontinua). Las señales **continuas** (triangular, seno rectificado) no presentan Gibbs y convergen mucho más rápido.

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
- Material del curso: [[T01-Lectura-analisis-series-fourier.pdf|Lectura — Análisis de las series de Fourier]].
