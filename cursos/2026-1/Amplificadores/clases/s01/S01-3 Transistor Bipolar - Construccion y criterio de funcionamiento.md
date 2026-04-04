---
title: "Transistor Bipolar - Construccion y criterio de funcionamiento"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 1
orden: 3
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/transistor-bjt
  - tema/polarizacion
  - tema/recta-de-carga
  - tema/punto-de-operacion
date: 2026-03-31
---

## Introduccion

La palabra transistor se deriva de **Trans**fer **Resistor** o resistencia de transferencia.

El transistor es un dispositivo electronico semiconductor que **se comporta como una resistencia variable** que depende de una senal electrica de control. Al variar el valor de la senal de control, varia la cantidad de corriente que pasa por el transistor.

## Tipos de transistores

- **BJT:** Transistores bipolares de union (PNP, NPN)
- **JFET:** Transistores de efecto de campo de union (Canal P, Canal N)
- **MOSFET:** Transistores de efecto de campo de metal-oxido-semiconductor
	- Empobrecimiento (Canal P, Canal N)
	- Enriquecimiento (Canal P, Canal N)
- **MESFET:** Transistores de efecto de campo de metal semiconductor

## Construccion de transistores BJT

### Repaso: el diodo

Los diodos se construyen uniendo dos tipos distintos de semiconductores: **tipo N** (catodo) y **tipo P** (anodo). El diodo esta polarizado directamente cuando el material tipo P tiene un potencial mas positivo que el material tipo N.

### Estructura del BJT

Se utilizan **tres capas semiconductoras**:
- Dos de tipo P y una de tipo N → transistor **PNP**
- Dos de tipo N y una de tipo P → transistor **NPN**

Se conoce como "transistor bipolar" debido a que su corriente electrica esta formada por **dos tipos de cargas: huecos y electrones**.

### Capas del transistor NPN

| Capa | Tamano | Dopaje | Funcion |
| ---- | ------ | ------ | ------- |
| **Emisor** | Medio | Fuertemente dopado | Emitir o inyectar electrones |
| **Base** | Pequeno | Ligeramente dopado | Pasar electrones |
| **Colector** | Grande | Muy poco dopado | Colectar electrones |

> [!important] Dopaje relativo
> - La base es poco dopada
> - El emisor es mas dopado que el colector

## Modos de operacion del BJT

El BJT tiene **4 modos de operacion** en funcion de la polarizacion de sus 2 uniones p-n:

| Union B-E | Union B-C | Operacion |
| --------- | --------- | --------- |
| Inversa | Inversa | **Corte** |
| Directa | Inversa | **Activa directa** |
| Inversa | Directa | **Activa inversa** |
| Directa | Directa | **Saturacion** |

Relaciones fundamentales:

$$I_E = I_C + I_B$$

$$V_{CE} = V_{BE} - V_{BC}$$

### Transistor sin polarizacion

Sin voltajes externos aplicados, se forman zonas de deplexion en ambas uniones (BE y BC) con un potencial de barrera $V_0$.

### Transistor polarizado en saturacion

Ambas uniones (BE y BC) estan polarizadas en directa. Es similar a dos diodos con polarizacion directa.

$$I_B + I_C = I_E$$

### Transistor polarizado en corte

Ambas uniones (BE y BC) estan polarizadas en inversa. Es similar a dos diodos con polarizacion inversa.

$$I_E = I_C = I_B = 0$$

### Transistor polarizado en region activa

La union BE se polariza en directa y la union BC en inversa. En un transistor PNP en modo activo:

- $I_{pB}$ = huecos que por difusion pasan del emisor a la base
- $I_{nB}$ = electrones que pasan de la base al emisor
- $I_{BB}$ = electrones procedentes del circuito para cubrir las recombinaciones
- $I_{nC}$ = debil corriente de electrones del colector a la base

La union BC inversa **puede conducir** si la union BE esta en directa: los huecos que se difunden de E a B llegan a C.

$$I_C = \beta I_B$$

