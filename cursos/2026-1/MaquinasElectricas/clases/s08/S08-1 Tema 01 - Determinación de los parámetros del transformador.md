---
title: Determinación de los parámetros del transformador (admitancia de excitación e impedancia serie)
curso: "[[Motores MOC]]"
unidad: 2
semana: 8
orden: 1
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/ensayo-vacio
  - tema/ensayo-cortocircuito
  - tema/admitancia-excitacion
  - tema/conductancia-pernucleo
  - tema/susceptancia-magnetizacion
  - tema/impedancia-serie
date: 2026-05-11
---

![[s08-t01-banner.png]]

## Introducción

Es posible determinar **experimentalmente los valores de las impedancias y resistencias** en el modelo del transformador haciendo **dos pruebas**: la prueba **en vacío** y la prueba en **cortocircuito** (ver fundamentos en [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real|S07-3]]).

> [!info] Diferencia con la semana 7
> En la semana 7 calculamos los parámetros con $R_{Fe}$ y $X_\mu$ como **impedancias paralelas vistas en serie con la fuente**. En esta semana usamos una **forma alternativa equivalente** basada en la **admitancia de excitación** $\mathbf{Y}_E = G_{Fe} - jB_\mu$, que es la formulación de Chapman y suele simplificar el álgebra fasorial.

## 1. Prueba en vacío

En la prueba de vacío, el devanado **secundario se deja sin conexión** mientras que el **primario se conecta a la línea de voltaje nominal**. Bajo estas condiciones, **toda la corriente de entrada fluye a través de la rama de excitación**.

Los elementos en serie $R_1$ y $X_1$ son **tan pequeños** en comparación con $R_{Fe}$ y $X_\mu$ que apenas causan una caída de tensión significativa — toda la tensión de entrada se disipa a través de la rama de excitación.

![[s08-t01-fig1-conexion-vacio.png]]
*Figura 1. Conexión para la prueba de vacío del transformador.*

Se registran:
- $V_0$ — voltaje de entrada (= $V_{1n}$)
- $I_0$ — corriente de entrada
- $P_0$ — potencia de entrada

A partir de esta información se determina el **factor de potencia** y, por lo tanto, la **magnitud y el ángulo de la impedancia de excitación**.

![[s08-t01-fig2-equivalente-primario.png]]
*Figura 2. Circuito equivalente del transformador real reducido al primario.*

![[s08-t01-fig3-equivalente-secundario.png]]
*Figura 3. Circuito equivalente del transformador real reducido al secundario.*

### Admitancia de excitación

La manera más fácil de calcular $R_{Fe}$ y $X_\mu$ es estimar primero la **admitancia** de la rama de excitación.

**Conductancia** del resistor de pérdidas en el núcleo:

$$G_{Fe} = \frac{1}{R_{Fe}}$$

**Susceptancia** del inductor de magnetización:

$$B_\mu = \frac{1}{X_\mu}$$

Puesto que los dos elementos están en paralelo, se suman sus admitancias y la **admitancia de excitación total** es:

![[s08-t01-fig4-equivalente-vacio.png]]
*Figura 4. Circuito equivalente en vacío.*

$$\boxed{\;\mathbf{Y}_E = G_{Fe} - j B_\mu\;}$$

$$\mathbf{Y}_E = \frac{1}{R_{Fe}} - j \, \frac{1}{X_\mu}$$

> [!note] Signo del término imaginario
> Aparece **menos** $jB_\mu$ porque la rama magnetizante es **inductiva**: su admitancia tiene parte imaginaria negativa, lo que equivale a $\mathbf{Y}_\mu = 1/(jX_\mu) = -j/X_\mu$.

### Cálculo desde las medidas

La **magnitud** de la admitancia de excitación (referida al lado donde se midió) se calcula con el voltaje y la corriente de la prueba de circuito abierto:

$$|\mathbf{Y}_E| = \frac{I_0}{V_0}$$

**Donde:**
- $I_0$ — corriente de la prueba en vacío
- $V_0$ — voltaje de la prueba en vacío

El **factor de potencia** del circuito abierto da el ángulo:

$$\text{FP} = \cos\theta = \frac{P_0}{V_0 \cdot I_0}$$

$$\theta = \cos^{-1}\!\left(\frac{P_0}{V_0 \cdot I_0}\right)$$

> El factor de potencia **siempre está en retraso** en un transformador real, por lo que el ángulo de la corriente está retrasado $\theta$ grados respecto al voltaje.

