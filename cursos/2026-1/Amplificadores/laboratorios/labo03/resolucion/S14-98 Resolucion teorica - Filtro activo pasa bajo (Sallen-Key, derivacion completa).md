---
title: "Resolución teórica LE3 - Filtro activo pasa bajo (Sallen-Key): derivación completa de H(s)"
curso: "[[Amplificadores MOC]]"
unidad: 3
semana: 14
orden: 98
tipo: ejercicio
tags:
  - curso/amplificadores
  - tipo/ejercicio
  - tema/filtros-activos
  - tema/sallen-key
  - tema/segundo-orden
  - tema/funcion-de-transferencia
  - tema/factor-q
date: 2026-07-14
---

> [!info] Qué es esta nota
> Deducción **paso a paso** de la función de transferencia del filtro activo pasa bajo de la guía [[S14-101 Informe LE3 - Filtro activo pasa bajo (3K3)|LE3]]. El [[S14-101 Informe LE3 - Filtro activo pasa bajo (3K3)|informe]] comprime el álgebra en una línea ("eliminando $V$ … se obtiene"); aquí se desarrolla **toda la eliminación de $V$**, tal como la resolvió el profesor en la pizarra (sesión de la semana 17). Coincide término a término con el resultado del informe y quedó verificada con SymPy.

> [!note] Sobre los caracteres inferidos de la pizarra
> Las fotos 3 y 4 son manuscritas y algo ilegibles. Se infirieron así: la sustitución clave es siempre $V^{+} = V_o/A$ (positiva, por ser amplificador **no inversor**); todo término $SCR$ es $sCR$; y el resultado final $H(s)$ coincide exactamente con el recuadro de la foto 4 y con el informe, lo que valida la transcripción.

---

## Planteamiento

Filtro **Sallen-Key** pasa bajo con LM741, que combina realimentación **negativa** (fija la ganancia) y **positiva** (la red $R$–$C$ da el 2.º orden):

- Amplificador **no inversor**: $\;A = 1 + \dfrac{R_2}{R_1}\;\Rightarrow\; V_o = A\,V^{+}\;\Rightarrow\; \boxed{V^{+} = \dfrac{V_o}{A}}$
- Dos ramas $R$–$C$ iguales; nudos de interés: $V^{+}$ (entrada no inversora) y $V$ (nudo intermedio de la red).

La estrategia: plantear KCL en $V^{+}$ y en $V$, usar $V^{+}=V_o/A$, **eliminar $V$** y despejar $H(s)=V_o/V_i$.

## 1. Nudo $V^{+}$ → despejar $V$

$$\frac{V^{+} - V_i}{R} + sC\,(V^{+} - V) = 0$$

Sustituyendo $V^{+}=V_o/A$ y multiplicando por $R$ (con $sCR$ como grupo):

$$\frac{V_o}{A} - V_i + sCR\left(\frac{V_o}{A} - V\right) = 0$$

$$\frac{V_o}{A} - V_i + sCR\,\frac{V_o}{A} - sCR\,V = 0$$

Agrupando y despejando $V$:

$$\frac{V_o}{A}\,(1 + sCR) - V_i = sCR\,V$$

$$\boxed{\;V = \frac{V_o\,(1 + sCR)}{A\,sCR} - \frac{V_i}{sCR}\;}\tag{I}$$

## 2. Nudo $V$ → relación con $V^{+}$

$$(V - V^{+})\,sC + sC\,V + \frac{V - V_o}{R} = 0$$

Multiplicando por $R$:

$$(V - V^{+})\,sCR + sCR\,V + V - V_o = 0$$

$$2\,sCR\,V - sCR\,V^{+} + V - V_o = 0$$

$$V\,(1 + 2sCR) = sCR\,V^{+} + V_o$$

Y con $V^{+}=V_o/A$:

$$\boxed{\;V\,(1 + 2sCR) = sCR\,\frac{V_o}{A} + V_o\;}\tag{II}$$

## 3. Sustituir (I) en (II) y despejar $H(s)$

Reemplazando $V$ de (I) en el lado izquierdo de (II):

$$\left[\frac{V_o\,(1 + sCR)}{A\,sCR} - \frac{V_i}{sCR}\right](1 + 2sCR) = sCR\,\frac{V_o}{A} + V_o$$

Desarrollando el producto del lado izquierdo (usa $\tfrac{2sCR}{sCR}=2$):

$$\frac{2V_o(1+sCR)}{A} + \frac{V_o(1+sCR)}{A\,sCR} - 2V_i - \frac{V_i}{sCR} = sCR\,\frac{V_o}{A} + V_o$$

Pasamos todo lo de $V_o$ a la izquierda y lo de $V_i$ a la derecha, y **factorizamos**:

$$V_o\left[\frac{sCR}{A} + \frac{2}{A} + \frac{1+sCR}{A\,sCR} - 1\right] = V_i\left[\frac{1}{sCR} + 2\right]$$

