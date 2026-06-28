---
title: "Ejercicio 3 — Circuito RLC II: carga y corriente por Laplace"
curso: "[[SeriesTransformadas MOC]]"
unidad: 3
semana: 14
orden: 4
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
> Considere un circuito **RLC serie**. Antes de cerrar el interruptor en $t=0$, la carga en el capacitor y la corriente en el circuito son cero. Con condiciones iniciales $q(0)=0$, $q'(0)=0$, resistencia $R=20\ \Omega$, inductor $L=1\text{ H}$, capacitancia $C=0{,}005\text{ F}$ y fuente $E=150\text{ V}$, determine la **carga** $q(t)$ en el capacitor y la **corriente resultante** $I(t)$.

> [!warning] Nota sobre la capacitancia
> El enunciado del video lee "$0{,}05$ faradios", pero el desarrollo usa $\dfrac{1}{C}=200$, es decir $C = 0{,}005\text{ F}$. Tomamos $C = 0{,}005\text{ F}$ por consistencia con todo el desarrollo.

Fuente: [[T01-Ej2-Circuitos-Guion.pdf|Guion del video — Circuitos eléctricos II]].

**Datos:** $L = 1\text{ H}$, $R = 20\ \Omega$, $C = 0{,}005\text{ F}$, $E = 150\text{ V}$, con $q(0)=0$, $q'(0)=0$.

## 1. Planteamiento por leyes de Kirchhoff

Por la ley de voltajes de Kirchhoff en la malla RLC serie:

$$L\frac{dI}{dt} + R\,I + \frac{q}{C} = E$$

Con $I = \dfrac{dq}{dt}$ y los datos ($L=1$, $R=20$, $\tfrac1C = 200$, $E=150$):

$$\boxed{\;q'' + 20\,q' + 200\,q = 150\;}\qquad q(0)=0,\;\; q'(0)=0$$

## 2. Aplicar transformada de Laplace

Con condiciones iniciales nulas:

$$s^2 Q(s) + 20s\,Q(s) + 200\,Q(s) = \frac{150}{s}$$

$$Q(s)\,(s^2 + 20s + 200) = \frac{150}{s} \qquad\Longrightarrow\qquad Q(s) = \frac{150}{s\,(s^2 + 20s + 200)}$$

## 3. Fracciones parciales

$$\frac{150}{s\,(s^2+20s+200)} = \frac{A}{s} + \frac{Bs + C}{s^2 + 20s + 200}$$

$$150 = A(s^2+20s+200) + (Bs+C)\,s$$

- $s = 0$: $\;200A = 150 \Rightarrow A = \dfrac{3}{4}$.
- Coef. $s^2$: $\;0 = A + B \Rightarrow B = -\dfrac{3}{4}$.
- Coef. $s^1$: $\;0 = 20A + C \Rightarrow C = -15$.

$$Q(s) = \frac{3/4}{s} + \frac{-\frac{3}{4}s - 15}{s^2 + 20s + 200}$$

## 4. Completar cuadrados y preparar la inversa

$$s^2 + 20s + 200 = (s+10)^2 + 100 = (s+10)^2 + 10^2$$

Reescribimos el numerador en términos de $(s+10)$:

$$-\tfrac{3}{4}s - 15 = -\tfrac{3}{4}(s+10) - 7{,}5$$

$$Q(s) = \frac{3}{4}\cdot\frac{1}{s} - \frac{3}{4}\cdot\frac{s+10}{(s+10)^2 + 10^2} - \frac{3}{4}\cdot\frac{10}{(s+10)^2 + 10^2}$$

(usando $-7{,}5 = -\tfrac{3}{4}\cdot 10$, lo que forma la transformada del seno).

## 5. Transformada inversa — carga $q(t)$

Con $\mathcal{L}^{-1}\!\left\{\dfrac{s+10}{(s+10)^2+10^2}\right\} = e^{-10t}\cos 10t$ y $\mathcal{L}^{-1}\!\left\{\dfrac{10}{(s+10)^2+10^2}\right\} = e^{-10t}\sin 10t$:

> [!success] Carga
> $$\boxed{\,q(t) = \frac{3}{4}\Bigl(1 - e^{-10t}\cos 10t - e^{-10t}\sin 10t\Bigr)\,}$$

## 6. Corriente $I(t) = q'(t)$

Derivando $q(t) = \tfrac34 - \tfrac34 e^{-10t}\cos 10t - \tfrac34 e^{-10t}\sin 10t$:

$$\frac{d}{dt}\bigl[-\tfrac34 e^{-10t}\cos 10t\bigr] = \tfrac{30}{4}e^{-10t}\cos 10t + \tfrac{30}{4}e^{-10t}\sin 10t$$
$$\frac{d}{dt}\bigl[-\tfrac34 e^{-10t}\sin 10t\bigr] = \tfrac{30}{4}e^{-10t}\sin 10t - \tfrac{30}{4}e^{-10t}\cos 10t$$

Los términos en $\cos 10t$ se cancelan y los de $\sin 10t$ suman $\tfrac{30}{4}+\tfrac{30}{4} = 15$:

> [!success] Corriente
> $$\boxed{\,I(t) = 15\,e^{-10t}\sin 10t\,}$$

> [!warning] Corrección al guion del video
> El guion del video concluye la corriente como $I(t)=110\,e^{-10t}\sin 10t - 90\,e^{-10t}\cos 10t$, pero ese resultado **no se obtiene** al derivar la $q(t)$ hallada (que el propio video da bien). Derivando correctamente, los términos en $\cos 10t$ se anulan y queda $I(t)=15\,e^{-10t}\sin 10t$. Se trata de un error de transcripción/derivación del video; el valor verificado es $\boxed{I(t)=15\,e^{-10t}\sin 10t}$.

## Verificación de condiciones iniciales

- $q(0) = \tfrac34(1 - 1 - 0) = 0$. ✓
- $I(0) = 15\,e^{0}\sin 0 = 0$. ✓
- Régimen permanente: $q_\infty = \tfrac34\text{ C} = C\cdot E = 0{,}005\cdot 150$. ✓

## Conceptos aplicados

- Mismo método que [[S14-3 Tema 01 - Ejercicio 2 - Circuito RLC carga y corriente|Ej 2]] (Kirchhoff → EDO → Laplace → fracciones parciales → inversa).
- [[S14-1 Tema 01 - Transformadas de Laplace#7. Transformada inversa de Laplace|Transformada inversa]].

## Bibliografía

- Hsu, H. P., & Ward, J. (1991). *Transformada de Laplace*. McGraw-Hill / Interamericana de México.
