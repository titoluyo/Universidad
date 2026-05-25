---
title: "Desarrollo PC2 - Práctica Calificada 2"
curso: "[[Motores MOC]]"
unidad: 2
semana: 9
orden: 100
tipo: evaluacion
subtipo: pc
tags:
  - curso/motores
  - tipo/evaluacion
  - subtipo/pc
  - tema/transformador-real
  - tema/ensayos
  - tema/transformador-trifasico
  - tema/circuito-equivalente
date: 2026-05-24
---

> [!info] Sobre este documento
> Desarrollo de la **PC2 — Práctica Calificada 2** (semana 9). Documento fuente: `attachments/s09_EXAMEN_DE_MAQUINAS_ELECTRICAS_2_SQOPWZ.docx`. Modalidad: subir el PDF resuelto en **Evaluaciones** y **Tareas**.
>
> Notas relacionadas: [[S09-99 Evaluación Semana 09 - PC2 Práctica Calificada 2|Metadatos PC2]] · [[S09-98 Indicaciones - Práctica Calificada 2|Indicaciones y rúbrica]].

## Datos de la evaluación

| Campo               | Valor                                                          |
| ------------------- | -------------------------------------------------------------- |
| Tipo                | Calificada — PC2 (10 % del ciclo)                              |
| Total de preguntas  | 4 (4 + 4 + 4 + 8 = 20 pts)                                    |
| Modalidad           | Subir PDF con desarrollo                                       |
| Trabajo             | Individual                                                     |
| Fecha límite        | Domingo 24 de mayo de 2026 — 23:59                            |

## Indicación del docente (encabezado)

> NOTA: Recuerda que el documento con la solución debe ser subido en **ambas secciones (el mismo documento)**, "Evaluaciones" y "Tareas", en formato **PDF**.

---

## Pregunta 1 — Material magnético para alta frecuencia (4 pts)

### Enunciado

¿Cuál de los siguientes materiales magnéticos se utilizaría si se quisiera fabricar un **transformador de alta frecuencia**?

- a) Ferroxcube
- b) Aceros Amorfos
- c) Núcleos de Ferrita
- d) Níquel-Hierro (Ni-Fe o Permalloy)
- e) Hierro-Silicio (Fe-Si)

### Referencia teórica

Ver [[S06-2 Tema 01 - Materiales magnéticos]] · [[S06-3 Tema 01 - Curvas experimentales de los materiales magnéticos]].

### Desarrollo

Para un **transformador de alta frecuencia** (kHz – MHz) el material del núcleo debe cumplir simultáneamente:

1. **Resistividad eléctrica muy alta**, para anular las pérdidas por **corrientes parásitas (Foucault)**, que crecen con $f^2$.
2. **Bajas pérdidas por histéresis** a esa frecuencia (lazo estrecho).
3. **Permeabilidad relativa elevada**, para reducir la sección requerida del núcleo.

Análisis por alternativa:

| Alternativa | Material | Aplicación típica | ¿Apto para alta frecuencia? |
| ----------- | -------- | ----------------- | --------------------------- |
| a) Ferroxcube | **Marca comercial** de ferritas (originalmente Philips). | HF, RF, fuentes conmutadas. | Es una **marca**, no el nombre genérico del material. |
| b) Aceros Amorfos (Metglas) | Aleaciones Fe-B-Si solidificadas rápidamente. | Transformadores de distribución 50/60 Hz, núcleos de bajas pérdidas. | Limitado a baja/media frecuencia. |
| c) **Núcleos de Ferrita** | Cerámicas ferromagnéticas (Mn-Zn, Ni-Zn) — son **aislantes eléctricos** (ρ ≫ metales). | **Transformadores HF**, fuentes conmutadas, RF, inductores. | **Sí — material por excelencia para HF**. |
| d) Níquel-Hierro (Permalloy) | Permeabilidad muy alta. | Audio, blindaje magnético, instrumentación. | Limitado por pérdidas a HF. |
| e) Hierro-Silicio (Fe-Si) | Acero al silicio laminado. | Transformadores y máquinas a 50/60 Hz. | No — pérdidas excesivas a HF. |

**Razonamiento del descarte de (a)**: aunque las ferritas comerciales se venden bajo marcas como "Ferroxcube", la opción técnicamente correcta y **académica** es el material genérico — **Ferrita** (c). Las ferritas son cerámicas Mn-Zn / Ni-Zn con resistividad de 10⁵–10⁸ Ω·m, lo que prácticamente elimina las corrientes de Foucault y permite operar de kHz hasta MHz.

