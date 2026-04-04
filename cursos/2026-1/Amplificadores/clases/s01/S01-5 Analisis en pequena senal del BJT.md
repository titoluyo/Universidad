---
title: "Analisis en pequena senal del BJT"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 1
orden: 5
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/pequena-senal
  - tema/modelo-hibrido
  - tema/modelo-re
  - tema/ganancia
date: 2026-03-31
---

## Introduccion

Para que los transistores BJT funcionen como **amplificadores** de corriente, se debe aplicar una pequena senal de corriente en la terminal base para controlar una corriente de salida mayor en las terminales colector y emisor.

La configuracion en emisor comun produce un **desfasamiento de 180°** entre las formas de onda de entrada y salida.

## Cuadripolos para pequena senal

Un **cuadripolo** es un circuito con 4 nudos (polos) accesibles desde el exterior, agrupados en 2 puertos. Los cuadripolos representan las caracteristicas electricas sin necesidad de conocer la topologia y componentes internos.

### Cuadripolo tipo H

Se usan cuadripolos **H** que consideran como variables independientes $i_1$ y $v_2$, siendo dependientes $v_1$ e $i_2$:

$$v_1 = h_i \cdot i_1 + h_r \cdot v_2$$

$$i_2 = h_f \cdot i_1 + h_o \cdot v_2$$

Donde los parametros hibridos se definen como:

$$h_i = \left.\frac{v_1}{i_1}\right|_{v_2=0} \quad \text{(impedancia de entrada, salida en cortocircuito)}$$

$$h_r = \left.\frac{v_1}{v_2}\right|_{i_1=0} \quad \text{(ganancia inversa de voltaje, entrada abierta)}$$

$$h_f = \left.\frac{i_2}{i_1}\right|_{v_2=0} \quad \text{(ganancia directa de corriente, salida en cortocircuito)}$$

$$h_o = \left.\frac{i_2}{v_2}\right|_{i_1=0} \quad \text{(admitancia de salida, entrada abierta)}$$

## Modelo de un transistor BJT

Un **modelo** es una combinacion de elementos de un circuito, apropiadamente seleccionados, que simula de forma aproximada el comportamiento real de un dispositivo semiconductor en condiciones especificas de operacion.

## Modelos H de un transistor bipolar

El transistor tiene 3 terminales pero el cuadripolo tiene 4 nudos. Se comparte un terminal como polo tanto de entrada como de salida, dando lugar a 3 configuraciones:

| Configuracion | $v_1$ | $v_2$ | $i_1$ | $i_2$ |
| ------------- | ------ | ------ | ------ | ------ |
| **EC** (Emisor Comun) | $V_{BE}$ | $V_{CE}$ | $i_B$ | $i_C$ |
| **BC** (Base Comun) | $V_{EB}$ | $V_{CB}$ | $-i_E$ | $i_C$ |
| **CC** (Colector Comun) | $V_{BC}$ | $V_{EC}$ | $i_B$ | $-i_E$ |

## Modelo H de la configuracion EC

### Derivacion mediante Taylor

Se desarrollan las funciones $v_{BE}(i_B, v_{CE})$ e $i_C(i_B, v_{CE})$ en serie de Taylor de primer orden alrededor del punto de operacion ($I_B$, $V_{CE}$):

$$v_{BE} \approx V_{BE} + \frac{\partial v_{BE}}{\partial i_B} \cdot (i_B - I_B) + \frac{\partial v_{BE}}{\partial v_{CE}} \cdot (v_{CE} - V_{CE})$$

$$i_C \approx I_C + \frac{\partial i_C}{\partial i_B} \cdot (i_B - I_B) + \frac{\partial i_C}{\partial v_{CE}} \cdot (v_{CE} - V_{CE})$$

Las variaciones de pequena senal resultan:

$$\boxed{v_{be} \approx h_{ie} \cdot i_b + h_{re} \cdot v_{ce}}$$

$$\boxed{i_c \approx h_{fe} \cdot i_b + h_{oe} \cdot v_{ce}}$$

Este es el **modelo H de pequena senal de un EC**.

### Circuito equivalente completo

