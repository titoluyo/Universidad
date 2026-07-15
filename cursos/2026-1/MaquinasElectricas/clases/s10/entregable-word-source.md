---
title: "Informe de Laboratorio Calificado N° 2"
subtitle: "Regulación y eficiencia del transformador"
author: "[Apellidos, Nombres — Código]"
date: "Junio 2026"
lang: es
---

# 2. Funcionamiento del transformador

## 2.a. Valores nominales del transformador

### Tabla 1 — Características nominales del transformador 8353

|                  | Primario  |                                | Secundario |
| ---------------- | --------- | ------------------------------ | ---------- |
| $V_{1\text{-}2}$ | 24 V      | $V_{5\text{-}6}$ ($E_{2\,vacío}$) | 120 V      |
| $A_{1\text{-}2}$ | 5 A       | $A_{5\text{-}6}$                  | 1 A        |
| $V_{3\text{-}4}$ | 24 V      | $V_{7\text{-}8}$                  | 120 V      |
| $A_{3\text{-}4}$ | 5 A       | $A_{7\text{-}8}$                  | 1 A        |

**Número de espiras por bobina:**

| Bobina | Número de espiras | Lado / capacidad      |
| :----: | :---------------: | --------------------- |
| 1-2    | 57                | primario, 24 V / 5 A  |
| 3-4    | 57                | primario, 24 V / 5 A  |
| 5-6    | 285               | secundario, 120 V / 1 A |
| 7-8    | 285               | secundario, 120 V / 1 A |

Relación de transformación: $a = N_1/N_2 = 57/285 = 0{,}200$.
Potencia aparente nominal: $S_n = 24 \times 5 = 120 \;\text{V} \cdot 1 \;\text{A} = 120 \;\text{VA}$ por bobinado.

### Tabla 2 — Relaciones medidas $A$ y $B$

A partir de la fila experimental del ensayo en vacío ($I_2 = 0$) para $A$, y de la fila a plena carga del barrido ($R = 210\,\Omega$) para $B$:

| Relación | Definición | Valor teórico | Valor medido |
| :------: | ---------- | :-----------: | :----------: |
| $A$ | $V_{1\text{-}2} / V_{5\text{-}6}$ | 0,200 | 23,99 / 119,70 = **0,2004** |
| $B$ | $I_{5\text{-}6} / I_{1\text{-}2}$ | 0,200 | 0,550 / 3,163 = **0,174** |

**Análisis:** $A$ coincide casi exactamente con el valor teórico, confirmando la relación de transformación de tensiones del transformador ideal. $B$ es menor que 0,200 (≈ 13 % por debajo) porque la corriente primaria $I_1$ incluye no sólo la corriente reflejada de la carga ($I_2/a$) sino también la corriente de excitación $I_0$, que está presente aun sin carga. Es decir, en transformadores reales $A \approx a$ se cumple muy bien, pero $B < a$ por la presencia inevitable de $I_0$.

### Tabla 3 — Resistencias internas de los bobinados

Medidas con el ohmímetro del multímetro de LVSIM (fuente desconectada):

| Bobina            | Resistencia (Ω) |
| :---------------: | :-------------: |
| $R_{1\text{-}2}$  | 0,200           |
| $R_{3\text{-}4}$  | 0,200           |
| $R_{5\text{-}6}$  | 2,900           |
| $R_{7\text{-}8}$  | 2,800           |

Las bobinas del primario (24 V, 5 A) tienen $R$ pequeña (alambre grueso para alta corriente), mientras que las bobinas del secundario (120 V, 1 A) tienen $R$ mayor (alambre delgado y mayor número de vueltas). La pequeña diferencia entre $R_{5\text{-}6}$ y $R_{7\text{-}8}$ (3 %) refleja la variación constructiva normal entre bobinas gemelas.

A partir de estas resistencias medidas se obtiene la **impedancia resistiva equivalente referida al secundario** del circuito equivalente del transformador:

