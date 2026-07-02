---
title: "Respuesta en frecuencia: red RC de corte inferior y su Bode"
curso: "[[Amplificadores MOC]]"
unidad: 3
semana: 15
orden: 1
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/diagrama-de-bode
  - tema/respuesta-en-frecuencia
  - tema/frecuencia-de-corte
  - tema/red-rc
  - tema/pasa-alto
date: 2026-06-30
---

## Contexto

Continuación de la [[S14-5 Tema 14 - Diagrama de Bode por factores|Semana 14]]. Ahora aplicamos las herramientas del Bode a la **red RC en serie** que aparece de forma natural en el acoplamiento de un amplificador: es la que fija su **frecuencia de corte inferior** $f_1$. El análisis (Boylestad, cap. 9) arranca estudiando qué pasa en los **extremos de frecuencia** y de ahí sale la gráfica de respuesta "con un mínimo de tiempo y esfuerzo".

> [!info] Toma de notas en clase
> Semana 15 — Red RC de la **Fig. 9.13** (capacitor en serie, salida sobre $R$): comportamiento a altas y bajas frecuencias, deducción de $f_1$ y su diagrama de Bode.

---

## 1. La red RC en serie (Fig. 9.13)

El capacitor $C$ va **en serie** con la entrada y la salida $V_o$ se toma **sobre $R$**:

$$V_i \;\to\; C \;\to\; \bullet \;\to\; V_o \text{ (sobre } R \text{ a tierra)}$$

Esta topología es un **filtro pasa-alto** de 1.er orden: el que en un amplificador introduce el capacitor de acoplamiento/paso y por eso define el **corte inferior**.

## 2. Comportamiento en los extremos de frecuencia

La clave está en cómo cambia la reactancia del capacitor con la frecuencia:

$$X_C = \dfrac{1}{2\pi f C}$$

- $\;X_C$ = reactancia capacitiva $[\Omega]$
- $\;f$ = frecuencia $[\text{Hz}]$
- $\;C$ = capacitancia $[\text{F}]$

### 2.1 Altas frecuencias — el capacitor es un cortocircuito (Fig. 9.14)

$$X_C = \dfrac{1}{2\pi f C} \cong 0\ \Omega$$

Con $X_C \approx 0$, el capacitor se sustituye por un **cortocircuito** (Fig. 9.14) y toda la tensión cae sobre $R$:

$$\boxed{V_o \cong V_i}\qquad \text{(a altas frecuencias)}$$

### 2.2 Frecuencia cero (DC) — el capacitor es un circuito abierto (Fig. 9.15)

$$X_C = \dfrac{1}{2\pi f C} = \dfrac{1}{2\pi (0)\,C} = \infty\ \Omega$$

Con $X_C \to \infty$ el capacitor se comporta como **circuito abierto**: no pasa corriente y

$$\boxed{V_o = 0\ \text{V}}\qquad \text{(a } f = 0\ \text{Hz)}$$

> [!note] Conclusión cualitativa
> La red **bloquea** la DC y las frecuencias bajas ($V_o\to 0$) y **deja pasar** las altas ($V_o\to V_i$). Es un **pasa-alto**: entre ambos extremos hay una transición cuyo punto medio es la **frecuencia de corte inferior** $f_1$.

## 3. Frecuencia de corte inferior $f_1$

Por divisor de tensión (fasorial), con $Z_C = -jX_C = \dfrac{1}{j\omega C}$:

$$A_v = \dfrac{V_o}{V_i} = \dfrac{R}{R - jX_C}\qquad\Rightarrow\qquad |A_v| = \dfrac{R}{\sqrt{R^2 + X_C^2}}$$

El **corte** se define donde la potencia cae a la mitad, es decir cuando $X_C = R$:

$$X_C = R \;\Rightarrow\; \dfrac{1}{2\pi f_1 C} = R \;\Rightarrow\; \boxed{f_1 = \dfrac{1}{2\pi R C}}$$

En ese punto:

$$|A_v| = \dfrac{R}{\sqrt{R^2+R^2}} = \dfrac{1}{\sqrt2} = 0.707 \;\Rightarrow\; 20\log(0.707) = -3\ \text{dB}$$

> [!tip] Regla de los −3 dB
> $f_1$ es la frecuencia a la que la ganancia cae **3 dB** por debajo de su valor de banda de paso ($V_o = 0.707\,V_i$). Es la definición estándar de frecuencia de corte de un filtro de 1.er orden — la misma que en [[S14-4 Tema 14 - Filtros de primer orden y diagrama de Bode|S14-4]].

## 4. Función de transferencia y su Bode

Reescribiendo con $\omega_1 = \dfrac{1}{RC}$ (es decir $\omega_1 = 2\pi f_1$):

$$A_v(j\omega) = \dfrac{V_o}{V_i} = \dfrac{R}{R + \frac{1}{j\omega C}} = \dfrac{j\omega RC}{1 + j\omega RC} = \dfrac{\,j\omega/\omega_1\,}{1 + j\omega/\omega_1}$$

Esto es exactamente el **producto de dos factores del diccionario de la [[S14-5 Tema 14 - Diagrama de Bode por factores|S14-5]]**:

| Factor | Aporte a la magnitud | Aporte a la fase |
|--------|----------------------|------------------|
| $(j\omega/\omega_1)$ — cero en el origen | $+20\ \text{dB/déc}$ (todo el rango) | $+90^\circ$ |
| $(1+j\omega/\omega_1)^{-1}$ — polo de 1.er orden | $0$ hasta $\omega_1$, luego $-20\ \text{dB/déc}$ | $0^\circ \to -90^\circ$ |

**Sumando** las asíntotas:

- $\;\omega \ll \omega_1$: pendiente **$+20\ \text{dB/década}$** (sube hacia el corte) y fase $\approx +90^\circ$.
- $\;\omega \gg \omega_1$: pendiente **$0$** (banda de paso plana en $0\ \text{dB}$) y fase $\approx 0^\circ$.
- $\;\omega = \omega_1$: **$-3\ \text{dB}$** y fase $+45^\circ$.

> [!note] Por qué es "pasa-alto"
> El cero en el origen hace que a baja frecuencia la salida se anule (recta que sube $+20\ \text{dB/déc}$ desde $-\infty$); el polo en $\omega_1$ "aplana" la respuesta al llegar a la banda de paso. El resultado es el espejo del pasa-bajo de la S14-4.

## 5. Gráfica

Bode de magnitud y fase de la red RC de corte inferior ($R=1\ \text{k}\Omega$, $C=0.1\ \mu\text{F}\Rightarrow f_1\approx 1.59\ \text{kHz}$): asíntotas de $+20\ \text{dB/déc}$ y $0\ \text{dB}$, curva real y punto de $-3\ \text{dB}$.

![[bode_rc_corte_inferior.png]]

Script: [`plot_bode_rc_corte_inferior.py`](plot_bode_rc_corte_inferior.py) — ejecutar con `uv run --with matplotlib --with numpy python plot_bode_rc_corte_inferior.py`.

---

## Bibliografía

- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*. Pearson — cap. 9 "Respuesta en frecuencia de BJT y JFET", Figs. 9.13–9.15 y frecuencia de corte inferior.
- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press — respuesta en frecuencia de amplificadores.
- Ogata, K. *Ingeniería de Control Moderna*. Pearson — construcción de diagramas de Bode.
