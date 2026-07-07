---
title: Laboratorio LE1 - Amplificador operacional (inversor y no inversor)
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 6
orden: 99
tipo: evaluacion
subtipo: laboratorio
tags:
  - curso/amplificadores
  - tipo/evaluacion
  - subtipo/laboratorio
  - tema/laboratorio
  - tema/opamp
  - tema/amplificador-inversor
  - tema/amplificador-no-inversor
  - tema/lm741
date: 2026-04-27
---

> [!info] Datos del laboratorio
> - **Tipo:** Laboratorio de Electrónica General — Guía Nº 1 (LE1)
> - **Tema:** Amplificador operacional (configuraciones inversor y no inversor)
> - **Curso:** Circuitos Electrónicos Amplificadores
> - **Ambiente:** Laboratorio de Electrónica General
> - **Código:** 100000I21N
> - **Versión:** 003 (aprobada 25/03/2025)
> - **Elaborado por:** Alberto Alvarado · **Aprobado por:** Alberto Duanee Alvarado Rivera
> - **Guía PDF:** `s06-laboratorio-le1-guia.pdf`
> - **Informe asociado:** [[S06-100 Informe LE1 - Amplificador operacional|S06-100 Informe LE1]]

---

## 1. Logro general de la unidad de aprendizaje

Al término del tema, los alumnos analizarán y diseñarán las diferentes clases de amplificadores, amplificadores diferenciales y operacionales en casos prácticos.

## 2. Objetivos específicos de la práctica

Al finalizar la práctica, el estudiante implementa circuitos amplificadores operacionales básicos en base a dispositivos y circuitos electrónicos mediante instrumentación electrónica.

---

## 3. Materiales y equipos

### Equipos del laboratorio

- Generador de funciones 220 V
- Multímetro digital CD 771
- Protoboard 1660 puntos (1 unidad)
- Osciloscopio digital
- Cable de hilo de cobre para protoboard macho-macho
- Cable de hilo de cobre para protoboard macho-hembra
- Cable de hilo de cobre para protoboard hembra-hembra
- Circuito integrado **LM741** (1 unidad)
- Fuente de alimentación 2231A 30 V 3 A (1 unidad)

### Materiales que trae el alumno

- Resistores de **10 kΩ, 2 kΩ, 2.2 kΩ, 5.6 kΩ** — todas de 1/2 W

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

Un **amplificador operacional** es técnicamente un amplificador electrónico, el cual activa su funcionamiento con corriente continua. Contiene una conexión de salida y dos conexiones de entrada. También se identifica a estos dispositivos con las siglas **OPAMP**, tomado del término en inglés *operational amplifier*. El diferencial de potencia de ambas entradas es considerablemente menor comparado con el de la salida.

![[s06-le1-opamp-pinout.png]]
*Símbolo del amplificador operacional: entrada no inversora (+), inversora (−), salida y alimentaciones $V^+$, $V^-$.*

### Parámetros del amplificador operacional

- **Impedancia de entrada:** resistencia entre las entradas del amplificador.
- **Impedancia de salida:** resistencia que se observa a la salida del amplificador.
- **Ganancia en lazo abierto** ($A_{ol}$): ganancia de tensión en ausencia de realimentación. Se expresa en V/V, V/mV o en dB.
- **Tensión en modo común** ($V_{cm}$): valor promedio de tensión aplicada a ambas entradas.
- **Tensión de desequilibrio (offset) de entrada** ($V_{io}$): diferencia de tensión entre entradas que hace que la salida sea cero voltios.
- **Corriente de desequilibrio de entrada** ($I_{io}$): diferencia de corriente entre las dos entradas que hace que la salida tome el valor cero.
- **Tensión de entrada diferencial** ($V_{id,max}$): mayor diferencia de tensión entre entradas que mantiene el dispositivo dentro de las especificaciones.
- **Corriente de polarización de entrada** ($I_B$): corriente media que circula por las entradas en ausencia de señal.
- **Rapidez de variación de tensión (slew rate, SR):** máxima variación de la tensión de salida respecto al tiempo, como respuesta a una tensión escalón. Se mide en V/µs o kV/µs. Está limitada por la compensación en frecuencia del amplificador.
- **Relación de Rechazo en Modo Común (RRMC / CMRR):** capacidad del amplificador de rechazar señales en modo común.

> [!tip] Referencia teórica
> Para el detalle teórico de configuraciones lineales, ver [[S04-1 Aplicaciones lineales del amplificador operacional]] y [[S06-1 Amplificadores lineales y no lineales]].

---

