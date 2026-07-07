---
title: Informe LE1 v2 - Amplificador operacional (marco teorico, calculo, simulacion y comparacion)
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 6
orden: 102
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
  - tema/multisim
date: 2026-07-07
---

> [!info] Documentos relacionados
> - [[S06-99 Laboratorio - LE1 Amplificador operacional|S06-99 Guía del laboratorio]]
> - [[S06-100 Informe LE1 - Amplificador operacional|S06-100 Informe LE1 (v1, con mediciones físicas)]]
> - [[S06-101 Espejo - Mejoras propuestas al informe LE1|S06-101 Espejo de mejoras]]
> - [[S04-1 Aplicaciones lineales del amplificador operacional]] · [[S06-1 Amplificadores lineales y no lineales]] (teoría)
> - [[Formulario - Amplificadores|Formulario]]

> [!example] Datos del entregable
> - **Curso:** Circuitos Electrónicos Amplificadores (100000I21N)
> - **Docente:** Ing. Jorge Luis Robles Bokun
> - **Ciclo:** 2026-1 — Semana 6
> - **Laboratorio:** LE1 — Amplificador operacional (inversor y no inversor)
> - **Modalidad:** Grupal
>
> **Integrantes:**
> - Ludeña Muñante, Harold — U23319438
> - Espinoza Abarca, Pedro Rodrigo — U18216101
> - Rojas Novoa, Ernesto Raúl — U21227968
> - Carlos Baldeón Hidalgo
> - Luyo Murata, Tito Takeo — U23210744

---

## 1. Objetivos

- Implementar y analizar las configuraciones **inversora** y **no inversora** del amplificador operacional LM741.
- Calcular teóricamente la ganancia en lazo cerrado de cada configuración.
- Simular ambos circuitos en **Multisim Live** y obtener las formas de onda de entrada y salida.
- Comparar los resultados teóricos con los de la simulación y evaluar el error.

---

## 2. Marco teórico

### 2.1. El amplificador operacional

El **amplificador operacional (OPAMP)** es un circuito integrado de alta ganancia con acoplamiento directo en continua, dos entradas diferenciales —**no inversora** ($V^+$) e **inversora** ($V^-$)— y una única salida $V_o$. Su función de transferencia en lazo abierto es:

$$V_o = A_{ol} \cdot (V^+ - V^-) = A_{ol} \cdot V_d$$

Donde:

- $V_d = V^+ - V^-$ = tensión diferencial de entrada.
- $A_{ol}$ = ganancia en lazo abierto, típicamente del orden de $10^5$–$10^6\,\text{V/V}$ en frecuencias bajas.

### 2.2. Regiones de operación

La curva $V_o$ vs $V_d$ presenta **tres zonas** delimitadas por la alimentación bipolar $\pm V_{cc}$:

| Región | Condición | Comportamiento |
| ------ | --------- | -------------- |
| Saturación negativa | $V_d < -V_{sat}/A_{ol}$ | $V_o \approx -V_{sat}$ |
| **Lineal**          | $\|V_d\| < V_{sat}/A_{ol}$ | $V_o = A_{ol} \cdot V_d$ |
| Saturación positiva | $V_d > +V_{sat}/A_{ol}$ | $V_o \approx +V_{sat}$ |

Como $A_{ol}$ es enorme, la zona lineal en lazo abierto es extremadamente angosta (del orden de $\mu\text{V}$). Para forzar al OPAMP a trabajar en la región lineal de manera estable se usa **realimentación negativa**: una fracción de la salida se reinyecta en la entrada inversora, lo que reduce la ganancia efectiva pero la hace dependiente solo de los componentes externos (no del $A_{ol}$ del integrado).

### 2.3. Modelo del OPAMP ideal

Para el análisis de circuitos lineales con realimentación negativa se usa el **modelo ideal**, basado en tres hipótesis:

1. **Corriente de entrada nula:** $I^+ = I^- = 0$ (impedancia de entrada infinita).
2. **Tensión diferencial nula** (tierra virtual): $V^+ = V^-$, consecuencia de $A_{ol} \to \infty$ con realimentación negativa estable.
3. **Impedancia de salida nula:** la salida entrega la corriente que demande la carga sin caída de tensión.

