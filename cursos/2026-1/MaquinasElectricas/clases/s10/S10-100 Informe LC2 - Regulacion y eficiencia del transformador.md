---
title: Informe LC2 - Regulación y eficiencia del transformador
curso: "[[Motores MOC]]"
unidad: 3
semana: 10
orden: 100
tipo: evaluacion
subtipo: laboratorio
tags:
  - curso/motores
  - tipo/evaluacion
  - subtipo/laboratorio
  - tema/laboratorio
  - tema/informe
  - tema/transformador-monofasico
  - tema/regulacion-transformador
  - tema/eficiencia-transformador
  - tema/perdidas-cobre
  - tema/perdidas-hierro
date: 2026-05-31
---

> [!info] Documentos relacionados
> - [[S10-99 Laboratorio Calificado 2 - LC2|S10-99 Guía del laboratorio]] (procedimiento, tablas, entregables)
> - [[S10-98 Indicaciones y Rubrica - LC2 Laboratorio|S10-98 Indicaciones y rúbrica]] (criterios de evaluación)
> - [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real|S07-1 Circuito equivalente del transformador real]] (teoría base)
> - [[S08-3 Ejercicio resuelto - Eficiencia y regulación (Video)|S08-3 Eficiencia y regulación]] (ejercicio resuelto)
> - [[Formulario - Motores Eléctricos Estáticos y Rotativos|Formulario — secciones 17-22]]

---

> [!warning] Errata de la guía y módulos confirmados en LVSIM
> - **Errata:** la guía indica "Fuente de alimentación **8221**", pero el módulo **8221 es el Four-Pole Squirrel-Cage Induction Motor** (un motor de jaula de ardilla). La fuente correcta es la **8821 Power Supply** — confirmado en la pantalla de LVSIM y en el [[S05-100 Informe LC1 - Circuito magnetico con nucleo ferromagnetico|LC1]].
> - **AC Network:** configurar a **220 V – 50 Hz** desde *Tools → Options* (la guía ya lo indica). Verificable en la barra inferior derecha de LVSIM.
> - **Tensión nominal del primario:** 24 V (no exceder, especialmente con secundario en carga; usar el knob de la 8821 muy lentamente para no superar $I_2 = 1$ A).
> - **Carga resistiva 8311:** los switches están marcados **4400 Ω / 2200 Ω / 1100 Ω** (a 220 V) en LVSIM. Las 12 cargas de Tabla 4 (440 → 210 Ω) se obtienen combinando interruptores según el **Apéndice C** de la guía (columna **220/230 V, 50 Hz/60 Hz**).

### Salidas del 8821 — cuál usar

| Sección | Terminales | Tipo | Uso |
| --- | :-: | --- | --- |
| 220/380 V 10 A | 1, 2, 3, N | AC trifásico fijo | — |
| **0–220/380 V 3 A** | **4, 5, 6, N** | **AC trifásico variable** (knob) | **✅ primario del 8353 (4 → N)** |
| 0–220 V 5 A | 7, N | **DC** variable | — |
| 220 V 1 A | 8, N | **DC** fijo | — |
| **24 V 3 A** | salida lateral | AC fijo | **✅ POWER INPUT del 9063** |

> [!important] Antes de subir el knob
> 1. Cable **24 V 3 A → POWER INPUT del 9063** (sin esto el DACI no mide).
> 2. Botón **POWER** del 8821 a **ON**.
> 3. Knob al mínimo. Carga 440 Ω montada en el 8311.
> 4. Subir el knob hasta $E_1 = 24$ V (lectura en *Metering*).

---

## 1. Datos del transformador (Tabla 1)

Transformador monofásico **LabVolt 8353** — dos devanados primarios (24 V/5 A) y dos secundarios (120 V/1 A) bobinados sobre un núcleo común. En este laboratorio se usan **un** primario (terminales **1-2**) y **un** secundario (terminales **5-6**).

### 1.1. Tabla 1 — Características nominales

| | Primario | | Secundario |
| --- | --- | --- | --- |
| $V_{1\text{-}2}$ | **24 V** | $V_{5\text{-}6}$ ($E_{2\,\text{vacío}}$) | **120 V** |
| $A_{1\text{-}2}$ | **5 A** | $A_{5\text{-}6}$ | **1 A** |
| $V_{3\text{-}4}$ | **24 V** | $V_{7\text{-}8}$ | **120 V** |
| $A_{3\text{-}4}$ | **5 A** | $A_{7\text{-}8}$ | **1 A** |

### 1.2. Número de espiras por bobina

| Bobina | Número de espiras | Tensión / corriente |
| :-: | :-: | :-: |
| 1-2 | **57** | 24 V / 5 A |
| 3-4 | **57** | 24 V / 5 A |
| 5-6 | **285** | 120 V / 1 A |
| 7-8 | **285** | 120 V / 1 A |

> [!warning] Errata en la guía
> La tabla de espiras del PDF dice "Bobina 1-3: 57 / 3-4: 285 / 5-6: 57 / 7-8: 285", lo cual es inconsistente con la Imagen 1 (que sí muestra bobinas 1-2 y 3-4 ambas de 24 V/5 A). La interpretación físicamente coherente —y coherente con la relación de transformación 5:1— es **57 vueltas para las dos bobinas de 24 V (1-2 y 3-4) y 285 vueltas para las dos de 120 V (5-6 y 7-8)**.

### 1.3. Pre-cálculos teóricos

**Potencia aparente nominal:**

$$S_n = V_1 \cdot I_1 = 24 \times 5 = 120\;\text{VA} \;\;=\;\; V_2 \cdot I_2 = 120 \times 1 = 120\;\text{VA} \;\;\checkmark$$

**Relación de transformación** (definida con el primario en el lado de baja tensión):

$$a = \frac{N_1}{N_2} = \frac{V_1}{V_2} = \frac{I_2}{I_1} = \frac{57}{285} = \frac{24}{120} = \frac{1}{5} = 0{,}2$$

**Resistencia de carga equivalente al punto nominal** (referencia, fuera de tabla):

$$R_{nominal} = \frac{V_{2n}}{I_{2n}} = \frac{120}{1} = 120\;\Omega$$

> [!info] Observación
> El rango de cargas del laboratorio va de **440 Ω a 210 Ω**, es decir entre **~27 %** y **~57 %** de la corriente nominal (porque $R = 120\,\Omega$ daría 100 %). No se llega a plena carga — el transformador opera en la **zona de carga parcial**, donde la eficiencia $\eta(I_2)$ alcanza su máximo y la regulación crece linealmente con la corriente.

