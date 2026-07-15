---
title: Ejercicio resuelto - Parámetros del transformador trifásico
curso: "[[Motores MOC]]"
unidad: 2
semana: 9
orden: 2
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/transformador-trifasico
  - tema/conexion-YY
  - tema/conexion-dd
  - tema/conexion-Yd
  - tema/conexion-dY
  - tema/relacion-transformacion
date: 2026-05-18
---

> [!info] Fuente
> Video "Desarrollo de un ejercicio de transformador trifásico" (Semana 09, Tema 01). Transcripción completa en [[#Guion del video|el Guion]] adjunto al final.

## Enunciado

Se conecta un **transformador trifásico reductor** a una línea de **20 kV** y absorbe **20 A**. Si la **relación de espiras por fase** es igual a **100**, calcular la **tensión de línea** y la **corriente de línea** en el secundario para las siguientes conexiones:

- **Y–Y** (estrella–estrella)
- **Δ–Δ** (triángulo–triángulo)
- **Y–Δ** (estrella–triángulo)
- **Δ–Y** (triángulo–estrella)

> Para este ejercicio se **desprecian las pérdidas** del transformador (transformador ideal).

## Datos

| Magnitud | Símbolo | Valor |
| -------- | ------- | ----- |
| Tensión de línea primaria | $V_{LP}$ | 20 kV |
| Corriente de línea primaria | $I_{LP}$ | 20 A |
| Relación de espiras **por fase** | $a$ | 100 |

## Potencia total (igual para todas las conexiones)

En un sistema trifásico, la potencia aparente se calcula como:

$$S = \sqrt{3} \cdot V_{LP} \cdot I_{LP}$$

$$S = \sqrt{3} \cdot 20\,000 \cdot 20 = \sqrt{3} \cdot 400\,000$$

$$\boxed{S \approx 692{,}8\,\text{kVA}}$$

## Conexión 1: Y–Y

**Primario (Y):**
- Voltaje de fase: $V_{\phi P} = V_{LP}/\sqrt{3} = 20\,000/\sqrt{3} \approx 11\,547\,\text{V}$
- Corriente de fase: $I_{\phi P} = I_{LP} = 20\,\text{A}$

**Secundario (Y):** aplicando $a = V_{\phi P}/V_{\phi S}$:
- $V_{\phi S} = V_{\phi P}/a = 11\,547/100 \approx 115{,}47\,\text{V}$
- $V_{LS} = \sqrt{3} \cdot V_{\phi S} = \sqrt{3} \cdot 115{,}47$ → $\boxed{V_{LS} = 200\,\text{V}}$
- $I_{\phi S} = a \cdot I_{\phi P} = 100 \cdot 20 = 2\,000\,\text{A}$
- $I_{LS} = I_{\phi S}$ → $\boxed{I_{LS} = 2\,000\,\text{A}}$

> En Y–Y las corrientes de fase **coinciden con las de línea** en ambos lados.

## Conexión 2: Δ–Δ

**Primario (Δ):**
- Voltaje de fase: $V_{\phi P} = V_{LP} = 20\,000\,\text{V}$
- Corriente de fase: $I_{\phi P} = I_{LP}/\sqrt{3} = 20/\sqrt{3} \approx 11{,}547\,\text{A}$

**Secundario (Δ):**
- $V_{\phi S} = V_{\phi P}/a = 20\,000/100 = 200\,\text{V}$
- $V_{LS} = V_{\phi S}$ → $\boxed{V_{LS} = 200\,\text{V}}$
- $I_{\phi S} = a \cdot I_{\phi P} = 100 \cdot 11{,}547 \approx 1\,154{,}7\,\text{A}$
- $I_{LS} = \sqrt{3} \cdot I_{\phi S} = \sqrt{3} \cdot 1\,154{,}7$ → $\boxed{I_{LS} = 2\,000\,\text{A}}$

## Conexión 3: Y–Δ

**Primario (Y):**
- $V_{\phi P} = V_{LP}/\sqrt{3} \approx 11\,547\,\text{V}$
- $I_{\phi P} = I_{LP} = 20\,\text{A}$

**Secundario (Δ):**
- $V_{\phi S} = V_{\phi P}/a = 11\,547/100 \approx 115{,}47\,\text{V}$
- $V_{LS} = V_{\phi S}$ → $\boxed{V_{LS} \approx 115{,}47\,\text{V}}$
- $I_{\phi S} = a \cdot I_{\phi P} = 100 \cdot 20 = 2\,000\,\text{A}$
- $I_{LS} = \sqrt{3} \cdot I_{\phi S} = \sqrt{3} \cdot 2\,000$ → $\boxed{I_{LS} \approx 3\,464\,\text{A}}$

## Conexión 4: Δ–Y

**Primario (Δ):**
- $V_{\phi P} = V_{LP} = 20\,000\,\text{V}$
- $I_{\phi P} = I_{LP}/\sqrt{3} = 20/\sqrt{3} \approx 11{,}547\,\text{A}$

**Secundario (Y):**
- $V_{\phi S} = V_{\phi P}/a = 20\,000/100 = 200\,\text{V}$
- $V_{LS} = \sqrt{3} \cdot V_{\phi S} = \sqrt{3} \cdot 200$ → $\boxed{V_{LS} \approx 346{,}4\,\text{V}}$
- $I_{\phi S} = a \cdot I_{\phi P} = 100 \cdot 11{,}547 \approx 1\,154{,}7\,\text{A}$
- $I_{LS} = I_{\phi S}$ → $\boxed{I_{LS} \approx 1\,154{,}7\,\text{A}}$

## Resumen de resultados

| Conexión | $V_{LS}$ | $I_{LS}$ | $V_{LP}/V_{LS}$ |
| -------- | -------- | -------- | --------------- |
| **Y–Y**   | $200\,\text{V}$ | $2\,000\,\text{A}$ | $a = 100$ |
| **Δ–Δ**   | $200\,\text{V}$ | $2\,000\,\text{A}$ | $a = 100$ |
| **Y–Δ**   | $115{,}47\,\text{V}$ | $3\,464\,\text{A}$ | $\sqrt{3} \cdot a = 173{,}2$ |
| **Δ–Y**   | $346{,}4\,\text{V}$ | $1\,154{,}7\,\text{A}$ | $a/\sqrt{3} = 57{,}74$ |

> [!tip] Verificación
> Para cada conexión se debe cumplir $S = \sqrt{3} \cdot V_{LS} \cdot I_{LS} \approx 692{,}8\,\text{kVA}$ (transformador ideal). Compruébalo en los cuatro casos.

> [!note] Lectura
> Con la misma relación **por fase** $a = 100$, las cuatro conexiones entregan **distintos voltajes de línea** en el secundario. **Y–Δ es la conexión más reductora** (relación $\sqrt{3} \cdot a$) y **Δ–Y la menos reductora** (relación $a/\sqrt{3}$). Las conexiones de igual tipo (Y–Y, Δ–Δ) entregan el mismo voltaje, igual a $V_{LP}/a$.

## Guion del video

![[s09-t01-ej-guion-trafo-trifasico.pdf]]

## Bibliografía

- Chapman, S. J. (2005). *Máquinas Eléctricas* (4.ª ed.). McGraw-Hill Interamericana.
