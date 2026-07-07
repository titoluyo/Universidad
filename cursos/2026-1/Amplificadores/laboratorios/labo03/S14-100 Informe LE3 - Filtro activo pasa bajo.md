---
title: Informe LE3 - Filtro activo pasa bajo (Sallen-Key)
curso: "[[Amplificadores MOC]]"
unidad: 3
semana: 14
orden: 100
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
> - Evidencias originales: `TitoLuyoMurata-Laboratorio3-Evidencias.docx`
> - Simulación corregida: carpeta `simulacion/` (`Lab3 - Filtro 2026 (1).csv` y capturas)

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
| Componentes pasivos | Resistores de $10\,\text{k}\Omega$ (×2) y de la red RC; condensadores cerámicos **104** ($0.1\,\mu\text{F}$) |
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

La guía presenta la red RC con dos valores nominales: $R = 5.6\,\text{k}\Omega$ en la figura del procedimiento (valor usado en la simulación) y $R = 3.3\,\text{k}\Omega$ en el circuito del fundamento (resistencia que trae el alumno). Se calculan ambos casos con $C = 0.1\,\mu\text{F}$:

| Parámetro | Fórmula | $R = 5.6\,\text{k}\Omega$ | $R = 3.3\,\text{k}\Omega$ |
| --------- | ------- | ------------------------- | ------------------------- |
| Frecuencia natural | $\omega_o = 1/RC$ | $1785.7\,\text{rad/s}$ | $3030.3\,\text{rad/s}$ |
| Frecuencia natural | $f_o = \omega_o / 2\pi$ | $284.2\,\text{Hz}$ | $482.3\,\text{Hz}$ |
| Cero del numerador | $f_z = f_o/2$ | $142.1\,\text{Hz}$ | $241.2\,\text{Hz}$ |
| Pico de resonancia | $f_{pico} \approx 0.946\,f_o$ | $269\,\text{Hz}$ | $456\,\text{Hz}$ |
| Ganancia máxima | $\|H\|_{max}$ | $4.50$ ($13.06\,\text{dB}$) | $4.50$ ($13.06\,\text{dB}$) |
| Corte a −3 dB de la banda de paso | $f_{-3dB} \approx 3.02\,f_o$ | $858\,\text{Hz}$ | $1456\,\text{Hz}$ |

Las funciones de transferencia numéricas quedan:

$$H_{5.6k}(s) = \frac{2 + 2.24\times10^{-3}\,s}{3.136\times10^{-7}\,s^2 + 5.6\times10^{-4}\,s + 1}$$

$$H_{3.3k}(s) = \frac{2 + 1.32\times10^{-3}\,s}{1.089\times10^{-7}\,s^2 + 3.3\times10^{-4}\,s + 1}$$

> [!tip] Forma de la respuesta esperada
> Con $Q = 1$ y el cero en $f_o/2$, la magnitud arranca plana en $A = 2$ ($6\,\text{dB}$), **sube hasta un máximo de $\approx 4.5$** ($13.1\,\text{dB}$) cerca de $f_o$, y luego cae con pendiente asintótica de $-20\,\text{dB/déc}$. No es una respuesta monótona tipo Butterworth: el pico es inherente al diseño con $A = 2$.

---

## 5. Simulación en Multisim

Se simuló el circuito con $R_3 = R_4 = 5.6\,\text{k}\Omega$ y los valores medidos de los condensadores ($C_1 = 97.5\,\text{nF}$, $C_2 = 113.7\,\text{nF}$), con un barrido AC de $1\,\text{Hz}$ a $1\,\text{MHz}$ y $V_i = 1\,\text{V}$:

![[s14-le3-multisim-esquema.png]]
*Esquema en Multisim: LM741 alimentado con ±12 V, sondas PR1 (Vi) y PR2 (Vo), $R_3 = R_4 = 5.6\,\text{k}\Omega$.*

![[s14-le3-multisim-bode.png]]
*AC Sweep: banda de paso en $6\,\text{dB}$ ($A_v = 2$), pico de resonancia de $12.4\,\text{dB}$ cerca de $250\,\text{Hz}$ y caída posterior, con la fase bajando hacia −90°.*