### Resultado

$$\boxed{\text{c) Núcleos de Ferrita}}$$

---

## Pregunta 2 — Ensayos para determinar los parámetros del transformador (4 pts)

### Enunciado

¿Cuáles son los **ensayos esenciales** empleados en la práctica para establecer los **parámetros del circuito** de un transformador?

- a) Ensayo de vacío y ensayo de cortocircuito
- b) Ensayo de magnetismo y ensayo de eficiencia
- c) Ensayo de vacío, ensayo de cortocircuito y ensayo de magnetismo
- d) Ensayo de magnetismo y ensayo de cortocircuito
- e) Ensayo de magnetismo, ensayo de eficiencia y ensayo de vacío

### Referencia teórica

Ver [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real]] · [[S08-1 Tema 01 - Determinación de los parámetros del transformador]].

### Desarrollo

Los **dos ensayos canónicos** que se realizan en planta y laboratorio para obtener los **6 parámetros** del circuito equivalente del transformador real son:

**1. Ensayo en vacío** (sin carga, alimentado por el devanado de **baja tensión** a $V_n$):
- Mide $V_0$, $I_0$ y $P_0$.
- Permite calcular la **rama paralela de excitación** $R_{Fe}$ y $X_\mu$, y las **pérdidas en el hierro** $P_{Fe} \approx P_0$.
- La corriente de vacío $I_0$ es muy pequeña (1 – 5 % de $I_n$), por lo que las pérdidas en el cobre del primario son despreciables.

**2. Ensayo en cortocircuito** (secundario cortocircuitado, alimentado por el **lado de alta tensión** con baja tensión hasta circular $I_n$):
- Mide $V_{cc}$, $I_{cc}$ y $P_{cc}$.
- Permite calcular la **impedancia serie equivalente** $R_{cc}$ y $X_{cc}$, y las **pérdidas en el cobre** $P_{Cu} \approx P_{cc}$.
- La tensión $V_{cc}$ es muy pequeña (≈ 5 – 10 % de $V_n$), por lo que las pérdidas en el hierro son despreciables (el flujo es proporcional a $V$).

> **No existe un "ensayo de magnetismo"** como ensayo normado del transformador — el comportamiento magnético se infiere del ensayo en vacío. Por lo tanto, todas las alternativas que mencionan "ensayo de magnetismo" (b, c, d, e) son incorrectas o redundantes.

Análisis por alternativa:

| Alt | Composición | Veredicto |
| --- | ----------- | --------- |
| a)  | Vacío + cortocircuito | ✅ **Correcta** — son los dos esenciales y suficientes. |
| b)  | Magnetismo + eficiencia | ❌ "Magnetismo" no es un ensayo normado; "eficiencia" es un cálculo derivado, no un ensayo. |
| c)  | Vacío + cortocircuito + magnetismo | ❌ Incluye los dos correctos pero agrega "magnetismo" como tercero innecesario. |
| d)  | Magnetismo + cortocircuito | ❌ Reemplaza vacío por "magnetismo" inexistente. |
| e)  | Magnetismo + eficiencia + vacío | ❌ Mezcla, no incluye cortocircuito. |

### Resultado

$$\boxed{\text{a) Ensayo de vacío y ensayo de cortocircuito}}$$

---

## Pregunta 3 — Conexión incorrecta en banco trifásico (4 pts)

### Enunciado

¿Cuál es la opción de **conexión incorrecta** en un banco de un transformador trifásico?

- a) Estrella - Ye
- b) Ye - Delta
- c) Delta - Ye
- d) Ye – Ye – Ye
- e) Delta - Delta

### Referencia teórica

Ver [[S09-1 Tema 01 - El transformador trifásico]] · [[S09-3 Tema 02 - Circuito equivalente aproximado del transformador trifásico]].

### Desarrollo

Un **banco trifásico** se forma con **dos** devanados por columna o por unidad monofásica (primario y secundario). Las cuatro **conexiones básicas** posibles son las combinaciones de Estrella (Y, "ye") y Triángulo (Δ, "delta") en cada lado:

| Conexión | Notación |
| -------- | -------- |
| **Estrella – Estrella** | Y – Y |
| **Estrella – Triángulo** | Y – Δ |
| **Triángulo – Estrella** | Δ – Y |
| **Triángulo – Triángulo** | Δ – Δ |

Es decir, **un banco trifásico tiene exactamente dos lados (primario y secundario)**, no tres.

Análisis por alternativa:

| Alt | Notación | ¿Conexión válida de banco trifásico? |
| --- | -------- | ------------------------------------- |
| a) Estrella - Ye   | Y – Y (escrita con ambos sinónimos del símbolo Y) | ✅ Equivalente a Y – Y. |
| b) Ye - Delta      | Y – Δ | ✅ Conexión estándar. |
| c) Delta - Ye      | Δ – Y | ✅ Conexión estándar (la más usada para subir tensión). |
| d) **Ye – Ye – Ye** | **Y – Y – Y** (tres devanados) | ❌ **Incorrecta** — un banco trifásico básico tiene **solo dos lados** (primario y secundario), no tres. Tres devanados corresponderían a un transformador de **tres devanados** (triple-winding), no a un banco trifásico básico. |
| e) Delta - Delta   | Δ – Δ | ✅ Conexión estándar. |

> **Por qué d) es la incorrecta**: la notación de un transformador trifásico siempre tiene **dos términos separados por guión** (primario – secundario). Tres términos describen otro objeto (transformador de tres devanados o autotransformador con terciario). Además, en el contenido de la semana 9 — [[S09-1 Tema 01 - El transformador trifásico]] — se presentan únicamente las **cuatro conexiones** Y–Y, Y–Δ, Δ–Y, Δ–Δ como las configuraciones posibles del banco.

### Resultado

$$\boxed{\text{d) Ye - Ye - Ye}}$$

---

## Pregunta 4 — Transformador 15 kVA, 2300/230 V (8 pts)

### Enunciado

Se va a probar un transformador de **15 kVA** y **2300 V / 230 V** para determinar los componentes de la **rama de la excitación**, sus **impedancias en serie** y su **regulación de voltaje**. Se obtuvieron los siguientes datos de las pruebas realizadas al transformador:

| PRUEBA EN VACÍO        | PRUEBA EN CORTOCIRCUITO (medido en el primario) |
| ---------------------- | ----------------------------------------------- |
| $V_0 = 230\ \text{V}$  | $V_{cc} = 47\ \text{V}$                         |
| $I_0 = 2{,}1\ \text{A}$ | $I_{cc} = 6\ \text{A}$                          |
| $P_0 = 50\ \text{W}$   | $P_{cc} = 160\ \text{W}$                        |

- **a)** Encontrar el circuito equivalente de este transformador referido al **lado de alto voltaje**.
- **b)** Encontrar el circuito equivalente de este transformador referido al **lado de bajo voltaje**.

> [!note] Observación de la transcripción
> El enunciado del problema menciona la **regulación de voltaje** como uno de los objetivos, pero los sub-ítems literales del documento `.docx` solo piden a) y b) (circuitos equivalentes referidos a AT y BT). Conviene verificar contigo si:
> 1. El examen efectivamente termina aquí, o
> 2. Existen sub-ítems adicionales (c, d, …) en el portal/PDF original que pidan calcular la regulación de voltaje (RV), eficiencia, índice de carga o diagrama fasorial — tal como anticipa la rúbrica de las [[S09-98 Indicaciones - Práctica Calificada 2|indicaciones]] (5 variables del caso de desarrollo).

### Datos clave

- $S_n = 15\ \text{kVA}$
- $V_{1n}/V_{2n} = 2300\ \text{V} / 230\ \text{V}$ → $a = V_{1n}/V_{2n} = 10$
- $I_{1n} = S_n/V_{1n} = 15000/2300 \approx 6{,}52\ \text{A}$
- $I_{2n} = S_n/V_{2n} = 15000/230 \approx 65{,}22\ \text{A}$

**Ensayo en vacío** (alimentado por el lado BT → mide $R_{Fe}$ y $X_\mu$ referidos a BT):
- $V_0 = 230\ \text{V}$, $I_0 = 2{,}1\ \text{A}$, $P_0 = 50\ \text{W}$

**Ensayo en cortocircuito** (alimentado por el lado AT/primario → mide $R_{cc}$ y $X_{cc}$ referidos a AT):
- $V_{cc} = 47\ \text{V}$, $I_{cc} = 6\ \text{A}$, $P_{cc} = 160\ \text{W}$

### Referencia teórica

Ver [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real]] · [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real]] · [[S08-1 Tema 01 - Determinación de los parámetros del transformador]] · [[S08-2 Tema 02 - Eficiencia y regulación del transformador real]] · [[Formulario - Motores Eléctricos Estáticos y Rotativos|Formulario §17–§22]].

### Desarrollo

