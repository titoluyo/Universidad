---
title: "Ejercicio resuelto - Torque en un bucle de corriente"
curso: "[[Motores MOC]]"
unidad: 3
semana: 11
orden: 3
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/torque-electromagnetico
  - tema/momento-dipolar-magnetico
  - tema/energia-potencial-magnetica
date: 2026-06-01
---

> [!info] Material original
> Ejercicio en video del docente. Guion (transcripción): [s11-guion-ejercicio-torque.pdf](attachments/s11-guion-ejercicio-torque.pdf) (UTP, Semana 11).

## Enunciado

Un **bucle circular** de radio $r = 2\ \text{cm}$ conduce una corriente de $I = 2\ \text{mA}$. Se pide calcular:

1. ¿Cuál es la magnitud de su **momento dipolar magnético**?
2. Si el dipolo está orientado a $\theta = 30°$ respecto a un **campo magnético uniforme** de magnitud $B = 0{,}5\ \text{T}$, ¿cuál es la magnitud del **torque** que experimenta y cuál es su **energía potencial**?

> [!note] Datos
> - Radio: $r = 2\ \text{cm} = 0{,}02\ \text{m}$
> - Corriente: $I = 2\ \text{mA} = 0{,}002\ \text{A}$
> - Campo magnético: $B = 0{,}5\ \text{T}$
> - Ángulo: $\theta = 30°$

## Estrategia

- El **momento dipolar** se define como la corriente por el área del bucle, $\mu = I\cdot A$. El área del bucle es la del círculo, $A = \pi r^2$.
- El **torque** y la **energía potencial** se calculan a partir del momento magnético, el campo magnético y el ángulo entre ambos vectores:
$$\vec{\tau} = \vec{\mu}\times\vec{B} \quad\Rightarrow\quad \tau = \mu B\sin\theta \qquad\qquad U = -\vec{\mu}\cdot\vec{B} = -\mu B\cos\theta$$

Las expresiones provienen del [[S11-2 Tema 01 - Torques de origen electromagnético|Tema 01 — Torques]].

## Desarrollo

### 1) Momento dipolar magnético

El área del bucle circular:

$$A = \pi r^2 = \pi\,(0{,}02\ \text{m})^2 = 1{,}2566\times10^{-3}\ \text{m}^2$$

El momento dipolar magnético:

$$\mu = I\cdot A = (0{,}002\ \text{A})\,(1{,}2566\times10^{-3}\ \text{m}^2)$$

$$\boxed{\mu \approx 2{,}5\times10^{-6}\ \text{A}\cdot\text{m}^2}$$

### 2) Torque

$$\tau = \mu\,B\,\sin\theta = (2{,}5\times10^{-6}\ \text{A}\cdot\text{m}^2)(0{,}5\ \text{T})\,\sin 30°$$

$$\tau = (2{,}5\times10^{-6})(0{,}5)(0{,}5)$$

$$\boxed{\tau \approx 6{,}3\times10^{-7}\ \text{N}\cdot\text{m}}$$

### 3) Energía potencial

$$U = -\mu\,B\,\cos\theta = -(2{,}5\times10^{-6}\ \text{A}\cdot\text{m}^2)(0{,}5\ \text{T})\,\cos 30°$$

$$U = -(2{,}5\times10^{-6})(0{,}5)(0{,}866)$$

$$\boxed{U \approx -1{,}1\times10^{-6}\ \text{J}}$$

> [!success] Resultados
> | Magnitud | Valor |
> | --- | --- |
> | Momento dipolar magnético $\mu$ | $2{,}5\times10^{-6}\ \text{A}\cdot\text{m}^2$ |
> | Torque $\tau$ | $6{,}3\times10^{-7}\ \text{N}\cdot\text{m}$ |
> | Energía potencial $U$ | $-1{,}1\times10^{-6}\ \text{J}$ |

> [!note] Lectura física
> La **energía potencial es negativa** porque el momento dipolar tiende a **alinearse con el campo** ($\theta < 90°$): el estado más estable es $\theta = 0°$ ($U = -\mu B$, mínimo) y el de máxima energía es $\theta = 180°$. El **torque** $\tau = \mu B\sin\theta$ es precisamente el que empuja al dipolo hacia esa alineación.

## Bibliografía

- Moebs, W., Ling, S. J., y Sanny, J. (2022). *Fuerza y torque en un bucle de corriente*. En *Física universitaria volumen 2*. OpenStax College.
- Pretel Díaz, Ch. H. (2026). *Ejercicio de torque* [Video – Guion]. UTP+class.
