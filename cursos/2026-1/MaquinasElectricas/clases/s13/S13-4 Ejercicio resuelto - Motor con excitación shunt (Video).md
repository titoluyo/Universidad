---
title: "Ejercicio resuelto - Motor con excitación shunt (derivación)"
curso: "[[Motores MOC]]"
unidad: 3
semana: 13
orden: 4
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/motor-shunt
  - tema/regulacion-de-velocidad
  - tema/reostato-de-campo
date: 2026-06-15
---

> [!info] Material original
> Ejercicio en video del docente. Guion (transcripción): [s13-guion-ejercicio2.pdf](attachments/s13-guion-ejercicio2.pdf) (UTP, Semana 13).

## Enunciado

Un **motor tipo derivación (shunt)** de $240\ \text{V}$ tiene una resistencia de inducido (incluyendo escobillas y polos auxiliares) $R_i = 0{,}04\ \Omega$ y una resistencia de campo $R_{exc} = 100\ \Omega$. Se pide:

- **a)** Resistencia a **añadir** al circuito inductor para subir la velocidad de $1200$ a $1500\ \text{rpm}$ con corriente de alimentación $200\ \text{A}$.
- **b)** Con esa resistencia de campo, velocidad cuando la corriente de alimentación sea $100\ \text{A}$.
- **c)** Corriente de campo a $1200\ \text{rpm}$.
- **d)** Velocidad cuando la corriente de excitación sea $2\ \text{A}$.

*(Curva de magnetización ideal — lineal.)*

## Estado inicial (1200 rpm, 200 A)

$$I_{exc} = \frac{V}{R_{exc}} = \frac{240}{100} = 2{,}4\ \text{A}$$

$$I_i = I_{línea} - I_{exc} = 200 - 2{,}4 = 197{,}6\ \text{A}$$

$$E = V - R_i\,I_i = 240 - (0{,}04)(197{,}6) = 232{,}1\ \text{V}$$

Con magnetización lineal, $E = K_E\,n\,I_{exc}$ (el flujo es proporcional a la corriente de excitación).

## a) Resistencia a añadir para 1500 rpm

Usando $\dfrac{E}{E'} = \dfrac{n\,I_{exc}}{n'\,I_{exc}'}$ junto con $E' = V - R_i\,(I_{línea} - I_{exc}')$, se obtiene:

$$E' = 232{,}1\ \text{V} \quad;\quad I_{exc}' = 1{,}92\ \text{A}$$

La resistencia total del circuito de campo necesaria:

$$R_{exc}' = \frac{V}{I_{exc}'} = \frac{240}{1{,}92} = 125\ \Omega$$

Como el inductor ya tiene $100\ \Omega$, hay que **añadir**:

$$\boxed{R_{añadir} = 125 - 100 = 25\ \Omega}$$

> [!note] Reducir el flujo sube la velocidad
> Añadir resistencia de campo **reduce la corriente de excitación** (de 2,4 a 1,92 A) → reduce el flujo → **aumenta la velocidad** (de 1200 a 1500 rpm), confirmando el método (a) de [[S13-2 Tema 02 - El motor de corriente continua#Regulación de velocidad|regulación de velocidad]].

## b) Velocidad con corriente de alimentación de 100 A

$$I_i'' = 100 - 1{,}92 = 98{,}08\ \text{A}$$

$$E'' = V - R_i\,I_i'' = 240 - (0{,}04)(98{,}08) = 236{,}07\ \text{V}$$

Aplicando la proporción de f.e.m.:

$$\boxed{n'' \approx 1525{,}6\ \text{rpm}}$$

## c) y d) Operación como generador

- **c)** Corriente de campo (régimen generador) a 1200 rpm: $\;E_g = 248{,}1\ \text{V}$, $\;I_{exc,g} \approx 2{,}56\ \text{A}$.
- **d)** Con $I_{exc} = 2\ \text{A}$ (generador, $I_i = 200 + 2 = 202\ \text{A}$): $\;E_g' = 240 + (0{,}04)(202) = 248{,}08\ \text{V}$ → $\;\boxed{n \approx 1539{,}1\ \text{rpm}}$.

> [!success] Resultados
> | Punto | Resultado |
> | --- | --- |
> | a) | Añadir $25\ \Omega$ al circuito de campo |
> | b) | $n'' = 1525{,}6\ \text{rpm}$ |
> | c) | $I_{exc,g} \approx 2{,}56\ \text{A}$ ($E_g = 248{,}1\ \text{V}$) |
> | d) | $n \approx 1539{,}1\ \text{rpm}$ |

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
- Pretel Díaz, Ch. H. (2026). *Ejercicio de motor de c.c. con excitación en shunt* [Video – Guion]. UTP+class.