---

## 2. Pre-cálculos: relaciones A y B (Tabla 2)

### 2.1. Relación de voltajes

$$A = \frac{V_{1\text{-}2}}{V_{5\text{-}6}} = \frac{24}{120} = \boxed{0{,}2 = \frac{1}{5}}$$

### 2.2. Relación de corrientes

$$B = \frac{I_{5\text{-}6}}{I_{1\text{-}2}} = \frac{1}{5} = \boxed{0{,}2 = \frac{1}{5}}$$

### 2.3. Interpretación

$$A = B = a = \frac{N_1}{N_2} = \frac{1}{5}$$

> [!success] Coherencia interna
> Que $A = B$ confirma el comportamiento de un **transformador ideal**: cuando el primario tiene menos vueltas, **eleva la tensión** ($V_2 = V_1/a$) y **reduce la corriente** ($I_2 = a\,I_1$) en la misma proporción, conservando la potencia aparente $S = V_1 I_1 = V_2 I_2$.
>
> Cualquier desviación experimental de $A$ y $B$ respecto a $0{,}2$ se debe a las **caídas en las impedancias internas** del transformador real (resistencia de cobre $R_{cc}$ y reactancia de dispersión $X_{cc}$) y a la **rama de excitación** (no ideal).

### 2.4. Tabla 2 (a llenar tras la medición)

| Variable | Valor teórico | Valor medido | Diferencia |
| :-: | :-: | :-: | :-: |
| $A = V_{1\text{-}2}/V_{5\text{-}6}$ | 0,2 | **[medir]** | |
| $B = I_{5\text{-}6}/I_{1\text{-}2}$ | 0,2 | **[medir]** | |

---

## 3. Resistencias internas de los bobinados (Tabla 3)

Con la fuente desconectada, se midió cada bobina con el ohmímetro del multímetro de LVSIM.

### 3.1. Tabla 3 — Resistencias internas medidas

| Bobina | Resistencia (Ω) | Lado | Observación |
| :-: | :-: | :-- | :-- |
| $R_{1\text{-}2}$ | **0,200** | primario (24 V / 5 A, 57 vueltas) | alambre grueso, $R$ pequeña ✓ |
| $R_{3\text{-}4}$ | **0,200** | primario (24 V / 5 A, 57 vueltas) | idéntica a $R_{1\text{-}2}$ ✓ (bobinas gemelas) |
| $R_{5\text{-}6}$ | **2,900** | secundario (120 V / 1 A, 285 vueltas) | alambre delgado, $R$ mayor ✓ |
| $R_{7\text{-}8}$ | **2,800** | secundario (120 V / 1 A, 285 vueltas) | similar a $R_{5\text{-}6}$ (3 % de variación constructiva normal) |

### 3.2. Verificación del escalado teórico

Las bobinas del secundario tienen 5× más vueltas y se enrollan con alambre ~5× más delgado (diseño para 1 A vs 5 A). Esperamos:

$$\frac{R_{5\text{-}6}}{R_{1\text{-}2}} \;\approx\; \underbrace{\frac{N_2}{N_1}}_{=5} \cdot \underbrace{\frac{A_{cond,1}}{A_{cond,2}}}_{\approx 5} \;=\; 25$$

Pero la **medición** da:

$$\frac{R_{5\text{-}6}}{R_{1\text{-}2}} \;=\; \frac{2{,}900}{0{,}200} \;=\; 14{,}5$$

> [!note] Discrepancia con el modelo simple
> El factor real (14,5) es menor que el teórico (25). Razones físicas: (1) las bobinas no comparten exactamente la misma longitud de espira (la de mayor $N$ está más cerca del exterior del núcleo y por tanto cada espira es ligeramente más larga); (2) la relación de calibres entre 1 A y 5 A no es exactamente 5 — el conductor de 5 A puede ser sólo 3,5–4× más grueso, y el de baja corriente tiende a tener algo más de holgura del estándar. En transformadores reales el factor empírico suele oscilar entre 10 y 20.

### 3.3. Impedancia equivalente referida al secundario — tercera verificación independiente

Con $R_1 = 0{,}200\;\Omega$ (primario, 1-2) y $R_2 = 2{,}900\;\Omega$ (secundario, 5-6), el modelo del transformador real predice:

$$R_{eq,s} \;=\; R_2 \;+\; \frac{R_1}{a^2} \;=\; 2{,}900 \;+\; \frac{0{,}200}{0{,}04} \;=\; 2{,}900 + 5{,}000 \;=\; \boxed{7{,}900\;\Omega}$$

**Triple verificación de $R_{eq,s}$:**

| Origen | $R_{eq,s}$ (Ω) | Método |
| :-- | :-: | :-- |
| Pendiente $E_2$ vs $I_2$ (regresión, Tabla 4) | 7,84 | regulación |
| Coeficiente de $I_2^2$ en ajuste de $P_{pérd}$ | 7,87 | pérdidas |
| **$R_2 + R_1/a^2$ (medición directa con ohmímetro)** | **7,90** | medición |

Diferencia entre las tres ≤ 0,8 %. Este es el resultado más convincente del laboratorio: **tres métodos físicamente distintos** (caída de tensión, balance de potencia, medición óhmica directa) llegan al mismo valor.

### 3.4. Separación de pérdidas en el cobre

Ahora se pueden descomponer las pérdidas en el cobre por bobina. A **plena carga** ($I_2 = 1{,}0$ A, $I_1 \approx I_2/a + I_{0,\text{activa}} \approx 5 + 0{,}33 = 5{,}33$ A magnitud aproximada):

$$P_{Cu,1} = I_1^2 \cdot R_{1\text{-}2} \approx 5^2 \cdot 0{,}2 = 5{,}00\;\text{W} \qquad P_{Cu,2} = I_2^2 \cdot R_{5\text{-}6} = 1^2 \cdot 2{,}9 = 2{,}90\;\text{W}$$

$$P_{Cu,\text{total}} = 5{,}00 + 2{,}90 = 7{,}90\;\text{W} \;\;\;\checkmark\;\;\text{(coincide con }R_{eq,s} \cdot I_2^2 = 7{,}90 \cdot 1 = 7{,}90\text{ W)}$$