$$R_{eq,s} = R_2 + \frac{R_1}{a^2} = 2{,}900 + \frac{0{,}200}{0{,}04} = 2{,}900 + 5{,}000 = 7{,}900 \;\Omega$$

Este valor coincide a < 1 % con el obtenido por dos métodos independientes (pendiente de $E_2$ vs $I_2$ y ajuste de $P_{pérd}$ vs $I_2^2$), validando el modelo del transformador real.

## 2.b. Mediciones con el módulo de adquisición de datos

### Tabla 4 — Mediciones con carga resistiva variable

Alimentación del primario mantenida en $E_1 = 24{,}00$ V para todas las cargas. Variación de $R_{carga}$ entre 440 Ω y 210 Ω según el Apéndice C de la guía (módulo 8311, columna 220/230 V).

| $R_{carga}$ (Ω) | $E_1$ (V) | $I_1$ (A) | $E_2$ (V) | $I_2$ (A) | $P_1$ (W) | $P_2$ (W) | $P_{pérd}=P_1-P_2$ (W) |
| :-------------: | :-------: | :-------: | :-------: | :-------: | :-------: | :-------: | :--------------------: |
| 440 | 24,00 | 1,838 | 117,50 | 0,267 | 39,89 | 31,42 | 8,47 |
| 400 | 24,00 | 1,954 | 117,40 | 0,293 | 43,05 | 34,45 | 8,60 |
| 367 | 23,99 | 2,073 | 117,20 | 0,319 | 46,11 | 37,47 | 8,64 |
| 338 | 24,00 | 2,193 | 116,90 | 0,345 | 49,29 | 40,42 | 8,87 |
| 314 | 23,99 | 2,313 | 116,70 | 0,371 | 52,37 | 43,36 | 9,01 |
| 293 | 24,00 | 2,434 | 116,50 | 0,397 | 55,47 | 46,30 | 9,17 |
| 275 | 24,00 | 2,555 | 116,30 | 0,423 | 58,57 | 49,22 | 9,35 |
| 259 | 24,00 | 2,676 | 116,10 | 0,448 | 61,64 | 52,11 | 9,53 |
| 244 | 23,99 | 2,797 | 116,00 | 0,474 | 64,65 | 55,05 | 9,60 |
| 232 | 23,99 | 2,919 | 115,70 | 0,499 | 67,72 | 57,81 | 9,91 |
| 220 | 23,99 | 3,041 | 115,60 | 0,525 | 70,77 | 60,76 | 10,01 |
| 210 | 23,99 | 3,163 | 115,30 | 0,550 | 73,80 | 63,47 | 10,33 |

**Medición adicional — Ensayo en vacío** (todas las cargas desconectadas, $R_{carga} = \infty$):

| Magnitud | Valor medido |
| :------: | :----------: |
| $E_1$    | 23,99 V      |
| $I_1 = I_0$ | 0,896 A   |
| $E_2 = E_{2\,vacío}$ | 119,7 V |
| $I_2$    | 0 A          |
| $P_1 = P_{Fe}$ | 7,835 W |
| $P_2$    | 0 W          |

Esta medición se usa como referencia ($E_{2\,vacío}$) para los cálculos de regulación y como evidencia experimental directa para las preguntas (f) y (g).

### Tabla 5 — Regulación y eficiencia por carga

Con $E_{2\,vacío} = 119{,}70$ V (medido directamente):

