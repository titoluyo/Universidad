---
title: "Ejercicio resuelto - Motor con excitación compuesta (compound)"
curso: "[[Motores MOC]]"
unidad: 3
semana: 13
orden: 5
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/motor-compuesto
  - tema/balance-de-potencias
  - tema/par-motor
date: 2026-06-15
---

> [!info] Material original
> Ejercicio en video del docente. Guion (transcripción): [s13-guion-ejercicio3.pdf](attachments/s13-guion-ejercicio3.pdf) (UTP, Semana 13).

## Enunciado

Un **motor DC en conexión compound de derivación larga** tiene: fuerza contraelectromotriz $E = 230\ \text{V}$, resistencia de armadura $R_a = 0{,}1\ \Omega$, resistencia de excitación shunt $R_{sh} = 40\ \Omega$ y resistencia de excitación serie $R_{se} = 0{,}1\ \Omega$. Se conecta a $V = 240\ \text{V}$. Calcular:

- **a)** Las corrientes que circulan por los devanados.
- **b)** La potencia mecánica suministrada, la potencia de línea y las pérdidas.
- **c)** El par motor a $1000\ \text{rpm}$.

## a) Corrientes

**Corriente de derivación (shunt):**

$$I_d = \frac{V}{R_{sh}} = \frac{240}{40} = 6\ \text{A}$$

**Corriente de armadura** (en derivación larga, la serie está con la armadura):

$$I_a = \frac{V - E}{R_a + R_{se}} = \frac{240 - 230}{0{,}1 + 0{,}1} = \frac{10}{0{,}2} = 50\ \text{A}$$

**Corriente de línea (de la fuente):**

$$I = I_a + I_d = 50 + 6 = 56\ \text{A}$$

## b) Potencias

**Potencia total de línea:**

$$P_{total} = V\,I = (240)(56) = 13\,440\ \text{W}$$

**Pérdidas (efecto Joule):**

$$P_{pérd} = I_a^2\,(R_a + R_{se}) + I_d^2\,R_{sh} = (50)^2(0{,}2) + (6)^2(40) = 500 + 1440 = 1940\ \text{W}$$

**Potencia mecánica (útil):**

$$P_{mec} = P_{total} - P_{pérd} = 13\,440 - 1940 = 11\,500\ \text{W}$$

## c) Par motor a 1000 rpm

$$T = \frac{P_{mec}}{\omega} = \frac{P_{mec}}{2\pi\frac{n}{60}} = \frac{11\,500}{2\pi\frac{1000}{60}} = \frac{11\,500}{104{,}72}$$

$$\boxed{T \approx 109{,}81\ \text{N}\cdot\text{m}}$$

> [!success] Resultados
> | Magnitud | Valor |
> | --- | --- |
> | $I_d$ (shunt) | $6\ \text{A}$ |
> | $I_a$ (armadura) | $50\ \text{A}$ |
> | $I$ (línea) | $56\ \text{A}$ |
> | $P_{total}$ | $13\,440\ \text{W}$ |
> | $P_{pérdidas}$ | $1940\ \text{W}$ |
> | $P_{mecánica}$ | $11\,500\ \text{W}$ |
> | $T$ (a 1000 rpm) | $109{,}81\ \text{N}\cdot\text{m}$ |

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
- Pretel Díaz, Ch. H. (2026). *Ejercicio de motor de c.c. con excitación en compuesto* [Video – Guion]. UTP+class.
