---
title: "Tema 01 - Arranque, frenado e inversión del sentido de giro en motores DC"
curso: "[[Motores MOC]]"
unidad: 3
semana: 14
orden: 1
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/arranque-motor-dc
  - tema/reostato-de-arranque
  - tema/frenado-motor-dc
  - tema/frenado-regenerativo
  - tema/frenado-dinamico
  - tema/frenado-contracorriente
  - tema/inversion-de-giro
date: 2026-06-22
---

## Arranque de motores DC

El **arranque** es un aspecto crítico en los motores de c.c. De la ecuación del inducido $V = E + R_i\,I_i$, la corriente vale:

$$I_i = \frac{V - E}{R_i} \quad\Longrightarrow\quad I_i\,(\text{arranque directo}) = \frac{V}{R_i}$$

En el **instante de arranque** la velocidad es nula, por lo que la **fuerza contraelectromotriz** (f.c.e.m.) $E = K_E\,n\,\phi$ también es nula. El inducido —de resistencia $R_i$ muy pequeña— ofrece poca oposición a la tensión de red, y la corriente de arranque resulta **peligrosamente alta**. Para limitarla se intercalan **reóstatos de arranque** en serie con el inducido.

> [!warning] Por qué no se arranca "en directo"
> Como $E=0$ al arrancar, $I_i = V/R_i$. Con $R_i$ del orden de centésimas de ohmio, esta corriente puede ser muchas veces la nominal, suficiente para dañar el colector, las escobillas y el devanado. El reóstato de arranque añade resistencia temporal para mantener $I_i$ en un rango admisible.

Los reóstatos de arranque, conectados también al inductor, cumplen varias funciones simultáneas:

1. Deben permitir el paso de corriente por el **inductor** antes —o, como mucho, al mismo tiempo— que por el circuito del **inducido**.
2. No pueden cortar el circuito inductor con tensión total ni sin asegurar un **circuito de descarga** para las corrientes de autoinducción del inductor.
3. Es deseable que permitan un **cambio fácil del sentido de rotación**.

### El reóstato de arranque

![[T01 - Figura 1. Reostato de arranque y su conexion.png]]
> **Figura 1.** Reóstato de arranque y su conexión (motor tipo derivación).

El reóstato de la figura 1 está formado por una **resistencia total subdividida en tramos** ($R_1, R_2, R_3, R_4$) conectados a piezas de latón llamadas **plots**. Una **manivela** con muelle en espiral, al girar en sentido horario desde la posición de parada (*Off*), va eliminando progresivamente resistencia en serie con el inducido, lo que produce un **arranque suave** sin picos de corriente mientras el motor gana velocidad.

También pueden emplearse **resistencias fijas** en lugar del reóstato, que se van intercalando en los circuitos del inducido (arranque) y del inductor (regulación) mediante la acción combinada de **contactores y relés de tiempo**.

![[T01 - Figura 2. Circuito de arranque de un motor DC.png]]
> **Figura 2.** Circuito eléctrico de un sistema de arranque de un motor de corriente continua.

## Frenado de motores DC

Se denomina **frenado** a la acción por la cual la fuerza electromagnética de la máquina **se opone al movimiento** para reducir la velocidad de forma controlada, evitando tiempos de parada excesivos o el embalamiento de la máquina.

### Motor serie

**Frenado a contracorriente.** Se agrega una resistencia al circuito para controlar la corriente cuando el par de la carga supera al par de cortocircuito. El frenado se logra **invirtiendo la polaridad de la tensión en el inducido**, manteniendo constante la corriente en el devanado de excitación. La carga debe limitarse según la corriente admisible del circuito.

![[T01 - Figura 3. Circuito equivalente frenado contracorriente.png]]
> **Figura 3.** Circuito equivalente del motor de c.c. para el análisis del frenado a contracorriente (al invertir, $V_a$ y $E_a$ se suman sobre $R_a$).

**Frenado dinámico** (la máquina pasa a funcionar como generador):

- **Con excitación independiente** — el devanado de excitación se conecta a la red a través de una resistencia que limita la corriente. En motores de baja potencia a veces se mantiene el flujo con **anillos de cobre cortocircuitados** en los polos.
- **Con autoexcitación** — el inducido y el devanado de excitación se desconectan de la red y se cierran sobre una resistencia. Conviene **invertir la polaridad del inducido** al pasar de motor a freno para evitar la desmagnetización, manteniendo el sentido de la corriente de excitación.

### Motor compound (compuesto)

El motor compuesto admite los tres procedimientos de frenado eléctrico:

- **Frenado regenerativo** (en hipersincronismo).
- **Frenado dinámico** o por corriente continua.
- **Frenado a contracorriente.**

En el frenado **regenerativo**, las corrientes pueden desmagnetizar la máquina al cambiar de dirección; para evitarlo, el **devanado serie se deriva** cuando la velocidad supera cierto umbral, lo que produce características mecánicas **lineales en el cuadrante II**. En el **dinámico** suele conectarse solo el devanado de excitación independiente, manteniendo el flujo constante. En cambio, las características en régimen de **contracorriente no son lineales**, por la influencia de la f.e.m. variable del devanado serie ante cambios de carga.

![[T01 - Figura 4. Circuito frenado dinamico.png]]
> **Figura 4.** Circuito de frenado dinámico: el inducido se desconecta de la red y se cierra sobre la resistencia $R_f$.

### Motor shunt (derivación)

El frenado del motor shunt es muy usado y puede lograrse de **tres formas**:

- **Frenado regenerativo** — devolviendo energía al circuito de alimentación.
- **Frenado a contracorriente** — invirtiendo el sentido de la corriente.
- **Frenado dinámico** — disipando la energía cinética en una resistencia.

**Frenado regenerativo.** Ocurre cuando la máquina, funcionando como motor, es forzada por la potencia impulsora a girar a una **velocidad mayor que la de vacío**. Al operar entonces como generador, la energía se **devuelve a la línea** y puede recuperarse.

![[T01 - Figura 5. Freno regenerativo.png]]
> **Figura 5.** Máquina operando en freno regenerativo.

**Frenado por inversión (contracorriente).** Ocurre cuando la carga mecánica hace girar la máquina en **sentido contrario** al momento electromagnético producido; la máquina recibe energía tanto del eje como de la línea. Se realiza de dos maneras: cuando la potencia impulsora hace girar la máquina contra el par motor, o **invirtiendo la corriente del inducido**.

**Frenado dinámico.** La máquina funciona como **generador con excitación independiente**: el inducido se desconecta de la alimentación y se conecta en paralelo con una **resistencia de carga**, sin variar la corriente de excitación, disipando la energía cinética almacenada.

## Inversión del sentido de giro de motores DC

¿Cómo se consigue invertir el giro? Basta con **conmutar (intercambiar) la conexión de los dos bornes del inducido** (armadura). En una posición de conexión gira en un sentido; al intercambiar los bornes, gira en sentido contrario.

- Un **motor de c.c.** cambia de sentido de giro al **cambiar la polaridad** en sus bornes.
- Un **motor de c.a. monofásico** cambia de giro al permutar la conexión de fase y neutro.
- Un **motor de c.a. trifásico** cambia de giro al **permutar dos de sus fases**.

![[T01 - Figura 6. Cambio de giro de motor DC.png]]
> **Figura 6.** Cambio de giro de un motor DC: al invertir la polaridad de bornes, el giro pasa de derecha a izquierda.

![[T01 - Figura 7. Conmutacion de conexiones para el cambio de giro.png]]
> **Figura 7.** Conmutación de conexiones para el cambio de giro.

La maniobra se realiza con dos contactores ($KM_1$ y $KM_2$) según la secuencia:

- $KM_1$ **cerrado**, $KM_2$ abierto → giro en **sentido directo**.
- Se **abre $KM_1$**, $KM_2$ abierto → el motor queda girando por inercia y debe frenarse.
- Se **cierra $KM_2$**, $KM_1$ abierto → cuando el giro directo casi se ha extinguido, arranca el motor en **sentido inverso**.

Este proceso puede automatizarse mediante **temporizadores** asociados a los contactores.

![[T01 - Figura 8. Esquema de inversion de giro en plano electrico.png]]
> **Figura 8.** Esquema de inversión de giro en plano eléctrico (con fusibles, relé temporizado y contactores $KM_2$/$KM_3$).

> [!summary] Idea central
> **Arranque:** como $E=0$ al partir, $I_i=V/R_i$ sería excesiva → se limita con **reóstato de arranque** en serie con el inducido. **Frenado:** la máquina pasa a generador y disipa o devuelve energía; modos **regenerativo** (recupera energía), **dinámico** (disipa en resistencia) y **contracorriente** (invierte tensión/corriente del inducido). **Inversión de giro:** se **permutan los bornes del inducido** (cambio de polaridad), maniobrado con contactores temporizados. Estos procedimientos se apoyan en las mismas ecuaciones de la [[S13-2 Tema 02 - El motor de corriente continua|máquina DC]] y enlazan con la [[S14-2 Tema 02 - Regulación de velocidad de un motor de corriente continua|regulación de velocidad]].

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