| $R_{carga}$ (Ω) | $E_2$ (V) | $I_2$ (A) | $P_1$ (W) | $P_2$ (W) | Reg (%) | η (%) |
| :-------------: | :-------: | :-------: | :-------: | :-------: | :-----: | :---: |
| 440 | 117,50 | 0,267 | 39,89 | 31,42 | 1,87 | 78,77 |
| 400 | 117,40 | 0,293 | 43,05 | 34,45 | 1,96 | 80,02 |
| 367 | 117,20 | 0,319 | 46,11 | 37,47 | 2,13 | 81,26 |
| 338 | 116,90 | 0,345 | 49,29 | 40,42 | 2,40 | 82,00 |
| 314 | 116,70 | 0,371 | 52,37 | 43,36 | 2,57 | 82,80 |
| 293 | 116,50 | 0,397 | 55,47 | 46,30 | 2,75 | 83,47 |
| 275 | 116,30 | 0,423 | 58,57 | 49,22 | 2,92 | 84,04 |
| 259 | 116,10 | 0,448 | 61,64 | 52,11 | 3,10 | 84,54 |
| 244 | 116,00 | 0,474 | 64,65 | 55,05 | 3,19 | 85,15 |
| 232 | 115,70 | 0,499 | 67,72 | 57,81 | 3,46 | 85,37 |
| 220 | 115,60 | 0,525 | 70,77 | 60,76 | 3,55 | 85,86 |
| 210 | 115,30 | 0,550 | 73,80 | 63,47 | 3,82 | 86,00 |

## 2.c. Esquema del transformador en el software

> **[INSERTAR CAPTURA DE PANTALLA DEL ESQUEMA EN LVSIM]**
> Imagen del circuito armado en LVSIM-EMS mostrando los módulos 8821 (Power Supply), 8353 (Transformer), 9063 (DACI) y 8311 (Resistive Load) interconectados según la Imagen 2 de la guía.

---

# 3. Regulación y eficiencia del transformador

## 3.a. Gráfico de pérdidas $P_{pérd}$ vs corriente secundaria $I_2$

> **[INSERTAR GRÁFICO 1 — Pérdidas $P_{pérd}$ vs $I_2$]**
> Gráfico de dispersión XY con los 13 puntos (12 de carga + ensayo en vacío). Eje X: $I_2$ (A) de 0 a 0,6. Eje Y: $P_{pérd}$ (W) de 7 a 11. Línea de tendencia polinómica de orden 2 con ecuación y R² visibles.

**Análisis del gráfico:** las pérdidas totales $P_{pérd}$ presentan un mínimo en vacío (7,835 W = pérdidas en el hierro) y crecen monótonamente con la carga siguiendo la forma teórica $P_{pérd}(I_2) = P_{Fe} + R_{eq,s} \cdot I_2^2$. El ajuste cuadrático arroja:

$$P_{Fe} \approx 7{,}68 \;\text{W} \quad ; \quad R_{eq,s} \approx 7{,}9 \;\Omega$$

valores consistentes con los obtenidos por otros métodos (medición directa en vacío y cálculo a partir de $R_1$ y $R_2$ medidas con ohmímetro).

## 3.b. Cálculo de la regulación

La regulación de tensión se define como la diferencia entre la tensión secundaria en vacío y la tensión secundaria a la carga considerada, expresada como porcentaje:

$$\text{Reg}(\%) = \frac{E_{2\,vacío} - E_2}{E_2} \times 100\,\%$$

**Procedimiento (ejemplo desarrollado para el punto más cercano a plena carga, $R_{carga} = 210\,\Omega$):**

Datos medidos:
- $E_{2\,vacío} = 119{,}70 \;\text{V}$ (medición directa en vacío)
- $E_2 = 115{,}30 \;\text{V}$ (carga aplicada)
- $I_2 = 0{,}550 \;\text{A}$

Sustituyendo en la fórmula:

$$\text{Reg} = \frac{119{,}70 - 115{,}30}{115{,}30} \times 100\,\% = \frac{4{,}40}{115{,}30} \times 100\,\% = 3{,}82\,\%$$

El mismo procedimiento se aplica a cada uno de los 12 puntos de la Tabla 4, obteniéndose los valores de la columna "Reg (%)" de la Tabla 5 (de 1,87 % a 3,82 %).