#### Paso 1 — Magnitudes nominales

$$a = \frac{V_{1n}}{V_{2n}} = \frac{2300}{230} = 10$$

$$I_{1n} = \frac{S_n}{V_{1n}} = \frac{15{,}000}{2300} = 6{,}522\ \text{A}$$

$$I_{2n} = \frac{S_n}{V_{2n}} = \frac{15{,}000}{230} = 65{,}217\ \text{A}$$

#### Paso 2 — Parámetros del **ensayo en cortocircuito** (referidos al **primario / AT**)

Como el ensayo se realizó alimentando por **el primario** (AT), las impedancias obtenidas quedan referidas al lado de alta tensión:

$$Z_{eq1} = \frac{V_{cc}}{I_{cc}} = \frac{47}{6} = 7{,}833\ \Omega$$

$$R_{eq1} = \frac{P_{cc}}{I_{cc}^{\,2}} = \frac{160}{6^{\,2}} = \frac{160}{36} = 4{,}444\ \Omega$$

$$X_{eq1} = \sqrt{Z_{eq1}^{\,2} - R_{eq1}^{\,2}} = \sqrt{7{,}833^{\,2} - 4{,}444^{\,2}} = \sqrt{61{,}36 - 19{,}75} = \sqrt{41{,}61} = 6{,}451\ \Omega$$

Factor de potencia del ensayo:

$$\cos\varphi_{cc} = \frac{R_{eq1}}{Z_{eq1}} = \frac{4{,}444}{7{,}833} = 0{,}567 \quad\Rightarrow\quad \varphi_{cc} \approx 55{,}43°$$

**Reparto uniforme primario/secundario** (suposición habitual cuando no hay otra información):

$$R_1 = R'_2 = \frac{R_{eq1}}{2} = 2{,}222\ \Omega \hspace{1cm} X_1 = X'_2 = \frac{X_{eq1}}{2} = 3{,}225\ \Omega$$

#### Paso 3 — Parámetros de la **rama de excitación** del ensayo en vacío (referidos al **secundario / BT**)

El ensayo en vacío se realizó alimentando por el **secundario** (BT), pues $V_0 = 230\ \text{V} = V_{2n}$. Los parámetros quedan referidos a BT.

Factor de potencia en vacío:

$$\cos\varphi_0 = \frac{P_0}{V_0\,I_0} = \frac{50}{230 \times 2{,}1} = \frac{50}{483} = 0{,}1035$$

$$\sin\varphi_0 = \sqrt{1 - 0{,}1035^{\,2}} = 0{,}9946$$

Descomposición de la corriente de vacío:

$$I_{Fe} = I_0 \cos\varphi_0 = 2{,}1 \times 0{,}1035 = 0{,}2174\ \text{A}$$

$$I_\mu = I_0 \sin\varphi_0 = 2{,}1 \times 0{,}9946 = 2{,}0887\ \text{A}$$

Parámetros (en BT):

$$R_{Fe}^{(BT)} = \frac{V_0}{I_{Fe}} = \frac{230}{0{,}2174} = 1058\ \Omega \quad\text{(o equivalente: } R_{Fe} = V_0^{\,2}/P_0 = 230^{\,2}/50 = 1058\ \Omega\text{)}$$

$$X_\mu^{(BT)} = \frac{V_0}{I_\mu} = \frac{230}{2{,}0887} = 110{,}1\ \Omega$$

**Verificación** vía admitancia (forma Chapman):

$$Y_E = \frac{I_0}{V_0} = \frac{2{,}1}{230} = 9{,}130\ \text{mS} \hspace{0.7cm} G_C = \frac{P_0}{V_0^{\,2}} = 0{,}9452\ \text{mS} \hspace{0.7cm} B_M = \sqrt{Y_E^{\,2} - G_C^{\,2}} = 9{,}081\ \text{mS}$$

$$\Rightarrow R_{Fe} = 1/G_C = 1058\ \Omega \hspace{0.7cm} X_\mu = 1/B_M = 110{,}1\ \Omega \checkmark$$

---

#### Parte a) — **Circuito equivalente referido al lado de ALTA TENSIÓN (AT)**

Las impedancias serie ya están referidas a AT. Solo hay que **referir la rama de excitación de BT a AT** multiplicando por $a^{\,2} = 100$:

$$R_{Fe}^{(AT)} = a^{\,2} \cdot R_{Fe}^{(BT)} = 100 \times 1058 = 105\,800\ \Omega \approx \mathbf{105{,}8\ k\Omega}$$

