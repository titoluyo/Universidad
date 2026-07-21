---
title: "Proyecto 2 v2 — Desarrollo analítico (teoría)"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
  - tema/transformada-de-laplace
  - tema/circuito-rlc
  - tema/leyes-de-kirchhoff
date: 2026-07-16
---

# Proyecto 2 v2 — Desarrollo analítico (teoría)

> [!info] Alcance
> Resolución **a mano, paso a paso** del voltaje del capacitor $V_o(t)$ de un circuito **R–L–C serie** con fuente escalón, siguiendo el **método exacto de clase** ([[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|S14-3]]): plantear en la **carga** $q(t)$, aplicar la Transformada de Laplace, fracciones parciales, completar cuadrados y antitransformar; al final se convierte $V_o = q/C$ (el paso que pide la consigna). Cubre el criterio **Dominio teórico (3 pts)** de la [[S18-98 PROY Indicaciones|rúbrica]]. Valores del caso según [[00 - Decision y alcance v2|la decisión v2]].

## 1. Definición del circuito

Circuito serie **R–L–C** alimentado por una **fuente escalón** de $E = 300$ V (un interruptor que cierra en $t=0$). La salida de interés es el **voltaje en el capacitor** $V_o(t) = q(t)/C$.

![[fig1_circuito.png]]

| Parámetro | Valor | Rol |
| --------- | ----- | --- |
| $R$ | $6\ \Omega$ | resistencia serie |
| $L$ | $1\ \text{mH} = 10^{-3}\ \text{H}$ | inductancia serie |
| $C$ | $4\ \mu\text{F} = 4\times10^{-6}\ \text{F}$ | capacitancia (salida $V_o = q/C$) |
| $E$ | $300$ V (escalón) | fem, cierra en $t=0$ |

**Condiciones iniciales.** Antes de $t=0$ el interruptor está abierto y el capacitor descargado:

$$q(0) = 0, \qquad I(0) = q'(0) = 0$$

## 2. Planteamiento por leyes de Kirchhoff