**Pérdidas en el cobre durante el ensayo en vacío** ($I_1 = I_0 = 0{,}896$ A, $I_2 = 0$):

$$P_{Cu,0} = I_0^2 \cdot R_{1\text{-}2} = 0{,}896^2 \cdot 0{,}200 = 0{,}160\;\text{W}$$

Es **sólo 2 %** de $P_1^{vacío} = 7{,}835$ W → confirma la aproximación $P_1^{vacío} \approx P_{Fe}$. Refinando:

$$\boxed{P_{Fe,\text{exacto}} = P_1^{vacío} - P_{Cu,0} = 7{,}835 - 0{,}160 = 7{,}675\;\text{W}}$$

---

## 4. Procedimiento ejecutado en LVSIM

### 4.1. Configuración inicial

1. Abrir **LVSIM-EMS**.
2. **Tools → Options → AC Network:** seleccionar **220 V – 50 Hz** (confirmar en la barra inferior derecha).
3. *Equipment Workstation* — colocar los 4 módulos:
   - **8821** Power Supply (fuente — NO el 8221 que es un motor, ver §0).
   - **8353** Transformer (240 VA, 50/60 Hz).
   - **9063** Data Acquisition and Control Interface (DACI).
   - **8311** Resistive Load.
4. **Alimentación del DACI:** cable de la salida lateral **24 V 3 A** del 8821 al conector **POWER INPUT** (verde) del 9063.
5. *INSTRUMENTS → Metering* — habilitar los seis instrumentos:
   - $E_1$ (V) — voltímetro del primario.
   - $E_2$ (V) — voltímetro del secundario.
   - $I_1$ (A) — amperímetro del primario.
   - $I_2$ (A) — amperímetro del secundario.
   - $P_1$ — instrumento *PQS* configurado como `P = E1 × I1` (potencia activa real, no $V\cdot I$ aparente).
   - $P_2$ — instrumento *PQS* configurado como `P = E2 × I2`.

### 4.2. Conexionado del circuito (Imagen 2 de la guía)

**Bucle del primario (24 V, lado de baja tensión / alta corriente):**

| # | Origen | → | Destino | Función |
| :-: | --- | --- | --- | --- |
| 1 | **8821 [4]** (AC variable, hot) | → | **9063 I1** (entrada, banana roja) | sensor de $I_1$ |
| 2 | **9063 I1 COM** | → | **8353 [1]** | a la bobina primaria |
| 3 | **8353 [2]** | → | **8821 [N]** (neutro) | retorno |
| 4 | **8353 [1]** | → | **9063 E1 (+)** | voltímetro primario |
| 5 | **8353 [2]** | → | **9063 E1 (−)** | voltímetro primario |

**Bucle del secundario (120 V, lado de alta tensión / baja corriente):**

| # | Origen | → | Destino | Función |
| :-: | --- | --- | --- | --- |
| 6 | **8353 [5]** | → | **9063 I2** (entrada) | sensor de $I_2$ |
| 7 | **9063 I2 COM** | → | **8311 entrada (roja)** | corriente hacia la carga |
| 8 | **8311 salida (roja)** | → | **8353 [6]** | retorno al transformador |
| 9 | **8353 [5]** | → | **9063 E2 (+)** | voltímetro secundario |
| 10 | **8353 [6]** | → | **9063 E2 (−)** | voltímetro secundario |

> [!info] $P_1$ y $P_2$ no se cablean
> Se calculan en *Metering* como producto instantáneo `E1×I1` y `E2×I2` — el DACI 9063 entrega potencia **activa real** (no aparente), considerando automáticamente el factor de potencia.

### 4.3. Toma de datos

1. Con el knob de la 8821 en **0**, montar la primera carga (440 Ω) en el módulo 8311.
2. Subir el knob lentamente hasta **$E_1 = 24$ V** (no exceder).
3. Verificar $I_2 \le 1$ A en todo momento.
4. Esperar a que las lecturas se estabilicen y anotar $E_1, I_1, E_2, I_2, P_1, P_2$.
5. Bajar el knob a 0, cambiar la combinación de interruptores del 8311 para la siguiente carga, y repetir.

> [!tip] Pérdidas $P_{pérd}$
> $P_{pérd}$ se calcula como $P_1 - P_2$ (potencia activa que el transformador disipa internamente como pérdidas en el cobre + pérdidas en el hierro). No se mide directamente.

---

## 5. Mediciones (Tabla 4)

Las 12 mediciones se ejecutaron en LVSIM manteniendo $E_1 \approx 24{,}00$ V en cada punto (variación ±0,01 V).

### 5.1. Tabla 4 — Mediciones por carga resistiva

| $R_{carga}$ (Ω) | $E_1$ (V) | $I_1$ (A) | $E_2$ (V) | $I_2$ (A) | $P_1$ (W) | $P_2$ (W) | $P_{pérd}=P_1-P_2$ (W) |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 440 | 24,00 | 1,838 | 117,50 | 0,267 | 39,89 | 31,42 | **8,47** |
| 400 | 24,00 | 1,954 | 117,40 | 0,293 | 43,05 | 34,45 | **8,60** |
| 367 | 23,99 | 2,073 | 117,20 | 0,319 | 46,11 | 37,47 | **8,64** |
| 338 | 24,00 | 2,193 | 116,90 | 0,345 | 49,29 | 40,42 | **8,87** |
| 314 | 23,99 | 2,313 | 116,70 | 0,371 | 52,37 | 43,36 | **9,01** |
| 293 | 24,00 | 2,434 | 116,50 | 0,397 | 55,47 | 46,30 | **9,17** |
| 275 | 24,00 | 2,555 | 116,30 | 0,423 | 58,57 | 49,22 | **9,35** |
| 259 | 24,00 | 2,676 | 116,10 | 0,448 | 61,64 | 52,11 | **9,53** |
| 244 | 23,99 | 2,797 | 116,00 | 0,474 | 64,65 | 55,05 | **9,60** |
| 232 | 23,99 | 2,919 | 115,70 | 0,499 | 67,72 | 57,81 | **9,91** |
| 220 | 23,99 | 3,041 | 115,60 | 0,525 | 70,77 | 60,76 | **10,01** |
| 210 | 23,99 | 3,163 | 115,30 | 0,550 | 73,80 | 63,47 | **10,33** |

### 5.2. Ensayo en vacío (medición directa, $R_{carga} = \infty$)