Donde $\beta$ es el **factor de ganancia** de corriente.

Corrientes en el transistor PNP (modo activo):

$$I_E = I_{pB} + I_{nB}$$

$$I_B = -I_{nC} + I_{BB} + I_{nB}$$

$$I_C = I_{pB} - I_{BB} + I_{nC}$$

## Configuraciones del transistor

Hay 4 variables que dependen del tipo de conexion: $V_{\text{salida}}$, $V_{\text{entrada}}$, $I_{\text{salida}}$, $I_{\text{entrada}}$.

### Base comun

- Variables: $V_{BE}$, $V_{CB}$, $I_E$, $I_C$

### Emisor comun

- Variables: $V_{BE}$, $V_{CE}$, $I_B$, $I_C$

### Configuracion emisor comun en detalle

En la configuracion emisor comun, la corriente de base $I_B$ (1%) controla la corriente de colector $I_C$ (99%), con $I_E$ = 100%.

$$\beta = \frac{I_C}{I_E} \cong 99$$

> [!example] Ejemplo numerico
> Si $I_B = 1\,\text{mA}$, entonces $I_C = 99\,\text{mA}$ e $I_E = 100\,\text{mA}$.

## Curvas caracteristicas

### Curva de entrada

Grafica de $I_B$ vs $V_{BE}$. Se comporta como un diodo, con conduccion significativa a partir de 0.7 V.

$$V_{BE} = V_{BB} - I_B R_B$$

$$V_{BE} \approx 0.7\,V \text{ (para silicio)}$$

### Curva de salida

Grafica de $I_C$ (mA) vs $V_{CE}$ para distintos valores de $I_B$.

$$V_{CE} = V_{CC} - I_C R_C$$

### Regiones en la curva de salida

En la curva $I_C$ vs $V_{CE}$ del transistor en emisor comun se identifican 4 regiones:

1. **Region de saturacion:** ambas uniones polarizadas directamente → cortocircuito
2. **Region activa:** union EB directa, BC inversa → amplificacion
3. **Region de corte:** ambas uniones polarizadas inversamente → circuito abierto
4. **Region de ruptura:** voltaje excesivo que dana el transistor

### Variables del emisor comun

$$V_{BE} \approx 0.7\,V$$

$$I_C = \beta I_B$$

$$V_{CE} = V_{CC} - I_C R_C$$

## Polarizacion de transistores

La **polarizacion de transistores** es el proceso de establecer un voltaje de operacion de CC o condiciones de corriente al nivel correcto para que cualquier senal de entrada de CA pueda amplificarse correctamente mediante el transistor.

Un estado de funcionamiento constante depende de la corriente base, voltaje del colector y corriente del colector. Si un transistor debe operar como **amplificador lineal**, debe estar polarizado adecuadamente para tener un punto de funcionamiento adecuado.

### Punto de trabajo Q

El **punto de operacion Q** (punto quiescente) es el conjunto de corrientes y tensiones que aparecen en los terminales del dispositivo: $V_{CEQ}$, $I_{CQ}$.

- Es un punto de reposo (en continua)
- Deben satisfacerse simultaneamente:
	- Las curvas caracteristicas del transistor (limitaciones del fabricante)
	- Las ecuaciones del circuito de polarizacion exterior (limitaciones de componentes)

## Circuitos de polarizacion y recta de carga estatica

### Recta de carga estatica

A partir de la malla de salida:

$$V_{CC} = I_C R_C + V_{CE}$$

Despejando $I_C$:

$$\boxed{I_C = \frac{V_{CC} - V_{CE}}{R_C} = \frac{V_{CC}}{R_C} - \frac{1}{R_C} V_{CE}}$$

Esta es la **ecuacion de la recta de carga estatica**. Se definen 2 puntos para trazar la recta:

- **Punto de corte** ($I_C = 0$): $V_{CE} = V_{CC}$
- **Punto de saturacion** ($V_{CE} = 0$): $I_C = \dfrac{V_{CC}}{R_C}$

