---
title: Informe LC1 - Circuito magnetico con nucleo ferromagnetico
curso: "[[Motores MOC]]"
unidad: 1
semana: 5
orden: 100
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/laboratorio
  - tema/informe
  - tema/circuito-magnetico
  - tema/transformador
date: 2026-04-26
---

> [!info] Documentos relacionados
> - [[S05-99 Laboratorio - LC1 Circuito magnetico con nucleo ferromagnetico|S05-99 Guía del laboratorio]]
> - [[S05-98 Indicaciones y Rubrica - LC1 Laboratorio|S05-98 Indicaciones y rúbrica]]
> - [[S05-1 Tema 01 - Perdidas magneticas en el nucleo|S05-1 Pérdidas magnéticas en el núcleo]] (teoría)
> - [[Formulario - Motores Eléctricos Estáticos y Rotativos|Formulario]]

> [!warning] Notas sobre el módulo en LVSIM
> - **El número de módulo "8221" indicado en la guía es errata**: 8221 corresponde al *Four-Pole Squirrel-Cage Induction Motor*. La fuente de alimentación correcta es **8821** (Power Supply de LabVolt).
> - **AC Network**: configurar a **220 V – 50 Hz** desde *Tools → Options*.
> - **Tensión nominal de la guía** (24 V) es a 60 Hz; al operar a 50 Hz se conserva la misma tensión por vuelta para no saturar el núcleo (la guía mantiene 24 V nominal).

---

## 1. Datos de partida

| Parámetro            | Esquema 1 | Esquema 2 |
| -------------------- | --------- | --------- |
| Tensión nominal $V$  | 24 V AC   | 48 V AC   |
| Número de espiras $N$ | 58        | 116       |
| Frecuencia $f$        | 50 Hz     | 50 Hz     |
| Pulsación $\omega = 2\pi f$ | 314,16 rad/s | 314,16 rad/s |
| Configuración        | 1 transformador 8353 | 2 transformadores 8353 en serie (primarios) |

---

## 2. Pre-cálculos teóricos

Se calculan los parámetros que dependen exclusivamente de $V$, $f$ y $N$ (independientes de mediciones).

### 2.1. Tensión por vuelta

$$\frac{V}{N} = \text{constante para ambos esquemas}$$

**Esquema 1:**
$$\frac{V_1}{N_1} = \frac{24}{58} = 0{,}4138 \text{ V/vuelta}$$

**Esquema 2:**
$$\frac{V_2}{N_2} = \frac{48}{116} = 0{,}4138 \text{ V/vuelta}$$

> [!success] Observación
> El cociente $V/N$ es idéntico en ambos esquemas. Esto es esperable: poner dos transformadores idénticos en serie duplica $V$ y $N$ proporcionalmente, manteniendo el mismo flujo por vuelta. Cada transformador en el esquema 2 ve los mismos 24 V que en el esquema 1.

### 2.2. Flujo magnético máximo

A partir de la ecuación fundamental del transformador:

$$V = 4{,}44 \cdot f \cdot N \cdot \phi_m \;\Rightarrow\; \phi_m = \frac{V}{4{,}44 \cdot f \cdot N}$$

**Esquema 1:**
$$\phi_{m,1} = \frac{24}{4{,}44 \times 50 \times 58} = \frac{24}{12\,876} = 1{,}864 \times 10^{-3} \text{ Wb}$$

$$\boxed{\phi_{m,1} \approx 1{,}864 \text{ mWb}}$$

**Esquema 2 (por transformador, ya que cada uno ve 24 V):**
$$\phi_{m,2} = \frac{24}{4{,}44 \times 50 \times 58} = 1{,}864 \times 10^{-3} \text{ Wb}$$

$$\boxed{\phi_{m,2} \approx 1{,}864 \text{ mWb (por transformador)}}$$

### 2.3. Densidad de flujo máxima

$$B_m = \frac{\phi_m}{A_{núcleo}}$$

> [!note] Área del núcleo
> El área efectiva del núcleo $A$ del transformador 8353 no aparece en la guía. Para un transformador EMS típico de bobinado bajo, $A \approx 8 - 13 \text{ cm}^2 = (0{,}8 - 1{,}3) \times 10^{-3} \text{ m}^2$.
>
> Asumiendo $A \approx 10 \text{ cm}^2$ como estimación:
> $$B_m \approx \frac{1{,}864 \times 10^{-3}}{10 \times 10^{-4}} \approx 1{,}86 \text{ T}$$
>
> *Verificar con datasheet del 8353 o medir directamente en LVSIM si está disponible.*

### 2.4. Resumen de pre-cálculos

