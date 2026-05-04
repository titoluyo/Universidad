---
title: "Informe de Laboratorio Calificado N° 1"
subtitle: "Circuito magnético con núcleo ferromagnético"
author: "[Nombre y código del estudiante]"
date: "Abril 2026"
lang: es
---

# Informe LC1 — Circuito magnético con núcleo ferromagnético

**Curso:** Máquinas Eléctricas Estáticas y Rotativas  
**Sección:** EL51  
**Ciclo:** 2026-1  
**Estudiante:** [Apellidos, Nombres — Código]  
**Fecha:** Abril 2026  
**Software:** LVSIM-EMS (LabVolt / Festo Didactic)

---

## 1. Introducción

El presente informe documenta la implementación y análisis de un circuito magnético con núcleo ferromagnético usando el software de simulación LVSIM-EMS. Se construyeron dos esquemas:

- **Esquema 1:** un transformador monofásico LabVolt 8353 alimentado en su devanado primario de 24 V (lado de 5 A) con secundario en vacío.
- **Esquema 2:** dos transformadores LabVolt 8353 con primarios conectados en serie, alimentados a 48 V, con secundarios en vacío.

Para cada esquema se midieron las variables eléctricas en el primario (tensión, corriente, potencia activa) y la tensión inducida en el secundario, y se calcularon los parámetros derivados: impedancia, flujo magnético máximo, fuerza magnetomotriz, reluctancia equivalente y factor de potencia.

## 2. Marco teórico

### 2.1. Ecuación fundamental del transformador

Aplicando la Ley de Faraday a un núcleo ferromagnético excitado con una tensión sinusoidal $v(t) = \sqrt{2} \cdot V \cdot \cos(\omega t)$, despreciando la caída resistiva del bobinado, se obtiene:

$$V = \frac{2\pi}{\sqrt{2}} \cdot f \cdot N \cdot \phi_m = 4{,}44 \cdot f \cdot N \cdot \phi_m$$

donde $V$ es el valor eficaz de la tensión aplicada, $f$ la frecuencia, $N$ el número de espiras y $\phi_m$ el flujo magnético máximo en el núcleo.

### 2.2. Ley de Hopkinson

La relación entre flujo, fuerza magnetomotriz y reluctancia es análoga a la Ley de Ohm:

$$\phi = \frac{\mathcal{F}}{\mathcal{R}}$$

donde $\mathcal{F} = N \cdot I$ es la fuerza magnetomotriz y $\mathcal{R}$ la reluctancia del circuito magnético.

### 2.3. Pérdidas en el núcleo

En condiciones de vacío, la potencia activa absorbida corresponde principalmente a las pérdidas en el hierro:

$$P_{Fe} = P_H + P_F = k_H \cdot f \cdot B_m^{\alpha} \cdot vol + k_F \cdot f^2 \cdot B_m^2 \cdot a^2 \cdot \sigma \cdot vol$$

donde $P_H$ son las pérdidas por histéresis (con $\alpha \approx 1{,}6$ para acero al silicio) y $P_F$ las pérdidas por corrientes de Foucault.

## 3. Materiales y configuración

| Módulo                                                      | Cantidad | Función                                          |
| ----------------------------------------------------------- | -------- | ------------------------------------------------ |
| Power Supply 8821                                           | 1        | Fuente AC variable 0–220 V (terminales 4–N)      |
| Single-Phase Transformer 8353                               | 2        | Transformador monofásico (primario 24 V/5 A, secundario 120 V/1 A) |
| Data Acquisition and Control Interface (DACI) 9063          | 1        | Voltímetros E1, E2 + amperímetro I1 + vatímetro PQS1 |

**Configuración LVSIM:**

- Red AC: **220 V — 50 Hz** (Tools → Options)
- Sistema de unidades: **SI**
- Frecuencia fundamental de muestreo: 50,00 Hz

## 4. Pre-cálculos teóricos

A partir de los datos de placa ($V$, $f$, $N$) se obtienen las magnitudes que dependen únicamente del régimen senoidal aplicado, sin necesidad de mediciones.

### 4.1. Tensión por vuelta

$$\frac{V}{N}_{esq.\,1} = \frac{24}{58} = 0{,}4138 \;\text{V/vuelta}$$

$$\frac{V}{N}_{esq.\,2} = \frac{48}{116} = 0{,}4138 \;\text{V/vuelta}$$