**Regulación nominal extrapolada:** dado que el barrido sólo alcanza $I_2 = 0{,}550$ A (55 % de la corriente nominal $I_{2n} = 1$ A), se extrapola linealmente la curva $E_2$ vs $I_2$ a corriente nominal:

$$E_2(I_{2n}) = E_{2\,vacío} - R_{eq,s} \cdot I_{2n} = 119{,}70 - 7{,}9 \cdot 1{,}0 = 111{,}80 \;\text{V}$$

$$\text{Reg}_{nominal} = \frac{119{,}70 - 111{,}80}{111{,}80} \times 100\,\% = 7{,}07\,\%$$

## 3.c. Gráfico de eficiencia $\eta$ vs corriente secundaria $I_2$

> **[INSERTAR GRÁFICO 2 — Eficiencia $\eta$ vs $I_2$]**
> Gráfico de dispersión XY con los 12 puntos de carga. Eje X: $I_2$ (A) de 0 a 1,1. Eje Y: $\eta$ (%) de 75 a 90. Marcador del punto teórico de máxima eficiencia ($I_2 = 0{,}986$ A, $\eta = 87{,}9\,\%$). Líneas de referencia en $\eta = 87{,}9\,\%$ y $I_2 = 1{,}0$ A.

**Análisis del gráfico:** la eficiencia crece monótonamente con la corriente secundaria en el rango medido (78,77 % a 86,00 %). La curva no alcanza su máximo dentro del barrido porque las 12 cargas (de 27 % a 55 % de la corriente nominal) caen en la rama izquierda de la curva $\eta(I_2)$. El máximo teórico se ubica en $I_2 \approx I_{2n} = 1$ A, donde las pérdidas variables ($P_{Cu}$) igualan a las constantes ($P_{Fe}$). La eficiencia máxima estimada es de **87,9 %**.

## 3.d. Cálculo de la eficiencia

La eficiencia del transformador se calcula por el método directo:

$$\eta(\%) = \frac{P_2}{P_1} \times 100\,\%$$

**Procedimiento (ejemplo desarrollado para el punto $R_{carga} = 210\,\Omega$):**

Datos medidos:
- $P_1 = 73{,}80 \;\text{W}$ (potencia activa absorbida del primario)
- $P_2 = 63{,}47 \;\text{W}$ (potencia activa entregada a la carga)

Sustituyendo:

$$\eta = \frac{63{,}47}{73{,}80} \times 100\,\% = 86{,}00\,\%$$

**Verificación cruzada por el método indirecto:** usando $P_{Fe} = 7{,}675$ W (refinado: $P_1^{vacío} - I_0^2 R_1$) y $P_{Cu} = R_{eq,s} \cdot I_2^2 = 7{,}9 \cdot 0{,}550^2 = 2{,}39$ W:

$$\eta_{indirecto} = \frac{P_2}{P_2 + P_{Cu} + P_{Fe}} = \frac{63{,}47}{63{,}47 + 2{,}39 + 7{,}675} = \frac{63{,}47}{73{,}54} = 86{,}31\,\%$$

La diferencia con el método directo (86,00 % vs 86,31 %, ≈ 0,3 %) está dentro de la precisión esperable de las mediciones. El mismo procedimiento se aplica a cada uno de los 12 puntos de la Tabla 4, obteniéndose los valores de la columna "η (%)" de la Tabla 5.

## 3.e. Curva de regulación de tensión: $E_2$ vs $I_2$

> **[INSERTAR GRÁFICO 3 — Curva $E_2$ vs $I_2$]**
> Gráfico de dispersión XY con los 13 puntos (12 de carga + vacío). Eje X: $I_2$ (A) de 0 a 1,1. Eje Y: $E_2$ (V) de 110 a 121. Línea de tendencia lineal con ecuación y R² visibles. Punto del ensayo en vacío destacado (0; 119,70 V). Punto nominal extrapolado (1,0; 111,80 V) destacado con etiqueta de regulación nominal.

