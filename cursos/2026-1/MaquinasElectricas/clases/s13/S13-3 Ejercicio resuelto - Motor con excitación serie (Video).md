---
title: "Ejercicio resuelto - Motor con excitación serie"
curso: "[[Motores MOC]]"
unidad: 3
semana: 13
orden: 3
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/motor-serie
  - tema/fuerza-contraelectromotriz
date: 2026-06-15
---

> [!info] Material original
> Ejercicio en video del docente. Guion (transcripción): [s13-guion-ejercicio1.pdf](attachments/s13-guion-ejercicio1.pdf) (UTP, Semana 13).

## Enunciado

Un **motor tipo serie** de $110\ \text{V}$, cuando gira a $1500\ \text{rpm}$ consume $35\ \text{A}$ y desarrolla un par electromagnético de $20\ \text{N}\cdot\text{m}$. La resistencia del motor es $R = 0{,}3\ \Omega$. Calcular a qué velocidad girará el motor:

- **a)** cuando el par desarrollado sea $15\ \text{N}\cdot\text{m}$, suponiendo el **flujo proporcional a la corriente**;
- **b)** cuando la corriente sea el **doble**, suponiendo que el flujo aumente un **30 %**.

## Punto de partida

La **fuerza contraelectromotriz** en el régimen inicial ($I = 35\ \text{A}$):

$$E = V - R\,I = 110 - (0{,}3)(35) = 99{,}5\ \text{V}$$

Igualando potencia electromagnética y mecánica, $E\,I = T\cdot\frac{2\pi n}{60}$:

$$n_{ref} = \frac{E\,I\cdot 60}{T\cdot 2\pi} = \frac{(99{,}5)(35)(60)}{(20)(2\pi)} \approx 1662{,}8\ \text{rpm}$$

> [!note] Dato inconsistente
> El enunciado indica $1500\ \text{rpm}$, pero el balance de potencias con los datos dados arroja $1662{,}8\ \text{rpm}$. Se sigue el desarrollo del video, que usa $n_{ref} = 1662{,}8\ \text{rpm}$ como estado de referencia.

En el motor serie el flujo es proporcional a la corriente, por lo que $E = K_E\,I\,n$ y $T = K_T\,I^2$.

## a) Par de $15\ \text{N}\cdot\text{m}$ (flujo ∝ corriente)

Como $T \propto I^2$:

$$I' = I\sqrt{\frac{T'}{T}} = 35\sqrt{\frac{15}{20}} = 30{,}31\ \text{A}$$

$$E' = V - R\,I' = 110 - (0{,}3)(30{,}31) = 100{,}9\ \text{V}$$

Aplicando la proporción $\dfrac{E}{E'} = \dfrac{n\,I}{n'\,I'}$ (o $E' = K_E\,I'\,n'$):

$$\boxed{n' \approx 1947{,}3\ \text{rpm}}$$

Al **disminuir el par/carga**, la velocidad del motor serie **aumenta** notablemente.

## b) Corriente doble, flujo +30 %

$$I'' = 2\,I = 2(35) = 70\ \text{A}$$

$$E'' = V - R\,I'' = 110 - (0{,}3)(70) = 89\ \text{V}$$

Con $E = K_E\,n\,\phi$ y $\phi'' = 1{,}3\,\phi$, de la proporción $\dfrac{E}{E''} = \dfrac{n\,\phi}{n''\,\phi''}$:

$$\frac{99{,}5}{89} = \frac{n_{ref}}{1{,}3\,n''} \quad\Longrightarrow\quad \boxed{n'' \approx 1144{,}1\ \text{rpm}}$$

> [!success] Resultados
> | Caso | Resultado |
> | --- | --- |
> | a) $T' = 15\ \text{N}\cdot\text{m}$ | $I' = 30{,}31\ \text{A}$, $n' = 1947{,}3\ \text{rpm}$ |
> | b) $I'' = 70\ \text{A}$, $\phi$ +30 % | $n'' = 1144{,}1\ \text{rpm}$ |
>
> Confirma la curva hiperbólica del [[S13-2 Tema 02 - El motor de corriente continua|motor serie]]: menos carga → más velocidad; más corriente/flujo → menos velocidad.

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
- Pretel Díaz, Ch. H. (2026). *Ejercicio de excitación en serie* [Video – Guion]. UTP+class.
