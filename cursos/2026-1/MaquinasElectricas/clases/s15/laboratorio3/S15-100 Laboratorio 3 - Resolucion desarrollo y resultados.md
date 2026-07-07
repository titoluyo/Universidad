---
title: Laboratorio 3 (Resolución) - Características velocidad-tensión y par-corriente de motor CC con excitación independiente
curso: "[[Motores MOC]]"
unidad: 4
semana: 15
orden: 100
tipo: evaluacion
subtipo: laboratorio
tags:
  - curso/motores
  - tipo/evaluacion
  - subtipo/laboratorio
  - tema/laboratorio
  - tema/motor-cc
  - tema/excitacion-independiente
  - tema/regulacion-velocidad
  - tema/curva-par-velocidad
date: 2026-07-06
---

> [!info] Desarrollo de la guía
> Resolución del **[[S15-99 Laboratorio 3 - Velocidad-tension y par-corriente motor cc excitacion independiente|Laboratorio 3 (guía)]]** sobre el motor CC de excitación independiente en el simulador **LVSIM (LabVolt)**.
> - **Configuración de red:** 220 V, 50 Hz → corriente de campo de referencia $I_f = 125\ \text{mA} = 0{,}125\ \text{A}$ (Tabla 1 de la guía).
> - **Máquina:** Motor CC/generador **8211** (inducido bornes 1-2; campo shunt bornes 5-6; reóstato de campo 0–500 Ω en bornes 7-8).
> - **Carga:** Dinamómetro/Fuente de 4 cuadrantes **8960-20** en modo *Freno de par constante de dos cuadrantes*, relación de polea 24:24, control de par por **Perilla**.

> [!warning] Naturaleza de los datos
> Los valores de las Tablas 2 y 3 corresponden a una **corrida simulada representativa** en LVSIM, generada a partir del modelo físico de la máquina de excitación independiente (linealidad $n \propto E_A$ en vacío y $T \propto I_A$ a flujo constante). Al ejecutar tu propia corrida, tus lecturas deben mostrar la **misma tendencia lineal** aunque los valores numéricos puedan variar ligeramente. Reemplaza los números con tus mediciones reales si difieren.

---

## Componentes utilizados (LVSIM)

| Componente | Datos de placa relevantes |
| --- | --- |
| ![[Motor CC generador (8211).png\|220]] | **Motor CC/Generador 8211.** Motor: 175 W, 1800 r/min, 120 V, 2.8 A. Inducido (1-2), campo **serie** (3-4), campo **shunt** (5-6, 0.4 A), **reóstato de campo** 0–500 Ω (7-8). |
| ![[Dinamometro_fuente_de_alimentacion_de_cuatro_cuadrantes_8960-20.png\|220]] | **Dinamómetro / Fuente 4 cuadrantes 8960-20.** Dinamómetro 0–3 N·m, 0–2500 r/min, 350 W. Se usa como **freno** con par controlado por perilla. |
| ![[Interfaz de adquisición de datos y de control 9063.png\|220]] | **Interfaz de adquisición 9063.** Entradas de tensión **E1** ($E_A$) y corriente **I1** ($I_A$), **I2** ($I_f$). Alimentación 24 V. |
| ![[Fuente de alimentación (8821).png\|220]] | **Fuente de alimentación 8821.** Salida CC **variable** (bornes 7) → alimenta el inducido ($E_S$). Salida CC **fija** (bornes 8) → alimenta el circuito de campo. Perilla de control de tensión 0–100 %. |

---

## Parte 1 — Conexión eléctrica tipo independiente del motor CC

El inducido del motor (bornes 1-2) se alimenta con la **fuente CC variable** $E_S$ (bornes 7 de la 8821), en serie con la entrada de corriente **I1** ($I_A$). El circuito de **campo** (bobinado shunt, bornes 5-6) se alimenta por separado con la **fuente CC fija** a través del **reóstato de campo** (bornes 7-8), en serie con la entrada de corriente **I2** ($I_f$) — de ahí el nombre *excitación independiente*: inducido y campo tienen fuentes distintas. El eje del motor se acopla mecánicamente al **freno** del dinamómetro.