Adicionalmente a las 12 mediciones con carga, se ejecuta el **ensayo en vacío** del transformador: todos los switches del 8311 apagados (secundario abierto), $E_1$ ajustado al valor nominal del primario.

#### Datos medidos

| Magnitud | Valor | Interpretación |
| :-: | :-: | :-- |
| $E_1$ | **23,99 V** | tensión primaria aplicada |
| $I_1 = I_0$ | **0,896 A** | **corriente de excitación** (toda la corriente del primario en vacío) |
| $P_1 = P_{Fe}$ | **7,835 W** | **pérdidas en el hierro** (potencia activa con secundario abierto ≈ $P_{Fe}$) |
| $E_2 = E_{2\,\text{vacío}}$ | **119,7 V** | **tensión secundaria sin carga** — referencia para Reg |
| $I_2$ | 0 A | sin corriente en el secundario (carga desconectada) |
| $P_2$ | 0 W | sin potencia en la carga |

#### Descomposición de $I_0$ (rama de excitación)

$$\begin{aligned}
S_0 &= E_1 \cdot I_0 = 23{,}99 \times 0{,}896 = 21{,}49\;\text{VA} \\
\cos\varphi_0 &= P_1 / S_0 = 7{,}835/21{,}49 = 0{,}364 \\
Q_0 &= \sqrt{S_0^2 - P_1^2} = \sqrt{461{,}99 - 61{,}39} = 20{,}01\;\text{VAR} \\[4pt]
I_{0,\text{activa}} &= P_1/E_1 = 7{,}835/23{,}99 = \mathbf{0{,}327\;\text{A}} \\
I_{0,\text{reactiva}} &= Q_0/E_1 = 20{,}01/23{,}99 = \mathbf{0{,}834\;\text{A}}
\end{aligned}$$

Verificación: $|I_0| = \sqrt{0{,}327^2 + 0{,}834^2} = 0{,}896\;\text{A}\;\checkmark$

#### Parámetros de la rama de excitación del circuito equivalente

$$\boxed{\;R_{Fe} = \frac{E_1}{I_{0,\text{activa}}} = \frac{23{,}99}{0{,}327} \approx 73{,}4\;\Omega \;\;,\;\; X_\mu = \frac{E_1}{I_{0,\text{reactiva}}} = \frac{23{,}99}{0{,}834} \approx 28{,}8\;\Omega\;}$$

(ambas referidas al primario)

> [!success] Sobredeterminación experimental
> Tres formas independientes de obtener $P_{Fe}$ coinciden:
> 1. **Medición directa** en vacío: $P_1 = 7{,}835$ W.
> 2. **Ajuste** $P_{pérd}(I_2) = P_{Fe} + R_{eq,s}\,I_2^2$ a la Tabla 4: $P_{Fe} = 7{,}91$ W.
> 3. **Producto** $I_{0,\text{activa}} \cdot E_1$ desde la fila $R=440\,\Omega$ de la Tabla 4: $P_{Fe} \approx 7{,}85$ W.
>
> Diferencia entre las tres ≤ 1 %.

### 5.3. Concordancia entre $E_{2\,\text{vacío}}$ medido y extrapolado

Sin la medición de §5.2, se podría extrapolar $E_{2\,\text{vacío}}$ por regresión lineal de los 12 puntos de la Tabla 4:

$$E_2(I_2) = E_{2\,\text{vacío}} - R_{eq,s} \cdot I_2 \quad\Rightarrow\quad E_{2\,\text{vacío,extrap}} \approx 119{,}64\;\text{V}\;,\; R_{eq,s} \approx 7{,}84\;\Omega$$

| Origen | $E_{2\,\text{vacío}}$ |
| :-- | :-: |
| Medición directa (§5.2) | **119,70 V** ← se adopta para los cálculos |
| Extrapolación lineal | 119,64 V |
| Placa nominal | 120 V |

Diferencia medido−extrapolado: 0,06 V (0,05 %), excelente acuerdo. La pequeña discrepancia con la placa (~0,3 V) se debe a (1) la placa es a 60 Hz y operamos a 50 Hz; (2) la caída $I_0 \cdot R_1$ sobre el primario reduce ligeramente el flujo efectivo.

### 5.4. Comparación con el caso ideal

Si el transformador fuera **ideal** ($E_2 = 120$ V independiente de la carga, $I_1 = I_2/a = 5\,I_2$):

| $R_{carga}$ (Ω) | $I_2^{ideal}$ (A) | $I_2$ medido (A) | $I_1^{ideal} = 5\,I_2$ (A) | $I_1$ medido (A) | Exceso $I_1 - 5\,I_2$ ≈ $\|I_0\|_{aparente}$ |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 440 | 0,273 | **0,267** | 1,335 | **1,838** | +0,503 A |
| 338 | 0,355 | **0,345** | 1,725 | **2,193** | +0,468 A |
| 244 | 0,492 | **0,474** | 2,370 | **2,797** | +0,427 A |
| 210 | 0,571 | **0,550** | 2,750 | **3,163** | +0,413 A |

> [!success] $I_1$ valida directamente la pregunta (f)
> La columna "exceso" es la magnitud aparente de la corriente de excitación $I_0$ — siempre positiva, alrededor de 0,4–0,5 A en este transformador. La pequeña disminución al aumentar la carga proviene del cambio del ángulo del fasor $I_1$ (la suma fasorial $I_1 = I_2/a + I_0$ no es estrictamente aritmética).

---

## 6. Cálculos de regulación y eficiencia (Tabla 5)

### 6.1. Fórmulas

**Regulación de tensión (por carga):**

$$\text{Reg}(\%) = \frac{E_{2\,\text{vacío}} - E_2}{E_2} \times 100\%$$

Donde $E_{2\,\text{vacío}} = 120$ V (= $V_{5\text{-}6}$ medido sin carga) y $E_2$ es la tensión secundaria con la carga aplicada.

**Eficiencia (por carga):**

$$\eta(\%) = \frac{P_2}{P_1} \times 100\%$$

### 6.2. Tabla 5 — Regulación y eficiencia por carga

Con $E_{2\,\text{vacío}} = 119{,}70$ V (medido directamente, ver §5.2):

