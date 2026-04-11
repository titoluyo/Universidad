---
title: Los circuitos magneticos
curso: "[[Motores MOC]]"
unidad: 1
semana: 1
orden: 2
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/circuito-magnetico
  - tema/reluctancia
  - tema/ley-de-hopkinson
date: 2026-03-28
---

Las líneas de [[S01-1 Tema 01 - Como se produce un campo magnético|campo magnético]] de una corriente continua rectilínea forman círculos concéntricos alrededor del hilo conductor. La dirección del campo magnético viene dada por la regla de la mano derecha: cuando el pulgar de la mano derecha señala la dirección de la corriente, los otros dedos rodean el hilo conductor en la dirección del campo magnético.
## Circuitos magnéticos a partir de los eléctricos

Mira el siguiente video para conocer más sobre los circuitos magnéticos:

[Video: circuitos magnéticos](https://www.youtube.com/watch?v=C87IiWG4U-4)
En un circuito eléctrico, el voltaje aplicado ocasiona un flujo de corriente I. En forma similar, en un circuito magnético, la fuerza magnetomotriz aplicada ocasiona un flujo. La relación entre voltaje y corriente en un circuito eléctrico está dada por la ley de Ohm (I = V / R); en forma semejante a la ley de Hopkinson, la relación entre la fuerza magnetomotriz y el flujo es:

$$\phi = \frac{F}{R}$$

Donde:

- $F$ = Fuerza magnetomotriz del circuito
- $\phi$ = Flujo del circuito
- $R$ = Reluctancia del núcleo

## La reluctancia

La reluctancia de un núcleo magnético es el homólogo de la resistencia del circuito eléctrico y se mide en **amperes-vueltas por weber**.

Existe también un análogo magnético de la conductancia. Así como la conductancia en el circuito eléctrico es el inverso de su resistencia, la permeancia **P** de un circuito magnético es el inverso de su reluctancia:

$$P = \frac{1}{R}$$

La relación entre la fuerza magnetomotriz y el flujo se puede expresar como:

$$\phi = F \cdot P$$

## ¿Cuál es la reluctancia en el núcleo?

En el núcleo el flujo está dado por la ecuación:

$$\phi = B \cdot A = \frac{\mu \cdot N \cdot i \cdot A}{l_n} = N \cdot i \cdot \frac{\mu \cdot A}{l_n} = F \cdot \frac{\mu \cdot A}{l_n}$$

Se observa que la reluctancia del núcleo es:

$$R = \frac{l_n}{\mu \cdot A}$$

En un circuito magnético las reluctancias obedecen las mismas reglas que las resistencias en un circuito eléctrico:

- En serie:

$$R_{eq} = R_1 + R_2 + R_3 + \cdots$$

- En paralelo:

$$\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \cdots$$

Las permeancias en serie y en paralelo obedecen las mismas reglas que las conductancias eléctricas.

## Ejercicio

En la siguiente figura 1 se observa un núcleo ferromagnético. Tres lados de este núcleo tienen una anchura uniforme, mientras que el cuarto es un poco más delgado. La profundidad del núcleo visto es de 10 cm, mientras que las demás dimensiones se muestran en la figura 1. Hay una bobina de 200 vueltas enrollada sobre el lado izquierdo del núcleo. Si la permeabilidad relativa $\mu_r$ es de 2 500, ¿qué cantidad de flujo producirá una corriente de 1 A en la bobina?

![[Figura 1. Núcleo ferromagnético del núcleo.png]]
**Figura 1.** Núcleo ferromagnético del núcleo

Solución:

Tres lados del núcleo tienen la misma área en la sección transversal, mientras que el cuarto lado tiene un área diferente. Entonces, se puede dividir el núcleo en dos regiones: 1) la correspondiente al lado más delgado y 2) la que forman los otros tres lados en conjunto.

El circuito magnético correspondiente a este núcleo se muestra en la figura 2.
![[Figura 2. Circuito magnético equivalente.png]]
**Figura 2.** Circuito magnético equivalente

La longitud media de la región 1 es de 45 cm y el área transversal de 10 x 10 cm = 100 $cm^2$. De esta forma, la reluctancia de la región es:

$$R_1 = \frac{l_1}{\mu_r \cdot \mu_0 \cdot A_1} = \frac{0.45 \, \mathrm{m}}{(2500) \cdot (4\pi \times 10^{-7}) \cdot (0.01 \, \mathrm{m^2})} = 14300 \, \mathrm{A \cdot \frac{espiras}{Wb}}$$

La longitud media de la región 2 es de 130 cm y el área de la sección transversal es de 15 x 10 cm = 150 $cm^2$. De esta forma, la reluctancia de esta región es:

$$R_2 = \frac{l_2}{\mu_r \cdot \mu_0 \cdot A_2} = \frac{1.3 \, \mathrm{m}}{(2500) \cdot (4\pi \times 10^{-7}) \cdot (0.015 \, \mathrm{m^2})} = 27600 \, \mathrm{A \cdot \frac{espiras}{Wb}}$$

Por lo tanto, la reluctancia total del núcleo es:

$$R_{eq} = R_1 + R_2 = 41900 \, \mathrm{A \cdot \frac{espiras}{Wb}}$$

La fuerza magnetomotriz total es:

$$F = N \cdot i = (200 \, \mathrm{espiras}) \cdot (1 \, \mathrm{A}) = 200 \, \mathrm{A \cdot espiras}$$

El flujo total en el núcleo está dado por:

$$\phi = \frac{F}{R} = \frac{200 \, \mathrm{A \cdot espiras}}{41900 \, \mathrm{A \cdot \frac{espiras}{Wb}}} = 0.0048 \, \mathrm{Wb}$$

## Bibliografía

- Chapman, S. J. (2012). _Máquinas Eléctricas_ (5a. ed.). McGraw-Hill Interamericana.