El modelo H del emisor comun consiste en:
- **Entrada:** Resistencia $h_{ie}$ en serie con fuente dependiente de voltaje $h_{re} \cdot v_{ce}$
- **Salida:** Fuente dependiente de corriente $h_{fe} \cdot i_b$ en paralelo con admitancia $h_{oe}$

> [!important] Universalidad del modelo
> - Valido tanto para NPN como para PNP
> - Cualquier transistor, sea cual sea su configuracion, se puede sustituir por el modelo de parametros H de EC

### Parametros H del fabricante

Los parametros H pueden extraerse del modelo Ebers-Moll, pero en la practica los fabricantes los proporcionan tabulados para distintos puntos de operacion.

Unicamente $h_{fe}$ es conocido de forma sencilla, ya que en zona activa:

$$h_{fe} \approx \frac{\partial i_C}{\partial i_B} \approx \beta$$

## Modelo H simplificado

Para la mayoria de casos practicos: $h_{re} \approx 0$ y $h_{oe} \to \infty$ (circuito abierto en la salida).

El modelo simplificado queda:
- **Entrada:** Solo la resistencia $h_{ie}$
- **Salida:** Solo la fuente de corriente $h_{fe} \cdot i_b$

> [!tip] Aplicacion
> Cualquier transistor, sea cual sea su configuracion, se puede sustituir por el modelo de parametros H simplificado de EC.

## Analisis general de un circuito amplificador a frecuencias medias

Para analizar un circuito amplificador a frecuencias medias:

1. Los **condensadores de acoplo** ($C_1$, $C_2$) se comportan como cortocircuitos ($Z_C \to \infty$ a frecuencias medias, pero dejan pasar la senal AC)
2. Se **pasivan las fuentes independientes de continua** ($V_{CC} \to$ cortocircuito a tierra)
3. Las resistencias del divisor de voltaje quedan en paralelo: $R_{B1} \parallel R_{B2}$

## Caracteristicas de la configuracion EC con parametros H

### Ganancia de corriente

$$A_I = \frac{i_o}{i_i} = \frac{-h_{fe} \cdot i_b}{i_b} = -h_{fe}$$

### Ganancia de voltaje

$$A_V = \frac{v_o}{v_i} = \frac{i_o \cdot R_L}{i_b \cdot h_{ie}} = -h_{fe} \frac{R_L}{h_{ie}}$$

### Impedancia de entrada

$$R_i = \frac{v_i}{i_i} = h_{ie}$$

## Modelo $r_e$ del transistor BJT

El modelo $r_e$ es una buena aproximacion del comportamiento real del transistor BJT para las configuraciones en emisor comun, base comun y colector comun.

### Configuracion en emisor comun

La resistencia dinamica del emisor:

$$\boxed{r_e = \frac{26\,mV}{I_E}}$$

La impedancia de entrada vista desde la base:

$$V_{be} = I_e r_e = (I_c + I_b) r_e = (\beta I_b + I_b) r_e = (\beta + 1) I_b r_e$$

$$Z_i = \frac{V_{be}}{I_b} = (\beta + 1) r_e \cong \beta r_e$$

### Circuito equivalente $r_e$ del BJT

- **Entre base y emisor:** Resistencia $\beta r_e$
- **Entre colector y emisor:** Fuente de corriente dependiente $\beta I_b$

### Ganancia de voltaje (EC sin $R_E$ desacoplada)

$$A_V = -\frac{R_C}{r_e}$$

> [!note] Signo negativo
> El signo negativo indica el desfasamiento de 180° entre entrada y salida, caracteristico de la configuracion emisor comun.

### Ganancia de voltaje (EC con $R_E$ sin desacoplar)

$$A_V \cong -\frac{\beta R_C}{Z_b}$$

Donde $Z_b = \beta r_e + (\beta + 1)R_E \cong \beta(r_e + R_E)$

### Ganancia de voltaje (Emisor seguidor / CC)

$$A_V = \frac{R_E}{R_E + r_e} \cong 1$$

## Ejercicios resueltos

### Ejemplo 1: Polarizacion fija (EC sin $R_E$)

**Datos:** $V_{CC} = 12\,V$, $R_B = 470\,k\Omega$, $R_C = 3\,k\Omega$, $\beta = 100$

**a) Analisis de CD:**

