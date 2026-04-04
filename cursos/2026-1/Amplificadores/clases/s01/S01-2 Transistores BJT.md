---
title: "Transistores BJT"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 1
orden: 2
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/transistor-bjt
  - tema/polarizacion
date: 2026-03-31
---

## Transistor de union bipolar (BJT)

El BJT (transistor de union bipolar) se construye con **tres regiones semiconductoras** separadas por dos uniones PN. Las tres regiones se llaman **emisor**, **base** y **colector**.

### Tipos de BJT

- **NPN:** Se compone de dos regiones N separadas por una region P.
- **PNP:** Se compone de dos regiones P separadas por una region N.

Cada tipo tiene tres terminales:
- **Colector (C)**
- **Base (B)**
- **Emisor (E)**

### Encapsulados comunes

Transistores de senal pequena para proposito general:

| Encapsulado | Tipo |
| ----------- | ---- |
| TO-92 | Senal pequena, 3 pines (E, B, C) |
| SOT-23 | Montaje superficial, 3 pines |
| TO-18 | Metalico, emisor mas cercano a la pestana |
| TO-220 | Potencia media (B, C, E) |
| TO-225 | Potencia media (E, C, B) |
| D-Pack | Montaje superficial potencia (B, E, C) |
| TO-3 | Alta potencia, carcasa metalica = colector |

Encapsulados multiples (varios transistores):
- **DIP / Quad flat-pack:** El punto indica el pin 1
- **Quad small outline (SO):** Para tecnologia de montaje superficial

## Polarizacion del transistor BJT

El transistor es un dispositivo semiconductor que permite el **control y regulacion de una corriente grande mediante una senal muy pequena**.

### NPN

- $I_B$ entra por la base
- $I_C$ entra por el colector
- $I_E$ sale por el emisor
- Voltajes: $V_{BE}$ (base-emisor, $+/-$), $V_{CE}$ (colector-emisor, $+/-$)

### PNP

- $I_B$ sale por la base
- $I_C$ sale por el colector
- $I_E$ entra por el emisor
- Voltajes: $V_{EB}$ (emisor-base, $+/-$), $V_{EC}$ (emisor-colector, $+/-$)

## Prueba de transistores BJT

Se utiliza un multimetro en modo de prueba de diodo ($\Omega$) para verificar las uniones del transistor.

### Prueba de la union Base-Emisor (BE)

| Polarizacion | Resultado esperado |
| ------------ | ------------------ |
| Directa (punta $+$ en B, $-$ en E) | Lectura de ~0.70 V (baja resistencia) |
| Inversa (punta $+$ en E, $-$ en B) | OL - circuito abierto (alta resistencia) |

### Prueba de la union Base-Colector (BC)

| Polarizacion | Resultado esperado |
| ------------ | ------------------ |
| Directa (punta $+$ en B, $-$ en C) | Lectura de ~0.70 V (baja resistencia) |
| Inversa (punta $+$ en C, $-$ en B) | OL - circuito abierto (alta resistencia) |

> [!tip] Criterio de prueba
> Un transistor en buen estado se comporta como dos diodos: la union BE y la union BC deben conducir en directa (~0.7 V) y bloquear en inversa (OL).

## Configuraciones del transistor BJT

### Emisor comun

- Terminal de entrada: Base
- Terminal de salida: Colector
- Terminal comun: Emisor

Se utiliza como **amplificador de voltaje y corriente** a bajas frecuencias.

### Colector comun (Seguidor de Emisor)

- Terminal de entrada: Base
- Terminal de salida: Emisor
- Terminal comun: Colector

Se utiliza para **transferir una tension** de un primer circuito con alta impedancia de salida a un segundo circuito con baja impedancia de entrada.

### Base comun

- Terminal de entrada: Emisor
- Terminal de salida: Colector
- Terminal comun: Base

Se aplica en **frecuencias muy altas**, presenta una respuesta excelente a altas frecuencias.

## Curva caracteristica de entrada del BJT

Para que un BJT opere adecuadamente como amplificador, las dos uniones PN deben estar correctamente polarizadas con voltajes de CD externos.

En la configuracion emisor comun:
- La **union BE** se polariza en **directa** ($V_{BE} = 0.7\,V$)
- La **union BC** se polariza en **inversa**

La curva de entrada grafica $I_B$ ($\mu A$) vs $V_{BE}$ (V) para distintos valores de $V_{CE}$. Se observa que la curva tiene un comportamiento similar al de un diodo, con conduccion significativa a partir de ~0.6-0.7 V.

### Analisis de la malla de entrada

Como el emisor esta conectado a tierra (0V), por la ley de Kirchhoff el voltaje a traves de $R_B$ es:

$$V_{R_B} = V_{BB} - V_{BE}$$

Por la ley de Ohm:

$$V_{R_B} = I_B R_B$$

Aplicando mallas en la entrada:

$$-V_{BB} + I_B R_B + V_{BE} = 0$$

Despejando $I_B$:

$$\boxed{I_B = \frac{V_{BB} - V_{BE}}{R_B}}$$

Donde:
- $I_B$ = corriente de base
- $V_{BB}$ = voltaje de la fuente de base
- $V_{BE}$ = voltaje base-emisor ($\approx 0.7\,V$)
- $R_B$ = resistencia de base

## Curva caracteristica de salida del BJT

### Analisis de la malla de salida

Caida de tension a traves de $R_C$:

$$V_{R_C} = I_C R_C$$

Aplicando mallas en la salida del colector-emisor:

$$-V_{CC} + I_C R_C + V_{CE} = 0$$

El voltaje en el colector con respecto al emisor:

$$\boxed{V_{CE} = V_{CC} - I_C R_C}$$

Donde:

$$I_C = \beta I_B$$

- $I_C$ = corriente de colector
- $\beta$ = ganancia de corriente del transistor
- $V_{CC}$ = voltaje de la fuente de colector
- $R_C$ = resistencia de colector

El voltaje a traves de la union colector-base polarizada en inversa es:

$$V_{CB} = V_{CE} - V_{BE}$$

### Curva $I_C$ vs $V_{CE}$

La curva de salida grafica $I_C$ contra $V_{CE}$ para distintos valores de $I_B$. Se identifican tres regiones de operacion.

## Regiones de operacion del BJT

### Region de saturacion

- Las uniones BE y BC se polarizan en **directa**
- Se emplea al transistor como un **interruptor cerrado** (corto circuito)

$$I_C = I_{C(sat)} = I_{C(max)}$$

$$V_{CE} = V_{CE(sat)} \approx 0.2\,V$$

### Region de corte

- Las uniones BE y BC se polarizan en **inversa**
- Existe una cantidad muy pequena de corriente de fuga en el colector, $I_{CE}$
- Corresponde al **interruptor abierto** (circuito abierto)

$$V_{CE} = V_{CC}$$

$$I_B = 0\,A$$

### Region activa

- La union BE se polariza en **directa**
- La union BC se polariza en **inversa**
- El transistor entra a la **region lineal** o *activa* de operacion
- Se emplea para **amplificar** voltaje, corriente o potencia
- $I_C$ se incrementa muy poco a medida de $V_{CE}$ se incrementa

$$V_{CE} > 0.7\,V$$

$$I_C = \beta I_B$$

> [!abstract] Resumen de regiones
>
> | Region | Union BE | Union BC | Funcion |
> | ------ | -------- | -------- | ------- |
> | Saturacion | Directa | Directa | Interruptor cerrado |
> | Corte | Inversa | Inversa | Interruptor abierto |
> | Activa | Directa | Inversa | Amplificacion |
