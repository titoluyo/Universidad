---
title: "Series de Fourier — definición, ortogonalidad y coeficientes"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 11
orden: 2
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/series-de-fourier
  - tema/ortogonalidad
  - tema/coeficientes-de-fourier
date: 2026-06-01
---

## Idea central

Una **serie de Fourier** expande una función **periódica** $f(t)$ de periodo $T$ como una suma infinita de senos y cosenos. La clave para hallar los coeficientes de esa suma es la **ortogonalidad** de las funciones trigonométricas: al integrar productos de senos/cosenos sobre un periodo, casi todos se anulan, dejando despejado el coeficiente buscado.

Fuente: [[T02-Lectura-series-fourier.pdf|Lectura — Series de Fourier]].

## 1. Definición — serie trigonométrica de Fourier

> [!summary] Serie de Fourier
> $$f(t) = \frac{1}{2}a_0 + \sum_{n=1}^{\infty}\bigl(a_n \cos n\omega t + b_n \sin n\omega t\bigr)$$
> con la **frecuencia angular fundamental**:
> $$\omega = \frac{2\pi}{T}$$

- $f(t)$ = función periódica de periodo $T$.
- $a_0,\ a_n,\ b_n$ = coeficientes de Fourier.
- $\omega = 2\pi/T$ = frecuencia angular fundamental.
- $n$ = número de armónico ($n = 1, 2, 3, \ldots$).

## 2. Ortogonalidad de señales

> [!note] Conjunto ortogonal
> Un conjunto de funciones $\{\phi_k(t)\}$ es **ortogonal** en $a < t < b$ si para dos funciones cualesquiera $\phi_m, \phi_n$ del conjunto:
> $$\int_a^b \phi_m(t)\,\phi_n(t)\,dt = \begin{cases} 0, & m \neq n \\ r_n, & m = n \end{cases}$$

Las funciones $\{\cos n\omega t,\ \sin n\omega t\}$ forman un conjunto ortogonal en $[-T/2,\, T/2]$. Con $\omega = 2\pi/T$ se cumplen las **relaciones de ortogonalidad**:

| # | Relación | Valor |
| - | -------- | ----- |
| a | $\displaystyle\int_{-T/2}^{T/2} \cos(m\omega t)\,dt$ | $0$, para $m \neq 0$ |
| b | $\displaystyle\int_{-T/2}^{T/2} \sin(m\omega t)\,dt$ | $0$, $\forall\, m$ |
| c | $\displaystyle\int_{-T/2}^{T/2} \cos(m\omega t)\cos(n\omega t)\,dt$ | $\begin{cases}0, & m\neq n\\ T/2, & m=n\end{cases}$ |
| d | $\displaystyle\int_{-T/2}^{T/2} \sin(m\omega t)\sin(n\omega t)\,dt$ | $\begin{cases}0, & m\neq n\\ T/2, & m=n\end{cases}$ |
| e | $\displaystyle\int_{-T/2}^{T/2} \sin(m\omega t)\cos(n\omega t)\,dt$ | $0$, $\forall\, m, n$ |

## 3. Evaluación de los coeficientes

La idea es **proyectar** $f(t)$ sobre cada función base: se multiplica la serie por $\cos(m\omega t)$ (o $\sin(m\omega t)$) y se integra sobre un periodo; por ortogonalidad sobrevive un solo término.

### Coeficiente $a_n$ (cosenos)

Multiplicando por $\cos(m\omega t)$ e integrando, por las relaciones (c) y (e):

$$\int_{-T/2}^{T/2} f(t)\cos(n\omega t)\,dt = \frac{T}{2}\,a_n$$

> [!summary] Coeficiente de cosenos
> $$a_n = \frac{2}{T}\int_{-T/2}^{T/2} f(t)\cos(n\omega t)\,dt, \qquad n = 0, 1, 2, \ldots$$

### Término constante $a_0$

Tomando $n = 0$ en la fórmula anterior:

$$a_0 = \frac{2}{T}\int_{-T/2}^{T/2} f(t)\,dt$$

> [!tip] Interpretación de $a_0$
> $\frac{1}{2}a_0$ es el **valor promedio** (componente DC) de la señal sobre un periodo.

### Coeficiente $b_n$ (senos)

Multiplicando por $\sin(m\omega t)$ e integrando, por las relaciones (d) y (e):

$$\int_{-T/2}^{T/2} f(t)\sin(n\omega t)\,dt = \frac{T}{2}\,b_n$$

> [!summary] Coeficiente de senos
> $$b_n = \frac{2}{T}\int_{-T/2}^{T/2} f(t)\sin(n\omega t)\,dt, \qquad n = 1, 2, 3, \ldots$$

## 4. Procedimiento operativo

> [!success] Pasos para hallar la serie de Fourier
> 1. Identificar el **periodo** $T$ y calcular $\omega = 2\pi/T$.
> 2. **Analizar la paridad** de $f(t)$ (ver [[S11-0 Tema 01 - Senales periodicas, pares e impares|señales pares e impares]]):
>    - $f$ **par** → $b_n = 0$ (solo cosenos).
>    - $f$ **impar** → $a_0 = a_n = 0$ (solo senos).
> 3. Calcular $a_0$, $a_n$ y $b_n$ con las integrales (saltando los que la paridad ya anula).
> 4. Identificar el **patrón** según $n$ (par/impar) y simplificar.
> 5. Escribir la serie reuniendo los términos no nulos.

Aplicaciones resueltas: [[S11-3 Tema 02 - Series de Fourier Ejercicio 1 - onda cuadrada|Ej 1 — onda cuadrada]] y [[S11-4 Tema 02 - Series de Fourier Ejercicio 2 - onda triangular|Ej 2 — onda triangular]].

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
- Material del curso: [[T02-Lectura-series-fourier.pdf|Lectura — Series de Fourier]].
