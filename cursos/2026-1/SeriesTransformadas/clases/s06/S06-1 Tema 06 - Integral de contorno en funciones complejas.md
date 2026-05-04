---
title: Integral de contorno en funciones complejas
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 6
orden: 1
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/integral-de-contorno
  - tema/parametrizacion
date: 2026-05-03
---

## Conocimientos previos

Para abordar la **integral de contorno en funciones complejas** se repasa primero la definición de integral de Riemann sobre una curva, generalizándola al plano complejo.

Sea $f(z)$ una función continua en todos los puntos de la curva $C$. Si subdividimos $C$ en $n$ partes mediante los puntos $z_1, z_2, z_3, \ldots, z_{n-1}$, elegidos arbitrariamente, siendo $z_1 = A$ y $z_n = B$.

Definiendo $\Delta z_k = \Delta x_k + i\,\Delta y_k$ y evaluando en $f(z_k)$ (Figura 1), se obtiene la sumatoria de Riemann:

$$\sum_{k=1}^{n} f(z_k)\,\Delta z_k \tag{1}$$

![[T01-Ej1-fig1-particion.jpeg]]

Si el número de subdivisiones $n$ aumenta tanto que $\Delta z_k \longrightarrow 0$, la sumatoria se aproxima a un límite que por definición es la **integral de contorno**:

$$\lim_{n \to \infty} \sum_{k=1}^{n} f(z_k)\,\Delta z_k = \int_{A}^{B} f(z)\,dz \tag{2}$$

> [!summary] Idea central
> La integral de contorno es la generalización de la integral definida real al plano complejo: en lugar de integrar a lo largo del eje real, se integra a lo largo de una curva $C$ que conecta dos puntos $A$ y $B$ del plano $\mathbb{C}$.

## Ejercicio resuelto: $\oint \dfrac{dz}{z} = 2\pi i$ con $C: |z|=1$

Aplicando la ecuación (2), demostrar:

$$\oint \frac{dz}{z} = 2\pi i, \quad \text{donde } C: |z| = 1$$

Graficamos la curva $|z| = 1$: una circunferencia centrada en el origen, recorrida con $0 < \theta < 2\pi$:

![[T01-Ej1-fig2-circunferencia.jpeg]]

### Método A: Parametrización trigonométrica

Sea $z(\theta) = x(\theta) + i\,y(\theta)$. Parametrizando:

$$x = \cos\theta, \qquad y = \text{sen}\,\theta$$

Por lo tanto:

$$z(\theta) = \cos\theta + i\,\text{sen}\,\theta \tag{3}$$

$$\dot{z}(\theta) = \frac{dz}{d\theta} = -\text{sen}\,\theta + i\,\cos\theta \tag{4}$$

Reescribimos la integral usando el cambio de variable $d\theta$:

$$\int_{A}^{B} f(z)\,dz = \int_{0}^{2\pi} f(z)\,\frac{dz}{d\theta}\,d\theta \tag{5}$$

Como $f(z) = 1/z$, sustituyendo (3) y (4) en (5):

$$\int_{0}^{2\pi} \frac{1}{\cos\theta + i\,\text{sen}\,\theta}\,(-\text{sen}\,\theta + i\,\cos\theta)\,d\theta$$

Multiplicando numerador y denominador por $i$ (truco para reconocer el integrando):

$$\int_{0}^{2\pi} \frac{-(i\,\text{sen}\,\theta + i^2\,\cos\theta)}{i(\cos\theta + i\,\text{sen}\,\theta)}\,d\theta = \int_{0}^{2\pi} \frac{-(i\,\text{sen}\,\theta - \cos\theta)}{i(\cos\theta + i\,\text{sen}\,\theta)}\,d\theta$$

Notando que $-(i\,\text{sen}\,\theta - \cos\theta) = \cos\theta - i\,\text{sen}\,\theta$, el integrando se simplifica a $-\frac{1}{i} \cdot \frac{(\cos\theta + i\,\text{sen}\,\theta)}{(\cos\theta + i\,\text{sen}\,\theta)} = -\frac{1}{i}$. Es decir:

$$\int_{0}^{2\pi} \frac{-1}{i}\,d\theta = -\frac{2\pi}{i} = 2\pi i$$

### Método B: Forma exponencial

Más directo: usando $z = |z|\,e^{i\theta}$ (con $|z| = 1$):

$$\frac{dz}{d\theta} = i\,|z|\,e^{i\theta} = i\,e^{i\theta}$$

$$\int_{0}^{2\pi} \frac{1}{|z|\,e^{i\theta}}\,(i\,e^{i\theta})\,d\theta = \int_{0}^{2\pi} \frac{i\,e^{i\theta}}{|z|\,e^{i\theta}}\,d\theta$$

Se simplifica $e^{i\theta}$ y $|z| = 1$:

$$\int_{0}^{2\pi} i\,d\theta = 2\pi i \checkmark$$

> [!success] Resultado clave
> $$\boxed{\oint_{|z|=1} \frac{dz}{z} = 2\pi i}$$
>
> Este resultado es la base del **Teorema integral de Cauchy** (siguiente sesión, ver [[S06-3 Tema 06 - Teorema de Cauchy]]) y motiva el cálculo de residuos: la integral de $1/z$ alrededor del origen no es cero porque $z=0$ es una singularidad.

## Continuacion

- [[S06-2 Tema 06 - Ejercicio 2 - Integral por dos caminos|Ejercicio 2 — ∫(z̄)² dz por dos caminos]] (video)
- [[S06-3 Tema 06 - Teorema de Cauchy|Tema 02 — Teorema de Cauchy]]