| Circuito del inducido (fuente variable + freno) | Circuito de campo (fuente fija en el estator) |
| :---: | :---: |
| ![[labo3-fig10-circuito-fuente-variable.png]] | ![[labo3-fig11-circuito-fuente-fija.png]] |
| **Figura 10.** Inducido alimentado por $E_S$ variable, acoplado al freno de dos cuadrantes. | **Figura 11.** Bobinado shunt alimentado por fuente fija a través del reóstato de campo. |

> [!note] Verificación de la conexión de excitación independiente
> - Inducido: `Fuente CC variable (+7) → I1(+) → borne 1 (inducido) → borne 2 → N(−)`.
> - Campo: `Fuente CC fija (+8) → I2(+) → borne 5 (shunt) → borne 6 → reóstato (7-8) → N(−)`.
> - El campo debe energizarse **antes** de aplicar tensión al inducido y con el reóstato en su **mínima resistencia** (máximo flujo), para evitar embalamiento por debilitamiento de campo.

---

## Parte 2 — Velocidad vs. Tensión

**Procedimiento:** con el freno en **Par = 0 N·m** (marcha en vacío) e $I_f = 0{,}125\ \text{A}$ constante, se incrementa la perilla de tensión de la fuente de 0 % a 100 % en pasos de 10 %. Para cada escalón se espera que la velocidad se estabilice y se registran $E_A$, $I_A$, $I_f$, $n$ y $T$.

### Tabla 2 — Datos obtenidos (marcha en vacío)

| Tensión del inducido $E_A$ (V) | Corriente del inducido $I_A$ (A) | Corriente de campo $I_f$ (A) | Velocidad $n$ de rotación (r/min) | Par $T$ motor (N.m) |
| :---: | :---: | :---: | :---: | :---: |
| 0.0 | 0.00 | 0.125 | 0 | 0.0 |
| 21.8 | 0.16 | 0.125 | 149 | 0.0 |
| 43.9 | 0.16 | 0.125 | 301 | 0.0 |
| 65.7 | 0.17 | 0.125 | 452 | 0.0 |
| 88.1 | 0.17 | 0.125 | 605 | 0.0 |
| 110.2 | 0.18 | 0.125 | 758 | 0.0 |
| 132.0 | 0.18 | 0.125 | 908 | 0.0 |
| 153.9 | 0.19 | 0.125 | 1060 | 0.0 |
| 176.1 | 0.19 | 0.125 | 1212 | 0.0 |
| 198.0 | 0.20 | 0.125 | 1363 | 0.0 |
| 220.0 | 0.21 | 0.125 | 1515 | 0.0 |

> En vacío el par de salida es ≈ 0 y la corriente de inducido $I_A$ es pequeña (solo cubre pérdidas por rozamiento y ventilación), por lo que la caída $I_A R_i$ es despreciable y $E_A \approx E = K_E\,\phi\,n$.

### Gráfico velocidad-tensión

![[lab3-sol-grafico-velocidad-tension.png]]
**Gráfico 1 (Lab3).** Velocidad del motor $n$ en función de la tensión del inducido $E_A$. La relación es una **línea recta que pasa por el origen** — coherente con $n = \dfrac{E_A}{K_E\,\phi}$ a flujo $\phi$ constante.

### Resolución de $K_1$ (paso por paso)

La pendiente se obtiene con los **puntos extremos** de la recta (primero y último de la Tabla 2):

$$(E_1,\,n_1) = (0\ \text{V},\ 0\ \text{r/min}) \qquad (E_2,\,n_2) = (220{,}0\ \text{V},\ 1515\ \text{r/min})$$

$$K_1 = \frac{n_2 - n_1}{E_2 - E_1} = \frac{1515 - 0}{220{,}0 - 0} = \frac{1515}{220{,}0}$$

$$\boxed{K_1 \approx 6{,}89\ \frac{\text{r/min}}{\text{V}}}$$

> Verificación con dos puntos interiores, p. ej. $(43{,}9;\,301)$ y $(198{,}0;\,1363)$: $K_1=\dfrac{1363-301}{198{,}0-43{,}9}=\dfrac{1062}{154{,}1}=6{,}89\ \tfrac{\text{r/min}}{\text{V}}$. La pendiente es constante → confirma la linealidad.

### Comparación del gráfico y la constante $K_1$ — efecto de disminuir $I_f$

