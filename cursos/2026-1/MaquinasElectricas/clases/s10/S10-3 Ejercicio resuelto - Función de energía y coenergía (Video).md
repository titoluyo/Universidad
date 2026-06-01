---
title: "Ejercicio resuelto - Función de energía y coenergía (video del docente)"
curso: "[[Motores MOC]]"
unidad: 3
semana: 10
orden: 3
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/energia-magnetica
  - tema/coenergia-magnetica
  - tema/electroiman
  - tema/balance-energia
date: 2026-05-25
---

> [!info] Origen del material
> Video explicativo del docente (Ch. H. Pretel Díaz, 2:55 min). Guion completo: [s10-guion-ejercicio-energia-coenergia.pdf](attachments/s10-guion-ejercicio-energia-coenergia.pdf). Recurso descargable en el portal: `.MP4`, `.MP3` y `.PDF`.

## Enunciado / dispositivo de estudio

Considera el dispositivo de la figura: un **núcleo tipo "O" abierto**, formado por dos piezas metálicas de **acero magnético**:

- Una pieza fija con forma de "C" (base) sobre la que está enrollada la bobina.
- Una pieza con forma de "**I**" acoplada a una base fija mediante un **resorte**; esta pieza se puede mover en la dirección "$X$".

La bobina tiene **$n$ vueltas**, es alimentada por una tensión $V$ y circula por ella una corriente $i$. El **enlace de flujo** vale:

$$\lambda = n\,\phi$$

donde $\phi$ es el flujo magnético que circula por el hierro.

> [!example] Diagrama de referencia
> El video utiliza el mismo dispositivo que la **Figura 1 del [[S10-2 Tema 02 - Función de energía y coenergía|Tema 02]]**: ver [s10-t2-fig1-conversion-energia.png](attachments/s10-t2-fig1-conversion-energia.png).

## Idea del experimento

**Fijemos** el dispositivo en una posición "$X$" (la pieza "I" inmóvil) y vamos **aumentando la corriente desde 0 hasta un valor final $i_1$**. A medida que $i$ crece:

1. El núcleo se va **magnetizando** y se establece un campo magnético en su interior.
2. La curva $\lambda$ vs $i$ crece **linealmente** al principio.
3. A partir de cierto punto la curva empieza a **saturarse** (el hierro deja de magnetizarse proporcionalmente).

## Balance de energía

La **variación de la energía electromagnética** suministrada por la fuente es igual a la suma de:

- La **variación de la energía almacenada en el campo** $dW_c$.
- La **variación de la energía mecánica** $dW_{\text{mec}} = F\,dx$ (fuerza por desplazamiento mecánico).

Sabiendo además que la variación de energía electromagnética entregada por la fuente es $i\,d\lambda$, resulta el balance fundamental:

$$i\,d\lambda \;=\; dW_c \;+\; F\,dx$$

> [!important] Condición experimental: pieza fija
> Si **mantenemos la pieza "I" fija** en una posición $X$, entonces $dx = 0$ y por lo tanto $F\,dx = 0$.
>
> El balance se reduce a:
>
> $$dW_c = i\,d\lambda$$
>
> Integrando desde $\lambda = 0$ hasta $\lambda = \lambda_1$:
>
> $$W_c \;=\; \int_{0}^{\lambda_1} i\,d\lambda$$

## Interpretación gráfica

Sobre la curva $\lambda$–$i$ (ver figura del video, equivalente a la **Figura 3** del [[S10-2 Tema 02 - Función de energía y coenergía|Tema 02]]):

| Región sobre la curva | Magnitud | Nombre |
| --------------------- | -------- | ------ |
| Área `0–b–c–0` (sobre la curva, entre la curva y el eje $\lambda$) | $W_c = \int_{0}^{\lambda_1} i\,d\lambda$ | **Energía magnética** almacenada en el campo |
| Área `0–a–b–0` (bajo la curva, entre la curva y el eje $i$) | $W'_c = \int_{0}^{i_1} \lambda\,di$ | **Coenergía** (definición auxiliar) |

> [!success] Suma de las dos áreas
> Ambas áreas son complementarias bajo el rectángulo $\lambda_1 \times i_1$:
>
> $$W_c + W'_c = \lambda_1 \cdot i_1$$
>
> En el **caso lineal** (sin saturación) ambas áreas son iguales: $W_c = W'_c = \tfrac{1}{2}\lambda_1\,i_1$.

## Cierre del docente

> Espero que esta explicación haya sido clara. Ahora que sabes más sobre energía y coenergía, te invito a continuar con nuestra sesión de aprendizaje. ¡Nos vemos!

## Notas para el laboratorio

> [!tip] Aplicación al LC2
> Este ejercicio aterriza los conceptos abstractos del [[S10-2 Tema 02 - Función de energía y coenergía|Tema 02]] en un dispositivo concreto (electroimán con armadura móvil) — exactamente la familia de dispositivos cuyo comportamiento se analiza en el [[S10-99 Laboratorio Calificado 2 - LC2|Laboratorio Calificado 2 (LC2)]]. Tener clara la **distinción $W_c$ vs $W'_c$** y la condición "$dx = 0$ ⇒ $dW_c = i\,d\lambda$" es la base para resolver los cálculos del informe.

## Bibliografía

- Pretel Díaz, Ch. H. (2026). *Guion – Coenergía* [Video y transcripción]. UTP+class.