$$X_\mu^{(AT)} = a^{\,2} \cdot X_\mu^{(BT)} = 100 \times 110{,}1 = 11\,012\ \Omega \approx \mathbf{11{,}01\ k\Omega}$$

> [!success] Resultado a) — Referido a **AT (primario)**
> | Parámetro | Valor |
> | --------- | ----- |
> | $R_1$ | $2{,}222\ \Omega$ |
> | $X_1$ | $3{,}225\ \Omega$ |
> | $R'_2$ (de BT a AT) | $2{,}222\ \Omega$ |
> | $X'_2$ (de BT a AT) | $3{,}225\ \Omega$ |
> | $R_{eq1} = R_1 + R'_2$ | $\mathbf{4{,}444\ \Omega}$ |
> | $X_{eq1} = X_1 + X'_2$ | $\mathbf{6{,}451\ \Omega}$ |
> | $R_{Fe}^{(AT)}$ | $\mathbf{105{,}8\ k\Omega}$ |
> | $X_\mu^{(AT)}$ | $\mathbf{11{,}01\ k\Omega}$ |

**Topología** (forma aproximada / cantilever) — la rama de excitación se desplaza a los **terminales del primario**:

```
   V1 o──┬──[R_eq1 = 4,444 Ω]──[jX_eq1 = j6,451 Ω]──o aV2
         │
       [R_Fe^(AT) = 105,8 kΩ]  ‖  [jX_μ^(AT) = j11,01 kΩ]
         │
         o
```

---

#### Parte b) — **Circuito equivalente referido al lado de BAJA TENSIÓN (BT)**

La rama de excitación ya está referida a BT (del propio ensayo en vacío). Solo hay que **referir la impedancia serie de AT a BT** dividiendo por $a^{\,2} = 100$:

$$R_{eq2} = \frac{R_{eq1}}{a^{\,2}} = \frac{4{,}444}{100} = 0{,}04444\ \Omega$$

$$X_{eq2} = \frac{X_{eq1}}{a^{\,2}} = \frac{6{,}451}{100} = 0{,}06451\ \Omega$$

Reparto uniforme en BT:

$$R'_1 = R_2 = \frac{R_{eq2}}{2} = 0{,}02222\ \Omega \hspace{1cm} X'_1 = X_2 = \frac{X_{eq2}}{2} = 0{,}03225\ \Omega$$

> [!success] Resultado b) — Referido a **BT (secundario)**
> | Parámetro | Valor |
> | --------- | ----- |
> | $R'_1$ (de AT a BT) | $0{,}02222\ \Omega$ |
> | $X'_1$ (de AT a BT) | $0{,}03225\ \Omega$ |
> | $R_2$ | $0{,}02222\ \Omega$ |
> | $X_2$ | $0{,}03225\ \Omega$ |
> | $R_{eq2} = R'_1 + R_2$ | $\mathbf{0{,}04444\ \Omega}$ |
> | $X_{eq2} = X'_1 + X_2$ | $\mathbf{0{,}06451\ \Omega}$ |
> | $R_{Fe}^{(BT)}$ | $\mathbf{1058\ \Omega}$ |
> | $X_\mu^{(BT)}$ | $\mathbf{110{,}1\ \Omega}$ |

**Topología** (forma aproximada) — rama de excitación a los terminales del **secundario**:

```
   V1/a o──┬──[R_eq2 = 0,04444 Ω]──[jX_eq2 = j0,06451 Ω]──o V2
           │
         [R_Fe^(BT) = 1058 Ω]  ‖  [jX_μ^(BT) = j110,1 Ω]
           │
           o
```

---

#### Verificaciones de coherencia

**Verificación 1 — Pérdidas en el hierro**:
$$P_{Fe} = \frac{V_0^{\,2}}{R_{Fe}^{(BT)}} = \frac{230^{\,2}}{1058} = \frac{52\,900}{1058} = 50{,}0\ \text{W} = P_0 \quad\checkmark$$

**Verificación 2 — Pérdidas en el cobre a $I_{cc}$**:
$$P_{Cu} = I_{cc}^{\,2}\,R_{eq1} = 6^{\,2} \times 4{,}444 = 36 \times 4{,}444 = 160{,}0\ \text{W} = P_{cc} \quad\checkmark$$

