---
title: Informe LE2 - Realimentación negativa (amplificador de transresistencia con BJT 2N2222)
curso: "[[Amplificadores MOC]]"
unidad: 3
semana: 9
orden: 100
tipo: evaluacion
subtipo: laboratorio
tags:
  - curso/amplificadores
  - tipo/evaluacion
  - subtipo/laboratorio
  - tema/laboratorio
  - tema/informe
  - tema/realimentacion-negativa
  - tema/realimentacion-shunt-shunt
  - tema/transresistencia
  - tema/impedancia-de-entrada
  - tema/respuesta-en-frecuencia
  - tema/2n2222
date: 2026-07-07
---

> [!info] Documentos relacionados
> - [[S09-99 Laboratorio - LE2 Realimentacion negativa|S09-99 Guía del laboratorio LE2]]
> - [[S08-1 Material 1|S08-1 Teoría de realimentación (topologías y parámetros)]]
> - [[Formulario - Amplificadores|Formulario]]
> - Simulaciones Multisim: carpeta [`simulacion_multisim/`](simulacion_multisim/) (`switch_abierto/`, `switch_cerrado/`)

> [!example] Datos del entregable
> - **Curso:** Circuitos Electrónicos Amplificadores
> - **Docente:** Jorge Luis Robles Bokun
> - **Ciclo:** 2026-1 — Semana 9
> - **Práctica:** Guía Nº 2 — Realimentación negativa (LE2)
> - **Modalidad:** Grupal
>
> **Integrantes:**
> - Ludeña Muñante, Harold — U23319438
> - Espinoza Abarca, Pedro Rodrigo — U18216101
> - Rojas Novoa, Ernesto Raúl — U21227968
> - Carlos Baldeón Hidalgo
> - Luyo Murata, Tito Takeo — U23210744

---

## 1. Objetivo

Analizar e implementar (en simulación) el funcionamiento de un amplificador con **realimentación negativa tipo tensión-paralelo (shunt-shunt)**, midiendo la **transresistencia** $R_m = V_o/I_g$ y la **impedancia de entrada** $Z_i = V_g/I_g$ del circuito **con** y **sin** realimentación, y comparando los resultados simulados con los valores teóricos.

---

## 2. Materiales y equipos

| Categoría | Elemento |
| --------- | -------- |
| Componente activo | Transistor BJT **2N2222A** |
| Componentes pasivos | Resistores $100\ \Omega$, $1\ \text{k}\Omega$, $2\times10\ \text{k}\Omega$, $2\times5.6\ \text{k}\Omega$; condensadores electrolíticos $3\times10\ \mu\text{F}/25\ \text{V}$ |
| Soporte | Protoboard 1660 puntos |
| Equipos | Generador de funciones, fuente de alimentación 2231A, multímetro digital CD 771, osciloscopio digital |
| Software | **Multisim Live** (simulación transitoria interactiva) |

---

## 3. Marco teórico

### 3.1. Realimentación negativa

La **realimentación** consiste en tomar una muestra de la señal de salida de un sistema y devolverla a su entrada. Cuando la señal devuelta se **opone** a la señal de excitación, la realimentación es **negativa**: la ganancia de lazo cerrado se reduce, pero a cambio se obtienen mejoras sistemáticas en el comportamiento del amplificador.

Para un amplificador de ganancia de lazo abierto $A$ y una red de realimentación de factor $\beta$, la ganancia con realimentación es:

$$A_f = \frac{A}{1 + A\beta}$$

Donde:
- $A$ = ganancia de lazo abierto (incluyendo el efecto de carga de la red $\beta$)
- $\beta$ = factor de realimentación (fracción de la salida devuelta a la entrada)
- $T = A\beta$ = **ganancia de lazo** (loop gain)
- $1 + T$ = **factor de desensibilización**

Los beneficios de la realimentación negativa escalan con $(1+T)$:

- **Estabilización de la ganancia:** $\dfrac{dA_f}{A_f} = \dfrac{1}{1+T}\cdot\dfrac{dA}{A}$ — la ganancia depende de la red pasiva $\beta$ y no de los parámetros del transistor.
- **Reducción de la distorsión no lineal** y del ruido generado dentro del lazo, en el factor $1/(1+T)$.
- **Extensión del ancho de banda:** el producto ganancia×ancho de banda se conserva; los polos se desplazan en $(1+T)$.
- **Modificación de impedancias** de entrada y salida según la topología.

