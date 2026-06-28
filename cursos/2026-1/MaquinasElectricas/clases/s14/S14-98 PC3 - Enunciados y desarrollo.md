---
title: PC3 - Práctica Calificada 3 - Enunciados y desarrollo
curso: "[[Motores MOC]]"
unidad: 3
semana: 14
orden: 98
tipo: evaluacion
subtipo: pc
tags:
  - curso/motores
  - tipo/evaluacion
  - subtipo/pc
  - tema/generador-dc
  - tema/motor-serie
  - tema/motor-compuesto
  - tema/regulacion-de-velocidad
  - tema/frenado-motor-dc
date: 2026-06-22
---

> [!info] Origen
> Enunciados transcritos del examen subido por el usuario (`EXAMEN DE MAQUINAS ELECTRICAS 3.docx`). Metadatos, indicaciones y rúbrica en [[S14-99 Evaluación Semana 14 - PC3 Práctica Calificada 3|S14-99]].

> [!note] Entrega
> El documento con la solución **debe subirse en ambas secciones** ("Evaluaciones" y "Tareas"), el **mismo PDF**. Las preguntas 2 y 3 deben resolverse **a mano** y adjuntarse como fotos.

---

## Pregunta 1 — Conceptos sobre generadores de CC (4 puntos)

**1.1.** ¿Cómo se les conoce a las máquinas donde los devanados inductor e inducido están **separados**, y el inductor es alimentado por una **fuente externa** (p. ej. una batería)?

> [!success] Respuesta: máquinas de **excitación independiente**
> El devanado inductor no toma corriente del propio inducido. Ver [[S13-1 Tema 01 - Generador de corriente continua|excitación independiente]].

**1.2.** ¿Cómo se les conoce a las máquinas donde inductor e inducido están **conectados entre sí** y la máquina puede excitarse a sí misma con la corriente del propio inducido?

> [!success] Respuesta: máquinas **autoexcitadas** (autoexcitación)
> Se subdividen en serie, derivación (shunt) y compuesta.

**1.3.** Máquinas cuyo inductor se conecta directamente a los terminales, **en paralelo con el inducido**, con devanado de **hilo delgado y gran número de espiras**:

> [!success] Respuesta: máquinas de **excitación en derivación (shunt)**

**1.4.** Máquinas donde la excitación se divide entre un devanado **en serie** (pocas espiras de hilo grueso) y otro **en paralelo** (muchas espiras de hilo delgado):

> [!success] Respuesta: máquinas de **excitación compuesta (compound)**

| # | Descripción | Tipo |
| --- | --- | --- |
| 1.1 | Inductor separado, fuente externa | **Independiente** |
| 1.2 | Se excita con su propia corriente | **Autoexcitada** |
| 1.3 | Inductor en paralelo, hilo delgado muchas espiras | **Derivación (shunt)** |
| 1.4 | Serie (hilo grueso) + paralelo (hilo delgado) | **Compuesta (compound)** |

---

## Pregunta 2 — Motor serie (6 puntos)

**Enunciado.** Un motor tipo **serie** de **110 V** gira a **1500 r.p.m.**, consume **35 A** y desarrolla un par de **20 N·m**. La resistencia del motor es **0,3 Ω**. Calcula a qué velocidad girará cuando el par sea de **15 N·m**, suponiendo que el **flujo es proporcional a la corriente**.

![[PC3 - P2 Circuito motor serie.png]]
> Circuito del motor serie: $V = 110\ \text{V}$, $R_i = 0{,}3\ \Omega$, $I = I_i = I_e$.

**Datos:** $V=110$ V, $n_1=1500$ rpm, $I_1=35$ A, $T_1=20$ N·m, $R_i=0{,}3\ \Omega$, $T_2=15$ N·m.

### Planteamiento

En el motor serie $\phi = K_I\,I_i$, por lo que el par es $T = K_T\,\phi\,I_i = K_T K_I\,I_i^2$, es decir **$T \propto I_i^2$**. La f.e.m. es $E = K_E\,\phi\,n = K_E K_I\,n\,I_i$.

### 1) Nueva corriente (de $T \propto I^2$)

$$\frac{I_2}{I_1} = \sqrt{\frac{T_2}{T_1}} = \sqrt{\frac{15}{20}} = \sqrt{0{,}75} = 0{,}8660$$

$$I_2 = 35 \times 0{,}8660 = 30{,}31\ \text{A}$$

### 2) Fuerzas contraelectromotrices

$$E_1 = V - R_i I_1 = 110 - 0{,}3(35) = 99{,}5\ \text{V}$$
$$E_2 = V - R_i I_2 = 110 - 0{,}3(30{,}31) = 100{,}91\ \text{V}$$

### 3) Nueva velocidad

Como $E = K_E K_I\,n\,I_i \Rightarrow n = \dfrac{E}{K_E K_I\,I_i}$, se tiene $\dfrac{n_2}{n_1} = \dfrac{E_2}{E_1}\cdot\dfrac{I_1}{I_2}$:

$$n_2 = n_1\,\frac{E_2}{E_1}\,\frac{I_1}{I_2} = 1500 \times \frac{100{,}91}{99{,}5} \times \frac{35}{30{,}31}$$

$$n_2 = 1500 \times 1{,}01414 \times 1{,}15474 = \boxed{1757\ \text{rpm}}$$

> [!success] Interpretación
> Al **reducir el par** (20 → 15 N·m) la corriente baja (35 → 30,3 A) y, como en el motor serie la velocidad **crece al disminuir la carga** ($n \propto 1/\sqrt{T}$ aprox.), la velocidad **sube** de 1500 a ≈1757 rpm. Coherente con la [[S14-2 Tema 02 - Regulación de velocidad de un motor de corriente continua|característica hiperbólica del motor serie]].

