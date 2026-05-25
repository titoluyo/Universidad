---
title: Ejercicio resuelto - Ensayos de vacío y cortocircuito del transformador
curso: "[[Motores MOC]]"
unidad: 2
semana: 7
orden: 4
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/ensayo-vacio
  - tema/ensayo-cortocircuito
  - tema/parametros-transformador
  - tema/corriente-falta
  - tema/tension-cortocircuito-porcentual
date: 2026-05-04
---

> [!info] Fuente
> Video "Desarrollo de un ejercicio de ensayo de vacío y de cortocircuito de un transformador real" (Semana 07, Tema 02). Transcripción completa en [[#Guion del video|el Guion]] adjunto al final.

## Enunciado

Un transformador monofásico de **250 kVA**, con una relación de **15 000 V / 250 V** y frecuencia **60 Hz**, ha dado los siguientes resultados en los ensayos:

| Ensayo | Tensión | Corriente | Potencia | Lado medido |
| ------ | ------- | --------- | -------- | ----------- |
| **Vacío** | 250 V | 80 A | 4 000 W | Baja tensión (secundario) |
| **Cortocircuito** | 600 V | $I_{1n}$ (a calcular) | 5 000 W | Alta tensión (primario) |

Se pide calcular:
- **a)** Los **parámetros del circuito equivalente** del transformador **reducido al primario**.
- **b)** La **corriente de cortocircuito de falta**.

## Datos

| Magnitud | Símbolo | Valor |
| -------- | ------- | ----- |
| Potencia aparente nominal | $S_n$ | 250 kVA |
| Tensión primaria nominal | $V_{1n}$ | 15 000 V |
| Tensión secundaria nominal | $V_{2n}$ | 250 V |
| Frecuencia | $f$ | 60 Hz |
| Ensayo vacío (BT) — tensión | $V_{20}$ | 250 V |
| Ensayo vacío (BT) — corriente | $I_{02}$ | 80 A |
| Ensayo vacío — potencia | $P_0$ | 4 000 W |
| Ensayo cortocircuito (AT) — tensión | $V_{1cc}$ | 600 V |
| Ensayo cortocircuito — potencia | $P_{cc}$ | 5 000 W |

## Desarrollo

### Relación de transformación

$$a = \frac{V_{1n}}{V_{2n}} = \frac{15\,000}{250}$$

$$\boxed{a = 60}$$

### Corriente nominal del primario

$$I_{1n} = \frac{S_n}{V_{1n}} = \frac{250\,000}{15\,000}$$

$$\boxed{I_{1n} \approx 16{,}67\,\text{A}}$$

### a) Parámetros del circuito equivalente reducido al primario

#### Ensayo de vacío — Rama paralela

El ensayo de vacío se realizó en el lado de **baja tensión** (secundario), por lo que hay que **reducir las medidas al primario** antes de calcular los parámetros:

$$V_1 = a \cdot V_{20} = 60 \cdot 250 = 15\,000\,\text{V} \approx V_{1n}$$

$$I_0 = \frac{I_{02}}{a} = \frac{80}{60} \approx 1{,}33\,\text{A}$$

La potencia $P_0 = 4\,000\,\text{W}$ se conserva al reducir (la potencia activa es independiente del lado).