Por lo tanto la admitancia $\mathbf{Y}_E$ es:

$$\boxed{\;\mathbf{Y}_E = \frac{I_0}{V_0}\,\angle(-\theta) = \frac{I_0}{V_0}\,\angle(-\cos^{-1}\!\text{FP})\;}$$

> [!tip] De $\mathbf{Y}_E$ a $R_{Fe}$ y $X_\mu$
> Una vez se tiene $\mathbf{Y}_E = G_{Fe} - jB_\mu$ en forma rectangular:
> $$R_{Fe} = \frac{1}{G_{Fe}} \hspace{0.5cm};\hspace{0.5cm} X_\mu = \frac{1}{B_\mu}$$

## 2. Prueba de cortocircuito

En la prueba de cortocircuito, se **cortocircuitan las terminales de bajo voltaje** del transformador, mientras que las **terminales de alto voltaje se conectan a una fuente de voltaje variable**.

Esta prueba se realiza típicamente en el **lado de alto voltaje** porque las corrientes son menores y resultan **más fáciles de manejar**. Se ajusta el voltaje de entrada gradualmente hasta que la corriente en los devanados en cortocircuito **alcance su valor nominal**.

> [!warning] Cuidado con el voltaje primario
> Es fundamental mantener el voltaje primario en un nivel **seguro** durante el ensayo — dañar los devanados del transformador durante la prueba no es recomendable.

![[s08-t01-fig5-conexion-cc.png]]
*Figura 5. Conexión para la prueba de cortocircuito del transformador.*

Dado el bajo voltaje de entrada durante el ensayo, la **corriente que circula por la rama de excitación es insignificante**. Al despreciar esta corriente, toda la caída de voltaje en el transformador puede atribuirse a los **elementos en serie** del circuito.

![[s08-t01-fig6-equivalente-cc.png]]
*Figura 6. Circuito equivalente en cortocircuito.*

### Cálculo de la impedancia serie

La **magnitud** de las impedancias en serie, referidas al lado primario, es:

$$|\mathbf{Z}_{serie}| = \frac{V_{cc}}{I_{cc}}$$

El **factor de potencia** de la corriente:

$$\text{FP} = \cos\theta = \frac{P_{cc}}{V_{cc} \cdot I_{cc}}$$

El factor de potencia está en **retraso**, por lo que el ángulo de la corriente es negativo y el ángulo de la impedancia total $\theta$ es positivo:

$$\theta = \cos^{-1}\!\left(\frac{P_{cc}}{V_{cc} \cdot I_{cc}}\right)$$

Por lo tanto:

$$\mathbf{Z}_{serie} = \frac{V_{cc}\,\angle 0°}{I_{cc}\,\angle(-\theta)} = \frac{V_{cc}}{I_{cc}}\,\angle\theta$$

En forma rectangular:

$$\boxed{\;\mathbf{Z}_{serie} = R_{eq} + jX_{eq}\;}$$

### Descomposición en componentes primario y secundario

Esta técnica permite determinar la impedancia en **serie total** referida al lado de alto voltaje. **No existe una manera sencilla** de descomponer la impedancia en sus componentes primario y secundario.

La **forma aproximada** de obtener las componentes (criterio habitual de reparto igualitario, ver [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real|circuito equivalente]]) es dividir la impedancia total según:

$$\mathbf{Z}_{serie} = (R_1 + a^2 R_2) + j(X_1 + a^2 X_2)$$

con $R_1 = a^2 R_2$ y $X_1 = a^2 X_2$, lo que da $R_1 = R'_2 = R_{eq}/2$ y $X_1 = X'_2 = X_{eq}/2$.

## Resumen de fórmulas

| Magnitud | Fórmula |
| -------- | ------- |
| Conductancia núcleo | $G_{Fe} = 1/R_{Fe}$ |
| Susceptancia magnetizante | $B_\mu = 1/X_\mu$ |
| Admitancia de excitación | $\mathbf{Y}_E = G_{Fe} - jB_\mu$ |
| $|\mathbf{Y}_E|$ desde medida | $I_0/V_0$ |
| $\angle\mathbf{Y}_E$ | $-\cos^{-1}(\text{FP}_0)$ |
| $\mathbf{Z}_{serie}$ desde CC | $(V_{cc}/I_{cc})\,\angle\,\cos^{-1}(\text{FP}_{cc})$ |
| $\mathbf{Z}_{serie}$ rectangular | $R_{eq} + jX_{eq}$ |

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
