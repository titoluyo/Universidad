---
title: Informe LE1 - Amplificador operacional (inversor y no inversor)
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 6
orden: 100
tipo: evaluacion
subtipo: laboratorio
tags:
  - curso/amplificadores
  - tipo/evaluacion
  - subtipo/laboratorio
  - tema/laboratorio
  - tema/informe
  - tema/opamp
  - tema/amplificador-inversor
  - tema/amplificador-no-inversor
  - tema/lm741
date: 2026-04-27
---

> [!info] Documentos relacionados
> - [[S06-99 Laboratorio - LE1 Amplificador operacional|S06-99 Guía del laboratorio]]
> - [[S06-1 Amplificadores lineales y no lineales|S06-1 Aplicaciones lineales y no lineales]] (teoría)
> - [[Formulario - Amplificadores|Formulario]]
> - Documento Word original: `Informe LE1 - Amplificador operacional.docx`

> [!example] Datos del entregable
> - **Curso:** Circuitos Electrónicos Amplificadores
> - **Docente:** Jorge Luis Robles Bokun
> - **Ciclo:** 2026-1 — Semana 6
> - **Modalidad:** Grupal
>
> **Integrantes:**
> - Ludeña Muñante, Harold — U23319438
> - Espinoza Abarca, Pedro Rodrigo — U18216101
> - Rojas Novoa, Ernesto Raúl — U21227968
> - Carlos Baldeón Hidalgo
> - Luyo Murata, Tito Takeo — U23210744

---

## 1. Materiales y equipos utilizados

| Categoría | Elemento |
| --------- | -------- |
| Componente activo | Circuito integrado **LM741** |
| Componentes pasivos | Resistores de $2\,\text{k}\Omega$, $2.2\,\text{k}\Omega$, $5.6\,\text{k}\Omega$ y $10\,\text{k}\Omega$ |
| Soporte | Protoboard |
| Cableado | Cables macho-macho |
| Equipos | Generador de funciones, multímetro digital CD 771, osciloscopio digital |

---

## 2. Desarrollo 1 — Amplificador inversor

### 2.1. Descripción

Amplificador operacional cuya **señal de entrada** se aplica a la terminal **inversora** del OPAMP, mientras que la terminal **no inversora** se conecta a tierra. La salida es una señal **amplificada e invertida** (desfasada $180°$) respecto de la entrada.

![[s06-le1-inversor-diagrama.png]]
*Configuración del amplificador inversor.*

### 2.2. Configuración y deducción de la ganancia

Para un OPAMP ideal, partiendo de:

$$V_o = A_v \cdot (V^+ - V^-)$$

Como $A_v \to \infty$ (ganancia en lazo abierto extremadamente grande), la diferencia de potencial entre entradas tiende a cero (**tierra virtual** en la entrada inversora). Aplicando KCL al nodo inversor:

$$\frac{V_i - 0}{R_1} = \frac{0 - V_o}{R_2}$$

De donde se obtiene la ganancia de la configuración inversora:

$$\boxed{A_v = -\frac{R_2}{R_1}}$$

### 2.3. Procedimiento aplicado

**Pasos ejecutados:**

1. Montaje del amplificador inversor utilizando $R_1 = 2\,\text{k}\Omega$ y $R_2 = 10\,\text{k}\Omega$.
2. Calibración de la fuente para alimentar el OPAMP con $+12\,\text{V}$ y $-12\,\text{V}$.
3. Generación de la señal de entrada: senoidal de $5\,\text{kHz}$ y $1\,\text{Vpp}$ desde el generador de funciones.
4. Visualización con osciloscopio: CH1 → entrada, CH2 → salida.

### 2.4. Implementación en protoboard

**Montaje del circuito:**

![[s06-le1-inversor-protoboard.png]]
*Montaje físico del amplificador inversor en protoboard.*

**Calibración de la fuente bipolar $\pm12\,\text{V}$:**

| Rama positiva | Rama negativa |
| ------------- | ------------- |
| ![[s06-le1-fuente-12v-pos.jpg]] | ![[s06-le1-fuente-12v-neg.jpg]] |
| Fuente a $+12\,\text{V}$ | Fuente a $-12\,\text{V}$ |

**Capturas del osciloscopio:**

![[s06-le1-inversor-osc-1.jpg]]

![[s06-le1-inversor-osc-2.jpg]]

![[s06-le1-inversor-osc-3.jpg]]

![[s06-le1-inversor-osc-4.jpg]]

### 2.5. Cálculos

Con $R_1 = 2\,\text{k}\Omega$ y $R_2 = 10\,\text{k}\Omega$:

$$A_v = -\frac{R_2}{R_1} = -\frac{10\,\text{k}\Omega}{2\,\text{k}\Omega} = -5$$

Tensión de salida pico-pico para $V_i = 1\,\text{Vpp}$:

$$V_o = A_v \cdot V_i = -5 \times 1\,\text{Vpp} = -5\,\text{Vpp}$$

$$\boxed{A_{v,\text{inv}} = -5 \quad ; \quad V_{o,\text{pp}} = 5\,\text{Vpp \;(invertida)}}$$

---

## 3. Desarrollo 2 — Amplificador no inversor

### 3.1. Descripción