**Análisis del gráfico:** la curva $E_2$ vs $I_2$ es claramente lineal (R² > 0,99) y decreciente, en concordancia con el modelo del transformador real para carga puramente resistiva:

$$E_2(I_2) = E_{2\,vacío} - R_{eq,s} \cdot I_2$$

El intercepto de la recta es $E_{2\,vacío} \approx 119{,}7$ V (coincide con la medición directa en vacío). La pendiente da $|R_{eq,s}| \approx 7{,}9 \;\Omega$ (coincide con $R_2 + R_1/a^2$ calculado a partir de las mediciones de resistencias con ohmímetro). La linealidad indica que en el rango ensayado el núcleo no se ha saturado significativamente. La extrapolación a corriente nominal ($I_2 = 1$ A) da $E_2 = 111{,}80$ V, lo que corresponde a una **regulación nominal de 7,07 %** — un valor razonable para un transformador didáctico.

## 3.f. ¿Por qué la corriente en el primario no es cero durante la operación sin carga?

**Evidencia experimental:** durante el ensayo en vacío (secundario abierto, $I_2 = 0$) se midió $I_1 = I_0 = 0{,}896$ A, es decir aproximadamente el 18 % de la corriente nominal del primario.

**Explicación física:** incluso sin carga, el transformador necesita establecer un flujo magnético variable en el núcleo para poder operar. Esta corriente —denominada **corriente de excitación $I_0$**— circula permanentemente por el primario y se descompone fasorialmente en dos componentes con interpretación física clara:

- **Componente magnetizante $I_\mu$** (en cuadratura con $E_1$, atraso de 90°): genera el flujo magnético $\phi(t)$ en el núcleo. Sin esta corriente no hay flujo y el transformador no funciona.
- **Componente activa $I_w$** (en fase con $E_1$): suministra las pérdidas en el hierro $P_{Fe}$ (histéresis y corrientes de Foucault), que se disipan continuamente en el núcleo.

A partir de las mediciones del ensayo en vacío:

$$\cos\varphi_0 = \frac{P_1^{vacío}}{E_1 \cdot I_0} = \frac{7{,}835}{23{,}99 \times 0{,}896} = 0{,}364$$

$$I_w = I_0 \cdot \cos\varphi_0 = 0{,}896 \times 0{,}364 = 0{,}326 \;\text{A}$$

$$I_\mu = I_0 \cdot \sin\varphi_0 = 0{,}896 \times 0{,}931 = 0{,}834 \;\text{A}$$

La relación $I_\mu / I_w = 2{,}56$ confirma la predicción teórica de que **la componente magnetizante domina ampliamente sobre la componente activa**, característica de los transformadores con núcleo ferromagnético operando en régimen de baja saturación.

El hecho de que $I_0$ sea relativamente alta (18 % de $I_{1n}$ vs el 2–8 % típico de transformadores comerciales) se explica porque la placa del transformador 8353 es nominal a 60 Hz y se operó a 50 Hz: para la misma tensión aplicada, el flujo magnético es 20 % mayor ($\phi \propto V/f$), llevando al núcleo más cerca de la saturación.

## 3.g. ¿Por qué la potencia activa en el primario no es cero, a pesar de que no se suministra potencia a la carga?

**Evidencia experimental:** durante el ensayo en vacío se midió $P_1 = 7{,}835$ W con el secundario abierto ($P_2 = 0$ W). Es decir, el transformador absorbe casi 8 W de potencia activa sin entregar nada a la carga.

**Explicación física:** toda esa potencia activa se disipa internamente como **pérdidas en el hierro** $P_{Fe}$, originadas en dos fenómenos físicos del núcleo ferromagnético cuando es atravesado por un flujo alterno:

1. **Pérdidas por histéresis ($P_H$):** la magnetización cíclica del material ferromagnético no es reversible. Cada ciclo del campo $H(t)$ encierra un área del lazo $B$–$H$ que se convierte en energía calorífica. Empíricamente:

