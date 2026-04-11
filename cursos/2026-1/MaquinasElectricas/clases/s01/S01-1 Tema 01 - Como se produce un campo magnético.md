---
title: Como se produce un campo magnetico
curso: "[[Motores MOC]]"
unidad: 1
semana: 1
orden: 1
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/campo-magnetico
  - tema/ley-de-ampere
date: 2026-03-28
---

## 1. ¿Qué es un campo magnético?

Un campo magnético es una descripción matemática de la influencia magnética de las corrientes eléctricas y de los materiales magnéticos. Existen cuatro principios básicos que describen cómo se utilizan los campos magnéticos:

1. Un conductor que porta corriente produce un campo magnético a su alrededor.

2. Un campo magnético variable en el tiempo induce un voltaje en una bobina de alambre si pasa a través de ella.

3. Un conductor que porta corriente en presencia de un campo magnético experimenta una fuerza inducida sobre él.

4. Un conductor eléctrico que se mueva en presencia de un campo magnético tendrá un voltaje inducido en él.

## 2. ¿Cómo se produce un campo magnético?

La ley básica que gobierna la producción de un campo magnético por medio de una corriente es la ley de Ampère:

$$\oint \vec{H} \cdot d\vec{l} = I_{\text{neta}}$$

Donde:

- $H$ es la intensidad del campo magnético producida por la corriente.
- $dl$ es el elemento diferencial a lo largo de la trayectoria de integración.

En unidades del SI, $I$ se mide en amperes y $H$ en amperes-vuelta por metro.

![[Figura 1. Un núcleo magnético sencillo.png]]
**Figura 1.** Un núcleo magnético sencillo

### Explicación de la Figura 1

Si el núcleo es de hierro o de ciertos metales similares, llamados [[S01-7 Tema 05 - Obtencion de la curva de magnetizacion|materiales ferromagnéticos]], casi todo el campo magnético producido por la corriente permanecerá dentro del núcleo, de modo que el camino de integración especificado en la ley de Ampère es la longitud media del núcleo $l_n$. La corriente que pasa por el camino de integración $I_{\text{neta}}$ es entonces $Ni$, puesto que la bobina de alambre corta dicho camino $N$ veces mientras pasa la corriente $i$. La ley de Ampère se expresa entonces como:

$$H \cdot l_n = N \cdot i$$

La potencia del campo magnético producido en el núcleo depende también del material de que está hecho. La relación entre la intensidad del campo magnético $H$ y la densidad del flujo magnético resultante $B$ producida dentro del material está dada por:

$$B = \mu H$$

Donde:

- $H$ = intensidad del campo magnético, se mide en ampere-vueltas por metro.
- $\mu$ = permeabilidad magnética del material, se mide en henrys por metro.
- $B$ = densidad de flujo magnético resultante, se mide en webers por metro cuadrado, conocido como teslas (T).

## Ejemplo

La permeabilidad del vacío (aire) se denomina $\mu_0$, y su valor es:

$$\mu_0 = 4\pi \times 10^{-7} \, \mathrm{H/m}$$

La permeabilidad de cualquier material comparada con la del espacio libre se denomina permeabilidad relativa: 

$$\mu_r = \frac{\mu}{\mu_0}$$

En un núcleo, la magnitud de la densidad de flujo está dada por:

$$B = \mu H = \frac{\mu N i}{l_n}$$

Ahora, el flujo total en cierta área está dado por:

$$\phi = \int_A B \, dA$$

Toma en cuenta lo siguiente: si el valor $B$ es constante, el flujo total sería $BA$.

De esta forma, el flujo total en el núcleo de la figura 1, producido por la corriente $i$ en el devanado, es:

$$\phi = BA = \frac{\mu N i A}{l_n}$$

Donde $A$ es el área de la sección transversal del núcleo.

---

> [!tip] Simulador
> Puedes continuar explorando el funcionamiento de un campo magnético en el siguiente simulador:
> [Abrir simulador PhET - Faraday](https://phet.colorado.edu/sims/cheerpj/faraday/latest/faraday.html?simulation=faraday&locale=es_PE)

## Bibliografía

- Chapman, S. J. (2012). _Máquinas Eléctricas_ (5a. ed.). McGraw-Hill Interamericana.