Idéntica en ambos esquemas: cada núcleo opera al mismo flujo por vuelta.

### 4.2. Flujo magnético máximo

$$\phi_m = \frac{V}{4{,}44 \cdot f \cdot N} = \frac{24}{4{,}44 \times 50 \times 58} = 1{,}864 \times 10^{-3} \;\text{Wb} = 1{,}864 \;\text{mWb}$$

Este valor es el mismo en ambos esquemas (por núcleo), pues cada transformador del esquema 2 ve sólo 24 V en su primario.

## 5. Esquema 1 — Transformador único

### 5.1. Procedimiento

1. Configurar AC Network 220 V – 50 Hz desde *Tools → Options*.
2. Colocar los módulos 8821, 8353 y 9063 en la workstation.
3. Cablear según el esquema:
   - 8821 terminal 4 (AC variable hot) → DACI 9063 entrada I1 (4 A)
   - DACI 9063 I1 común → 8353 terminal 1 (primario, lado 5 A)
   - 8353 terminal 2 → 8821 terminal N (variable AC neutral)
   - Voltímetro E1 en paralelo con el primario (terminales 1 y 2)
   - Voltímetro E2 en paralelo con el secundario (terminales 5 y 6)
4. Desde *Aparatos de Medición*, habilitar M1=E1, M2=E2, M7=I1 y M13=PQS1 (potencia activa P, watts).
5. Establecer la tensión de la fuente a 0 V, energizar el módulo 8821 y subir lentamente el voltaje hasta 24 V. Si se dispara el breaker, presionar REINICIAR.
6. Anotar las lecturas estables.

### 5.2. Parámetros del transformador (Tabla 1)

| Parámetro                                                  | Valor              |
| ---------------------------------------------------------- | ------------------ |
| Tensión nominal a 60 Hz (placa)                            | 24 V AC            |
| Número de vueltas del devanado primario                    | 58                 |
| Máxima tensión de la fuente variable (8821)                | 220 V AC           |
| Frecuencia de la fuente variable                           | 50 Hz              |

### 5.3. Mediciones y cálculos (Tabla 2)

| Parámetro                                       | Valor                       |
| ----------------------------------------------- | --------------------------- |
| Corriente primario $I_1$ (medida)               | **0,896 A**                 |
| Tensión primario $E_1$ (medida)                 | **24,01 V**                 |
| Tensión secundario $E_2$ (medida)               | **119,7 V**                 |
| Pérdidas en el núcleo $P_{Fe,1}$ (medida)       | **7,857 W**                 |
| Impedancia primaria $Z_1 = E_1 / I_1$           | **26,80 Ω**                 |
| Flujo máximo $\phi_m$ (calculado)               | **1,865 × 10⁻³ Wb**         |
| Fuerza magnetomotriz $\mathcal{F}_1 = N \cdot I_1$ | **51,97 A·v**            |
| Reluctancia $\mathcal{R}_1 = \mathcal{F}_1 / \phi_m$ | **27 866 A·v/Wb**      |
| Relación de transformación $a = E_2 / E_1$      | **4,99 ≈ 5:1**              |
| Potencia aparente $S_1 = E_1 \cdot I_1$         | **21,51 VA**                |
| Factor de potencia $\cos \varphi$               | **0,365**                   |
| Potencia reactiva $Q_1$                         | **20,02 VAR**               |

### 5.4. Desarrollo de cálculos

**Impedancia del primario:**

$$Z_1 = \frac{E_1}{I_1} = \frac{24{,}01}{0{,}896} = 26{,}80 \;\Omega$$

**Fuerza magnetomotriz:**

$$\mathcal{F}_1 = N_1 \cdot I_1 = 58 \times 0{,}896 = 51{,}97 \;\text{A·vuelta}$$

**Flujo máximo (a partir de la tensión medida):**

$$\phi_{m,1} = \frac{E_1}{4{,}44 \cdot f \cdot N_1} = \frac{24{,}01}{4{,}44 \times 50 \times 58} = 1{,}865 \times 10^{-3} \;\text{Wb}$$

Este resultado coincide con el pre-cálculo teórico (1,864 mWb), validando la **ecuación fundamental del transformador**.

**Reluctancia del circuito magnético:**

$$\mathcal{R}_1 = \frac{\mathcal{F}_1}{\phi_{m,1}} = \frac{51{,}97}{1{,}865 \times 10^{-3}} = 27\,866 \;\text{A·v/Wb}$$

