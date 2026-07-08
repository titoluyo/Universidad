---
title: Informe LE3 - Filtro activo pasa bajo (Sallen-Key, R = 3.3 kΩ)
curso: "[[Amplificadores MOC]]"
unidad: 3
semana: 14
orden: 101
tipo: evaluacion
subtipo: laboratorio
tags:
  - curso/amplificadores
  - tipo/evaluacion
  - subtipo/laboratorio
  - tema/laboratorio
  - tema/informe
  - tema/filtro-activo
  - tema/filtro-pasa-bajo
  - tema/sallen-key
  - tema/respuesta-en-frecuencia
  - tema/diagrama-de-bode
  - tema/lm741
date: 2026-06-23
---

> [!info] Documentos relacionados
> - [[s14-laboratorio-le3-guia|Guía N° 3: Filtro activo pasa bajo]]
> - [[S14-2 Tema 14 - Filtros activos - introduccion y clasificacion|S14-2 Filtros activos: introducción y clasificación]] (teoría)
> - [[S14-3 Tema 14 - Funcion de transferencia de filtros - polos y ceros|S14-3 Función de transferencia: polos y ceros]] (teoría)
> - [[S14-4 Tema 14 - Filtros de primer orden y diagrama de Bode|S14-4 Filtros de primer orden y diagrama de Bode]] (teoría)
> - [[S14-5 Tema 14 - Diagrama de Bode por factores|S14-5 Diagrama de Bode por factores]] (teoría)
> - Evidencias: `TitoLuyoMurata-Laboratorio3-Evidencias.docx`
> - Simulación: carpeta `simulacion/3.3K/`

> [!example] Datos del entregable
> - **Curso:** Circuitos Electrónicos Amplificadores
> - **Docente:** Jorge Luis Robles Bokun
> - **Ciclo:** 2026-1 — Semana 14
> - **Práctica:** Laboratorio 3 — Filtro activo pasa bajo
>
> **Integrante:**
> - Luyo Murata, Tito Takeo — U23210744

---

## 1. Objetivo de la práctica

Analizar e implementar el amplificador operacional como **filtro activo pasa bajo** y medir su **respuesta en frecuencia**, contrastando los valores teóricos con la simulación (Multisim) y con las mediciones experimentales.

---

## 2. Materiales y equipos utilizados

| Categoría | Elemento |
| --------- | -------- |
| Componente activo | Circuito integrado **LM741** |
| Componentes pasivos | Resistores de $10\,\text{k}\Omega$ (×2, red de ganancia) y $3.3\,\text{k}\Omega$ (×2, red RC); condensadores cerámicos **104** ($0.1\,\mu\text{F}$, ×2) |
| Soporte | Protoboard 1660 puntos |
| Cableado | Cables macho-macho, pinzas de medición |
| Equipos | Osciloscopio digital / generador de funciones **RIGOL DHO924S**, multímetro digital, fuente de alimentación $\pm 12\,\text{V}$ |

---

## 3. Marco teórico

### 3.1. Filtros activos

Un **filtro activo** combina elementos pasivos ($R$, $C$) con un elemento activo (el OPAMP), lo que le permite — a diferencia de un filtro pasivo — tener **ganancia mayor que la unidad** en la banda de paso, impedancia de salida baja (el filtro no se "carga" con la etapa siguiente) y prescindir de inductores. El filtro **pasa bajo** deja pasar las frecuencias por debajo de su frecuencia de corte y atenúa las superiores.

### 3.2. Topología de la experiencia (Sallen-Key con realimentación positiva y negativa)

El circuito de la práctica emplea simultáneamente **realimentación negativa** (divisor $R_2$–$R_1$ hacia la entrada inversora, que fija la ganancia) y **realimentación positiva** (rama $R$–$C$ desde la salida hacia la red de entrada), manteniendo comportamiento lineal:

![[s14-le3-circuito-fundamento.png]]
*Circuito del fundamento: filtro activo pasa bajo con LM741.*

La realimentación negativa forma un amplificador no inversor de ganancia:

$$A = 1 + \frac{R_2}{R_1} \qquad\Longrightarrow\qquad V_o = A \cdot V^{+}$$

