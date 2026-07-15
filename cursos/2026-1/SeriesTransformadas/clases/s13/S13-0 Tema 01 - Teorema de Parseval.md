---
title: "Teorema de Parseval — identidad de la energía y demostración"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 13
orden: 0
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/teorema-de-parseval
  - tema/series-de-fourier
  - tema/error-cuadratico-medio
date: 2026-06-15
---

## Idea central

El **teorema de Parseval** establece que la **energía (potencia promedio)** de una señal periódica es igual a la **suma de las energías de todas sus componentes armónicas**. Es la versión "energética" de la serie de Fourier y conecta el dominio del tiempo con el dominio de la frecuencia: la potencia se reparte entre el término constante y cada armónico.

Tiene aplicación directa en **procesamiento de señales** (telecomunicaciones, audio, imágenes) para identificar y conservar las frecuencias más relevantes, y como **truco de cálculo** para sumar series numéricas (ver ejercicios).

Fuente: [[T01-Lectura-teorema-parseval.pdf|Lectura — Teorema de Parseval]].

## 1. Valor medio de una señal

El **valor medio** de una señal es el promedio de todos los valores que la componen; su suma representa el **área bajo la curva** en un periodo:

$$\text{Área} = \int_0^T f(t)\,dt$$

Geométricamente equivale a un rectángulo de base $T$ y altura $h$ (la **altura promedio**), de modo que $\text{Área} = T\cdot h$.

## 2. Identidad de Parseval (señales periódicas)

> [!summary] Teorema de Parseval
> Si $a_0$, $a_n$ y $b_n$ ($n = 1, 2, \ldots$) son los coeficientes de la expansión de Fourier de una función periódica $f(t)$ de periodo $T$, entonces:
> $$\boxed{\;\frac{1}{T}\int_{-T/2}^{T/2}\bigl[f(t)\bigr]^2\,dt = \frac{a_0^2}{4} + \frac{1}{2}\sum_{n=1}^{\infty}\bigl(a_n^2 + b_n^2\bigr)\;}$$

- $\dfrac{1}{T}\displaystyle\int_{-T/2}^{T/2}[f(t)]^2 dt$ = **potencia promedio** (valor cuadrático medio) de la señal.
- $\dfrac{a_0^2}{4}$ = potencia de la componente continua (DC).
- $\dfrac{1}{2}(a_n^2 + b_n^2)$ = potencia del $n$-ésimo armónico.

> [!tip] Interpretación
> La potencia total de la señal es la suma de las potencias de cada componente espectral. No se pierde energía al pasar al dominio de la frecuencia.

## 3. Demostración (a partir del error cuadrático)

Se parte del **error cuadrático medio** $E_k$ de la aproximación por la suma parcial $S_k(t)$ (ver [[S12-0 Tema 01 - Analisis de las series de Fourier#2. Aproximaciones finitas y error cuadrático medio|semana 12]]):

$$E_k = \frac{1}{T}\int_{-T/2}^{T/2}\bigl[f(t)\bigr]^2 dt - \frac{a_0^2}{4} - \frac{1}{2}\sum_{n=1}^{k}\bigl(a_n^2 + b_n^2\bigr) = \frac{1}{T}\int_{-T/2}^{T/2}\bigl[f(t) - S_k(t)\bigr]^2 dt \;\geq\; 0$$

Se define la sucesión:

$$E_{k+1} = E_k - \frac{1}{2}\bigl(a_{k+1}^2 + b_{k+1}^2\bigr)$$

> [!note] Convergencia de la sucesión
> La sucesión $\{E_k\}$ contiene solo términos **no negativos** y es **no creciente** (cada paso resta una cantidad $\geq 0$), por lo tanto **converge**.

Como la serie de Fourier converge a $f(t)$, el error tiende a cero:

$$\lim_{k\to\infty}\varepsilon_k(t) = f(t) - \lim_{k\to\infty}S_k(t) = 0 \quad\Longrightarrow\quad \lim_{k\to\infty}E_k = 0$$

Sustituyendo $\lim E_k = 0$ en la definición de $E_k$:

$$0 = \frac{1}{T}\int_{-T/2}^{T/2}\bigl[f(t)\bigr]^2 dt - \frac{a_0^2}{4} - \frac{1}{2}\sum_{n=1}^{\infty}\bigl(a_n^2 + b_n^2\bigr)$$

de donde se concluye la **identidad de Parseval**. $\blacksquare$

## 4. Aplicación: sumar series numéricas

> [!success] Estrategia
> 1. Desarrollar $f(t)$ en serie de Fourier (aprovechando la paridad para anular coeficientes).
> 2. Aplicar la identidad de Parseval.
> 3. Calcular la integral $\frac{1}{T}\int [f(t)]^2 dt$ y despejar la suma de la serie.

Ejemplos resueltos:
- [[S13-1 Tema 01 - Ejercicio 1 - Parseval prueba suma 1 sobre n cuadrado|Ej 1]] — con $f(x)=x$ se prueba $\displaystyle\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$.
- [[S13-2 Tema 01 - Ejercicio 2 - Parseval convergencia 1 sobre (2n-1) cuarta|Ej 2]] — con $f(x)=1+|x|$ se prueba $\displaystyle\sum_{n=1}^\infty \frac{1}{(2n-1)^4} = \frac{\pi^4}{96}$.

## Bibliografía

- Hsu, H. P., & Ward, J. (1973). *Análisis de Fourier*. Fondo Educativo Interamericano. Colombia.
- Material del curso: [[T01-Lectura-teorema-parseval.pdf|Lectura — Teorema de Parseval]].