**Relación de transformación medida en vacío:**

$$a = \frac{E_2}{E_1} = \frac{119{,}7}{24{,}01} = 4{,}99 \approx 5{:}1$$

Confirma la conexión: primario en el lado de 5 A (24 V, 58 vueltas), secundario en el lado de 1 A (120 V, ≈ 290 vueltas).

**Análisis de potencias** (descomposición $S = P + jQ$):

$$S_1 = E_1 \cdot I_1 = 24{,}01 \times 0{,}896 = 21{,}51 \;\text{VA}$$

$$Q_1 = \sqrt{S_1^2 - P_{Fe,1}^2} = \sqrt{21{,}51^2 - 7{,}857^2} = 20{,}02 \;\text{VAR}$$

$$\cos \varphi_1 = \frac{P_{Fe,1}}{S_1} = \frac{7{,}857}{21{,}51} = 0{,}365$$

El bajo factor de potencia es típico del ensayo en vacío: la corriente de magnetización (componente reactiva $Q$) domina sobre la activa ($P$ = pérdidas en el hierro).

## 6. Esquema 2 — Dos transformadores en serie

### 6.1. Procedimiento

1. Mantener la configuración 220 V – 50 Hz.
2. Agregar un segundo transformador 8353 a la workstation.
3. Modificar el cableado para conectar los **primarios en serie**:
   - 8821 terminal 4 → 9063 I1 (4 A)
   - 9063 I1 común → 8353 #1 terminal 1
   - 8353 #1 terminal 2 → 8353 #2 terminal 1 (puente serie)
   - 8353 #2 terminal 2 → 8821 terminal N
   - Voltímetro E1 entre la entrada del primario #1 y la salida del primario #2 (mide la tensión total)
   - Voltímetro E2 sobre el secundario del trafo #1 (terminales 5–6)
4. Establecer la fuente a 0 V, energizar y subir gradualmente hasta 48 V.
5. Anotar las lecturas estables.

### 6.2. Parámetros del transformador (Tabla 3)

| Parámetro                                                  | Valor              |
| ---------------------------------------------------------- | ------------------ |
| Tensión nominal a 60 Hz (placa, total serie)               | 48 V AC            |
| Número de vueltas del devanado primario total              | 116 (= 58 + 58)    |
| Máxima tensión de la fuente variable                       | 220 V AC           |
| Frecuencia de la fuente variable                           | 50 Hz              |

### 6.3. Mediciones y cálculos (Tabla 4)

| Parámetro                                                | Valor                          |
| -------------------------------------------------------- | ------------------------------ |
| Corriente serie $I_2$ (medida)                           | **0,894 A**                    |
| Tensión total $E_1$ (medida)                             | **47,97 V**                    |
| Tensión secundario $E_2$ (medida, sobre un trafo)        | **119,6 V**                    |
| Pérdidas totales $P_{Fe,2}$ (medida)                     | **15,65 W**                    |
| Impedancia equivalente $Z_2 = E_1 / I_2$                 | **53,66 Ω**                    |
| Flujo máximo $\phi_m$ por núcleo (calculado)             | **1,864 × 10⁻³ Wb**            |
| Fuerza magnetomotriz total $\mathcal{F}_2 = N_T \cdot I_2$ | **103,7 A·v**                |
| Reluctancia equivalente $\mathcal{R}_{eq,2}$             | **55 632 A·v/Wb**              |
| Potencia aparente $S_2$                                  | **42,88 VA**                   |
| Factor de potencia $\cos \varphi$                        | **0,365**                      |
| Potencia reactiva $Q_2$                                  | **39,92 VAR**                  |

### 6.4. Desarrollo de cálculos

**Impedancia equivalente del primario serie:**

$$Z_2 = \frac{E_1}{I_2} = \frac{47{,}97}{0{,}894} = 53{,}66 \;\Omega \approx 2 \cdot Z_1$$

**FMM total** (con $N_{total} = 116$ vueltas):

$$\mathcal{F}_2 = N_{total} \cdot I_2 = 116 \times 0{,}894 = 103{,}7 \;\text{A·vuelta} \approx 2 \cdot \mathcal{F}_1$$

**Flujo máximo en cada núcleo** (cada trafo ve 24 V, igual al esquema 1):