Estas tres hipótesis bastan para deducir la ganancia de cualquier topología lineal aplicando la **Ley de Kirchhoff de Corrientes (LKC)** en la entrada inversora.

### 2.4. Configuración inversora

La señal de entrada se aplica a la terminal **inversora** a través de $R_1$, con la entrada **no inversora** conectada a tierra. La realimentación se cierra mediante $R_2$ entre la salida y la entrada inversora.

Aplicando tierra virtual ($V^- = V^+ = 0\,\text{V}$) y LKC en el nodo inversor (donde $I^- = 0$):

$$\frac{V_i - 0}{R_1} = \frac{0 - V_o}{R_2}$$

Despejando se obtiene la ganancia en lazo cerrado:

$$\boxed{A_v = \frac{V_o}{V_i} = -\frac{R_2}{R_1}}$$

El signo negativo indica que la salida está **desfasada $180°$** respecto a la entrada (inversión de polaridad). La ganancia depende exclusivamente del cociente de las dos resistencias externas.

### 2.5. Configuración no inversora

La señal de entrada se aplica a la terminal **no inversora**. La entrada inversora se realimenta desde la salida mediante un divisor formado por $R_1$ (a tierra) y $R_2$ (al nodo de salida).

Por tierra virtual: $V^- = V^+ = V_i$. Aplicando LKC en el nodo inversor:

$$\frac{0 - V_i}{R_1} + \frac{V_o - V_i}{R_2} = 0$$

De donde:

$$\boxed{A_v = \frac{V_o}{V_i} = 1 + \frac{R_2}{R_1}}$$

La salida está **en fase** con la entrada ($0°$) y la ganancia es siempre **mayor o igual a 1** (esta topología no permite atenuar). El término "$+1$" representa el seguimiento directo de la entrada por la terminal $V^+$, y el cociente $R_2/R_1$ aporta la amplificación adicional.

### 2.6. Parámetros del LM741 relevantes para esta práctica

| Parámetro | Símbolo | Valor típico LM741 | Implicancia en el laboratorio |
| --------- | ------- | ------------------ | ----------------------------- |
| Ganancia en lazo abierto | $A_{ol}$ | $\approx 2 \times 10^5$ | Justifica la aproximación de tierra virtual |
| Tensión de alimentación | $V^+, V^-$ | $\pm 12\,\text{V}$ (en este lab) | Define el techo y piso de saturación |
| Tensión de salida máxima | $V_{o,sat}$ | $\approx \pm 10{,}5\,\text{V}$ | Por debajo de $V_{cc}$; limita la excursión |
| Slew rate | $SR$ | $0{,}5\,\text{V}/\mu\text{s}$ | Limitación a alta frecuencia / alta amplitud |
| Impedancia de entrada | $Z_{in}$ | $\approx 2\,\text{M}\Omega$ | Permite asumir $I_{in} \approx 0$ |
| Producto ganancia–ancho de banda | $GBW$ | $\approx 1\,\text{MHz}$ | A $5\,\text{kHz}$ con $\|A_v\|=5$, BW $\approx 200\,\text{kHz}$ — sin afectación |
| Tensión de offset de entrada | $V_{io}$ | $\approx 1\,\text{mV}$ | Despreciable frente a la señal de entrada |
| CMRR | — | $\approx 90\,\text{dB}$ | Buen rechazo a ruido de modo común |

### 2.7. Verificación de operación en zona lineal

Antes de simular/medir conviene verificar que el circuito no satura ni se ve limitado por slew rate (para la amplitud usada en la simulación, $V_i = 1\,\text{V}$ pico):

- **Saturación:** la excursión máxima de salida es $2 \cdot V_{o,sat} \approx 21\,\text{Vpp}$. La mayor salida esperada es la del inversor: $10\,\text{Vpp} \ll 21\,\text{Vpp}$. **No satura.**
- **Slew rate:** la pendiente máxima de $V_o(t) = V_{op}\sin(2\pi f t)$ es $|dV_o/dt|_{max} = 2\pi f \cdot V_{op}$. Para $f = 5\,\text{kHz}$ y $V_{op} = 5\,\text{V}$: $2\pi \times 5000 \times 5 \approx 0{,}157\,\text{V}/\mu\text{s} \ll SR = 0{,}5\,\text{V}/\mu\text{s}$. **Sin distorsión por slew rate.**

