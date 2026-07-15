---
title: "Transformada de Fourier — forma compleja, definición, propiedades y transformadas elementales"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 15
orden: 1
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/transformada-de-fourier
  - tema/serie-de-fourier-compleja
  - tema/espectro-de-frecuencia
  - tema/delta-de-dirac
date: 2026-06-29
---

## Idea central

La **transformada de Fourier** (TF) extiende la serie de Fourier a señales **no periódicas**: se obtiene tomando el límite $T\to\infty$ de la serie de Fourier compleja. Convierte una función del tiempo $f(t)$ en una función de la **frecuencia angular** $F(\omega)$, revelando su contenido espectral. Es la base del análisis de señales en el dominio de la frecuencia.

Fuente: [[T01-Lectura-transformadas-fourier.pdf|Lectura — Transformadas de Fourier]].

## 1. Forma compleja de la serie de Fourier

Usando la fórmula de Euler $e^{i\theta} = \cos\theta + i\sin\theta$, una función periódica $f(t)$ se expresa como:

$$f(t) = \sum_{n=-\infty}^{+\infty} C_n\,e^{in\omega_0 t},\qquad \omega_0 = \frac{2\pi}{T}$$

con coeficientes complejos:

$$C_n = \frac{1}{T}\int_{-T/2}^{T/2} f(t)\,e^{-in\omega_0 t}\,dt$$

### Relación con los coeficientes reales $a_n$, $b_n$

$$C_n = \frac{a_n}{2} - \frac{i\,b_n}{2},\qquad C_{-n} = \frac{a_n}{2} + \frac{i\,b_n}{2}$$

$$C_n = |C_n|\,e^{i\phi_n},\qquad |C_n| = \frac{1}{2}\sqrt{a_n^2 + b_n^2}$$

## 2. Espectro de frecuencia

- El **espectro de amplitud** es la gráfica de $|C_n|$ en función de la frecuencia $\omega_0$.
- El **espectro de fase** es la gráfica del ángulo $\phi_n$ de $C_n$ en función de $\omega_0$.
- Como $n$ toma valores **enteros**, ambos espectros son **discretos** en la variable $n\omega_0$ → se les llama **espectros de línea** (espectros de frecuencia discreta).

## 3. Evaluación de coeficientes por diferenciación

Para funciones con **discontinuidades**, el cálculo de los coeficientes puede facilitarse usando la **delta de Dirac** junto con la diferenciación. Si $f$ es continua y periódica $2\pi$, con derivada suave a trozos en $[-\pi,\pi]$:

$$f(t) = \frac{1}{2}a_0 + \sum_{n=1}^{\infty}(a_n\cos n\omega t + b_n\sin n\omega t)$$

entonces la serie de Fourier de la derivada $f'$ se obtiene derivando término a término:

$$f'(t) = \sum_{n=1}^{\infty} n\,(b_n\cos n\omega t - a_n\sin n\omega t)$$

## 4. Definición de la transformada de Fourier

Partiendo de la serie de Fourier compleja y tomando el límite $T\to\infty$ (con $n\omega_0\to\omega$, $\omega_0\to d\omega$, y $\frac{1}{T}=\frac{\omega_0}{2\pi}$), la suma se convierte en integral:

> [!summary] Par de transformadas de Fourier
> **Transformada (directa):**
> $$\boxed{\;F(\omega) = \int_{-\infty}^{\infty} f(t)\,e^{-i\omega t}\,dt\;}$$
> **Transformada inversa:**
> $$\boxed{\;f(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} F(\omega)\,e^{i\omega t}\,d\omega\;}$$

$F(\omega)$ representa el contenido en frecuencia de $f(t)$; la inversa reconstruye $f(t)$ a partir de $F(\omega)$.

## 5. Propiedades de la transformada de Fourier