$$\phi_{m,2} = \frac{V_{por\,trafo}}{4{,}44 \cdot f \cdot N_{por\,trafo}} = \frac{24}{4{,}44 \times 50 \times 58} = 1{,}864 \times 10^{-3} \;\text{Wb}$$

**Reluctancia equivalente** (dos núcleos magnéticamente independientes alimentados por una FMM compartida):

$$\mathcal{R}_{eq,2} = \frac{\mathcal{F}_2}{\phi_{m,2}} = \frac{103{,}7}{1{,}864 \times 10^{-3}} = 55\,632 \;\text{A·v/Wb} \approx 2 \cdot \mathcal{R}_1$$

**Análisis de potencias:**

$$S_2 = E_1 \cdot I_2 = 47{,}97 \times 0{,}894 = 42{,}88 \;\text{VA}$$

$$Q_2 = \sqrt{S_2^2 - P_{Fe,2}^2} = \sqrt{42{,}88^2 - 15{,}65^2} = 39{,}92 \;\text{VAR}$$

$$\cos \varphi_2 = \frac{P_{Fe,2}}{S_2} = \frac{15{,}65}{42{,}88} = 0{,}365$$

Las pérdidas totales se duplican respecto al esquema 1, confirmando que cada núcleo disipa lo mismo individualmente y se suman en paralelo eléctrico (suma de potencias en serie eléctrica).

## 7. Análisis de resultados

### 7.1. Comparación esquema 1 vs esquema 2

| Variable                          | Esquema 1   | Esquema 2  | Relación esperada | Relación observada |
| --------------------------------- | ----------- | ---------- | ----------------- | ------------------ |
| Tensión alimentación $V$          | 24,01 V     | 47,97 V    | 2:1               | 2,00:1             |
| Corriente $I$                     | 0,896 A     | 0,894 A    | ≈ 1:1             | 1,00:1             |
| Pérdidas $P_{Fe}$                 | 7,857 W     | 15,65 W    | ≈ 1:2             | 1,99:1             |
| Tensión secundario $E_2$          | 119,7 V     | 119,6 V    | 1:1               | 1,00:1             |
| Flujo máximo $\phi_m$ (por núcleo) | 1,865 mWb  | 1,864 mWb  | 1:1               | 1,00:1             |
| Impedancia $Z$                    | 26,80 Ω     | 53,66 Ω    | 1:2               | 2,00:1             |
| FMM total $\mathcal{F}$           | 51,97 A·v   | 103,7 A·v  | 1:2               | 2,00:1             |
| Reluctancia equiv. $\mathcal{R}$  | 27 866 A·v/Wb | 55 632 A·v/Wb | 1:2  | 2,00:1             |
| Factor de potencia $\cos \varphi$ | 0,365       | 0,365      | 1:1               | 1,00:1             |

Las relaciones experimentales **coinciden con las teóricas** en todos los parámetros, validando el modelo del transformador en vacío.

### 7.2. Discusión

**Conservación del flujo y la tensión por vuelta.** La igualdad $E_2$ = 119,7 V (esquema 1) ≈ 119,6 V (esquema 2) confirma que cada núcleo del esquema 2 opera al mismo punto de operación que el del esquema 1. Esto se sigue directamente de la ecuación fundamental: como $V/N$ es constante (0,4138 V/vuelta), el flujo por núcleo es invariante. La tensión inducida en cada secundario depende solo del flujo y del número de espiras del secundario, ambos invariantes.

**Duplicación de pérdidas e impedancia en serie.** Al conectar dos transformadores en serie, cada núcleo individual opera idénticamente al caso de un solo transformador, pero el circuito eléctrico ahora contiene dos veces los elementos disipativos y reactivos. Por eso $P_{Fe}$ y $Z$ se duplican mientras la corriente se mantiene. El factor de potencia, sin embargo, permanece constante (0,365) porque ambos transformadores operan en el mismo punto de la curva de magnetización.

**Validación de la ecuación fundamental.** El flujo máximo calculado a partir de $E_1$ medida (1,865 mWb) coincide con el calculado a partir de la tensión nominal (1,864 mWb) con un error inferior al 0,1 %. Esto valida directamente $V = 4{,}44 \cdot f \cdot N \cdot \phi_m$.

**Comportamiento del factor de potencia.** El bajo $\cos \varphi = 0{,}365$ es característico de un ensayo en vacío donde la corriente está dominada por la componente reactiva (corriente de magnetización para crear el flujo). En operación con carga, el factor de potencia mejora porque la componente activa de la corriente refleja la potencia transferida al secundario.

