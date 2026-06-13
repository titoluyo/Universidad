---
title: Conclusiones semana 12 - Máquinas de corriente continua
curso: "[[Motores MOC]]"
unidad: 3
semana: 12
orden: 8
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tipo/resumen
  - tema/maquina-dc
  - tema/reaccion-de-armadura
  - tema/conmutacion
date: 2026-06-08
---

> [!info] Origen del material
> El cierre de la semana 12 es un **foro de discusión no calificado** ("Conclusiones semana 12", disponible desde el lunes 8 de junio de 2026). La consigna del docente:
> > ¡Finalizaste la semana! Reflexiona sobre los temas revisados, identifica los conceptos más importantes y elige **3 o 4 frases cortas** que capturen las ideas clave de la sesión, y regístralas en el foro. *(Actividad no calificada.)*

## Ideas clave de la semana

> [!summary] 1. La máquina DC y el colector de delgas
> La **máquina de corriente continua** convierte, mediante el **colector de delgas y las escobillas**, la corriente alterna inducida en las bobinas del [[S12-1 Tema 01 - Máquinas de corriente continua|inducido]] en corriente continua hacia el exterior (y viceversa). Consta de **estator** (polos inductores, culata) y **rotor** (inducido + colector).

> [!summary] 2. Tensión inducida y par dependen del flujo y la corriente
> En la [[S12-2 Tema 02 - Fuerza magnetomotriz y tensión inducida|espira giratoria]], el **voltaje inducido** es $e_{ind} = 2(\vec{v}\times\vec{B})\cdot\vec{l}$ y el **par** $\tau_{ind} = \frac{2}{\pi}\phi\,i$. El par de toda máquina real depende de **tres factores**: el **flujo**, la **corriente** y una **constante constructiva** ($T = K_T\,I_i\,\phi$).

> [!summary] 3. La misma máquina opera como motor o generador
> Según el [[S12-3 Ejercicio resuelto - Máquina elemental DC (Video)|ejercicio]], cuando la batería entrega corriente la máquina es **motor** ($e_{ind} < V_B$); cuando un par externo impulsa el eje, invierte la corriente y actúa como **generador** ($e_{ind} > V_B$). Además, **reducir el flujo aumenta la velocidad**.

> [!summary] 4. La reacción de armadura degrada la conmutación
> Bajo carga, la [[S12-4 Tema 03 - Reacción de armadura y conmutación|reacción de armadura]] **distorsiona el campo** de los polos: **desplaza el plano neutro** y **debilita el campo**, generando **chispas** en el colector durante la **conmutación**. Se corrige con **interpolos de conmutación** y **devanados de compensación**.

## Conexión con la siguiente unidad

Esta semana describió la **construcción** y las **ecuaciones fundamentales** de la máquina DC, más los fenómenos parásitos (reacción de armadura, conmutación). En las próximas semanas se estudian los **tipos concretos** de máquinas DC —generador DC y motores DC serie, shunt y compuesto— con sus curvas características.

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
