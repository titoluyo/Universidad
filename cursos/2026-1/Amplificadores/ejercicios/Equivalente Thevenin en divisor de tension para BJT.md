---
title: "Equivalente Thevenin en divisor de tension para BJT"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 1
tipo: ejercicio
tags:
  - curso/amplificadores
  - tipo/ejercicio
  - tema/thevenin
  - tema/polarizacion
  - tema/divisor-de-tension
  - tema/transistor-bjt
date: 2026-04-19
---

## Objetivo

Aplicar el **teorema de Thevenin** a la malla de entrada de un amplificador BJT polarizado por **divisor de tension** para reducir las dos resistencias de base ($R_1$ y $R_2$) a una sola fuente $V_{TH}$ en serie con una sola resistencia $R_{TH}$. Esto simplifica el analisis DC a una unica ecuacion para $I_B$.

Ver tambien: [[S01-2 Transistores BJT]].

## Circuito original

```
        V_CC
         │
     ┌───┴───┐
     │       │
     R1      R_C
     │       │
     ├───────┤── Colector
     │    B  │
     │    ├──┤ BJT (β)
     R2   │  │
     │    E  │
     │       │
     │       R_E
     │       │
     └───┬───┘
         │
        GND
```

El nodo base es alimentado desde la union entre $R_1$ y $R_2$. El objetivo es reemplazar **todo lo que esta a la izquierda de la base** por su equivalente Thevenin.

## Procedimiento

### Paso 1 — Calcular $V_{TH}$

Se **desconecta** la base (circuito abierto) y se mide la tension entre ese nodo y tierra. Sin carga, $R_1$ y $R_2$ forman un divisor de tension puro:

$$
V_{TH} = V_{CC} \cdot \dfrac{R_2}{R_1 + R_2}
$$

Donde:
- $V_{TH}$ = tension equivalente que "ve" la base
- $V_{CC}$ = fuente de alimentacion DC
- $R_2$ = resistencia inferior (conectada a GND)
- $R_1$ = resistencia superior (conectada a $V_{CC}$)

> [!tip] Intuicion
> $V_{TH}$ es la tension que tendria la base **si el transistor no estuviera conectado**. Por eso tambien se le llama *tension en circuito abierto*.

### Paso 2 — Calcular $R_{TH}$

Se **apagan las fuentes independientes** ($V_{CC}$ se reemplaza por un corto a tierra) y se mira la resistencia desde el nodo de la base hacia adentro.

Al cortocircuitar $V_{CC}$:
- $R_1$ queda entre la base y tierra (porque $V_{CC}$ ahora es GND)
- $R_2$ ya estaba entre la base y tierra

Ambas quedan **en paralelo**:

$$
R_{TH} = R_1 \parallel R_2 = \dfrac{R_1 \cdot R_2}{R_1 + R_2}
$$

### Paso 3 — Circuito equivalente y ecuacion de malla

Tras aplicar Thevenin, la malla de entrada queda reducida a una sola rama:

$$
V_{TH} \;\longrightarrow\; R_{TH} \;\longrightarrow\; B \;\longrightarrow\; V_{BE} \;\longrightarrow\; E \;\longrightarrow\; R_E \;\longrightarrow\; GND
$$

Aplicando **LKV** (ley de Kirchhoff de tensiones) en la malla base–emisor y usando $I_E = (\beta + 1) \, I_B$:

$$
V_{TH} = I_B \cdot R_{TH} + V_{BE} + (\beta + 1) \cdot I_B \cdot R_E
$$

Despejando $I_B$:

$$
\boxed{\, I_B = \dfrac{V_{TH} - V_{BE}}{R_{TH} + (\beta + 1)\, R_E} \,}
$$

Con $I_B$ se obtiene luego $I_C = \beta \, I_B$ y el resto del punto de operacion Q.

## Ejemplo resuelto

### Enunciado

Para el amplificador BJT con polarizacion por divisor de tension, determinar $V_{TH}$, $R_{TH}$, $I_B$ e $I_C$.

### Datos

| Parametro | Valor |
| --------- | ----- |
| $V_{CC}$ | $12\text{ V}$ |
| $R_1$ | $47\text{ k}\Omega$ |
| $R_2$ | $10\text{ k}\Omega$ |
| $R_E$ | $1\text{ k}\Omega$ |
| $\beta$ | $100$ |
| $V_{BE}$ | $0.7\text{ V}$ |

### Solucion

**Tension de Thevenin:**

$$
V_{TH} = 12 \cdot \dfrac{10}{47 + 10} = 12 \cdot 0.1754 \approx 2.11\text{ V}
$$

**Resistencia de Thevenin:**

$$
R_{TH} = \dfrac{47 \cdot 10}{47 + 10} = \dfrac{470}{57} \approx 8.25\text{ k}\Omega
$$

**Corriente de base:**

$$
I_B = \dfrac{V_{TH} - V_{BE}}{R_{TH} + (\beta + 1)\, R_E} = \dfrac{2.11 - 0.7}{8.25\text{ k}\Omega + 101 \cdot 1\text{ k}\Omega} = \dfrac{1.41}{109.25\text{ k}\Omega} \approx 12.9\text{ }\mu\text{A}
$$

**Corriente de colector:**

$$
I_C = \beta \cdot I_B = 100 \cdot 12.9\text{ }\mu\text{A} \approx 1.29\text{ mA}
$$

### Respuesta

| Magnitud | Valor |
| -------- | ----- |
| $V_{TH}$ | $2.11\text{ V}$ |
| $R_{TH}$ | $8.25\text{ k}\Omega$ |
| $I_B$ | $12.9\text{ }\mu\text{A}$ |
| $I_C$ | $1.29\text{ mA}$ |

## Condicion de diseno estable

Para que el punto Q sea **insensible a las variaciones de $\beta$** (que cambia con la temperatura y entre unidades), se busca que la caida de tension en $R_{TH}$ sea despreciable frente a la caida en $(\beta + 1) R_E$:

$$
R_{TH} \ll (\beta + 1)\, R_E
$$

Regla practica usual:

$$
R_{TH} \leq \dfrac{1}{10}\, \beta\, R_E
$$

> [!warning] Caso ideal
> Si se cumple la condicion, $\beta$ desaparece de la ecuacion y $I_C$ queda aproximadamente como:
>
> $$ I_C \approx \dfrac{V_{TH} - V_{BE}}{R_E} $$
>
> lo que hace al circuito robusto ante reemplazos del transistor o cambios termicos.

**Verificacion en el ejemplo:**
- $R_{TH} = 8.25\text{ k}\Omega$
- $\dfrac{1}{10}\, \beta \, R_E = \dfrac{1}{10} \cdot 100 \cdot 1\text{ k}\Omega = 10\text{ k}\Omega$
- $8.25\text{ k}\Omega < 10\text{ k}\Omega$ ✓ diseno estable

## Bibliografia

- Boylestad, R. & Nashelsky, L. (2009). *Electronica: teoria de circuitos y dispositivos electronicos* (10ma ed.). Pearson.
- Sedra, A. & Smith, K. (2015). *Microelectronic Circuits* (7ma ed.). Oxford University Press.
