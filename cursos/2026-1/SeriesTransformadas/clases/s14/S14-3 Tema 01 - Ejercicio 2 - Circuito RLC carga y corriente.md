---
title: "Ejercicio 2 — Circuito RLC: carga y corriente por Laplace"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 14
orden: 3
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/transformada-de-laplace
  - tema/circuito-rlc
  - tema/leyes-de-kirchhoff
date: 2026-06-22
---

## Enunciado

> [!question] Problema
> Un inductor de $2\text{ H}$, una resistencia y un condensador de $0{,}02\text{ F}$ se conectan en **serie** con una fem de $E$ voltios. En el tiempo $t=0$ tanto la carga del condensador como la corriente del circuito valen cero. Encontrar la **carga** y la **corriente** en cualquier tiempo $t>0$ si $E = 300\text{ V}$.

> [!warning] Nota sobre el valor de la resistencia
> El enunciado del video menciona $R = 18\ \Omega$, pero **todo el desarrollo usa $R = 16\ \Omega$** (que es el valor consistente: produce $\frac{R}{2}=8$ y el discriminante perfecto $(s+4)^2+3^2$). Tomamos $R = 16\ \Omega$ como el valor correcto del problema; con $18\ \Omega$ no se obtienen los números limpios del desarrollo.

Fuente: [[T01-Ej1-Circuitos-Guion.pdf|Guion del video — Circuitos eléctricos]].

**Datos:** $L = 2\text{ H}$, $R = 16\ \Omega$, $C = 0{,}02\text{ F}$, $E = 300\text{ V}$, con $Q(0)=0$ e $I(0)=0$.

## 1. Planteamiento por leyes de Kirchhoff

Por la **ley de voltajes de Kirchhoff**, la suma de las caídas de potencial en la malla es igual a la fem. Las caídas en cada elemento (circuito RLC serie) son:

- Resistencia: $V_R = R\,I$
- Condensador: $V_C = \dfrac{Q}{C}$
- Inductor: $V_L = L\,\dfrac{dI}{dt}$

$$L\frac{dI}{dt} + R\,I + \frac{Q}{C} = E$$

Como la corriente es la derivada de la carga, $I = \dfrac{dQ}{dt}$, escribimos todo en función de $Q$:

$$2\frac{d^2Q}{dt^2} + 16\frac{dQ}{dt} + \frac{1}{0{,}02}\,Q = 300$$

Con $\dfrac{1}{0{,}02} = 50$ y dividiendo entre $2$:

$$\boxed{\;Q'' + 8\,Q' + 25\,Q = 150\;}\qquad Q(0)=0,\;\; Q'(0)=I(0)=0$$

## 2. Aplicar transformada de Laplace

Usando $\mathcal{L}\{Q''\} = s^2 Q(s) - sQ(0) - Q'(0)$ y $\mathcal{L}\{Q'\} = sQ(s) - Q(0)$, con condiciones iniciales nulas:

$$s^2 Q(s) + 8s\,Q(s) + 25\,Q(s) = \frac{150}{s}$$

$$Q(s)\,(s^2 + 8s + 25) = \frac{150}{s} \qquad\Longrightarrow\qquad Q(s) = \frac{150}{s\,(s^2 + 8s + 25)}$$

## 3. Fracciones parciales

$$\frac{150}{s\,(s^2+8s+25)} = \frac{A}{s} + \frac{Bs + C}{s^2 + 8s + 25}$$

$$150 = A(s^2+8s+25) + (Bs+C)\,s$$

- $s = 0$: $\;150 = 25A \Rightarrow A = 6$.
- Coef. $s^2$: $\;0 = A + B \Rightarrow B = -6$.
- Coef. $s^1$: $\;0 = 8A + C \Rightarrow C = -48$.

$$Q(s) = \frac{6}{s} + \frac{-6s - 48}{s^2 + 8s + 25}$$

## 4. Completar cuadrados y preparar la inversa

$$s^2 + 8s + 25 = (s+4)^2 + 9 = (s+4)^2 + 3^2$$

Reescribimos el numerador en términos de $(s+4)$:

$$-6s - 48 = -6(s+4) - 24$$

$$Q(s) = \frac{6}{s} - 6\cdot\frac{s+4}{(s+4)^2 + 3^2} - 8\cdot\frac{3}{(s+4)^2 + 3^2}$$

(usando $-24 = -8\cdot 3$ para formar la transformada del seno).

## 5. Transformada inversa — carga $Q(t)$

Con $\mathcal{L}^{-1}\!\left\{\dfrac{s+4}{(s+4)^2+3^2}\right\} = e^{-4t}\cos 3t$ y $\mathcal{L}^{-1}\!\left\{\dfrac{3}{(s+4)^2+3^2}\right\} = e^{-4t}\sin 3t$:

> [!success] Carga
> $$\boxed{\,Q(t) = 6 - 6\,e^{-4t}\cos 3t - 8\,e^{-4t}\sin 3t\,}$$

## 6. Corriente $I(t) = Q'(t)$

Derivando cada término:

$$\frac{d}{dt}\bigl[-6e^{-4t}\cos 3t\bigr] = 24\,e^{-4t}\cos 3t + 18\,e^{-4t}\sin 3t$$
$$\frac{d}{dt}\bigl[-8e^{-4t}\sin 3t\bigr] = -24\,e^{-4t}\cos 3t + 32\,e^{-4t}\sin 3t$$

Los términos en $\cos 3t$ se cancelan ($24 - 24 = 0$) y los de $\sin 3t$ suman $18 + 32 = 50$:

> [!success] Corriente
> $$\boxed{\,I(t) = 50\,e^{-4t}\sin 3t\,}$$

## Verificación de condiciones iniciales

- $Q(0) = 6 - 6(1)(1) - 8(1)(0) = 0$. ✓
- $I(0) = 50\,e^{0}\sin 0 = 0$. ✓

Ambas magnitudes son **transitorios amortiguados** (factor $e^{-4t}$): la carga tiende al valor de régimen permanente $Q_\infty = 6\text{ C}$ ($= C\cdot E = 0{,}02\cdot 300$) y la corriente se extingue.

## Conceptos aplicados

- [[S14-1 Tema 01 - Transformadas de Laplace#5. Transformada de Laplace de las derivadas|Transformada de las derivadas]] (incorpora las condiciones iniciales).
- [[S14-1 Tema 01 - Transformadas de Laplace#7. Transformada inversa de Laplace|Transformada inversa]] vía fracciones parciales + completar cuadrados.
- Continúa en [[S14-4 Tema 01 - Ejercicio 3 - Circuito RLC II|Ej 3 — Circuito RLC II]].

## Bibliografía

- Hsu, H. P., & Ward, J. (1991). *Transformada de Laplace*. McGraw-Hill / Interamericana de México.