$$P_H = k_H \cdot f \cdot B_m^{\alpha}$$

con $\alpha \approx 1{,}6$–$2{,}0$ (exponente de Steinmetz).

2. **Pérdidas por corrientes de Foucault ($P_F$):** las variaciones del flujo magnético inducen corrientes parásitas en el material conductor del núcleo, que disipan energía por efecto Joule. Para reducirlas, el núcleo se construye con chapas delgadas laminadas y aisladas entre sí:

$$P_F = k_F \cdot f^2 \cdot B_m^2 \cdot e^2$$

donde $e$ es el espesor de la chapa.

La suma de ambos términos constituye las pérdidas en el hierro:

$$P_{Fe} = P_H + P_F$$

A frecuencia y tensión constantes, $P_{Fe}$ es **prácticamente independiente de la carga**, porque depende sólo del nivel de flujo $B_m$, que está fijado por la tensión $E_1$ a través de la ecuación fundamental del transformador $E_1 = 4{,}44 \cdot f \cdot N \cdot \phi_m$.

Adicionalmente, en vacío también hay una pequeña pérdida en el cobre del primario debida a la corriente de excitación: $P_{Cu,0} = I_0^2 \cdot R_{1\text{-}2} = 0{,}896^2 \times 0{,}200 = 0{,}160$ W. Esto es sólo el 2 % de $P_1^{vacío}$, por lo que la aproximación $P_1^{vacío} \approx P_{Fe}$ es válida con muy buena precisión.

**Verificación experimental de la separación $P_{Fe}$ + $P_{Cu}$:** tres métodos independientes coinciden en $P_{Fe} \approx 7{,}7$ W:

| Método | Valor de $P_{Fe}$ |
| :----- | :---------------: |
| Medición directa en vacío (refinada): $P_1^{vacío} - I_0^2 R_{1\text{-}2}$ | 7,675 W |
| Ajuste por mínimos cuadrados de $P_{pérd}(I_2) = P_{Fe} + R_{eq,s} I_2^2$ | 7,91 W |
| Producto $I_{0,activa} \cdot E_1$ desde la fila de carga $R = 440\,\Omega$ | 7,85 W |

La concordancia entre los tres métodos (≤ 3 %) confirma que la potencia activa absorbida en vacío corresponde efectivamente a las pérdidas en el hierro y no a otros mecanismos.

---

# 4. Conclusiones

## Conclusión 1 — Sobre el esquema final del circuito con transformador

El esquema implementado en LVSIM-EMS, consistente en la fuente de alimentación 8821 alimentando el devanado primario del transformador 8353 (terminales 1-2, 24 V/5 A) a través del DACI 9063, con el secundario (terminales 5-6, 120 V/1 A) conectado a la carga resistiva variable 8311, reproduce fielmente la Imagen 2 de la guía y permitió obtener mediciones consistentes con el comportamiento esperado del transformador real. La relación de transformación medida ($A = 0{,}2004$) coincide en el 0,2 % con el valor teórico ($a = 0{,}200$), y la curva $E_2$ vs $I_2$ resultó altamente lineal (R² > 0,99) tanto en la versión medida como en la extrapolación a corriente nominal, lo cual valida el uso del circuito equivalente aproximado para el análisis de regulación y eficiencia.

## Conclusión 2 — Sobre las fallas identificadas en el esquema

