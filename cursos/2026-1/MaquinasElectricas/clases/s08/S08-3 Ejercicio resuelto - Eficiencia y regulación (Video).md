---
title: Ejercicio resuelto - Parámetros y regulación de un transformador
curso: "[[Motores MOC]]"
unidad: 2
semana: 8
orden: 3
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/transformador-real
  - tema/admitancia-excitacion
  - tema/regulacion-tension
  - tema/ensayo-vacio
  - tema/ensayo-cortocircuito
date: 2026-05-11
---

> [!info] Fuente
> Video "Desarrollo de un ejercicio de eficiencia y regulación de un transformador" (Semana 08, Tema 02). Transcripción completa en [[#Guion del video|el Guion]] adjunto al final.

## Enunciado

Se va a probar un transformador de **15 kVA**, **2 300/230 V**, para determinar los componentes de la **rama de excitación**, sus **impedancias en serie** y su **regulación de voltaje**. Se obtuvieron los siguientes datos de las pruebas:

| Prueba | Medido en | $V$ | $I$ | $P$ |
| ------ | --------- | --- | --- | --- |
| **Vacío** | secundario (BT) | 230 V | 2,1 A | 50 W |
| **Cortocircuito** | primario (AT) | 47 V | 6 A | 160 W |

Se pide:
- **1)** Encontrar el circuito equivalente referido al **lado de alto voltaje** (primario).
- **2)** Encontrar el circuito equivalente referido al **lado de bajo voltaje** (secundario).
- **3)** Calcular la **regulación de voltaje** a plena carga con factor de potencia **0,8 en retraso**, **1** y **0,8 en adelanto**, usando la ecuación exacta.

## Datos

| Magnitud | Símbolo | Valor |
| -------- | ------- | ----- |
| Potencia nominal | $S_n$ | 15 kVA |
| Tensión primaria | $V_{1n}$ | 2 300 V |
| Tensión secundaria | $V_{2n}$ | 230 V |
| Vacío (BT) — voltaje | $V_0$ | 230 V |
| Vacío (BT) — corriente | $I_0$ | 2,1 A |
| Vacío — potencia | $P_0$ | 50 W |
| CC (AT) — voltaje | $V_{cc}$ | 47 V |
| CC (AT) — corriente | $I_{cc}$ | 6 A |
| CC — potencia | $P_{cc}$ | 160 W |

## Desarrollo

### Relación de transformación

$$a = \frac{V_{1n}}{V_{2n}} = \frac{2\,300}{230} = 10$$

### 1) Circuito equivalente referido al primario

#### Rama de excitación (calculada en BT y reflejada al AT)

Como el ensayo de vacío se midió en BT, calculamos primero la admitancia $\mathbf{Y}_E$ **referida al secundario** y luego la reflejamos.

**Factor de potencia en vacío:**

$$\cos\varphi_0 = \frac{P_0}{V_0 \cdot I_0} = \frac{50}{230 \cdot 2{,}1} = \frac{50}{483} \approx 0{,}1035$$

$$\varphi_0 = \cos^{-1}(0{,}1035) \approx 84°$$