**Factor de potencia en vacío** (ver [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real#Factor de potencia en vacío|teoría]]):

$$\cos\varphi_0 = \frac{P_0}{V_1 \cdot I_0} = \frac{4\,000}{15\,000 \cdot 1{,}33} = \frac{4\,000}{20\,000}$$

$$\boxed{\cos\varphi_0 = 0{,}2}$$

$$\sin\varphi_0 = \sqrt{1 - 0{,}2^2} = \sqrt{0{,}96} \approx 0{,}98$$

**Componentes de la corriente de vacío:**

$$I_{Fe} = I_0 \cos\varphi_0 = 1{,}33 \cdot 0{,}2 \approx 0{,}267\,\text{A}$$

$$I_\mu = I_0 \sin\varphi_0 = 1{,}33 \cdot 0{,}98 \approx 1{,}307\,\text{A}$$

**Resistencia de pérdidas en el hierro:**

$$R_{Fe} = \frac{V_1}{I_{Fe}} = \frac{15\,000}{0{,}267}$$

$$\boxed{R_{Fe} \approx 56{,}25\,\text{k}\Omega \;\;(\approx 56{,}4\,\text{k}\Omega \text{ en el video})}$$

**Reactancia magnetizante:**

$$X_\mu = \frac{V_1}{I_\mu} = \frac{15\,000}{1{,}307}$$

$$\boxed{X_\mu \approx 11{,}5\,\text{k}\Omega}$$

#### Ensayo de cortocircuito — Rama serie

Los datos del ensayo de cortocircuito **ya están en el lado primario**, por lo que se aplican directamente.

**Factor de potencia en cortocircuito:**

$$\cos\varphi_{cc} = \frac{P_{cc}}{V_{1cc} \cdot I_{1n}} = \frac{5\,000}{600 \cdot 16{,}67} = \frac{5\,000}{10\,000}$$

$$\boxed{\cos\varphi_{cc} = 0{,}5}$$

$$\sin\varphi_{cc} = \sqrt{1 - 0{,}5^2} = \sqrt{0{,}75} \approx 0{,}866$$

**Resistencia de cortocircuito:**

$$R_{cc} = \frac{V_{1cc} \cdot \cos\varphi_{cc}}{I_{1n}} = \frac{600 \cdot 0{,}5}{16{,}67}$$

$$\boxed{R_{cc} = 18\,\Omega}$$

**Reactancia de cortocircuito:**

$$X_{cc} = \frac{V_{1cc} \cdot \sin\varphi_{cc}}{I_{1n}} = \frac{600 \cdot 0{,}866}{16{,}67}$$

$$\boxed{X_{cc} \approx 31{,}2\,\Omega}$$

> [!note] Magnitud de los parámetros
> Como esperábamos por la [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real|teoría]], los valores de la **rama serie** ($R_{cc} = 18\,\Omega$, $X_{cc} = 31{,}2\,\Omega$) son **muy pequeños** comparados con los de la **rama paralela** ($R_{Fe} = 56{,}25\,\text{k}\Omega$, $X_\mu = 11{,}5\,\text{k}\Omega$). Es lo que justifica el uso del circuito equivalente aproximado.

### Tensión relativa de cortocircuito

$$\varepsilon_{cc} = \frac{V_{1cc}}{V_{1n}} \cdot 100 = \frac{600}{15\,000} \cdot 100$$

$$\boxed{\varepsilon_{cc} = 4\,\%}$$

> Valor típico para un transformador de distribución (rango 1 %–6 %).

### b) Corriente de cortocircuito de falta

#### En el primario

A falta de un cortocircuito accidental en el transformador (secundario en cortocircuito con $V_{1n}$ aplicada al primario):

$$I_{1falta} = \frac{100}{\varepsilon_{cc}} \cdot I_{1n} = \frac{100}{4} \cdot 16{,}67$$

$$\boxed{I_{1falta} \approx 416{,}75\,\text{A}}$$

#### En el secundario

Primero la corriente nominal del secundario:

$$I_{2n} = \frac{S_n}{V_{2n}} = \frac{250\,000}{250} = 1\,000\,\text{A}$$

Y la corriente de falta del secundario:

$$I_{2falta} = \frac{100}{\varepsilon_{cc}} \cdot I_{2n} = 25 \cdot 1\,000$$

$$\boxed{I_{2falta} = 25\,000\,\text{A} = 25\,\text{kA}}$$

> [!warning] Magnitud de la corriente de falta
> $I_{2falta} = 25\,\text{kA}$ es **25 veces** la corriente nominal del secundario. Esta corriente es **altamente peligrosa** para la integridad de la máquina por sus efectos térmicos y electrodinámicos. De ahí la importancia de los **dispositivos de protección** (fusibles, interruptores) dimensionados para cortar el cortocircuito antes de que cause daño irreversible.

## Resumen de resultados

| Parámetro | Valor |
| --------- | ----- |
| Relación de transformación $a$ | $60$ |
| Corriente nominal primario $I_{1n}$ | $16{,}67\,\text{A}$ |
| Corriente nominal secundario $I_{2n}$ | $1\,000\,\text{A}$ |
| $\cos\varphi_0$ (vacío) | $0{,}2$ |
| $R_{Fe}$ | $56{,}25\,\text{k}\Omega$ |
| $X_\mu$ | $11{,}5\,\text{k}\Omega$ |
| $\cos\varphi_{cc}$ | $0{,}5$ |
| $R_{cc}$ | $18\,\Omega$ |
| $X_{cc}$ | $31{,}2\,\Omega$ |
| Tensión relativa $\varepsilon_{cc}$ | $4\,\%$ |
| $I_{1falta}$ | $\approx 417\,\text{A}$ |
| $I_{2falta}$ | $25\,\text{kA}$ |

## Guion del video

![[s07-t02-ej-guion-ensayos-trafo.pdf]]

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