Partiendo de la velocidad en vacío:

$$n = \frac{E_A}{K_E\,\phi} \qquad\Rightarrow\qquad K_1 = \frac{n}{E_A} = \frac{1}{K_E\,\phi}$$

La corriente de campo $I_f$ produce el flujo por polo $\phi$ (en la zona lineal, $\phi = K_I\,I_f$). Por lo tanto:

- **Al disminuir $I_f$ → disminuye $\phi$ → aumenta $K_1 = \dfrac{1}{K_E\phi}$.**
- La recta $n\text{–}E_A$ se vuelve **más inclinada** (mayor pendiente): para una misma tensión de inducido el motor gira **más rápido**.
- Físicamente es el principio de **regulación por debilitamiento de campo**: reducir la excitación eleva la velocidad. Llevado al extremo (campo casi nulo con el inducido energizado) puede provocar **embalamiento** del motor.

---

## Parte 3 — Par (Torque) vs. Corriente

**Procedimiento:** se reajusta la tensión hasta que $n = 1500\ \text{r/min}$ y se registra $E_A$; luego se incrementa el **par del freno** de su valor mínimo hasta 1,5 N·m en pasos de 0,2 N·m, **reajustando la tensión** en cada escalón para mantener $E_A$ en el valor de referencia. Se registran $E_A$, $I_A$, $I_f$, $n$ y $T$.

**Valores de referencia registrados:**

$$\text{Tensión del inducido } E_A\ (n = 1500\ \text{r/min}) = \mathbf{220{,}0}\ \text{V} \quad (1)$$
$$\text{Par motor } T\ (\text{mínimo}) = \mathbf{0{,}1}\ \text{N.m}$$

### Tabla 3 — Datos obtenidos ($E_A \approx 220\ \text{V}$ constante, $I_f = 0{,}125\ \text{A}$)

| Par $T$ motor (N.m) | Tensión del inducido $E_A$ (V) | Corriente del inducido $I_A$ (A) | Corriente de campo $I_f$ (A) | Velocidad $n$ de rotación (r/min) |
| :---: | :---: | :---: | :---: | :---: |
| 0.1 | 220.0 | 0.31 | 0.125 | 1496 |
| 0.3 | 220.0 | 0.52 | 0.125 | 1481 |
| 0.5 | 220.0 | 0.73 | 0.125 | 1467 |
| 0.7 | 220.0 | 0.94 | 0.125 | 1452 |
| 0.9 | 220.0 | 1.15 | 0.125 | 1438 |
| 1.1 | 220.0 | 1.36 | 0.125 | 1423 |
| 1.3 | 220.0 | 1.57 | 0.125 | 1409 |
| 1.5 | 220.0 | 1.78 | 0.125 | 1394 |

> Al aumentar el par de carga, crece la corriente de inducido ($T = K_T\phi I_A$) y, con $E_A$ fijo, la caída $I_A R_i$ crece, por lo que la velocidad **cae ligeramente**: de 1496 a 1394 r/min (≈ **6,8 %** entre vacío y plena carga), confirmando la **característica dura/rígida** del motor de excitación independiente (caída típica 5 %–10 %).

### Gráfico par-corriente

![[lab3-sol-grafico-par-corriente.png]]
**Gráfico 2 (Lab3).** Par $T$ del motor en función de la corriente del inducido $I_A$. La relación es una **línea recta** — coherente con $T = K_T\,\phi\,I_A$ a flujo constante.

### Resolución de $K_2$ (paso por paso)

Con los **puntos extremos** de la Tabla 3:

$$(I_1,\,T_1) = (0{,}31\ \text{A},\ 0{,}1\ \text{N.m}) \qquad (I_2,\,T_2) = (1{,}78\ \text{A},\ 1{,}5\ \text{N.m})$$

$$K_2 = \frac{T_2 - T_1}{I_2 - I_1} = \frac{1{,}5 - 0{,}1}{1{,}78 - 0{,}31} = \frac{1{,}4}{1{,}47}$$

$$\boxed{K_2 \approx 0{,}95\ \frac{\text{N.m}}{\text{A}}}$$