### 3.3. Función de transferencia

Aplicando KCL en el nudo $V^{+}$ y en el nudo intermedio $V$ de la red RC:

**En el nudo $V^{+}$:**

$$\frac{V^{+} - V_i}{R} + sC\,(V^{+} - V) = 0$$

**En el nudo $V$:**

$$(V - V^{+})\,Cs + V\,Cs + \frac{V - V_o}{R} = 0$$

Eliminando $V$ y usando $V^{+} = V_o / A$ se obtiene la función de transferencia de **segundo orden**:

$$\boxed{H(s) = \frac{A\,(1 + 2RCs)}{R^2C^2\,s^2 + (3 - A)\,RC\,s + 1}}$$

Del denominador (forma canónica de segundo orden) se identifican los parámetros:

- $\omega_o = \dfrac{1}{RC}$ = frecuencia natural
- $\alpha = \dfrac{3 - A}{2RC}$ = factor de atenuación
- $Q = \dfrac{\omega_o}{2\alpha} = \dfrac{1}{3 - A}$ = factor de calidad
- $\zeta = \dfrac{\alpha}{\omega_o} = \dfrac{3 - A}{2}$ = relación de amortiguamiento

> [!note] Dos particularidades de esta topología
> 1. El numerador contiene un **cero real** en $\omega_z = \frac{1}{2RC}$ (es decir, $f_z = \frac{f_o}{2}$). Por ello la pendiente asintótica en alta frecuencia es **−20 dB/déc** (los dos polos aportan −40 dB/déc y el cero devuelve +20 dB/déc) y no −40 dB/déc como en un pasa bajo de segundo orden "puro".
> 2. La estabilidad y el amortiguamiento dependen de la ganancia: si $A \to 3$, entonces $Q \to \infty$ y el circuito **oscila**. Con $A = 2$ se obtiene $Q = 1$, que produce un **pico de resonancia** moderado cerca de $f_o$ antes de la caída.

---

## 4. Cálculo teórico

### 4.1. Ganancia en banda de paso

Con $R_1 = R_2 = 10\,\text{k}\Omega$:

$$A = 1 + \frac{R_2}{R_1} = 1 + \frac{10\,\text{k}\Omega}{10\,\text{k}\Omega} = 2 \;\;(= 6.02\,\text{dB})$$

$$Q = \frac{1}{3 - A} = 1 \qquad \zeta = \frac{3 - A}{2} = 0.5$$

### 4.2. Parámetros de frecuencia

Red RC con $R = 3.3\,\text{k}\Omega$ y $C = 0.1\,\mu\text{F}$:

$$\omega_o = \frac{1}{RC} = \frac{1}{(3.3\times10^3)(0.1\times10^{-6})} = 3030.3\,\text{rad/s} \;\Rightarrow\; f_o = \frac{\omega_o}{2\pi} = 482.3\,\text{Hz}$$

| Parámetro | Fórmula | Valor |
| --------- | ------- | ----- |
| Frecuencia natural | $\omega_o = 1/RC$ | $3030.3\,\text{rad/s}$ |
| Frecuencia natural | $f_o = \omega_o / 2\pi$ | $482.3\,\text{Hz}$ |
| Cero del numerador | $f_z = f_o/2$ | $241.2\,\text{Hz}$ |
| Factor de calidad | $Q = 1/(3-A)$ | $1.0$ |
| Relación de amortiguamiento | $\zeta = (3-A)/2$ | $0.5$ |
| Frecuencia del pico | $f_{pico} \approx 0.946\,f_o$ | $456\,\text{Hz}$ |
| Ganancia máxima (pico) | $\|H\|_{max}$ | $4.50$ ($13.06\,\text{dB}$) |
| Corte a −3 dB de la banda de paso | $f_{-3dB} \approx 3.02\,f_o$ | $1456\,\text{Hz}$ |

La función de transferencia numérica queda:

$$H(s) = \frac{2 + 1.32\times10^{-3}\,s}{1.089\times10^{-7}\,s^2 + 3.3\times10^{-4}\,s + 1}$$

