---
title: "Tema 01 - Curvas características del motor asíncrono y regulación de velocidad"
curso: "[[Motores MOC]]"
unidad: 4
semana: 17
orden: 1
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/motor-asincrono
  - tema/curvas-caracteristicas
  - tema/par-velocidad
  - tema/regulacion-de-velocidad
date: 2026-07-13
---

> [!info] Material original
> Manual del docente: [S17-Manual-Curvas-caracteristicas-motor-sincrono.pdf](attachments/S17-Manual-Curvas-caracteristicas-motor-sincrono.pdf) (UTP, Semana 17).

> [!warning] El título del ítem en el portal está mal puesto
> El ítem del portal se titula *"Curvas características del motor **síncrono**"*, pero tanto el nombre del tema en el acordeón como la portada del manual dicen **"Curvas características del motor asíncrono y regulación de velocidad"**, y el contenido desarrolla íntegramente el **motor de inducción (asíncrono)**. Esta nota sigue el contenido real. Para el motor **síncrono** propiamente dicho, ver [[S17-4 Tema 03 - Máquina síncrona trifásica|Máquina síncrona trifásica]], donde la velocidad es fija y la regulación de velocidad es del 0 %.

## Curvas características de los motores de inducción

Se analiza la relación **par-velocidad** desde el punto de vista físico del comportamiento del campo magnético del motor. A partir de ese análisis cualitativo se deduce después la **ecuación general del par en función del deslizamiento**, partiendo del circuito equivalente por fase del motor de inducción.

### Par inducido desde el punto de vista físico

En un motor de inducción **en vacío**, el deslizamiento del rotor es muy reducido. En consecuencia:

- El movimiento relativo entre el rotor y los campos magnéticos es mínimo.
- El voltaje inducido en las barras del rotor es muy reducido y la frecuencia del rotor es muy pequeña.
- La reactancia del rotor es casi igual a cero, por lo que la corriente máxima del rotor está **casi en fase** con el voltaje del rotor.
- Se produce un campo magnético pequeño, con un ángulo ligeramente mayor a $90°$ por detrás del campo magnético neto.

El par inducido se expresa vectorialmente como:

$$\tau_{ind} = k\,\mathbf{B}_R \times \mathbf{B}_{net}$$

y su magnitud está dada por:

$$\tau_{ind} = k\,B_R\,B_{net}\operatorname{sen}\delta$$

- $\tau_{ind}$ = par inducido.
- $k$ = constante que depende de la construcción de la máquina.
- $B_R$ = campo magnético del rotor.
- $B_{net}$ = campo magnético neto de la máquina.
- $\delta$ = ángulo entre el campo del rotor y el campo neto.

### Comportamiento con carga

Cuando el motor de inducción opera con una **carga considerable** se observan dos efectos simultáneos:

1. Un **aumento de la corriente del rotor**, y con ella de $B_R$, que **tiende a aumentar** el par.
2. Un **incremento del ángulo $\delta$**, que **tiende a reducirlo**, puesto que el par es proporcional a $\operatorname{sen}\delta$ y $\delta > 90°$.

Como el efecto del primer aumento es **más significativo** que el segundo, el par total inducido aumenta para compensar el incremento en la carga del motor.

## Análisis término a término de la ecuación del par

Cada término de $\tau_{ind} = k\,B_R\,B_{net}\operatorname{sen}\delta$ puede analizarse individualmente para comprender el comportamiento general de la máquina.

### Campo magnético del rotor $B_R$

El campo magnético del rotor aumenta en **proporción directa** a la corriente que lo atraviesa, mientras el rotor no se sature. El flujo de corriente en el rotor **aumenta con el incremento del deslizamiento** (es decir, con la disminución de la velocidad).

### Campo magnético neto $B_{net}$

El campo magnético neto en el motor es **aproximadamente constante** y proporcional a $E_1$. Aunque $E_1$ disminuye ligeramente con un aumento del flujo de corriente, este efecto es insignificante frente a otros factores y se desprecia en el desarrollo gráfico.

### Término $\operatorname{sen}\delta$

El ángulo $\delta$ entre el campo magnético del rotor y el campo magnético neto puede expresarse de manera útil como **el ángulo del factor de potencia del rotor más $90°$**. Por lo tanto:

$$\operatorname{sen}\delta = \operatorname{sen}(\theta_R + 90°) = \cos\theta_R$$

Este término es, precisamente, el **factor de potencia del rotor**. El ángulo del factor de potencia es:

