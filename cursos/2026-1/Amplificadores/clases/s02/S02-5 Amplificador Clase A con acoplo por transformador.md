---
title: "Amplificador Clase A con acoplo por transformador"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 2
orden: 5
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/amplificador-de-potencia
  - tema/amplificador-clase-a
  - tema/transformador
  - tema/eficiencia
date: 2026-04-07
---

## Introduccion

A diferencia del [[S02-3 Amplificadores de potencia - Clase A|acoplo directo]], en esta configuracion se coloca un **transformador** entre el colector y la carga $R_L$. Esto **separa las rectas de carga DC y AC**, permitiendo mayor excursion de senal y mayor eficiencia.

## Circuito

El primario del transformador se conecta entre $V_{CC}$ y el colector del transistor. La carga $R_L$ se conecta al secundario.

- El primario tiene resistencia DC muy baja → en DC el transistor "ve" practicamente un cortocircuito a $V_{CC}$
- En AC, el transistor ve la **carga reflejada**: $R_L' = a^2 R_L$

Donde:
- $a = N_1 / N_2$ = relacion de vueltas del transformador
- $R_L'$ = resistencia de carga reflejada al primario

## Rectas de carga

| Recta | Pendiente | Descripcion |
| ----- | --------- | ----------- |
| **DC (rcc)** | $\approx 0$ (casi horizontal) | Resistencia del primario despreciable |
| **AC (rca)** | $-1/R_L'$ | El transistor ve $R_L' = a^2 R_L$ |

> [!important] Diferencia clave con acoplo directo
> En acoplo directo la recta DC = recta AC (misma pendiente). Con transformador son **diferentes**, lo que permite mayor excursion de $V_{CE}$.

## Punto Q optimo

$$V_{CEQ} = V_{CC}$$

$$I_{CQ} = \frac{V_{CC}}{R_L'} = \frac{V_{CC}}{a^2 R_L}$$

## Excursion de $V_{CE}$

Como $V_{CEQ} = V_{CC}$, la senal puede oscilar simetricamente:

$$V_{CE\,min} = 0 \qquad V_{CE\,max} = 2V_{CC}$$

Esto es el **doble** que en acoplo directo, donde $V_{CE}$ solo llega hasta $V_{CC}$.

## Potencia en la carga

$$\boxed{P_L = \frac{V_{CC}^2}{2R_L'} = \frac{V_{CC}^2}{2a^2 R_L}}$$

## Potencia de la fuente

$$P_{CC} = V_{CC} \cdot I_{CQ} = \frac{V_{CC}^2}{R_L'}$$

## Eficiencia maxima

$$\boxed{\eta = \frac{P_L}{P_{CC}} = \frac{V_{CC}^2 / 2R_L'}{V_{CC}^2 / R_L'} = 0.50 = 50\%}$$

> [!success] El doble que acoplo directo
> La eficiencia maxima es **50%**, comparado con el 25% del [[S02-3 Amplificadores de potencia - Clase A|acoplo directo]].

## Relaciones de potencia

$$P_{D\,MAX} = P_{L\,MAX}$$

$$P_{CC} = 2 \cdot P_{L\,MAX}$$

## ¿Por que es mas eficiente?

1. **No hay potencia DC desperdiciada en la carga** — la resistencia DC del primario es $\approx 0$, asi que no existe $P_{L(DC)}$
2. **Mayor excursion de voltaje** — $V_{CE}$ oscila hasta $2V_{CC}$, extrayendo mas potencia de senal
3. **Adaptacion de impedancia** — el transformador permite ajustar $a$ para que $R_L'$ sea optima para el transistor

## Comparacion con acoplo directo

| Parametro | Acoplo directo | Acoplo por transformador |
| --------- | -------------- | ------------------------ |
| $\eta_{max}$ | 25% | **50%** |
| $V_{CE\,max}$ | $V_{CC}$ | $2V_{CC}$ |
| $P_D / P_L$ | 2 | 1 |
| $P_{CC} / P_L$ | 4 | 2 |
| Rectas DC = AC | Si | No |

## Bibliografia

- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson.
