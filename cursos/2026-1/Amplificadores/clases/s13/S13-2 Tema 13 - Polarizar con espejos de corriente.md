---
title: "Polarizar con espejos de corriente"
curso: "[[Amplificadores MOC]]"
unidad: 2
semana: 13
orden: 2
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/espejo-de-corriente
  - tema/polarizacion
  - tema/fuente-de-corriente
  - tema/carga-activa
  - tema/par-diferencial
date: 2026-06-15
---

## Contexto

**Polarizar** un amplificador es fijar su punto de operación en DC (las corrientes y tensiones de reposo) para que cada transistor trabaje en la región activa. En circuitos integrados, esa polarización **no** se hace con redes de resistencias por etapa —como en los circuitos discretos— sino con **espejos de corriente**: se genera **una sola** corriente de referencia y se "espeja" (copia, escalada) hacia todas las etapas que la necesitan.

Esta nota continúa [[S13-1 Tema 13 - Que son los espejos de corriente|qué son los espejos de corriente]] y muestra **cómo se usan para polarizar**.

> [!info] Toma de notas en clase
> Semana 13 — Sesión 25. De "qué es un espejo" a "para qué sirve": distribución de una referencia única, escalado por relación de áreas/tamaños, la fuente de cola del par diferencial y el espejo como carga activa.

---

## 1. El problema: polarizar con resistencias no escala

En un circuito discreto cada etapa se polariza con su propio divisor de tensión y resistencias de emisor. En un **chip** eso es inviable:

- Las resistencias **ocupan mucha área** y son **imprecisas** (tolerancias grandes, derivan con la temperatura).
- El punto de operación quedaría a merced de $\beta$, de $V_{BE}$ y de la temperatura, todos mal controlados en valor absoluto.

> [!tip] La solución
> Generar **una** corriente de referencia bien definida y **copiarla** a cada etapa con espejos. Lo que está bien controlado en un IC no es el valor absoluto de un componente, sino el **apareamiento** (matching) entre transistores vecinos. El espejo convierte ese apareamiento en corrientes de bias precisas y repetibles.

## 2. Una referencia, muchas salidas

El transistor diodo-conectado de la referencia fija un $V_{BE}$ común. Si conectamos la **base** de varios transistores de salida a ese mismo nodo, **todos** copian la corriente: una sola referencia polariza muchas etapas a la vez.

```
            V_CC
             │
             R                I_O1     I_O2     I_O3
             │                 ↑        ↑        ↑
   I_REF →   ├────────┬────────┼────────┼────────┤   (bases unidas)
             │        │        │        │        │
            ┌┴┐      ┌┴┐      ┌┴┐      ┌┴┐      ┌┴┐
            │Q0│     │Q1│     │Q2│     │Q3│     │Q4│
            └┬┘      └┬┘      └┬┘      └┬┘      └┬┘
          (diodo)    │        │        │        │
            └────────┴────────┴────────┴───────┴──── GND
```

- $Q_0$ = transistor de referencia (diodo-conectado), por él pasa $I_{REF}$.
- $Q_1\ldots Q_n$ = espejos de salida, cada uno entrega su corriente de bias a una etapa.

> [!note] Por eso se llama "banco de corriente" (*current bias network*)
> Una única $I_{REF}$ se reparte por todo el amplificador. Cambiar $R$ (o la referencia) reajusta **todas** las corrientes de bias de forma proporcional.

## 3. Escalado por relación de áreas / tamaños

Las salidas no tienen por qué ser iguales a $I_{REF}$: copiando con transistores de **distinto tamaño** se obtienen **múltiplos** de la referencia. El factor es la relación de áreas (BJT) o de $W/L$ (MOSFET):

$$\boxed{\,I_O = m\,I_{REF}, \qquad m = \dfrac{(\text{área o } W/L)_{\text{salida}}}{(\text{área o } W/L)_{\text{referencia}}}\,}$$

- $I_O$ = corriente de salida espejada
- $I_{REF}$ = corriente de referencia
- $m$ = factor de escala (relación de tamaños)

En BJT, poner $m$ transistores idénticos **en paralelo** equivale a un transistor de área $m$ veces mayor, que conduce $m\,I_{REF}$. En MOSFET basta diseñar el ancho $W$ adecuado.