**Saturación del núcleo.** El flujo máximo de 1,864 mWb implica una densidad de flujo $B_m \approx 1{,}86$ T (suponiendo un área efectiva del núcleo de 10 cm²), valor cercano al codo de saturación del acero al silicio (típico $B_{sat} \approx 2{,}0$ T). Esto explica la corriente de excitación relativamente alta (0,896 A ≈ 18 % del rated de 5 A): el núcleo está operando en la zona no-lineal de la curva $B(H)$, donde pequeños incrementos de $B$ requieren incrementos grandes de $H$ (y por tanto de corriente).

**Pérdidas según teoría de Steinmetz y Foucault.** Las pérdidas medidas $P_{Fe}$ son la suma $P_H + P_F$. Como ambos esquemas operan a la misma frecuencia (50 Hz) y la misma densidad de flujo $B_m$, las pérdidas por unidad de volumen son idénticas. Las pérdidas totales se duplican exactamente porque hay dos núcleos disipando.

**Errores experimentales.** Las pequeñas discrepancias observadas (corriente 0,894 vs 0,896 A; tensión secundario 119,6 vs 119,7 V) están dentro del orden del 0,1 %, atribuibles a redondeo y a posibles diferencias mínimas entre los dos transformadores idealizados en LVSIM.

## 8. Conclusiones

1. **Esquema final del circuito magnético.** El circuito implementado en LVSIM (Power Supply 8821 → DACI 9063 → uno o dos transformadores 8353) reproduce fielmente el esquema descrito en la guía. Las mediciones de $E_1$, $E_2$, $I_1$ y $P_{Fe}$ son consistentes con la teoría del reactor con núcleo de hierro y validan la ecuación fundamental del transformador $V = 4{,}44 \cdot f \cdot N \cdot \phi_m$ con un flujo máximo medido de **1,865 mWb**, prácticamente idéntico al teórico (**1,864 mWb**).

2. **Fallas identificadas.** Durante la implementación se identificaron dos puntos a tener en cuenta. Primero, el módulo etiquetado como "8221" en la guía corresponde en realidad al motor de inducción jaula de ardilla; la **fuente de alimentación correcta es la 8821**. Segundo, durante el cableado los conductores deben hacer "snap" exacto sobre los terminales (círculos verdes al hover); de lo contrario el cable se ve dibujado pero no transmite señal y las mediciones quedan en cero. También se observó que al sobrepasar la tensión nominal del transformador, el breaker se dispara y debe reiniciarse con el botón **REINICIAR**.

3. **Uso del software.** LVSIM-EMS proporciona una réplica fiel de la estación física LabVolt. La configuración correcta de la red AC (220 V – 50 Hz) en *Tools → Options* es indispensable previo a las mediciones. La sub-ventana **Aparatos de medición** permite habilitar simultáneamente voltímetros (E1, E2), amperímetros (I1) y vatímetros (PQS1 = E1×I1 con modo P en watts), facilitando la medición instantánea de todas las variables eléctricas. Es importante activar manualmente el casillero "Encendido" en cada medidor PQS para que registre valores.

4. **Dificultades experimentadas.** Las principales dificultades fueron: (i) interpretar correctamente la nomenclatura de los módulos (8221 vs 8821); (ii) seleccionar los terminales correctos del transformador 8353 — el primario de 24 V está en el lado de 5 A (terminales 1-2) y el secundario en el lado de 1 A (terminales 5-6); (iii) confirmar que cada conductor hizo snap correcto sobre los terminales antes de energizar el circuito (verificable porque el voltímetro analógico de la fuente sí mostraba tensión pero los medidores digitales del DACI marcaban cero); (iv) ajustar el knob de tensión variable lentamente para evitar disparar el breaker.

## 9. Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5ta ed.). McGraw-Hill Interamericana.
- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6ta ed.). McGraw-Hill Interamericana.
- LabVolt Series (2013). *Relaciones de tensiones y corrientes*. En *Electricidad y Nuevas Energías – Transformadores de potencia monofásicos* (pp. 8–21). Québec, Canadá: Festo Didactic. ISBN 978-2-89640-664-7.
- LabVolt Series (2013). *Apéndices*. En *Electricidad y Nuevas Energías – Circuitos ca monofásicos* (pp. 121–131). Québec, Canadá: Festo Didactic. ISBN 978-2-89640-664-7.