Valores representativos exportados del Grapher (`Lab3 - Filtro 2026 (1).csv`):

| $f$ [Hz] | 10 | 100 | 251 | 284 | 500 | 1 k | 10 k | 100 k |
| -------- | -- | --- | --- | --- | --- | --- | ---- | ----- |
| $\|V_o/V_i\|$ sim | 2.01 | 2.62 | **4.18** | 4.02 | 2.45 | 1.12 | 0.108 | 0.0108 |

La simulación reproduce la respuesta teórica de la sección 4 para $R = 5.6\,\text{k}\Omega$: pico de $4.18$ ($12.4\,\text{dB}$) en $251\,\text{Hz}$ frente a los $4.50$ ($13.1\,\text{dB}$) en $269\,\text{Hz}$ del cálculo ideal. La pequeña diferencia (−7 % en amplitud) proviene de que $C_1 \neq C_2$ en el esquema ($97.5$ vs $113.7\,\text{nF}$, valores medidos) y del modelo real del LM741, mientras que el cálculo asume condensadores idénticos de $0.1\,\mu\text{F}$ y OPAMP ideal.

> [!warning] Error detectado y corregido en la primera simulación
> La primera versión del esquema tenía la resistencia de realimentación positiva capturada como $R_4 = 5.608\,\Omega$ (ohmios) en lugar de $5.6\,\text{k}\Omega$ — un error de unidad al digitar el valor. Con $R_4 \approx 0$ el nodo intermedio queda conectado casi directamente a la salida y la respuesta degenera a un **primer orden sin pico**, $H(s) \approx \frac{2}{1 - sRC}$, con fase en adelanto (imposible en un pasa bajo de fase mínima):
>
> ![[s14-le3-multisim-bode-error-r4.png]]
> *AC Sweep de la primera simulación (con $R_4 = 5.608\,\Omega$): respuesta de primer orden, sin pico de resonancia.*
>
> El diagnóstico se verificó resolviendo numéricamente las ecuaciones de nodos con los valores exactos del esquema erróneo: el resultado coincide dígito a dígito con el CSV original (p. ej., en $1\,\text{kHz}$: modelo $0.5600$ vs CSV $0.5601$). Tras corregir $R_4$, el AC Sweep mostró el pico de resonancia esperado.

---

## 6. Datos experimentales

### 6.1. Montaje

![[s14-le3-protoboard.png]]
*Montaje del filtro en protoboard: LM741, resistencias de 10 kΩ y condensadores cerámicos 104 (0.1 µF).*

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

La respuesta medida reproduce la forma predicha por la teoría: banda de paso con $A_v \approx 2.1$, **pico de resonancia $A_v \approx 4.4$ alrededor de $450\,\text{Hz}$** y caída posterior de $\approx -20\,\text{dB/déc}$ (entre 1 kHz y 10 kHz la ganancia cae un factor $\approx 9.2$ por década).

---

## 7. Comparación teórico vs. experimental (Entregable 1)

El pico medido ($A_v = 4.36$ en $\approx 450\,\text{Hz}$) **no** coincide con la predicción para $R = 5.6\,\text{k}\Omega$ (pico en $269\,\text{Hz}$), pero calza casi exactamente con la predicción para $R = 3.3\,\text{k}\Omega$ (pico de $4.50$ en $456\,\text{Hz}$) — la resistencia del circuito del fundamento y del material del alumno. La tabla compara las mediciones contra ambos casos teóricos y contra la simulación:

