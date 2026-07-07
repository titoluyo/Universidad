---
title: Laboratorio LE2 - Realimentación negativa (amplificador transresistencia, BJT 2N2222)
curso: "[[Amplificadores MOC]]"
unidad: 3
semana: 9
orden: 99
tipo: evaluacion
subtipo: laboratorio
tags:
  - curso/amplificadores
  - tipo/evaluacion
  - subtipo/laboratorio
  - tema/laboratorio
  - tema/realimentacion-negativa
  - tema/realimentacion-shunt-shunt
  - tema/transresistencia
  - tema/impedancia-de-entrada
  - tema/respuesta-en-frecuencia
  - tema/2n2222
date: 2026-05-18
---

> [!info] Datos del laboratorio
> - **Tipo:** Laboratorio de Electrónica General — Guía Nº 2 (LE2 / LABELEGE01)
> - **Tema:** Realimentación negativa
> - **Curso:** Circuitos Electrónicos Amplificadores
> - **Ambiente:** Laboratorio de Electrónica General
> - **Código:** 100000I21N
> - **Versión:** 005 (aprobada 24/10/2025)
> - **Elaborado por:** Alberto Alvarado · **Aprobado por:** DDA Ingenierías Electrónicas
> - **Guía PDF (páginas):** [[guia2-P01.png]] … [[guia2-P06.png]] (carpeta [`guia/`](guia/))

---

## 1. Logro general de la unidad de aprendizaje

Al finalizar la unidad, el estudiante analiza las topologías de realimentación en los amplificadores y de los circuitos osciladores, y las diferentes configuraciones de los reguladores en casos prácticos.

## 2. Objetivos específicos de la práctica

Al final del laboratorio, el estudiante analiza e implementa el funcionamiento de los circuitos electrónicos con realimentación negativa.

---

## 3. Materiales y equipos

### Equipos del laboratorio

- Generador de funciones 220 V
- Multímetro digital CD 771
- Protoboard 1660 puntos
- Osciloscopio digital
- Fuente de alimentación 2231A 30 V 3 A
- Transistor **2N2222A**
- Resistencias 1/2 W: **100 Ω, 220 Ω, 1 kΩ, 10 kΩ**
- Condensador electrolítico **10 µF / 25 V**
- Cables de hilo de cobre para protoboard (macho-macho, macho-hembra, hembra-hembra)

### Materiales que trae el alumno

- Resistencia **5.6 kΩ — 1/2 W**

> [!note] Componentes vs. lista
> El circuito usa además **RE = 100 Ω**, **RC = 1 kΩ**, **R1 = R2 = 10 kΩ**, **R3 = R4 = 5.6 kΩ** y tres condensadores de **10 µF** (C1, C2, C3). La resistencia de **220 Ω** aparece en la lista de equipos pero no se usa en el esquema de esta guía.

---

## 4. Pautas de seguridad

### 4.1. Recomendaciones de seguridad

- a. El laboratorio cuenta con señaléticas de prohibiciones, seguridad y emergencias, los cuales deben ser respetados.
- b. Es responsabilidad del alumno o grupo de trabajo mantener el orden y limpieza.
- c. Todos los equipos deben ser maniobrados bajo la estricta supervisión del docente del curso.
- d. Todo el grupo de trabajo es responsable por la rotura y/o deterioro del material entregado y/o equipos del laboratorio durante el desarrollo de las prácticas.

### 4.2. Uso de EPP

- a. Guardapolvo.

---

## 5. Fundamento

La realimentación en general es un proceso que consiste en la transferencia de energía presente en la salida de un sistema a la entrada del mismo (o a otras entradas internas o subsiguientes). En el caso de los circuitos electrónicos, consiste en tomar parte o toda la salida de corriente o tensión que hay en la salida y llevarla a la entrada.

Este proceso puede realizarse de una manera externa o producirse por efectos internos de los dispositivos y componentes empleados en el circuito, como por ejemplo las capacidades parásitas. Es un proceso tan fundamental en los circuitos electrónicos, como lo son la amplificación y la rectificación. Además de estar presente en muchísimos circuitos, es la base del funcionamiento de los sistemas que emplean **amplificadores operacionales**.

> [!tip] Referencia teórica del curso
> La teoría de soporte está en [[S08-1 Material 1|las notas de la semana 8]] sobre topologías, configuraciones y parámetros de la realimentación, y en [[S09-1 Amplificadores con realimentacion positiva y osciladores]] para el contraste con la realimentación positiva.

