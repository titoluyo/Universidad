---
title: Polaridad y conversión de impedancias en el transformador ideal
curso: "[[Motores MOC]]"
unidad: 2
semana: 6
orden: 6
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/transformador-ideal
  - tema/polaridad-puntos
  - tema/impedancia-reflejada
  - tema/conversion-impedancias
date: 2026-04-27
---

![[s06-t02-pol-banner.jpg]]

## Polaridad: la convención de puntos

![[s06-t02-pol-fig1-simbologia-trafo-puntos.png]]
*Figura 1. Simbología de un transformador ideal.*

Los **puntos** que aparecen en un extremo de cada devanado en la figura de arriba muestran la **polaridad del voltaje y de la corriente** en el lado secundario del transformador. La relación es la siguiente:

> [!summary] Regla de los puntos (dot convention)
> - Si la polaridad del voltaje en un extremo marcado del **devanado primario es positiva**, entonces la polaridad del voltaje en el extremo marcado del **devanado secundario también será positiva**.
> - En el caso de que la corriente fluya **hacia el interior** en el extremo señalado del devanado primario, la corriente en el extremo señalado del devanado secundario fluirá **hacia afuera**.

> [!note] Por qué importa
> Sin la convención de puntos, no hay forma de saber a qué lado del secundario sale la tensión positiva. Cuando dos transformadores se conectan en paralelo o se hace un autotransformador, **un cruce de polaridades produce un cortocircuito** — la convención existe para evitar este error de cableado.

## Impedancias en el transformador ideal

La **impedancia** de un dispositivo o elemento se establece como la proporción entre el voltaje fasorial que atraviesa dicho elemento y la corriente fasorial que circula por él. Por ende, la impedancia en la carga será:

$$\mathbf{Z}_L = \frac{\mathbf{V}_S}{\mathbf{I}_S}$$

![[s06-t02-pol-fig2-impedancia-trafo.png]]
*Figura 2. Impedancia a través de un transformador.*

### Impedancia reflejada al primario

La **impedancia aparente del circuito primario** del transformador es:

$$\mathbf{Z}_L^{\prime} = \frac{\mathbf{V}_P}{\mathbf{I}_P}$$

Reemplazando con las [[S06-4 Tema 02 - El transformador monofásico ideal#Relación de transformación|relaciones de transformación]] $\mathbf{V}_P = a\,\mathbf{V}_S$ y $\mathbf{I}_P = \mathbf{I}_S/a$:

$$\mathbf{Z}_L^{\prime} = \frac{\mathbf{V}_P}{\mathbf{I}_P} = \frac{a\,\mathbf{V}_S}{\dfrac{\mathbf{I}_S}{a}} = a^2 \cdot \mathbf{Z}_L$$

> [!success] Fórmula clave
> $$\boxed{\;\mathbf{Z}_L^{\prime} = a^2 \cdot \mathbf{Z}_L\;}$$
>
> La impedancia conectada al secundario **se refleja al primario multiplicada por $a^2$**.

**Donde:**
- $a = N_P/N_S$ — relación de transformación (adimensional).
- $\mathbf{Z}_L$ — impedancia conectada al secundario ($\Omega$).
- $\mathbf{Z}_L^{\prime}$ — impedancia equivalente vista desde el primario ($\Omega$).

> [!tip] Aplicación: adaptación de impedancias
> Esta propiedad permite que un transformador actúe como **adaptador de impedancias**. Por ejemplo, en audio se usan transformadores para acoplar un altavoz de baja impedancia (4–8 Ω) a la salida de alta impedancia de un amplificador a válvulas: se elige $a$ tal que $a^2 \cdot Z_L$ coincida con la impedancia de salida deseada.

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