### 3.2. Topología tensión-paralelo (shunt-shunt) y transresistencia

Existen cuatro topologías según **qué se muestrea** en la salida (tensión o corriente) y **cómo se mezcla** en la entrada (serie o paralelo). En este laboratorio:

- Se **muestrea la tensión** del colector ($V_o$).
- Se **devuelve una corriente** al nudo de base, en **paralelo** con la fuente de señal.

Es decir, una realimentación **tensión-paralelo (shunt-shunt)**, cuya magnitud natural estabilizada es la **transresistencia**:

$$R_m = \frac{V_o}{I_g} \quad [\Omega]$$

Donde:
- $V_o$ = tensión de salida (colector)
- $I_g$ = corriente de señal inyectada al nudo de entrada

Los efectos de esta topología sobre las impedancias son:

$$R_{mf} = \frac{R_m}{1+T}\,, \qquad Z_{if} = \frac{Z_i}{1+T}\,, \qquad Z_{of} = \frac{Z_o}{1+T}$$

**Ambas impedancias disminuyen** (mezcla paralelo → baja $Z_i$; muestreo de tensión → baja $Z_o$). Con ganancia de lazo alta, la transresistencia queda fijada por la resistencia de realimentación:

$$R_{mf} \;\xrightarrow{\;T\gg1\;}\; -R_f \quad\text{con } R_f = R_3 + R_4$$

### 3.3. El circuito de la práctica

![[guia2-circuito.png]]
*Etapa en emisor común (2N2222) con red de realimentación $R_3+R_4$ de colector a base.*

- La fuente $V_g$ con $R_1 = 10\ \text{k}\Omega$ en serie se comporta como **fuente de corriente** de señal: $I_g = (V_g - V_i)/R_1$ — apropiada para excitar un amplificador de transresistencia.
- $R_3 + R_4 = 11.2\ \text{k}\Omega$ conectan colector→base: forman simultáneamente el **bias por realimentación de colector** (DC) y la **red de realimentación** de señal (AC).
- $C_3$ puentea a $R_E$ para que el emisor quede a tierra de señal (máxima ganancia interna).
- **S1 y $C_2$** controlan el lazo **sin alterar el punto de operación** ($C_2$ bloquea la DC):
	- **S1 abierto** → el punto medio de $R_3$–$R_4$ queda flotante → el camino colector→base está completo → **realimentación ACTIVA** → se miden $R_{mf}$, $Z_{if}$ (paso 3b de la guía).
	- **S1 cerrado** → el punto medio queda a tierra de señal vía $C_2$ → el lazo se **rompe**: $R_3$ pasa a ser una carga a tierra en la entrada y $R_4$ una carga a tierra en el colector → **SIN realimentación** → se miden $R_m$, $Z_i$ (paso 3a de la guía).

> [!note] Correspondencia confirmada por simulación
> La simulación confirma el mapeo: con S1 **cerrado** la transresistencia es alta ($\sim63\ \text{k}\Omega$, lazo abierto) y con S1 **abierto** cae a $\sim9.8\ \text{k}\Omega \approx R_f = 11.2\ \text{k}\Omega$, la firma inequívoca del lazo cerrado.

---

## 4. Cálculo teórico

### 4.1. Punto de operación DC

Con S1 en cualquier posición el bias es el mismo ($C_2$ bloquea la DC). El bias es por **realimentación de colector**: $V_{CC} \to R_C \to$ colector $\to R_3+R_4 \to$ base, con $R_2$ de base a tierra ($R_1$ no conduce DC por $C_1$). Tomando $\beta = 160$ y $V_{BE} = 0.7\ \text{V}$:

**Nudo de base** ($I_B = I_E/(\beta+1)$, $I_E = (V_B - 0.7)/R_E$):

$$\frac{V_C - V_B}{R_3+R_4} = I_B + \frac{V_B}{R_2}$$

**Nudo de colector:**

$$\frac{V_{CC} - V_C}{R_C} = I_C + \frac{V_C - V_B}{R_3+R_4}$$