| Parámetro                  | Esquema 1            | Esquema 2 (por trafo) | Esquema 2 (total)    |
| -------------------------- | -------------------- | ---------------------- | -------------------- |
| Tensión por vuelta $V/N$   | 0,4138 V/v           | 0,4138 V/v             | 0,4138 V/v           |
| Flujo máximo $\phi_m$      | 1,864 mWb            | 1,864 mWb              | 1,864 mWb*           |
| $B_m$ (con $A=10$ cm²)     | ≈ 1,86 T             | ≈ 1,86 T               | ≈ 1,86 T*            |
| Pulsación $\omega$         | 314,16 rad/s         | 314,16 rad/s           | 314,16 rad/s         |

\* El flujo es por núcleo; en serie cada núcleo opera independientemente con el mismo $\phi_m$.

---

## 3. Esquema 1 — Transformador único

### 3.1. Esquema del circuito

> [!todo] Insertar imagen
> Reemplazar con captura del esquema implementado en LVSIM (módulos 8821, 8353, 9063 cableados según [[S05-99 Laboratorio - LC1 Circuito magnetico con nucleo ferromagnetico|guía Imagen 3]]).
>
> `![[s05-lvsim-esquema1.png]]`

### 3.2. Procedimiento ejecutado

1. Configuración LVSIM: AC Network 220 V – 50 Hz (Tools → Options).
2. Módulos colocados: Power Supply **8821**, Transformador **8353**, DACI **9063**.
3. Cableado:
   - 8821 terminal **4** (AC variable hot) → 9063 **I1 (4 A)** entrada.
   - 9063 **I1 common** → 8353 terminal **1** (primario, 5 A side).
   - 8353 terminal **2** → 8821 terminal **N** (variable AC neutral).
   - 8353 terminales **1, 2** → 9063 **E1** (+, –) (voltímetro primario).
   - 8353 terminales **5, 6** → 9063 **E2** (+, –) (voltímetro secundario).
4. Metering: instrumentos **E1** (V), **E2** (V), **I1** (A) y **PQS1 = E1×I1** (W) habilitados.
5. Ajustar voltaje de 0 → 24 V con el knob de la 8821.
6. Anotar lecturas estables.

### 3.3. Tabla 1 — Parámetros del esquema 1

| Parámetro                                                  | Valor              |
| ---------------------------------------------------------- | ------------------ |
| Tensión nominal a 60 Hz (placa)                            | 24 V AC            |
| Número de vueltas del devanado primario del transformador  | 58                 |
| Resistencia del cobre de la bobina primaria $R_{Cu}$       | **[medir con ohmímetro]** Ω |
| Máxima tensión de la fuente variable (8821 AC variable)    | 220 V AC           |
| Frecuencia de la fuente variable                           | 50 Hz              |

### 3.4. Tabla 2 — Mediciones y cálculos del esquema 1

| Parámetro                          | Resultado / cálculo                          |
| ---------------------------------- | -------------------------------------------- |
| **Corriente $I_1$** (medida)       | **0,896 A** (M7)                             |
| **Voltaje $E_1$** (medido)         | **24,01 V** (M1)                             |
| **Voltaje $E_2$** (secundario)     | **119,7 V** (M2)                             |
| **Pérdidas en el núcleo $P_{Fe,1}$** | **7,857 W** (M13, PQS1.P)                  |
| **Impedancia $Z_1 = V/I$**         | **26,80 Ω**                                  |
| **Flujo máximo $\phi_m$**          | **1,865 × 10⁻³ Wb = 1,865 mWb**              |
| **Fuerza magnetomotriz $\mathcal{F}_1 = N \cdot I_1$** | **51,97 A·v**                  |
| **Reluctancia $\mathcal{R}_1 = \mathcal{F}/\phi_m$**   | **27 866 A·v/Wb ≈ 27,87 × 10³ A·v/Wb** |
| **Relación de transformación $a = V_2/V_1$**           | **4,99 ≈ 5:1** (step-up)              |
| **Potencia aparente $S_1 = V_1 \cdot I_1$** | **21,51 VA**                            |
| **Factor de potencia $\cos \varphi = P/S$** | **0,365** (carácter inductivo dominante) |
| **Potencia reactiva $Q_1 = \sqrt{S^2 - P^2}$** | **20,02 VAR**                        |

### 3.5. Desarrollo de fórmulas — Esquema 1

**Impedancia del primario:**
$$Z_1 = \frac{E_1}{I_1} = \frac{24{,}01}{0{,}896} = \boxed{26{,}80 \;\Omega}$$

