---
title: "Oscilador puente de Wien: análisis y criterio de Barkhausen"
curso: "[[Amplificadores MOC]]"
unidad: 4
semana: 17
orden: 1
tipo: ejercicio
tags:
  - curso/amplificadores
  - tipo/ejercicio
  - tema/oscilador-puente-de-wien
  - tema/criterio-de-barkhausen
  - tema/osciladores
  - tema/realimentacion-positiva
  - tema/red-rc
date: 2026-07-14
---

## Contexto

Continuación de los [[S08-2 Realimentacion negativa y realimentacion positiva|amplificadores realimentados]]. Un **oscilador** es un amplificador con **realimentación positiva** que genera una señal periódica **sin excitación de entrada**: se autoexcita a partir del ruido. El **puente de Wien** es el oscilador RC clásico para bajas y medias frecuencias (audio, típicamente decenas de Hz a cientos de kHz).

La estrategia de análisis: separar el circuito en el **amplificador $A$** (un no inversor) y la **red de realimentación $\beta$** (red resonante RC), y aplicarles el **criterio de Barkhausen**.

> [!info] Toma de notas en clase
> Semana 17 — Jorge Luis Robles. Se redibuja el oscilador para identificar $A$ y $\beta$, se calculan las impedancias serie/paralelo de la red RC y se impone Barkhausen para hallar la **frecuencia de oscilación** y la **ganancia mínima**.

---

## Enunciado

Para el oscilador puente de Wien de la figura, con la misma $R$ y el mismo $C$ en las dos ramas de la red de realimentación:

1. Obtener $\beta(\omega) = V_f / V_{out}$ en función de $Z_1$ y $Z_2$.
2. Aplicar el **criterio de Barkhausen** para deducir la **frecuencia de oscilación** $f_0$.
3. Determinar la **ganancia** $A$ que debe tener el amplificador y la relación entre $R_2$ y $R_1$.

## Datos

- Amplificador **no inversor** (realimentación positiva hacia la entrada $+$):

$$A = \frac{V_{out}}{V_{in}} = \frac{R_2 + R_1}{R_1} = 1 + \frac{R_2}{R_1}$$

- Red de realimentación (divisor de tensión entre $Z_1$ y $Z_2$):

$$\beta(\omega) = \frac{V_f}{V_{out}} = \frac{Z_2}{Z_1 + Z_2}$$

- **Rama serie** $Z_1$ ($R$ en serie con $C$):

$$Z_1 = R + \frac{1}{j\omega C} = \frac{1 + j\omega RC}{j\omega C}$$

- **Rama paralelo** $Z_2$ ($R$ en paralelo con $C$):

$$Z_2 = \frac{R \cdot \dfrac{1}{j\omega C}}{R + \dfrac{1}{j\omega C}} = \frac{R}{1 + j\omega RC}$$

Donde:

- $\;R,\ C$ = resistencia y capacitancia de **ambas** ramas (iguales) $[\Omega],\ [\text{F}]$
- $\;\omega$ = frecuencia angular $[\text{rad/s}]$
- $\;R_1,\ R_2$ = resistencias del lazo de realimentación negativa del no inversor $[\Omega]$

---

## Solución

### 1. Factor de realimentación $\beta(\omega)$

Conviene dividir numerador y denominador entre $Z_2$:

$$\beta = \frac{Z_2}{Z_1 + Z_2} = \frac{1}{1 + \dfrac{Z_1}{Z_2}}$$

Calculamos el cociente $Z_1/Z_2$:

$$\frac{Z_1}{Z_2} = \frac{1 + j\omega RC}{j\omega C}\cdot\frac{1 + j\omega RC}{R} = \frac{(1 + j\omega RC)^2}{j\omega RC}$$

Entonces:

$$1 + \frac{Z_1}{Z_2} = \frac{j\omega RC + (1 + j\omega RC)^2}{j\omega RC}$$

Desarrollando el cuadrado, $(1 + j\omega RC)^2 = 1 + 2j\omega RC - \omega^2 R^2 C^2$, el numerador queda:

$$j\omega RC + 1 + 2j\omega RC - \omega^2 R^2 C^2 = \big(1 - \omega^2 R^2 C^2\big) + 3\,j\omega RC$$

Por lo tanto:

$$\boxed{\ \beta(\omega) = \frac{j\omega RC}{\big(1 - \omega^2 R^2 C^2\big) + 3\,j\omega RC}\ }$$

### 2. Criterio de Barkhausen

Para que un lazo realimentado **oscile de forma sostenida**, la ganancia de lazo $\beta A$ debe cumplir dos condiciones simultáneas:

$$\boxed{\ |\beta A| = 1 \qquad\text{y}\qquad \angle(\beta A) = 0^\circ\ }$$

Es decir, la señal que recorre el lazo debe volver **con la misma amplitud y en fase**. En la diapositiva esto se plantea como la **ecuación característica del lazo** $1 + \beta A = 0$:

$$1 + \left(\frac{Z_2}{Z_1 + Z_2}\right)\left(\frac{R_2 + R_1}{R_1}\right) = 0$$

