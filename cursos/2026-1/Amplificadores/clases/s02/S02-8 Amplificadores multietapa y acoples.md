---
title: "Amplificadores multietapa y acoples entre etapas"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 2
orden: 8
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/amplificador-multietapa
  - tema/acople-capacitivo
  - tema/acople-directo
  - tema/acople-por-transformador
date: 2026-04-07
---

## Concepto

Un amplificador multietapa es la **conexion en cascada de dos o mas etapas amplificadoras**, donde la salida de una alimenta la entrada de la siguiente. Se usa porque un solo transistor rara vez proporciona la ganancia suficiente de voltaje, corriente o potencia.

## Ganancia total

$$\boxed{A_{V\,total} = A_{V1} \cdot A_{V2} \cdot A_{V3} \cdots A_{Vn}}$$

En decibeles:

$$A_{V\,total\,(dB)} = A_{V1\,(dB)} + A_{V2\,(dB)} + \cdots + A_{Vn\,(dB)}$$

Cada etapa cumple un rol distinto:
- **Primera etapa:** alta ganancia de voltaje
- **Etapas intermedias:** ganancia adicional o adaptacion de impedancia
- **Etapa final:** potencia (clase A, B o AB) para excitar la carga

---

## Tipos de acople entre etapas

### 1. Acople por condensador (RC)

El condensador de acople bloquea la componente DC entre etapas y solo deja pasar la senal AC.

**Ventajas:**
- **Aisla los puntos Q** — cada etapa se polariza independientemente
- Diseno sencillo y economico
- Muy utilizado en audio y frecuencias medias

**Desventajas:**
- No funciona en DC ni a frecuencias muy bajas
- Introduce una **frecuencia de corte inferior**: $f_L = \dfrac{1}{2\pi RC}$
- No es integrable en circuitos integrados (los condensadores grandes ocupan mucho area en silicio)

> [!tip] ¿Por que separar DC de AC?
> Sin condensador, la tension DC de salida de la primera etapa ($V_{CEQ}$) se suma a la polarizacion de la siguiente. Por ejemplo, si $V_{CEQ1} = 5\,V$ entra directo a la base de Q2 (que necesita $\approx 0.7\,V$), Q2 se **satura** y deja de amplificar. El condensador bloquea esos $5\,V$ DC y deja pasar solo la senal AC, permitiendo que cada etapa defina su propio punto Q con su propia red de polarizacion.

---

### 2. Acople directo (DC)

La salida de una etapa se conecta directamente a la entrada de la siguiente, sin ningun elemento de bloqueo.

**Ventajas:**
- Respuesta desde **DC hasta alta frecuencia** (sin frecuencia de corte inferior)
- **Ideal para circuitos integrados** — no requiere condensadores ni transformadores
- Usado en amplificadores operacionales y amplificadores diferenciales

**Desventajas:**
- Los **puntos Q estan acoplados** — un cambio en la polarizacion de una etapa afecta a todas las siguientes
- Sensible a **derivas termicas** que se propagan y amplifican etapa a etapa
- Requiere tecnicas sofisticadas de estabilizacion (realimentacion negativa, pares diferenciales)

---

### 3. Acople por transformador

Se usa un transformador entre etapas para transferir la senal y adaptar impedancias.

**Ventajas:**
- **Adaptacion de impedancia** con la relacion de vueltas $a = N_1/N_2$
- **Maxima transferencia de potencia** entre etapas
- Aislamiento galvanico (aislamiento electrico) entre etapas

**Desventajas:**
- Voluminoso, pesado y costoso
- **No integrable** en circuitos integrados
- Respuesta en frecuencia limitada por inductancias de dispersion y capacitancias parasitas
- Introduce **distorsion** si el nucleo se satura

---

## Resumen comparativo

| Caracteristica | Condensador (RC) | Directo (DC) | Transformador |
| -------------- | ---------------- | ------------ | ------------- |
| Respuesta en DC | No | **Si** | No |
| Aislamiento de punto Q | **Si** | No | **Si** |
| Adaptacion de impedancia | No | No | **Si** |
| Integrable en CI | No | **Si** | No |
| Costo/tamano | Bajo | **Minimo** | Alto |
| Uso tipico | Audio, frecuencias medias | Op-amps, CI | Etapas de potencia, RF |

## Bibliografia

- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson.