**Fuerza magnetomotriz:**
$$\mathcal{F}_1 = N_1 \cdot I_1 = 58 \times 0{,}896 = \boxed{51{,}97 \;\text{A·vuelta}}$$

**Flujo máximo** (calculado a partir de $V_1$, $f$ y $N_1$):
$$\phi_{m,1} = \frac{V_1}{4{,}44 \cdot f \cdot N_1} = \frac{24{,}01}{4{,}44 \times 50 \times 58} = \boxed{1{,}865 \times 10^{-3} \;\text{Wb}}$$

> [!success] Coincidencia teórico vs medido
> El flujo máximo calculado a partir de la tensión medida (1,865 mWb) coincide con el pre-cálculo teórico (1,864 mWb). Esto valida directamente la **ecuación fundamental del transformador** $V = 4{,}44 \cdot f \cdot N \cdot \phi_m$ para condiciones del laboratorio.

**Reluctancia equivalente del circuito magnético:**
$$\mathcal{R}_1 = \frac{\mathcal{F}_1}{\phi_{m,1}} = \frac{51{,}97}{1{,}865 \times 10^{-3}} = \boxed{27\,866 \;\text{A·v/Wb}}$$

**Relación de transformación** (medida a partir de $V_2$ en vacío):
$$a = \frac{V_2}{V_1} = \frac{119{,}7}{24{,}01} = \boxed{4{,}99 \approx 5{:}1}$$

Esto confirma que el transformador 8353 está conectado con el primario en su **lado de baja tensión / alta corriente** (terminales 1-2, 24 V/5 A, 58 vueltas) y el secundario en el **lado de alta tensión / baja corriente** (terminales 5-6, ~120 V/1 A, ~290 vueltas). Es la configuración solicitada por la guía.

**Análisis de potencias** (descomposición $S = P + jQ$):

$$S_1 = V_1 \cdot I_1 = 24{,}01 \times 0{,}896 = 21{,}51 \;\text{VA}$$

$$P_{Fe,1} = 7{,}857 \;\text{W} \;\;\text{(medido)} \quad;\quad Q_1 = \sqrt{S_1^2 - P_{Fe,1}^2} = \sqrt{21{,}51^2 - 7{,}857^2} = 20{,}02 \;\text{VAR}$$

$$\cos \varphi_1 = \frac{P_{Fe,1}}{S_1} = \frac{7{,}857}{21{,}51} = 0{,}365$$

> [!info] Interpretación del bajo factor de potencia
> El $\cos \varphi \approx 0{,}37$ es típico en ensayo de **vacío**: la componente reactiva $Q$ (corriente de magnetización para crear el flujo) domina sobre la activa $P$ (pérdidas en el hierro). En carga el factor de potencia mejora porque la corriente activa aumenta proporcionalmente a la carga.

**Pérdidas en el núcleo** medidas directamente:
$$\boxed{P_{Fe,1} = 7{,}857 \;\text{W}}$$

Como el ensayo es en **vacío** (secundario abierto, $I_2 = 0$), prácticamente toda la potencia activa absorbida son pérdidas en el hierro (histéresis + Foucault). Las pérdidas en el cobre primario $I_1^2 \cdot R_{Cu}$ son pequeñas y se pueden estimar una vez medido $R_{Cu}$ con el ohmímetro.

---

## 4. Esquema 2 — Dos transformadores en serie

### 4.1. Esquema del circuito

> [!todo] Insertar imagen
> Reemplazar con captura del esquema implementado en LVSIM (dos transformadores 8353 con primarios en serie, alimentados a 48 V).
>
> `![[s05-lvsim-esquema2.png]]`

### 4.2. Procedimiento ejecutado

