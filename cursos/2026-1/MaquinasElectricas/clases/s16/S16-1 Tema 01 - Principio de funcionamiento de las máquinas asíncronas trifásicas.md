---
title: "Tema 01 - Principio de funcionamiento de las máquinas asíncronas trifásicas"
curso: "[[Motores MOC]]"
unidad: 4
semana: 16
orden: 1
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/motor-de-induccion
  - tema/jaula-de-ardilla
  - tema/velocidad-sincrona
  - tema/par-inducido
date: 2026-07-06
---

> [!info] Material original
> Manual del docente: [S16-Manual-Principio-funcionamiento-asincronas.pdf](attachments/S16-Manual-Principio-funcionamiento-asincronas.pdf) (UTP, Semana 16).

## Máquinas asíncronas o de inducción

Las máquinas asíncronas son **máquinas rotativas** ($n \neq 0$) y se caracterizan por las siguientes relaciones de frecuencia:

$$f_1 \neq 0 \hspace{1.5cm} f_2 = f_1 \pm \frac{n\,p}{60} \hspace{1.5cm} f_L = f_2$$

- $f_1$ = frecuencia de la corriente de alimentación del devanado inductor (estator).
- $f_2$ = frecuencia de las magnitudes del rotor.
- $f_L$ = frecuencia en la carga (coincide con $f_2$).
- $n$ = velocidad de giro del rotor.
- $p$ = número de pares de polos.

Las máquinas de inducción tienen un **devanado inductor en el estator**, alimentado con corriente alterna de frecuencia $f_1$. Para máquinas con potencia superior a $1/2\ \text{CV}$, este devanado es **trifásico**, al igual que la corriente de alimentación, y genera un **campo magnético giratorio** cuya velocidad se determina según:

$$n = \frac{60\,f_1}{p}$$

- $n$ = velocidad del campo magnético giratorio, en rpm.
- $f_1$ = frecuencia de alimentación, en Hz.
- $p$ = número de **pares** de polos.

En la mayoría de los casos, el rotor de la máquina de inducción está compuesto por **conductores cortocircuitados por dos anillos extremos**, formando una **jaula de ardilla**. Gracias a esta construcción, la máquina puede operar tanto como **motor** como **generador**.

## Aspectos constructivos de las máquinas asíncronas trifásicas

### Construcción de un motor de inducción

Un motor de inducción tiene físicamente **el mismo estator que una máquina síncrona**, pero con un **rotor de construcción diferente**. Un estator típico de dos polos se parece al estator de una máquina síncrona. Existen **dos tipos** de rotores que pueden utilizarse dentro del estator:

1. **Rotor de jaula de ardilla** (o rotor de jaula).
2. **Rotor devanado**.

### Rotor de jaula de ardilla

Los rotores tipo jaula de ardilla constan de una **serie de barras conductoras** dispuestas dentro de **ranuras labradas en la cara del rotor** y puestas **en cortocircuito** en alguno de sus extremos mediante **grandes anillos de cortocircuito**.

### Rotor devanado

Los rotores devanados son **más grandes** que los de jaula y **necesitan más mantenimiento** debido al desgaste de las **escobillas** y los **anillos rozantes**, por lo que **rara vez se utilizan** en los motores de inducción.

> [!note] Analogía de funcionamiento
> La operación de los motores de inducción es básicamente **igual a la de los motores síncronos con devanados de amortiguamiento**.

## Desarrollo del par inducido en un motor de inducción

Considérese un motor de inducción con un rotor de tipo jaula de ardilla. Se aplica un **conjunto trifásico de voltajes al estator**, lo que genera un **conjunto trifásico de corrientes**, produciendo un **campo magnético rotativo** $B_S$ en sentido contrario a las manecillas del reloj. La velocidad de rotación del campo magnético está determinada por:

$$n_{sinc} = \frac{120 \cdot f_e}{P}$$

- $n_{sinc}$ = velocidad síncrona del campo magnético giratorio, en rpm.
- $f_e$ = frecuencia del sistema, en Hz.
- $P$ = **número de polos** de la máquina (no el número de pares de polos).