Por la **ley de voltajes de Kirchhoff**, la suma de las caídas de potencial en la malla iguala la fem. Las caídas en cada elemento son (ver [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente#1. Planteamiento por leyes de Kirchhoff|S14-3 §1]]):

- Resistencia: $V_R = R\,I$
- Inductor: $V_L = L\,\dfrac{dI}{dt}$
- Condensador: $V_C = \dfrac{q}{C}$

$$L\frac{dI}{dt} + R\,I + \frac{q}{C} = E$$

Como la corriente es la derivada de la carga, $I = \dfrac{dq}{dt}$, todo queda en función de $q$:

$$10^{-3}\,\frac{d^2q}{dt^2} + 6\,\frac{dq}{dt} + \frac{q}{4\times10^{-6}} = 300$$

Dividiendo entre $L = 10^{-3}$, con $\dfrac{R}{L} = 6000$, $\dfrac{1}{LC} = \dfrac{1}{4\times10^{-9}} = 2{,}5\times10^{8}$ y $\dfrac{E}{L} = 3\times10^{5}$:

$$\boxed{\;q'' + 6000\,q' + 2{,}5\times10^{8}\,q = 3\times10^{5}\;}\qquad q(0)=0,\;\; q'(0)=0$$

## 3. Aplicar transformada de Laplace

Sea $Q(s) = \mathcal{L}\{q(t)\}$. Con la [[S14-1 Tema 01 - Transformadas de Laplace#5. Transformada de Laplace de las derivadas|transformada de las derivadas]] y condiciones iniciales nulas:

$$\mathcal{L}\{q''\} = s^2 Q(s), \qquad \mathcal{L}\{q'\} = s\,Q(s), \qquad \mathcal{L}\{3\times10^{5}\} = \frac{3\times10^{5}}{s}$$

$$s^2 Q(s) + 6000\,s\,Q(s) + 2{,}5\times10^{8}\,Q(s) = \frac{3\times10^{5}}{s}$$

$$Q(s)\,\bigl(s^2 + 6000s + 2{,}5\times10^{8}\bigr) = \frac{3\times10^{5}}{s} \qquad\Longrightarrow\qquad \boxed{\;Q(s) = \frac{3\times10^{5}}{s\,\bigl(s^2 + 6000s + 2{,}5\times10^{8}\bigr)}\;}$$

## 4. Fracciones parciales

$$\frac{3\times10^{5}}{s\,(s^2+6000s+2{,}5\times10^{8})} = \frac{A}{s} + \frac{Bs + D}{s^2 + 6000s + 2{,}5\times10^{8}}$$

Multiplicando por el denominador común: $\;3\times10^{5} = A\,(s^2+6000s+2{,}5\times10^{8}) + (Bs+D)\,s$.

- $s = 0$: $\;3\times10^{5} = 2{,}5\times10^{8}\,A \Rightarrow \boxed{A = 1{,}2\times10^{-3}}$
- Coef. $s^2$: $\;0 = A + B \Rightarrow \boxed{B = -1{,}2\times10^{-3}}$
- Coef. $s^1$: $\;0 = 6000A + D \Rightarrow \boxed{D = -7{,}2}$

$$Q(s) = \frac{1{,}2\times10^{-3}}{s} + \frac{-1{,}2\times10^{-3}\,s - 7{,}2}{s^2 + 6000s + 2{,}5\times10^{8}}$$

## 5. Completar cuadrados y preparar la inversa

El denominador cuadrático **no tiene raíces reales** (discriminante $6000^2 - 4\cdot2{,}5\times10^{8} = 3{,}6\times10^{7} - 10^{9} < 0$); se completa el cuadrado:

$$s^2 + 6000s + 2{,}5\times10^{8} = (s+3000)^2 + 2{,}41\times10^{8} = (s+3000)^2 + \omega_d^{\,2}$$

$$\omega_d = \sqrt{2{,}41\times10^{8}} = 1000\sqrt{241} \approx 15\,524{,}2\ \text{rad/s}$$

Reescribimos el numerador en términos de $(s+3000)$ para calzar con las formas de la [[S14-1 Tema 01 - Transformadas de Laplace#3. Tabla de transformadas elementales|tabla]] $\frac{s-b}{(s-b)^2+a^2}$ y $\frac{a}{(s-b)^2+a^2}$:

$$-1{,}2\times10^{-3}\,s - 7{,}2 = -1{,}2\times10^{-3}\,(s+3000) - 3{,}6$$

y como $-3{,}6 = -\dfrac{3{,}6}{\omega_d}\cdot\omega_d$ con $\dfrac{3{,}6}{\omega_d} = \dfrac{3{,}6\times10^{-3}}{\sqrt{241}} \approx 2{,}319\times10^{-4}$:

$$Q(s) = \frac{1{,}2\times10^{-3}}{s} \;-\; 1{,}2\times10^{-3}\cdot\frac{s+3000}{(s+3000)^2 + \omega_d^{\,2}} \;-\; 2{,}319\times10^{-4}\cdot\frac{\omega_d}{(s+3000)^2 + \omega_d^{\,2}}$$

## 6. Transformada inversa — carga $q(t)$

Con $\mathcal{L}^{-1}\!\left\{\dfrac{1}{s}\right\}=1$, $\;\mathcal{L}^{-1}\!\left\{\dfrac{s+3000}{(s+3000)^2+\omega_d^2}\right\} = e^{-3000t}\cos\omega_d t\;$ y $\;\mathcal{L}^{-1}\!\left\{\dfrac{\omega_d}{(s+3000)^2+\omega_d^2}\right\} = e^{-3000t}\sin\omega_d t$:

> [!success] Carga
> $$\boxed{\,q(t) = 1{,}2 - e^{-3000t}\bigl(1{,}2\cos\omega_d t + 0{,}2319\sin\omega_d t\bigr)\ \text{mC}\,}$$

En régimen permanente $q_\infty = 1{,}2\ \text{mC} = C\cdot E = 4\times10^{-6}\cdot300$ ✓ (el capacitor se carga al valor de la fuente).

## 7. Corriente $I(t) = q'(t)$

Derivando cada término (los términos en $\cos\omega_d t$ se cancelan, igual que en [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente#6. Corriente $I(t) = Q'(t)$|S14-3 §6]]):

- coef. de $\cos$: $\;1{,}2\times10^{-3}\cdot3000 - 2{,}319\times10^{-4}\cdot\omega_d = 3{,}6 - 3{,}6 = 0$
- coef. de $\sin$: $\;1{,}2\times10^{-3}\cdot\omega_d + 2{,}319\times10^{-4}\cdot3000 = \dfrac{300}{\sqrt{241}} \approx 19{,}32$

> [!success] Corriente
> $$\boxed{\,I(t) = \frac{300}{\sqrt{241}}\,e^{-3000t}\sin\omega_d t \approx 19{,}32\,e^{-3000t}\sin\omega_d t\ \text{A}\,}$$

## 8. Voltaje del capacitor $V_o(t) = q(t)/C$ — lo que pide la consigna

La consigna pide **el voltaje del capacitor**. Basta dividir la carga entre $C = 4\times10^{-6}$ F:

$$V_o(t) = \frac{q(t)}{C}: \qquad \frac{1{,}2\times10^{-3}}{4\times10^{-6}} = 300; \qquad \frac{2{,}319\times10^{-4}}{4\times10^{-6}} = \frac{900}{\sqrt{241}} \approx 57{,}97$$

> [!success] Voltaje del capacitor
> $$\boxed{\;V_o(t) = 300 - e^{-3000t}\Bigl(300\cos\omega_d t + \tfrac{900}{\sqrt{241}}\sin\omega_d t\Bigr) \approx 300 - e^{-3000t}\bigl(300\cos\omega_d t + 57{,}97\sin\omega_d t\bigr)\ \text{V}\;}$$
> con $\omega_d = 1000\sqrt{241} \approx 15\,524{,}2$ rad/s (frecuencia de oscilación $f_d = \omega_d/2\pi \approx 2{,}47$ kHz).

## 9. Autocomprobación (límites físicos)

| Comprobación | Cálculo | Resultado |
| ------------ | ------- | --------- |
| $V_o(0)$ | $300 - (300\cdot1 + 57{,}97\cdot0)$ | $0$ V ✓ (capacitor descargado) |
| $V_o(\infty)$ | el factor $e^{-3000t}\to 0$ | $300$ V ✓ (se carga a la fuente) |
| $I(0)$ | $19{,}32\,e^{0}\sin 0$ | $0$ A ✓ |
| $q(\infty)$ | $C\cdot E = 4\times10^{-6}\cdot300$ | $1{,}2$ mC ✓ |

## 10. Análisis de los resultados teóricos

La ecuación característica $s^2 + 6000s + 2{,}5\times10^{8} = 0$ tiene **polos complejos conjugados** $s = -3000 \pm j\,1000\sqrt{241}$: la respuesta es un **transitorio oscilatorio amortiguado**. La envolvente $e^{-3000t}$ (constante de tiempo $1/3000 \approx 0{,}33$ ms) extingue el transitorio en unos $1{,}3$ ms, mientras la oscilación ocurre a $\omega_d \approx 15\,524$ rad/s (período $2\pi/\omega_d \approx 0{,}40$ ms).

**El pico de voltaje** se obtiene evaluando el resultado en el primer semiciclo, $\omega_d t = \pi$ (allí $\sin = 0$, $\cos = -1$), es decir en $t_p = \pi/\omega_d \approx 0{,}202$ ms:

$$V_o(t_p) = 300\bigl(1 + e^{-3000\pi/\omega_d}\bigr) = 300\bigl(1 + e^{-3\pi/\sqrt{241}}\bigr) \approx 463{,}5\ \text{V}$$

> [!tip] Lectura de ingeniería
> Con este amortiguamiento débil, el capacitor **sobrepasa la fuente en ~54 %** (463 V frente a 300 V) antes de estabilizarse. En la práctica esto obliga a especificar el capacitor (y el resto de componentes) para una tensión muy superior a la nominal del bus — el hallazgo central que se discute en las conclusiones del [[05 - Documento final|documento]].

Este resultado es la **referencia de control** contra la que se compara la [[04 - Simulacion (Octave)|simulación en Octave]].

## Bibliografía

- Hsu, H. P., & Ward, J. (1991). *Transformada de Laplace*. McGraw-Hill / Interamericana de México.
- Notas del curso: [[S14-1 Tema 01 - Transformadas de Laplace|definición y propiedades de Laplace]], [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|circuito RLC (carga y corriente)]], [[S14-4 Tema 01 - Ejercicio 3 - Circuito RLC II|circuito RLC II]].
