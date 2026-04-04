---
title: "Amplificador Darlington y amplificadores operacionales"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 2
orden: 2
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/darlington
  - tema/opamp
  - tema/amplificador-inversor
  - tema/amplificador-no-inversor
  - tema/amplificador-de-instrumentacion
date: 2026-03-31
---

## Amplificador Darlington

Una conexion muy popular de dos transistores de union bipolar que opera como un transistor "super beta". El transistor compuesto actua como **una sola unidad** con una ganancia de corriente que es el **producto** de las ganancias individuales.

### Ganancia de corriente

Con transistores de ganancias $\beta_1$ y $\beta_2$:

$$\boxed{\beta_D = \beta_1 \cdot \beta_2}$$

Si ambos transistores son iguales ($\beta_1 = \beta_2 = \beta$):

$$\beta_D = \beta^2$$

> [!tip] Orden de magnitud
> Una conexion Darlington proporciona una ganancia de corriente muy grande, por lo general de **unos miles**.

### Polarizacion DC del circuito Darlington

$$I_B = \frac{V_{CC} - V_{BE}}{R_B + \beta_D R_E}$$

Donde $V_{BE}$ del par Darlington es mayor que la de un transistor individual (tipicamente $V_{BE} \approx 1.5-1.6\,V$ porque hay dos uniones BE en serie).

$$I_E = (\beta_D + 1)I_B \approx \beta_D I_B$$

$$V_E = I_E R_E$$

$$V_B = V_E + V_{BE}$$

### Ejemplo 1: Polarizacion fija Darlington

**Datos:** $V_{CC} = 18\,V$, $R_B = 3.3\,M\Omega$, $R_E = 390\,\Omega$, $\beta_D = 8000$, $V_{BE} = 1.6\,V$

**Solucion:**

$$I_B = \frac{18\,V - 1.6\,V}{3.3\,M\Omega + 8000(390\,\Omega)} = \frac{16.4\,V}{6.42\,M\Omega} \approx 2.55\,\mu A$$

$$I_E \approx 8000(2.55\,\mu A) = 20.48\,mA \approx I_C$$

$$V_E = 20.48\,mA \times 390\,\Omega \approx 8.06\,V$$

$$V_B = 8.06\,V + 1.6\,V = 9.65\,V$$

$$V_C = V_{CC} = 18\,V$$

### Ejemplo 2: Divisor de voltaje con par Darlington

**Datos:** $V_{CC} = 27\,V$, $R_1 = 470\,k\Omega$, $R_2 = 220\,k\Omega$, $R_C = 1.2\,k\Omega$, $R_E = 680\,\Omega$, $\beta_1 = \beta_2 = 110$, $V_{BE} = 1.5\,V$

**Analisis DC:**

$$\beta_D = \beta_1 \cdot \beta_2 = 110 \times 110 = 12{,}100$$

$$V_B = \frac{R_2}{R_1 + R_2} V_{CC} = \frac{220\,k\Omega \cdot 27\,V}{470\,k\Omega + 220\,k\Omega} = 8.61\,V$$

$$V_E = V_B - V_{BE} = 8.61\,V - 1.5\,V = 7.11\,V$$

$$I_E = \frac{V_E}{R_E} = \frac{7.11\,V}{680\,\Omega} = 10.46\,mA$$

$$I_B = \frac{I_E}{\beta_D} = \frac{10.46\,mA}{12{,}100} = 0.864\,\mu A$$

**Analisis AC (modelo $r_e$):**

$$r_{e_2} = \frac{26\,mV}{I_{E_2}} = \frac{26\,mV}{10.46\,mA} = 2.49\,\Omega$$

$$I_{E_1} = I_{B_2} = \frac{I_{E_2}}{\beta_2} = \frac{10.46\,mA}{110} = 0.095\,mA$$

$$r_{e_1} = \frac{26\,mV}{0.095\,mA} = 273.7\,\Omega$$

### Ganancia de corriente del par Darlington

Del circuito equivalente AC:

$$I_o = \beta_1 I_{b_1} + \beta_2 I_{b_2}$$

Como $I_{b_2} = (\beta_1 + 1)I_{b_1}$:

$$A_i' = \frac{I_o}{I_i'} = \beta_1 + \beta_2(\beta_1 + 1) \cong \beta_1 \beta_2 = \beta_D$$

Para el circuito completo con $R_1$ y $R_2$:

$$\boxed{A_i = \frac{\beta_D (R_1 \parallel R_2)}{R_1 \parallel R_2 + Z_i'}}$$

Para el ejemplo: $A_i = \dfrac{(12{,}100)(149.86\,k\Omega)}{149.86\,k\Omega + 60.24\,k\Omega} = 8630.7$

### Ganancia de voltaje

$$\boxed{A_v = \frac{\beta_D R_C}{Z_i'}}$$

Para el ejemplo: $A_v = \dfrac{(12{,}000)(1.2\,k\Omega)}{60.24\,k\Omega} = 241.04$

## Fundamentos de amplificadores operacionales

Un amplificador operacional (OPAM) es un amplificador de **muy alta ganancia** con:
- Impedancia de entrada muy alta ($\geq M\Omega$)
- Impedancia de salida baja ($\leq 100\,\Omega$)
- Dos entradas: **inversora** ($-$) y **no inversora** ($+$)

### Modelo del OPAM

$$V_s = A_0 (v_+ - v_-)$$

Donde:
- $A_0$ = ganancia interna en lazo abierto
- $10^4 \leq A_0 \leq 10^6$ (valores tipicos)
- $r_e \geq 10^6\,\Omega$ (impedancia de entrada)
- $r_s \leq 100\,\Omega$ (impedancia de salida)

### Aproximacion ideal

- $A_0 \to \infty \implies v_+ = v_-$ (tierra virtual)
- $r_{in} \to \infty \implies i_+ = i_- = 0$ (no entra corriente por las entradas)
- $r_{out} \to 0 \implies v_{out} = v_0$ (fuente de voltaje ideal)
- Limites de saturacion: $\pm V_{CC}$

### Encapsulados

- **DIP 8 pines** (LM741CN): Offset Null (1,5), Inv Input (2), Non-Inv Input (3), $V^-$ (4), Output (6), $V^+$ (7), NC (8)
- **Metal Can** (TO-99)
- **Ceramic DIP 14 pines**

## Circuitos amplificadores de senal con OPAM

### Amplificador no inversor

$$\boxed{\frac{v_{out}}{v_{in}} = \frac{R_2 + R_1}{R_2} = 1 + \frac{R_1}{R_2}}$$

$$R_{in} = \frac{v_{in}}{i_{in}} = \infty$$

### Amplificador inversor

$$\boxed{\frac{v_{out}}{v_{in}} = -\frac{R_2}{R_1}}$$

$$R_{in} = \frac{v_{in}}{i_{in}} = R_1$$

### Seguidor de voltaje (buffer)

$$\frac{v_{out}}{v_{in}} = 1$$

### Amplificador diferencial (restador)

Con la condicion $\dfrac{R_4}{R_3} = \dfrac{R_2}{R_1}$:

$$\boxed{v_o = \frac{R_2}{R_1}(v_1 - v_2)}$$

## Circuitos operadores de senal

### Amplificador sumador

$$\boxed{v_{out} = -R_f \left(\frac{v_1}{R_1} + \frac{v_2}{R_2} + \cdots + \frac{v_n}{R_n}\right)}$$

### Integrador

$$\boxed{v_{out} = \frac{-1}{RC} \int v_{in}\,dt}$$

### Diferenciador

$$\boxed{v_{out} = -RC \frac{dv_{in}}{dt}}$$

### Comparador

Sin realimentacion (lazo abierto):
- Si $v_i = v_2 - v_1 > 0 \implies v_o = +V_{SAT}$
- Si $v_i = v_2 - v_1 < 0 \implies v_o = -V_{SAT}$

## Circuitos convertidores de senal

### Convertidor Digital/Analogico (D/A)

Produce una salida igual a la **suma ponderada** de las entradas digitales. Para un DAC de 4 bits con resistencias ponderadas por potencias de 2:

$$R_0 = R_0, \quad R_1 = R_0/2, \quad R_2 = R_0/4, \quad R_3 = R_0/8$$

$$R_f = R_3 \text{ (resistencia mas baja)}$$

### Convertidor Analogico/Digital (A/D)

Produce un conjunto de salidas con solo dos niveles de voltaje (0 y 1) a partir de un rango de voltajes a la entrada.

$$\text{Resolucion} = \frac{V_{ref}}{n + 1}$$

Donde $n$ = numero de bits de salida.

## Amplificador de instrumentacion

Circuito de dos etapas con 3 amplificadores operacionales ($X_1$, $X_2$, $X_3$):

**Primera etapa:** Dos OPAM no inversores con resistencia comun $R_1$

$$i_{R1} = \frac{v_1 - v_2}{2R_1}$$

$$v_{o,x2} - v_{o,x1} = \left(1 + \frac{R_2}{R_1}\right)(v_1 - v_2)$$

**Segunda etapa:** Amplificador diferencial con resistencias $R$

$$\boxed{v_o = \left(1 + \frac{R_2}{R_1}\right)(v_1 - v_2)}$$

> [!tip] Ventaja
> La ganancia se ajusta con una sola resistencia ($R_1$), sin afectar el rechazo de modo comun.

## Aplicaciones tipicas de los OPAM

| Categoria | Circuitos |
| --------- | --------- |
| Amplificadores de senal | Inversor, No inversor |
| Operadores de senal | Sumador, Derivador, Integrador, Comparador |
| Convertidores de senal | D/A, A/D |
| Filtros activos | Paso bajo, Paso alto, Paso banda, Banda eliminada |

## Bibliografia

- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson.