> [!warning] Polos vs. pares de polos
> Conviven **dos formas** de la misma expresión: $n = 60 f_1 / p$ usa el número de **pares** de polos $p$, mientras que $n_{sinc} = 120 f_e / P$ usa el **número de polos** $P = 2p$. Ambas dan el mismo resultado; el error clásico es mezclar la constante ($60$ o $120$) con el denominador equivocado.

### Voltaje inducido en las barras del rotor

El campo magnético giratorio $B_S$ se genera con una frecuencia determinada por la **frecuencia del sistema** en hertz ($f_e$) y el **número de polos** en la máquina ($P$). Este campo **pasa sobre las barras del rotor**, induciendo un voltaje en ellas. El voltaje inducido en una barra de rotor específica se expresa mediante:

$$e_{ind} = (\vec{v} \times \vec{B}) \cdot \vec{l}$$

- $e_{ind}$ = voltaje inducido en la barra del rotor.
- $\vec{v}$ = velocidad de la barra **relativa** al campo magnético.
- $\vec{B}$ = vector de densidad de flujo magnético.
- $\vec{l}$ = vector longitud del conductor, en la dirección de la barra.

Esto resulta en un **flujo de corriente hacia afuera en las barras superiores** y **hacia adentro en las barras inferiores**. Sin embargo, debido a que el ensamblado del rotor es **inductivo**, la **corriente pico del rotor se retrasa** respecto al voltaje pico del rotor.

### Par inducido

El flujo de corriente en el rotor genera un **campo magnético en este**, denominado $B_R$. Por último, el par inducido en la máquina está determinado por:

$$\tau_{ind} = k \cdot (\vec{B_R} \times \vec{B_S})$$

- $\tau_{ind}$ = par inducido.
- $k$ = constante que depende de la construcción de la máquina.
- $\vec{B_R}$ = campo magnético del rotor; $\vec{B_S}$ = campo magnético del estator.

El par resultante tiene **sentido contrario a las manecillas del reloj**, por lo que el rotor **acelera en la dirección del campo giratorio**.

## Límite superior de velocidad: por qué el motor nunca alcanza el sincronismo

Existe un **límite superior finito** para la velocidad del motor de inducción. Si el rotor girase a **velocidad síncrona**, las barras del rotor estarían **estacionarias respecto al campo magnético** y, en consecuencia, **no habría voltaje inducido**.

El razonamiento encadena así:

1. Si $e_{ind} = 0$, **no habrá corriente** en el rotor.
2. Sin corriente en el rotor, **no habrá campo magnético** $B_R$ en él.
3. Sin $B_R$, el **par inducido es nulo** ($\tau_{ind} = k(B_R \times B_S) = 0$).
4. Con par nulo, el rotor **se frena** por las pérdidas por fricción, vuelve a aparecer movimiento relativo y con él el voltaje inducido.

Por lo tanto, un motor de inducción **puede acelerar hasta acercarse a la velocidad síncrona, pero nunca alcanzarla exactamente**. Durante la operación normal, los campos magnéticos del rotor y del estator ($B_R$ y $B_S$) **giran juntos a la velocidad síncrona** $n_{sinc}$, mientras que **el rotor gira a una velocidad menor**.

> [!summary] Idea central
> El estator trifásico crea un **campo giratorio** a velocidad síncrona ($n_{sinc} = 120 f_e / P$, equivalente a $n = 60 f_1 / p$). Ese campo barre las barras del rotor —cortocircuitadas en la **jaula de ardilla**— e induce en ellas $e_{ind} = (\vec{v} \times \vec{B}) \cdot \vec{l}$; la corriente resultante crea $B_R$ y con él el par $\tau_{ind} = k(\vec{B_R} \times \vec{B_S})$. Todo el mecanismo **depende del movimiento relativo**: al llegar al sincronismo, $e_{ind} = 0$, el par se anula y el motor se frena. De ahí que la máquina sea **asíncrona** y que ese movimiento relativo —el **deslizamiento**— sea la variable que gobierna el [[S16-2 Tema 02 - Circuito equivalente de un motor de inducción|circuito equivalente]] y el [[S16-3 Tema 03 - Potencia y par en los motores de inducción|balance de potencia y par]] de la máquina.

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
