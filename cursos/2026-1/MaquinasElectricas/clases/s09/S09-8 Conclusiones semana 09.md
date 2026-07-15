---
title: Conclusiones semana 09 - Transformador trifásico
curso: "[[Motores MOC]]"
unidad: 2
semana: 9
orden: 8
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/transformador-trifasico
  - tema/cierre-semanal
date: 2026-05-22
---

¡Finalizaste la semana! El cierre es un **crucigrama interactivo (H5P)** dentro de la plataforma — sin material descargable. A continuación se resume lo aprendido.

## Ideas clave de la semana

> [!success] 1. Dos formas de construir un transformador trifásico
> - **Banco de 3 monofásicos** — redundancia, flexibilidad de inventario.
> - **Trifásico con núcleo de 3 columnas** — menor tamaño, peso y costo.
>
> → Detalle: [[S09-1 Tema 01 - El transformador trifásico|El transformador trifásico]].

> [!success] 2. Cuatro conexiones básicas
> | Conexión | $V_{LP}/V_{LS}$ | Desfase | Comentario |
> | -------- | --------------- | ------- | ---------- |
> | **Y–Y**   | $a$              | 0°      | Problemas con cargas desbalanceadas y 3.er armónico |
> | **Y–Δ**   | $\sqrt{3}\,a$    | 30°     | Robusta — la más usada en distribución (con neutro) |
> | **Δ–Y**   | $a/\sqrt{3}$     | 30°     | Igual ventaja; usada para subir tensión |
> | **Δ–Δ**   | $a$              | 0°      | Sin problemas, sin neutro accesible |

> [!success] 3. Análisis por fase
> Todo el marco del transformador monofásico real (circuito equivalente, ensayos, eficiencia, regulación) se aplica **por fase** al transformador trifásico, escalando con $\sqrt{3}$ las magnitudes de línea según la conexión.
>
> → Detalle: [[S09-3 Tema 02 - Circuito equivalente aproximado del transformador trifásico|Circuito equivalente aproximado]].

> [!success] 4. Índice horario
> El **grupo de conexión** (Yy0, Dd0, Dy5, Dy11, Yd5, Yd11, etc.) indica el **desfase entre primario y secundario** en múltiplos de 30°. **Dos transformadores en paralelo deben tener el mismo índice horario** para evitar corrientes circulantes.

## Mapa de la semana

| Tema | Notas |
| ---- | ----- |
| **Tema 01** — Transformador trifásico | [[S09-1 Tema 01 - El transformador trifásico\|Construcción y conexiones]] · [[S09-2 Ejercicio resuelto - Transformador trifásico (Video)\|Ejercicio de las 4 conexiones]] |
| **Tema 02** — Circuito equivalente aproximado | [[S09-3 Tema 02 - Circuito equivalente aproximado del transformador trifásico\|Circuito equivalente e índice horario]] · [[S09-4 Ejercicio resuelto - Circuito equivalente trifásico (Video)\|Ejercicio Δ–Y con carga y línea]] |
| **Material** | [[S09-98 Indicaciones - Práctica Calificada 2\|Indicaciones de la PC2]] |
| **Evaluación** | [[S09-99 Evaluación Semana 09 - PC2 Práctica Calificada 2\|🔴 PC2 - Práctica Calificada 2]] · calificada · 20 pts · 90 min |

## Próxima semana

> [!info] Semana 10
> Cerramos la unidad 2 (transformadores) y abrimos la **Unidad 3 — Conversión de energía electromecánica**: función energía y coenergía. Es la base para entender cómo una máquina rotativa (motor o generador) convierte energía eléctrica en mecánica y viceversa. También se rinde la **LC2** (Laboratorio Calificado 2).

## Cierre — crucigrama H5P

El contenido del cierre es un **crucigrama interactivo** en la plataforma (H5P). No se puede transcribir aquí — para resolverlo, ingresar al portal:
- `/learnv2/week/9/.../theme/e5907618.../content/277aae28.../html`

Sirve como autoevaluación rápida de los términos clave: conexión, fase, línea, desplazamiento, banco, neutro, armónico, etc.