## 6. Procedimiento (desarrollo de la práctica)

### 6.1. Amplificador inversor

**Componentes:** $R_1 = 2\,\text{k}\Omega$, $R_2 = 10\,\text{k}\Omega$, LM741.

**Pasos:**

1. Realice el montaje del amplificador inversor según la figura, utilizando $R_1 = 2\,\text{k}\Omega$ y $R_2 = 10\,\text{k}\Omega$.
2. Calibre los voltajes del módulo para la alimentación del OPAMP: $+12\,\text{V}$ y $-12\,\text{V}$.
3. La señal de entrada se obtiene del generador de funciones (señal senoidal de **5 kHz** y **1 Vpp**). Para visualizar las señales se usa el osciloscopio:
   - **CH1** mide la onda de entrada del circuito.
   - **CH2** mide la onda de salida del circuito.

> [!warning] Conexión de tierras
> Las tierras del generador de señales, del osciloscopio y de la fuente de alimentación deben estar **unidas** para tener el mismo punto de referencia.

![[s06-le1-inversor-setup.png]]
*Esquema del amplificador inversor con $R_1 = 2\,\text{k}\Omega$, $R_2 = 10\,\text{k}\Omega$ y alimentación bipolar $\pm12\,\text{V}$. CH1 mide $V_{in}$, CH2 mide $V_{out}$.*

**Tareas a desarrollar:**

- Dibujar en el recuadro del informe las ondas de entrada y de salida (respetando escalas y posiciones de las flechas de referencia).
- **Calcular la ganancia del circuito** $G = -\dfrac{R_2}{R_1}$.
- Indicar **cómo se encuentran** las formas de onda de la entrada y la salida (relación de fase y amplitud).

### 6.2. Amplificador no inversor

**Componentes:** $R_1 = 2.2\,\text{k}\Omega$, $R_2 = 5.6\,\text{k}\Omega$, LM741.

**Pasos:**

1. Realice el montaje del amplificador no inversor según la figura, utilizando $R_1 = 2.2\,\text{k}\Omega$ y $R_2 = 5.6\,\text{k}\Omega$.
2. Calibre los voltajes del módulo para la alimentación del OPAMP: $+12\,\text{V}$ y $-12\,\text{V}$.
3. La señal de entrada se obtiene del generador de funciones (señal senoidal de **5 kHz** y **1 Vpp**). Para visualizar:
   - **CH1** mide la onda de entrada.
   - **CH2** mide la onda de salida.

> [!warning] Conexión de tierras
> Las tierras del generador, osciloscopio y fuente de alimentación deben estar unidas (mismo punto de referencia).

![[s06-le1-no-inversor-setup.png]]
*Esquema del amplificador no inversor con $R_1 = 2.2\,\text{k}\Omega$, $R_2 = 5.6\,\text{k}\Omega$ y alimentación bipolar $\pm12\,\text{V}$.*

**Tareas a desarrollar:**

- Dibujar en el recuadro las ondas de entrada y salida.
- **Calcular la ganancia** $G = 1 + \dfrac{R_2}{R_1}$.
- Indicar cómo se encuentran las formas de onda (fase y amplitud).

---

## 7. Entregables

> [!important] Entregables exigidos por la guía
> 1. **Informe** con las capturas de las gráficas tomadas en el osciloscopio.
> 2. **Simulación** del circuito en software libre u online (p. ej. Multisim Live, Falstad, LTspice, etc.).
> 3. **Observaciones y conclusiones** de la práctica.

---

## 8. Fuentes de información complementaria

- Amplificador Operacional — vídeo de YouTube: [https://www.youtube.com/watch?v=mESXqQ-gfcg](https://www.youtube.com/watch?v=mESXqQ-gfcg)

---

## Fórmulas a utilizar

> [!abstract] Resumen de fórmulas
> Ver [[Formulario - Amplificadores|Formulario]] para el desarrollo completo.
>
> - **Ganancia del amplificador inversor:** $A_v = -\dfrac{R_2}{R_1}$
> - **Tensión de salida (inversor):** $V_o = -\dfrac{R_2}{R_1} \cdot V_i$
> - **Ganancia del amplificador no inversor:** $A_v = 1 + \dfrac{R_2}{R_1}$
> - **Tensión de salida (no inversor):** $V_o = \left(1 + \dfrac{R_2}{R_1}\right) \cdot V_i$

---

## Bibliografía

- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*. Pearson.
- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press.
- Coughlin, R. F. & Driscoll, F. F. *Amplificadores operacionales y circuitos integrados lineales*. Prentice Hall.
