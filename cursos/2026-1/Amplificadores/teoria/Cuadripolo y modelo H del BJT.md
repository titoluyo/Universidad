---
title: "Cuadripolo y modelo H del BJT"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 1
tipo: referencia
tags:
  - curso/amplificadores
  - tipo/referencia
  - tema/cuadripolo
  - tema/modelo-h
  - tema/parametros-hibridos
  - tema/transistor-bjt
date: 2026-04-19
---

## ¿Que es un cuadripolo?

Un **cuadripolo** (o red de dos puertos) es cualquier circuito con **dos pares de terminales**: uno de entrada (puerto 1) y uno de salida (puerto 2). Se describe completamente con 4 variables: dos tensiones ($V_1, V_2$) y dos corrientes ($I_1, I_2$).

```
     I1 →                    ← I2
     ┌──────────────────────────┐
 + ──┤                          ├── +
V1   │        CUADRIPOLO        │   V2
 − ──┤                          ├── −
     └──────────────────────────┘
   Puerto 1                  Puerto 2
   (entrada)                 (salida)
```

De las 4 variables, **2 son independientes y 2 dependientes**. Segun que par se tome como independiente, se obtienen distintos modelos: **Z** (impedancia), **Y** (admitancia), **ABCD** (transmision) y **H** (hibrido).

El modelo **H** es el que mejor se ajusta al BJT porque:

- En la **entrada** el BJT se comporta como **resistencia** (la corriente controla la tension)
- En la **salida** se comporta como **fuente de corriente** (la tension influye poco en la corriente)

Por eso se llama "hibrido": mezcla unidades de ohms, siemens y magnitudes adimensionales.

## Modelo H completo

Tomando $I_1$ y $V_2$ como variables independientes, el sistema general es:

$$
V_1 = h_{11} \cdot I_1 + h_{12} \cdot V_2
$$

$$
I_2 = h_{21} \cdot I_1 + h_{22} \cdot V_2
$$

Para un BJT en **emisor comun** (los subindices llevan "**e**" de *emitter*), se renombran los 4 parametros:

| Parametro | Nombre | Significado | Unidad |
| --------- | ------ | ----------- | ------ |
| $h_{ie}$ | *input* | Resistencia de entrada (salida en corto) | $\Omega$ |
| $h_{re}$ | *reverse* | Ganancia inversa de tension (entrada abierta) | adimensional |
| $h_{fe}$ | *forward* | Ganancia de corriente directa (salida en corto) | adimensional |
| $h_{oe}$ | *output* | Admitancia de salida (entrada abierta) | $S$ (siemens) |

Las ecuaciones del BJT en pequena senal quedan:

$$
v_{be} = h_{ie} \cdot i_b + h_{re} \cdot v_{ce}
$$

$$
i_c = h_{fe} \cdot i_b + h_{oe} \cdot v_{ce}
$$

> [!note] Mnemotecnico
> $h_{\mathbf{i}e}$ = **i**nput, $h_{\mathbf{r}e}$ = **r**everse, $h_{\mathbf{f}e}$ = **f**orward, $h_{\mathbf{o}e}$ = **o**utput. El **segundo subindice** indica la configuracion: **e** = emisor comun, **b** = base comun, **c** = colector comun.

## $h_{re}$ — ganancia inversa de tension

**Definicion formal:**

$$
h_{re} = \left. \dfrac{v_{be}}{v_{ce}} \right|_{i_b = 0}
$$

Es decir: **con la entrada en circuito abierto** ($i_b = 0$), que fraccion de la tension de salida $v_{ce}$ "aparece reflejada" en la entrada $v_{be}$.

- **Fisicamente** modela el efecto de la tension colector–emisor sobre la union base–emisor (es el **efecto Early** reflejado hacia la entrada).
- **Valor tipico:** $h_{re} \approx 10^{-4}$ — muy pequeno.
- **Interpretacion:** un cambio de $1\text{ V}$ en la salida produce solo $\approx 0.1\text{ mV}$ en la entrada → practicamente despreciable.

## $h_{oe}$ — admitancia de salida

**Definicion formal:**

