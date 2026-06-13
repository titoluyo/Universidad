---
title: "Tema 01 Ej 2 — Error cuadrático de la aproximación de $f(t)=t$"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 12
orden: 2
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/series-de-fourier
  - tema/error-cuadratico-medio
date: 2026-06-08
---

## Enunciado

Aproximar la función $f(t) = t$ en el intervalo $-\pi < t < \pi$ mediante una serie de Fourier de **cinco términos no nulos**, y calcular el **error cuadrático medio** de la aproximación.

Fuente: [[T01-Ej2-Guion-error-cuadratico.pdf|Guion del video — Teoría del error cuadrático medio]].

## Paso 0: datos y paridad

Periodo $T = 2\pi$, frecuencia $\omega_0 = \dfrac{2\pi}{T} = 1$. La función $f(t) = t$ es **impar** ($f(-t) = -t = -f(t)$), por lo que:

$$a_0 = 0, \qquad a_n = 0 \quad(\text{solo senos})$$

## Paso 1: verificar $a_0 = 0$

$$a_0 = \frac{2}{T}\int_{-\pi}^{\pi} t\,dt = \frac{1}{\pi}\cdot\frac{t^2}{2}\Big|_{-\pi}^{\pi} = \frac{1}{\pi}\left(\frac{\pi^2}{2} - \frac{\pi^2}{2}\right) = 0 \quad\checkmark$$

## Paso 2: verificar $a_n = 0$ por paridad

El integrando $t\cos(nt)$ es **impar × par = impar**, y la integral de una función impar en un intervalo simétrico es cero:

$$a_n = \frac{2}{T}\int_{-\pi}^{\pi} t\cos(nt)\,dt = 0 \quad\checkmark$$

## Paso 3: coeficiente $b_n$ (integración por partes)

$t\sin(nt)$ es **impar × impar = par**, así que la integral existe:

$$b_n = \frac{2}{T}\int_{-\pi}^{\pi} t\sin(nt)\,dt = \frac{1}{\pi}\int_{-\pi}^{\pi} t\sin(nt)\,dt$$

Con $u = t$, $dv = \sin(nt)\,dt$ → $du = dt$, $v = -\dfrac{\cos(nt)}{n}$:

$$b_n = \frac{1}{\pi}\left[-\frac{t\cos(nt)}{n}\Big|_{-\pi}^{\pi} + \frac{1}{n}\underbrace{\int_{-\pi}^{\pi}\cos(nt)\,dt}_{=\,0}\right]$$

El término integral da $\sin$ evaluado en $\pm\pi$, que se anula. Evaluando el primer término con $\cos(\pm n\pi) = (-1)^n$:

$$b_n = \frac{1}{\pi}\cdot\left(-\frac{1}{n}\right)\bigl[\pi(-1)^n - (-\pi)(-1)^n\bigr] = \frac{1}{\pi}\cdot\left(-\frac{2\pi(-1)^n}{n}\right) = -\frac{2(-1)^n}{n}$$

> [!success] Coeficiente $b_n$
> $$b_n = \frac{2(-1)^{n+1}}{n}$$

## Paso 4: serie a cinco términos

| $n$ | $b_n$ |
| --- | ----- |
| $1$ | $2$ |
| $2$ | $-1$ |
| $3$ | $2/3$ |
| $4$ | $-1/2$ |
| $5$ | $2/5$ |

$$f(t) \approx 2\sin t - \sin 2t + \frac{2}{3}\sin 3t - \frac{1}{2}\sin 4t + \frac{2}{5}\sin 5t$$

En forma general: $\;f(t) = 2\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin(nt)$.

## Paso 5: error cuadrático medio a $k = 5$

> [!note] Fórmula
> $$E_k = \frac{1}{T}\int_{-T/2}^{T/2}\bigl[f(t)\bigr]^2 dt - \frac{a_0^2}{4} - \frac{1}{2}\sum_{n=1}^{k}\bigl(a_n^2 + b_n^2\bigr)$$

Como $a_0 = a_n = 0$, solo contribuye $b_n$. La potencia media de $f(t) = t$:

$$\frac{1}{T}\int_{-\pi}^{\pi} t^2\,dt = \frac{1}{2\pi}\cdot\frac{t^3}{3}\Big|_{-\pi}^{\pi} = \frac{1}{2\pi}\cdot\frac{2\pi^3}{3} = \frac{\pi^2}{3}$$

Suma de los cuadrados de los coeficientes ($b_n^2 = \dfrac{4}{n^2}$):

$$\sum_{n=1}^{5} b_n^2 = 4\left(1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \frac{1}{25}\right) = 4(1.4636) = 5.8544$$

Por tanto:

$$E_5 = \frac{\pi^2}{3} - \frac{1}{2}(5.8544) = 3.2899 - 2.9272$$

> [!success] Resultado
> $$\boxed{\;E_5 \approx 0.363\;}$$

## Conclusión

La función $f(t) = t$ (diente de sierra, **discontinua** en los extremos $\pm\pi$) deja un error cuadrático medio **apreciable** ($\approx 0.363$) con solo 5 términos, porque su discontinuidad hace que la serie converja lentamente (presencia del [[S12-0 Tema 01 - Analisis de las series de Fourier#3. Fenómeno de Gibbs|fenómeno de Gibbs]]). Compárese con el [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado|seno rectificado]] (señal continua), cuyo error es del orden de $10^{-4}$.

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
- Material del curso: [[T01-Ej2-Guion-error-cuadratico.pdf|Guion del video — Teoría del error cuadrático medio]].
