---
title: "Ejercicio resuelto - Máquina elemental DC (espira giratoria)"
curso: "[[Motores MOC]]"
unidad: 3
semana: 12
orden: 3
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/maquina-dc
  - tema/tension-inducida
  - tema/par-inducido
  - tema/motor-vs-generador
date: 2026-06-08
---

> [!info] Material original
> Ejercicio en video del docente. Guion (transcripción): [s12-guion-ejercicio-fmm.pdf](attachments/s12-guion-ejercicio-fmm.pdf) (UTP, Semana 12).

## Enunciado

Una **espira giratoria sencilla** entre caras polares curvas está conectada a una **batería** y a un **resistor** mediante un interruptor. El resistor representa la resistencia total de la batería y del alambre. Datos de la máquina:

> [!note] Datos
> - Radio: $r = 0{,}5\ \text{m}$
> - Longitud: $l = 1\ \text{m}$
> - Resistencia: $R = 0{,}3\ \Omega$
> - Inducción de campo magnético: $B = 0{,}25\ \text{T}$
> - Voltaje de la batería: $V_B = 120\ \text{V}$

Se pide:
- **a)** ¿Qué sucede cuando se cierra el interruptor?
- **b)** ¿Cuál es la corriente de arranque máxima? ¿Y la velocidad angular en estado estacionario en vacío?
- **c)** Si se añade una carga con par resultante de $10\ \text{N}\cdot\text{m}$: ¿nueva velocidad? ¿potencia al eje? ¿potencia de la batería? ¿motor o generador?
- **d)** En vacío de nuevo, se aplica al eje un par de $7{,}5\ \text{N}\cdot\text{m}$ **en el sentido de rotación**: ¿nueva velocidad? ¿motor o generador?
- **e)** En vacío, si se reduce la densidad de flujo a $B = 0{,}20\ \text{T}$: ¿velocidad final?

## Relaciones de la máquina

De la [[S12-2 Tema 02 - Fuerza magnetomotriz y tensión inducida|deducción del Tema 02]], con $\dfrac{2}{\pi}\phi = \dfrac{2}{\pi}(\pi r l B) = 2rlB$:

$$e_{ind} = \frac{2}{\pi}\phi\,\omega = 2rlB\,\omega \qquad ; \qquad \tau_{ind} = \frac{2}{\pi}\phi\,i = 2rlB\,i$$

Conviene calcular el factor común $\;2rlB = 2(0{,}5)(1)(0{,}25) = 0{,}25$.

## Desarrollo

### a) Al cerrar el interruptor

La espira está **estacionaria**, por lo que $e_{ind} = 0$. La corriente arranca con todo el voltaje de la batería:

$$i = \frac{V_B - e_{ind}}{R} = \frac{V_B}{R}$$

Esta corriente produce un **par inducido** $\tau_{ind} = 2rlB\,i$ que **acelera el rotor**. Al girar, aparece una $e_{ind}$ creciente que **reduce** la corriente.

### b) Corriente de arranque y velocidad en vacío

$$i_{arr} = \frac{V_B}{R} = \frac{120}{0{,}3} = \boxed{400\ \text{A}}$$

En estado estacionario **en vacío** no hay carga → $\tau_{ind} = 0$ → $i = 0$ → $V_B = e_{ind}$. Despejando la velocidad:

$$\omega = \frac{V_B}{2rlB} = \frac{120}{0{,}25} = \boxed{480\ \text{rad/s}}$$

### c) Con carga de $10\ \text{N}\cdot\text{m}$

$$i = \frac{\tau}{2rlB} = \frac{10}{0{,}25} = 40\ \text{A}$$

$$e_{ind} = V_B - iR = 120 - (40)(0{,}3) = 108\ \text{V}$$

$$\omega = \frac{e_{ind}}{2rlB} = \frac{108}{0{,}25} = \boxed{432\ \text{rad/s}}$$

$$P_{eje} = \tau\cdot\omega = (10)(432) = 4320\ \text{W} \approx 4{,}3\ \text{kW}$$

$$P_{bat} = V_B\cdot i = (120)(40) = 4800\ \text{W} = 4{,}8\ \text{kW}$$

> [!success] Opera como MOTOR
> Convierte **potencia eléctrica en mecánica**. La batería entrega $4{,}8\ \text{kW}$, de los cuales $4{,}3\ \text{kW}$ van al eje (la diferencia, $480\ \text{W}$, se disipa en $R$: $i^2R = 40^2\cdot0{,}3 = 480\ \text{W}$ ✓).

### d) Par externo de $7{,}5\ \text{N}\cdot\text{m}$ en el sentido de rotación

El par externo **impulsa** el eje → la corriente invierte su sentido y el par inducido se **opone** al movimiento.

$$i = \frac{\tau}{2rlB} = \frac{7{,}5}{0{,}25} = 30\ \text{A}$$

$$e_{ind} = V_B + iR = 120 + (30)(0{,}3) = 129\ \text{V}$$

$$\omega = \frac{e_{ind}}{2rlB} = \frac{129}{0{,}25} = \boxed{516\ \text{rad/s}}$$

> [!success] Opera como GENERADOR
> El par externo entrega potencia mecánica que la máquina convierte en eléctrica y **devuelve a la batería** ($e_{ind} > V_B$).

### e) En vacío con $B = 0{,}20\ \text{T}$

Nuevo factor: $2rlB = 2(0{,}5)(1)(0{,}20) = 0{,}20$. En vacío $\tau=0 \Rightarrow i=0 \Rightarrow V_B = e_{ind}$:

$$\omega = \frac{V_B}{2rlB} = \frac{120}{0{,}20} = \boxed{600\ \text{rad/s}}$$

> [!note] Al disminuir el flujo, aumenta la velocidad
> Bajar el flujo de $0{,}25$ a $0{,}20\ \text{T}$ subió la velocidad de $480$ a $600\ \text{rad/s}$. Es el **mismo comportamiento de los motores DC reales**: el debilitamiento de campo es un método clásico para aumentar la velocidad.

## Resumen de resultados

| Inciso | Condición | Resultado |
| --- | --- | --- |
| b | Arranque | $i_{arr} = 400\ \text{A}$ |
| b | Vacío ($B=0{,}25$) | $\omega = 480\ \text{rad/s}$ |
| c | Carga $10\ \text{N}\cdot\text{m}$ | $i=40\ \text{A}$, $\omega=432\ \text{rad/s}$, $P_{eje}=4{,}3\ \text{kW}$, $P_{bat}=4{,}8\ \text{kW}$ → **motor** |
| d | Par externo $7{,}5\ \text{N}\cdot\text{m}$ | $i=30\ \text{A}$, $\omega=516\ \text{rad/s}$ → **generador** |
| e | Vacío ($B=0{,}20$) | $\omega = 600\ \text{rad/s}$ |

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
- Pretel Díaz, Ch. H. (2026). *Ejercicio de fuerza magnetomotriz y tensión inducida* [Video – Guion]. UTP+class.