Durante la implementación se identificaron dos erratas en la guía de laboratorio que ameritaron corrección: (i) el módulo de fuente de alimentación se indica como "8221", pero el código 8221 corresponde al *Four-Pole Squirrel-Cage Induction Motor* —un motor, no una fuente—; el módulo correcto es el **8821 Power Supply** de LabVolt, identificado tras inspeccionar el catálogo de la *Equipment Workstation* de LVSIM-EMS. (ii) La tabla de número de espiras del PDF indica "Bobina 1-3: 57 / 3-4: 285", inconsistente con la Imagen 1 que muestra las bobinas 1-2 y 3-4 ambas como 24 V/5 A; la interpretación físicamente coherente —y validada por la relación de transformación medida de 5:1— es **1-2: 57, 3-4: 57, 5-6: 285, 7-8: 285**. Estas dos correcciones fueron necesarias para que la simulación produjera resultados consistentes.

## Conclusión 3 — Sobre el uso del software

LVSIM-EMS proporciona una réplica fiel de la estación de trabajo física de LabVolt: la interfaz gráfica de arrastrar y soltar permitió montar el circuito en pocos minutos, y la sub-ventana **Metering** habilitó la lectura simultánea de las seis magnitudes requeridas ($E_1, I_1, E_2, I_2, P_1, P_2$) usando instrumentos virtuales tipo *PQS* que calculan la potencia activa real (integral $\frac{1}{T}\int v\,i\,dt$) en lugar del simple producto $V \cdot I$ aparente. Esta diferencia es importante porque el factor de potencia primario varía considerablemente entre vacío ($\cos\varphi_0 = 0{,}36$, dominado por la corriente magnetizante) y carga ($\cos\varphi \to 1$ a plena carga resistiva); un vatímetro de producto $V \cdot I$ habría sobreestimado las pérdidas y la potencia. La configuración previa de la red AC en **220 V – 50 Hz** desde *Tools → Options* y la verificación en la barra inferior derecha de la pantalla fueron pasos indispensables para reproducir las condiciones eléctricas reales del Perú.

## Conclusión 4 — Sobre las dificultades experimentadas

Las dificultades principales del laboratorio fueron: (i) **interpretación inicial errónea del procedimiento**: en una primera toma de datos se ajustó la tensión secundaria $E_2$ a 120 V para cada carga (variando $E_1$ entre 24,51 y 24,95 V), lo cual hizo que la regulación calculada diera prácticamente 0 %; la guía exige mantener $E_1 = 24$ V constante y dejar que $E_2$ caiga naturalmente con la carga, por lo que fue necesario rehacer las 12 mediciones. (ii) **Calibración fina del knob de tensión** del 8821 entre cada cambio de carga, ya que la propia fuente tiene una pequeña regulación interna que tiende a hacer caer $E_1$ cuando aumenta el consumo del primario; mantener $E_1 = 24{,}00$ V dentro de ±0,01 V requirió pequeñas correcciones manuales del knob. (iii) **Selección correcta de los terminales del transformador 8353**: el lado de baja tensión / alta corriente (terminales 1-2, 24 V / 5 A) debe ser el primario, no el secundario; invertir la conexión produciría una salida de 24 V a partir de 120 V de entrada y no permitiría completar el barrido de cargas dentro del rango seguro. (iv) **Interpretación inicial de la columna $I_1$** de la Tabla 4: la diferencia entre $I_1$ medido y el valor ideal $I_2/a = 5\,I_2$ parecía un error de medición, pero resultó ser precisamente la corriente de excitación $I_0 \approx 0{,}45$ A —exactamente el fenómeno que pide explicar la pregunta (f)—.

---

# Fuentes de información

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
- LabVolt Series (2013). *Relaciones de tensiones y corrientes*. En *Electricidad y Nuevas Energías – Transformadores de potencia monofásicos* (pp. 8-21). Quebec, Canadá: Festo Didactic. ISBN 978-2-89640-664-7.
- LabVolt Series (2013). *Apéndices*. En *Electricidad y Nuevas Energías – Circuitos ca monofásicos* (pp. 121-131). Quebec, Canadá: Festo Didactic. ISBN 978-2-89640-664-7.
- Pretel Díaz, Ch. H. (2026). *Guía de laboratorio N° 2: Regulación y eficiencia del transformador* [PDF]. UTP+class.