---

## Pregunta 3 — Motor compound en derivación larga (6 puntos)

**Enunciado.** Un motor de CC **compound en derivación larga** tiene: f.c.e.m. $E'=230$ V, resistencia de armadura $R_a=0{,}1\ \Omega$, resistencia de excitación shunt $R_d=40\ \Omega$ y resistencia de excitación serie $R_s=0{,}1\ \Omega$. Se conecta a $V_b=240$ V.

![[PC3 - P3 Circuito motor compound derivacion larga.png]]
> Conexión **derivación larga**: el devanado shunt $R_d$ va en paralelo con todo el conjunto (serie + armadura), directamente a la línea $V_b$.

### a) Corrientes en los devanados

**Corriente de excitación shunt** (el devanado $R_d$ está a la tensión de línea):

$$I_d = \frac{V_b}{R_d} = \frac{240}{40} = \boxed{6\ \text{A}}$$

**Corriente de armadura** (rama serie + armadura): $V_b = E' + I_a(R_a + R_s)$

$$I_a = \frac{V_b - E'}{R_a + R_s} = \frac{240 - 230}{0{,}1 + 0{,}1} = \frac{10}{0{,}2} = \boxed{50\ \text{A}}$$

**Corriente de línea:**

$$I = I_a + I_d = 50 + 6 = \boxed{56\ \text{A}}$$

### b) Potencias y pérdidas

**Potencia de la línea (entrada eléctrica):**
$$P_{\text{línea}} = V_b\,I = 240 \times 56 = 13\,440\ \text{W} = 13{,}44\ \text{kW}$$

**Potencia mecánica desarrollada (electromagnética):**
$$P_{\text{mec}} = E'\,I_a = 230 \times 50 = 11\,500\ \text{W} = 11{,}5\ \text{kW}$$

**Pérdidas en los devanados (cobre):**

| Devanado | Pérdida | Valor |
| --- | --- | --- |
| Armadura | $I_a^2 R_a = 50^2(0{,}1)$ | 250 W |
| Serie | $I_a^2 R_s = 50^2(0{,}1)$ | 250 W |
| Shunt | $I_d^2 R_d = 6^2(40) = V_b I_d$ | 1440 W |
| **Total** | | **1940 W** |

> [!check] Balance de potencias
> $P_{\text{mec}} + P_{\text{cobre}} = 11\,500 + 1940 = 13\,440\ \text{W} = P_{\text{línea}}$ ✓

### c) Par motor a 1000 r.p.m.

$$\omega = \frac{2\pi n}{60} = \frac{2\pi(1000)}{60} = 104{,}72\ \text{rad/s}$$
$$T = \frac{P_{\text{mec}}}{\omega} = \frac{11\,500}{104{,}72} = \boxed{109{,}8\ \text{N·m}}$$

### d) Posición del compound en la escala de velocidad

> [!success] Respuesta: velocidad **media (intermedia)**
> En la gráfica $n$–$T$, el **motor shunt** mantiene velocidad casi constante (alta) y el **motor serie** parte muy alto y cae bruscamente con el par. El **compound** queda **entre ambos**: ocupa la posición **media** de la escala de velocidad. Ver [[S13-2 Tema 02 - El motor de corriente continua|curvas características]].

---

## Pregunta 4 — Relacionar enunciados (4 puntos)

| N° | Enunciado | Respuesta |
| --- | --- | --- |
| 1 | Dispositivo que permite el paso de corriente por el inductor antes o al mismo tiempo que por el inducido | **c) Reóstato** (de arranque) |
| 2 | Motor con frenado **contracorriente** y **dinámico** (con excitación independiente y autoexcitación) | **d) Motor serie** |
| 3 | Motor con frenado **regenerativo (hipersincronismo)**, **dinámico/por c.c.** y **contracorriente** | **b) Motor Compound** |
| 4 | Motor con frenado **regenerativo**, **contracorriente** y **dinámico** | **a) Motor Shunt** |

> [!info] Sustento
> Los tipos de frenado por motor se desarrollan en [[S14-1 Tema 01 - Arranque, frenado e inversión del sentido de giro en motores DC|Tema 01]]: el **reóstato de arranque** controla la corriente inductora; el **motor serie** admite contracorriente y dinámico (indep./autoexc.); el **compound** admite regenerativo, dinámico y contracorriente; el **shunt** admite regenerativo, contracorriente y dinámico.
>
> **Respuestas:** 1→c, 2→d, 3→b, 4→a.

---

## Resumen de respuestas

| Pregunta | Respuesta |
| --- | --- |
| 1 | Independiente · Autoexcitada · Derivación (shunt) · Compuesta (compound) |
| 2 | $I_2=30{,}31$ A; $E_2=100{,}91$ V; **$n_2 \approx 1757$ rpm** |
| 3 | $I_d=6$ A, $I_a=50$ A, $I=56$ A; $P_\text{línea}=13{,}44$ kW, $P_\text{mec}=11{,}5$ kW, $P_\text{cu}=1940$ W; $T=109{,}8$ N·m; posición **media** |
| 4 | 1→c, 2→d, 3→b, 4→a |

## Notas relacionadas

- [[S14-1 Tema 01 - Arranque, frenado e inversión del sentido de giro en motores DC|Arranque, frenado e inversión]]
- [[S14-2 Tema 02 - Regulación de velocidad de un motor de corriente continua|Regulación de velocidad]]
- [[S14-3 Ejercicio resuelto - Regulación de velocidad de motor serie (Video)|Ejercicio motor serie con saturación]]
- [[S13-1 Tema 01 - Generador de corriente continua|Generador de corriente continua]] · [[S13-2 Tema 02 - El motor de corriente continua|Motor de corriente continua]]
