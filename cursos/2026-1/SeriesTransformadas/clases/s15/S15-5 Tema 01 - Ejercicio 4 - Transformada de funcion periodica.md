---
title: "Ejercicio 4 — Transformada de Fourier de una función periódica (tren de pulsos)"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 15
orden: 5
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/transformada-de-fourier
  - tema/funcion-sinc
date: 2026-06-29
---

## Enunciado

> [!question] Problema
> Hallar la transformada de Fourier de un **tren de pulsos rectangulares** de ancho $d$ y periodo $T$. Cada pulso vale $1$ en un ancho $d$ centrado en el origen.

Fuente: [[T01-Ej-FuncionPeriodica-Guion.pdf|Guion del video — Transformada de Fourier de una función periódica]].

## Desarrollo

### Paso 1 — Definir la función sobre un periodo

Centrando el pulso para simplificar el cálculo, $f(t) = 1$ para $-\frac{d}{2} \le t \le \frac{d}{2}$ y $0$ fuera. La definición de la TF es:

$$F(\omega) = \int_{-\infty}^{\infty} f(t)\,e^{-i\omega_0 t}\,dt = \int_{-d/2}^{d/2} e^{-i\omega_0 t}\,dt$$

donde $\omega_0 = \dfrac{2\pi}{T}$ es la frecuencia fundamental.

### Paso 2 — Integrar

$$F(\omega) = \frac{e^{-i\omega_0 t}}{-i\omega_0}\bigg|_{-d/2}^{d/2} = \frac{1}{i\omega_0}\left[e^{i\omega_0 d/2} - e^{-i\omega_0 d/2}\right]$$

### Paso 3 — Reconocer el seno

Multiplicando y dividiendo por $2$ para formar $\sin\theta = \dfrac{e^{i\theta}-e^{-i\theta}}{2i}$:

$$F(\omega) = \frac{2}{\omega_0}\left[\frac{e^{i\omega_0 d/2} - e^{-i\omega_0 d/2}}{2i}\right] = \frac{2}{\omega_0}\sin\frac{\omega_0 d}{2}$$

### Resultado

Multiplicando y dividiendo por $d$ para escribirlo en forma sinc:

> [!success] Resultado
> $$\boxed{\;F(\omega) = d\,\frac{\sin\frac{\omega_0 d}{2}}{\frac{\omega_0 d}{2}} = d\,\operatorname{sinc}\!\left(\frac{\omega_0 d}{2}\right)\;}$$

> [!note] Conexión con la serie de Fourier
> El resultado coincide en forma con la **envolvente sinc** de los coeficientes de la serie de Fourier de un tren de pulsos: al aplicar la TF a una función periódica reaparece la estructura de la serie de Fourier, evaluada sobre la frecuencia fundamental $\omega_0$. Es el mismo cálculo de [[S15-2 Tema 01 - Ejercicio 1 - Transformada del pulso rectangular|Ej 1]] aplicado al pulso del periodo.

## Conceptos aplicados

- [[S15-1 Tema 01 - Transformada de Fourier#1. Forma compleja de la serie de Fourier|Forma compleja de la serie de Fourier]].
- [[S15-1 Tema 01 - Transformada de Fourier#6.5 Función periódica (desplazamiento en frecuencia)|TF de una función periódica]].

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
