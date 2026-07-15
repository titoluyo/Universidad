---
title: "Tema 03 - Potencia y par en los motores de inducción"
curso: "[[Motores MOC]]"
unidad: 4
semana: 16
orden: 3
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/flujo-de-potencia
  - tema/par-inducido
  - tema/potencia-en-el-entrehierro
  - tema/perdidas
date: 2026-07-06
---

![[S16-T03-01-S16-B2.png]]

Los motores de inducción son máquinas de **una sola excitación**, y sus relaciones de potencia y par difieren considerablemente de las máquinas síncronas.

## Pérdidas y diagrama de flujo de potencia

Un motor de inducción puede describirse como un **transformador rotatorio**, donde la entrada es un sistema trifásico de voltajes y corrientes. A diferencia de un transformador ordinario, donde la salida es la potencia eléctrica de los devanados secundarios, en un motor de inducción los devanados secundarios (el rotor) están **en cortocircuito**, lo que significa que no hay salida de electricidad: la salida es **mecánica**. La relación entre la potencia eléctrica de entrada y la potencia mecánica de salida se ilustra en el diagrama de flujo de potencia de la Figura 1.

![[S16-T03-02-Figura-1-Diagrama-de-flujo-de-potencia-de-un.png]]
> **Figura 1.** Diagrama de flujo de potencia de un motor de inducción.

El recorrido de la potencia a través de la máquina es el siguiente:

1. La **potencia de entrada**, $P_{entr}$, se presenta en forma de voltajes y corrientes eléctricas trifásicas.
2. Las primeras pérdidas encontradas son las pérdidas $I^2R$ en los devanados del estator (**pérdidas en el cobre del estator**, $P_{PCE}$).
3. Luego se pierde cierta cantidad de potencia por la **histéresis y las corrientes parásitas** del estator ($P_{núcleo}$).
4. La potencia restante se transfiere al rotor a través del **entrehierro** entre el estator y el rotor: es la **potencia en el entrehierro** ($P_{EH}$).
5. Una vez transferida al rotor, una parte se pierde en pérdidas $I^2R$ (**pérdidas en el cobre del rotor**, $P_{PCR}$), y el resto se **convierte** de su forma eléctrica a mecánica ($P_{conv}$).
6. Por último, se restan las pérdidas por **fricción y rozamiento con el aire** ($P_{FyR}$) y las **pérdidas misceláneas** ($P_{misc}$). La potencia restante es la salida del motor ($P_{sal}$).

## Deducción de las ecuaciones a partir del circuito equivalente

La Figura 2 presenta el [[S16-2 Tema 02 - Circuito equivalente de un motor de inducción|circuito equivalente por fase de un motor de inducción]]. Al examinar detenidamente este circuito, se pueden deducir las ecuaciones de la potencia y el par que rigen la operación del motor.

La **corriente de entrada** a una fase del motor se calcula dividiendo el voltaje de entrada entre la impedancia equivalente total:

$$I_1 = \frac{V_\phi}{Z_{eq}}$$

Donde:

$$Z_{eq} = R_1 + jX_1 + \cfrac{1}{G_C - jB_M + \cfrac{1}{\dfrac{R_2}{s} + jX_2}}$$

- $V_\phi$ = voltaje de fase aplicado al estator.
- $R_1$, $X_1$ = resistencia y reactancia de dispersión del estator.
- $G_C$, $B_M$ = conductancia de pérdidas en el núcleo y susceptancia de magnetización.
- $R_2$, $X_2$ = resistencia y reactancia del rotor referidas al estator; $s$ = deslizamiento.

![[S16-T03-03-Figura-2-Circuito-equivalente-por-fase-de-un.png]]
> **Figura 2.** Circuito equivalente por fase de un motor de inducción.

Con la corriente conocida se pueden calcular las pérdidas en el cobre del estator, las pérdidas en el núcleo y las pérdidas en el cobre del rotor.

### Pérdidas en el cobre del estator y en el núcleo

Las **pérdidas en el cobre del estator** en las tres fases están definidas por:

$$P_{PCE} = 3\,I_1^2\,R_1$$

Las **pérdidas en el núcleo** están dadas por:

$$P_{núcleo} = 3\,E_1^2\,G_C$$

- $E_1$ = voltaje interno del estator (tensión sobre la rama de magnetización).

### Potencia en el entrehierro

Por lo que la **potencia en el entrehierro** es:

$$P_{EH} = P_{entr} - P_{PCE} - P_{núcleo}$$

Si se examina detenidamente el circuito equivalente del rotor, se observa que el único elemento del circuito donde se puede disipar la potencia en el entrehierro es el resistor $\dfrac{R_2}{s}$. Por lo tanto, la potencia en el entrehierro también se puede calcular así:

$$P_{EH} = 3\,I_2^2\,\frac{R_2}{s}$$

- $I_2$ = corriente del rotor referida al estator.

### Pérdidas en el cobre del rotor

Las **pérdidas resistivas reales** en el circuito del rotor están dadas por:

$$P_{PCR} = 3\,I_R^2\,R_R$$

Dado que la potencia **no cambia a través de un transformador ideal**, las pérdidas en el cobre del rotor pueden expresarse igualmente con las magnitudes referidas:

$$P_{PCR} = 3\,I_2^2\,R_2$$

### Potencia convertida

