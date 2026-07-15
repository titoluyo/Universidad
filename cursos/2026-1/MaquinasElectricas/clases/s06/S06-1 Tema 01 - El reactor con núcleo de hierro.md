---
title: El reactor con núcleo de hierro
curso: "[[Motores MOC]]"
unidad: 2
semana: 6
orden: 1
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/transformador
  - tema/nucleo-magnetico
  - tema/laminacion-grano-orientado
  - tema/seccion-cruciforme
date: 2026-04-27
---

![[s06-t01-banner.jpg]]

## Introducción

El reactor con núcleo de hierro es el componente que da soporte físico al **circuito magnético** del transformador. Se construye con láminas de acero al silicio (carlite) cuya geometría y disposición buscan dos objetivos en simultáneo: reducir las pérdidas en el hierro y aprovechar al máximo el espacio dentro del devanado.

## 1. El núcleo

Se hace referencia al **núcleo del transformador** como el componente que configura su circuito magnético. Este núcleo está compuesto por **láminas de acero al silicio**, actualmente laminadas en frío con orientación de grano, que han sido sometidas a un tratamiento químico especial conocido comercialmente como **carlite**.

Este tratamiento proporciona a las láminas un recubrimiento aislante extremadamente delgado (0,01 mm), lo que resulta en una **significativa reducción de las pérdidas de hierro** (ver [[S05-1 Tema 01 - Perdidas magneticas en el nucleo|pérdidas por histéresis y Foucault]]).

![[s06-t01-fig1-nucleo-transformador.png]]
*Imagen 1. Núcleo del transformador.*

## 2. Características, propiedades y parámetros del núcleo

El conjunto magnético se conforma mediante:

- **Columnas:** secciones destinadas al montaje de los devanados.
- **Culatas:** establecen la conexión entre las columnas.
- **Ventanas del núcleo:** espacios por donde transcurren los devanados, situados entre las columnas y las culatas.

La clasificación de los transformadores como **acorazados** depende de la posición relativa entre el núcleo y los devanados: en su mayoría, los devanados se encuentran envueltos o protegidos por el núcleo magnético.

![[s06-t01-fig2-nucleo-acorazado.png]]
*Imagen 2. Circuito magnético con núcleo acorazado.*

En la imagen 3 podemos ver un **circuito magnético con núcleo de columnas**, donde son los devanados los que envuelven casi en su totalidad el núcleo magnético.

![[s06-t01-fig3-nucleo-columnas.png]]
*Imagen 3. Circuito magnético con núcleo por columnas.*

> [!summary] Acorazado vs. columnas
> - **Acorazado:** las espiras quedan más firmemente sujetas mecánicamente.
> - **De columnas:** construcción más simple, se adapta mejor a **elevadas tensiones** porque la superficie que requiere aislamiento es menor. Por esto se usa con mayor frecuencia en la práctica, excepto en transformadores monofásicos de baja potencia y tensión.

### Juntas: tope y solape

Los puntos de unión entre las columnas y las culatas se conocen como **juntas**. Es crucial que tengan un grosor mínimo para **minimizar la reluctancia** en el circuito magnético. La culata superior debe ser de apertura para facilitar la instalación de las bobinas y los materiales aislantes. Las uniones se llevan a cabo de dos maneras:

**Uniones a tope (planas):** las columnas y culatas se ensamblan por separado y luego se unen mediante elementos de sujeción.

![[s06-t01-fig4-uniones-tope.png]]
*Imagen 4. Uniones al tope.*

**Uniones al solape (entrelazadas):** el núcleo magnético se crea integralmente, ensamblando las láminas con un desplazamiento de posición entre capas sucesivas (pares e impares) igual al ancho de las láminas de la culata. Aunque este ensamblaje es más complejo, **proporciona una mayor estabilidad mecánica** al conjunto.

![[s06-t01-fig5-uniones-solape.png]]
*Imagen 5. Uniones al solape.*

> [!warning] Corte a 45°
> En ambas situaciones existe una región adyacente a la unión en la cual el flujo **no sigue la dirección de la laminación**. En láminas de grano orientado esto provoca calentamiento local por aumento de pérdidas en el hierro. Para prevenirlo, las uniones (a tope o al solape) se realizan no a 90° sino **a 45°**.

### Sección cruciforme

En transformadores de menor tamaño, las secciones transversales de las columnas se fabrican uniformes. Pero, para maximizar la utilización del espacio interno de los devanados (de sección circular), la sección transversal se configura como un **polígono escalonado**, con un número de escalones que aumenta proporcionalmente a la potencia del transformador. Se dice entonces que la sección es del tipo **cruciforme**.

![[s06-t01-fig6-nucleos-cruciforme.png]]
*Imagen 6. Núcleos del transformador tipo cruciforme.*

### Dimensionamiento de una sección cruciforme de 3 escalones

Para una sección con tres escalones, el área real de hierro vale:

$$S = b^2 + 2ac - 2bc$$

De la figura se deduce que:

$$d^2 = a^2 + c^2 \hspace{0.5cm};\hspace{0.5cm} d^2 = 2b^2$$

Despejando $c$:

$$S = \frac{d^2}{2} + 2a\sqrt{d^2 - a^2} - d\sqrt{2(d^2 - a^2)}$$

Para un determinado diámetro $d$, el dimensionamiento óptimo (que **maximiza el área de hierro inscrita** en el círculo del devanado) da lugar a:

$$\begin{aligned}
a &= 0{,}906 \cdot d \\
b &= 0{,}707 \cdot d \\
c &= 0{,}423 \cdot d
\end{aligned}$$

**Donde:**
- $d$ = diámetro de la circunferencia que circunscribe al núcleo (m).
- $a$ = ancho de la lámina más externa (m).
- $b$ = ancho de la lámina del escalón intermedio (m).
- $c$ = ancho de la lámina del escalón interior (m).
- $S$ = área real de hierro de la sección cruciforme (m²).

![[s06-t01-fig7-nucleo-cruciforme-dimensiones.png]]
*Imagen 7. Núcleo del transformador tipo cruciforme con sus dimensiones.*

> [!tip] Por qué cruciforme
> Aproximar la sección de hierro a un círculo permite que el devanado (que físicamente es de sección circular) **no desperdicie espacio**. A mayor número de escalones, mejor aprovechamiento del cobre — al precio de una construcción más compleja.

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
