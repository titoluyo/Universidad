---
title: "Proyecto 2 — Desarrollo analítico (teoría)"
curso: "[[SeriesTransformadas MOC]]"
tipo: proyecto
tags:
  - curso/series-transformadas
  - tipo/proyecto
  - tema/proyecto-final
  - tema/transformada-de-laplace
  - tema/circuito-rlc
  - tema/leyes-de-kirchhoff
date: 2026-07-13
---

# Proyecto 2 — Desarrollo analítico (Etapa B)

> [!info] Alcance
> Resolución **a mano, paso a paso** del voltaje del capacitor $V_o(t)$ de un circuito **RLC serie** con fuente escalón, mediante la **Transformada de Laplace**. Cubre el criterio **Dominio teórico (3 pts)** de la [[S18-98 PROY Indicaciones|rúbrica]]. Cada propiedad usada se respalda en [[S14-1 Tema 01 - Transformadas de Laplace|S14-1]], y el método replica el de [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|Ej 2]] y [[S14-4 Tema 01 - Ejercicio 3 - Circuito RLC II|Ej 3]]. Valores del caso según el [[Proyecto2/02 - Plan de trabajo|plan]]: $L=1$ H, $R=6\ \Omega$, $C=0{,}04$ F, $E=100$ V.

## 1. Definición del circuito

Circuito **RLC serie** alimentado por una **fuente escalón** de $E = 100$ V (un interruptor que cierra en $t=0$). La salida es el **voltaje en el capacitor** $V_o(t) = v_C(t)$.

![[fig1_circuito.png]]

| Parámetro | Valor | Rol |
| --------- | ----- | --- |
| $L$ | $1\ \text{H}$ | inductancia serie |
| $R$ | $6\ \Omega$ | resistencia serie |
| $C$ | $0{,}04\ \text{F}$ | capacitancia (salida $V_o = q/C$) |
| $E$ | $100\ \text{V}$ (escalón) | fem, cierra en $t=0$ |

**Condiciones iniciales.** Antes de $t=0$ el interruptor está abierto y el capacitor descargado, de modo que:

$$v_C(0) = 0, \qquad i(0) = 0 \;\Rightarrow\; v_C'(0) = \frac{i(0)}{C} = 0$$

> [!note] Diferencia con los ejercicios del curso
> [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|Ej 2]] y [[S14-4 Tema 01 - Ejercicio 3 - Circuito RLC II|Ej 3]] resuelven la **carga** $q(t)$. Aquí la incógnita es el **voltaje del capacitor** $V_o = q/C$: se plantea la ecuación directamente en $v_C$, lo que aporta un paso propio y evita duplicar las notas de clase.

## 2. Planteamiento por leyes de Kirchhoff