| $F$ [Hz] | $A_v$ teórico ($5.6\,\text{k}\Omega$) | $A_v$ simulado | $A_v$ **experimental** | $A_v$ teórico ($3.3\,\text{k}\Omega$) | Dif. exp. vs. teo. $3.3\,\text{k}$ |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 50 | 2.15 | 2.16 | **2.09** | 2.05 | +1.8 % |
| 100 | 2.59 | 2.62 | **2.25** | 2.21 | +1.8 % |
| 150 | 3.25 | 3.28 | **2.49** | 2.47 | +0.8 % |
| 200 | 3.99 | 3.90 | **2.83** | 2.81 | +0.9 % |
| 250 | 4.46 | 4.17 | **3.19** | 3.21 | −0.7 % |
| 300 | 4.40 | 3.94 | **3.59** | 3.66 | −1.8 % |
| 350 | 3.98 | 3.56 | **3.96** | 4.07 | −2.7 % |
| 400 | 3.48 | 3.14 | **4.24** | 4.37 | −3.1 % |
| 450 | 3.04 | 2.77 | **4.36** | 4.50 | −3.0 % |
| 500 | 2.67 | 2.45 | **4.31** | 4.43 | −2.7 % |
| 1 k | 1.19 | 1.12 | **2.25** | 2.19 | +2.8 % |
| 2 k | 0.58 | 0.55 | **1.08** | 1.00 | +7.6 % |
| 5 k | 0.23 | 0.22 | **0.44** | 0.39 | +13.4 % |
| 10 k | 0.11 | 0.11 | **0.245** | 0.19 | +26.8 % |

### Razones de las diferencias

1. **Valor efectivo de la red RC ($R = 3.3\,\text{k}\Omega$).** La respuesta medida se ajusta al 1–3 % (hasta 1 kHz) a la curva teórica con $R = 3.3\,\text{k}\Omega$ ($f_o = 482\,\text{Hz}$), no a la de $5.6\,\text{k}\Omega$ ($f_o = 284\,\text{Hz}$). Esto indica que el montaje físico se armó con las resistencias de $3.3\,\text{k}\Omega$ que la guía lista como "material que trae el alumno" (y que aparecen como $R = 3\text{K}3$ en el circuito del fundamento). Es la razón dominante del corrimiento de todo el eje de frecuencias en un factor $\approx 5.6/3.3 = 1.7$.
2. **Coherencia teoría–simulación.** Con $R_4$ ya corregida (ver sección 5), la simulación sigue la curva teórica de $5.6\,\text{k}\Omega$ dentro de un 7 %: la columna "simulado" difiere de la experimental por la misma razón que la teórica de $5.6\,\text{k}\Omega$ — el montaje físico usó otra $R$. La diferencia residual sim/teoría se debe a $C_1 \neq C_2$ ($97.5$ vs $113.7\,\text{nF}$) y al modelo real del LM741.
3. **Tolerancias de los componentes.** Los condensadores cerámicos 104 tienen tolerancias típicas de ±10–20 % (los valores medidos en el esquema, $97.5\,\text{nF}$ y $113.7\,\text{nF}$, difieren entre sí un 16 %). Con $C_1 \neq C_2$ el pico real se desplaza y se reduce ligeramente — consistente con el máximo medido de $4.36$ frente al teórico de $4.50$ (−3 %).
4. **Limitaciones del LM741 y de la medición en alta frecuencia.** Sobre 2 kHz la diferencia crece (hasta +27 % en 10 kHz) porque: la salida es ya muy pequeña ($0.49\,\text{V}_{pp}$) y la lectura de $V_{pp}$ en el osciloscopio incluye ruido y rizado (sesgo hacia arriba); el producto ganancia–ancho de banda finito del 741 ($\approx 1\,\text{MHz}$) y su impedancia de salida modifican la respuesta lejos de $f_o$; y los errores porcentuales se amplifican al dividir números pequeños.
5. **Ganancia de banda de paso.** En 50 Hz se midió $A_v = 2.09$ vs. $2.0$ teórico (+4.5 %): tolerancia de $R_1, R_2$ (±5 %) y resolución de lectura del generador ($V_{i,pp} = 2.04\,\text{V}$ reales según el osciloscopio, no 2.00 V exactos).

---

## 8. Diagramas de Bode (Entregable 2)

![[s14-le3-bode-comparacion.png]]
*Diagrama de Bode de $H(s)$: curvas teóricas para $R = 5.6\,\text{k}\Omega$ (azul) y $R = 3.3\,\text{k}\Omega$ (rojo), barrido AC de Multisim corregido (verde, se superpone a la curva azul) y puntos experimentales (negro). Las mediciones caen sobre la curva de $3.3\,\text{k}\Omega$.*