Multiplicamos ambos lados por $A\,sCR$ para limpiar denominadores. Término a término, el corchete izquierdo da:

$$\frac{sCR}{A}\!\cdot\! A\,sCR = s^2C^2R^2,\quad \frac{2}{A}\!\cdot\! A\,sCR = 2sCR,\quad \frac{1+sCR}{A\,sCR}\!\cdot\! A\,sCR = 1+sCR,\quad (-1)\!\cdot\! A\,sCR = -A\,sCR$$

Sumando: $\;s^2C^2R^2 + 2sCR + 1 + sCR - A\,sCR = s^2C^2R^2 + (3-A)\,sCR + 1$.

Y el lado derecho: $\;V_i\left(\dfrac{1}{sCR}+2\right)A\,sCR = V_i\,A\,(1 + 2sCR)$.

Queda:

$$V_o\big[\,s^2C^2R^2 + (3-A)\,sCR + 1\,\big] = A\,(1 + 2sCR)\,V_i$$

## 4. Función de transferencia

$$\boxed{\;H(s) = \frac{V_o}{V_i} = \frac{A\,(1 + 2sCR)}{\,s^2C^2R^2 + (3 - A)\,sCR + 1\,}\;}$$

Idéntica al recuadro de la pizarra (foto 4) y al [[S14-101 Informe LE3 - Filtro activo pasa bajo (3K3)|informe LE3]]. ✓ (verificada con SymPy)

## 5. Identificación de parámetros

Llevando el denominador a la forma canónica $s^2 + \frac{\omega_o}{Q}s + \omega_o^2$ (dividido entre $C^2R^2$):

| Parámetro | Expresión | Con $A=2$, $R=3{,}3\,\text{k}\Omega$, $C=0{,}1\,\mu\text{F}$ |
| --- | --- | --- |
| Frecuencia natural | $\omega_o = \dfrac{1}{RC}$ | $3030{,}3\ \text{rad/s} \Rightarrow f_o = 482{,}3\ \text{Hz}$ |
| Factor de atenuación | $\alpha = \dfrac{3-A}{2RC}$ | $1515{,}2\ \text{s}^{-1}$ |
| Factor de calidad | $Q = \dfrac{\omega_o}{2\alpha} = \dfrac{1}{3-A}$ | $1$ |
| Amortiguamiento | $\zeta = \dfrac{\alpha}{\omega_o} = \dfrac{3-A}{2}$ | $0{,}5$ |

> [!note] Dos rasgos de esta topología
> 1. **Cero en el numerador** en $\omega_z = \dfrac{1}{2RC}$ ($f_z = f_o/2$): por él la caída asintótica es de $-20\ \text{dB/déc}$ (los dos polos dan $-40$ y el cero devuelve $+20$), no $-40\ \text{dB/déc}$ como un pasa bajo de 2.º orden "puro".
> 2. **La ganancia controla la estabilidad:** $Q=\dfrac{1}{3-A}$. Si $A\to 3$, $Q\to\infty$ y el circuito **oscila** — el mismo límite del [[S17-1 Tema 17 - Oscilador puente de Wien - analisis y criterio de Barkhausen|oscilador de Wien]]. Ver también [[S17-2 Tema 17 - Filtros de primer y segundo orden - comparacion|S17-2]] y [[S17-3 Tema 17 - Filtro pasivo RLC de segundo orden y resonancia|S17-3]].

## 6. Criterio de diseño de la ganancia

El amortiguamiento depende **solo** de $A$:

$$\zeta = \frac{3-A}{2} \qquad\Longrightarrow\qquad A = 3 - 2\zeta$$

- Para una respuesta **plana tipo Butterworth** (poco sobreimpulso), $\zeta \approx 0{,}707 \Rightarrow \boxed{A = 1{,}6}$ (como indica la diapositiva).
- El **circuito real** de la guía usa $R_1 = R_2 = 10\,\text{k}\Omega \Rightarrow A = 2$, de modo que $\zeta = 0{,}5$ y $Q = 1$: hay un **pico de resonancia** (medido $\approx 4{,}5$, $13\ \text{dB}$, cerca de $f_o$) antes de la caída. No es Butterworth — el sobrepico es inherente a $A=2$.

> [!tip] Cierre
> $\omega_o$ lo fijan $R$ y $C$ ($f_o = 482\ \text{Hz}$); la **forma** (pico o planicie) la fija $A$ vía $\zeta = (3-A)/2$. La parte experimental (barrido en frecuencia, Bode medido, comparación con Multisim) está en [[S14-101 Informe LE3 - Filtro activo pasa bajo (3K3)|el informe LE3]].

## Bibliografía

- Sedra, A. & Smith, K. *Microelectronic Circuits* — filtros activos, topología Sallen-Key, funciones de 2.º orden. Oxford University Press.
- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos* — filtros activos y factor de calidad. Pearson.