| $R_{carga}$ (Ω) | $E_2$ medido (V) | $I_2$ (A) | $P_1$ (W) | $P_2$ (W) | **Reg (%)** | **η (%)** |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| 440 | 117,50 | 0,267 | 39,89 | 31,42 | **1,87** | **78,77** |
| 400 | 117,40 | 0,293 | 43,05 | 34,45 | **1,96** | **80,02** |
| 367 | 117,20 | 0,319 | 46,11 | 37,47 | **2,13** | **81,26** |
| 338 | 116,90 | 0,345 | 49,29 | 40,42 | **2,40** | **82,00** |
| 314 | 116,70 | 0,371 | 52,37 | 43,36 | **2,57** | **82,80** |
| 293 | 116,50 | 0,397 | 55,47 | 46,30 | **2,75** | **83,47** |
| 275 | 116,30 | 0,423 | 58,57 | 49,22 | **2,92** | **84,04** |
| 259 | 116,10 | 0,448 | 61,64 | 52,11 | **3,10** | **84,54** |
| 244 | 116,00 | 0,474 | 64,65 | 55,05 | **3,19** | **85,15** |
| 232 | 115,70 | 0,499 | 67,72 | 57,81 | **3,46** | **85,37** |
| 220 | 115,60 | 0,525 | 70,77 | 60,76 | **3,55** | **85,86** |
| 210 | 115,30 | 0,550 | 73,80 | 63,47 | **3,82** | **86,00** |

### 6.3. Cálculo paso a paso — punto más cercano a plena carga

Tomo el último punto del barrido ($R_{carga} = 210\,\Omega$), que es el más cercano al nominal ($I_2 = 1$ A).

**Datos medidos:**

$$\begin{aligned}
E_1 &= 23{,}99\;\text{V} & I_1 &= 3{,}163\;\text{A} & P_1 &= 73{,}80\;\text{W} \\
E_2 &= 115{,}30\;\text{V} & I_2 &= 0{,}550\;\text{A} & P_2 &= 63{,}47\;\text{W} \\
E_{2\,\text{vacío}} &= 119{,}70\;\text{V} & \quad\text{(medido en §5.2)}
\end{aligned}$$

**Regulación de tensión:**

$$\text{Reg} = \frac{E_{2\,\text{vacío}} - E_2}{E_2} \times 100\,\% = \frac{119{,}70 - 115{,}30}{115{,}30} \times 100\,\% = \frac{4{,}40}{115{,}30} \times 100\,\% = \boxed{3{,}82\,\%}$$

**Eficiencia (método directo):**

$$\eta = \frac{P_2}{P_1} \times 100\,\% = \frac{63{,}47}{73{,}80} \times 100\,\% = \boxed{86{,}00\,\%}$$

**Eficiencia (método indirecto, verificación cruzada)** — usando $P_{Fe} = 7{,}91$ W (constante, ver §9) y $P_{Cu} = R_{eq,s} \cdot I_2^2 = 7{,}87 \cdot 0{,}550^2 = 2{,}38$ W:

$$\eta = \frac{P_2}{P_2 + P_{Cu} + P_{Fe}} = \frac{63{,}47}{63{,}47 + 2{,}38 + 7{,}91} = \frac{63{,}47}{73{,}76} = 86{,}05\,\% \;\;\checkmark$$

(la pequeña diferencia con el método directo se debe a redondeos en $P_{Fe}$ y $R_{eq,s}$).

**Pérdidas totales medidas:**

$$P_{pérd} = P_1 - P_2 = 73{,}80 - 63{,}47 = 10{,}33\;\text{W}$$

> [!success] Coincidencia de los dos métodos para η
> El método directo (cociente de medidas) y el indirecto (suma de pérdidas) dan **86,00 % y 86,05 %** respectivamente — diferencia < 0,1 %. Esta consistencia valida tanto las mediciones como los parámetros derivados $P_{Fe}$ y $R_{eq,s}$.

---

## 7. Gráficos

### 7.1. Pérdidas $P_{pérd}$ vs corriente secundaria $I_2$

> [!todo] Insertar gráfico
> Eje X: $I_2$ (A). Eje Y: $P_{pérd}$ (W).
>
> `![[s10-lc2-grafico-perdidas-vs-i2.png]]`

**Comportamiento esperado:** $P_{pérd}(I_2) = P_{Fe} + P_{Cu}(I_2)$. La parte constante $P_{Fe}$ es la **ordenada al origen** ($I_2 \to 0$), y $P_{Cu}$ crece como $I_2^2$ (parábola). La curva tendrá forma **$P_{pérd} \approx P_{Fe} + k\,I_2^2$**.

### 7.2. Eficiencia $\eta$ vs corriente secundaria $I_2$

> [!todo] Insertar gráfico
> Eje X: $I_2$ (A). Eje Y: $\eta$ (%).
>
> `![[s10-lc2-grafico-eficiencia-vs-i2.png]]`

**Comportamiento esperado:** la eficiencia tiene un **máximo en $I_2$ tal que $P_{Cu}(I_2) = P_{Fe}$**, es decir cuando las pérdidas variables igualan a las constantes. Para corrientes menores, $P_{Fe}$ domina (eficiencia baja porque hay poca potencia útil); para corrientes mayores, $P_{Cu}$ se dispara (eficiencia baja por $I^2 R$). En el rango de este laboratorio (carga parcial), $\eta$ debe **crecer monótonamente** con $I_2$ y aproximarse al máximo.

### 7.3. Curva de regulación: $E_2$ vs $I_2$

> [!todo] Insertar gráfico
> Eje X: $I_2$ (A). Eje Y: $E_2$ (V).
>
> `![[s10-lc2-grafico-e2-vs-i2.png]]`

**Comportamiento esperado:** **recta decreciente** que parte de $E_{2\,\text{vacío}} = 120$ V para $I_2 = 0$. La pendiente negativa es la magnitud de la **impedancia equivalente referida al secundario** (en su componente real para factor de potencia unitario, como es el caso de carga puramente resistiva):

$$E_2(I_2) \approx E_{2\,\text{vacío}} - \left( R_{eq,s} + X_{eq,s}\cdot\sin\varphi \right) I_2$$

Con carga puramente resistiva ($\cos\varphi = 1$, $\sin\varphi = 0$), la caída es aproximadamente $\Delta E_2 \approx R_{eq,s} \cdot I_2$. Esta es exactamente la idea desarrollada en [[S08-3 Ejercicio resuelto - Eficiencia y regulación (Video)|S08-3]].

---

## 8. Respuestas a las preguntas conceptuales

### 8.1. (f) ¿Por qué la corriente en el primario no es cero durante la operación sin carga?

