---
title: Laboratorio LC2 - Regulación y eficiencia del transformador
curso: "[[Motores MOC]]"
unidad: 3
semana: 10
orden: 99
tipo: evaluacion
subtipo: laboratorio
tags:
  - curso/motores
  - tipo/evaluacion
  - subtipo/laboratorio
  - tema/laboratorio
  - tema/transformador-monofasico
  - tema/regulacion-transformador
  - tema/eficiencia-transformador
  - tema/perdidas-cobre
  - tema/perdidas-hierro
date: 2026-05-25
---

> [!info] Datos del laboratorio
> - **Tipo:** Laboratorio Calificado 2 (LC2) — Guía de laboratorio Nº 2
> - **Tema:** Regulación y eficiencia del transformador (monofásico)
> - **Modalidad:** Evaluación flexible (individual o grupal)
> - **Semana:** 10
> - **Software:** LVSIM (LabVolt)
> - **Entrega:** Lunes 1 de junio de 2026, 11:59 p.m. (apertura: lunes 25 de mayo, 12:00 a.m.) — vía plataforma virtual de aprendizaje.
> - **Indicaciones y rúbrica:** [[S10-98 Indicaciones y Rubrica - LC2 Laboratorio|S10-98 Indicaciones y Rúbrica LC2]]
> - **Guía oficial (PDF):** [s10-laboratorio-lc2-guia.pdf](attachments/s10-laboratorio-lc2-guia.pdf)

---

## Logro general de la unidad de aprendizaje

Al finalizar la unidad, el estudiante **analiza el comportamiento de las diferentes configuraciones de transformadores monofásicos y trifásicos** para su aplicación en los sistemas de energía eléctrica.

## Objetivos específicos de la práctica

- Entender el **funcionamiento de un Transformador Monofásico**.
- Conocer de manera experimental el **ensayo de Regulación**.
- Conocer de manera experimental el **ensayo de Eficiencia**.

## Materiales y equipos (en el software LVSIM)

| Descripción | Cantidad |
| --- | :-: |
| Puesto de trabajo | 1 |
| Carga resistiva **8311** | 1 |
| Transformador **8353** | 1 |
| Multímetro | 1 |
| Cables de conexión | 1 |
| Interfaz de adquisición de datos y de control **9063** | 1 |
| Fuente de alimentación **8221** | 1 |

---

## Fundamento

### 1. El transformador y su relación de transformación

El transformador es un dispositivo que permite **elevar o disminuir el voltaje** en un circuito por medio de un **campo magnético**, manteniendo una misma potencia. Su funcionamiento se basa en el principio de **inducción electromagnética**.

Para un **transformador ideal**, la tensión inducida en el secundario depende únicamente de la relación entre el número de espiras de los devanados:

$$a \;=\; \frac{n_1}{n_2} \;=\; \frac{V_1}{V_2}$$

Donde:
- $a$ = relación de transformación
- $n_1$, $n_2$ = espiras del primario y secundario
- $V_1$, $V_2$ = tensiones del primario y secundario

> [!info] Material de soporte
> Sustento teórico previo en [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real|S07-1: circuito equivalente del transformador]] y [[S08-3 Tema 02 - Determinación de la eficiencia y regulación de un transformador|S08-3: eficiencia y regulación]].

### 2. Regulación de tensión

Se define como la **diferencia entre los voltajes secundarios en vacío y a plena carga**, medidos en terminales, expresada como un **porcentaje del voltaje a plena carga**:

$$\text{Reg} \;=\; \frac{E_{2\,\text{vacío}} - E_{2\,\text{nominal}}}{E_{2\,\text{nominal}}} \times 100\%$$

Para el cálculo del voltaje en vacío se debe considerar el **factor de potencia de la carga**. Los efectos de la **rama de excitación** pueden ignorarse — solo las impedancias en serie del circuito equivalente importan para la regulación. La regulación depende tanto de la **magnitud** de estas impedancias como del **ángulo de fase** de la corriente.

> [!example] Por qué importa la regulación
> Los equipos eléctricos, electrónicos, motores y lámparas son **muy sensibles a cambios de tensión** que pueden causarles daños. Una "buena regulación" significa que la tensión secundaria varía poco entre vacío y plena carga; es esencial para dimensionar transformadores y líneas, y depende del tipo de carga (resistiva, inductiva, capacitiva).