Una vez que se deducen las pérdidas en el cobre del estator, las pérdidas en el núcleo y las pérdidas en el cobre del rotor de la potencia de entrada al motor, la potencia restante se convierte de su forma eléctrica a mecánica. Esta **potencia convertida**, a veces llamada **potencia mecánica desarrollada**, se expresa como:

$$\begin{aligned}
P_{conv} &= P_{EH} - P_{PCR} = 3I_2^2\,\frac{R_2}{s} - 3I_2^2 R_2 \\
P_{conv} &= 3I_2^2 R_2 \left( \frac{1}{s} - 1 \right) \\
P_{conv} &= 3I_2^2 R_2 \left( \frac{1-s}{s} \right)
\end{aligned}$$

Comparando $P_{PCR} = 3I_2^2 R_2$ con $P_{EH} = 3I_2^2 R_2/s$, se deduce que las **pérdidas en el cobre del rotor son iguales a la potencia en el entrehierro multiplicada por el deslizamiento**:

$$P_{PCR} = s\,P_{EH}$$

> [!important] Consecuencia práctica
> Cuanto **menor sea el deslizamiento** del motor, menores serán las pérdidas del rotor. Si el rotor no gira, el deslizamiento es $s = 1$ y el rotor **consume toda la potencia en el entrehierro**. Esto es lógico, ya que si el rotor no gira, la potencia de salida ($P_{sal} = \tau_{carga} \cdot \omega_m$) debe ser cero.

Dado que $P_{conv} = P_{EH} - P_{PCR}$, esto también representa otra relación entre la potencia en el entrehierro y la potencia convertida de forma eléctrica a mecánica:

$$\begin{aligned}
P_{conv} &= P_{EH} - P_{PCR} = P_{EH} - s\,P_{EH} \\
P_{conv} &= (1-s)\,P_{EH}
\end{aligned}$$

### Potencia de salida

Finalmente, si se conocen las pérdidas por fricción, rozamiento con el aire y las pérdidas misceláneas, la **potencia de salida** se determina de la siguiente manera:

$$P_{sal} = P_{conv} - P_{FyR} - P_{misc}$$

## Par inducido

El **par inducido**, $\tau_{ind}$, en una máquina se define como el par generado por la conversión de potencia interna de eléctrica a mecánica. Este par difiere del par realmente disponible en los terminales del motor por una cantidad igual a los pares de fricción y de rozamiento con el aire en la máquina. El par inducido está dado por:

$$\tau_{ind} = \frac{P_{conv}}{\omega_m}$$

- $\tau_{ind}$ = par inducido o **par desarrollado** de la máquina.
- $\omega_m$ = velocidad mecánica del rotor.

Sustituyendo las relaciones $P_{conv} = (1-s)P_{EH}$ y $\omega_m = (1-s)\,\omega_{sinc}$ en la ecuación anterior, el factor $(1-s)$ se cancela:

$$\begin{aligned}
\tau_{ind} &= \frac{(1-s)\,P_{EH}}{(1-s)\,\omega_{sinc}} \\
\tau_{ind} &= \frac{P_{EH}}{\omega_{sinc}}
\end{aligned}$$

- $\omega_{sinc}$ = velocidad síncrona (del campo magnético giratorio).

Esta última ecuación es especialmente útil porque expresa el par inducido **directamente en términos de la potencia en el entrehierro y la velocidad síncrona**, la cual permanece constante. Conocer $P_{EH}$ proporciona automáticamente el valor de $\tau_{ind}$.

## Separación de las pérdidas en el cobre del rotor y la potencia convertida en el circuito equivalente

La potencia en el entrehierro es la potencia que se consumiría en un resistor de valor $\dfrac{R_2}{s}$, mientras que las pérdidas en el cobre del rotor son la potencia que se consumiría en un resistor de valor $R_2$. La diferencia entre ellos es $P_{conv}$, que, por lo tanto, debe ser la potencia consumida en un resistor de valor:

$$R_{conv} = \frac{R_2}{s} - R_2 = R_2 \left( \frac{1}{s} - 1 \right) = R_2 \left( \frac{1-s}{s} \right)$$

- $R_{conv}$ = resistencia ficticia que representa la **carga mecánica** del motor.

La Figura 3 muestra el circuito equivalente por fase con las pérdidas en el cobre del rotor y la potencia convertida en forma mecánica representadas por **elementos distintos**. Así, la potencia disipada en $R_2$ son pérdidas reales y la disipada en $R_{conv}$ es la potencia que sale por el eje.

![[S16-T03-04-Figura-3-Circuito-equivalente-por-fase-con-pe.png]]
> **Figura 3.** Circuito equivalente por fase con pérdidas en el rotor y $P_{núcleo}$ separadas.

> [!summary] Idea central
> La potencia entra como electricidad trifásica y se degrada en cascada: $P_{entr} \to P_{PCE} \to P_{núcleo} \to \mathbf{P_{EH}} \to P_{PCR} \to \mathbf{P_{conv}} \to P_{FyR},\,P_{misc} \to P_{sal}$. Toda la $P_{EH}$ se disipa en el resistor $R_2/s$ del circuito equivalente, y se reparte entre pérdidas del rotor ($P_{PCR} = sP_{EH}$, en $R_2$) y potencia convertida ($P_{conv} = (1-s)P_{EH}$, en $R_{conv}$). De ahí el resultado clave: $\tau_{ind} = P_{EH}/\omega_{sinc}$, que solo requiere conocer la potencia en el entrehierro y la velocidad síncrona **constante**.

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
