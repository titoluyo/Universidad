---
title: "Ejercicios de transistor bipolar en DC"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 1
orden: 4
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/polarizacion
  - tema/transistor-bjt
  - tema/punto-de-operacion
date: 2026-03-31
---

## Circuitos de polarizacion

Resumen de las configuraciones de polarizacion del transistor BJT en DC y ejercicios resueltos para cada una.

### Tipos de polarizacion cubiertos

| Configuracion | Caracteristica principal |
| ------------- | ----------------------- |
| Polarizacion fija | $I_B$ constante, depende de $\beta$ |
| Estabilizada por emisor | Mejora estabilidad con $R_E$ |
| Divisor de voltaje | No depende de $\beta$ (Thevenin) |
| Base comun | Baja impedancia de entrada, alta de salida |
| Realimentacion de colector | $R_B$ conectada al colector, realimentacion negativa |
| Emisor seguidor | Salida en el emisor, ganancia de voltaje $\approx 1$ |

## Polarizacion fija

### Formulas

$$I_B = \frac{V_{CC} - V_{BE}}{R_B} \approx \frac{V_{CC}}{R_B} = \text{cte}$$

$$I_C = \beta I_B$$

$$V_{CE} = V_{CC} - I_C R_C$$

### Ejemplo

**Datos:** $V_{CC} = 12\,V$, $R_B = 240\,k\Omega$, $R_C = 2.2\,k\Omega$, $\beta = 50$

**Determinar:** $I_{B_Q}$, $I_{C_Q}$, $V_{CE_Q}$, $V_B$, $V_C$, $V_{BC}$

**Solucion:**

**a)** Corriente de base y colector:

$$I_{B_Q} = \frac{V_{CC} - V_{BE}}{R_B} = \frac{12\,V - 0.7\,V}{240\,k\Omega} = 47.08\,\mu A$$

$$I_{C_Q} = \beta I_{B_Q} = (50)(47.08\,\mu A) = 2.35\,mA$$

**b)** Voltaje colector-emisor:

$$V_{CE_Q} = V_{CC} - I_C R_C = 12\,V - (2.35\,mA)(2.2\,k\Omega) = 6.83\,V$$

**c)** Voltajes nodales:

$$V_B = V_{BE} = 0.7\,V$$

$$V_C = V_{CE} = 6.83\,V$$

**d)** Voltaje base-colector:

$$V_{BC} = V_B - V_C = 0.7\,V - 6.83\,V = -6.13\,V$$

> [!tip] Verificacion
> El signo negativo de $V_{BC}$ revela que la union esta polarizada en inversa, como debe ser para amplificacion lineal.

## Polarizacion estabilizada por emisor

En este circuito se mejora la estabilidad del transistor al agregar una resistencia $R_E$ en el emisor.

### Formulas

$$I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1)R_E}$$

$$I_C = \beta I_B$$

$$V_{CE} = V_{CC} - I_C(R_C + R_E)$$

$$V_C = V_{CC} - I_C R_C$$

$$V_E = I_E R_E \cong I_C R_E$$

$$V_B = V_{BE} + V_E$$

### Ejemplo

**Datos:** $V_{CC} = 20\,V$, $R_B = 430\,k\Omega$, $R_C = 2\,k\Omega$, $R_E = 1\,k\Omega$, $\beta = 50$

**Determinar:** $I_B$, $I_C$, $V_{CE}$, $V_C$, $V_E$, $V_B$, $V_{BC}$

**Solucion:**

**a)** Corriente de base:

$$I_B = \frac{V_{CC} - V_{BE}}{R_B + (\beta + 1)R_E} = \frac{20\,V - 0.7\,V}{430\,k\Omega + (51)(1\,k\Omega)} = \frac{19.3\,V}{481\,k\Omega} = 40.1\,\mu A$$

**b)** Corriente de colector:

$$I_C = \beta I_B = (50)(40.1\,\mu A) \cong 2.01\,mA$$

**c)** Voltaje colector-emisor:

$$V_{CE} = V_{CC} - I_C(R_C + R_E) = 20\,V - (2.01\,mA)(2\,k\Omega + 1\,k\Omega) = 20\,V - 6.03\,V = 13.97\,V$$

**d)** Voltaje en el colector:

$$V_C = V_{CC} - I_C R_C = 20\,V - (2.01\,mA)(2\,k\Omega) = 20\,V - 4.02\,V = 15.98\,V$$

**e)** Voltaje en el emisor:

$$V_E = V_C - V_{CE} = 15.98\,V - 13.97\,V = 2.01\,V$$