Código MATLAB que genera los diagramas de Bode de la función de transferencia teórica:

```matlab
% Filtro activo pasa bajo Sallen-Key con A = 2 (Q = 1)
A = 2;  C = 0.1e-6;
R1 = 5600;   % valor nominal del procedimiento (y de la simulacion)
R2 = 3300;   % valor del circuito del fundamento (material del alumno)

H1 = tf(A*[2*R1*C 1], [(R1*C)^2 (3-A)*R1*C 1]);
H2 = tf(A*[2*R2*C 1], [(R2*C)^2 (3-A)*R2*C 1]);

figure;
bode(H1, 'b', H2, 'r', {2*pi*10, 2*pi*1e5});  grid on;
legend('R = 5.6 k\Omega  (f_o = 284 Hz)', 'R = 3.3 k\Omega  (f_o = 482 Hz)');
title('Filtro activo pasa bajo — H(s) = A(1+2RCs)/(R^2C^2s^2+(3-A)RCs+1)');

% Verificacion de parametros
damp(H1)              % wn = 1786 rad/s, zeta = 0.5
allmargin(H1)
[mag,~,w] = bode(H2); % pico: max(mag) = 4.50 en w = 2*pi*456 rad/s
```

Lectura del diagrama:

- **Banda de paso:** $6.02\,\text{dB}$ ($A_v = 2$) en ambas curvas.
- **Pico de resonancia:** $+13.06\,\text{dB}$ ($A_v = 4.50$) en $269\,\text{Hz}$ ($5.6\,\text{k}\Omega$) o $456\,\text{Hz}$ ($3.3\,\text{k}\Omega$), consecuencia de $Q = 1$ y del cero en $f_o/2$.
- **Alta frecuencia:** pendiente de $-20\,\text{dB/déc}$ (dos polos − un cero), verificada tanto en la simulación como en las mediciones.
- **Fase:** parte de $0°$, sube levemente por el cero y cae hacia $-90°$ en alta frecuencia (fase de red de fase mínima con exceso polo-cero de 1).

---

## 9. Conclusiones (Entregable 3)

- Se comprobó experimentalmente que el circuito se comporta como un **filtro activo pasa bajo de segundo orden**: banda de paso con ganancia $A_v \approx 2.1$ (teórico $A = 1 + R_2/R_1 = 2$), pico de resonancia y caída posterior de $\approx -20\,\text{dB/déc}$, tal como predice la función de transferencia $H(s)$ deducida en el marco teórico.
- Con $A = 2$ el factor de calidad vale $Q = 1$ ($\zeta = 0.5$), lo que produce un **sobrepico de ganancia** cerca de $f_o$: se midió $A_{v,max} = 4.36$ ($12.8\,\text{dB}$) frente a los $4.50$ ($13.1\,\text{dB}$) teóricos — un error de solo **3 %**. La respuesta de este filtro no es plana tipo Butterworth ($\zeta \approx 0.707$, que requeriría $A = 1.6$), y la práctica lo evidenció con claridad.
- La **posición del pico medido** ($\approx 450$–$500\,\text{Hz}$) identifica el valor efectivo de la red RC: las mediciones se ajustan al 1–3 % a la curva teórica con $R = 3.3\,\text{k}\Omega$ ($f_o = 482\,\text{Hz}$), lo que confirma que el montaje usó la resistencia de $3.3\,\text{k}\Omega$ del alumno y no la de $5.6\,\text{k}\Omega$ de la figura del procedimiento. La respuesta en frecuencia funciona así como método indirecto de verificación de componentes.
- La pendiente medida entre 1 kHz y 10 kHz ($\approx -19\,\text{dB/déc}$) confirma la presencia del **cero en el numerador** de $H(s)$: sin él, un segundo orden caería a $-40\,\text{dB/déc}$.
- La simulación resultó una lección en sí misma: en la primera versión, un **error de unidad** ($R_4 = 5.608\,\Omega$ en lugar de $\text{k}\Omega$) degeneró la respuesta simulada a primer orden y suprimió el pico. Contrastar la simulación contra el cálculo teórico permitió detectar el error, corregirlo y validar la versión final: el AC Sweep corregido reproduce la curva teórica de $5.6\,\text{k}\Omega$ con un pico de $4.18$ en $251\,\text{Hz}$ (−7 % respecto del ideal, por $C_1 \neq C_2$).
- El diagrama de Bode demostró ser la herramienta natural para **comparar teoría, simulación y experimento** en un solo gráfico, evidenciando de inmediato tanto el corrimiento de $f_o$ como la ausencia del pico en la simulación.