> [!tip] Forma de la respuesta esperada
> Con $Q = 1$ y el cero en $f_o/2$, la magnitud arranca plana en $A = 2$ ($6\,\text{dB}$), **sube hasta un máximo de $\approx 4.5$** ($13.1\,\text{dB}$) cerca de $f_o = 482\,\text{Hz}$, y luego cae con pendiente asintótica de $-20\,\text{dB/déc}$. No es una respuesta monótona tipo Butterworth: el pico es inherente al diseño con $A = 2$.

---

## 5. Simulación en Multisim

Se simuló el circuito con $R_3 = R_4 = 3.3\,\text{k}\Omega$ y los valores medidos de los condensadores ($C_1 = 97.5\,\text{nF}$, $C_2 = 113.7\,\text{nF}$), con un barrido AC de $1\,\text{Hz}$ a $1\,\text{MHz}$ y $V_i = 1\,\text{V}$:

![[s14-le3-multisim-esquema-3k3.png]]
*Esquema en Multisim: LM741 alimentado con ±12 V, $R_1 = R_2 = 10\,\text{k}\Omega$, $R_3 = R_4 = 3.3\,\text{k}\Omega$, sondas PR1 (Vi) y PR2 (Vo).*

![[s14-le3-multisim-bode-3k3.png]]
*AC Sweep: banda de paso en $6\,\text{dB}$ ($A_v = 2$), pico de resonancia de $12.4\,\text{dB}$ cerca de $400\,\text{Hz}$ y caída de $-20\,\text{dB/déc}$, con la fase bajando hacia −90°.*

Valores representativos exportados del Grapher (`Lab3 - Filtro 2026 (3.3K).csv`):

| $f$ [Hz] | 10 | 100 | 200 | 398 | 500 | 1 k | 10 k | 100 k |
| -------- | -- | --- | --- | --- | --- | --- | ---- | ----- |
| $\|V_o/V_i\|$ sim | 2.00 | 2.23 | 2.84 | **4.14** | 4.03 | 2.02 | 0.184 | 0.0184 |

La simulación reproduce la respuesta teórica de la sección 4: pico de $4.14$ ($12.4\,\text{dB}$) en $\approx 400\,\text{Hz}$ frente a los $4.50$ ($13.1\,\text{dB}$) en $456\,\text{Hz}$ del cálculo ideal. La pequeña diferencia (−8 % en amplitud, pico algo desplazado hacia abajo) proviene de que $C_1 \neq C_2$ en el esquema ($97.5$ vs $113.7\,\text{nF}$, valores medidos), mientras que el cálculo asume condensadores idénticos de $0.1\,\mu\text{F}$ y OPAMP ideal.

---

## 6. Datos experimentales

### 6.1. Montaje

![[s14-le3-protoboard.png]]
*Montaje del filtro en protoboard: LM741, resistencias y condensadores cerámicos 104 (0.1 µF).*

**Calibración de la fuente bipolar $\pm 12\,\text{V}$ (pin 7: +12 V, pin 4: −12 V):**

![[s14-le3-fuente-12v.png]]
*Verificación de la alimentación con multímetro: 12.1 V en la rama medida.*

![[s14-le3-montaje-equipos.png]]
*Vista general: fuente, protoboard y osciloscopio RIGOL DHO924S con ambos canales conectados.*

### 6.2. Medición de referencia

![[s14-le3-osc-50hz.png]]
*Captura a $f = 50\,\text{Hz}$: CH1 (entrada) $V_{pp} = 2.04\,\text{V}$, CH2 (salida) $V_{pp} = 4.21\,\text{V}$ → $A_v \approx 2.06$, coherente con la ganancia teórica de banda de paso $A = 2$.*

### 6.3. Tabla de mediciones

Señal de entrada: senoidal, $V_i = 1\,\text{V}_p$ ($2\,\text{V}_{pp}$). $V_o$ medido en $\text{V}_{pp}$ con el osciloscopio; $A_v = V_{o,pp} / V_{i,pp}$:

| $F$ [Hz] | 50 | 100 | 150 | 200 | 250 | 300 | 350 | 400 | 450 | 500 | 1 k | 2 k | 5 k | 10 k |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $V_o$ [$\text{V}_{pp}$] | 4.18 | 4.50 | 4.97 | 5.66 | 6.38 | 7.18 | 7.92 | 8.47 | 8.72 | 8.62 | 4.50 | 2.15 | 0.88 | 0.49 |
| $A_v$ | 2.09 | 2.25 | 2.49 | 2.83 | 3.19 | 3.59 | 3.96 | 4.24 | 4.36 | 4.31 | 2.25 | 1.08 | 0.44 | 0.245 |

La respuesta medida reproduce la forma predicha por la teoría: banda de paso con $A_v \approx 2.1$, **pico de resonancia $A_v \approx 4.36$ alrededor de $450\,\text{Hz}$** y caída posterior de $\approx -20\,\text{dB/déc}$ (entre 1 kHz y 10 kHz la ganancia cae un factor $\approx 9.2$ por década).

---

## 7. Comparación teórico vs. simulado vs. experimental (Entregable 1)

Las tres respuestas — teórica, simulada y experimental — coinciden en forma, banda de paso, posición del pico y pendiente de caída:

| $F$ [Hz] | $A_v$ teórico | $A_v$ simulado | $A_v$ **experimental** | Dif. exp. vs. teórico | Dif. exp. vs. simulado |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 50 | 2.05 | 2.06 | **2.09** | +1.8 % | +1.6 % |
| 100 | 2.21 | 2.23 | **2.25** | +1.8 % | +1.1 % |
| 150 | 2.47 | 2.50 | **2.49** | +0.8 % | −0.6 % |
| 200 | 2.81 | 2.84 | **2.83** | +0.9 % | −0.3 % |
| 250 | 3.21 | 3.24 | **3.19** | −0.7 % | −1.4 % |
| 300 | 3.66 | 3.64 | **3.59** | −1.8 % | −1.2 % |
| 350 | 4.07 | 3.92 | **3.96** | −2.7 % | +0.9 % |
| 400 | 4.37 | 4.14 | **4.24** | −3.1 % | +2.3 % |
| 450 | 4.50 | 4.08 | **4.36** | −3.0 % | +6.8 % |
| 500 | 4.43 | 4.03 | **4.31** | −2.7 % | +7.0 % |
| 1 k | 2.19 | 2.02 | **2.25** | +2.8 % | +11.3 % |
| 2 k | 1.00 | 0.95 | **1.08** | +7.6 % | +13.8 % |
| 5 k | 0.39 | 0.37 | **0.44** | +13.4 % | +19.1 % |
| 10 k | 0.19 | 0.18 | **0.245** | +26.8 % | +33.2 % |

### Razones de las diferencias

1. **Excelente acuerdo en banda de paso y zona del pico.** Hasta $\approx 350\,\text{Hz}$ las tres curvas coinciden dentro del **3 %**. La banda de paso experimental ($A_v \approx 2.1$) concuerda con $A = 1 + R_2/R_1 = 2$, y el pico medido ($A_v = 4.36$ en $\approx 450\,\text{Hz}$) concuerda con el teórico ($4.50$ en $456\,\text{Hz}$) dentro del 3 %.
2. **Tolerancia de los condensadores.** Los condensadores cerámicos 104 tienen tolerancias de ±10–20 %; los valores medidos en el esquema ($97.5$ y $113.7\,\text{nF}$) difieren entre sí un 16 %. Como $C_1 \neq C_2$, el pico simulado ($4.14$ en $400\,\text{Hz}$) queda algo por debajo del teórico ideal ($4.50$ en $456\,\text{Hz}$), que asume $C_1 = C_2 = 0.1\,\mu\text{F}$. El pico experimental cae **entre** ambos ($4.36$ en $450\,\text{Hz}$), como es de esperar.
3. **Limitaciones del LM741 y de la medición en alta frecuencia.** Sobre 2 kHz la diferencia crece (hasta +27 % vs. teórico y +33 % vs. simulado en 10 kHz) porque: la salida es ya muy pequeña ($0.49\,\text{V}_{pp}$) y la lectura de $V_{pp}$ en el osciloscopio incluye ruido y rizado (sesgo hacia arriba); el producto ganancia–ancho de banda finito del 741 ($\approx 1\,\text{MHz}$) y su impedancia de salida modifican la respuesta lejos de $f_o$; y los errores porcentuales se amplifican al dividir números pequeños.
4. **Tolerancia de las resistencias.** $R_1$, $R_2$, $R_3$ y $R_4$ tienen tolerancia típica de ±5 %, lo que introduce pequeños corrimientos en $A$ y $f_o$. En 50 Hz se midió $A_v = 2.09$ vs. $2.0$ teórico (+4.5 %), consistente con la tolerancia de $R_1$, $R_2$ y con la resolución de lectura del generador ($V_{i,pp} = 2.04\,\text{V}$ reales según el osciloscopio, no 2.00 V exactos).

