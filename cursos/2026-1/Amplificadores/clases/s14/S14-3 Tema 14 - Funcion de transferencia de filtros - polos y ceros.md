---
title: "Función de transferencia de filtros: dominio de Laplace, polos y ceros"
curso: "[[Amplificadores MOC]]"
unidad: 3
semana: 14
orden: 3
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/funcion-de-transferencia
  - tema/filtros-activos
  - tema/transformada-de-laplace
  - tema/polos-y-ceros
  - tema/factor-q
  - tema/respuesta-en-frecuencia
date: 2026-06-22
---

## Contexto

En la [[S14-1 Tema 14 - Funcion de transferencia|nota de la pizarra]] vimos que un sistema queda descrito por $\text{F.T}=Y/X$, y en [[S14-2 Tema 14 - Filtros activos - introduccion y clasificacion|S14-2]] clasificamos los filtros. Esta nota **profundiza la función de transferencia de los filtros**: cómo se escribe como un **cociente de polinomios**, qué son sus **polos y ceros**, y cómo esos números —no el dibujo del circuito— determinan **qué tipo de filtro es, su frecuencia de corte, su selectividad ($Q$) y su estabilidad**.

Es el lenguaje con el que se diseñan todos los filtros que vienen después (primer y segundo orden, Sallen-Key, Butterworth/Chebyshev/Bessel) y la antesala de los **diagramas de Bode** y los **criterios de estabilidad** de la semana 15.

> [!info] Toma de notas en clase
> Semana 14 — Sesiones 27–28 (continuación). Profundización de la **función de transferencia** del pizarrón: el paso de $H(f)$ a $H(s)$ (Laplace), $H(s)$ como cociente $N(s)/D(s)$, el significado de **polos** y **ceros**, las **formas canónicas** de 1.er y 2.º orden, y cómo $\omega_0$ y $Q$ salen del denominador.

> [!note] De dónde parte
> El pizarrón da la definición operativa $H(f)=\dfrac{Y(f)}{X(f)}$ y que $Y(f)=X(f)\,H(f)$ (la convolución del tiempo vuelta producto). Aquí generalizamos $f \to s$ para poder **factorizar** la función y leer su comportamiento.

---

## 1. De $H(f)$ a $H(s)$: el dominio de Laplace

Para analizar filtros conviene usar la variable compleja de **Laplace** $s$ en lugar de $j2\pi f$:

$$s = \sigma + j\omega,\qquad \omega = 2\pi f$$

La **respuesta en frecuencia** (lo que mide el pizarrón) se recupera evaluando sobre el eje imaginario:

$$\boxed{\,H(f) = H(s)\big|_{s=j\omega} = H(s)\big|_{s=j2\pi f}\,}$$

- $\sigma$ = parte real (relacionada con el amortiguamiento / transitorios).
- $\omega = 2\pi f$ = parte imaginaria (la frecuencia que se observa en estado estacionario).

> [!tip] Por qué $s$ y no solo $f$
> Con $s$, la función de transferencia se vuelve un **cociente de polinomios** que se puede **factorizar**. Las raíces de esos polinomios (polos y ceros) resumen todo el comportamiento del filtro: forma de la respuesta, selectividad y estabilidad. Sobre el eje $s=j\omega$ se obtiene la magnitud y fase del pizarrón.

## 2. $H(s)$ como cociente de polinomios: ceros y polos

Toda función de transferencia de un filtro lineal es un cociente de dos polinomios en $s$:

$$\boxed{\,H(s) = \dfrac{N(s)}{D(s)} = K\,\dfrac{(s-z_1)(s-z_2)\cdots(s-z_m)}{(s-p_1)(s-p_2)\cdots(s-p_n)}\,}$$

- **Ceros** $z_i$: raíces del **numerador** $N(s)$. Donde $H=0$ → frecuencias que el filtro **anula**.
- **Polos** $p_i$: raíces del **denominador** $D(s)$. Donde $H\to\infty$ → frecuencias que el filtro **realza/resuena**.
- $K$ = constante de ganancia.
- $n$ = grado de $D(s)$ = **orden** del filtro.

> [!note] Idea central
> El **denominador es el mismo** para los cuatro tipos de un filtro de un orden dado; **lo que cambia es el numerador** (los ceros). Es decir, *los polos fijan la "forma" y la selectividad; los ceros deciden qué banda se rechaza*. Por eso pasa bajo, pasa alto, pasa banda y supresor de un mismo $Q$ comparten denominador.

## 3. Cómo polos y ceros dan la forma del filtro

Evaluando $|H(j\omega)|$ como producto de distancias en el plano $s$:

- Acercarse a un **polo** (que está cerca del eje $j\omega$) → la magnitud **sube** (pico de resonancia).
- Acercarse a un **cero** sobre el eje → la magnitud **cae** a cero (el *notch* del supresor).
- Cada **polo** aporta $-20\ \text{dB/década}$ de caída; cada **cero**, $+20\ \text{dB/década}$ de subida.