| Propiedad | Fórmula |
| --------- | ------- |
| **Linealidad** | $\mathcal{F}\{a\,f_1(t) + b\,f_2(t)\} = a\,F_1(\omega) + b\,F_2(\omega)$ |
| **Escalado** | $\mathcal{F}\{f(at)\} = \dfrac{1}{a}\,F\!\left(\dfrac{\omega}{a}\right)$ |
| **Traslación en el tiempo** | $\mathcal{F}\{g(t-a)\} = e^{-i\omega a}\,G(\omega)$ |
| **Derivada** | $\mathcal{F}\{f'(t)\} = i\omega\,F(\omega)$;  en general $\mathcal{F}\{f^{(n)}(t)\} = (i\omega)^n F(\omega)$ |

## 6. Transformadas de Fourier de funciones elementales y especiales

### 6.1 Función delta de Dirac

$$\mathcal{F}\{\delta(t)\} = \int_{-\infty}^{\infty}\delta(t)\,e^{-i\omega t}\,dt = 1$$

> [!note] Dualidad delta ↔ constante
> Recíprocamente, la TF de la constante $\frac{1}{2\pi}$ es $2\pi\delta(t)$: transformar una **constante** produce una **delta** (un impulso en frecuencia), porque es el proceso inverso.

### 6.2 Seno y coseno

$$\mathcal{F}\{\cos\omega_0 t\} = \pi\bigl(\delta(\omega - \omega_0) + \delta(\omega + \omega_0)\bigr)$$
$$\mathcal{F}\{\sin\omega_0 t\} = i\pi\bigl(\delta(\omega + \omega_0) - \delta(\omega - \omega_0)\bigr)$$

Cada sinusoide pura se transforma en **dos deltas** simétricas en $\pm\omega_0$ (espectro de línea).

### 6.3 Escalón unitario

A partir de $\dfrac{du(t)}{dt} = \delta(t)$ y la propiedad de la derivada $\mathcal{F}\{\delta(t)\} = i\omega\,F(\omega) = 1$:

$$\mathcal{F}\{u(t)\} = \pi\delta(\omega) + \frac{1}{i\omega}$$

(desarrollo completo en [[S15-4 Tema 01 - Ejercicio 3 - Transformada del escalon unitario|Ej 3]]).

### 6.4 Constante

Por dualidad con la delta:

$$\mathcal{F}\{1\} = 2\pi\delta(\omega),\qquad \mathcal{F}\{A\} = 2\pi A\,\delta(\omega)$$

### 6.5 Función periódica (desplazamiento en frecuencia)

Si $f(t)=1$ y $\mathcal{F}\{1\}=2\pi\delta(\omega)$, por la propiedad de desplazamiento en frecuencia:

$$\mathcal{F}\{e^{i\omega_0 t}\} = 2\pi\,\delta(\omega - \omega_0)$$

### 6.6 Función generalizada (ecuación de Parseval)

Para funciones generalizadas y ciertas funciones ordinarias se usa la **ecuación de Parseval**:

$$\int_{-\infty}^{\infty} f(x)\,G(x)\,dx = \int_{-\infty}^{\infty} F(x)\,g(x)\,dx$$

Si $\phi(t)$ es una función de prueba con $\mathcal{F}\{\phi(t)\}=\Phi(\omega)$, la TF $F(\omega)$ de una función generalizada $f(t)$ se define por:

$$\int_{-\infty}^{\infty} F(x)\,\phi(x)\,dx = \int_{-\infty}^{\infty} f(x)\,\Phi(x)\,dx$$

## 7. Aplicación: teoría de muestreo

> [!abstract] Teorema de muestreo (dominio del tiempo)
> Si una función $f(t)$ no contiene componentes de frecuencia superiores a $f_M$ ciclos por segundo, entonces $f(t)$ puede determinarse por completo a partir de sus valores tomados en intervalos uniformes menores a $\dfrac{1}{f_M}$ segundos.

**Teorema del muestreo (dominio de la frecuencia):** si $f(t)$ es cero salvo en el intervalo $-T<t<T$, su transformada $F(\omega)$ queda determinada de forma única por sus valores $F\!\left(\frac{n\pi}{T}\right)$ en puntos equidistantes separados $\frac{\pi}{T}$:

$$F(\omega) = \sum_{n=-\infty}^{+\infty} F\!\left(\frac{n\pi}{T}\right)\frac{\sin(\omega T - n\pi)}{\omega T - n\pi}$$

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
- Material del curso: [[T01-Lectura-transformadas-fourier.pdf|Lectura — Transformadas de Fourier]].
