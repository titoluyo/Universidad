---
title: "Ejercicio 2 — Transformada de Fourier del impulso desplazado δ(t−t₀)"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 15
orden: 3
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/transformada-de-fourier
  - tema/delta-de-dirac
date: 2026-06-29
---

## Enunciado

> [!question] Problema
> Hallar la transformada de Fourier de la **función impulso desplazada** $\delta(t - t_0)$.

![[fig-impulso-desplazado.png]]

## Desarrollo

### Paso 1 — Aplicar la definición

$$F(\omega) = \mathcal{F}\{\delta(t - t_0)\} = \int_{-\infty}^{\infty} \delta(t - t_0)\,e^{-i\omega t}\,dt$$

### Paso 2 — Propiedad de cribado (sifting) de la delta

La delta "selecciona" el valor del integrando en $t = t_0$:

> [!success] Resultado
> $$F(\omega) = e^{-i\omega t}\big|_{t = t_0} = e^{-i\omega t_0}$$

### Paso 3 — Interpretación gráfica

El espectro tiene **magnitud constante** $|F(\omega)| = 1$ y **fase lineal** $-\omega t_0$: el desplazamiento en el tiempo se traduce en un factor de fase $e^{-i\omega t_0}$ (propiedad de traslación en el tiempo).

![[fig-impulso-espectro.png]]

> [!tip] Casos particulares
> - Para $t_0 = 0$: $\mathcal{F}\{\delta(t)\} = 1$ (espectro plano — contiene todas las frecuencias por igual).
> - Confirma la **propiedad de traslación**: $\mathcal{F}\{g(t-a)\} = e^{-i\omega a}G(\omega)$ con $g=\delta$, $G=1$.

## Conceptos aplicados

- [[S15-1 Tema 01 - Transformada de Fourier#6.1 Función delta de Dirac|TF de la delta de Dirac]].
- [[S15-1 Tema 01 - Transformada de Fourier#5. Propiedades de la transformada de Fourier|Propiedad de traslación en el tiempo]].

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