---

## 8. Diagramas de Bode (Entregable 2)

![[s14-le3-bode-comparacion-3k3.png]]
*Diagrama de Bode de $H(s)$ para $R = 3.3\,\text{k}\Omega$: curva teórica (rojo), barrido AC de Multisim (verde discontinuo) y puntos experimentales (negro). Las tres respuestas se superponen en banda de paso, pico y pendiente de caída.*

Código MATLAB que genera el diagrama de Bode de la función de transferencia teórica:

```matlab
% Filtro activo pasa bajo Sallen-Key con A = 2 (Q = 1), R = 3.3 kOhm
A = 2;  C = 0.1e-6;  R = 3300;

H = tf(A*[2*R*C 1], [(R*C)^2 (3-A)*R*C 1]);

figure;
bode(H, 'r', {2*pi*10, 2*pi*1e5});  grid on;
legend('R = 3.3 k\Omega  (f_o = 482 Hz)');
title('Filtro activo pasa bajo — H(s) = A(1+2RCs)/(R^2C^2s^2+(3-A)RCs+1)');

% Verificacion de parametros
damp(H)                 % wn = 3030 rad/s, zeta = 0.5
[mag,~,w] = bode(H);    % pico: max(mag) = 4.50 en w = 2*pi*456 rad/s
```

Lectura del diagrama:

- **Banda de paso:** $6.02\,\text{dB}$ ($A_v = 2$).
- **Pico de resonancia:** $+13.06\,\text{dB}$ ($A_v = 4.50$) en $456\,\text{Hz}$, consecuencia de $Q = 1$ y del cero en $f_o/2$.
- **Alta frecuencia:** pendiente de $-20\,\text{dB/déc}$ (dos polos − un cero), verificada en teoría, simulación y mediciones.
- **Fase:** parte de $0°$, sube levemente por el cero y cae hacia $-90°$ en alta frecuencia (red de fase mínima con exceso polo-cero de 1).

---

## 9. Conclusiones (Entregable 3)

- Se comprobó experimentalmente que el circuito se comporta como un **filtro activo pasa bajo de segundo orden**: banda de paso con ganancia $A_v \approx 2.1$ (teórico $A = 1 + R_2/R_1 = 2$), pico de resonancia y caída posterior de $\approx -20\,\text{dB/déc}$, tal como predice la función de transferencia $H(s)$ deducida en el marco teórico.
- Con $A = 2$ el factor de calidad vale $Q = 1$ ($\zeta = 0.5$), lo que produce un **sobrepico de ganancia** cerca de $f_o$: se midió $A_{v,max} = 4.36$ ($12.8\,\text{dB}$) frente a los $4.50$ ($13.1\,\text{dB}$) teóricos — un error de solo **3 %**. La respuesta de este filtro no es plana tipo Butterworth ($\zeta \approx 0.707$, que requeriría $A = 1.6$), y la práctica lo evidenció con claridad.
- La frecuencia natural medida ($f_o \approx 482\,\text{Hz}$, pico en $\approx 450\,\text{Hz}$) concuerda con la calculada a partir de $R = 3.3\,\text{k}\Omega$ y $C = 0.1\,\mu\text{F}$: $f_o = 1/(2\pi RC) = 482\,\text{Hz}$. Teoría, simulación y experimento coinciden dentro del 3 % en toda la banda de paso.
- La pendiente medida entre 1 kHz y 10 kHz ($\approx -19\,\text{dB/déc}$) confirma la presencia del **cero en el numerador** de $H(s)$: sin él, un segundo orden caería a $-40\,\text{dB/déc}$.
- La simulación en Multisim reproduce fielmente la respuesta teórica; la ligera reducción del pico ($4.14$ vs. $4.50$) se explica por la diferencia entre los condensadores reales ($C_1 = 97.5\,\text{nF}$, $C_2 = 113.7\,\text{nF}$), que el modelo ideal no contempla.
- El diagrama de Bode resultó la herramienta natural para **comparar teoría, simulación y experimento** en un solo gráfico, mostrando la coincidencia de las tres respuestas en banda de paso, frecuencia y amplitud del pico, y pendiente de atenuación.