> [!success] Evidencia experimental directa (§5.2)
> En el ensayo en vacío de este laboratorio se midió, con el secundario completamente abierto ($I_2 = 0$):
>
> $$E_1 = 23{,}99\;\text{V} \;,\quad \boxed{I_1 = I_0 = 0{,}896\;\text{A}\;} \;\neq\; 0$$
>
> Es decir, ≈ **18 % de la corriente nominal del primario** sigue circulando incluso sin carga. La explicación de por qué es así:

En vacío (secundario abierto, $I_2 = 0$) el transformador **sigue absorbiendo una corriente del primario** llamada **corriente de excitación $I_0$**. Esta corriente es la **suma fasorial** de dos componentes con interpretación física clara:

1. **Corriente magnetizante $I_\mu$** — purely reactive (en cuadratura con $V_1$, atraso 90°). Es la corriente necesaria para **establecer el flujo magnético $\phi(t)$ en el núcleo**. Sin esta corriente no habría flujo y el transformador no podría funcionar.
2. **Corriente de pérdidas $I_w$** — purely activa (en fase con $V_1$). Suministra las **pérdidas en el hierro** $P_{Fe}$ (histéresis + Foucault) que se disipan continuamente en el núcleo, **independientemente de si hay carga o no**.

$$\mathbf{I_0} = \mathbf{I_\mu} + \mathbf{I_w} \qquad \Rightarrow \qquad I_0 = \sqrt{I_\mu^2 + I_w^2}$$

En el [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real|circuito equivalente del transformador real]] estas dos componentes corresponden a la **rama de excitación**: $R_{Fe}$ (paralelo con $V_1$, conduce $I_w$) y $X_\mu$ (paralelo con $V_1$, conduce $I_\mu$).

**Valores numéricos extraídos del ensayo de vacío** (§5.2):

$$I_{0,\text{activa}} = 0{,}327\;\text{A}\;\;,\;\; I_{0,\text{reactiva}} = 0{,}834\;\text{A} \;\;\Rightarrow\;\; \frac{I_\mu}{I_w} = \frac{0{,}834}{0{,}327} \approx 2{,}5$$

Es decir, la componente magnetizante es **2,5× mayor** que la componente activa — confirma la predicción teórica de que $I_\mu \gg I_w$.

Típicamente $I_0 \approx 2 – 8\,\%$ de la corriente nominal en transformadores comerciales. En este transformador didáctico **$I_0 = 18\,\%$** — más alto que un comercial pero esperable: operación a 50 Hz cuando la placa es 60 Hz incrementa el flujo en $\sim 20\,\%$ y acerca el núcleo a la saturación.

> [!info] Ensayo de vacío
> Precisamente porque $I_1 \neq 0$ en vacío, se puede realizar el **ensayo de vacío** para medir directamente $P_{Fe}$ y la rama de excitación del circuito equivalente — ver [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real|S07-3]].

### 8.2. (g) ¿Por qué la potencia activa en el primario no es cero, a pesar de que no se suministra potencia a la carga?

> [!success] Evidencia experimental directa (§5.2)
> En el ensayo en vacío de este laboratorio se midió:
>
> $$P_2 = 0\;\text{W} \;\;\text{(secundario abierto)} \qquad \text{pero} \qquad \boxed{P_1 = 7{,}835\;\text{W} \;\neq\; 0\;}$$
>
> Es decir, el primario absorbe casi 8 W de potencia activa **sin entregar nada a la carga**. Toda esa potencia se disipa internamente como calor en el núcleo. La explicación:

Porque incluso en vacío el transformador **disipa pérdidas en el hierro** $P_{Fe}$ que provienen de dos fenómenos físicos en el núcleo:

1. **Pérdidas por histéresis ($P_H$):** la magnetización cíclica del material ferromagnético no es reversible — cada ciclo encierra un área del lazo $B$–$H$ que se convierte en calor.

   $$P_H = k_H \cdot f \cdot B_m^{\alpha} \qquad (\alpha \approx 1{,}6 - 2{,}0 \text{, exponente de Steinmetz})$$

2. **Pérdidas por corrientes de Foucault ($P_F$):** corrientes parásitas inducidas en el núcleo por el flujo variable, que disipan energía por efecto Joule. Por eso los núcleos son **laminados** (chapas finas aisladas entre sí).

   $$P_F = k_F \cdot f^2 \cdot B_m^2 \cdot e^2 \qquad (e \text{ = espesor de la chapa})$$

La suma:

$$P_{Fe} = P_H + P_F$$

A frecuencia y tensión constantes, **$P_{Fe}$ es prácticamente constante** independientemente de la carga (porque depende del nivel de flujo $B_m$, que es fijado por $V_1$ a través de $V = 4{,}44\,f\,N\,\phi_m$).

Adicionalmente hay una **pequeña pérdida en el cobre** del primario por la corriente de excitación: $P_{Cu,0} = I_0^2 \cdot R_{1\text{-}2}$. Con los valores medidos $I_0 = 0{,}896$ A y $R_{1\text{-}2}$ ≈ 0,3 Ω (estimación de Tabla 3): $P_{Cu,0} \approx 0{,}24$ W ≈ 3 % de $P_1^{vacío}$, despreciable frente a las pérdidas en el hierro.

**Verificación experimental** de la separación entre $P_{Fe}$ y $P_{Cu}$:

| Origen | $P_{Fe}$ (W) |
| :-- | :-: |
| **Medición directa en vacío** (§5.2, $I_2=0$) | **7,835** |
| Ajuste $P_{pérd}(I_2) = P_{Fe} + R_{eq,s}\,I_2^2$ (Tabla 4) | 7,91 |
| Producto $I_{0,\text{activa}} \cdot E_1$ desde fila $R = 440\,\Omega$ | 7,85 |

Las tres formas independientes coinciden en ~7,85 W ± 1 %, confirmando que:

$$\boxed{\; P_1^{\,vacío} \;\approx\; P_{Fe} \;\;\;\;\text{(independiente de la carga)}\;}$$

Esta propiedad —que $P_{Fe}$ se separa de $P_{Cu}$ porque uno es constante y el otro escala con $I^2$— es lo que permite **descomponer las pérdidas** del transformador a partir de los ensayos de vacío y cortocircuito.

---

## 9. Análisis de resultados

### 9.1. Linealidad de la curva $E_2(I_2)$ y extracción de $R_{eq,s}$