$$\theta_R = \tan^{-1}\frac{X_R}{R_R} = \tan^{-1}\frac{s\,X_{R0}}{R_R}$$

- $\theta_R$ = ángulo del factor de potencia del rotor.
- $X_R$ = reactancia del rotor a la frecuencia de deslizamiento; $X_{R0}$ = reactancia del rotor a rotor bloqueado.
- $R_R$ = resistencia del rotor.
- $s$ = deslizamiento.

Y el factor de potencia del rotor resulta:

$$FP_R = \cos\theta_R = \cos\!\left(\tan^{-1}\frac{s\,X_{R0}}{R_R}\right)$$

Combinando las tres gráficas parciales ($B_R$, $B_{net}$ y $\cos\theta_R$ frente a la velocidad) se obtiene la **característica par-velocidad** del motor de inducción, que se divide en **tres regiones**: bajo deslizamiento, deslizamiento moderado y alto deslizamiento.

## Ecuación del par inducido en el motor de inducción

Se puede emplear el circuito equivalente del motor de inducción junto con el **diagrama de flujo de potencia** para derivar una expresión general del par inducido en relación con la velocidad. El par inducido está dado por:

$$\tau_{ind} = \frac{P_{conv}}{\omega_m} \qquad\qquad \tau_{ind} = \frac{P_{EH}}{\omega_{sinc}}$$

- $P_{conv}$ = potencia convertida (mecánica desarrollada).
- $P_{EH}$ = potencia en el entrehierro.
- $\omega_m$ = velocidad angular mecánica del rotor.
- $\omega_{sinc}$ = velocidad angular de sincronismo.

Del circuito equivalente se ve que la potencia en el entrehierro suministrada a **una fase** del motor es:

$$P_{EH,1\phi} = I_2^{2}\,\frac{R_2}{s}$$

Por lo tanto, para las tres fases:

$$P_{EH} = 3\,I_2^{2}\,\frac{R_2}{s}$$

- $I_2$ = corriente del rotor referida al estator.
- $R_2$ = resistencia del rotor referida al estator.

### Equivalente de Thevenin del circuito de entrada

Para calcular la corriente $I_2$, posiblemente lo más fácil es determinar el **equivalente de Thevenin** del circuito de entrada. Aplicando la regla del divisor de voltaje:

$$\mathbf{V}_{TH} = \mathbf{V}_\phi\,\frac{\mathbf{Z}_M}{\mathbf{Z}_M + \mathbf{Z}_1} = \mathbf{V}_\phi\,\frac{jX_M}{R_1 + jX_1 + jX_M}$$

La **magnitud** del voltaje de Thevenin es:

$$V_{TH} = V_\phi\,\frac{X_M}{\sqrt{R_1^{2} + (X_1 + X_M)^{2}}}$$

- $V_\phi$ = tensión de fase aplicada al estator.
- $R_1$, $X_1$ = resistencia y reactancia de dispersión del estator.
- $X_M$ = reactancia de magnetización.

La **impedancia de Thevenin** es:

$$\mathbf{Z}_{TH} = \frac{jX_M\,(R_1 + jX_1)}{R_1 + j(X_1 + X_M)}$$

Puesto que $X_M \gg X_1$ y $X_M \gg R_1$, la magnitud del voltaje de Thevenin es aproximadamente:

$$V_{TH} \approx V_\phi\,\frac{X_M}{X_1 + X_M}$$

Vista como asociación de impedancias en paralelo, la impedancia de Thevenin también se escribe:

$$\mathbf{Z}_{TH} = \frac{\mathbf{Z}_1\,\mathbf{Z}_M}{\mathbf{Z}_1 + \mathbf{Z}_M}$$

que se reduce a:

$$\mathbf{Z}_{TH} = R_{TH} + jX_{TH} = \frac{jX_M\,(R_1 + jX_1)}{R_1 + j(X_1 + X_M)}$$

Puesto que $X_M \gg X_1$ y $X_M + X_1 \gg R_1$, la resistencia y la reactancia de Thevenin están dadas aproximadamente por:

$$R_{TH} \approx R_1\left(\frac{X_M}{X_1 + X_M}\right)^{2} \qquad\qquad X_{TH} \approx X_1$$

### Corriente del rotor y par resultante

En el circuito equivalente simplificado resultante, la corriente $I_2$ está dada por:

$$\mathbf{I}_2 = \frac{\mathbf{V}_{TH}}{\mathbf{Z}_{TH} + \mathbf{Z}_2} = \frac{\mathbf{V}_{TH}}{R_{TH} + \dfrac{R_2}{s} + jX_{TH} + jX_2}$$

y su magnitud es:

$$I_2 = \frac{V_{TH}}{\sqrt{\left(R_{TH} + \dfrac{R_2}{s}\right)^{2} + (X_{TH} + X_2)^{2}}}$$

Por lo tanto, la potencia en el entrehierro resulta:

$$P_{EH} = 3\,I_2^{2}\,\frac{R_2}{s} = \frac{3\,V_{TH}^{2}\,\dfrac{R_2}{s}}{\left(R_{TH} + \dfrac{R_2}{s}\right)^{2} + (X_{TH} + X_2)^{2}}$$

Y el **par inducido del rotor** queda finalmente:

$$\tau_{ind} = \frac{P_{EH}}{\omega_{sinc}} = \frac{3\,V_{TH}^{2}\,\dfrac{R_2}{s}}{\omega_{sinc}\left[\left(R_{TH} + \dfrac{R_2}{s}\right)^{2} + (X_{TH} + X_2)^{2}\right]}$$

- $X_2$ = reactancia de dispersión del rotor referida al estator.

Al graficar esta expresión se obtiene el par en función de la velocidad (y del deslizamiento) para el **intervalo normal** de operación, y —extendiendo el rango de velocidades por arriba y por debajo— aparecen además la **región de frenado** y la **región de generador**.

## Par máximo: ¿cuándo es máxima la potencia suministrada a $R_2/s$?

El **teorema de máxima transferencia de potencia** establece que la potencia máxima transferida al resistor de carga $R_2/s$ se presenta cuando la **magnitud de esta impedancia es igual a la magnitud de la impedancia de la fuente**. La impedancia equivalente de la fuente en el circuito es:

$$\mathbf{Z}_{fuente} = R_{TH} + jX_{TH} + jX_2$$

Por lo que la máxima transferencia de potencia se presenta cuando:

$$\frac{R_2}{s} = \sqrt{R_{TH}^{2} + (X_{TH} + X_2)^{2}}$$

De aquí, el **deslizamiento para el par máximo** está dado por:

$$s_{máx} = \frac{R_2}{\sqrt{R_{TH}^{2} + (X_{TH} + X_2)^{2}}}$$

Y la ecuación resultante del **par máximo** es:

$$\tau_{máx} = \frac{3\,V_{TH}^{2}}{2\,\omega_{sinc}\left[R_{TH} + \sqrt{R_{TH}^{2} + (X_{TH} + X_2)^{2}}\right]}$$

> [!tip] Consecuencia clave
> $s_{máx}$ es **proporcional a $R_2$**, pero $\tau_{máx}$ **no depende de $R_2$**. Por eso, al aumentar la resistencia del rotor, el par máximo se desplaza hacia velocidades menores conservando su valor. Esta propiedad se explota en el [[S17-2 Ejercicio resuelto - Regulación de velocidad de motor de inducción (Video)|ejercicio resuelto de la semana]].

## Regulación de velocidad en los motores de inducción

Existen **dos técnicas principales** para controlar la velocidad de un motor de inducción:

1. **Ajustar la velocidad síncrona** —la velocidad de los campos magnéticos del estator y del rotor—, ya que la velocidad del rotor tiende a permanecer cerca de ella.
2. **Variar el deslizamiento** del rotor para una carga específica.

La velocidad síncrona de un motor de inducción se define como:

$$n_{sinc} = \frac{120\,f_e}{P}$$

- $n_{sinc}$ = velocidad síncrona (rpm).
- $f_e$ = frecuencia eléctrica aplicada.
- $P$ = número de polos de la máquina.

Por lo tanto, las **únicas maneras** de modificar la velocidad síncrona de una máquina son:

1. Cambiando la **frecuencia eléctrica**.
2. Cambiando el **número de polos** de la máquina.

Y el control del **deslizamiento** se logra modificando la **resistencia del rotor** o el **voltaje en los terminales** del motor.

### Control de velocidad mediante el cambio de polos

Hay dos métodos importantes para cambiar el número de polos en un motor de inducción:

1. **Método de polos consecuentes.**
2. **Devanados de estator múltiples.**

El método de **polos consecuentes** es una antigua técnica de control de velocidad, desarrollada en **1897**. Se fundamenta en la capacidad de cambiar fácilmente el número de polos en los devanados del estator en un factor de **2:1** mediante cambios en las conexiones de las bobinas. Su **principal desventaja** es precisamente esa: las velocidades deben guardar una relación 2:1.