El punto Q se ubica en la interseccion de la recta de carga con la curva de $I_{B_Q}$.

### Eleccion del punto Q

Se disena $I_B$ y se calcula $R_B$ de forma que:

$$I_B = \frac{V_{CC} - V_{BE}}{R_B}$$

Datos necesarios: $V_{CC}$, $R_C$.

### Variacion del punto Q

El punto Q se desplaza al:
- **Incrementar $I_B$:** Q sube a lo largo de la recta de carga
- **Modificar $R_C$:** cambia la pendiente de la recta ($R_3 > R_2 > R_1$)
- **Disminuir $V_{CC}$:** la recta se desplaza a la izquierda ($V_{CC_1} > V_{CC_2} > V_{CC_3}$)

## Tipos de polarizacion

### Polarizacion fija

$$I_B = \frac{V_{CC} - V_{BE}}{R_B} \approx \frac{V_{CC}}{R_B} = \text{cte}$$

$$I_C = \beta I_B$$

Circuito simple con $R_B$ y $R_C$. La corriente de base es constante, pero depende fuertemente de $\beta$.

### Polarizacion con realimentacion de colector

- $I_B$ no es fija, depende de $V_C$
- **Realimentacion negativa**
- Q es mas estable ante variaciones de $\beta$

### Polarizacion con divisor de tension y realimentacion de emisor

- $I_B$ no es fija, depende de $R_1 \parallel R_2$, $R_E$
- **Realimentacion negativa**
- Q mas estable que en el caso anterior

## Saturacion del transistor

Es el punto donde $I_C$ es maxima ($I_{C_{max}} = I_{C_{sat}}$). Para hallar $I_{C_{max}}$, se considera $V_{CE} = 0\,V$:

$$\boxed{I_{C_{sat}} = \frac{V_{CC}}{R_C}}$$

## Polarizacion con divisor de voltaje

Es un circuito de polarizacion que **no depende del valor $\beta$**.

### Procedimiento de solucion

**Paso 1:** Identificar el circuito con $R_1$, $R_2$, $R_C$, $R_E$.

**Paso 2:** Aplicar equivalente de Thevenin en la base.

**Paso 3:** Hallar $R_{Th}$:

$$R_{Th} = R_1 \parallel R_2 = \frac{R_1 \cdot R_2}{R_1 + R_2}$$

**Paso 4:** Hallar $V_{Th}$ (equivalente de Thevenin = $E_{Th} = V_{R_2}$):

$$V_{Th} = V_{CC} \cdot \frac{R_2}{R_1 + R_2}$$

## El transistor en conmutacion

El transistor pasa de la zona de **corte** a la de **saturacion** y viceversa (conmuta entre estos dos estados). Tanto la entrada como la salida son "digitales".

La conmutacion se considera instantanea, si bien existen retardos debido a la redistribucion de cargas en las uniones.

### Condiciones

- **Corte:** $V_e < 0.6\,V \implies V_s = V_{CC}$
- **Saturacion:** $I_C < \beta I_B \implies V_s = 0.2\,V$

En saturacion:

$$I_B = \frac{V_e - 0.6\,V}{R_B} \quad;\quad I_C = \frac{V_{CC} - 0.2\,V}{R_C}$$

Voltaje minimo de entrada para saturacion:

$$V_e > R_B \cdot \frac{V_{CC} - 0.2\,V}{\beta \cdot R_C} + 0.6\,V = V_{e_{sat}}$$

$$I_{B_{sat\,min}} = \frac{V_{e_{sat}} - 0.6}{R_B} \quad;\quad I_{C_{sat}} = \frac{V_{CC} - 0.2\,V}{R_C}$$

> [!info] Inversor elemental
> El transistor en conmutacion actua como un **inversor** con desfase de 180°: cuando la entrada es alta ($V_e > V_{e_{sat}}$), la salida es baja ($V_{CE_{sat}} \approx 0.2\,V$), y viceversa.

## El transistor como amplificador