Por la **ley de voltajes de Kirchhoff**, la suma de caídas en la malla iguala la fem. Las caídas en cada elemento del RLC serie son (ver [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente#1. Planteamiento por leyes de Kirchhoff|Ej 2 §1]]):

- Resistencia: $V_R = R\,i$
- Inductor: $V_L = L\,\dfrac{di}{dt}$
- Condensador: $V_C = v_C$

$$L\frac{di}{dt} + R\,i + v_C = E$$

En un RLC serie la corriente es la que carga el capacitor, $i = C\dfrac{dv_C}{dt}$, luego $\dfrac{di}{dt} = C\dfrac{d^2 v_C}{dt^2}$. Sustituyendo:

$$LC\,\frac{d^2 v_C}{dt^2} + RC\,\frac{dv_C}{dt} + v_C = E$$

Dividiendo entre $LC$ y usando $\dfrac{R}{L}=6$, $\dfrac{1}{LC}=\dfrac{1}{1\cdot 0{,}04}=25$ y $\dfrac{E}{LC}=\dfrac{100}{0{,}04}=2500$:

$$\boxed{\;v_C'' + 6\,v_C' + 25\,v_C = 2500\;}\qquad v_C(0)=0,\;\; v_C'(0)=0$$

## 3. Aplicar transformada de Laplace

Sea $V_o(s) = \mathcal{L}\{v_C(t)\}$. Con la [[S14-1 Tema 01 - Transformadas de Laplace#5. Transformada de Laplace de las derivadas|transformada de las derivadas]] y condiciones iniciales nulas:

$$\mathcal{L}\{v_C''\} = s^2 V_o(s), \qquad \mathcal{L}\{v_C'\} = s\,V_o(s), \qquad \mathcal{L}\{2500\} = \frac{2500}{s}$$

$$s^2 V_o(s) + 6s\,V_o(s) + 25\,V_o(s) = \frac{2500}{s}$$

$$V_o(s)\,(s^2 + 6s + 25) = \frac{2500}{s} \qquad\Longrightarrow\qquad \boxed{\;V_o(s) = \frac{2500}{s\,(s^2 + 6s + 25)}\;}$$

## 4. Fracciones parciales

$$\frac{2500}{s\,(s^2+6s+25)} = \frac{A}{s} + \frac{Bs + C}{s^2 + 6s + 25}$$

Multiplicando por el denominador común: $2500 = A(s^2+6s+25) + (Bs+C)\,s$.

- $s = 0$: $\;2500 = 25A \Rightarrow \boxed{A = 100}$.
- Coef. $s^2$: $\;0 = A + B \Rightarrow \boxed{B = -100}$.
- Coef. $s^1$: $\;0 = 6A + C \Rightarrow \boxed{C = -600}$.

$$V_o(s) = \frac{100}{s} + \frac{-100\,s - 600}{s^2 + 6s + 25}$$

## 5. Completar cuadrados y preparar la inversa

El denominador cuadrático **no tiene raíces reales** (discriminante $6^2 - 4\cdot 25 = -64 < 0$); se completa el cuadrado:

$$s^2 + 6s + 25 = (s+3)^2 + 16 = (s+3)^2 + 4^2$$

Reescribimos el numerador en términos de $(s+3)$ para calzar con las formas de la [[S14-1 Tema 01 - Transformadas de Laplace#3. Tabla de transformadas elementales|tabla]] $\frac{s-b}{(s-b)^2+a^2}$ y $\frac{a}{(s-b)^2+a^2}$:

$$-100\,s - 600 = -100(s+3) - 300$$

y como $-300 = -75\cdot 4$:

$$V_o(s) = \frac{100}{s} \;-\; 100\cdot\frac{s+3}{(s+3)^2 + 4^2} \;-\; 75\cdot\frac{4}{(s+3)^2 + 4^2}$$

## 6. Transformada inversa — voltaje $V_o(t)$

Con $\mathcal{L}^{-1}\!\left\{\dfrac{1}{s}\right\}=1$, $\;\mathcal{L}^{-1}\!\left\{\dfrac{s+3}{(s+3)^2+4^2}\right\} = e^{-3t}\cos 4t$ y $\;\mathcal{L}^{-1}\!\left\{\dfrac{4}{(s+3)^2+4^2}\right\} = e^{-3t}\sin 4t$:

> [!success] Voltaje del capacitor
> $$\boxed{\,V_o(t) = 100 - 100\,e^{-3t}\cos 4t - 75\,e^{-3t}\sin 4t\,}$$
>
> Forma compacta: $\;V_o(t) = 100\left[\,1 - e^{-3t}\!\left(\cos 4t + \tfrac{3}{4}\sin 4t\right)\right]$ V.

Este resultado coincide con la referencia de control del [[Proyecto2/02 - Plan de trabajo#2. Definición del caso: circuito propuesto|plan §2]], lo que valida el desarrollo.

**Corriente** (dato de apoyo, $i = C\,v_C'$). Derivando $V_o(t)$ se cancelan los cosenos y queda $v_C'(t) = 625\,e^{-3t}\sin 4t$, luego:

$$i(t) = C\,v_C'(t) = 0{,}04\cdot 625\,e^{-3t}\sin 4t = 25\,e^{-3t}\sin 4t \ \text{A}$$

## 7. Autocomprobación (límites físicos)

| Comprobación | Cálculo | Resultado |
| ------------ | ------- | --------- |
| $V_o(0)$ | $100 - 100(1)(1) - 75(1)(0)$ | $0$ V ✓ (capacitor descargado) |
| $V_o(\infty)$ | el factor $e^{-3t}\to 0$ | $100$ V ✓ (se carga a la fuente) |
| $v_C'(0)$ | $625\,e^{0}\sin 0$ | $0$ ✓ ($i(0)=0$) |
| $i(0)$ | $25\,e^{0}\sin 0$ | $0$ A ✓ |

Las cuatro condiciones se cumplen: el capacitor parte de $0$ V, la corriente inicial es nula y en régimen permanente $V_o \to E = 100$ V. Es coherente con la física del circuito.

## 8. Análisis del régimen (parámetros del sistema)

La ecuación característica $s^2 + 6s + 25 = 0$ tiene polos complejos conjugados $s = -3 \pm 4j$. Comparando con la forma canónica de segundo orden $s^2 + 2\zeta\omega_0 s + \omega_0^2$:

| Parámetro | Fórmula | Valor |
| --------- | ------- | ----- |
| Frecuencia natural no amortiguada | $\omega_0 = \sqrt{1/LC}$ | $5$ rad/s |
| Atenuación | $\alpha = R/(2L)$ | $3$ s⁻¹ |
| **Factor de amortiguamiento** | $\zeta = \alpha/\omega_0$ | $0{,}6$ → **subamortiguado** ($\zeta<1$) |
| Frecuencia amortiguada | $\omega_d = \omega_0\sqrt{1-\zeta^2}$ | $4$ rad/s |
| Sobreimpulso | $M_p = e^{-\zeta\pi/\sqrt{1-\zeta^2}}$ | $9{,}48\%$ |
| Voltaje pico | $V_p = E(1+M_p)$ | $109{,}48$ V |
| Tiempo de pico | $t_p = \pi/\omega_d$ | $0{,}785$ s |
| Tiempo de establecimiento (2 %) | $t_s \approx 4/\alpha$ | $1{,}33$ s |

> [!tip] Lectura física
> Al ser $\zeta = 0{,}6 < 1$ el sistema es **subamortiguado**: el voltaje del capacitor **sobrepasa** el valor final ($109{,}5$ V ≈ $9{,}5\%$ por encima de los 100 V) alrededor de $t_p = 0{,}785$ s y luego **oscila** amortiguadamente a $\omega_d = 4$ rad/s hasta estabilizarse en $100$ V tras ≈ $1{,}33$ s. Este sobreimpulso y la oscilación son el material que se discute en las conclusiones (criterio 5). La gráfica de $V_o(t)$ y las curvas comparadas están en [[Proyecto2/04 - Simulacion (Octave)|la Etapa C]].

## Bibliografía

- Hsu, H. P., & Ward, J. (1991). *Transformada de Laplace*. McGraw-Hill / Interamericana de México.
- Notas del curso: [[S14-1 Tema 01 - Transformadas de Laplace|definición y propiedades de Laplace]], [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|circuito RLC (carga y corriente)]], [[S14-4 Tema 01 - Ejercicio 3 - Circuito RLC II|circuito RLC II]].
