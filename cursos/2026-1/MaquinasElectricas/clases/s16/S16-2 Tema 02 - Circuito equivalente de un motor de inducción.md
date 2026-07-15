---
title: "Tema 02 - Circuito equivalente de un motor de inducción"
curso: "[[Motores MOC]]"
unidad: 4
semana: 16
orden: 2
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/circuito-equivalente
  - tema/motor-de-induccion
  - tema/deslizamiento
  - tema/modelo-de-transformador
date: 2026-07-06
---

![[S16-T02-01-S16-B1.png]]

El circuito equivalente de un motor de inducción se deduce a partir del conocimiento de los **transformadores** y de la relación entre la **frecuencia del rotor y la velocidad**, considerando los efectos de la frecuencia variable del rotor y otros factores similares. La analogía es directa: el estator hace de primario y el rotor, cortocircuitado, hace de secundario.

## Modelo de transformador de un motor de inducción

La Figura 1 ilustra un circuito equivalente **por fase** que describe el funcionamiento de un motor de inducción como si fuera un transformador. Al igual que en cualquier otro transformador, los devanados primarios (**estator**) tienen una cierta resistencia y autoinductancia que deben representarse en el circuito equivalente de la máquina:

- $R_1$ = resistencia del estator.
- $X_1$ = reactancia de dispersión del estator.

Estos componentes se encuentran justo **en la entrada** del modelo de la máquina. El voltaje primario interno del estator $E_1$ se acopla al secundario $E_R$ por medio de un **transformador ideal** con una relación efectiva de vueltas $a_{ef}$.

![[S16-T02-02-Figura-1-Modelo-de-transformador-de-un-motor.png]]
> **Figura 1.** Modelo de transformador de un motor de inducción, con el rotor y el estator conectados por un transformador ideal con una relación de vueltas de $a_{ef}$.

## Modelo de circuito del rotor

Cuando se aplica voltaje a los devanados del estator de un motor de inducción, se **induce un voltaje** en los devanados del rotor de la máquina. Su magnitud depende del **movimiento relativo** entre el campo giratorio y el rotor (ver [[S16-1 Tema 01 - Principio de funcionamiento de las máquinas asíncronas trifásicas|principio de funcionamiento de las máquinas asíncronas]]):

- La condición de **mayor** movimiento relativo ocurre cuando el rotor está estacionario, denominada condición de **rotor bloqueado o detenido**, donde se induce el mayor voltaje y la mayor frecuencia en el rotor.
- El **menor** voltaje ($0\ \text{V}$) y frecuencia ($0\ \text{Hz}$) se presentan cuando el rotor se mueve a la misma velocidad que el campo magnético del estator, lo que resulta en **ausencia de movimiento relativo**.
- La magnitud y la frecuencia del voltaje inducido en el rotor a cualquier velocidad entre estos dos extremos es **directamente proporcional al deslizamiento** del rotor.

Así, si llamamos $E_{R0}$ a la magnitud del voltaje inducido del rotor en condición de rotor bloqueado, la magnitud del voltaje inducido con cualquier deslizamiento está dada por:

$$E_R = s \cdot E_{R0}$$

- $E_R$ = voltaje inducido en el rotor con deslizamiento $s$.
- $E_{R0}$ = voltaje inducido en el rotor con rotor bloqueado ($s = 1$).
- $s$ = deslizamiento.

Y la **frecuencia** del voltaje inducido con cualquier deslizamiento está dada por:

$$f_r = s\,f_e$$

- $f_r$ = frecuencia del rotor.
- $f_e$ = frecuencia eléctrica del estator (red).

El voltaje inducido en el rotor de un motor de inducción se produce en un rotor que tiene tanto **resistencia** como **reactancia**.

![[S16-T02-03-Figura-2-Modelo-de-circuito-de-rotor-de-un-mo.png]]
> **Figura 2.** Modelo de circuito de rotor de un motor de inducción.

La resistencia del rotor, $R_R$, **permanece constante** —excepto por el efecto superficial o pelicular— independientemente del deslizamiento. Por otro lado, la **reactancia** del rotor se ve afectada de manera más compleja por el deslizamiento: depende de la inductancia del rotor y de la frecuencia del voltaje y la corriente en el rotor. Con una inductancia del rotor $L_R$, la reactancia del rotor está dada por:

$$X_R = \omega_r L_R = 2\pi f_r L_R$$

Sustituyendo $f_r = s\,f_e$ se obtiene:

$$\begin{aligned}
X_R &= 2\pi s f_e L_R \\
X_R &= s\,(2\pi f_e L_R) \\
X_R &= s\,X_{R0}
\end{aligned}$$

donde $X_{R0}$ es la **reactancia del rotor en estado bloqueado o detenido**.

> [!note] Lectura del resultado
> Tanto el voltaje ($E_R = s E_{R0}$) como la reactancia ($X_R = s X_{R0}$) del rotor escalan con el deslizamiento, mientras que $R_R$ no lo hace. Esta asimetría es la que permite, dividiendo entre $s$, eliminar la dependencia con la velocidad y llegar a un circuito equivalente **estático**.

### Circuito equivalente

En la Figura 4 se muestra una gráfica del flujo de corriente en el rotor, obtenida de la siguiente ecuación:

$$I_R = \frac{E_R}{R_R + jX_R} = \frac{E_R}{R_R + j s X_{R0}} = \frac{E_{R0}}{\dfrac{R_R}{s} + jX_{R0}}$$

- $I_R$ = corriente del rotor.
- $R_R$ = resistencia del rotor; $X_{R0}$ = reactancia del rotor bloqueado.

Nótese que en la última expresión **todos los efectos de la velocidad del rotor quedan concentrados en la impedancia** $R_R/s$: el circuito se comporta como si estuviera alimentado por la fuente constante $E_{R0}$ con una resistencia variable con el deslizamiento.

![[S16-T02-04-Figura-4-Corriente-del-rotor-en-funcion-de-la.png]]
> **Figura 4.** Corriente del rotor en función de la velocidad del rotor.

### Circuito equivalente final

En un transformador ordinario se pueden **referir** los voltajes, corrientes e impedancias del lado secundario del aparato al lado primario por medio de la relación de vueltas del transformador:

$$V_P = V'_S = a\,V_S \hspace{2cm} I_P = I'_S = \frac{I_S}{a} \hspace{2cm} Z'_S = a^2 Z_S$$

Si la relación efectiva de vueltas de un motor de inducción es $a_{ef}$, entonces el **voltaje transformado del rotor** es:

$$E_1 = E'_R = a_{ef}\,E_{R0}$$

La **corriente del rotor** referida al estator es:

$$I_2 = \frac{I_R}{a_{ef}}$$

Y la **impedancia del rotor** referida al estator:

$$Z_2 = a_{ef}^2 \left( \frac{R_R}{s} + jX_{R0} \right)$$

de donde se definen los parámetros del rotor referidos al estator:

$$\begin{aligned}
R_2 &= a_{ef}^2\,R_R \\
X_2 &= a_{ef}^2\,X_{R0}
\end{aligned}$$

- $R_2$ = resistencia del rotor referida al estator.
- $X_2$ = reactancia del rotor bloqueado referida al estator.

Así, el **circuito equivalente por fase final** del motor de inducción se muestra en la Figura 5: la rama de magnetización ($G_C$, $B_M$) queda en paralelo, y la rama del rotor aparece como $R_2/s$ en serie con $jX_2$, ya sin transformador ideal.

![[S16-T02-05-Figura-5-Circuito-equivalente-por-fase-de-un.png]]
> **Figura 5.** Circuito equivalente por fase de un motor de inducción.

> [!summary] Idea central
> El motor de inducción se modela como un **transformador rotatorio** cuyo secundario (rotor) está en cortocircuito. Como el voltaje y la reactancia del rotor dependen del deslizamiento ($E_R = sE_{R0}$, $X_R = sX_{R0}$) pero $R_R$ no, al dividir entre $s$ toda la dependencia con la velocidad se concentra en el término $R_R/s$. Refiriendo el rotor al estator con la relación efectiva de vueltas $a_{ef}$ ($R_2 = a_{ef}^2 R_R$, $X_2 = a_{ef}^2 X_{R0}$) se obtiene un **circuito equivalente por fase estático**, base para calcular corrientes, pérdidas y el [[S16-3 Tema 03 - Potencia y par en los motores de inducción|par y la potencia del motor]].

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