Configuración con la señal de entrada conectada a la terminal **no inversora**, lo que hace que la ganancia sea **positiva** (señal de salida en fase con la entrada). La realimentación es negativa (a través de $R_2$ a la entrada inversora). La ganancia siempre es **mayor que 1**.

![[s06-le1-no-inversor-diagrama.png]]
*Configuración del amplificador no inversor.*

### 3.2. Ecuación de la ganancia

Aplicando el principio de tierra virtual y KCL en la entrada inversora:

$$\boxed{A_v = 1 + \frac{R_2}{R_1}} \quad\Longrightarrow\quad V_o = \left(1 + \frac{R_2}{R_1}\right) V_i$$

### 3.3. Procedimiento aplicado

**Pasos ejecutados:**

1. Montaje del amplificador no inversor utilizando $R_1 = 2.2\,\text{k}\Omega$ y $R_2 = 5.6\,\text{k}\Omega$.
2. Calibración de la fuente: $\pm12\,\text{V}$ para el OPAMP.
3. Generación de señal: senoidal de $5\,\text{kHz}$ y $1\,\text{Vpp}$.
4. Osciloscopio: CH1 → entrada, CH2 → salida.

### 3.4. Implementación en protoboard

![[s06-le1-no-inversor-osc-1.jpg]]

![[s06-le1-no-inversor-osc-2.jpg]]

![[s06-le1-no-inversor-osc-3.jpg]]

![[s06-le1-no-inversor-osc-4.jpg]]

### 3.5. Cálculos

Con $R_1 = 2.2\,\text{k}\Omega$ y $R_2 = 5.6\,\text{k}\Omega$:

$$A_v = 1 + \frac{R_2}{R_1} = 1 + \frac{5.6\,\text{k}\Omega}{2.2\,\text{k}\Omega} = 1 + 2{,}545 = 3{,}545$$

Tensión de salida para $V_i = 1\,\text{Vpp}$:

$$V_o = 3{,}545 \times 1\,\text{Vpp} = 3{,}545\,\text{Vpp}$$

$$\boxed{A_{v,\text{noinv}} \approx 3{,}545 \quad ; \quad V_{o,\text{pp}} \approx 3{,}545\,\text{Vpp \;(en fase)}}$$

---

## 4. Simulación en Multisim Live

### 4.1. Caso 1 — Amplificador inversor

![[s06-le1-multisim-inversor.jpg]]
*Simulación en Multisim Live: amplificador inversor con $R_1 = 2\,\text{k}\Omega$, $R_2 = 10\,\text{k}\Omega$.*

### 4.2. Caso 2 — Amplificador no inversor

![[s06-le1-multisim-no-inversor.jpg]]
*Simulación en Multisim Live: amplificador no inversor con $R_1 = 2.2\,\text{k}\Omega$, $R_2 = 5.6\,\text{k}\Omega$.*

---

## 5. Observaciones

- Durante el armado del circuito en protoboard se verificó que una **mala conexión o falso contacto** generaba ruido en la señal de salida, lo que obligó a revisar cuidadosamente el cableado.
- En el amplificador inversor se observó claramente que la señal de salida estaba **desfasada $180°$** respecto a la señal de entrada, tal como predice la teoría.
- El uso del osciloscopio permitió visualizar con claridad las formas de onda y comparar simultáneamente las señales de entrada y salida.
- Al aumentar la amplitud de la señal de entrada, la salida podía presentar **distorsión** al acercarse a los límites de alimentación del OPAMP (saturación a $\pm V_{cc}$).

---

## 6. Conclusiones

- Durante la práctica se comprobó en condiciones reales cómo responde un amplificador operacional en configuraciones básicas, observándose un comportamiento **consistente con lo esperado teóricamente** para señales de pequeña amplitud.
- El uso del osciloscopio fue clave para visualizar los cambios de **amplitud y fase**, permitiendo contrastar de forma directa lo calculado con lo medido sobre el circuito armado.
- La ganancia obtenida en ambos circuitos no es arbitraria, sino que depende directamente de la **relación entre las resistencias** ($R_2/R_1$), lo cual permite controlar la amplificación variando los valores de los componentes externos.
- El amplificador operacional resulta una herramienta muy versátil dentro de la electrónica: con configuraciones simples (inversor / no inversor) permite obtener distintos comportamientos útiles en aplicaciones reales.

---

## 7. Resumen de resultados

| Configuración | $R_1$ | $R_2$ | $A_v$ teórico | $V_i$ | $V_o$ esperado | Fase |
| ------------- | ----- | ----- | ------------- | ----- | -------------- | ---- |
| Inversor      | $2\,\text{k}\Omega$   | $10\,\text{k}\Omega$  | $-5$    | $1\,\text{Vpp}$ | $5\,\text{Vpp}$       | $180°$ |
| No inversor   | $2.2\,\text{k}\Omega$ | $5.6\,\text{k}\Omega$ | $3{,}545$ | $1\,\text{Vpp}$ | $3{,}545\,\text{Vpp}$ | $0°$  |

---

## Bibliografía

- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*. Pearson.
- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press.
- Coughlin, R. F. & Driscoll, F. F. *Amplificadores operacionales y circuitos integrados lineales*. Prentice Hall.
