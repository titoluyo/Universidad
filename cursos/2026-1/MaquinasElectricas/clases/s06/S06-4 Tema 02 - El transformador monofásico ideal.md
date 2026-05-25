---
title: El transformador monofásico ideal
curso: "[[Motores MOC]]"
unidad: 2
semana: 6
orden: 4
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/transformador-ideal
  - tema/relacion-transformacion
  - tema/devanado-primario
  - tema/devanado-secundario
  - tema/conservacion-potencia
date: 2026-04-27
---

![[s06-t02-banner.jpg]]

## ¿Qué es un transformador?

Un **transformador** es un dispositivo que **convierte la potencia eléctrica en forma de corriente alterna**, cambiando el nivel de voltaje mediante la influencia de un campo magnético.

Consiste en **dos o más bobinas de conductor** enrolladas alrededor de un **núcleo ferromagnético compartido** (ver [[S06-1 Tema 01 - El reactor con núcleo de hierro|el reactor con núcleo de hierro]]). Estas bobinas **no suelen estar directamente conectadas entre sí** — la única conexión entre ellas es el **flujo magnético común** presente dentro del núcleo.

- Uno de los devanados se conecta a una **fuente de corriente alterna**.
- El segundo (y posiblemente un tercero) **suministra energía eléctrica a las cargas**.

### Nomenclatura de los devanados

| Devanado | Otro nombre | Conexión |
| -------- | ----------- | -------- |
| **Primario** | Devanado de entrada | A la fuente de energía |
| **Secundario** | Devanado de salida | A las cargas |
| **Terciario** | (cuando existe) | A una segunda carga / sistema |

![[s06-t02-fig1-transformador-monofasico-taps.jpg]]
*Imagen 1. Transformador monofásico con taps intermedios.*

![[s06-t02-fig2-transformador-multiples-salidas.png]]
*Imagen 2. Transformador de múltiples salidas.*

## Definición del transformador ideal

Un **transformador ideal** se define como un **dispositivo sin pérdidas** que posee un devanado de entrada y un devanado de salida. Las relaciones entre el voltaje de entrada y el de salida, así como entre la corriente de entrada y la de salida, se expresan mediante **dos ecuaciones simples**.

![[s06-t02-fig3-transformador-ideal.png]]
*Imagen 3. Transformador monofásico ideal.*

> [!summary] Hipótesis del transformador ideal
> - Sin pérdidas en el hierro ni en el cobre.
> - Permeabilidad infinita del núcleo (reluctancia nula).
> - Acoplamiento perfecto entre devanados (sin flujo de dispersión).

## Relación de transformación

### Relación de voltajes

En un transformador ideal con $N_P$ vueltas en el primario y $N_S$ vueltas en el secundario, la relación entre el voltaje $V_P(t)$ aplicado al primario y el voltaje $V_S(t)$ generado en el secundario es:

$$\frac{V_P(t)}{V_S(t)} = \frac{N_P}{N_S}$$

Si definimos la **relación de transformación**:

$$\boxed{\;\frac{N_P}{N_S} = a\;}$$

![[s06-t02-fig4-simbologia-transformador.png]]
*Imagen 4. Simbología esquemática de un transformador.*

### Relación de corrientes (Ley de Ampere)

La relación entre la corriente $i_P(t)$ que circula por el primario y la corriente $i_S(t)$ que sale del secundario es:

$$N_P \, i_P(t) = N_S \, i_S(t) \hspace{0.5cm} \Longrightarrow \hspace{0.5cm} \frac{i_P(t)}{i_S(t)} = \frac{1}{a}$$

> [!note] Origen físico
> Esta relación es la **ley de Ampere** aplicada al núcleo: en condiciones ideales (reluctancia nula), la suma de las fuerzas magnetomotrices es cero, $N_P i_P = N_S i_S$.

### Forma fasorial

Quedando estas ecuaciones en vectores (fasores) como:

$$\frac{V_P}{V_S} = a \hspace{0.5cm}\text{y}\hspace{0.5cm} \frac{I_P}{I_S} = \frac{1}{a}$$

**Donde:**
- $a$ = relación de transformación (adimensional).
- $V_P, V_S$ = fasores de voltaje primario y secundario (V).
- $I_P, I_S$ = fasores de corriente primaria y secundaria (A).
- $N_P, N_S$ = número de vueltas de los devanados primario y secundario.

## Potencia en el transformador ideal

### Potencia activa de entrada y salida

La **potencia de entrada** está dada por:

$$P_{in} = V_P \, I_P \cdot \cos\theta_P$$

**Donde** $\theta_P$ = ángulo entre el voltaje y la corriente en el primario.

La **potencia de salida** está dada por:

$$P_{out} = V_S \, I_S \cdot \cos\theta_S$$

**Donde** $\theta_S$ = ángulo entre el voltaje y la corriente en el secundario.

### Conservación de la potencia

Como los ángulos del voltaje y de la corriente **no se ven afectados** por el transformador ideal:

$$\theta_S = \theta_P = \theta$$

Aplicando las ecuaciones de relación de vueltas:

$$P_{out} = \frac{V_P}{a}\,(a\,I_P)\,\cos\theta \hspace{0.5cm}\longrightarrow\hspace{0.5cm} P_{out} = V_P \, I_P \, \cos\theta = P_{in}$$

> [!success] Conservación
> **La potencia entregada por un transformador ideal en su salida es equivalente a la potencia suministrada en su entrada.**

Esta misma relación se extiende a la potencia reactiva $Q$ y a la potencia aparente $S$:

$$\begin{aligned}
Q_{in} &= V_P \, I_P \cdot \sin\theta = V_S \, I_S \cdot \sin\theta = Q_{out} \\
S_{in} &= V_P \, I_P = V_S \, I_S = S_{out}
\end{aligned}$$

> [!tip] Lectura física
> El transformador ideal **no almacena ni disipa energía** — sólo cambia los niveles de tensión y corriente preservando todas las componentes de la potencia (activa, reactiva y aparente). Esto se rompe en el transformador real (semanas 7–8), donde aparecen pérdidas en el cobre, pérdidas en el hierro y dispersiones de flujo.

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