Esto explica directo la clasificación de [[S14-2 Tema 14 - Filtros activos - introduccion y clasificacion|S14-2]]:

| Tipo | Numerador $N(s)$ | Efecto |
|------|------------------|--------|
| Pasa bajo | constante | sin ceros → cae en alta por los polos |
| Pasa alto | $s^n$ | ceros en $s=0$ → bloquea continua/baja |
| Pasa banda | $s$ | cero en $0$ y en $\infty$ → solo pasa el centro |
| Supresor (notch) | $s^2+\omega_0^2$ | ceros en $\pm j\omega_0$ → anula $\omega_0$ |

## 4. Formas canónicas

### 4.1 Primer orden ($n=1$)

$$\text{Pasa bajo: } H(s)=\dfrac{A_0\,\omega_c}{s+\omega_c}\qquad\quad \text{Pasa alto: } H(s)=\dfrac{A_0\,s}{s+\omega_c}$$

Un **único polo** en $s=-\omega_c$ → caída de $-20\ \text{dB/década}$ y corte en $\omega_c=2\pi f_c$. Es el $H(f)=\dfrac{A_0}{1+jf/f_c}$ de [[S14-2 Tema 14 - Filtros activos - introduccion y clasificacion|S14-2]] escrito en $s$.

### 4.2 Segundo orden ($n=2$) — la forma estándar

El denominador canónico de **todo** filtro de 2.º orden es:

$$\boxed{\,D(s) = s^2 + \dfrac{\omega_0}{Q}\,s + \omega_0^2\,}$$

y según el numerador se obtiene cada tipo (mismo $\omega_0$ y $Q$):

$$H_{LP}=\dfrac{A_0\,\omega_0^2}{D(s)}\quad H_{HP}=\dfrac{A_0\,s^2}{D(s)}\quad H_{BP}=\dfrac{A_0\,\frac{\omega_0}{Q}s}{D(s)}\quad H_{BS}=\dfrac{A_0\,(s^2+\omega_0^2)}{D(s)}$$

- $\omega_0=2\pi f_0$ = frecuencia natural / central (rad/s).
- $Q$ = factor de calidad (selectividad), [[S14-2 Tema 14 - Filtros activos - introduccion y clasificacion|definido en S14-2]] como $Q=f_0/\text{BW}$.
- Pendiente fuera de banda: $-40\ \text{dB/década}$ (dos polos).

## 5. $Q$, $\omega_0$ y los polos

Resolviendo $D(s)=0$ se obtienen los dos polos:

$$p_{1,2} = -\dfrac{\omega_0}{2Q} \pm \omega_0\sqrt{\dfrac{1}{4Q^2}-1}$$

El **factor de amortiguamiento** se relaciona con $Q$ por $\zeta = \dfrac{1}{2Q}$. Según $Q$:

| $Q$ | Polos | Respuesta |
|-----|-------|-----------|
| $Q<0{,}5$ | reales y distintos (sobreamortiguado) | sin pico, caída lenta al corte |
| $Q=0{,}707$ | complejos | **Butterworth**: máxima planicie, sin pico |
| $Q>0{,}707$ | complejos cerca del eje $j\omega$ | **pico de resonancia** en $\approx\omega_0$ |
| $Q\to\infty$ | sobre el eje $j\omega$ | oscilador (límite de estabilidad) |

> [!warning] Conexión con estabilidad (semana 15)
> Si la parte real de un polo se vuelve **positiva** (cruza al semiplano derecho), el circuito **oscila/se vuelve inestable**. Por eso el criterio de estabilidad se enuncia sobre la **ubicación de los polos**: deben quedar en el semiplano izquierdo ($\sigma<0$). El caso $Q\to\infty$ (polos sobre el eje) es justo la frontera — y es como se diseñan los osciladores de [[S11-2 Analisis del oscilador puente de Wien|S11]].

## 6. Gráfica

Pasa bajo de 2.º orden con $f_0 = 1\ \text{kHz}$ y varios $Q$. Se ve cómo, al subir $Q$, los polos se acercan al eje $j\omega$ y aparece el **pico de resonancia**; en $Q=0{,}707$ (Butterworth) la banda de paso es lo más plana posible.

![[filtros_transferencia_Q.png]]

Script: [`plot_filtros_transferencia_Q.py`](plot_filtros_transferencia_Q.py) — ejecutar con `uv run --with matplotlib --with numpy python plot_filtros_transferencia_Q.py`.

---

## Bibliografía

- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press — funciones de transferencia, polos/ceros y filtros de 2.º orden.
- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*. Pearson — respuesta en frecuencia y filtros activos.
- Oppenheim, A. & Willsky, S. *Señales y Sistemas*. Prentice Hall — transformada de Laplace, polos y ceros, estabilidad.