$$I_B = \frac{V_{CC} - V_{BE}}{R_B} = \frac{12\,V - 0.7\,V}{470\,k\Omega} = 24.04\,\mu A$$

$$I_E = (\beta + 1)I_B = (101)(24.04\,\mu A) = 2.428\,mA$$

$$r_e = \frac{26\,mV}{I_E} = \frac{26\,mV}{2.428\,mA} = 10.71\,\Omega$$

**b) Ganancia de voltaje:**

$$\beta r_e = (100)(10.71\,\Omega) = 1.071\,k\Omega$$

$$A_V = -\frac{R_C}{r_e} = -\frac{3\,k\Omega}{10.71\,\Omega} = \mathbf{-280.11}$$

### Ejemplo 2: Divisor de voltaje (EC sin $R_E$ desacoplada)

**Datos:** $V_{CC} = 22\,V$, $R_1 = 56\,k\Omega$, $R_2 = 8.2\,k\Omega$, $R_C = 6.8\,k\Omega$, $R_E = 1.5\,k\Omega$, $\beta = 90$

**a) Analisis de CD:**

$$V_B = \frac{R_2}{R_1 + R_2} V_{CC} = \frac{(8.2\,k\Omega)(22\,V)}{56\,k\Omega + 8.2\,k\Omega} = 2.81\,V$$

$$V_E = V_B - V_{BE} = 2.81\,V - 0.7\,V = 2.11\,V$$

$$I_E = \frac{V_E}{R_E} = \frac{2.11\,V}{1.5\,k\Omega} = 1.41\,mA$$

$$r_e = \frac{26\,mV}{1.41\,mA} = 18.44\,\Omega$$

**b) Ganancia de voltaje:**

$$A_V = -\frac{R_C}{r_e} = -\frac{6.8\,k\Omega}{18.44\,\Omega} = \mathbf{-368.76}$$

### Ejemplo 3: Polarizacion con $R_E$ (EC con $R_E$ sin desacoplar)

**Datos:** $V_{CC} = 20\,V$, $R_B = 470\,k\Omega$, $R_C = 2.2\,k\Omega$, $R_E = 0.56\,k\Omega$, $\beta = 120$

**a) Analisis de CD:**

$$I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1)R_E} = \frac{20\,V - 0.7\,V}{470\,k\Omega + (121)(0.56\,k\Omega)} = 35.89\,\mu A$$

$$I_E = (\beta + 1)I_B = (121)(35.89\,\mu A) = 4.34\,mA$$

$$r_e = \frac{26\,mV}{4.34\,mA} = 5.99\,\Omega$$

**b) Ganancia de voltaje:**

$$Z_b = \beta r_e + (\beta + 1)R_E \approx \beta(r_e + R_E)$$

$$A_V \cong -\frac{\beta R_C}{Z_b} = -\frac{(120)(2.2\,k\Omega)}{67.92\,k\Omega} = \mathbf{-3.89}$$

> [!warning] Efecto de $R_E$ sin desacoplar
> La ganancia cae drasticamente (de ~280 a ~3.9) cuando $R_E$ no esta desacoplada con un condensador, pero se mejora la estabilidad del punto Q.

### Ejemplo 4: Emisor seguidor (CC)

**Datos:** $V_{CC} = 12\,V$, $R_B = 220\,k\Omega$, $R_E = 3.3\,k\Omega$, $\beta = 100$

**a) Analisis de CD:**

$$I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1)R_E} = \frac{12\,V - 0.7\,V}{220\,k\Omega + (101)(3.3\,k\Omega)} = 20.42\,\mu A$$

$$I_E = (\beta + 1)I_B = (101)(20.42\,\mu A) = 2.062\,mA$$

$$r_e = \frac{26\,mV}{2.062\,mA} = 12.61\,\Omega$$

**b) Ganancia de voltaje:**

$$A_V = \frac{R_E}{R_E + r_e} = \frac{3.3\,k\Omega}{3.3\,k\Omega + 12.61\,\Omega} = 0.996 \cong \mathbf{1}$$

> [!tip] Emisor seguidor
> La ganancia de voltaje es practicamente 1 (seguidor de voltaje). Su utilidad radica en la **alta impedancia de entrada** y **baja impedancia de salida** (adaptador de impedancias).

## Bibliografia

- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson.