> [!example] Ejemplo de distribución
> Con $I_{REF}=100\ \mu A$:
> - $m=1 \Rightarrow I_O = 100\ \mu A$
> - $m=2 \Rightarrow I_O = 200\ \mu A$
> - $m=0.5 \Rightarrow I_O = 50\ \mu A$
> - $m=4 \Rightarrow I_O = 400\ \mu A$ (p. ej. la cola de un par diferencial)
>
> Todas a partir de **una sola** $R$ y un solo $I_{REF}$.

## 4. La referencia $I_{REF}$

La forma más simple es una resistencia desde $V_{CC}$ al transistor diodo-conectado:

$$\boxed{\,I_{REF} = \dfrac{V_{CC} - V_{BE}}{R}\,}$$

(en MOSFET, $V_{BE}\to V_{GS}$). Su inconveniente es que **depende de $V_{CC}$**: si la alimentación varía, toda la polarización se mueve. Por eso en diseños buenos se reemplaza por una **fuente independiente de polarización** (referencia que no depende de $V_{CC}$, basada p. ej. en $V_{BE}$ o en bandgap), tema de las notas siguientes.

## 5. Caso típico: fuente de cola del par diferencial

El **par diferencial** necesita una corriente de cola $I_{COLA}$ constante en su nodo común de emisores (o fuentes). Una resistencia haría esa corriente sensible al modo común; en su lugar se usa **la salida de un espejo**:

```
        +V_CC
       ┌──┴──┐
      Q_A   Q_B        ← par diferencial
       └──┬──┘
          │  I_COLA  (constante, fijada por el espejo)
        ┌─┴─┐
        │Q_x│ ← salida del espejo (m·I_REF)
        └─┬─┘
         GND
```

> [!note] Por qué mejora el rechazo de modo común (CMRR)
> Una fuente de corriente ideal tiene resistencia de salida $r_o$ enorme. Cuanto mayor es $r_o$ en la cola, mejor se rechazan las señales de **modo común**: el par "ve" una corriente fija sin importar el nivel común de entrada. Por eso el espejo (alta $r_o$) es muy superior a una resistencia de cola.

## 6. El espejo también es la carga (carga activa)

Polarizar con espejos y **amplificar** con espejos van de la mano. Si la resistencia de colector $R_C$ se sustituye por la salida de un espejo, esa **carga activa** aporta una resistencia $r_o$ altísima, y la ganancia de la etapa crece:

$$A_v \approx -g_m \,(r_{o,\text{amp}} \parallel r_{o,\text{carga}})$$

- $g_m$ = transconductancia del transistor amplificador
- $r_{o,\text{amp}}$, $r_{o,\text{carga}}$ = resistencias de salida del transistor y de la carga activa

> [!tip] Doble papel del espejo
> En un amplificador integrado el mismo bloque **polariza** (fija las corrientes de reposo) y sirve de **carga activa** (maximiza la ganancia). Ambas cosas dependen de la alta $r_o$ del espejo.

---

## 7. Gráfica

Distribución de polarización: una referencia única de $100\ \mu A$ genera varias corrientes de bias escaladas por la relación de tamaños $m$ de cada transistor de salida. La barra gris es la rama de referencia; las azules, las etapas polarizadas.

![[polarizacion_espejos.png]]

> [!example] Verificación numérica
> La cola del par diferencial ($m=4$) recibe $I_O = m\,I_{REF} = 4 \times 100\ \mu A = 400\ \mu A$, mientras que con una sola $R$ y un solo $I_{REF}$ las demás etapas quedan en $100$, $200$ y $50\ \mu A$ — exactamente lo que muestran las barras.

Script: [`plot_polarizacion_espejos.py`](plot_polarizacion_espejos.py) — ejecutar con `uv run --with matplotlib --with numpy python plot_polarizacion_espejos.py`.

---

## Bibliografía

- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press — fuentes de corriente, espejos y polarización de circuitos integrados.
- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*. Pearson.
- Jaeger, R. & Blalock, T. *Microelectronic Circuit Design*. McGraw-Hill.