### 3. Pérdidas en el transformador

Ninguna máquina trabaja sin pérdidas. En un transformador:

| Tipo de pérdida | Símbolo | Origen |
| --- | --- | --- |
| Pérdidas por corriente de Foucault | $P_F$ | Corrientes inducidas en el núcleo (efecto Joule) |
| Pérdidas por histéresis | $P_H$ | Ciclo de magnetización del hierro |
| Pérdidas en el cobre | $P_{Cu}$ | $I^2R$ en los devanados |

Las pérdidas por **Foucault** y por **histéresis** se agrupan como **pérdidas en el hierro** $P_{Fe}$:

$$P_{Fe} \;=\; P_F + P_H$$

Para reducir las pérdidas de Foucault los núcleos no son macizos sino **laminados** (chapas magnéticas delgadas, apiladas y aisladas entre sí).

### 4. Rendimiento (eficiencia) del transformador

**Método directo:**

$$\eta \;=\; \frac{P_2}{P_1} \times 100\%$$

Donde $P_2$ es la potencia cedida por el secundario y $P_1$ la absorbida por el primario.

**Método indirecto** (cuando el error de los vatímetros es comparable a $P_1 - P_2$):

$$\eta \;=\; \frac{P_u}{P_u + P_{Cu} + P_{Fe}}$$

Donde:
- $P_u$ = potencia útil entregada a la carga
- $P_{Cu}$ = pérdidas en el cobre
- $P_{Fe}$ = pérdidas en el hierro

---

## Procedimiento del laboratorio

### A. Funcionamiento del transformador

1. **Ingresa a LVSIM** con tu código de acceso. Configura el programa para **tensión nominal 220 V** y **frecuencia 50 Hz**.
2. Selecciona los módulos: Fuente de alimentación (8221), Transformador (8353), Interfaz de adquisición de datos y de control (9063), Carga resistiva (8311).
3. **Revisa las características nominales** del Módulo de Transformador 8353 (Imagen 1 de la guía) y completa la **Tabla 1**:

   **Tabla 1 — Características del transformador**

   | | Primario | | Secundario |
   | --- | --- | --- | --- |
   | $V_{1\text{-}2}$ | ___ | $V_{5\text{-}6}$ ($E_2\ \text{vacío}$) | ___ |
   | $A_{1\text{-}2}$ | ___ | $A_{5\text{-}6}$ | ___ |
   | $V_{3\text{-}4}$ | ___ | $V_{7\text{-}8}$ | ___ |
   | $A_{3\text{-}4}$ | ___ | $A_{7\text{-}8}$ | ___ |

   **Número de espiras por bobina:**

   | Bobina | Número de espiras |
   | --- | :-: |
   | 1-3 | 57 |
   | 3-4 | 285 |
   | 5-6 | 57 |
   | 7-8 | 285 |

4. **Calcula** la relación de voltajes ($A$) y de corrientes ($B$), y registra en la **Tabla 2**:

   $$A = \frac{V_{1\text{-}2}}{V_{5\text{-}6}} \qquad B = \frac{I_{5\text{-}6}}{I_{1\text{-}2}}$$

5. **Mide las resistencias internas** de los bobinados con el multímetro (Tabla 3): $R_{1\text{-}2}$, $R_{3\text{-}4}$, $R_{5\text{-}6}$, $R_{7\text{-}8}$ en Ω.

6. **Conexión** (Imagen 2 de la guía): transformador a fuente de alimentación AC y a la interfaz de adquisición. Carga resistiva $R_L$ en el secundario, con vatímetros $P_1, P_2$ y amperímetros $I_1, I_2$.