Al **combinar** el método de polos consecuentes con el de estatores de devanados múltiples es posible construir un motor de inducción de **cuatro velocidades**. Por ejemplo, utilizando devanados separados de cuatro y seis polos en un motor de $60\ \text{Hz}$, se puede lograr que opere a $600$, $900$, $1200$ y $1800\ \text{rpm}$.

### Control de velocidad mediante el cambio en la frecuencia de la línea

El control de **frecuencia variable** permite ajustar la velocidad del motor de inducción **por encima o por debajo** de su velocidad base. Un controlador bien diseñado ofrece gran flexibilidad, permitiendo ajustar la velocidad en un rango desde aproximadamente el **5 % hasta el doble** de la velocidad base. Es esencial mantener límites adecuados en el **voltaje y el par** del motor durante el ajuste de la frecuencia para asegurar una operación segura.

El fundamento es el flujo en el núcleo, obtenido al integrar la tensión aplicada:

$$\phi(t) = \frac{1}{N_P}\int v(t)\,dt = \frac{1}{N_P}\int V_M \operatorname{sen}\omega t\,dt = -\frac{V_M}{\omega\,N_P}\cos\omega t$$

- $\phi(t)$ = flujo en el núcleo.
- $N_P$ = número de espiras por fase.
- $V_M$ = valor pico de la tensión aplicada; $\omega$ = frecuencia angular eléctrica.

Al **disminuir un 10 %** la frecuencia eléctrica aplicada al estator **manteniendo constante** la magnitud del voltaje, el flujo en el núcleo del motor **aumentará un 10 %**, ya que la frecuencia eléctrica aparece en el **denominador** de la expresión. Esto resulta en un incremento de la corriente de magnetización del motor.

Por el contrario, cuando el voltaje aplicado **varía en forma lineal con la frecuencia** por debajo de la velocidad base, el flujo permanece **aproximadamente constante** y, por lo tanto, el par máximo que el motor puede suministrar se mantiene relativamente alto.

### Control de velocidad mediante el cambio del voltaje de línea

El par desarrollado por un motor de inducción es **proporcional al cuadrado del voltaje aplicado**. Con una carga que presente una característica par-velocidad adecuada, la velocidad del motor puede controlarse dentro de un **intervalo limitado** modificando el voltaje de línea. Este método se emplea a menudo en el manejo de **pequeños motores de ventilación**.

### Control de velocidad mediante el cambio de la resistencia del rotor

En los motores de inducción con **rotor devanado** es posible modificar la curva par-velocidad añadiendo **resistencias adicionales** al circuito del rotor. Si la carga tiene una curva par-velocidad dada, el ajuste de la resistencia del rotor **cambiará la velocidad de operación** del motor.

Sin embargo, añadir resistencia al circuito del rotor **reduce significativamente la eficiencia** de la máquina. Este método es hoy principalmente de **interés histórico**, ya que se fabrican muy pocos motores de inducción con rotor devanado; cuando se utiliza, generalmente es solo por **períodos cortos** debido a los problemas de eficiencia mencionados.

> [!summary] Idea central
> El par del motor de inducción, $\tau_{ind} = k\,B_R\,B_{net}\operatorname{sen}\delta$, crece con la carga porque el aumento de $B_R$ pesa más que el crecimiento de $\delta$; con $\operatorname{sen}\delta = \cos\theta_R$, el tercer factor resulta ser el **factor de potencia del rotor**. Reduciendo el circuito de entrada a su equivalente de Thevenin se obtiene la ecuación general $\tau_{ind} = \dfrac{3V_{TH}^{2}(R_2/s)}{\omega_{sinc}\left[(R_{TH}+R_2/s)^{2}+(X_{TH}+X_2)^{2}\right]}$, cuyo máximo ocurre en $s_{máx} = R_2/\sqrt{R_{TH}^{2}+(X_{TH}+X_2)^{2}}$ con $\tau_{máx}$ **independiente de $R_2$**. La velocidad se regula sobre $n_{sinc} = 120f_e/P$ (frecuencia, polos) o sobre el **deslizamiento** (resistencia del rotor, voltaje de línea). A diferencia de la [[S17-4 Tema 03 - Máquina síncrona trifásica|máquina síncrona]], cuya regulación de velocidad es del 0 %, aquí la velocidad **sí depende de la carga**.

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
