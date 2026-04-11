---
title: Ejercicio de la ley de Ampere
curso: "[[Motores MOC]]"
unidad: 1
semana: 1
orden: 6
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/ley-de-ampere
  - tema/toroide
date: 2026-03-28
---

> [!info] Fuente
> Video: [Semana 1 - Ley de Ampere - Campo magnético de un toroide](https://www.youtube.com/watch?v=D-6v7CYDOV8) — Aprendizaje Virtual UTP (3:41)

## Enunciado

Un toroide con núcleo de aire uniformemente enrollado tiene **750 vueltas**. El radio que pasa en su centro y su devanado es de **5 cm**. ¿Qué corriente en el devanado producirá una densidad de flujo de $1{,}8 \times 10^{-3}$ T?

![[video-ampere-enunciado.png]]
**Figura 1.** Enunciado del problema

### Datos

- $N = 750$ vueltas
- $r = 5 \, \text{cm} = 0{,}05 \, \text{m}$
- $B = 1{,}8 \times 10^{-3} \, \text{T}$
- Núcleo de aire ($\mu_r = 1$)
- $\mu_0 = 4\pi \times 10^{-7} \, \text{H/m}$

---

## Resolución

### Paso 1: Ecuación de partida

Aplicando la [[S01-1 Tema 01 - Como se produce un campo magnético|ley de Ampère]] para un [[S01-5 Tema 04 - Campo magnetico de un toroide|toroide]]:

$$B \cdot S = \mu_0 \cdot N \cdot I \cdot S$$

Simplificando la sección $S$ y sabiendo que para un toroide la longitud de la línea media magnética es $l = 2\pi r$:

$$B = \mu_0 \cdot \frac{N \cdot I}{2\pi r}$$

### Paso 2: Despejar la corriente $I$

$$I = \frac{B \cdot 2\pi r}{\mu_0 \cdot N}$$

### Paso 3: Reemplazar valores

$$I = \frac{1{,}8 \times 10^{-3} \times 2\pi \times 0{,}05}{4\pi \times 10^{-7} \times 750}$$

![[video-ampere-resultado.png]]
**Figura 2.** Desarrollo y resultado del ejercicio

$$I = \frac{1{,}8 \times 10^{-3} \times 0{,}1\pi}{4\pi \times 10^{-7} \times 750}$$

$$\boxed{I = 0{,}6 \, \text{A}}$$

---

## Resultado

La corriente que debe circular por el devanado del toroide para producir una densidad de flujo de $1{,}8 \times 10^{-3}$ T es de **0,6 amperios**.