---

## 6. Procedimiento (desarrollo de la práctica)

### 6.1. Circuito a ensamblar

![[guia2-circuito.png]]
*Amplificador en emisor común con BJT 2N2222 y red de realimentación R3–R4 de colector a base. La entrada es la corriente $I_g$ (tras C1); la salida $V_o$ se toma en el colector. El interruptor S1 (con C2) conecta el punto medio de R3–R4 a tierra de señal.*

**Valores del circuito:**

| Componente | Valor | Función |
| ---------- | ----- | ------- |
| $V_{CC}$   | +12 V | Alimentación |
| $R_C$      | 1 kΩ  | Resistencia de colector (carga) |
| $R_E$      | 100 Ω | Resistencia de emisor (puenteada en AC por $C_3$) |
| $R_1$      | 10 kΩ | Resistencia de acoplamiento de entrada (define $I_g$) |
| $R_2$      | 10 kΩ | Resistencia de base a tierra |
| $R_3,\,R_4$ | 5.6 kΩ c/u | Red de realimentación colector→base ($R_f = R_3+R_4 = 11.2\,\text{k}\Omega$) |
| $C_1,\,C_2,\,C_3$ | 10 µF | Acoplo de entrada / desacople del punto medio / puente de emisor |
| $Q_1$      | 2N2222 | Transistor amplificador |

### 6.2. Mediciones en DC

1. Con **S1 abierto**, medir las tensiones en todos los nudos del circuito (puntos de operación: $V_B$, $V_E$, $V_C$).
2. Aplicar la señal de entrada $V_g$ con amplitud **200 mV pico-pico** y frecuencia **1 kHz**.

### 6.3. Mediciones de realimentación

A continuación, comparar el circuito **con** y **sin** realimentación conmutando S1:

- **a)** Con **S1 abierto**, medir la transresistencia y la impedancia de entrada.
- **b)** Con **S1 cerrado**, medir la transresistencia y la impedancia de entrada.

Definiciones que da la guía:

- **c)** La transresistencia se define como: $\;R_{mf} = \dfrac{V_o}{I_g}$
- **d)** La impedancia de entrada se halla con: $\;Z_{if} = \dfrac{V_g}{I_g}$

3. **¿Cómo hará la medición de $I_g$?** — La corriente de entrada circula por $R_1$. Con $C_1$ comportándose como cortocircuito a la frecuencia de trabajo, $I_g = \dfrac{V_g - V_i}{R_1}$, donde $V_i$ es la tensión en el nudo de base (medida sobre $R_2$). Es decir, basta medir la caída en $R_1$ y dividir entre $R_1$.

   Para cada uno de los pasos **3a** y **3b**, medir la **respuesta en frecuencia** del circuito y la **impedancia de entrada** barriendo las frecuencias de la tabla.

4. **Recomendación:** Hacer sólo las mediciones de tensión y dejar los cálculos para el informe.

### 6.4. Tabla de toma de datos (respuesta en frecuencia)

| Paso  | Magnitud | 20 | 100 | 200 | 1K | 2K | 5K | 10K | 20K | 50K | 70K | 100K | 150K |
| ----- | -------- | -- | --- | --- | -- | -- | -- | --- | --- | --- | --- | ---- | ---- |
| 3a    | $R_m$    |    |     |     |    |    |    |     |     |     |     |      |      |
| 3a    | $Z_i$    |    |     |     |    |    |    |     |     |     |     |      |      |
| 3b    | $R_{mf}$ |    |     |     |    |    |    |     |     |     |     |      |      |
| 3b    | $Z_{if}$ |    |     |     |    |    |    |     |     |     |     |      |      |

*Frecuencias de barrido en Hz. $R_m,\,Z_i$ = sin subíndice; $R_{mf},\,Z_{if}$ = con realimentación (subíndice $f$).*

---

## 7. Entregables

> [!important] Entregables exigidos por la guía
> 1. Hacer una **tabla comparando los valores teóricos con los experimentales**.
> 2. Indicar la **forma de realimentación** que se ha hecho en el paso 3 del experimento.
> 3. ¿Cuál es el **método empleado para medir la impedancia de entrada**? Explicar el fundamento teórico.
> 4. ¿Cómo haría la **medición de la impedancia de salida**?
> 5. Hacer el **gráfico de la respuesta en frecuencia de la transresistencia** para cada caso y explicar por qué tiene la forma medida.
> 6. Indicar **observaciones y conclusiones** del experimento.
> 7. Presentar el **informe completo la siguiente clase práctica**.

