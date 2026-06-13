---
title: "Tema 01 - Torques de origen electromagnético"
curso: "[[Motores MOC]]"
unidad: 3
semana: 11
orden: 2
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/torque-electromagnetico
  - tema/momento-dipolar-magnetico
  - tema/conmutador
  - tema/dipolo-magnetico
date: 2026-06-01
---

![[S11 - B1.png]]

## El torque en un bucle de corriente

Cuando la corriente pasa por los bucles, el **campo magnético ejerce un torque** sobre ellos, que hace girar un eje. La **energía eléctrica se convierte en trabajo mecánico** en el proceso.

Una vez que la superficie del bucle se alinea con el campo magnético, el **sentido de la corriente se invierte**, por lo que hay un **torque continuo** sobre el bucle. Esta inversión de la corriente se realiza con **conmutadores y escobillas**:

- El **conmutador** se ajusta para invertir el flujo de corriente en los puntos establecidos, manteniendo un movimiento continuo en el motor. Un conmutador básico tiene **zonas de contacto que hay que evitar** y **puntos muertos** en los que el bucle tendría un torque instantáneo cero.
- Las **escobillas** presionan contra el conmutador, creando el **contacto eléctrico** entre sus partes durante el giro.

### Funcionamiento del conmutador

![[Imagen 1. Funcionamiento del conmutador con conduccion de corriente.jpg]]
> **Imagen 1.** Funcionamiento del conmutador **con** conducción de corriente. Mientras circula corriente, el campo magnético ejerce torque sobre el bucle.

Cuando **no hay conducción de corriente** por el conmutador, sobre el bucle **no actúa ningún torque**, pero el bucle **sigue girando** a partir de la velocidad inicial (inercia).

![[Imagen 2. Funcionamiento del conmutador sin conduccion de corriente.jpg]]
> **Imagen 2.** Funcionamiento del conmutador **sin** conducción de corriente. El bucle mantiene el giro por inercia hasta que se reanuda la conducción.

## Deducción del torque neto

Para calcular el torque neto en el bucle de corriente, primero consideramos las fuerzas $F_1$ y $F_3$. Como tienen la **misma línea de acción** y son **iguales y opuestas**, la suma de sus torques alrededor de cualquier eje es **cero**. Por lo tanto, si hay algún torque en el bucle, debe ser proporcionado por $F_2$ y $F_4$.

![[Imagen 3. Bucle de corriente rectangular en un campo magnetico uniforme.png]]
> **Imagen 3.** Bucle de corriente rectangular en un campo magnético uniforme. Solo $F_2$ y $F_4$ contribuyen al torque neto.

Calculemos los torques alrededor del eje que pasa por el punto $O$ (una **vista lateral** de la bobina) y es perpendicular al plano de la página. El punto $O$ está a una distancia $x$ del lado 2 y a una distancia $(a-x)$ del lado 4 del bucle. Los **brazos de momento** de $F_2$ y $F_4$ son $x\sin\theta$ y $(a-x)\sin\theta$ respectivamente.

![[Imagen 4. Vista lateral de la bobina.png]]
> **Imagen 4.** Vista lateral de la bobina. Se aprecian los brazos de momento $x\sin\theta$ y $(a-x)\sin\theta$ de las fuerzas $F_2$ y $F_4$.

El **torque neto** en el bucle es:

$$\sum\vec{\tau} = \vec{\tau}_1 + \vec{\tau}_2 + \vec{\tau}_3 + \vec{\tau}_4 = -I\,b\,B\,x\sin\theta\;\hat{i} \;-\; I\,b\,B\,(a-x)\sin\theta\;\hat{i}$$

Esto se simplifica a:

$$\vec{\tau} = -I\,A\,B\sin\theta\;\hat{i}$$

donde $A = a\,b$ es el **área del bucle**.

> [!note] El torque es independiente de la posición del eje
> Este momento de torsión es **independiente de la posición $x$**: no importa dónde esté ubicado el punto $O$ en el plano del bucle. El bucle experimenta el **mismo torque** del campo magnético alrededor de cualquier eje en el plano del bucle paralelo al eje $x$.

## Momento dipolar magnético

Se suele llamar **dipolo magnético** a un lazo de corriente cerrado, y el valor $I\cdot A$ se identifica como su **momento dipolar magnético** $\mu$. De hecho, el momento dipolar magnético es un **vector** definido como:

$$\vec{\mu} = I\,A\,\hat{n}$$

donde $\hat{n}$ es un **vector unitario** dirigido perpendicularmente al plano del bucle. Si el bucle contiene $N$ vueltas de cable, su momento dipolar magnético viene dado por:

$$\vec{\mu} = N\,I\,A\,\hat{n}$$

En términos del momento dipolar magnético, el torque en un bucle de corriente debido a un campo magnético uniforme puede escribirse simplemente como:

$$\boxed{\vec{\tau} = \vec{\mu} \times \vec{B}}$$

> [!summary] Idea central
> El **par electromagnético** sobre una espira de corriente es $\vec{\tau} = \vec{\mu}\times\vec{B}$, con $\vec{\mu} = N\,I\,A\,\hat{n}$. Su magnitud $\tau = \mu B\sin\theta$ es **máxima** cuando el plano de la espira es **paralelo** al campo ($\theta = 90°$) y **nula** cuando es **perpendicular** ($\theta = 0°$). El conmutador invierte la corriente para sostener un par en un solo sentido y lograr el giro continuo. Aplicación numérica en el [[S11-3 Ejercicio resuelto - Torque en un bucle de corriente (Video)|ejercicio resuelto]].

## Bibliografía

- Moebs, W., Ling, S. J., y Sanny, J. (2022). *Fuerza y torque en un bucle de corriente*. En *Física universitaria volumen 2*. OpenStax College. Recuperado de https://openstax.org/books/f%C3%ADsica-universitaria-volumen-2/pages/11-5-fuerza-y-torque-en-un-bucle-de-corriente
- Pretel Díaz, Ch. H. (2026). *Torques de origen electromagnético* [Material de estudio]. UTP+class.
