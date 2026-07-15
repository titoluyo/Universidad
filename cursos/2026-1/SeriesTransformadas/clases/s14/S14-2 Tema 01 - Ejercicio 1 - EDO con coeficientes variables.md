---
title: "Ejercicio 1 — EDO con coeficientes variables $tY''+2Y'+tY=0$ por Laplace"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 14
orden: 2
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/transformada-de-laplace
  - tema/transformada-inversa-de-laplace
date: 2026-06-22
---

## Enunciado

> [!question] Problema
> Hallar la solución general de
> $$tY'' + 2Y' + tY = 0$$
> si $Y(0) = 1$ y $Y(\pi) = 0$.

Aplicamos transformada de Laplace. Como el primer y tercer término están multiplicados por la variable $t$, necesitamos la propiedad de **multiplicación por $t^n$** (transformada de Laplace de $t^n f(t)$), además de la transformada de las derivadas.

## Desarrollo

### Paso 1 — Propiedad de multiplicación por $t^n$

$$\mathcal{L}\{t^n f(t)\} = (-1)^n \frac{d^n}{ds^n}F(s)$$

### Paso 2 — Aplicar Laplace a toda la ecuación (con $n=1$)

$$\mathcal{L}\{tY'' + 2Y' + tY\} = 0$$
$$-\frac{d}{ds}\,\mathcal{L}\{Y''\} + 2\,\mathcal{L}\{Y'\} - \frac{d}{ds}\,\mathcal{L}\{Y\} = 0$$

(El factor $t$ introduce el $-\frac{d}{ds}$ por la propiedad del Paso 1.)

### Paso 3 — Transformada de las derivadas

$$\mathcal{L}\{F^{(n)}(t)\} = s^n f(s) - s^{n-1}F(0) - s^{n-2}F'(0) - \cdots - F^{(n-1)}(0)$$

### Paso 4 — Sustituir las transformadas

Escribiendo $y = y(s) = \mathcal{L}\{Y(t)\}$:

$$\mathcal{L}\{Y''\} = s^2 y - s\,Y(0) - Y'(0)$$
$$\mathcal{L}\{Y'\} = s\,y - Y(0)$$
$$\mathcal{L}\{Y\} = y$$

Sustituyendo en la ecuación del Paso 2:

$$-\frac{d}{ds}\Bigl(s^2 y - s\,Y(0) - Y'(0)\Bigr) + 2\bigl(s\,y - Y(0)\bigr) - \frac{d}{ds}\bigl(y\bigr) = 0$$

Derivando respecto de $s$ (recordando que $y = y(s)$):

$$-\bigl(2s\,y + s^2 y' - Y(0)\bigr) + 2s\,y - 2Y(0) - y' = 0$$

### Paso 5 — Aplicar la condición inicial $Y(0)=1$

$$-s^2 y' - 2s\,y + 1 + 2s\,y - 2 - y' = 0$$

Los términos $\pm 2s\,y$ se cancelan:

$$-(s^2 + 1)\,y' - 1 = 0 \qquad\Longrightarrow\qquad y'(s) = \frac{-1}{s^2 + 1}$$

> [!note] Sobre las condiciones iniciales
> Para que la sustitución cierre, se usa $Y(0) = 1$ (las constantes dan $+1 - 2 = -1$). La condición $Y(\pi)=0$ no interviene en este desarrollo por Laplace; el método produce directamente la solución particular.

### Paso 6 — Integrar la EDO de primer orden en $y(s)$

$$\int dy = -\int \frac{1}{s^2 + 1}\,ds$$
$$y(s) = -\tan^{-1}s + A$$

Para fijar la constante $A$ usamos el comportamiento asintótico: cuando $s \to \infty$, debe cumplirse $y(s) \to 0$ (toda transformada de Laplace tiende a $0$). Como $\tan^{-1}(\infty) = \frac{\pi}{2}$:

$$0 = -\frac{\pi}{2} + A \qquad\Longrightarrow\qquad A = \frac{\pi}{2}$$

Por lo tanto:

$$y(s) = \frac{\pi}{2} - \tan^{-1}s = \cot^{-1}s = \tan^{-1}\!\left(\frac{1}{s}\right)$$

### Paso 7 — Transformada inversa

$$Y(t) = \mathcal{L}^{-1}\{y(s)\} = \mathcal{L}^{-1}\!\left\{\frac{\pi}{2} - \tan^{-1}s\right\} = \mathcal{L}^{-1}\!\left\{\tan^{-1}\frac{1}{s}\right\}$$

Usando el resultado conocido $\mathcal{L}\left\{\dfrac{\sin t}{t}\right\} = \tan^{-1}\dfrac{1}{s}$:

> [!success] Solución
> $$\boxed{\,Y(t) = \frac{\sin t}{t}\,}$$

## Verificación

La solución satisface las condiciones del problema:

- $\displaystyle \lim_{t\to 0}\frac{\sin t}{t} = 1 = Y(0)$. ✓
- $\displaystyle Y(\pi) = \frac{\sin \pi}{\pi} = \frac{0}{\pi} = 0 = Y(\pi)$. ✓

La función $Y(t) = \dfrac{\sin t}{t}$ es la **función seno cardinal** ($\operatorname{sinc}$), que aparece de forma natural en teoría de señales.

## Conceptos aplicados

- [[S14-1 Tema 01 - Transformadas de Laplace#4. Propiedades de la transformada de Laplace|Propiedad de multiplicación por $t^n$]] (vía $-\frac{d}{ds}$).
- [[S14-1 Tema 01 - Transformadas de Laplace#5. Transformada de Laplace de las derivadas|Transformada de las derivadas]].
- [[S14-1 Tema 01 - Transformadas de Laplace#7. Transformada inversa de Laplace|Transformada inversa de Laplace]].

## Bibliografía

- Hsu, H. P., & Ward, J. (1991). *Transformada de Laplace*. McGraw-Hill / Interamericana de México.