Ambas verificaciones aseguran que las fórmulas ideales $-R_2/R_1$ y $1 + R_2/R_1$ aplican válidamente.

---

## 3. Cálculo teórico

> [!note] Amplitud de la señal de entrada
> La guía indica una señal senoidal de $5\,\text{kHz}$ y $1\,\text{Vpp}$. En la simulación la fuente V1 se configuró con **amplitud de $1\,\text{V}$ pico** (es decir, $2\,\text{Vpp}$). Como la ganancia es independiente de la amplitud (zona lineal), los cálculos siguientes se presentan para la amplitud simulada de $2\,\text{Vpp}$; para $1\,\text{Vpp}$ basta dividir las salidas entre 2.

### 3.1. Amplificador inversor ($R_1 = 2\,\text{k}\Omega$, $R_2 = 10\,\text{k}\Omega$)

Ganancia teórica:

$$A_v = -\frac{R_2}{R_1} = -\frac{10\,\text{k}\Omega}{2\,\text{k}\Omega} = -5{,}000$$

Tensión de salida esperada con $V_i = 2\,\text{Vpp}$ ($1\,\text{V}$ pico):

$$V_o = |A_v| \cdot V_i = 5 \times 2\,\text{Vpp} = 10\,\text{Vpp} \quad (5\,\text{V pico, desfasada } 180°)$$

$$\boxed{A_{v,\text{inv}} = -5{,}000 \quad ; \quad V_{o} = 10\,\text{Vpp} \; \text{invertida}}$$

### 3.2. Amplificador no inversor ($R_1 = 2.2\,\text{k}\Omega$, $R_2 = 5.6\,\text{k}\Omega$)

Ganancia teórica:

$$A_v = 1 + \frac{R_2}{R_1} = 1 + \frac{5.6\,\text{k}\Omega}{2.2\,\text{k}\Omega} = 1 + 2{,}5455 = 3{,}5455$$

Tensión de salida esperada con $V_i = 2\,\text{Vpp}$:

$$V_o = 3{,}5455 \times 2\,\text{Vpp} = 7{,}091\,\text{Vpp} \quad (3{,}545\,\text{V pico, en fase})$$

$$\boxed{A_{v,\text{noinv}} = +3{,}5455 \quad ; \quad V_{o} \approx 7{,}09\,\text{Vpp} \; \text{en fase}}$$

---

## 4. Simulación en Multisim Live

Ambos circuitos se simularon en **Multisim Live** con el modelo del LM741, alimentación bipolar $\pm 12\,\text{V}$ (fuentes V2 y V3) y fuente senoidal V1 de $1\,\text{V}$ pico y $5\,\text{kHz}$. Las sondas PR1 (verde) y PR2 (azul) registran $V_i$ y $V_o$ respectivamente en el analizador transitorio (Grapher).

### 4.1. Amplificador inversor

**Esquemático:**

![[Lab1 - Inversor-schematic.png]]
*Circuito inversor en Multisim Live: $R_1 = 2\,\text{k}\Omega$ en serie con la entrada inversora, $R_2 = 10\,\text{k}\Omega$ de realimentación, entrada no inversora a tierra.*

**Formas de onda:**

![[Lab1 - Inversor-Grapher.png]]
*Grapher: $V_i$ (verde, $1\,\text{V}$ pico) y $V_o$ (azul, $5\,\text{V}$ pico). Se aprecia el desfase de $180°$: cuando la entrada alcanza su máximo, la salida está en su mínimo.*

**Lecturas de la simulación** (extraídas del CSV exportado, régimen estacionario):

| Magnitud | $V_i$ (PR1) | $V_o$ (PR2) |
| -------- | ----------- | ----------- |
| Valor pico positivo | $+0{,}9998\,\text{V}$ | $+4{,}9993\,\text{V}$ |
| Valor pico negativo | $-0{,}9998\,\text{V}$ | $-4{,}9987\,\text{V}$ |
| Valor pico-pico | $1{,}9996\,\text{Vpp}$ | $9{,}9980\,\text{Vpp}$ |
| Fase relativa | referencia | $180°$ (invertida) |

Ganancia simulada:

$$|A_{v,\text{sim}}| = \frac{V_{o,pp}}{V_{i,pp}} = \frac{9{,}9980}{1{,}9996} = 4{,}9999 \;\Rightarrow\; \boxed{A_{v,\text{sim}} = -5{,}000}$$

