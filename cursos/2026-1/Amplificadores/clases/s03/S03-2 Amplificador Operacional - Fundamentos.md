---
title: "Amplificador Operacional - Fundamentos"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 3
orden: 2
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/opamp
  - tema/amplificador-operacional
date: 2026-04-07
---

## ¿Que es un amplificador operacional?

El amplificador operacional (op-amp) es un **amplificador de voltaje diferencial de alta ganancia** con entrada diferencial y salida single-ended. Se llama "operacional" porque originalmente se diseño para realizar **operaciones matematicas** (suma, resta, integracion, derivacion) en computadoras analogicas.

> [!info] Componente fundamental
> El op-amp es el bloque de construccion mas importante de la electronica analogica moderna. Un solo circuito integrado como el LM741 contiene ~20 transistores, resistencias y capacitores internos.

## Simbolo y terminales

```
        V+
        |
  V1 (+)|\ 
        | \
        |  >---- Vo (salida)
        | /
  V2 (-)|/
        |
        V-
```

| Terminal | Nombre | Descripcion |
| -------- | ------ | ----------- |
| $V_1$ (+) | Entrada no inversora | La salida esta **en fase** con esta entrada |
| $V_2$ (-) | Entrada inversora | La salida esta en **contrafase** con esta entrada |
| $V_o$ | Salida | Voltaje amplificado |
| $V^+$ | Alimentacion positiva | Tipicamente +15V, +12V o +5V |
| $V^-$ | Alimentacion negativa | Tipicamente -15V, -12V o GND |

> [!warning] Signo + y - en las entradas
> Los signos (+) y (-) **no** indican polaridad de voltaje. Indican la **relacion de fase** con la salida. No confundir con las terminales de alimentacion $V^+$ y $V^-$.

## Estructura interna

Como se vio en [[S03-1 Amplificador diferencial con BJT PNP|la nota anterior]], el op-amp esta compuesto por tres etapas en cascada:

| Etapa | Funcion | Caracteristica clave |
| ----- | ------- | -------------------- |
| **Diferencial** (entrada) | Amplifica $V_1 - V_2$ | Alta $Z_{in}$, alto CMRR |
| **Ganancia** (intermedia) | Aumenta la ganancia total | Ganancia de voltaje muy alta |
| **Salida** (push-pull) | Entrega corriente a la carga | Baja $Z_{out}$ |

---

## Op-amp ideal vs real

### Caracteristicas del op-amp ideal

| Parametro | Valor ideal | Significado |
| --------- | ----------- | ----------- |
| Ganancia de lazo abierto $A_{OL}$ | $\infty$ | Amplifica cualquier diferencia infinitamente |
| Impedancia de entrada $Z_{in}$ | $\infty$ | No consume corriente de la fuente de senal |
| Impedancia de salida $Z_{out}$ | $0$ | Entrega cualquier corriente sin caida de voltaje |
| Ancho de banda $BW$ | $\infty$ | Funciona a cualquier frecuencia |
| $V_{offset}$ | $0$ | Si $V_1 = V_2$, entonces $V_o = 0$ exactamente |
| CMRR | $\infty$ | Rechaza completamente senales en modo comun |

### Valores tipicos reales (LM741)

| Parametro | Valor tipico |
| --------- | ------------ |
| $A_{OL}$ | $200{,}000$ ($106\,dB$) |
| $Z_{in}$ | $2\,M\Omega$ |
| $Z_{out}$ | $75\,\Omega$ |
| $BW$ (lazo abierto) | $\sim 5\,Hz$ (polo dominante) |
| GBW (producto ganancia-ancho de banda) | $1\,MHz$ |
| Slew rate | $0.5\,V/\mu s$ |
| $V_{offset}$ | $\pm 1\,mV$ |

---

## Ecuacion fundamental

La salida del op-amp es proporcional a la **diferencia** de las entradas:

$$\boxed{V_o = A_{OL}(V_1 - V_2)}$$