Resolviendo el sistema:

$$\boxed{V_B = 1.51\ \text{V} \qquad V_E = 0.81\ \text{V} \qquad V_C = 3.76\ \text{V} \qquad I_C \approx 8.0\ \text{mA}}$$

El punto medio de la red queda en $V_M = (V_B + V_C)/2 = 2.64\ \text{V}$ (resistencias iguales).

### 4.2. Parámetros de pequeña señal

$$g_m = \frac{I_C}{V_T} = \frac{8.03\ \text{mA}}{25\ \text{mV}} = 0.321\ \text{S} \qquad r_\pi = \frac{\beta}{g_m} \approx 498\ \Omega \qquad r_o = \frac{V_A}{I_C} \approx 9.3\ \text{k}\Omega$$

### 4.3. Sin realimentación (S1 cerrado) — banda media

Con el punto medio a tierra de señal, la entrada ve $R_3$ a tierra y el colector ve $R_4$ a tierra:

**Impedancia del nudo de entrada:**

$$Z_{i,\text{nodo}} = R_2 \parallel R_3 \parallel r_\pi = 10\text{k} \parallel 5.6\text{k} \parallel 498 \approx 437\ \Omega$$

**Impedancia vista por el generador** (la que define la guía, $Z_i = V_g/I_g$):

$$Z_i = R_1 + Z_{i,\text{nodo}} \approx 10.4\ \text{k}\Omega$$

**Carga efectiva de colector y ganancia de tensión:**

$$R_L' = R_C \parallel R_4 \parallel r_o \approx 780\ \Omega \qquad A_v = -g_m R_L' \approx -250$$

**Transresistencia** (banda media, $C_3$ como cortocircuito perfecto):

$$R_m = \frac{V_o}{I_g} = A_v \cdot Z_{i,\text{nodo}} = -250 \times 437 \approx \boxed{-109\ \text{k}\Omega}$$

### 4.4. Con realimentación (S1 abierto) — banda media

Análisis shunt-shunt con $R_f = R_3 + R_4 = 11.2\ \text{k}\Omega$ y $\beta_{fb} = -1/R_f$:

**Lazo abierto con carga de la red** ($R_f$ carga la entrada y la salida):

$$R_i' = R_2 \parallel R_f \parallel r_\pi \approx 455\ \Omega \qquad R_L'' = R_C \parallel R_f \parallel r_o \approx 836\ \Omega$$

$$R_{m0} = -g_m R_L'' \cdot R_i' = -0.321 \times 836 \times 455 \approx -122\ \text{k}\Omega$$

**Ganancia de lazo y factor de desensibilización:**

$$T = |R_{m0}| \cdot \frac{1}{R_f} = \frac{122\text{k}}{11.2\text{k}} \approx 10.9 \qquad 1 + T \approx 11.9$$

**Magnitudes de lazo cerrado:**

$$R_{mf} = \frac{R_{m0}}{1+T} = \frac{-122\ \text{k}\Omega}{11.9} \approx \boxed{-10.3\ \text{k}\Omega} \qquad\left(\to -R_f = -11.2\ \text{k}\Omega \text{ si } T\to\infty\right)$$

