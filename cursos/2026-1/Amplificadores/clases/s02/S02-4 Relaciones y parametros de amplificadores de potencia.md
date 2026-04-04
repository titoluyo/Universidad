---
title: "Relaciones y parametros de amplificadores de potencia"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 2
orden: 4
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/amplificador-de-potencia
  - tema/amplificador-clase-a
  - tema/eficiencia
date: 2026-03-31
---

## Relaciones basicas en los amplificadores de potencia

El amplificador de potencia convierte la potencia de CC de la fuente de alimentacion en una senal de potencia en la carga.

### Eficiencia

$$\boxed{\eta = \frac{P_{L(CA)}}{P_{CC}}}$$

Donde:
- $\eta$ = eficiencia
- $P_{L(CA)}$ = potencia media de senal (CA) en la carga
- $P_{CC}$ = potencia media entregada por la fuente de alimentacion

### Potencia disipada en el transistor

$$\boxed{P_{CE} = P_{CC} - P_L}$$

Donde $P_L = P_{L(DC)} + P_{L(CA)}$ es la potencia total en la carga (componente continua + alterna).

### Potencia instantanea

$$p = v \cdot i$$

Para formas de onda periodicas con componente continua y alterna:

$$v = V_{DC} + v_{CA}$$

$$i = I_{DC} + i_{CA}$$

### Potencia media en un periodo T

$$P = \frac{1}{2\pi} \int_0^{2\pi} p \, d\omega t = V_{DC} I_{DC} + \frac{1}{2\pi}\int_0^{2\pi} v_{CA} \, i_{CA} \, d\omega t$$

$$\boxed{P = \underbrace{V_{DC} I_{DC}}_{P_{CC}} + \underbrace{\frac{V_m I_m}{2}}_{P_{CA}}}$$

Como $2 = \sqrt{2} \cdot \sqrt{2}$:

$$P = V_{DC} I_{DC} + V_{rms} I_{rms}$$

### Valor RMS con componente continua

Para una senal periodica con componente continua y armonicos:

$$I_{rms} = \sqrt{I_{DC}^2 + I_{1_{rms}}^2 + I_{2_{rms}}^2 + \cdots + I_{n_{rms}}^2}$$

Para una senal sinusoidal con componente continua:

$$I_{rms} = \sqrt{I_{DC}^2 + I_{rms}^2}$$

## El amplificador de clase A - Emisor comun

En operacion clase A, el amplificador reproduce **toda la senal** de entrada. La corriente de colector es distinta de cero **todo el tiempo**, lo cual es muy ineficiente: con senal cero en la entrada, $I_{CQ} > 0$ y el transistor disipa potencia.

### Circuito emisor comun (con $R_E = 0$)

**Circuito DC (b):**

$$i_C = -\frac{v_{CE}}{R_L} + \frac{V_{CC}}{R_L}$$

**Circuito AC (c):**

$$i_C = -\frac{v_{CE}}{R_L} + \frac{V_{CEQ}}{R_L} + I_{CQ}$$

### Eleccion del punto Q optimo

Las rectas de carga (CC y CA) intersectan con la curva $P_{CE\,MAX}$ en dos puntos Q posibles. Se elige el punto $Q_1$ (menor $I_C$, mayor $V_{CE}$) porque implica:
- Menor corriente de colector
- Menor distorsion
- Menor corriente de base requerida

Para que la realizacion sea factible: $V_{CE1} < V_{CEO}$, tomando $V_{CE1} = V_{CC}$.

### Punto Q para maxima excursion simetrica

$$I_{CQ} = \frac{I_{C\,Max}}{2} = \frac{V_{CC}}{2R_L}$$

$$V_{CEQ} = \frac{V_{CE\,Max}}{2} = \frac{V_{CC}}{2}$$

La recta de carga de CA tiene la **misma pendiente** que la recta de carga de CC (porque $R_E = 0$ y la carga es la misma en DC y AC).

### Formas de onda

- $i_C$: oscila entre 0 y $I_{C\,Max}$, con valor medio $I_{CQ} = V_{CC}/2R_L$
- $v_{CE}$: oscila entre 0 y $V_{CE\,Max}$, con valor medio $V_{CEQ} = V_{CC}/2$
- $p_{CC} = V_{CC} \cdot i_C$: tiene la misma forma que $i_C$
- $p_{CE} = i_C \cdot v_{CE}$: tiene frecuencia **el doble** de las otras formas de onda

## Determinacion de la eficiencia

### Potencia en la carga

$$P_L = I_{C_{rms}}^2 R_L$$

Considerando que la corriente tiene componente DC y AC ($I_{CQ}$ e $I_{CQ}/\sqrt{2}$):

$$P_L = \left[\sqrt{I_{CQ}^2 + \left(\frac{I_{CQ}}{\sqrt{2}}\right)^2}\right]^2 R_L = I_{CQ}^2 R_L + \frac{I_{CQ}^2}{2} R_L$$

Sustituyendo $I_{CQ} = V_{CC}/2R_L$:

$$\boxed{P_L = \underbrace{\frac{V_{CC}^2}{4R_L}}_{P_{L(CC)}} + \underbrace{\frac{V_{CC}^2}{8R_L}}_{P_{L(CA)}}}$$

### Potencia de la fuente

$$P_{CC} = V_{CC} I_{CQ} = \frac{V_{CC}^2}{2R_L}$$

### Potencia disipada en el transistor

$$P_{CE} = P_{CC} - P_L = \frac{V_{CC}^2}{2R_L} - \left(\frac{V_{CC}^2}{4R_L} + \frac{V_{CC}^2}{8R_L}\right) = \frac{V_{CC}^2}{4R_L} - \frac{V_{CC}^2}{8R_L}$$

$$P_{CE} = \frac{V_{CC}^2}{8R_L}$$

### Eficiencia

$$\boxed{\eta = \frac{P_{L(CA)}}{P_{CC}} = \frac{V_{CC}^2 / 8R_L}{V_{CC}^2 / 2R_L} = 0.25 = 25\%}$$

> [!warning] Baja eficiencia
> La eficiencia del amplificador clase A con acoplo directo es solo **25%**. Esto se debe principalmente a que se mantiene una corriente de reposo $I_{CQ}$ en la carga, la cual es desperdiciada (no contribuye a la senal).

## Resumen de potencias - Clase A acoplo directo

> [!abstract] Tabla de potencias
>
> | Potencia | Formula | Proporcion |
> | -------- | ------- | ---------- |
> | $P_{L(CA)}$ (senal en carga) | $\dfrac{V_{CC}^2}{8R_L}$ | $1\times$ |
> | $P_{CE}$ (disipada en transistor) | $\dfrac{V_{CC}^2}{8R_L}$ | $1\times$ |
> | $P_{L(DC)}$ (DC en carga) | $\dfrac{V_{CC}^2}{4R_L}$ | $2\times$ |
> | $P_{CC}$ (fuente) | $\dfrac{V_{CC}^2}{2R_L}$ | $4\times$ |

## Bibliografia

- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson.