---

## 8. Fuentes de información complementaria

- Realimentación negativa — vídeo de YouTube: [https://www.youtube.com/watch?v=oxG2LapDq0M](https://www.youtube.com/watch?v=oxG2LapDq0M)

---

## Análisis para entender la guía

> [!abstract] Lectura de ingeniería (no está en la guía — es mi interpretación para trabajar después)

### Qué amplificador es

Es una etapa en **emisor común** (BJT 2N2222) convertida en **amplificador de transresistencia** por una red de realimentación. La señal de excitación se inyecta como **corriente** $I_g$ en el nudo de base y la salida útil es la **tensión** $V_o$ en el colector — por eso la figura de mérito es la **transresistencia** $R_m = V_o/I_g$ (unidades de ohmios).

### Topología de la realimentación

- Se **muestrea la tensión** de salida (en el colector) y se **devuelve corriente** al nudo de entrada (base) a través de $R_3+R_4$. Esto es **realimentación tensión-paralelo (shunt-shunt)**, que es la topología que estabiliza la **transresistencia**.
- Efectos esperados de la realimentación negativa shunt-shunt:
  - **Transresistencia** se reduce y se estabiliza: con ganancia de lazo alta, $R_{mf} \approx -(R_3+R_4) = -11.2\,\text{k}\Omega$ (fijada por la red, casi independiente del transistor).
  - **Impedancia de entrada** disminuye (la realimentación paralelo baja $Z_{in}$): $Z_{if} < Z_i$.
  - **Impedancia de salida** disminuye (muestreo de tensión).
  - **Ancho de banda** aumenta (la respuesta en frecuencia se aplana y el polo superior se corre a mayor frecuencia).

### Para qué sirve S1 (y por qué C2)

- **$C_2$ bloquea la DC** en el punto medio de R3–R4, así que **el punto de operación (bias) es el mismo** esté S1 abierto o cerrado. El bias es de tipo **realimentación de colector** ($R_3+R_4$ de colector a base, más $R_2$ a tierra).
- **S1 abierto** → el punto medio queda flotante → $R_3+R_4$ forman un camino continuo colector→base → **realimentación negativa ACTIVA** (lazo cerrado).
- **S1 cerrado** → el punto medio queda a **tierra de señal** (vía $C_2$) → se rompe el camino de realimentación; $R_4$ pasa a ser carga adicional de colector ($R_C \parallel R_4$) y $R_3$ una carga en paralelo a la entrada → **SIN realimentación** (lazo abierto efectivo).

> [!warning] Inconsistencia de etiquetas a confirmar
> Físicamente, **S1 abierto = con realimentación** ($R_{mf}, Z_{if}$) y **S1 cerrado = sin realimentación** ($R_m, Z_i$). Pero la guía lista en la sección de mediciones "a) S1 abierto" y "b) S1 cerrado", mientras que la tabla rotula "3a → $R_m, Z_i$" (sin subíndice) y "3b → $R_{mf}, Z_{if}$" (con subíndice). El orden a)/b) y 3a/3b **queda cruzado** respecto a la convención de subíndices. Antes de tabular conviene fijar la correspondencia:
> - **Sin realimentación** ($R_m, Z_i$) → **S1 cerrado**
> - **Con realimentación** ($R_{mf}, Z_{if}$) → **S1 abierto**
>
> (A verificar con el docente o por medición; la física respalda este mapeo.)

### Cómo se medirá cada cosa (resumen operativo)

| Magnitud | Fórmula | Cómo medir |
| -------- | ------- | ---------- |
| $I_g$    | $(V_g - V_i)/R_1$ | Tensión a ambos lados de $R_1$ (osciloscopio), dividir entre 10 kΩ |
| $R_m$ / $R_{mf}$ | $V_o/I_g$ | Medir $V_o$ en colector y $I_g$ |
| $Z_i$ / $Z_{if}$ | $V_g/I_g$ | Medir $V_g$ del generador y $I_g$ |
| $Z_{out}$ | (entregable 4) | Método de la tensión en vacío vs. con carga, o inyección de señal en la salida |

---

## Bibliografía

- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*. Pearson. (Cap. realimentación)
- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press. (Cap. *Feedback* — topología shunt-shunt / transresistance)