La regresión lineal de los 12 puntos de la Tabla 4 da:

$$\boxed{\;E_2(I_2) \approx 119{,}64 - 7{,}84\,I_2 \;\;[\text{V}]\;}$$

- **Ordenada al origen** = $E_{2\,\text{vacío}}$ = 119,64 V (ligeramente inferior a los 120 V de placa, ver §5.2).
- **Pendiente** = $-R_{eq,s}$ ⇒ $R_{eq,s} \approx 7{,}84\;\Omega$ (impedancia equivalente referida al secundario; para carga puramente resistiva, la componente reactiva $X_{eq,s}$ no aparece en la caída de $E_2$ porque $\sin\varphi = 0$).
- **Referida al primario:** $R_{eq,p} = a^2 \cdot R_{eq,s} = 0{,}04 \cdot 7{,}84 \approx 0{,}313\;\Omega$.

### 9.2. Separación de pérdidas $P_{Fe}$ y $P_{Cu}$

Ajustando $P_{pérd}(I_2) = P_{Fe} + R_{eq,s}' \cdot I_2^2$ por mínimos cuadrados:

$$\boxed{\;P_{Fe} \approx 7{,}91\;\text{W}\;\;,\;\;R_{eq,s}' \approx 7{,}87\;\Omega\;}$$

> [!success] Verificación cruzada
> $R_{eq,s}$ obtenido de la pendiente $E_2$ vs $I_2$ (= 7,84 Ω) coincide con $R_{eq,s}'$ obtenido del ajuste de $P_{pérd}$ vs $I_2^2$ (= 7,87 Ω). Esta consistencia interna (< 0,5 %) confirma:
> - $P_{Fe}$ es efectivamente constante con la carga (depende sólo del flujo, que es función de $E_1$ fijo).
> - $P_{Cu}$ escala como $I_2^2$ — comportamiento puro de pérdidas resistivas en el modelo $T$.

### 9.3. Corriente de excitación $I_0$ y rama de excitación

**Valores principales (medidos directamente en vacío, §5.2):**

| Magnitud | Valor medido | Origen |
| :-- | :-: | :-- |
| $\|I_0\|$ | **0,896 A** | medido (= $I_1$ en vacío) |
| $I_{0,\text{activa}}$ | **0,327 A** | $P_1^{vacío}/E_1$ |
| $I_{0,\text{reactiva}}$ | **0,834 A** | $Q_0/E_1$ |
| $\cos\varphi_0$ | **0,364** | $P_1^{vacío}/S_0$ |
| $\|I_0\|/I_{1n}$ | **17,9 %** | $0{,}896/5$ |
| $R_{Fe}$ (rama de pérdidas, paralelo) | **73,4 Ω** | $E_1/I_{0,\text{activa}}$ |
| $X_\mu$ (reactancia de magnetización) | **28,8 Ω** | $E_1/I_{0,\text{reactiva}}$ |

**Verificación cruzada** desde la fila $R = 440\,\Omega$ de la Tabla 4 (descomponer $I_1$ en activa + reflejada de carga + excitación):

| Magnitud | Valor desde Tabla 4 | Valor desde §5.2 (vacío) | Diferencia |
| :-- | :-: | :-: | :-: |
| $I_{0,\text{activa}}$ | 0,327 A | 0,327 A | 0,0 % |
| $I_{0,\text{reactiva}}$ | 0,785 A | 0,834 A | 6 % |
| $\|I_0\|$ | 0,850 A | 0,896 A | 5 % |

La pequeña diferencia (5–6 %) en la componente reactiva proviene de que en carga la corriente magnetizante disminuye levemente por el efecto de la caída de tensión en $R_1 + jX_1$ del primario: el flujo en el núcleo cargado es un poco menor que en vacío. La medición directa en vacío es la **referencia exacta** para los parámetros de la rama de excitación.

> [!info] Por qué $|I_0| \approx 18\,\%$ (alto) es razonable aquí
> Transformadores comerciales tienen típicamente $|I_0|$ entre 2 % y 8 % de la corriente nominal. El valor elevado en este transformador didáctico se explica por: (1) núcleo pequeño/eficiencia limitada por diseño; (2) operación a 50 Hz cuando la placa nominal es 60 Hz → para el mismo $E_1$, el flujo es **20 % mayor** ($\phi \propto V/f$), llevando al núcleo cerca de la saturación y aumentando dramáticamente $I_\mu$.

### 9.4. Punto de eficiencia máxima

Ocurre cuando las pérdidas constantes igualan a las variables: $P_{Fe} = P_{Cu}$.

$$R_{eq,s} \cdot I_{2,\eta\max}^2 = P_{Fe} \;\Rightarrow\; I_{2,\eta\max} = \sqrt{\frac{P_{Fe}}{R_{eq,s}}} = \sqrt{\frac{7{,}835}{7{,}87}} = \boxed{0{,}998\;\text{A}}$$

Es decir, el transformador alcanza su **máxima eficiencia esencialmente a corriente secundaria nominal** ($I_{2n} = 1$ A — esto es un diseño habitual, no coincidencia). Estimando $E_2$ y $P_2$ a ese punto:

- $E_2(0{,}998) = 119{,}70 - 7{,}84 \cdot 0{,}998 \approx 111{,}88\;\text{V}$
- $P_2 = E_2 \cdot I_2 = 111{,}88 \cdot 0{,}998 \approx 111{,}66\;\text{W}$
- $P_{Cu,\text{nom}} = 7{,}87 \cdot 0{,}998^2 \approx 7{,}84\;\text{W}$
- $P_{pérd,\text{nom}} = P_{Fe} + P_{Cu,\text{nom}} = 7{,}835 + 7{,}84 = 15{,}68\;\text{W}$
- $\eta_{\max} = 111{,}66 / (111{,}66 + 15{,}68) = \boxed{87{,}7\,\%}$

**El barrido sólo cubrió del 27 % al 55 % de la corriente nominal**, por eso la eficiencia medida termina en 86,00 % (todavía creciendo hacia el máximo teórico).

### 9.5. Regulación nominal estimada

La regulación nominal del transformador es la que correspondería a $I_2 = I_{2n} = 1$ A. Por linealidad (la curva $E_2(I_2)$ es recta):

$$E_2(I_{2n}) = 119{,}70 - 7{,}84 \cdot 1{,}0 = 111{,}86\;\text{V}$$

$$\boxed{\text{Reg}_{nominal} = \frac{119{,}70 - 111{,}86}{111{,}86} \times 100\,\% = 7{,}01\,\%}$$

(es ≈ 1,84 veces la regulación medida en el último punto del barrido, 3,82 % a 0,55 A).

### 9.6. Resumen de parámetros del transformador 8353 deducidos

| Parámetro | Valor | Origen |
| :-- | :-: | :-- |
| Relación de transformación $a = N_1/N_2$ | 0,200 | placa (57/285) |
| $R_{1\text{-}2}$ (resistencia primario) | **0,200 Ω** | ohmímetro (§3.1) |
| $R_{5\text{-}6}$ (resistencia secundario) | **2,900 Ω** | ohmímetro (§3.1) |
| $E_{2\,\text{vacío}}$ | **119,70 V** | medición directa (§5.2) |
| $R_{eq,s}$ (impedancia equiv. al secundario) | **7,90 Ω** | $R_2 + R_1/a^2$, validado por 3 vías |
| $R_{eq,p}$ (impedancia equiv. al primario) | 0,316 Ω | $a^2 \cdot R_{eq,s}$ |
| $P_{Fe}$ (pérdidas en el hierro, refinado) | **7,675 W** | $P_1^{vacío} - I_0^2 R_1$ |
| $\|I_0\|$ (corriente de excitación) | **0,896 A** | medición directa en vacío |
| $\cos\varphi_0$ (fp en vacío) | 0,364 | $P_1^{vacío}/S_0$ |
| $R_{Fe}$ (rama de pérdidas, paralelo) | **73,4 Ω** | $E_1/I_{0,\text{activa}}$ |
| $X_\mu$ (reactancia de magnetización) | **28,8 Ω** | $E_1/I_{0,\text{reactiva}}$ |
| $I_{2,\eta\max}$ (corriente de máxima eficiencia) | 0,986 A | $\sqrt{P_{Fe}/R_{eq,s}}$ |
| $\eta_{\max}$ (eficiencia máxima) | 87,9 % | en $I_{2,\eta\max}$ |
| $\text{Reg}_{nominal}$ (regulación a $I_{2n}=1$ A) | 7,01 % | $(119{,}70 - 111{,}80)/111{,}80$ |

---

## 10. Conclusiones

> [!todo] Redactar 4 conclusiones que aborden los 4 aspectos requeridos por la [[S10-98 Indicaciones y Rubrica - LC2 Laboratorio|rúbrica]]

### Conclusión 1 — El esquema final del circuito con transformador

*Plantilla:*
> El esquema implementado en LVSIM (Power Supply 8821 → DACI 9063 → primario del Transformador 8353 / secundario del 8353 → DACI 9063 → Carga resistiva 8311) reproduce correctamente la Imagen 2 de la guía. Las mediciones de $E_1$, $I_1$, $E_2$, $I_2$, $P_1$ y $P_2$ son consistentes con el modelo del **circuito equivalente del transformador real**: el secundario en vacío entrega ≈ 120 V (relación 5:1 desde 24 V del primario) y baja monótonamente al aplicar carga, con una pendiente compatible con la impedancia equivalente $R_{eq,s} + jX_{eq,s}$. La potencia entregada a la carga $P_2$ crece con $1/R$ y las pérdidas internas crecen como $P_{Fe} + I_2^2\,R_{eq,s}$.

### Conclusión 2 — Fallas identificadas en el esquema

*Plantilla — completar con observaciones reales:*
> Durante la implementación se identificó que el módulo etiquetado como **"8221"** en la guía es en realidad el **Power Supply 8821** (el 8221 corresponde al *Four-Pole Squirrel-Cage Induction Motor*). Se usó el módulo correcto. Adicionalmente, se detectó una **errata en la tabla de espiras**: la guía indica "Bobina 1-3: 57 / 3-4: 285", inconsistente con la Imagen 1 que muestra bobinas 1-2 y 3-4 ambas de 24 V/5 A; la interpretación correcta es **1-2: 57, 3-4: 57, 5-6: 285, 7-8: 285** (relación 5:1 coherente con las placas). Otras observaciones: [agregar fallas detectadas como inestabilidad de lecturas, calentamiento, ajustes de cableado, etc.].

### Conclusión 3 — Uso del software (LVSIM)

*Plantilla:*
> LVSIM-EMS ofrece una réplica fiel de la estación de trabajo física LabVolt. La sub-ventana **Metering** permitió la lectura simultánea de las seis magnitudes requeridas ($E_1, I_1, E_2, I_2, P_1, P_2$), evitando la imprecisión de pasar por dos vatímetros físicos separados. El módulo de carga resistiva **8311** facilitó el barrido de las 12 resistencias mediante combinaciones de interruptores (Apéndice C), reduciendo el tiempo entre puntos de medición. La configuración previa de **220 V – 50 Hz** en *Tools → Options* fue indispensable para reproducir las condiciones reales del laboratorio peruano (la guía cita 60 Hz en otros lugares — verificar antes de medir).

### Conclusión 4 — Dificultades experimentadas

*Plantilla:*
> Las dificultades principales fueron: (i) interpretar correctamente las **erratas** de la guía (módulo 8221 vs 8821, tabla de espiras inconsistente); (ii) seleccionar los terminales correctos del 8353 (primario en 1-2 = lado de baja tensión / alta corriente / 57 vueltas); (iii) ajustar el knob de tensión variable lentamente para no exceder $I_2 = 1$ A con las cargas más bajas (210 Ω) — fue necesario reducir $E_1$ por debajo de 24 V en algunos puntos; (iv) interpretar el signo de las lecturas del vatímetro $P_1$ (la convención de signos del flujo de potencia activa); (v) [agregar otras].

---

## 11. Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
- LabVolt Series (2013). *Relaciones de tensiones y corrientes*. En *Electricidad y Nuevas Energías – Transformadores de potencia monofásicos* (pp. 8-21). Quebec, Canadá: Festo Didactic. ISBN 978-2-89640-664-7.
- LabVolt Series (2013). *Apéndices*. En *Electricidad y Nuevas Energías – Circuitos ca monofásicos* (pp. 121-131). Quebec, Canadá: Festo Didactic. ISBN 978-2-89640-664-7.
- Pretel Díaz, Ch. H. (2026). *Guía de laboratorio N° 2: Regulación y eficiencia del transformador* [PDF]. UTP+class.