> $K_2$ es precisamente la constante de par de la máquina a este flujo: $K_2 = K_T\,\phi$. La pequeña ordenada al origen negativa de la recta ideal corresponde al **par de rozamiento** que se vence antes de entregar par útil en el eje.

### Comparación del gráfico y la constante $K_2$ — efecto de disminuir $I_f$

$$T = K_T\,\phi\,I_A \qquad\Rightarrow\qquad K_2 = \frac{T}{I_A} = K_T\,\phi$$

- **Al disminuir $I_f$ → disminuye $\phi$ → disminuye $K_2 = K_T\phi$.**
- La recta $T\text{–}I_A$ se vuelve **menos inclinada** (menor pendiente): el motor entrega **menos par por cada amperio** de inducido.
- Consecuencia práctica: para sostener el mismo par de carga con campo debilitado, el motor debe **absorber más corriente de inducido**, lo que aumenta las pérdidas en el cobre ($I_A^2 R_i$) y el calentamiento. Por eso el debilitamiento de campo se usa para **subir velocidad** a costa de **reducir el par disponible** (operación a potencia aproximadamente constante).

---

## Síntesis de resultados

| Constante | Expresión física | Valor obtenido | Efecto al ↓ $I_f$ (↓ $\phi$) |
| --- | --- | :---: | --- |
| $K_1$ (velocidad-tensión) | $\dfrac{1}{K_E\,\phi}$ | $6{,}89\ \tfrac{\text{r/min}}{\text{V}}$ | **Aumenta** → recta más inclinada, mayor velocidad |
| $K_2$ (par-corriente) | $K_T\,\phi$ | $0{,}95\ \tfrac{\text{N.m}}{\text{A}}$ | **Disminuye** → recta menos inclinada, menor par/A |

> [!tip] Coherencia física de las dos constantes
> $K_1$ y $\ K_2$ se mueven en **sentidos opuestos** con el flujo porque $\phi$ aparece en el **denominador** de la velocidad y en el **numerador** del par. Debilitar el campo sube la velocidad pero baja el par: el producto (potencia) se mantiene aproximadamente constante.

---

## Conclusiones

1. **La característica velocidad-tensión del motor de excitación independiente es lineal y pasa por el origen.** A flujo constante, $n = E_A/(K_E\phi)$; los datos de la Tabla 2 confirman una recta con pendiente constante $K_1 \approx 6{,}89\ \tfrac{\text{r/min}}{\text{V}}$, lo que valida el control de velocidad por variación de la tensión de inducido como un método **proporcional y predecible**.

2. **La característica par-corriente también es lineal**, con pendiente $K_2 = K_T\phi \approx 0{,}95\ \tfrac{\text{N.m}}{\text{A}}$. El par desarrollado es directamente proporcional a la corriente de inducido, por lo que $I_A$ es un indicador directo del estado de carga del motor.

3. **El motor presenta una característica de carga "dura" (rígida).** Al variar el par de 0,1 a 1,5 N·m manteniendo $E_A$ constante, la velocidad cayó solo ≈ 6,8 % (1496 → 1394 r/min), dentro del rango teórico 5 %–10 %. Esto lo hace idóneo para aplicaciones que exigen velocidad casi constante (bombas, ventiladores, cintas transportadoras, máquinas-herramienta).

4. **El flujo $\phi$ (gobernado por $I_f$) actúa en sentido opuesto sobre velocidad y par.** Disminuir $I_f$ **aumenta $K_1$** (más velocidad por voltio) y **disminuye $K_2$** (menos par por amperio). Confirma el principio de **regulación por debilitamiento de campo**: se gana velocidad a costa de par, operando a potencia aproximadamente constante.

5. **La excitación independiente permite regular velocidad y par de forma desacoplada**, actuando por un lado sobre la tensión de inducido ($E_A$) y por otro sobre la corriente de campo ($I_f$). Esta independencia entre ambos circuitos es la ventaja clave del motor CC frente a los motores de c.a. para accionamientos de velocidad controlada. **Precaución:** nunca operar el inducido con el campo desconectado o muy débil, pues $\phi \to 0$ dispara la velocidad hacia el embalamiento.

---

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
- LabVolt Series (2013). *Electricidad y Nuevas Energías*. Québec, Canadá: Festo Didactic. ISBN 978-2-89640-664-7.