O tambien: $V_E = I_E R_E \cong I_C R_E = (2.01\,mA)(1\,k\Omega) = 2.01\,V$

**f)** Voltaje en la base:

$$V_B = V_{BE} + V_E = 0.7\,V + 2.01\,V = 2.71\,V$$

**g)** Voltaje base-colector:

$$V_{BC} = V_B - V_C = 2.71\,V - 15.98\,V = -13.27\,V \quad \text{(polarizacion en inversa)}$$

## Polarizacion con divisor de voltaje

Es un circuito de polarizacion que **no depende del valor $\beta$**. Se resuelve mediante el equivalente de Thevenin.

### Procedimiento de solucion

**Paso 1:** Identificar el circuito con $R_1$, $R_2$, $R_C$, $R_E$

**Paso 2:** Separar la red del divisor de voltaje del transistor

**Paso 3:** Hallar $R_{Th}$:

$$R_{Th} = R_1 \parallel R_2 = \frac{R_1 \cdot R_2}{R_1 + R_2}$$

**Paso 4:** Hallar $E_{Th}$:

$$E_{Th} = \frac{R_2 \cdot V_{CC}}{R_1 + R_2}$$

**Paso 5:** Dibujar el circuito equivalente de Thevenin

**Paso 6:** Hallar $I_B$ y $V_{CE}$:

$$I_B = \frac{E_{Th} - V_{BE}}{R_{Th} + (\beta + 1)R_E}$$

$$I_C = \beta I_B$$

$$V_{CE} = V_{CC} - I_C(R_C + R_E)$$

### Ejemplo

**Datos:** $V_{CC} = 22\,V$, $R_1 = 39\,k\Omega$, $R_2 = 3.9\,k\Omega$, $R_C = 10\,k\Omega$, $R_E = 1.5\,k\Omega$, $\beta = 100$

**Determinar:** $V_{CE}$ e $I_C$

**Solucion:**

Resistencia de Thevenin:

$$R_{Th} = R_1 \parallel R_2 = \frac{(39\,k\Omega)(3.9\,k\Omega)}{39\,k\Omega + 3.9\,k\Omega} = 3.55\,k\Omega$$

Voltaje de Thevenin:

$$E_{Th} = \frac{R_2 \cdot V_{CC}}{R_1 + R_2} = \frac{(3.9\,k\Omega)(22\,V)}{39\,k\Omega + 3.9\,k\Omega} = 2\,V$$

Corriente de base:

$$I_B = \frac{E_{Th} - V_{BE}}{R_{Th} + (\beta + 1)R_E} = \frac{2\,V - 0.7\,V}{3.55\,k\Omega + (101)(1.5\,k\Omega)} = \frac{1.3\,V}{3.55\,k\Omega + 151.5\,k\Omega} = 8.38\,\mu A$$

Corriente de colector:

$$I_C = \beta I_B = (100)(8.38\,\mu A) = 0.84\,mA$$

Voltaje colector-emisor:

$$V_{CE} = V_{CC} - I_C(R_C + R_E) = 22\,V - (0.84\,mA)(10\,k\Omega + 1.5\,k\Omega) = 22\,V - 9.66\,V = \mathbf{12.34\,V}$$

## Polarizacion con base comun

Tiene muy buena ganancia, una **baja impedancia de entrada** y una **alta impedancia de salida**.

### Formulas

Malla del emisor:

$$I_E = \frac{V_{EE} - V_{BE}}{R_E}$$

Malla completa:

$$V_{CE} = V_{EE} + V_{CC} - I_E(R_C + R_E)$$

Voltaje colector-base:

$$V_{CB} = V_{CC} - I_C R_C$$

### Ejemplo

**Datos:** $V_{EE} = 4\,V$, $V_{CC} = 10\,V$, $R_E = 1.2\,k\Omega$, $R_C = 2.4\,k\Omega$, $\beta = 60$

**Determinar:** $I_E$, $I_B$, $V_{CE}$, $V_{CB}$

**Solucion:**

Corriente de emisor:

$$I_E = \frac{V_{EE} - V_{BE}}{R_E} = \frac{4\,V - 0.7\,V}{1.2\,k\Omega} = 2.75\,mA$$

Corriente de base:

$$I_B = \frac{I_E}{\beta + 1} = \frac{2.75\,mA}{60 + 1} = \frac{2.75\,mA}{61} = 45.08\,\mu A$$

Voltaje colector-emisor:

$$V_{CE} = V_{EE} + V_{CC} - I_E(R_C + R_E) = 4\,V + 10\,V - (2.75\,mA)(2.4\,k\Omega + 1.2\,k\Omega)$$