---

## 10. Recomendaciones

- **Medir y registrar** con multímetro los valores reales de todas las resistencias y condensadores antes del montaje, y usar esos valores (no los nominales) en el cálculo teórico y la simulación, ya que la tolerancia de los condensadores es la principal fuente de discrepancia en la zona del pico.
- **Verificar cuidadosamente las unidades** ($\Omega$/k$\Omega$, nF/µF) al ingresar los valores de los componentes en la simulación, y contrastar siempre la respuesta simulada con el cálculo teórico antes de darla por válida.
- **Densificar las mediciones alrededor de $f_o$** (p. ej. cada 25 Hz entre 350 y 550 Hz) para ubicar con precisión la frecuencia y amplitud del pico, y medir también la **fase** entre entrada y salida para completar el diagrama de Bode experimental.
- Usar condensadores de **poliéster o cerámicos NP0/C0G** de tolerancia conocida en la red RC (los electrolíticos de la lista de materiales no son adecuados para señal AC por su polaridad y tolerancia ±20 %); emparejar $C_1$ y $C_2$ mejora la simetría del pico.
- En alta frecuencia, medir $V_o$ con **promediado** o con la función de medición RMS del osciloscopio para reducir el sesgo del ruido cuando la señal es pequeña ($< 1\,\text{V}_{pp}$).
- Para trabajos con $f_o$ mayores o $Q$ altos, reemplazar el LM741 por un OPAMP de mayor producto ganancia–ancho de banda (TL072, TL081), ya que el 741 ($GBW \approx 1\,\text{MHz}$, $SR = 0.5\,\text{V}/\mu\text{s}$) empieza a limitar la respuesta.

---

## 11. Resumen de resultados

| Magnitud | Teórico ($R = 3.3\,\text{k}\Omega$, $C = 0.1\,\mu\text{F}$) | Simulado | Experimental | Error exp. vs. teórico |
| -------- | --------------------------------------------------------- | -------- | ------------ | ----- |
| Ganancia en banda de paso $A_v$ | $2.00$ ($6.0\,\text{dB}$) | $2.01$ | $2.09$ ($6.4\,\text{dB}$) | $+4.5\,\%$ |
| Ganancia máxima $A_{v,max}$ | $4.50$ ($13.1\,\text{dB}$) | $4.14$ | $4.36$ ($12.8\,\text{dB}$) | $-3.0\,\%$ |
| Frecuencia del pico $f_{pico}$ | $456\,\text{Hz}$ | $\approx 400\,\text{Hz}$ | $\approx 450\,\text{Hz}$ | $\approx -1\,\%$ |
| Frecuencia natural $f_o$ | $482\,\text{Hz}$ | — | $\approx 482\,\text{Hz}$ | — |
| Pendiente en alta frecuencia | $-20\,\text{dB/déc}$ | $-20\,\text{dB/déc}$ | $\approx -19\,\text{dB/déc}$ | — |
| Factor de calidad $Q$ | $1$ | $\approx 0.95$ | $\approx 0.97$ | $-3\,\%$ |

---

## Bibliografía

- Sedra, A. & Smith, K. (2015). *Microelectronic Circuits* (7.ª ed.). Oxford University Press. — Capítulo de filtros activos (topología Sallen-Key).
- Boylestad, R. & Nashelsky, L. (2017). *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos* (11.ª ed.). Pearson.
- Coughlin, R. F. & Driscoll, F. F. (1999). *Amplificadores operacionales y circuitos integrados lineales* (5.ª ed.). Prentice Hall.
- Texas Instruments. (2018). *LM741 Operational Amplifier — Datasheet* (SNOSC25D).