$$
h_{oe} = \left. \dfrac{i_c}{v_{ce}} \right|_{i_b = 0}
$$

Es decir: **con la entrada en circuito abierto**, cuanta corriente de colector varia cuando cambia $v_{ce}$.

- **Fisicamente** es la inversa de la **resistencia de salida** del transistor:

$$
r_o = \dfrac{1}{h_{oe}}
$$

- Modela que la curva $I_C$ vs $V_{CE}$ **no es perfectamente horizontal** (pendiente pequena debida al efecto Early).
- **Valor tipico:** $h_{oe} \approx 10\text{ }\mu\text{S}$ → $r_o \approx 100\text{ k}\Omega$.
- **Interpretacion:** la salida se comporta casi como **fuente de corriente ideal** (resistencia muy alta).

## Modelo H simplificado

Como $h_{re}$ y $h_{oe}$ son muy pequenos en la mayoria de los BJT de senal pequena, en los analisis practicos se **desprecian**:

$$
h_{re} \approx 0 \qquad h_{oe} \approx 0
$$

Esto reduce las ecuaciones a:

$$
\boxed{\, v_{be} = h_{ie} \cdot i_b \,} \qquad \boxed{\, i_c = h_{fe} \cdot i_b \,}
$$

Y el circuito equivalente AC del BJT queda:

```
     B  ┌──── h_ie ────┐  ┌─────────── C
  i_b → │              │  │
 v_be   │              │  ↓ h_fe · i_b   (fuente de
        │              │  │               corriente)
        └──────────────┴──┴─────────── E
```

Solo queda:

- Una **resistencia $h_{ie}$** en la entrada
- Una **fuente de corriente dependiente $h_{fe} \cdot i_b$** en la salida

> [!tip] Por que se permite la simplificacion
> - Despreciar $h_{re}$ significa asumir que la salida **no influye** en la entrada (sin realimentacion interna del transistor).
> - Despreciar $h_{oe}$ significa asumir que la salida es una **fuente de corriente ideal** (resistencia de salida infinita).
>
> El error introducido es tipicamente $<5\%$, muy aceptable para calculos de diseno.

> [!warning] Cuando SI considerar $h_{re}$ y $h_{oe}$
> - Cuando el **$R_C$ es muy grande** (del orden de $r_o$ o mayor), $h_{oe}$ deja de ser despreciable.
> - Cuando se analiza **realimentacion interna** o se disena con alta precision.
> - En amplificadores de alta ganancia donde pequenos errores se acumulan.

## Relacion con otros modelos

| Parametro H | Equivalente en modelo $\pi$-hibrido |
| ----------- | ----------------------------------- |
| $h_{fe}$ | $\beta$ (AC) |
| $h_{ie}$ | $\beta \cdot r_e$, donde $r_e = V_T / I_E \approx 25\text{ mV}/I_E$ |
| $1/h_{oe}$ | $r_o$ (resistencia de salida) |
| $h_{re}$ | $v_{be}/v_{ce}$ (usualmente no tiene simbolo dedicado en $\pi$-hibrido) |

## Variantes segun configuracion

El segundo subindice cambia segun la configuracion del BJT:

| Configuracion | Subindices | Uso tipico |
| ------------- | ---------- | ---------- |
| Emisor comun (CE) | $h_{ie}, h_{re}, h_{fe}, h_{oe}$ | Mayor ganancia de tension y corriente |
| Base comun (CB) | $h_{ib}, h_{rb}, h_{fb}, h_{ob}$ | Alta frecuencia, baja impedancia de entrada |
| Colector comun (CC) | $h_{ic}, h_{rc}, h_{fc}, h_{oc}$ | Seguidor de emisor, adaptador de impedancia |

## Bibliografia

- Boylestad, R. & Nashelsky, L. (2009). *Electronica: teoria de circuitos y dispositivos electronicos* (10ma ed.). Pearson.
- Sedra, A. & Smith, K. (2015). *Microelectronic Circuits* (7ma ed.). Oxford University Press.
- Malvino, A. & Bates, D. (2016). *Principios de electronica* (8va ed.). McGraw-Hill.
