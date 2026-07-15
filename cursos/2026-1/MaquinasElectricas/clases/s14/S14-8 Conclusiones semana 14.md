---
title: Conclusiones semana 14 - Arranque, frenado, inversión y regulación de motores DC
curso: "[[Motores MOC]]"
unidad: 3
semana: 14
orden: 8
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tipo/resumen
  - tema/arranque-motor-dc
  - tema/frenado-motor-dc
  - tema/inversion-de-giro
  - tema/regulacion-de-velocidad
date: 2026-06-22
---

> [!info] Origen del material
> Infografía estática de cierre del docente.

![[Semana 14 - Infografia - Ideas clave.pdf]]

¡Finalizaste la semana! Revisa las **ideas clave** que cierran la sesión y la **Unidad 3**.

## Ideas clave de la semana

> [!summary] 1. Arranque: limitar la corriente
> Al arrancar, $E = 0$ y la corriente directa $I_i = V/R_i$ sería excesiva. Se intercala un **reóstato de arranque** en serie con el inducido, que va eliminando resistencia por tramos para un **arranque suave**, sin picos que dañen el colector y las escobillas.
>
> Detalle en [[S14-1 Tema 01 - Arranque, frenado e inversión del sentido de giro en motores DC|Tema 01]].

> [!summary] 2. Frenado: tres modos
> La máquina se opone al movimiento pasando a funcionar como **generador**: **regenerativo** (devuelve energía a la red, en hipersincronismo), **dinámico** (disipa la energía cinética en una resistencia) y **a contracorriente** (invierte la tensión/corriente del inducido). Aplicables a motores serie, shunt y compuesto.

> [!summary] 3. Inversión del sentido de giro
> Se logra **permutando los bornes del inducido** (cambio de polaridad). La maniobra automatizada usa **contactores temporizados** ($KM_1$/$KM_2$): giro directo → frenado por inercia → arranque inverso.

> [!summary] 4. Regulación de velocidad
> De $n = \dfrac{V - R_i I_i}{K_E\,\phi}$ surgen los tres mandos: **tensión** $V$ (rectas paralelas, distinto $n_0$), **resistencia de inducido** (mayor pendiente, mismo $n_0$) y **flujo** $\phi$ (debilitar el campo sube la velocidad). En el **serie**, $n \propto 1/\sqrt{T}$ → no arrancar en vacío; el **compuesto** queda entre shunt y serie.
>
> Desarrollo en [[S14-2 Tema 02 - Regulación de velocidad de un motor de corriente continua|Tema 02]] y aplicación en el [[S14-3 Ejercicio resuelto - Regulación de velocidad de motor serie (Video)|ejercicio del motor serie]].

## Cierre de la Unidad 3

Con esta semana concluye la **Unidad 3** (conversión de energía electromecánica y máquinas de corriente continua). Lo aprendido se evalúa en la [[S14-99 Evaluación Semana 14 - PC3 Práctica Calificada 3|Práctica Calificada 3]]. La **Unidad 4** (semanas 15-18) aborda las **máquinas de corriente alterna**: la máquina asíncrona trifásica y la máquina síncrona.

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
- Pretel Díaz, Ch. H. (2026). *Ideas clave de la semana 14* [Infografía estática]. UTP+class.