Donde:
- $V_o$ = voltaje de salida
- $A_{OL}$ = ganancia de lazo abierto (open loop)
- $V_1$ = voltaje en la entrada no inversora (+)
- $V_2$ = voltaje en la entrada inversora (-)

> [!tip] Consecuencia practica
> Como $A_{OL}$ es enorme (~$10^5$), basta una diferencia de **microvoltios** entre las entradas para que la salida se sature. Por eso el op-amp **casi nunca se usa en lazo abierto** para amplificacion lineal.

---

## Saturacion

La salida no puede exceder los voltajes de alimentacion:

$$V^- + V_{sat} \leq V_o \leq V^+ - V_{sat}$$

Donde $V_{sat} \approx 1\text{-}2\,V$ para op-amps convencionales (como el 741). En op-amps **rail-to-rail**, $V_{sat} \approx 0$.

```
Vo
 ^
 |         ___________  V+ - Vsat (saturacion positiva)
 |        /
 |       / ← pendiente = A_OL (muy grande)
 |      /
 |_____/______________ → Vd = V1 - V2
 |    /
 |   /
 |__/_______________   V- + Vsat (saturacion negativa)
```

---

## Reglas de analisis (op-amp ideal con realimentacion negativa)

Cuando el op-amp opera en **lazo cerrado** con realimentacion negativa, se aplican dos reglas fundamentales:

> [!success] Regla 1: Cortocircuito virtual
> $$V_1 = V_2$$
> La diferencia de voltaje entre las entradas es **cero** (porque $A_{OL} \to \infty$).

> [!success] Regla 2: Corriente de entrada cero
> $$I_+ = I_- = 0$$
> No entra corriente por ninguna terminal de entrada (porque $Z_{in} \to \infty$).

> [!warning] Condicion necesaria
> Estas reglas **solo son validas** cuando hay **realimentacion negativa** (la salida se conecta de vuelta a la entrada inversora). Sin realimentacion, el op-amp satura.

---

## Modos de operacion

| Modo | Realimentacion | Comportamiento | Aplicacion |
| ---- | -------------- | -------------- | ---------- |
| **Lazo abierto** | Ninguna | Saturacion (+/−) | Comparadores |
| **Lazo cerrado lineal** | Negativa | Amplificacion controlada | Amplificadores, filtros |
| **Lazo cerrado no lineal** | Positiva | Conmutacion, oscilacion | Schmitt trigger, osciladores |

---

## Alimentacion

### Fuente simetrica (dual supply)

```
     +Vcc (+15V)
       |
    [Op-Amp]
       |
     -Vcc (-15V)
```

- Permite senales positivas y negativas en la salida
- Uso tipico: circuitos de audio, instrumentacion

### Fuente simple (single supply)

```
     +Vcc (+5V)
       |
    [Op-Amp]
       |
      GND (0V)
```

- La salida solo puede ser positiva (entre GND y $V_{CC}$)
- Se debe **polarizar** la entrada a $V_{CC}/2$ para centrar la senal
- Uso tipico: circuitos digitales, microcontroladores

---

## Op-amps comunes

| Modelo | $A_{OL}$ (dB) | GBW | Slew Rate | Alimentacion | Nota |
| ------ | -------------- | --- | --------- | ------------ | ---- |
| LM741 | 106 | 1 MHz | 0.5 V/µs | ±15V | Clasico, educativo |
| LM358 | 100 | 1 MHz | 0.3 V/µs | 3-32V | Fuente simple, bajo costo |
| LM324 | 100 | 1 MHz | 0.5 V/µs | 3-32V | Cuadruple, entrada PNP |
| TL072 | 106 | 3 MHz | 13 V/µs | ±18V | JFET, alta $Z_{in}$ |
| OPA2134 | 120 | 8 MHz | 20 V/µs | ±18V | Audio de alta fidelidad |

## Bibliografia

- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson.
- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press.