**Admitancia de excitación** (ver [[S08-1 Tema 01 - Determinación de los parámetros del transformador#Cálculo desde las medidas|cálculo]]):

$$|\mathbf{Y}_E| = \frac{I_0}{V_0} = \frac{2{,}1}{230} \approx 9{,}13 \times 10^{-3}\,\text{S}$$

$$\mathbf{Y}_E = 9{,}13 \times 10^{-3} \angle (-84°)\,\text{S}$$

En forma rectangular:

$$\boxed{\;\mathbf{Y}_E = G_{Fe} - jB_\mu = 9{,}54 \times 10^{-4} - j\,9{,}08 \times 10^{-3}\,\text{S}\;}$$

Componentes referidos al secundario:

$$R_{Fe}^{(BT)} = \frac{1}{G_{Fe}} = \frac{1}{9{,}54 \times 10^{-4}} \approx 1\,050\,\Omega$$

$$X_\mu^{(BT)} = \frac{1}{B_\mu} = \frac{1}{9{,}08 \times 10^{-3}} \approx 110\,\Omega$$

Reflejando al primario (×$a^2 = 100$):

$$\boxed{\;R_{Fe}^{(AT)} = 100 \cdot 1\,050 = 105\,\text{k}\Omega \hspace{0.5cm};\hspace{0.5cm} X_\mu^{(AT)} = 100 \cdot 110 = 11\,\text{k}\Omega\;}$$

#### Impedancia serie (calculada directamente en AT)

**Factor de potencia en cortocircuito:**

$$\cos\varphi_{cc} = \frac{P_{cc}}{V_{cc} \cdot I_{cc}} = \frac{160}{47 \cdot 6} = \frac{160}{282} \approx 0{,}567$$

$$\varphi_{cc} = \cos^{-1}(0{,}567) \approx 55{,}4°$$

**Impedancia serie:**

$$|\mathbf{Z}_{serie}| = \frac{V_{cc}}{I_{cc}} = \frac{47}{6} \approx 7{,}83\,\Omega$$

$$\mathbf{Z}_{serie} = 7{,}83 \angle 55{,}4°\,\Omega$$

En forma rectangular:

$$\boxed{\;\mathbf{Z}_{serie}^{(AT)} = 4{,}45 + j\,6{,}45\,\Omega\;}$$

$$R_{eq}^{(AT)} = 4{,}45\,\Omega \hspace{0.5cm};\hspace{0.5cm} X_{eq}^{(AT)} = 6{,}45\,\Omega$$

#### Resumen circuito al primario

| Parámetro | Valor |
| --------- | ----- |
| $R_{Fe}$ | $105\,\text{k}\Omega$ |
| $X_\mu$ | $11\,\text{k}\Omega$ |
| $R_{eq}$ ($= R_1 + a^2 R_2$) | $4{,}45\,\Omega$ |
| $X_{eq}$ ($= X_1 + a^2 X_2$) | $6{,}45\,\Omega$ |

### 2) Circuito equivalente referido al secundario

Para reducir al secundario, dividir las impedancias entre $a^2 = 100$:

$$R_{eq}^{(BT)} = \frac{R_{eq}^{(AT)}}{a^2} = \frac{4{,}45}{100} = 0{,}0445\,\Omega$$

$$X_{eq}^{(BT)} = \frac{X_{eq}^{(AT)}}{a^2} = \frac{6{,}45}{100} = 0{,}0645\,\Omega$$

#### Resumen circuito al secundario

| Parámetro | Valor |
| --------- | ----- |
| $R_{Fe}$ | $1\,050\,\Omega$ |
| $X_\mu$ | $110\,\Omega$ |
| $R_{eq}$ | $0{,}0445\,\Omega$ |
| $X_{eq}$ | $0{,}0645\,\Omega$ |

### 3) Regulación de voltaje a plena carga

#### Corriente nominal en el secundario

$$I_S = \frac{S_n}{V_{2n}} = \frac{15\,000}{230} \approx 65{,}22\,\text{A}$$

#### Ecuación exacta (todos los valores referidos al secundario)

$$\frac{\mathbf{V}_P}{a} = \mathbf{V}_S + (R_{eq} + jX_{eq}) \cdot \mathbf{I}_S$$

$$RV = \frac{|V_P/a| - V_S}{V_S} \cdot 100\,\%$$

Tomamos $\mathbf{V}_S = 230 \angle 0°\,\text{V}$ como referencia. El ángulo de $\mathbf{I}_S$ depende del factor de potencia.

#### Caso 1: $\cos\theta = 0{,}8$ en **retraso** (inductivo)

$$\mathbf{I}_S = 65{,}22 \angle (-36{,}9°)\,\text{A}$$

Calculando $(0{,}0445 + j\,0{,}0645) \cdot \mathbf{I}_S$:
- Real: $0{,}0445 \cdot 65{,}22 \cdot \cos(-36{,}9°) - 0{,}0645 \cdot 65{,}22 \cdot \sin(-36{,}9°) = 2{,}322 + 2{,}524 = 4{,}846$
- Imag: $0{,}0445 \cdot 65{,}22 \cdot \sin(-36{,}9°) + 0{,}0645 \cdot 65{,}22 \cdot \cos(-36{,}9°) = -1{,}741 + 3{,}366 = 1{,}625$

$$\frac{\mathbf{V}_P}{a} = 230 + 4{,}846 + j\,1{,}625 = 234{,}85 + j\,1{,}625$$

$$\left|\frac{V_P}{a}\right| = \sqrt{234{,}85^2 + 1{,}625^2} \approx 234{,}86\,\text{V}$$

$$RV = \frac{234{,}86 - 230}{230} \cdot 100\,\%$$

$$\boxed{\;RV_{0{,}8\,\text{ind}} \approx 2{,}1\,\%\;}$$

#### Caso 2: $\cos\theta = 1$ (resistivo)

$$\mathbf{I}_S = 65{,}22 \angle 0°\,\text{A}$$

$$(R_{eq} + jX_{eq}) \cdot \mathbf{I}_S = (0{,}0445 + j\,0{,}0645) \cdot 65{,}22 = 2{,}903 + j\,4{,}207$$

$$\frac{\mathbf{V}_P}{a} = 230 + 2{,}903 + j\,4{,}207 = 232{,}90 + j\,4{,}207$$

$$\left|\frac{V_P}{a}\right| = \sqrt{232{,}90^2 + 4{,}207^2} \approx 232{,}94\,\text{V}$$

$$\boxed{\;RV_{\cos\theta=1} \approx 1{,}28\,\%\;}$$

#### Caso 3: $\cos\theta = 0{,}8$ en **adelanto** (capacitivo)

$$\mathbf{I}_S = 65{,}22 \angle 36{,}9°\,\text{A}$$

Calculando $(0{,}0445 + j\,0{,}0645) \cdot \mathbf{I}_S$:
- Real: $0{,}0445 \cdot 65{,}22 \cdot \cos(36{,}9°) - 0{,}0645 \cdot 65{,}22 \cdot \sin(36{,}9°) = 2{,}322 - 2{,}524 = -0{,}202$
- Imag: $0{,}0445 \cdot 65{,}22 \cdot \sin(36{,}9°) + 0{,}0645 \cdot 65{,}22 \cdot \cos(36{,}9°) = 1{,}741 + 3{,}366 = 5{,}107$

$$\frac{\mathbf{V}_P}{a} = 230 - 0{,}202 + j\,5{,}107 = 229{,}80 + j\,5{,}107$$

$$\left|\frac{V_P}{a}\right| = \sqrt{229{,}80^2 + 5{,}107^2} \approx 229{,}86\,\text{V}$$

$$\boxed{\;RV_{0{,}8\,\text{cap}} \approx -0{,}06\,\%\;}$$

> [!note] Discrepancia con el video
> En el video el docente reporta $\approx -0{,}62\,\%$, pero parece ser un error de lectura — el cálculo con los mismos parámetros entrega $-0{,}06\,\%$. Lo importante es el **signo negativo**: con carga capacitiva, la tensión en el secundario **sube** por encima del valor nominal (efecto Ferranti reducido).

## Resumen de resultados

| Magnitud | Valor |
| -------- | ----- |
| $a$ | $10$ |
| $\mathbf{Y}_E$ (BT) | $9{,}54 \times 10^{-4} - j\,9{,}08 \times 10^{-3}$ S |
| $\mathbf{Z}_{serie}$ (AT) | $4{,}45 + j\,6{,}45$ Ω |
| $R_{Fe}$ / $X_\mu$ al primario | $105$ kΩ / $11$ kΩ |
| $R_{Fe}$ / $X_\mu$ al secundario | $1\,050$ Ω / $110$ Ω |
| $R_{eq}$ / $X_{eq}$ al primario | $4{,}45$ Ω / $6{,}45$ Ω |
| $R_{eq}$ / $X_{eq}$ al secundario | $0{,}0445$ Ω / $0{,}0645$ Ω |
| $I_S$ a plena carga | $65{,}22$ A |
| **RV** @ $\cos\theta = 0{,}8$ ind | $\approx 2{,}1\,\%$ |
| **RV** @ $\cos\theta = 1$ | $\approx 1{,}28\,\%$ |
| **RV** @ $\cos\theta = 0{,}8$ cap | $\approx -0{,}06\,\%$ |

> [!tip] Interpretación
> El RV depende fuertemente del **factor de potencia** de la carga:
> - **Inductivo** → RV positivo grande (tensión cae al cargar).
> - **Resistivo** → RV positivo moderado.
> - **Capacitivo** → RV puede ser **negativo** (tensión sube al cargar).
>
> Los transformadores se especifican típicamente con RV referida al peor caso (inductivo, $\cos\theta \approx 0{,}8$ a $0{,}9$).

## Guion del video

![[s08-t02-ej-guion-eficiencia-regulacion.pdf]]

## Bibliografía

- Chapman, S. J. (2005). *Máquinas Eléctricas* (4.ª ed.). McGraw-Hill Interamericana.