$$Z_{if,\text{nodo}} = \frac{R_i'}{1+T} = \frac{455}{11.9} \approx 38\ \Omega \qquad Z_{if} = R_1 + 38 \approx \boxed{10.04\ \text{k}\Omega}$$

**Impedancia de salida:** $Z_o \approx R_C \parallel R_4 \parallel r_o \approx 780\ \Omega$ sin realimentación; $Z_{of} \approx 836/11.9 \approx 70\ \Omega$ con realimentación.

### 4.5. Respuesta en frecuencia teórica

Modelo nodal completo de pequeña señal (incluye $C_1$, $C_2$, $C_3$, $r_\pi$, $r_o$, $C_\pi \approx 162\ \text{pF}$, $C_\mu \approx 8\ \text{pF}$), evaluado en las frecuencias de la tabla de la guía:

| $f$ (Hz) | $R_m$ (3a, sin realim.) | $Z_i$ (3a) | $R_{mf}$ (3b, con realim.) | $Z_{if}$ (3b) |
| -------: | ----------------------: | ---------: | -------------------------: | ------------: |
| 20 | 18.7 kΩ | 12.12 kΩ | 8.5 kΩ | 10.99 kΩ |
| 100 | 25.8 kΩ | 12.69 kΩ | 8.9 kΩ | 10.78 kΩ |
| 200 | 34.6 kΩ | 12.62 kΩ | 9.4 kΩ | 10.50 kΩ |
| 1 k | 87.4 kΩ | 11.37 kΩ | 10.2 kΩ | 10.07 kΩ |
| 2 k | 102.4 kΩ | 10.77 kΩ | 10.2 kΩ | 10.05 kΩ |
| 5 k | 108.4 kΩ | 10.49 kΩ | 10.3 kΩ | 10.04 kΩ |
| 10 k | 109.2 kΩ | 10.44 kΩ | 10.3 kΩ | 10.04 kΩ |
| 20 k | 108.8 kΩ | 10.43 kΩ | 10.3 kΩ | 10.04 kΩ |
| 50 k | 105.0 kΩ | 10.39 kΩ | 10.3 kΩ | 10.04 kΩ |
| 70 k | 101.1 kΩ | 10.37 kΩ | 10.3 kΩ | 10.04 kΩ |
| 100 k | 94.0 kΩ | 10.32 kΩ | 10.2 kΩ | 10.04 kΩ |
| 150 k | 81.4 kΩ | 10.24 kΩ | 10.2 kΩ | 10.04 kΩ |

![[s09-le2-respuesta-frecuencia.png]]
*Respuesta en frecuencia teórica de la transresistencia y de la impedancia de entrada, con los puntos medidos en Multisim a 1 kHz superpuestos.*

**Por qué tiene esta forma** (entregable 5):

- **Caída en baja frecuencia (sin realimentación):** el polo dominante lo pone el condensador de puenteo $C_3$. La resistencia que ve $C_3$ es muy pequeña — $R_E \parallel \left(r_e + \tfrac{R_{th,B}}{\beta+1}\right) \approx 16\ \Omega$ — de modo que su frecuencia de corte es:

$$f_{C_3} \approx \frac{1}{2\pi \cdot 16\ \Omega \cdot 10\ \mu\text{F}} \approx 1\ \text{kHz}$$

  Por debajo de $\sim$1 kHz, $R_E$ deja de estar puenteada, aparece **degeneración de emisor** y la ganancia (y con ella $R_m$) cae. A 1 kHz el circuito está *justo en el codo*: por eso la medición a 1 kHz da menos que el valor de banda media.
- **Banda media plana** (2 k–70 kHz): todos los condensadores de acoplo/puenteo son cortocircuitos y las capacidades del transistor aún no actúan.
- **Caída en alta frecuencia:** $C_\pi$ y, sobre todo, $C_\mu$ multiplicada por efecto **Miller** ($C_{in} \approx C_\pi + C_\mu(1+g_mR_L') \approx 2.2\ \text{nF}$) forman un polo con la resistencia del nudo de base ($\sim$437 Ω) alrededor de 150–200 kHz.
- **Con realimentación la curva es plana casi en todo el rango:** la realimentación desensibiliza la ganancia — mientras $T \gg 1$, $R_{mf} \approx -R_f$ sin importar cuánto varíe la ganancia interna. Los polos se desplazan en $(1+T)$: el ancho de banda se **extiende** por ambos extremos. Es la demostración clásica del intercambio **ganancia ↔ ancho de banda**.

---

## 5. Simulación en Multisim

Simulación transitoria interactiva con $V_g = 1\ \text{V}_{pp}$ (500 mV de amplitud) a 1 kHz. Sondas: PRA = $V_g$, PRB = $V_i$ (base), PRD = punto medio $V_M$, PRC = $V_o$ (colector), PRE = $V_E$, PR1 = $I_g$.

### 5.1. Caso 3a — S1 cerrado (sin realimentación)

![[s09-le2-sim-cerrado-esquema.png]]
*Esquemático con S1 cerrado: el punto medio de $R_3$–$R_4$ queda a tierra de señal a través de $C_2$.*

![[s09-le2-sim-cerrado-grapher.png]]
*Formas de onda: $V_o$ (celeste) alcanza $5.67\ \text{V}_{pp}$ con distorsión visible; el punto medio $V_M$ (magenta) queda plano — confirmación de que el lazo está roto.*

### 5.2. Caso 3b — S1 abierto (con realimentación)

![[s09-le2-sim-abierto-esquema.png]]
*Esquemático con S1 abierto: $R_3+R_4$ conectan colector→base y cierran el lazo.*

![[s09-le2-sim-abierto-grapher.png]]
*Formas de onda: $V_o$ (celeste) se reduce a $0.96\ \text{V}_{pp}$ pero perfectamente senoidal; el punto medio $V_M$ (magenta) ahora sí lleva señal ($0.48\ \text{V}_{pp}$) — el lazo está activo.*

### 5.3. Mediciones extraídas de la simulación

Valores en régimen estacionario (últimos 10 ciclos del CSV exportado del Grapher):

**Punto de operación DC** (idéntico en ambos casos, $t=0$):

| Nudo | $V_B$ | $V_M$ | $V_C$ | $V_E$ |
| ---- | ----- | ----- | ----- | ----- |
| Multisim | 1.498 V | 2.634 V | 3.771 V | 0.808 V |

**Señales a 1 kHz:**

| Magnitud | 3a — S1 cerrado | 3b — S1 abierto |
| -------- | --------------- | --------------- |
| $V_g$ | 0.999 V$_{pp}$ | 0.999 V$_{pp}$ |
| $V_i$ (base) | 120.5 mV$_{pp}$ | **18.9 mV$_{pp}$** |
| $V_o$ (colector) | **5.673 V$_{pp}$** | **0.964 V$_{pp}$** |
| $I_g$ | 90.4 µA$_{pp}$ | 98.8 µA$_{pp}$ |
| $R_m = V_o/I_g$ | **62.8 kΩ** | **9.76 kΩ** |
| $Z_i = V_g/I_g$ | **11.06 kΩ** | **10.11 kΩ** |
| $Z_{i,\text{nodo}} = V_i/I_g$ | 1.33 kΩ | 192 Ω |

---

## 6. Comparación teórico vs. simulado

| Magnitud | Teórico (1 kHz) | Multisim (1 kHz) | Error | Comentario |
| -------- | --------------- | ---------------- | ----- | ---------- |
| $V_B$ | 1.51 V | 1.498 V | 0.8 % | Bias por realimentación de colector |
| $V_C$ | 3.76 V | 3.771 V | 0.3 % | $I_C \approx 8$ mA confirmada |
| $V_E$ | 0.81 V | 0.808 V | 0.2 % | — |
| $R_m$ (sin realim.) | 87.4 kΩ | 62.8 kΩ | −28 % | Distorsión de gran señal: con 1 V$_{pp}$ de entrada el modelo lineal deja de valer (ver §6.1) |
| $Z_i$ (sin realim.) | 11.37 kΩ | 11.06 kΩ | 3 % | — |
| $R_{mf}$ (con realim.) | 10.2 kΩ | 9.76 kΩ | 4 % | La realimentación fija $R_{mf} \approx R_f \cdot \tfrac{T}{1+T}$ |
| $Z_{if}$ (con realim.) | 10.07 kΩ | 10.11 kΩ | 0.4 % | Dominada por $R_1$; el nudo cae de 1.33 kΩ → 192 Ω |

**Efecto neto de la realimentación medido en simulación:**

$$\frac{R_m}{R_{mf}}\bigg|_{sim} = \frac{62.8\ \text{k}\Omega}{9.76\ \text{k}\Omega} \approx 6.4 \qquad \frac{Z_{i,\text{nodo}}}{Z_{if,\text{nodo}}}\bigg|_{sim} = \frac{1.33\ \text{k}\Omega}{192\ \Omega} \approx 6.9$$

Ambos cocientes coinciden entre sí (~$1+T$ efectivo a 1 kHz con gran señal), como predice la teoría shunt-shunt: transresistencia e impedancia de entrada se dividen por el **mismo** factor.

### 6.1. Sobre la discrepancia en $R_m$ sin realimentación

La diferencia del 28 % **no es un error de montaje** sino consecuencia de operar en gran señal sin lazo:

1. La guía pide $V_g = 200\ \text{mV}_{pp}$; la simulación se corrió con $1\ \text{V}_{pp}$ (5× más).
2. Sin realimentación, esa amplitud lleva la base a $\pm60$ mV de excursión — muy por encima del límite de pequeña señal ($\sim$10 mV). La salida se comprime asimétricamente (pico superior redondeado en 6.87 V, valle en 1.20 V), visible en el Grapher.
3. La compresión reduce la componente fundamental → $R_m$ medida < $R_m$ lineal.
4. **Con realimentación la misma amplitud no distorsiona** ($V_i$ cae a 19 mV$_{pp}$ y el error teórico-simulado baja a 4 %): la realimentación negativa redujo la distorsión, exactamente como predice $D_f = D/(1+T)$.

---

## 7. Respuestas a los entregables de la guía

1. **Tabla comparativa teórico vs. experimental** → sección §6.
2. **Forma de realimentación del paso 3:** tensión-paralelo (**shunt-shunt** / *voltage-shunt*): se muestrea la **tensión** de colector y se reinyecta **corriente** al nudo de base a través de $R_3+R_4$. Es la topología que estabiliza la transresistencia y reduce ambas impedancias.
3. **Método para medir la impedancia de entrada y su fundamento:** no se mide corriente directamente; se mide la **caída de tensión sobre una resistencia conocida**. Con el osciloscopio se toman $V_g$ (antes de $R_1$) y $V_i$ (después de $R_1$); entonces $I_g = (V_g - V_i)/R_1$ y $Z_{if} = V_g/I_g$. El fundamento es la ley de Ohm sobre $R_1$, que actúa como *resistencia de sensado*: convierte la medición de corriente (difícil con osciloscopio) en dos mediciones de tensión (fáciles y no invasivas).
4. **Medición de la impedancia de salida:** método de la **carga variable**: (i) medir la salida en vacío $V_{oc}$; (ii) conectar una carga conocida $R_L$ y medir $V_L$; (iii) despejar del divisor de tensión:
$$Z_o = R_L\left(\frac{V_{oc}}{V_L} - 1\right)$$
   Alternativa: apagar la fuente de señal ($V_g = 0$, manteniendo el bias), inyectar una tensión de prueba $V_x$ en la salida a través de un condensador y medir la corriente $I_x$: $Z_o = V_x/I_x$. Valores esperados: $\sim$780 Ω sin realimentación → $\sim$70 Ω con realimentación (el muestreo de tensión baja $Z_o$ en $1+T$).
5. **Gráfico de la respuesta en frecuencia de la transresistencia y explicación** → sección §4.5.
6. **Observaciones y conclusiones** → secciones §8 y §9.
7. Informe presentado en la siguiente clase práctica. ✓

---

## 8. Observaciones

- El punto de operación DC es **idéntico con S1 abierto o cerrado** (diferencias < 1 mV en la simulación): $C_2$ aísla la DC del punto medio, de modo que la comparación con/sin realimentación se hace sobre el **mismo** punto de trabajo — un diseño de experimento limpio.
- Con el lazo cerrado, la señal en el nudo de base casi desaparece (18.9 mV$_{pp}$ vs. 120.5 mV$_{pp}$): el nudo de entrada se comporta como **tierra virtual de baja impedancia** (192 Ω), análogo al nudo inversor de un OPAMP con realimentación shunt.
- La traza del punto medio $V_M$ es el mejor indicador del estado del lazo: plana con S1 cerrado (tierra de señal), con señal de $0.48\ \text{V}_{pp}$ con S1 abierto (lazo activo).
- La salida sin realimentación muestra **distorsión asimétrica** evidente (compresión del semiciclo superior); con realimentación la senoide es limpia a simple vista, con amplitud 5.9 veces menor.
- A 1 kHz el circuito trabaja justo en el codo del polo de $C_3$ ($f_{C_3} \approx 1$ kHz): las mediciones sin realimentación a esa frecuencia quedan por debajo del valor de banda media (que se alcanza recién a partir de $\sim$2–5 kHz).
- $Z_i$ vista por el generador está dominada por $R_1 = 10\ \text{k}\Omega$ en ambos casos; el efecto de la realimentación se aprecia con claridad recién al referirla al nudo de base ($V_i/I_g$: 1.33 kΩ → 192 Ω).

## 9. Conclusiones

- Se verificó cuantitativamente el efecto de la **realimentación negativa shunt-shunt**: al cerrar el lazo, la transresistencia cae de 62.8 kΩ a 9.76 kΩ y la impedancia del nudo de entrada de 1.33 kΩ a 192 Ω — **ambas divididas por el mismo factor** (~6.5), tal como predice la teoría ($X_f = X/(1+T)$).
- Con ganancia de lazo alta, la transresistencia de lazo cerrado queda **fijada por la red pasiva**: $R_{mf} \approx 9.8$–$10.3\ \text{k}\Omega \approx R_f\cdot\tfrac{T}{1+T}$, con $R_f = R_3+R_4 = 11.2\ \text{k}\Omega$, casi independiente del transistor. Esto es lo que hace reproducible y manufacturable a un amplificador realimentado.
- La realimentación negativa **linealiza**: la misma entrada que distorsiona visiblemente la salida en lazo abierto (error teórico-simulado del 28 % por compresión) produce una senoide limpia en lazo cerrado (error del 4 %). La distorsión se reduce en $\approx 1/(1+T)$.
- La realimentación **aplana y extiende la respuesta en frecuencia**: la curva teórica de $R_{mf}$ es prácticamente constante de 100 Hz a 150 kHz, mientras que $R_m$ sin lazo varía más de 5:1 en ese rango (polo de $C_3$ abajo, efecto Miller arriba). Se paga ganancia para comprar ancho de banda y estabilidad.
- El punto de operación calculado a mano ($V_B = 1.51$ V, $V_C = 3.76$ V, $I_C = 8$ mA con $\beta=160$) coincide con la simulación con error < 1 %, validando el modelo del bias por realimentación de colector.
- Este circuito es el **análogo discreto del amplificador de transimpedancia** con OPAMP: mismo principio (shunt-shunt, $V_o \approx -R_f I_g$), misma tierra virtual, y la base del funcionamiento de los circuitos con [[S06-1 Amplificadores lineales y no lineales|amplificadores operacionales]] vistos en LE1.

## 10. Recomendaciones

- **Respetar la amplitud de la guía (200 mV$_{pp}$)** al medir el caso sin realimentación: con 1 V$_{pp}$ la etapa en lazo abierto se satura parcialmente y la transresistencia medida subestima el valor de pequeña señal. Alternativamente, medir la componente fundamental con FFT del osciloscopio.
- **Medir la banda media donde el circuito es plano (2–20 kHz)**, no solo a 1 kHz: a 1 kHz el polo de $C_3$ todavía afecta la medición sin realimentación. Si se quiere banda media a 1 kHz, aumentar $C_3$ a 100 µF.
- Para el barrido en frecuencia, tomar **las dos tensiones ($V_g$ y $V_i$) en cada punto** y calcular $I_g$ por diferencia; usar acoplamiento AC del osciloscopio para las señales pequeñas montadas sobre DC (p. ej. $V_i$ sobre 1.5 V).
- Verificar la polaridad de los electrolíticos al montar ($C_2$ con el + hacia el punto medio, que está a 2.6 V DC) y confirmar el bias con multímetro **antes** de inyectar señal: si $V_C \approx 3.8$ V, el montaje está correcto.
- En el protoboard, mantener cortas las conexiones del nudo de base: es el nudo de alta impedancia en lazo abierto y capta ruido/50 Hz con facilidad.

---

## Bibliografía

- Sedra, A. & Smith, K. (2015). *Microelectronic Circuits* (7.ª ed.). Oxford University Press. — Cap. 11: *Feedback* (topología shunt-shunt, amplificador de transresistencia).
- Boylestad, R. & Nashelsky, L. (2009). *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos* (10.ª ed.). Pearson. — Cap. 14: Realimentación y circuitos osciladores.
- Millman, J. & Halkias, C. *Integrated Electronics*. McGraw-Hill. — Análisis de amplificadores realimentados.
- Guía Nº 2 del curso: [[S09-99 Laboratorio - LE2 Realimentacion negativa]].
