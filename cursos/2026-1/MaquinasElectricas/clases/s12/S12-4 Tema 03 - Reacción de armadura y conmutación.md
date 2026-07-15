---
title: "Tema 03 - Reacción de armadura y conmutación"
curso: "[[Motores MOC]]"
unidad: 3
semana: 12
orden: 4
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/conmutacion
  - tema/reaccion-de-armadura
  - tema/plano-neutro
  - tema/colector-de-delgas
  - tema/maquina-dc
date: 2026-06-08
---

![[S12 - B2.png]]

## Conmutación

La **conmutación** se refiere a los fenómenos asociados con la **variación de corriente** en las espiras del inducido al pasar por la zona de cierre con las escobillas en el colector.

- Una **buena conmutación** se logra **sin chispas** en el colector.
- Una **mala conmutación** genera **chispas**, lo que conduce a un deterioro significativo del colector y afecta el funcionamiento de la máquina a largo plazo.

El chisporroteo entre escobillas y colector puede deberse a causas **mecánicas** (ajuste defectuoso de las escobillas, resaltes en algunas delgas) y **eléctricas** (elevación de la tensión entre delgas adyacentes por **autoinducción** en el arrollamiento del inducido).

![[T03 - Figura 1. Conmutacion en una maquina DC.jpg]]
> **Figura 1.** Conmutación en una máquina DC.

### Proceso de conmutación de una sección

Suponiendo un colector mecánicamente perfecto y despreciando las f.e.m. inducidas y las resistencias de las espiras frente a la resistencia de contacto escobilla–colector, se analiza la conmutación de una sección **C** del inducido:

- **Instante inicial:** la corriente sale de la escobilla por la delga 3; en la sección C la corriente es $\frac{I_i}{2}$ y fluye de derecha a izquierda.
- **Instante intermedio:** la sección C atraviesa la **línea neutra** e **invierte su dirección**, repartiéndose la corriente entre las delgas.
- **Final:** la escobilla pierde contacto con la delga 3; la corriente en C se ha invertido y vuelve a $\frac{I_i}{2}$.

![[T03 - Figura 2. Proceso de conmutacion en una seccion del inducido.png]]
> **Figura 2.** Proceso de conmutación en una sección del inducido (posiciones a, b, c).

El intervalo requerido se denomina **periodo $T$ de conmutación**. Si $R_e$ es la resistencia de contacto cuando escobilla y delga están totalmente unidas, al alejarse la escobilla de la delga 3 la superficie de contacto disminuye proporcionalmente al tiempo $t$, por lo que la resistencia de transición aumenta:

$$R_1 = R_e\,\frac{T}{T-t} \qquad ; \qquad R_2 = R_e\,\frac{T}{t}$$

donde $R_1$ es la resistencia de transición entre la delga 3 y la escobilla, y $R_2$ la de la delga siguiente.

Aplicando las **leyes de Kirchhoff** al circuito (ignorando resistencias de espiras y f.e.m. inducidas):

$$i_1 + i_2 = I_i \qquad ; \qquad R_1\,i_1 = R_2\,i_2 \qquad ; \qquad \frac{I_i}{2} + i = i_1$$

Resultando:

$$i_1 = I_i\,\frac{T-t}{T} \qquad ; \qquad i_2 = I_i\,\frac{t}{T}$$

Por lo tanto, la corriente $i$ en la sección conmutada es:

$$i = i_1 - \frac{I_i}{2} = \frac{I_i}{2}\left(1 - 2\,\frac{t}{T}\right)$$

que es la **ecuación de una recta** → **conmutación rectilínea o lineal**.

![[T03 - Figura 3. Variacion de la corriente en la conmutacion.png]]
> **Figura 3.** Variación de la corriente en la conmutación (conmutación lineal ideal).

> [!warning] En la práctica la conmutación no es lineal
> La conmutación lineal **nunca ocurre** en la práctica debido a la **f.e.m. de autoinducción e inducción mutua** en la sección conmutada, provocada por la variación de corriente en la propia sección y en las adyacentes.

## Reacción de armadura

Al conectar una **carga** a los terminales de la máquina, circula corriente por los devanados del inducido. Esta corriente produce un **campo magnético propio** que **distorsiona el campo original** de los polos. Esta distorsión del flujo conforme aumenta la carga se llama **reacción de armadura** (o reacción del inducido) y produce **dos problemas**:

1. **Desplazamiento del plano neutro.**
2. **Debilitamiento del campo magnético** de los polos de la máquina.

![[T03 - Figura 4. Reaccion de inducido y desplazamiento del plano neutro.jpg]]
> **Figura 4.** Reacción de inducido y desplazamiento del plano neutro.

### Consecuencia sobre la conmutación

En la posición intermedia, la escobilla pasa de la delga 3 a la 4, quedando la sección C **en cortocircuito** (resistencia muy baja). Un flujo magnético variable enlazado en la bobina produce una f.e.m. muy alta. Hay dos casos:

- **Sección C se cortocircuita justo en el plano neutro:** el flujo pasa de crecer a decrecer, su derivada es **cero** y también la f.e.m. inducida → no hay problema.
- **El plano neutro se ha desplazado:** la derivada del flujo **no es cero**, se induce una f.e.m. en la sección cortocircuitada. Al tener resistencia muy baja, cualquier f.e.m. produce una **corriente circulante** → **chispas** y baja vida del colector y las escobillas.

![[T03 - Figura 5. Tramo del devanado en cortocircuito en la conmutacion.png]]
> **Figura 5.** Tramo del devanado en cortocircuito durante la conmutación.

### Métodos de corrección

Los problemas derivados de la reacción de inducido se corrigen:

- **Desplazando las escobillas** al nuevo plano neutro.
- Colocando en el estator **polos o interpolos de conmutación**.
- Colocando en el inducido **devanados de compensación**.

> [!summary] Idea central
> La **reacción de armadura** distorsiona el campo de los polos bajo carga → **desplaza el plano neutro** y **debilita el campo**, provocando **chispas** en el colector durante la **conmutación**. Se corrige con **interpolos de conmutación** y **devanados de compensación**. Estos efectos cierran la descripción de la máquina DC iniciada en el [[S12-1 Tema 01 - Máquinas de corriente continua|Tema 01]].

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