### 4.2. Amplificador no inversor

**Esquemático:**

![[Lab1 - NoInversor-schematic.png]]
*Circuito no inversor en Multisim Live: señal a la entrada no inversora; divisor de realimentación con $R_1 = 2.2\,\text{k}\Omega$ a tierra y $R_2 = 5.6\,\text{k}\Omega$ a la salida.*

**Formas de onda:**

![[Lab1 - NoInversor-Grapher.png]]
*Grapher: $V_i$ (verde, $1\,\text{V}$ pico) y $V_o$ (azul, $\approx 3{,}54\,\text{V}$ pico). Ambas señales cruzan por cero y alcanzan sus máximos en los mismos instantes: están **en fase** ($0°$).*

**Lecturas de la simulación** (CSV, régimen estacionario):

| Magnitud | $V_i$ (PR1) | $V_o$ (PR2) |
| -------- | ----------- | ----------- |
| Valor pico positivo | $+0{,}9994\,\text{V}$ | $+3{,}5434\,\text{V}$ |
| Valor pico negativo | $-0{,}9994\,\text{V}$ | $-3{,}5431\,\text{V}$ |
| Valor pico-pico | $1{,}9988\,\text{Vpp}$ | $7{,}0865\,\text{Vpp}$ |
| Fase relativa | referencia | $0°$ (en fase) |

Ganancia simulada:

$$A_{v,\text{sim}} = \frac{V_{o,pp}}{V_{i,pp}} = \frac{7{,}0865}{1{,}9988} = \boxed{+3{,}5453}$$

---

## 5. Comparación de resultados

### 5.1. Teórico vs simulado

| Configuración | $A_v$ teórico | $A_v$ Multisim Live | Error relativo | Fase teórica | Fase simulada |
| ------------- | ------------- | ------------------- | -------------- | ------------ | ------------- |
| Inversor ($R_1=2\,\text{k}\Omega$, $R_2=10\,\text{k}\Omega$) | $-5{,}0000$ | $-4{,}9999$ | $0{,}002\,\%$ | $180°$ | $180°$ ✓ |
| No inversor ($R_1=2.2\,\text{k}\Omega$, $R_2=5.6\,\text{k}\Omega$) | $+3{,}5455$ | $+3{,}5453$ | $0{,}005\,\%$ | $0°$ | $0°$ ✓ |

**Análisis:**

- La concordancia entre teoría y simulación es prácticamente exacta (error $< 0{,}01\,\%$). La diferencia residual se explica por la **ganancia en lazo abierto finita** del modelo del LM741 ($A_{ol} \approx 2\times10^5$): la ganancia real en lazo cerrado del inversor es $A_v = \dfrac{-R_2/R_1}{1 + (1 + R_2/R_1)/A_{ol}}$, ligeramente menor en módulo que el valor ideal.
- La **relación de fase** se cumple exactamente como predice cada topología: $180°$ en el inversor (señales en oposición) y $0°$ en el no inversor (señales en fase).
- La salida se mantiene **senoidal sin recorte** en ambos casos: $10\,\text{Vpp}$ y $7{,}09\,\text{Vpp}$ están muy por debajo del límite de saturación ($\approx 21\,\text{Vpp}$ con $\pm12\,\text{V}$), y la exigencia de slew rate ($0{,}157\,\text{V}/\mu\text{s}$ máx.) es muy inferior a los $0{,}5\,\text{V}/\mu\text{s}$ del LM741 — coherente con la verificación de la sección 2.7.

### 5.2. Contraste con las mediciones físicas del laboratorio

En la sesión presencial (ver [[S06-100 Informe LE1 - Amplificador operacional|informe v1]]) se midió con el osciloscopio una ganancia de $-4{,}81$ para el inversor y $+3{,}41$ para el no inversor (error $\approx 3{,}9\,\%$ respecto al teórico en ambos casos):

| Configuración | $A_v$ teórico | $A_v$ simulado | $A_v$ medido (osciloscopio) | Error medido vs teórico |
| ------------- | ------------- | -------------- | --------------------------- | ----------------------- |
| Inversor | $-5{,}000$ | $-5{,}000$ | $-4{,}81$ | $3{,}85\,\%$ |
| No inversor | $+3{,}545$ | $+3{,}545$ | $+3{,}41$ | $3{,}89\,\%$ |