7. **Adquiere datos** variando la **carga resistiva** según la siguiente tabla (cuidado de **no exceder 1 A** en la bobina secundaria; tensión primaria ≤ 24 V):

   **Tabla 4 — Mediciones (12 cargas)**

   | $R_{\text{carga}}$ (Ω) | $E_1$ (V) | $I_1$ (A) | $E_2$ (V) | $I_2$ (A) | $P_1$ (W) | $P_2$ (W) | $P_{\text{pérd}} = P_1 - P_2$ |
   | :-: | --- | --- | --- | --- | --- | --- | --- |
   | 440 | | | | | | | |
   | 400 | | | | | | | |
   | 367 | | | | | | | |
   | 338 | | | | | | | |
   | 314 | | | | | | | |
   | 293 | | | | | | | |
   | 275 | | | | | | | |
   | 259 | | | | | | | |
   | 244 | | | | | | | |
   | 232 | | | | | | | |
   | 220 | | | | | | | |
   | 210 | | | | | | | |

   > [!tip] Selección de cargas (Apéndice C)
   > Los valores de $R_{\text{carga}}$ corresponden a combinaciones de interruptores del módulo **8311** en la columna **220/230 V, 50 Hz/60 Hz**. Ver Apéndice C de la guía (Tabla 1 de impedancia, Figura 45 de ubicación de los elementos).

### B. Regulación

8. Elige el valor de $R_{\text{carga}}$ que más se acerque a la **tensión nominal** del secundario.
9. Calcula:

   $$\text{Reg} = \frac{E_{2\,\text{vacío}} - E_{2\,\text{nominal}}}{E_{2\,\text{nominal}}} \times 100\%$$

### C. Eficiencia

10. Con los mismos valores nominales, calcula:

    $$\eta = \frac{P_2}{P_1} \times 100\%$$

11. Llena la **Tabla 5** con la regulación y eficiencia para todas las cargas:

   **Tabla 5 — Regulación y eficiencia por carga**

   | $R_{\text{carga}}$ (Ω) | Regulación (%) | Eficiencia (%) |
   | :-: | --- | --- |
   | 440 | | |
   | 400 | | |
   | 367 | | |
   | 338 | | |
   | 314 | | |
   | 293 | | |
   | 275 | | |
   | 259 | | |
   | 244 | | |
   | 232 | | |
   | 220 | | |
   | 210 | | |

12. **Conclusiones:** Redactar al menos **cuatro** conclusiones sobre valores obtenidos, experiencia desarrollada y dificultades.

---

## Entregables del informe

Estructura obligatoria del informe Word (Arial, interlineado 1.5):

1. **Carátula:** nombre, apellidos y código.
2. **Funcionamiento del transformador:**
   a. Tablas 1, 2 y 3 (valores nominales).
   b. Tablas 4 y 5 (mediciones, regulación y eficiencia).
   c. Imagen del esquema construido en LVSIM.
3. **Regulación y eficiencia del transformador:**
   a. Gráfico de **pérdidas** $P_{\text{pérd}}$ vs corriente secundaria $I_2$.
   b. Cálculo de la **regulación**: presentar el procedimiento.
   c. Gráfico de **eficiencia** $\eta$ vs $I_2$.
   d. Cálculo de la **eficiencia**: presentar el procedimiento.
   e. **Curva de regulación de tensión** $E_2$ vs $I_2$.
   f. Explicar por qué **la corriente en el primario no es cero en vacío**.
   g. Explicar por qué **la potencia activa en el primario no es cero** aunque no se suministra potencia a la carga.
4. **Conclusiones:** al menos **4 conclusiones** de la experiencia y los resultados obtenidos.

> [!warning] Preguntas conceptuales clave (3f y 3g)
> Ambas se responden con el **circuito equivalente del transformador real** (ver [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real|S07-1]]):
>
> - **(f)** En vacío sigue circulando una **corriente de excitación** $I_0$ por el primario (corriente magnetizante $I_m$ + corriente de pérdidas $I_w$), responsable de magnetizar el núcleo y suplir las pérdidas en el hierro.
> - **(g)** La potencia activa en vacío no es cero porque alimenta las **pérdidas en el hierro** (Foucault + histéresis) — son disipativas y constantes, independientes de la carga.

## Fuentes de información

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
- LabVolt Series (2013). *Relaciones de tensiones y corrientes*. En **Electricidad y Nuevas Energías – Transformadores de potencia monofásicos** (pp. 8-21). Quebec, Canadá: Festo Didactic. ISBN 978-2-89640-664-7.
- LabVolt Series (2013). *Apéndices*. En **Electricidad y Nuevas Energías – Circuitos ca monofásicos** (pp. 121-131). Quebec, Canadá: Festo Didactic. ISBN 978-2-89640-664-7.
