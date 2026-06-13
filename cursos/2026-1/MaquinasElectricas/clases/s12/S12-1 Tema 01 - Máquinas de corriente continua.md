---
title: "Tema 01 - Máquinas de corriente continua"
curso: "[[Motores MOC]]"
unidad: 3
semana: 12
orden: 1
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/maquina-dc
  - tema/colector-de-delgas
  - tema/devanado-inducido
  - tema/fem-media
  - tema/par-electromagnetico
date: 2026-06-08
---

> [!info] Material original
> Manual del docente: [s12-manual-maquina-dc.pdf](attachments/s12-manual-maquina-dc.pdf) (UTP, Semana 12).

## La máquina de corriente continua (DC)

Las **máquinas de corriente continua (c.c.)** tienen una importancia histórica significativa: fueron pioneras en la producción de energía eléctrica a gran escala entre **1830 y 1880**. A pesar de que la dínamo fue desarrollada antes que el alternador, su etapa experimental buscaba generar una **corriente similar a la de las pilas galvánicas**, previo a los descubrimientos de Oersted y Faraday en electromagnetismo e inducción magnética.

El desarrollo se enfocó en **transformar la corriente alterna inducida en corriente continua** mediante el **conmutador o colector de delgas**, como propuso **Pixii en 1831** y **Gramme** implementó en **1867**. Los motores de corriente continua, basados en el principio de reciprocidad de Faraday y Lenz, ofrecían mayor flexibilidad en el control de velocidad y par, lo que los hizo ideales para accionamientos industriales como tornos de fundición, telares y tracción eléctrica. Sin embargo, con el avance de la electrónica de potencia, los motores de corriente alterna han ganado terreno debido a su menor coste de fabricación y mantenimiento.

## Aspectos constructivos

La máquina de corriente continua (c.c.) se compone de dos partes principales: el **estator** y el **rotor**.

![[T01 - Figura 1. Estructura constructiva de una maquina DC.png]]
> **Figura 1.** Estructura constructiva de una máquina DC: estator (polos inductores, expansión/zapata polar, culata o yugo) y rotor (inducido, colector de delgas).

### Estator

- La **pieza fija** de la máquina; constituye el **circuito magnético inductor**.
- Aloja los **polos inductores** y, si el rotor es de devanado imbricado o de delgas, **proporciona soporte mecánico** a la culata.
- La **culata (yugo)** es la base que **cierra el circuito magnético** entre polos; suele incluir los **polos de conmutación** (interpolos) para mejorar la conmutación.
- Las **expansiones o zapatas polares** distribuyen el flujo magnético sobre la periferia del inducido.

### Rotor (inducido)

- Se compone de dos elementos principales: el **inducido** y el **colector de delgas (conmutador)**.
- El inducido es un cilindro de chapas magnéticas apiladas con **perforaciones en la periferia** para alojar los conductores.
- El **colector** convierte la corriente alterna inducida en las bobinas en **corriente continua** hacia el exterior (o viceversa). Está formado por **delgas de cobre separadas por mica**.
- Las **escobillas** (metalográficas) se mantienen en una posición constante respecto a los polos y extraen/suministran la corriente al colector mediante un contacto deslizante.

> [!note] Tipos de devanado del inducido
> El devanado del inducido puede ser **imbricado** u **ondulado**. En ambos casos las bobinas forman dos ramas en paralelo; el devanado ondulado permite un mayor número de ramas para **maximizar la fuerza electromotriz (f.e.m.)**.

## Principio de funcionamiento

La máquina de c.c. puede operar como **generador** o como **motor**. Para entender el principio de generación de la f.e.m., se analiza una máquina de c.c. con rotor de tipo anillo (**máquina de Gramme**).

![[T01 - Figura 2. Maquina DC con rotor tipo anillo (Gramme) y ejes.png]]
> **Figura 2.** Máquina DC con rotor tipo anillo (Gramme). Se distinguen el **eje longitudinal o directo** (alineado con los polos N–S) y el **eje transversal o de cuadratura** (la **línea neutra**, donde la f.e.m. inducida es nula).

### F.e.m. media inducida

La **f.e.m. media** generada en una espira del inducido, durante medio periodo $T/2$ de variación del flujo, es:

$$E_{med} = \frac{1}{T/2}\int_{0}^{T/2} d\phi = \frac{\phi}{T/2}$$

Como la **frecuencia** de la tensión generada está ligada al número de polos $2p$ y a la velocidad de rotación $n$ (en r.p.m.) por la relación:

$$f = \frac{n \cdot p}{60}$$

la f.e.m. media en una espira del inducido resulta:

$$\boxed{E_{med} = 4\,\phi\,\frac{n \cdot p}{60}}$$

### Par electromagnético

La máquina de c.c. produce un **par electromagnético** en el rotor cuando una corriente continua atraviesa los conductores del inducido. Este par es **resistente** cuando opera como **generador** y **motor** cuando impulsa una carga mecánica.

Si la corriente total del inducido es $I_i$, la corriente por conductor en una máquina con $2c$ circuitos derivados es $\frac{I_i}{2c}$. Con $B_{med}$ la inducción media bajo los polos y $L$ la longitud del conductor, la **fuerza media** por conductor (ley de Laplace) es:

$$F_{med} = B_{med}\cdot L\cdot \frac{I_i}{2c}$$

Con $R$ = radio del rotor y $Z$ = número de conductores del inducido, el **par resultante** es:

$$T = R\cdot F_{med}\cdot Z = R\cdot B_{med}\cdot L\cdot \frac{I_i}{2c}\cdot Z$$

Dado que la superficie del inducido bajo un paso polar es $S_i = \dfrac{2\pi R L}{2p}$, el **flujo por polo** es:

$$\phi = B_{med}\cdot \frac{2\pi R L}{2p}$$

Sustituyendo, el **par en función del flujo por polo** queda:

$$\boxed{T = \frac{1}{2\pi}\cdot\frac{p}{c}\cdot Z\cdot \phi\cdot I_i = K_T\cdot I_i\cdot \phi}$$

donde $K_T = \dfrac{Z}{2\pi}\cdot\dfrac{p}{c}$ es una **constante propia de cada máquina**.

![[T01 - Figura 3. Maquina de cc funcionando como motor.png]]
> **Figura 3.** Máquina de c.c. funcionando como motor: la batería $V$ inyecta corriente $I_i$ al inducido; la interacción con el campo N–S produce el **par electromagnético** en el sentido de rotación.

### Potencia electromagnética

Reescribiendo el par en términos de la f.e.m. del inducido:

$$T = \frac{E\cdot I_i}{2\pi\cdot\frac{n}{60}}\quad [\text{N}\cdot\text{m}]$$

Y la **potencia electromagnética** es el producto del par por la velocidad angular mecánica $\Omega$:

$$\boxed{P_a = E\cdot I_i = T\cdot\Omega = T\cdot 2\pi\cdot\frac{n}{60}\quad [\text{W}]}$$

> [!summary] Idea central
> El **par de una máquina DC** depende de tres factores: el **flujo** $\phi$, la **corriente del inducido** $I_i$ y una **constante constructiva** $K_T$ → $T = K_T\,I_i\,\phi$. La **f.e.m.** es proporcional al flujo y a la velocidad. La deducción detallada del voltaje y el par sobre la espira giratoria se desarrolla en el [[S12-2 Tema 02 - Fuerza magnetomotriz y tensión inducida|Tema 02]].

## Bibliografía

- Chapman, S. J., Rodríguez, C., y Santana, A. (2012). *Máquinas eléctricas* (5.ª ed.). McGraw-Hill.
- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