El transistor trabaja en la **zona activa** (es necesario fijar adecuadamente el punto Q).

Se conecta a la malla base-emisor:
- Un generador de continua de valor $V_{BB}$
- En serie con un generador de alterna $v_s = V_P \sin(\omega t)$

### Corriente de base variable

$$I_{B\,max} = \frac{(V_{BB} + V_P) - V_{BE}}{R_B}$$

$$i_B(t) = \frac{(V_{BB} + V_P \sin(\omega t)) - V_{BE}}{R_B}$$

$$I_{B\,min} = \frac{(V_{BB} - V_P) - V_{BE}}{R_B}$$

### Corriente de colector variable

$$I_{C\,max} = \beta \cdot I_{B\,max} = \beta \cdot \frac{(V_{BB} + V_P) - V_{BE}}{R_B}$$

$$i_C(t) = \beta \cdot i_B(t) = \beta \cdot \frac{(V_{BB} + V_P \sin(\omega t)) - V_{BE}}{R_B}$$

$$I_{C\,min} = \beta \cdot I_{B\,min} = \beta \cdot \frac{(V_{BB} - V_P) - V_{BE}}{R_B}$$

### Tension colector-emisor variable

$$V_{CE\,min} = V_{CC} - R_C \cdot I_{C\,max}$$

$$v_{CE}(t) = V_{CC} - R_C \cdot i_C(t)$$

$$V_{CE\,max} = V_{CC} - R_C \cdot I_{C\,min}$$

### Ganancias

- **Ganancia de corriente:** $\dfrac{\Delta i_C}{\Delta i_B}$
- **Ganancia de tension:** $\dfrac{\Delta v_{CE}}{\Delta v_s}$ (donde $v_s$ es la entrada alterna)

> [!note] Convencion de notacion
> Las minusculas representan magnitudes instantaneas (variantes en el tiempo).

## Limites de operacion

Para cada transistor existe una **zona de operacion segura** (SOA), dentro de la cual debe trabajar para exhibir una distorsion minima. Los limites vienen definidos en las hojas de especificaciones tecnicas:

- **$I_{C\,max}$:** Corriente maxima continua de colector
- **$V_{CEO}$:** Voltaje maximo entre colector y emisor (con base desconectada o polarizada inversamente)
- **$V_{CE_{sat}}$:** Voltaje minimo que se puede aplicar para no caer en la zona de saturacion
- **$P_{C\,max}$:** Maxima potencia de disipacion del colector (define la curva hiperbolica de potencia)

> [!warning] Zona de rechazo
> El transistor NO debe operar fuera de la zona de trabajo segura, delimitada por $I_{C\,max}$, $V_{CE\,max}$ y $P_{C\,max}$.

## Aplicaciones

- Amplificadores de senal
- Conmutador electronico
- Diseno de circuitos digitales logicos, memorias de PC y otros

## Ejercicio: Recta de carga

**Datos de la grafica:** Punto Q ubicado en $I_B = 25\,\mu A$, con $V_{CC} = 20\,V$, $I_{C_{sat}} = 10\,\text{mA}$.

**Determinar:** $R_C$ y $R_B$ para un circuito de polarizacion fija.

**Solucion:**

Del punto de corte: $V_{CE} = V_{CC} = 20\,V$ con $I_C = 0\,\text{mA}$

Del punto de saturacion: $I_C = \dfrac{V_{CC}}{R_C}$ con $V_{CE} = 0\,V$

$$R_C = \frac{V_{CC}}{I_C} = \frac{20\,V}{10\,\text{mA}} = 2\,k\Omega$$

Para la corriente de base:

$$I_B = \frac{V_{CC} - V_{BE}}{R_B}$$

$$R_B = \frac{V_{CC} - V_{BE}}{I_B} = \frac{20\,V - 0.7\,V}{25\,\mu A} = 772\,k\Omega$$

## Bibliografia

- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson.
- Floyd, T. *Dispositivos Electronicos*. Pearson.
