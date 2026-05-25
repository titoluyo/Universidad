---
title: Introducción a la semana 08 - Pérdidas, eficiencia y regulación del transformador
curso: "[[Motores MOC]]"
unidad: 2
semana: 8
orden: 0
tipo: introduccion
tags:
  - curso/motores
  - tipo/introduccion
  - tema/transformador-ideal-vs-real
  - tema/perdidas-transformador
  - tema/eficiencia-transformador
  - tema/regulacion-tension
date: 2026-05-11
---

## Bienvenida

¡Te damos la bienvenida! En esta sesión de aprendizaje **analizaremos las pérdidas y la eficiencia de un transformador monofásico real** a través de su circuito equivalente. Iniciemos revisando las **diferencias entre el transformador ideal y real**.

## Diferencias entre transformador ideal y real

Mientras que un **transformador ideal** es un concepto teórico que se utiliza para simplificar los cálculos y análisis en la teoría eléctrica, un **transformador real** tiene limitaciones y características físicas que lo hacen menos eficiente y más complejo en la práctica.

| Aspecto | Transformador ideal | Transformador real |
| ------- | ------------------- | ------------------ |
| **Eficiencia** | No tiene pérdidas de energía. | Experimenta pérdidas debido a la **resistencia eléctrica de los devanados de cobre** y al **flujo de corrientes parásitas y pérdidas por histéresis**, lo que resulta en una eficiencia inferior. |
| **Inductancia** | La inductancia es **puramente magnética**. | Además de la inductancia magnética, hay una **inductancia debida a la dispersión** del flujo magnético en cada devanado. |
| **Regulación de voltaje** | La relación de voltaje es **exactamente proporcional al número de vueltas** de los devanados. | Debido a las pérdidas y la resistencia, la relación de voltaje **puede variar ligeramente con la carga** y las condiciones de operación. |
| **Pérdidas** | No tiene pérdidas. | Experimenta **pérdidas por efecto Joule** en los devanados (cobre) y **pérdidas magnéticas** en el núcleo (hierro). |
| **Físico** | No tiene dimensiones físicas. | Tiene una estructura física que incluye **núcleo, devanados y aislamiento**. |

> [!info] Conexión con la semana
> En la [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real|semana 7]] construimos el circuito equivalente del transformador real con todos sus parámetros. En la [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real|semana 7 — Tema 02]] vimos cómo los ensayos de vacío y cortocircuito entregan esos parámetros. **Esta semana aplicamos ese circuito** para calcular el desempeño real del transformador: eficiencia, regulación de tensión, diagrama fasorial. Y abrimos el autotransformador como aplicación práctica.

## Mapa de la semana

| Tema | Notas |
| ---- | ----- |
| **Tema 01** — Parámetros | [[S08-1 Tema 01 - Determinación de los parámetros del transformador\|Determinación de los parámetros del transformador]] |
| **Tema 02** — Eficiencia y regulación | [[S08-2 Tema 02 - Eficiencia y regulación del transformador real\|Eficiencia y regulación]] · [[S08-3 Ejercicio resuelto - Eficiencia y regulación (Video)\|Ejercicio resuelto]] |
| **Tema 03** — Diagrama fasorial | [[S08-4 Tema 03 - Diagrama fasorial\|Diagrama fasorial]] |
| **Tema 04** — Autotransformador | [[S08-5 Tema 04 - El autotransformador\|El autotransformador]] |
| **Evaluación** | [[S08-99 Evaluación Semana 08 - PA Práctica Aplicada\|🔴 PA - Práctica Aplicada (AC-S08)]] · calificada · vencida 17 may |
| **Cierre** | [[S08-8 Conclusiones semana 08\|Conclusiones]] |

> [!warning] PA — Práctica Aplicada
> Esta semana se rinde la **Práctica Aplicada (PA)** — primera de las 4 evaluaciones individuales del PA promediado (semanas 03, 08, 13, 16). Aporta al 10 % del promedio final. Ventana: viernes 15 a domingo 17 de mayo de 2026.

## Infografía original

![[s08-intro-infografia-ideal-vs-real.pdf]]
