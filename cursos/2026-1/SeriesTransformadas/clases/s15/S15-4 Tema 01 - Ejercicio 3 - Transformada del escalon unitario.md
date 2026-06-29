---
title: "Ejercicio 3 — Transformada de Fourier del escalón unitario u(t)"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 15
orden: 4
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/transformada-de-fourier
  - tema/escalon-unitario
  - tema/delta-de-dirac
date: 2026-06-29
---

## Enunciado

> [!question] Problema
> Hallar la transformada de Fourier del **escalón unitario** $u(t)$, definido por:
> $$u(t) = \begin{cases} 1, & t > 0 \\ 0, & t < 0 \end{cases}$$

Fuente: [[T01-Ej-FuncionUnitaria-Guion.pdf|Guion del video — Transformada de Fourier de una función escalón]].

## Desarrollo

### Paso 1 — Descomponer usando la simetría

El escalón reflejado es $u(-t) = \begin{cases} 0, & t>0 \\ 1, & t<0\end{cases}$, de modo que:

$$u(t) + u(-t) = 1 \quad (\text{salvo en } t=0,\ \text{donde hay discontinuidad})$$

Proponemos que la transformada tenga una **parte par** (un múltiplo de la delta) y una **parte impar**:

$$F(\omega) = \mathcal{F}\{u(t)\} = k\,\delta(\omega) + B(\omega)$$

### Paso 2 — Hallar $k$ (parte par)

Aplicando la TF a $u(t)+u(-t)=1$ y usando $\mathcal{F}\{1\}=2\pi\delta(\omega)$:

$$\mathcal{F}\{u(t)\} + \mathcal{F}\{u(-t)\} = 2\pi\delta(\omega)$$

La parte $\delta$ (función **par**) se suma y la parte $B$ (función **impar**) se cancela:

$$2k\,\delta(\omega) = 2\pi\delta(\omega) \qquad\Longrightarrow\qquad k = \pi$$

### Paso 3 — Hallar $B(\omega)$ (parte impar) vía la derivada

Como $\dfrac{du(t)}{dt} = \delta(t)$, aplicamos la propiedad de la derivada $\mathcal{F}\{f'(t)\} = i\omega F(\omega)$:

$$\mathcal{F}\{\delta(t)\} = i\omega\,F(\omega) = i\omega\,\bigl(\pi\delta(\omega) + B(\omega)\bigr)$$

Como $\mathcal{F}\{\delta(t)\} = 1$ y $\omega\,\delta(\omega) = 0$:

$$1 = i\omega\,B(\omega) \qquad\Longrightarrow\qquad B(\omega) = \frac{1}{i\omega}$$

### Resultado

> [!success] Transformada del escalón unitario
> $$\boxed{\;\mathcal{F}\{u(t)\} = \pi\,\delta(\omega) + \frac{1}{i\omega}\;}$$

> [!note] Interpretación
> La **delta** $\pi\delta(\omega)$ representa el valor medio (componente DC) del escalón; el término $\frac{1}{i\omega}$ aporta el resto del espectro. El ejercicio muestra que la **función Dirac** y la **función unitaria** están relacionadas mediante la **derivada**.

## Conceptos aplicados

- [[S15-1 Tema 01 - Transformada de Fourier#6.3 Escalón unitario|TF del escalón unitario]].
- [[S15-1 Tema 01 - Transformada de Fourier#5. Propiedades de la transformada de Fourier|Propiedad de la derivada]].

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
