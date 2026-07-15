---
title: "Ejercicio 1 — Transformada de Fourier del pulso rectangular (sinc)"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 15
orden: 2
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
> Encontrar la transformada de Fourier del **pulso rectangular** $P_d(t)$ definido por:
> $$P_d(t) = \begin{cases} 1, & |t| < \tfrac{1}{2}d \\ 0, & |t| > \tfrac{1}{2}d \end{cases}$$

![[fig-pulso-rectangular.png]]

## Desarrollo

### Paso 1 — Aplicar la definición

$$F(\omega) = \mathcal{F}\{P_d(t)\} = \int_{-\infty}^{\infty} P_d(t)\,e^{-i\omega t}\,dt$$

### Paso 2 — Integrar (el pulso vale 1 en $[-d/2,\,d/2]$)

$$F(\omega) = \int_{-d/2}^{d/2} e^{-i\omega t}\,dt = \frac{e^{-i\omega t}}{-i\omega}\bigg|_{-d/2}^{d/2}$$

$$F(\omega) = \frac{1}{i\omega}\left[e^{i\omega d/2} - e^{-i\omega d/2}\right] = \frac{2}{\omega}\left[\frac{e^{i\omega d/2} - e^{-i\omega d/2}}{2i}\right]$$

### Paso 3 — Reconocer la forma del seno

Usando $\sin\theta = \dfrac{e^{i\theta} - e^{-i\theta}}{2i}$:

> [!success] Resultado
> $$F(\omega) = \frac{2}{\omega}\sin\frac{\omega d}{2} = d\,\frac{\sin\frac{\omega d}{2}}{\frac{\omega d}{2}} = d\,\operatorname{sinc}\!\left(\frac{\omega d}{2}\right)$$

### Paso 4 — Interpretación gráfica

El espectro es una **función sinc**: lóbulo central de altura $d$ centrado en $\omega=0$ y ceros en $\omega = \frac{2\pi k}{d}$.

![[fig-pulso-sinc.png]]

> [!tip] Dualidad tiempo–frecuencia
> Un pulso **rectangular** en el tiempo tiene espectro **sinc**. A mayor ancho $d$ del pulso, más estrecho su espectro (y viceversa): es la manifestación del principio de incertidumbre tiempo-frecuencia.

## Conceptos aplicados

- [[S15-1 Tema 01 - Transformada de Fourier#4. Definición de la transformada de Fourier|Definición de la transformada de Fourier]].

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