$$= 14\,V - (2.75\,mA)(3.6\,k\Omega) = 14\,V - 9.9\,V = \mathbf{4.1\,V}$$

Voltaje colector-base:

$$V_{CB} = V_{CC} - I_C R_C = V_{CC} - \beta I_B R_C = 10\,V - (60)(45.08\,\mu A)(2.4\,k\Omega)$$

$$= 10\,V - 6.49\,V = \mathbf{3.51\,V}$$

## Configuracion de realimentacion de colector

### Formulas

$$I_B = \frac{V_{CC} - V_{BE}}{R_B + \beta(R_C + R_E)}$$

$$I_C = \beta I_B$$

$$V_{CE} = V_{CC} - I_C(R_C + R_E)$$

### Ejemplo

**Datos:** $V_{CC} = 10\,V$, $R_B = 250\,k\Omega$, $R_C = 4.7\,k\Omega$, $R_E = 1.2\,k\Omega$, $\beta = 90$

**Determinar:** $I_{C_Q}$ y $V_{CE_Q}$

**Solucion:**

$$I_B = \frac{V_{CC} - V_{BE}}{R_B + \beta(R_C + R_E)} = \frac{10\,V - 0.7\,V}{250\,k\Omega + (90)(4.7\,k\Omega + 1.2\,k\Omega)} = \frac{9.3\,V}{250\,k\Omega + 531\,k\Omega} = \frac{9.3\,V}{781\,k\Omega} = 11.91\,\mu A$$

$$I_{C_Q} = \beta I_B = (90)(11.91\,\mu A) = \mathbf{1.07\,mA}$$

$$V_{CE_Q} = V_{CC} - I_C(R_C + R_E) = 10\,V - (1.07\,mA)(4.7\,k\Omega + 1.2\,k\Omega) = 10\,V - 6.31\,V = \mathbf{3.69\,V}$$

## Configuracion en emisor seguidor

### Formulas

$$I_B = \frac{V_{EE} - V_{BE}}{R_B + (\beta + 1)R_E}$$

$$I_E = (\beta + 1)I_B$$

$$V_{CE_Q} = V_{EE} - I_E R_E$$

### Ejemplo

**Datos:** $V_{EE} = 20\,V$, $R_B = 240\,k\Omega$, $R_E = 2\,k\Omega$, $\beta = 90$

**Determinar:** $V_{CE_Q}$ e $I_{E_Q}$

**Solucion:**

$$I_B = \frac{V_{EE} - V_{BE}}{R_B + (\beta + 1)R_E} = \frac{20\,V - 0.7\,V}{240\,k\Omega + (91)(2\,k\Omega)} = \frac{19.3\,V}{240\,k\Omega + 182\,k\Omega} = \frac{19.3\,V}{422\,k\Omega} = 45.73\,\mu A$$

$$V_{CE_Q} = V_{EE} - (\beta + 1)I_B R_E = 20\,V - (91)(45.73\,\mu A)(2\,k\Omega) = 20\,V - 8.32\,V = \mathbf{11.68\,V}$$

$$I_{E_Q} = (\beta + 1)I_B = (91)(45.73\,\mu A) = \mathbf{4.16\,mA}$$

## Resumen de formulas por configuracion

> [!abstract] Tabla resumen
>
> | Configuracion | Formula de $I_B$ | Formula de $V_{CE}$ |
> | ------------- | ---------------- | -------------------- |
> | Fija | $\dfrac{V_{CC} - V_{BE}}{R_B}$ | $V_{CC} - I_C R_C$ |
> | Estabilizada por emisor | $\dfrac{V_{CC} - V_{BE}}{R_B + (\beta+1)R_E}$ | $V_{CC} - I_C(R_C + R_E)$ |
> | Divisor de voltaje | $\dfrac{E_{Th} - V_{BE}}{R_{Th} + (\beta+1)R_E}$ | $V_{CC} - I_C(R_C + R_E)$ |
> | Realimentacion de colector | $\dfrac{V_{CC} - V_{BE}}{R_B + \beta(R_C + R_E)}$ | $V_{CC} - I_C(R_C + R_E)$ |
> | Base comun | $I_E = \dfrac{V_{EE} - V_{BE}}{R_E}$ | $V_{EE} + V_{CC} - I_E(R_C + R_E)$ |
> | Emisor seguidor | $\dfrac{V_{EE} - V_{BE}}{R_B + (\beta+1)R_E}$ | $V_{EE} - I_E R_E$ |

## Bibliografia

- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson.
