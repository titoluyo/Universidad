---
title: "Tema 02 Ej 1 — Serie de Fourier de una onda cuadrada"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 11
orden: 3
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/series-de-fourier
  - tema/coeficientes-de-fourier
  - tema/onda-cuadrada
date: 2026-06-01
---

## Enunciado

Encontrar la serie de Fourier de la función $f(t)$, periódica con periodo $T$, definida por:

$$f(t) = \begin{cases} -1, & -\dfrac{T}{2} < t < 0 \\[4pt] \phantom{-}1, & 0 < t < \dfrac{T}{2} \end{cases}$$

Fuente: [[T02-Ej1-Guion-coeficientes.pdf|Guion del video — Series de Fourier]].

## Paso 0: forma de la serie y análisis de paridad

La serie buscada es:

$$f(t) = \frac{1}{2}a_0 + \sum_{n=1}^{\infty}\bigl(a_n\cos n\omega t + b_n\sin n\omega t\bigr), \qquad \omega = \frac{2\pi}{T}$$

La función es **impar** ($f(-t) = -f(t)$: vale $-1$ a la izquierda y $+1$ a la derecha). Por la [[S11-0 Tema 01 - Senales periodicas, pares e impares|propiedad de paridad]] se anticipa que $a_0 = 0$ y $a_n = 0$; solo sobreviven los senos. A continuación se verifica por cálculo directo.

## Paso 1: coeficiente $a_n$

$$a_n = \frac{2}{T}\int_{-T/2}^{T/2} f(t)\cos(n\omega t)\,dt = \frac{2}{T}\left[\int_{-T/2}^{0}(-1)\cos(n\omega t)\,dt + \int_{0}^{T/2}(1)\cos(n\omega t)\,dt\right]$$

Integrando ($\int\cos(n\omega t)\,dt = \dfrac{\sin(n\omega t)}{n\omega}$):

$$a_n = \frac{2}{T}\left[-\frac{\sin(n\omega t)}{n\omega}\Big|_{-T/2}^{0} + \frac{\sin(n\omega t)}{n\omega}\Big|_{0}^{T/2}\right]$$

Como $\sin(0) = 0$ y, con $\omega = 2\pi/T$, $\;n\omega\cdot\tfrac{T}{2} = n\pi$, queda $\sin(\pm n\pi) = 0$. Por tanto:

$$\boxed{a_n = 0} \qquad (\text{y en particular } a_0 = 0)$$

## Paso 2: término constante $a_0$ (comprobación directa)

$$a_0 = \frac{2}{T}\int_{-T/2}^{T/2} f(t)\,dt = \frac{2}{T}\left[\int_{-T/2}^{0}(-1)\,dt + \int_{0}^{T/2}(1)\,dt\right] = \frac{2}{T}\left[-\frac{T}{2} + \frac{T}{2}\right] = 0$$

> [!note] Consistente con la paridad
> $a_0 = 0$ confirma que la señal no tiene componente DC (su promedio en un periodo es cero), como corresponde a una función impar.

## Paso 3: coeficiente $b_n$

$$b_n = \frac{2}{T}\left[\int_{-T/2}^{0}(-1)\sin(n\omega t)\,dt + \int_{0}^{T/2}(1)\sin(n\omega t)\,dt\right]$$

Usando $\int\sin(n\omega t)\,dt = -\dfrac{\cos(n\omega t)}{n\omega}$:

$$b_n = \frac{2}{T}\left[\frac{\cos(n\omega t)}{n\omega}\Big|_{-T/2}^{0} - \frac{\cos(n\omega t)}{n\omega}\Big|_{0}^{T/2}\right]$$

Evaluando con $\cos(0) = 1$ y $\cos\!\left(n\omega\cdot\tfrac{T}{2}\right) = \cos(n\pi)$:

$$b_n = \frac{2}{T}\cdot\frac{1}{n\omega}\Bigl[\underbrace{(1 - \cos n\pi)}_{\text{primer tramo}} - \underbrace{(\cos n\pi - 1)}_{\text{segundo tramo}}\Bigr] = \frac{2}{T}\cdot\frac{2 - 2\cos n\pi}{n\omega}$$

Sustituyendo $\omega = 2\pi/T$ (el $T$ y un factor $2$ se cancelan):

$$b_n = \frac{2 - 2\cos n\pi}{n\pi} = \frac{2}{n\pi}\bigl(1 - \cos n\pi\bigr) = \frac{2}{n\pi}\bigl(1 - (-1)^n\bigr)$$

## Paso 4: analizar el patrón según $n$

Como $\cos n\pi = (-1)^n$:

| $n$ | $1 - (-1)^n$ | $b_n$ |
| --- | ------------ | ----- |
| par | $1 - 1 = 0$ | $0$ |
| impar | $1 - (-1) = 2$ | $\dfrac{4}{n\pi}$ |

> [!tip] Solo armónicos impares
> Los términos de orden **par se anulan**; solo sobreviven los **impares** con $b_n = \dfrac{4}{n\pi}$.

## Paso 5: escribir la serie

> [!success] Resultado
> $$\boxed{\;f(t) = \sum_{\substack{n=1 \\ n\ \text{impar}}}^{\infty} \frac{4}{n\pi}\,\sin(n\omega t), \qquad \omega = \frac{2\pi}{T}\;}$$
>
> Desarrollada:
> $$f(t) = \frac{4}{\pi}\left(\sin\omega t + \frac{1}{3}\sin 3\omega t + \frac{1}{5}\sin 5\omega t + \cdots\right)$$

## Conclusión

La onda cuadrada impar se representa como una suma de **solo senos de armónicos impares**, con amplitudes que decaen como $1/n$. El reconocimiento de la **paridad impar** anticipa $a_0 = a_n = 0$ y reduce el trabajo a una sola integral ($b_n$). Este resultado es el ejemplo clásico que motiva el **fenómeno de Gibbs** (semana 12).

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
- Material del curso: [[T02-Ej1-Guion-coeficientes.pdf|Guion del video — Series de Fourier]], [[T02-Lectura-series-fourier.pdf|Lectura — Series de Fourier]].