La simulación reproduce el valor ideal casi sin error porque usa resistores exactos; en el circuito físico la desviación de $\approx 4\,\%$ proviene principalmente de la **tolerancia de los resistores** ($\pm 5\,\%$) y del error de lectura del osciloscopio. Los tres métodos coinciden dentro del $\pm 4\,\%$, validando el modelo ideal del OPAMP.

---

## 6. Conclusiones

- Se verificó, mediante cálculo teórico y simulación en Multisim Live, el comportamiento de las dos configuraciones básicas del amplificador operacional: el **inversor** con $A_v = -5{,}000$ y el **no inversor** con $A_v = +3{,}545$, con un error entre teoría y simulación menor al $0{,}01\,\%$.
- La **ganancia en lazo cerrado depende exclusivamente de la relación de resistencias externas** ($R_2/R_1$), no de los parámetros internos del integrado, lo cual confirma la utilidad de la realimentación negativa: convierte un dispositivo de ganancia enorme e imprecisa ($A_{ol} \approx 2\times10^5$) en un amplificador de ganancia exacta y controlable.
- La **relación de fase** observada en las formas de onda coincide con la predicción teórica de cada topología: inversión de $180°$ cuando la señal ingresa por la terminal inversora, y fase $0°$ cuando ingresa por la no inversora.
- Las verificaciones de **saturación y slew rate** demostraron que el LM741, alimentado con $\pm12\,\text{V}$ y operando a $5\,\text{kHz}$ con salidas de hasta $10\,\text{Vpp}$, trabaja holgadamente dentro de su zona lineal, condición necesaria para que las fórmulas ideales sean válidas.
- El contraste teoría–simulación–experimento (error experimental $\approx 4\,\%$ frente al $< 0{,}01\,\%$ de la simulación) muestra que las desviaciones en el laboratorio físico provienen de los componentes reales (tolerancias) y de la instrumentación, no del modelo teórico.

---

## 7. Recomendaciones

- **Verificar la tolerancia de los resistores** con el multímetro antes del montaje y usar los valores medidos (no los nominales) en el cálculo teórico: esto reduce la brecha entre ganancia calculada y medida.
- **Unir las tierras** del generador de funciones, el osciloscopio y la fuente de alimentación en un único punto de referencia antes de energizar; una referencia flotante produce lecturas erróneas y ruido.
- **Confirmar la alimentación bipolar $\pm12\,\text{V}$ con el multímetro** antes de insertar el LM741, y revisar el pinout (pin 7 = $V^+$, pin 4 = $V^-$): una inversión de alimentación puede dañar el integrado.
- **Mantener la señal de entrada dentro del margen lineal**: con $|A_v| = 5$ y $V_{o,sat} \approx \pm10{,}5\,\text{V}$, la entrada no debe superar $\approx 4{,}2\,\text{Vpp}$ para evitar el recorte por saturación.
- **Simular antes de montar**: la simulación permite anticipar amplitudes, fases y márgenes de saturación, de modo que en el laboratorio el tiempo se dedica a medir y no a depurar errores de conexión.
- Al comparar con el osciloscopio, **usar las mediciones automáticas ($V_{pp}$, frecuencia, fase)** en lugar de la lectura visual de divisiones, para reducir el error de paralaje.
- Para trabajos futuros a mayor frecuencia o amplitud, considerar un OPAMP con mayor $GBW$ y slew rate (p. ej. TL081), pues el LM741 comienza a distorsionar cuando $2\pi f V_{op}$ se acerca a $0{,}5\,\text{V}/\mu\text{s}$.

---

## Bibliografía

- Boylestad, R. L. & Nashelsky, L. (2009). *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos* (10.ª ed.). Pearson Educación.
- Sedra, A. S. & Smith, K. C. (2015). *Microelectronic Circuits* (7.ª ed.). Oxford University Press.
- Coughlin, R. F. & Driscoll, F. F. (1999). *Amplificadores Operacionales y Circuitos Integrados Lineales* (5.ª ed.). Pearson Educación.
- Texas Instruments. (2015). *LM741 Operational Amplifier — Datasheet (SNOSC25D)*.
- National Instruments. *Multisim Live* — [https://www.multisim.com](https://www.multisim.com)