Sustituimos $\beta(\omega)$ y escribimos $A = \dfrac{R_2+R_1}{R_1}$:

$$1 + \frac{j\omega RC}{(1-\omega^2R^2C^2)+3j\omega RC}\,A = 0$$

Multiplicamos por el denominador $(1-\omega^2R^2C^2)+3j\omega RC$:

$$(1-\omega^2R^2C^2) + 3\,j\omega RC + j\omega RC\,A = 0$$

y **agrupamos parte real y parte imaginaria**:

$$\boxed{\ \underbrace{(1-\omega^2R^2C^2)}_{\text{parte real}} \; + \; \underbrace{j\,\omega RC\,(3+A)}_{\text{parte imaginaria}} \; = \; 0\ }$$

Un número complejo es cero **solo si su parte real y su parte imaginaria valen cero por separado**. Esas dos ecuaciones dan, una la **frecuencia** y la otra la **ganancia**.

### 3. Parte real $=0$ → frecuencia de oscilación

$$1 - \omega_0^2 R^2 C^2 = 0 \;\;\Longrightarrow\;\; \omega_0^2 = \frac{1}{R^2 C^2} \;\;\Longrightarrow\;\; \omega_0 = \frac{1}{RC}$$

Y como $\omega_0 = 2\pi f_0$:

$$\boxed{\ f_0 = \frac{1}{2\pi RC}\ }$$

Esta es la **frecuencia de oscilación**: la fija exclusivamente la red RC.

### 4. Parte imaginaria $=0$ → ganancia del amplificador

Como $\omega RC \neq 0$, el factor que debe anularse es $(3+A)$:

$$3 + A = 0 \;\;\Longrightarrow\;\; |A| = 3$$

Y de $A = 1 + \dfrac{R_2}{R_1} = 3$:

$$\frac{R_2}{R_1} = 2 \;\;\Longrightarrow\;\; \boxed{R_2 = 2\,R_1}$$

También sirve como verificación evaluar $\beta$ en $\omega_0 = 1/RC$ (se anula la parte real del denominador): $\beta(\omega_0) = \dfrac{j\omega_0 RC}{3\,j\omega_0 RC} = \dfrac{1}{3}$. El amplificador debe compensar esa atenuación de $\tfrac{1}{3}$, de ahí $|A| = 3$.

> [!note] Sobre el signo ($A = -3$ vs. $A = +3$)
> Al separar partes, la ecuación de la diapositiva entrega literalmente $3 + A = 0$, o sea $A = -3$. El amplificador **no inversor** real, en cambio, tiene $A = 1 + R_2/R_1 = +3$ (positivo). La diferencia es **solo de convenio**: escribir Barkhausen como $1+\beta A = 0$ equivale a pedir $\beta A = -1$, mientras que para esta topología de realimentación **positiva** la forma físicamente correcta es $\beta A = 1$ (equivalente a $1-\beta A = 0$). En ambos convenios el resultado medible es idéntico: **$|A| = 3$** y **$R_2 = 2R_1$**.

> [!warning] Arranque vs. régimen permanente
> $A = 3$ es el valor **exacto** para oscilación sostenida. Para que las oscilaciones **arranquen** desde el ruido hace falta $A$ un poco **mayor** que 3 (lazo $\beta A > 1$), y luego un mecanismo de **control automático de ganancia** (p. ej. lámpara incandescente, diodos o FET en $R_2$) que la reduzca hasta 3 para no saturar. Con $A = 3$ exacto, cualquier deriva por temperatura apaga o satura el oscilador.

---

## Respuesta

| Magnitud | Resultado | Comentario |
| --- | --- | --- |
| Factor de realimentación | $\beta(\omega) = \dfrac{j\omega RC}{(1-\omega^2R^2C^2)+3j\omega RC}$ | Divisor de la red RC |
| Frecuencia de oscilación | $\displaystyle f_0 = \frac{1}{2\pi RC}$ | De la **parte real** $=0$ |
| $\beta$ en $f_0$ | $\beta(\omega_0) = \tfrac{1}{3}$ | Atenuación de la red en resonancia |
| Ganancia del amplificador | $\lvert A\rvert = 3$ | De la **parte imaginaria** $=0$ ($A\gtrsim 3$ para arrancar) |
| Relación de resistencias | $R_2 = 2\,R_1$ | Del no inversor $A = 1 + R_2/R_1$ |

> [!success] Idea clave
> En el puente de Wien la **red RC decide la frecuencia** ($f_0 = 1/2\pi RC$) y el **amplificador decide la amplitud** (necesita $A \gtrsim 3$ para compensar la atenuación $\beta = 1/3$ de la red). Barkhausen une ambas: fase $\to f_0$, módulo $\to A$.

## Bibliografía

- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos* (osciladores, criterio de Barkhausen, oscilador puente de Wien). Pearson.
- Sedra, A. & Smith, K. *Microelectronic Circuits* (RC oscillators, Wien-bridge oscillator). Oxford University Press.
