---
title: Ejercicio resuelto - Parámetros del transformador ideal
curso: "[[Motores MOC]]"
unidad: 2
semana: 6
orden: 5
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/transformador-ideal
  - tema/relacion-transformacion
  - tema/factor-potencia
date: 2026-04-27
---

> [!info] Fuente
> Video "Desarrollo de un ejercicio de parámetros del transformador ideal" (Semana 06, Tema 02). Transcripción completa en [[#Guion del video|el Guion]] adjunto al final.

## Enunciado

Un transformador monofásico de relación de transformación de **400 V a 230 V** suministra a una carga **600 W** de potencia a 230 V. Considerando el transformador **ideal** y un **factor de potencia de 0,9 inductivo**, calcular:

- **a)** La relación de transformación.
- **b)** La intensidad que suministra el transformador en el secundario $I_S$.
- **c)** La intensidad $I_P$ que circula por el primario.

## Datos

| Magnitud | Símbolo | Valor |
| -------- | ------- | ----- |
| Tensión primaria | $V_P$ | 400 V |
| Tensión secundaria | $V_S$ | 230 V |
| Potencia activa de la carga | $P_{out}$ | 600 W |
| Factor de potencia | $\cos\theta$ | 0,9 inductivo |

## Desarrollo

### a) Relación de transformación

Aplicando la [[S06-4 Tema 02 - El transformador monofásico ideal#Relación de voltajes|relación de voltajes del transformador ideal]]:

$$\frac{V_P}{V_S} = \frac{N_P}{N_S} = a$$

Reemplazando los valores del enunciado:

$$a = \frac{400\,\text{V}}{230\,\text{V}} = 1{,}74$$

> [!success] Resultado (a)
> $\boxed{a \approx 1{,}74}$

### b) Intensidad en el secundario $I_S$

Como el transformador es **ideal**, la [[S06-4 Tema 02 - El transformador monofásico ideal#Conservación de la potencia|potencia se conserva]]:

$$P_{in} = P_{out} = 600\,\text{W}$$

El ángulo del factor de potencia:

$$\theta_S = \cos^{-1}(0{,}9) = 25{,}8^{\circ}$$

La potencia activa de salida es:

$$P_{out} = V_S \cdot I_S \cdot \cos\theta_S$$

Despejando $I_S$:

$$I_S = \frac{P_{out}}{V_S \cdot \cos\theta_S} = \frac{600}{230 \cdot 0{,}9} = \frac{600}{207}$$

$$\boxed{I_S \approx 2{,}89\,\text{A}}$$

### c) Intensidad en el primario $I_P$

En un transformador ideal el ángulo de fase es el mismo en ambos lados:

$$\theta_P = \theta_S = \theta = 25{,}8^{\circ}$$

Trabajando con la potencia en el primario:

$$P_{in} = V_P \cdot I_P \cdot \cos\theta_P$$

$$600 = 400 \cdot I_P \cdot 0{,}9$$

Despejando $I_P$:

$$I_P = \frac{600}{400 \cdot 0{,}9} = \frac{600}{360}$$

$$\boxed{I_P \approx 1{,}67\,\text{A}}$$

### Verificación con la relación de corrientes

Aplicando $\dfrac{I_P}{I_S} = \dfrac{1}{a}$:

$$I_P = \frac{I_S}{a} = \frac{2{,}89}{1{,}74} \approx 1{,}66\,\text{A}\;\checkmark$$

La diferencia con $1{,}67$ A se debe al redondeo de $a$ y $I_S$ a dos decimales.

## Resumen de resultados

| Magnitud | Valor |
| -------- | ----- |
| Relación de transformación $a$ | $1{,}74$ |
| Corriente secundaria $I_S$ | $2{,}89\,\text{A}$ |
| Corriente primaria $I_P$ | $1{,}67\,\text{A}$ |
| Ángulo del fp $\theta$ | $25{,}8^{\circ}$ |

> [!tip] Lectura física
> Como en este transformador $V_P > V_S$ ($a > 1$), es un transformador **reductor**. Al reducir la tensión, **eleva** la corriente para mantener la potencia (1,67 A → 2,89 A).

## Guion del video

![[s06-t02-ej1-guion-parametros-trafo-ideal.pdf]]

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