---

## 10. Recomendaciones

- **Medir y registrar** con multímetro los valores reales de todas las resistencias y condensadores antes del montaje, y usar esos valores (no los nominales) en el cálculo teórico y la simulación; la guía misma maneja dos valores de $R$ distintos (fundamento vs. procedimiento) y conviene fijar cuál se usa.
- **Validar la simulación contra el cálculo teórico** antes de darla por buena: revisar siempre las unidades ($\Omega$/k$\Omega$, nF/µF) al digitar valores en Multisim — un solo error de unidad en $R_4$ cambió el orden aparente del filtro, y solo el contraste con la teoría lo hizo evidente.
- **Densificar las mediciones alrededor de $f_o$** (p. ej. cada 25 Hz entre 350 y 550 Hz) para ubicar con precisión la frecuencia y amplitud del pico, y medir también la **fase** entre entrada y salida para completar el diagrama de Bode experimental.
- Usar condensadores de **poliéster o cerámicos NP0/C0G** de tolerancia conocida en la red RC (los electrolíticos de la lista de materiales no son adecuados para señal AC por su polaridad y tolerancia ±20 %).
- En alta frecuencia, medir $V_o$ con **promediado** o con la función de medición RMS del osciloscopio para reducir el sesgo del ruido cuando la señal es pequeña ($< 1\,\text{V}_{pp}$).
- Para trabajos con $f_o$ mayores o $Q$ altos, reemplazar el LM741 por un OPAMP de mayor producto ganancia–ancho de banda (TL072, TL081), ya que el 741 ($GBW \approx 1\,\text{MHz}$, $SR = 0.5\,\text{V}/\mu\text{s}$) empieza a limitar la respuesta.

---

## 11. Resumen de resultados

| Magnitud | Teórico ($R = 3.3\,\text{k}\Omega$, $C = 0.1\,\mu\text{F}$) | Experimental | Error |
| -------- | --------------------------------------------------------- | ------------ | ----- |
| Ganancia en banda de paso $A_v$ | $2.00$ ($6.0\,\text{dB}$) | $2.09$ ($6.4\,\text{dB}$) | $+4.5\,\%$ |
| Ganancia máxima $A_{v,max}$ | $4.50$ ($13.1\,\text{dB}$) | $4.36$ ($12.8\,\text{dB}$) | $-3.0\,\%$ |
| Frecuencia del pico $f_{pico}$ | $456\,\text{Hz}$ | $\approx 450\,\text{Hz}$ | $\approx -1\,\%$ |
| Pendiente en alta frecuencia | $-20\,\text{dB/déc}$ | $\approx -19\,\text{dB/déc}$ | — |
| Factor de calidad $Q$ | $1$ | $\approx 0.97$ (del pico medido) | $-3\,\%$ |

---

## Bibliografía

- Sedra, A. & Smith, K. (2015). *Microelectronic Circuits* (7.ª ed.). Oxford University Press. — Capítulo de filtros activos (topología Sallen-Key).
- Boylestad, R. & Nashelsky, L. (2017). *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos* (11.ª ed.). Pearson.
- Coughlin, R. F. & Driscoll, F. F. (1999). *Amplificadores operacionales y circuitos integrados lineales* (5.ª ed.). Prentice Hall.
- Texas Instruments. (2018). *LM741 Operational Amplifier — Datasheet* (SNOSC25D).