**Verificación 3 — Coherencia del cambio de lado** (la potencia consumida por cada elemento no debe cambiar al referir):
$$P_{Cu,n} = I_{1n}^{\,2}\,R_{eq1} = 6{,}522^{\,2} \times 4{,}444 \approx 189{,}1\ \text{W}$$
$$P_{Cu,n} = I_{2n}^{\,2}\,R_{eq2} = 65{,}217^{\,2} \times 0{,}04444 \approx 189{,}1\ \text{W} \quad\checkmark$$

---

#### Complemento — Regulación de voltaje a plena carga

El enunciado menciona la regulación de voltaje como objetivo. Usando la fórmula simplificada referida al secundario:

$$RV \approx \frac{I_{2n}\,(R_{eq2}\cos\theta + X_{eq2}\sin\theta)}{V_{2n}} \times 100\,\%$$

Con $I_{2n} = 65{,}217\ \text{A}$, $V_{2n} = 230\ \text{V}$, $R_{eq2} = 0{,}04444\ \Omega$, $X_{eq2} = 0{,}06451\ \Omega$:

| Carga | $\cos\theta$ | $\sin\theta$ | $RV$ |
| ----- | ------------ | ------------ | ---- |
| FP unitario | 1 | 0 | $\dfrac{65{,}217 \times 0{,}04444}{230} \times 100\,\% = \mathbf{1{,}26\,\%}$ |
| FP 0,8 inductivo | 0,8 | +0,6 | $\dfrac{65{,}217\,(0{,}04444 \times 0{,}8 + 0{,}06451 \times 0{,}6)}{230} \times 100\,\% = \mathbf{2{,}11\,\%}$ |
| FP 0,8 capacitivo | 0,8 | −0,6 | $\dfrac{65{,}217\,(0{,}04444 \times 0{,}8 - 0{,}06451 \times 0{,}6)}{230} \times 100\,\% = \mathbf{-0{,}09\,\%}$ |

> Coincide con el ejercicio resuelto [[S08-3 Ejercicio resuelto - Eficiencia y regulación (Video)]] (mismo transformador).

### Resultado

**a) Referido a AT:**
$$\boxed{R_{eq1} = 4{,}444\ \Omega,\ X_{eq1} = 6{,}451\ \Omega,\ R_{Fe} = 105{,}8\ \text{k}\Omega,\ X_\mu = 11{,}01\ \text{k}\Omega}$$

**b) Referido a BT:**
$$\boxed{R_{eq2} = 0{,}04444\ \Omega,\ X_{eq2} = 0{,}06451\ \Omega,\ R_{Fe} = 1058\ \Omega,\ X_\mu = 110{,}1\ \Omega}$$

---

## Resumen de respuestas

| #  | Tema                                | Puntos | Respuesta |
| -- | ----------------------------------- | ------ | --------- |
| 1  | Material magnético alta frecuencia  | 4      | **c) Núcleos de Ferrita** |
| 2  | Ensayos esenciales del transformador| 4      | **a) Ensayo de vacío y ensayo de cortocircuito** |
| 3  | Conexión incorrecta trifásica       | 4      | **d) Ye – Ye – Ye** |
| 4a | Circuito eq. referido a AT          | 4      | $R_{eq1}=4{,}444\ \Omega$ · $X_{eq1}=6{,}451\ \Omega$ · $R_{Fe}=105{,}8\ \text{k}\Omega$ · $X_\mu=11{,}01\ \text{k}\Omega$ |
| 4b | Circuito eq. referido a BT          | 4      | $R_{eq2}=0{,}04444\ \Omega$ · $X_{eq2}=0{,}06451\ \Omega$ · $R_{Fe}=1058\ \Omega$ · $X_\mu=110{,}1\ \Omega$ |
| —  | **Total**                           | **20** |           |

## Material de soporte

- Consigna PDF: [[s09-pc2-indicaciones-rubrica.pdf|Indicaciones y rúbrica de la PC2]]
- Documento de preguntas (origen): `attachments/s09_EXAMEN_DE_MAQUINAS_ELECTRICAS_2_SQOPWZ.docx`
- Teoría: [[S06-2 Tema 01 - Materiales magnéticos]] · [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real]] · [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real]] · [[S08-1 Tema 01 - Determinación de los parámetros del transformador]] · [[S08-2 Tema 02 - Eficiencia y regulación del transformador real]] · [[S09-1 Tema 01 - El transformador trifásico]]
- Ejercicios resueltos: [[S07-4 Ejercicio resuelto - Ensayos del transformador (Video)]] · [[S08-3 Ejercicio resuelto - Eficiencia y regulación (Video)]]
- Formulario: [[Formulario - Motores Eléctricos Estáticos y Rotativos|§17–§22]]
