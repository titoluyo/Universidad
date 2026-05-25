---
title: Introducción a la semana 07 - El transformador real
curso: "[[Motores MOC]]"
unidad: 2
semana: 7
orden: 0
tipo: introduccion
tags:
  - curso/motores
  - tipo/introduccion
  - tema/transformador-real
  - tema/perdidas-transformador
date: 2026-05-04
---

## Bienvenida

¡Te damos la bienvenida a esta semana! En esta sesión de aprendizaje **analizaremos los parámetros básicos del transformador real**, aplicando los métodos de análisis **exacto y aproximado**.

## Historieta: ¿por qué no llegamos a 400 V?

> [!example] Escena
> En el taller, se escuchaba el zumbido constante de la máquina CNC. El ingeniero Martínez está ajustando algunos parámetros. Mientras tanto, David, estudiante de ingeniería, nota que **el voltaje de la máquina no es de 400 V**.

**David:** Ingeniero, ¿por qué no alcanza los 400 voltios? Pensé que debería llegar a ese nivel.

**Ing. Martínez:** Bueno, David, la máquina CNC está conectada a través de un transformador, y eso hace que las cosas sean un poco diferentes a lo que vemos en los libros de texto.

**David:** ¿Cómo es eso?

**Ing. Martínez:** Lo que sucede en un transformador podría elevar o reducir el voltaje **sin pérdida alguna**; pero, en el mundo real, **siempre hay pérdidas**. Por eso no estamos viendo esos 400 V que esperamos.

**David:** ¿Pérdidas? No entendí.

**Ing. Martínez:** Un [[S06-4 Tema 02 - El transformador monofásico ideal|transformador ideal]] no tendría resistencia interna ni pérdidas, lo que significa que toda la energía que entra debería salir sin cambios; pero, en la realidad, **el cobre del bobinado genera calor**. Además, el **núcleo magnético** también experimenta pérdidas por [[S05-1 Tema 01 - Perdidas magneticas en el nucleo|histéresis y corrientes parásitas]].

**David:** Entiendo... Entonces, ¿por eso no llegamos a los 400 voltios?

**Ing. Martínez:** ¡Exacto! La realidad es que parte de la energía se disipa en forma de calor, y eso nos deja con un voltaje ligeramente menor. Si miras la pantalla, verás que estamos cerca, pero no exactamente en los 400 V que queremos.

**David:** ¿Esto quiere decir que siempre habrá pérdidas en un transformador real?

**Ing. Martínez:** Sí, siempre habrá ciertas pérdidas. La clave está en **minimizarlas tanto como sea posible** para obtener un rendimiento eficiente. En la práctica, los ingenieros debemos tener en cuenta estas pérdidas al diseñar sistemas eléctricos.

## Mapa de la semana

| Tema | Notas |
| ---- | ----- |
| **Tema 01** — Circuito equivalente | [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real\|Circuito equivalente exacto y aproximado]] · [[S07-2 Ejercicio resuelto - Circuito equivalente del transformador real (Video)\|Ejercicio circuito equivalente]] |
| **Tema 02** — Ensayos | [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real\|Ensayo de vacío y cortocircuito]] · [[S07-4 Ejercicio resuelto - Ensayos del transformador (Video)\|Ejercicio ensayos]] |
| **Evaluación** | [[S07-99 Evaluación Semana 07 - Cuestionario de autoevaluación\|Cuestionario de autoevaluación]] (no calificada) |
| **Cierre** | [[S07-8 Conclusiones semana 07\|Conclusiones]] |

> [!tip] Idea clave de la semana
> Esta semana **rompemos las hipótesis del transformador ideal** y modelamos cada imperfección como un elemento de circuito (resistencia, reactancia de dispersión, rama de magnetización). Los **ensayos de vacío y cortocircuito** son el método estándar para medir esos parámetros sin desarmar el transformador.

## Historieta original

![[s07-intro-historieta.pdf]]
