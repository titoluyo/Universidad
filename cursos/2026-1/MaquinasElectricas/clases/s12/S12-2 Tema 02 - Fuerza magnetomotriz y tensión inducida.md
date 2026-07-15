---
title: "Tema 02 - Fuerza magnetomotriz y tensión inducida"
curso: "[[Motores MOC]]"
unidad: 3
semana: 12
orden: 2
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/fuerza-magnetomotriz
  - tema/tension-inducida
  - tema/fem
  - tema/par-inducido
  - tema/maquina-dc
date: 2026-06-08
---

![[S12 - B1.png]]

## La fuerza electromotriz (FEM)

La **fuerza electromotriz (FEM)** o **voltaje inducido** es una acción eléctrica medida en voltios, generada por fuentes **no eléctricas** como baterías o generadores. Los transductores eléctricos convierten otras formas de energía en energía eléctrica para proporcionar FEM; esta conversión se logra **aplicando trabajo físico sobre cargas eléctricas**.

La FEM puede **mantener una diferencia de potencial** en un circuito abierto o **generar corriente** en uno cerrado, siendo una característica de cada generador eléctrico. En inducción electromagnética, la FEM se define como el **trabajo electromagnético realizado sobre una carga** al moverse alrededor de una espira cerrada de un conductor.

![[T02 - Figura 1. Fuerza electromotriz (FEM).png]]
> **Figura 1.** Fuerza electromotriz (FEM).

## El voltaje en la espira giratoria

Si el rotor está en movimiento, se genera una fuerza electromotriz en la espira de alambre. La espira es **rectangular**, con sus lados **AB y CD perpendiculares** al plano y los lados **BC y DA paralelos**. El campo magnético es **uniforme y perpendicular** a la superficie del rotor bajo las caras polares, y **disminuye rápidamente a cero** más allá de los bordes de los polos.

El voltaje inducido en un segmento de conductor es:

$$e_{ind} = (\vec{v}\times\vec{B})\cdot\vec{l}$$

![[T02 - Figura 2. Deduccion del voltaje inducido en la espira.png]]
> **Figura 2.** Deducción de la ecuación del voltaje inducido en la espira.

**Segmentos ab y cd.** Bajo la cara polar, la velocidad $\vec{v}$ es perpendicular a $\vec{B}$ y el producto $\vec{v}\times\vec{B}$ apunta a lo largo del conductor. El voltaje inducido es:

$$e_{ba} = e_{cd} = (\vec{v}\times\vec{B})\cdot\vec{l}$$

**Segmentos bc y da.** Aquí $\vec{v}\times\vec{B}$ es **perpendicular a $\vec{l}$**, por lo que:

$$e_{cb} = e_{da} = 0$$

El **voltaje total inducido** en la espira es:

$$e_{ind} = e_{ba} + e_{cb} + e_{dc} + e_{ad} = 2\,(\vec{v}\times\vec{B})\cdot\vec{l}$$

![[T02 - Figura 3. Voltaje de salida de la espira.png]]
> **Figura 3.** Voltaje de salida de la espira: alterna mientras la espira está bajo los polos y se anula en la línea neutra.

## El par inducido en la espira giratoria

¿Cuánto par se produce cuando se cierra el interruptor y fluye corriente por la espira? La magnitud de la **fuerza** en un segmento es:

$$\vec{F} = i\,(\vec{l}\times\vec{B})$$

Y el **par**:

$$\tau = r\cdot F\cdot \sin\theta$$

donde $\theta$ es el ángulo entre $\vec{r}$ y $\vec{F}$. El par es esencialmente **cero** cuando la espira está más allá del borde de los polos.

![[T02 - Figura 4. Deduccion del par inducido en la espira.png]]
> **Figura 4.** Deducción de la ecuación del par inducido en la espira.

**Segmentos ab y cd.** El campo bajo las caras polares apunta radialmente hacia afuera, por lo que la fuerza es:

$$F_{ab} = F_{cd} = i\,(\vec{l}\times\vec{B}) = i\,l\,B\;\hat{u}_z$$

El par en el rotor provocado por esta fuerza (con $\theta = 90°$) es:

$$\tau_{ab} = \tau_{cd} = r\cdot F\cdot\sin\theta = r\,(i\,l\,B)\,\sin 90° = r\,i\,l\,B$$

**Segmentos bc y da.** Como $\vec{l}$ es **paralela a $\vec{B}$**:

$$F_{bc} = F_{da} = 0 \qquad ;\qquad \tau_{bc} = \tau_{da} = 0$$

![[T02 - Figura 5. Vista frontal del par inducido en la espira.png]]
> **Figura 5.** Vista frontal del par inducido en la espira.

El **par total inducido** resultante es:

$$\tau_{ind} = 2\,r\,(i\,l\,B)$$

Dado que el área bajo cada polo es $A_P \approx \pi r l$ y el flujo $\phi = A_P\cdot B$, la expresión se reduce a:

$$\boxed{\tau_{ind} = \frac{2}{\pi}\,\phi\,i}$$

> [!summary] El par depende de tres factores
> El par de cualquier máquina real se obtiene multiplicando el **flujo** y la **corriente** en la máquina, por un factor que representa su **estructura mecánica** (el porcentaje del rotor cubierto por las caras polares). En resumen, el par depende de:
> 1. El **flujo** en la máquina.
> 2. La **corriente** en la máquina.
> 3. Una **constante** que caracteriza su construcción.
>
> Aplicación numérica completa (espira giratoria entre caras polares) en el [[S12-3 Ejercicio resuelto - Máquina elemental DC (Video)|ejercicio resuelto]].

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