1. Mantener la configuración 220 V – 50 Hz.
2. Agregar un segundo transformador **8353** a la workstation.
3. Cablear con primarios **en serie**:
   - 8821 terminal **4** → 9063 **I1 (4 A)**.
   - 9063 **I1 common** → 8353 (#1) terminal **1**.
   - 8353 (#1) terminal **2** → 8353 (#2) terminal **1** (conexión serie).
   - 8353 (#2) terminal **2** → 8821 terminal **N**.
   - Voltímetro **E1** sobre todo el conjunto serie (de la entrada al primario #1, salida del primario #2).
   - Voltímetro **E2** sobre uno de los secundarios (terminales 5–6 del trafo #1).
4. Ajustar voltaje a **48 V**.

### 4.3. Tabla 3 — Parámetros del esquema 2

| Parámetro                                                  | Valor              |
| ---------------------------------------------------------- | ------------------ |
| Tensión nominal a 60 Hz (placa, total serie)               | 48 V AC            |
| Número de vueltas del devanado primario total              | 116 (= 58 + 58)    |
| Resistencia del cobre de la bobina primaria $R_{Cu}$       | **[medir]** ≈ 2 × $R_{Cu,1}$ Ω |
| Máxima tensión de la fuente variable                       | 220 V AC           |
| Frecuencia de la fuente variable                           | 50 Hz              |

### 4.4. Tabla 4 — Mediciones y cálculos del esquema 2

| Parámetro                          | Resultado / cálculo                          |
| ---------------------------------- | -------------------------------------------- |
| **Corriente $I_2$** (medida)       | **0,894 A** (M7) — prácticamente igual a $I_1$ del esquema 1 |
| **Voltaje $E_1$ total** (medido)   | **47,97 V** (M1) — ≈ 2 × $V_1$ del esquema 1 |
| **Voltaje $E_2$** (secundario de un trafo) | **119,6 V** (M2) — ≈ igual al esquema 1 |
| **Pérdidas en el núcleo $P_{Fe,2}$ totales** | **15,65 W** (M13) — ≈ 2 × $P_{Fe,1}$ |
| **Impedancia $Z_2 = V/I$**         | **53,66 Ω** (≈ 2 · $Z_1$)                    |
| **Flujo máximo $\phi_m$ (por trafo)** | **1,864 × 10⁻³ Wb** (igual al esquema 1)  |
| **Fuerza magnetomotriz total $\mathcal{F}_2 = N_{total} \cdot I_2$** | **103,7 A·v** (≈ 2 · $\mathcal{F}_1$) |
| **Reluctancia equivalente $\mathcal{R}_{eq,2}$** | **55 632 A·v/Wb** (≈ 2 · $\mathcal{R}_1$)  |
| **Potencia aparente $S_2$**        | **42,88 VA**                                 |
| **Factor de potencia $\cos \varphi_2$** | **0,365** (idéntico al esquema 1)        |
| **Potencia reactiva $Q_2$**        | **39,92 VAR** (≈ 2 · $Q_1$)                  |

### 4.5. Desarrollo de fórmulas — Esquema 2

**Impedancia total (dos transformadores idénticos en serie):**
$$Z_2 = \frac{E_{1,total}}{I_2} = \frac{48}{I_2} \;[\Omega]$$

Si los transformadores son idénticos: $Z_2 = 2 \cdot Z_1$

**FMM total** (suma de FMMs por estar en serie las bobinas, alimentando núcleos magnéticamente independientes):
$$\mathcal{F}_2 = N_{total} \cdot I_2 = 116 \cdot I_2 \;[\text{A} \cdot \text{vuelta}]$$

**Flujo máximo en cada núcleo:**
$$\phi_{m,2} = \frac{V_{por\ trafo}}{4{,}44 \cdot f \cdot N_{por\ trafo}} = \frac{24}{4{,}44 \cdot 50 \cdot 58} = 1{,}864 \times 10^{-3} \text{ Wb}$$

**Reluctancia equivalente del circuito serie:**

Para dos circuitos magnéticos idénticos *independientes* alimentados desde una FMM común (caso de dos transformadores físicamente separados con primarios en serie):
$$\mathcal{R}_{eq} = \frac{\mathcal{F}_2}{\phi_{m,2}} = \frac{116 \cdot I_2}{1{,}864 \times 10^{-3}} \;[\text{A} \cdot \text{v/Wb}]$$

**Pérdidas totales:**
$$P_{Fe,2} \approx 2 \cdot P_{Fe,1}$$
(suma de pérdidas en ambos núcleos, ambos operando al mismo punto de inducción $B_m$)

---

## 5. Análisis de resultados

### 5.1. Comparación esquema 1 vs esquema 2

| Variable                 | Esquema 1   | Esquema 2  | Relación esperada | Relación observada |
| ------------------------ | ----------- | ---------- | ----------------- | ------------------ |
| Tensión alimentación $V$ | 24,01 V     | 47,97 V    | 2:1               | **2,00:1** ✓       |
| Corriente $I$            | 0,896 A     | 0,894 A    | ≈ 1:1             | **1,00:1** ✓       |
| Pérdidas $P_{Fe}$        | 7,857 W     | 15,65 W    | ≈ 1:2             | **1,99:1** ✓       |
| Tensión secundario $E_2$ | 119,7 V     | 119,6 V    | 1:1               | **1,00:1** ✓       |
| Flujo máximo $\phi_m$    | 1,865 mWb   | 1,864 mWb  | 1:1               | **1,00:1** ✓       |
| Impedancia $Z$           | 26,80 Ω     | 53,66 Ω    | 1:2               | **2,00:1** ✓       |
| FMM total $\mathcal{F}$  | 51,97 A·v   | 103,7 A·v  | 1:2               | **2,00:1** ✓       |
| Reluctancia eq. $\mathcal{R}$ | 27 866 A·v/Wb | 55 632 A·v/Wb | 1:2  | **2,00:1** ✓       |
| Factor de potencia $\cos \varphi$ | 0,365 | 0,365 | 1:1               | **1,00:1** ✓       |

> [!success] Las relaciones experimentales coinciden con las teóricas en todos los parámetros — el modelo de transformador se valida.

### 5.2. Discusión

> [!todo] Redactar análisis (mínimo 1 hoja según rúbrica) abordando

- **Diferencias entre valores calculados y medidos**: comentar errores experimentales (resistencia de bobinado, no-linealidad del núcleo, saturación si $B_m$ se acerca a 1,8 T).
- **Comportamiento del flujo**: el flujo máximo por núcleo se mantiene constante porque la tensión por vuelta es la misma; esto valida la ecuación $V = 4{,}44 f N \phi_m$.
- **Pérdidas**: aproximadamente se duplican porque hay dos núcleos disipando.
- **Impedancia**: se duplica porque las inductancias en serie se suman.
- **Saturación**: comentar si $B_m$ teórico (≈ 1,86 T) está cerca de la saturación del acero al silicio (típica $B_{sat} \approx 2{,}0$ T) y si esto produce una corriente de magnetización con armónicos.
- **Comparación con teoría** [[S05-1 Tema 01 - Perdidas magneticas en el nucleo|S05-1]]: las pérdidas medidas son la suma $P_H + P_F$ (histéresis + Foucault). A 50 Hz fija, dependen de $B_m^\alpha$ (Steinmetz) para histéresis y $B_m^2$ para Foucault.

---

## 6. Conclusiones

> [!todo] Redactar 4 conclusiones que aborden los 4 aspectos requeridos por la [[S05-98 Indicaciones y Rubrica - LC1 Laboratorio|rúbrica]]

### Conclusión 1 — El esquema final del circuito magnético

*Plantilla:*
> El esquema implementado en LVSIM (Power Supply 8821 → DACI 9063 → Transformador 8353) reproduce correctamente el circuito magnético descrito en la Imagen 3 de la guía. Las mediciones de $E_1$, $E_2$, $I_1$ y $P_{Fe}$ son consistentes con el modelo del reactor con núcleo de hierro, validando la ecuación fundamental $V = 4{,}44 \cdot f \cdot N \cdot \phi_m$ con un flujo máximo de **1,864 mWb** en ambos esquemas (porque la tensión por vuelta se mantiene en 0,4138 V/v).

### Conclusión 2 — Fallas identificadas en el esquema

*Plantilla — completar con observaciones reales:*
> Durante la implementación se identificó que el módulo etiquetado como "8221" en la guía es en realidad el **Power Supply 8821** (el 8221 es un motor de inducción de jaula de ardilla). Esta errata se corrigió usando el módulo correcto. Adicionalmente, se observó que [agregar otras fallas: lecturas inestables, calentamiento, conexiones que requirieron ajuste, etc.].

### Conclusión 3 — Uso del software LVSIM

*Plantilla:*
> LVSIM-EMS provee una réplica fiel de la estación de trabajo física LabVolt. La interfaz de arrastrar-y-soltar permite armar el circuito en minutos. La sub-ventana **Metering** con los instrumentos $E_1$, $E_2$, $I_1$ y $PQS_1 = E_1 \cdot I_1$ habilita la lectura simultánea de tensión, corriente y potencia activa. La configuración de red AC a **220 V – 50 Hz** desde *Tools → Options* es indispensable antes de cualquier medición para reproducir las condiciones del laboratorio peruano.

### Conclusión 4 — Dificultades experimentadas

*Plantilla:*
> Las dificultades principales fueron: (i) interpretar correctamente las erratas de numeración de módulos en la guía (8221 vs 8821); (ii) elegir los terminales correctos del transformador 8353 (lado de 5 A para el primario de 24 V, ya que es el devanado de baja tensión / alta corriente); (iii) ajustar el knob de tensión variable lentamente para evitar transitorios; (iv) [agregar otras dificultades].

---

## 7. Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5ta. ed.). McGraw-Hill Interamericana.
- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6ta. ed.). McGraw-Hill Interamericana.
- LabVolt Series (2013). *Relaciones de tensiones y corrientes*. En *Electricidad y Nuevas Energías – Transformadores de potencia monofásicos* (pp. 8-21). Québec, Canadá: Festo Didactic. ISBN 978-2-89640-664-7.
