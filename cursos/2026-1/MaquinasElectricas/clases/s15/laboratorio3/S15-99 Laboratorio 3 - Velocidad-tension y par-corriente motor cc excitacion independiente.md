---
title: Laboratorio 3 - Características velocidad-tensión y par-corriente de motor CC con excitación independiente
curso: "[[Motores MOC]]"
unidad: 4
semana: 15
orden: 99
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
  - tema/balance-de-potencias
date: 2026-07-06
---

> [!info] Datos del laboratorio
> - **Tipo:** Guía de laboratorio Nº 3
> - **Tema:** Características de velocidad-tensión y par-corriente de motor CC con excitación independiente
> - **Software:** LVSIM (LabVolt)
> - **Guía oficial (PDF):** [MaquinasElectricas_Labo3.pdf](MaquinasElectricas_Labo3.pdf)

---

## Logro general de la unidad de aprendizaje

Al finalizar la unidad, el estudiante analiza el comportamiento de los tipos de motores de corriente continua para la regulación de velocidad.

## Objetivos específicos de la práctica

Al finalizar la unidad, el estudiante analiza el comportamiento de los tipos de motores de corriente continua para la regulación de velocidad.

- Calcular los requerimientos iniciales del circuito de accionamiento de la máquina.
- Elaborar el esquema de una primera fase del circuito de accionamiento de la máquina con los componentes y la tensión de alimentación calculados.
- Analizar las medidas efectuadas en el circuito de accionamiento de la máquina y comprobación de su correcto funcionamiento.

## Materiales y equipos

| Descripción | Cantidad |
| --- | :-: |
| Puesto de trabajo | 1 |
| Motor CC/generador (**8211**) | 1 |
| Multímetro | 1 |
| Cables de conexión | 1 |
| Dinamómetro / Fuente de alimentación de cuatro cuadrantes (**8960-20**) | 1 |
| Computadora | 1 |
| Interfaz de adquisición de datos y de control (**9063**) | 1 |
| Fuente de alimentación (**8821**) | 1 |

---

## Fundamento

Un motor de corriente continua convierte energía eléctrica en energía mecánica. Funciona como una dinamo en reversa, siguiendo el principio de reciprocidad electromagnética de Faraday y Lenz.

La comprensión del principio de reciprocidad en un motor de corriente continua implica aplicar la segunda ley de Kirchhoff al circuito del inducido, lo que conduce a una ecuación relevante, que denominando $V_i = V + V_{esc}$ a la tensión neta en el inducido nos da una corriente $I_I$:

Cuando la fuerza electromotriz (f.e.m.) $E$ supera la diferencia de potencial (d.d.p.) $V_i$ (generalmente igual a la tensión de la red), la corriente en el inducido fluye en la misma dirección que $E$. En este caso, la máquina funciona como **generador**, suministrando una potencia electromagnética $E I_i$. Esto genera un par resistente que se opone al movimiento del motor primario.

Cuando la fuerza electromotriz (f.e.m.) del generador disminuye, reduciendo la velocidad de rotación o la excitación del inductor, y $E$ se vuelve menor que la tensión $V_i$, la corriente $I_i$ del inducido cambia de sentido. Esto indica que la máquina produce una fuerza contra-electromotriz, ya que $E$ se opone a la corriente $I_i$. En esta situación, la máquina trabaja como **motor**, produciendo un par electromagnético que coincide con el de rotación, pasando de un par resistente a un par motor. Desconectando el motor primario, la máquina de corriente continua continuará girando en el mismo sentido que cuando actuaba como generador, desarrollando ahora su propio par motor. Este cambio se debe a que se ha invertido la polaridad de la corriente en uno de los devanados. En resumen, al fijar la polaridad eléctrica de los terminales de un motor de corriente continua y mantener el sentido de giro del rotor, la escobilla positiva es el borne por donde sale la corriente del inducido cuando la máquina trabaja como generador, mientras que funciona como motor, por esa escobilla es por donde entra la corriente de la red de corriente continua.

| Funcionamiento como generador | Funcionamiento como motor |
| :---: | :---: |
| ![[labo3-fig1-generador.png]] | ![[labo3-fig2-motor.png]] |
| **Figura 1.** Funcionamiento de las máquinas de c.c. como generador | **Figura 2.** Funcionamiento de las máquinas de c.c. como motor |

Al considerar la corriente $I_i$ absorbida como positiva durante el funcionamiento como motor, al aplicar el segundo lema de Kirchhoff al circuito del inducido en la figura 2, se obtiene:

$$V = E + R_i I_i + V_{esc}$$

Para determinar el proceso de transformación de energía mecánica en eléctrica en el motor de c.c., se ha de obtener una ecuación del balance de potencias. Para ello, si se multiplica la ecuación anterior por $I_i$ resulta:

$$V I_i = E I_i + R_i I_i^2 + V_{esc} I_i$$

cuyos términos significan:

- $P_i = V I_i$: Potencia eléctrica absorbida por el inducido del motor
- $P_{esc} = V_{esc} I_i$: Pérdidas en los contactos de las escobillas
- $P_{cui} = R_i I_i^2$: Pérdidas en el cobre del inducido
- $P_a = E I_i$: Potencia electromagnética desarrollada por la máquina

De acuerdo con esta nomenclatura, el balance de potencias en el inducido se convierte en:

$$P_i = P_a + P_{cui} + P_{esc}$$

La potencia electromagnética $P_a$ representa la potencia mecánica total generada por un motor. Al dividirla por la velocidad de giro, se obtiene el par interno desarrollado por la máquina, cuya expresión:

$$T = \frac{E I_i}{2\pi \dfrac{n}{60}} \quad [\text{N.m}]$$

Si se sustituye en esta ecuación la **f.e.m. $E$**, se obtiene la siguiente expresión:

$$T = \frac{1}{2\pi}\frac{p}{c} Z\phi I_i = K_T \phi I_i$$

Para calcular la potencia mecánica útil en el árbol del motor, es necesario restar a la potencia electromagnética $P_a$ las pérdidas rotóricas, que incluyen las pérdidas en el hierro $P_{Fe}$ y las pérdidas mecánicas $P_m$ de rozamiento y ventilación. Por lo tanto, la potencia útil del motor $P_2$ se puede expresar como:

$$P_2 = P_a - P_{Fe} - P_m$$

En el caso de un motor con excitación independiente, la potencia absorbida por la máquina $P_1$ es igual a la potencia que llega al inducido $P_i$. Sin embargo, en máquinas autoexcitadas, la potencia de entrada debe compensar también las pérdidas en el circuito de excitación $P_{exc}$, que se deben al efecto Joule en el cobre del inductor. Por lo tanto, se obtiene:

$$P_1 = P_i + P_{exc} - P_m$$

En la figura 3 se muestra de una forma esquemática el reparto de potencias en el motor de c.c. La potencia de entrada $P_1$ es el producto de la tensión de alimentación por la corriente absorbida, y el rendimiento del motor será:

$$n = \frac{P_2}{P_1}$$

![[labo3-fig3-balance-potencias.png]]
**Figura 3.** Balance de potencias en el motor de c.c.

Los motores de corriente continua se clasifican según el tipo de excitación de manera similar a los generadores. Así, se distinguen motores con excitación independiente, serie, derivación y compuesta. En cada caso, el par electromagnético está determinado por:

$$T = K_T \phi I_i$$

Desde un punto de vista práctico, estos motores de c.c. presentan una gran ventaja sobre los motores de c.a., debido a su posibilidad de regulación de velocidad, si se incluye en $R_i$ la resistencia del inducido y escobillas se tiene:

$$V = E + R_i I_i$$

La expresión general de la f.e.m.:

$$E = \frac{n}{60} Z\phi \frac{p}{c} = K_E n\phi$$

Despejando la velocidad **$n$**, se obtiene:

$$n = \frac{V - R_i I_i}{K_E \phi}$$

La velocidad de un motor de corriente continua puede regularse controlando varias variables:

- **El flujo por polo generado por la corriente de excitación:** Disminuir el flujo aumenta la velocidad de rotación. Sin embargo, arrancar el motor sin conectar la excitación puede llevar a un embalamiento del motor, limitado por el magnetismo remanente de los polos.
- **La tensión de alimentación $V$ aplicada al motor:** Reducir/aumentar esta tensión disminuye/aumenta la velocidad.
- **La resistencia del circuito del inducido:** Conectar una resistencia o reóstato variable en serie con este devanado permite controlar la velocidad. Aumentar/disminuir la resistencia del inducido provoca una disminución/aumento en la velocidad.

---

## Tipos de excitación de motores de corriente continua

### Motores de c.c. con excitación independiente y derivación

En los motores de corriente continua, los esquemas de conexión para el arranque y la regulación de velocidad son similares y se muestran en la figura 4. En el caso de excitación independiente, los circuitos del inductor y del inducido se alimentan de fuentes distintas, mientras que en el caso del motor derivación (shunt) las fuentes coinciden. Si la tensión de alimentación al inducido se mantiene constante ($V = V_e$), no hay diferencia práctica en el comportamiento de estos dos tipos de motores.

![[labo3-fig4-independiente-derivacion.png]]
**Figura 4.** Motores con excitación independiente y derivación.

Durante el arranque, es crucial que el flujo en el entrehierro alcance su máximo valor para que el motor pueda generar el par de arranque necesario con la corriente mínima en el inducido. Por lo tanto, desde el inicio del arranque, el devanado de excitación debe estar conectado a la tensión de la red, y el reóstato $R_s$ en serie con el inductor debe tener la mínima resistencia para maximizar la corriente de excitación o campo. Para analizar las características $n = f(T)$ de estos motores, se asume que inicialmente operan en la zona lineal de la curva de magnetización, utilizando las siguientes expresiones.

$$T = K_T\phi I_i \quad ; \quad V = E + R_i I_i \quad ; \quad E = K_E n\phi$$

Donde:

$$I = \frac{V - K_E n\phi}{R_i}$$

Que lleva a la expresión de velocidad en función del par:

$$n = \frac{V - R_i I_i}{K_E \phi} = \frac{1}{K_E \phi}V - \frac{R_i}{K_E K_T \phi^2}T$$

Cuando el motor de derivación está funcionando con un par resistente determinado y este par aumenta, la máquina experimenta un frenado, lo que disminuye la velocidad del rotor y, como consecuencia, reduce la f.c.e.m. (fuerza contraelectromotriz) del motor. Esto lleva a un aumento en la corriente absorbida por el inducido según la ecuación $I = \dfrac{V - K_E n\phi}{R_i}$, y el par de la máquina, según $T = K_T\phi I_i$, se eleva para igualarse con el nuevo par resistente ofrecido por la carga. La curva par-velocidad $n = f(T)$ del motor derivación (y por extensión, del motor con excitación independiente) es una línea recta, como se muestra en la figura 5. Esta recta, para los valores asignados de tensión aplicada y resistencia del inductor (sin resistencia adicional en el circuito de campo), se denomina **característica natural** de la máquina.

![[labo3-fig5-curva-derivacion.png]]
**Figura 5.** Curva par-velocidad $n = f(T)$ del motor derivación.

La velocidad del motor en vacío (cuando el par es cero) está definida por el término $n_0 = \dfrac{V}{K_E \phi}$. Para altos pares de carga, aumenta la corriente del rotor y por ello se reduce el flujo resultante a consecuencia de la reacción del inducido; de ahí que en realidad la característica $n = f(T)$ de estos motores se desvíe ligeramente de la recta anterior. La caída de velocidad con el aumento del par en la curva anterior es muy pequeña (del orden del 5% al 10%), lo que indica que los motores en derivación presentan una característica de carga dura o rígida (similar a la de los motores asíncronos) y por ello se utilizan en aquellas aplicaciones que requieran una velocidad casi constante: ventiladores, bombas centrífugas, cintas transportadoras, máquinas herramientas, etc.

La regulación de velocidad de los motores derivación e independiente se logra de las siguientes formas:

1. Ajustando la tensión del inducido.
2. Variando la resistencia del circuito del inducido (aunque este método es poco práctico debido a las pérdidas que se producen y, por lo tanto, tiene un bajo rendimiento).
3. Cambiando la resistencia del circuito de excitación, lo que a su vez regula el flujo del motor.

### Motores de c.c. con excitación serie

El esquema de conexiones de este tipo de motor es el indicado en la figura 6. El flujo de la máquina depende de la corriente del inducido $I = I_i$, y en consecuencia depende de la carga. Si no hay saturación en el circuito magnético, el flujo es directamente proporcional a la corriente $I_i$, y la característica de carga se puede obtener de las ecuaciones básicas.

$$T = K_T\phi I_i \quad ; \quad V = E + R_i I_i \quad ; \quad E = K_E n\phi$$

![[labo3-fig6-serie.png]]
**Figura 6.** Motores con excitación en serie.

que en el supuesto de que el motor no esté saturado y se cumpla la proporcionalidad $\phi = K_I I_i$ resulta:

$$T = K_T K_I I_i^2 \Rightarrow I_i = \sqrt{\frac{T}{K_T K_I}}$$

lo que conduce a una característica del par teniendo en cuenta que viene definida por la siguiente ecuación:

$$n = \frac{V - R_i I_i}{K_E \phi} = \frac{V}{K_E K_I I_i} - \frac{R_i}{K_E K_I} = \frac{1}{K_E}\sqrt{\frac{K_T}{K_I}}\frac{V}{\sqrt{T}} - \frac{R_i}{K_E K_I}$$

y denominando **$a$** y **$b$** a las siguientes constantes:

$$a = \frac{1}{K_E}\sqrt{\frac{K_T}{K_I}} \quad ; \quad b = \frac{R_i}{K_E K_I}$$

la ecuación se transforma en:

$$n = a\frac{V}{\sqrt{T}} - b \approx a\frac{V}{\sqrt{T}} \Rightarrow n^2 T = aV = \text{constante}$$

Dado que la resistencia del inducido $R_i$ es muy pequeña, el término $b$ es despreciable. Por lo tanto, con una tensión de alimentación constante, el par de un motor serie varía en relación inversa con el cuadrado de la velocidad. En la figura 7 se muestra la representación de la curva $n = f(T)$, donde el par de arranque es el que tiene la máquina para $n = 0$, y de acuerdo con $T_{arr} = \dfrac{a^2 V^2}{b^2}$, indica que el par de arranque de estos motores es muy elevado. En condiciones de saturación, la característica par/velocidad tiende a ser una hipérbola equilátera $nT = \text{constante}$. Si se desprecia la reacción del inducido y la saturación magnética, al duplicarse el par aplicado al eje del motor, la corriente consumida aumenta solo un 140% del valor original, y el número de revoluciones cae hasta un 70% del valor inicial.

![[labo3-fig7-curva-serie.png]]
**Figura 7.** Curva par velocidad de un motor serie.

En un motor derivación, una sobrecarga similar prácticamente no altera la velocidad, pero la máquina consume aproximadamente el doble de corriente inicial. Por otro lado, el motor en serie puede soportar sobrecargas elevadas, aumentando solo moderadamente la corriente.

Esta capacidad es su propiedad más valiosa. Cuando se reduce el par resistente, el motor disminuye lentamente su consumo de corriente, mientras que su velocidad aumenta rápidamente. Sin embargo, para cargas inferiores al 25% de la asignada, la velocidad alcanza valores peligrosos para la integridad del motor. Por esta razón, **no se debe arrancar el motor serie en vacío o con una carga pequeña**.

> [!warning] Ambos motores tienen velocidades iguales en todo momento
> La variación de velocidad se logra mediante la conexión serie-paralelo de ambos motores, lo que permite obtener dos velocidades básicas de trabajo con un buen rendimiento energético.

### Motores de c.c. con excitación compuesta

El esquema de conexiones de este motor se muestra en la figura 8. El devanado de excitación serie puede conectarse de forma aditiva o diferencial al campo derivación. La corriente del devanado derivación es constante, mientras que la del arrollamiento serie aumenta con la carga, lo que produce un flujo por polo que también aumenta con la carga, aunque no tan rápidamente como en un motor serie.

![[labo3-fig8-compuesta.png]]
**Figura 8.** Motor con excitación compuesta.

La característica mecánica de estos motores se ilustra en la figura 9, siendo intermedia entre las curvas del motor derivación y serie.

![[labo3-fig9-curvas-cc.png]]
**Figura 9.** Curva par velocidad de los motores de c.c.

---

## Procedimiento del laboratorio

### Instalaciones y conexiones

- Instala los equipos en el puesto de trabajo y configura el programa para tensión nominal de 220 voltios y frecuencia de 50 Hz.
- Asegúrate de que el interruptor del Dinamómetro/Fuente de alimentación esté apagado.
- En la fuente de alimentación, asegúrate de que el interruptor principal y el de energía de 24 V se encuentren apagados.
- Conecta la entrada de potencia de la interfaz de datos de 24 V a la fuente de alimentación.
- Realiza la conexión según la figura. Usa la salida de tensión CC variable de la fuente de alimentación para implementar la fuente de energía CC de tensión variable $E_S$.
- Realiza las conexiones según las figuras 10 y 11. Usa la salida de tensión CC variable de la fuente de alimentación para implementar la fuente de energía CC de tensión variable $E_S$. Luego, usa la salida de tensión CC fija de la fuente de alimentación para alimentar la fuente de energía CC de tensión fija de la figura 11. $E_1$, $I_1$ e $I_2$ son entradas de tensión y corriente de la interfaz de adquisición de datos.

![[labo3-fig10-circuito-fuente-variable.png]]
**Figura 10.** Circuito con fuente variable y Motor dc con excitación independiente acoplado a un freno.

![[labo3-fig11-circuito-fuente-fija.png]]
**Figura 11.** Circuito con fuente fija en el estator.

- En el "Dinamómetro/Fuente de alimentación", ajusta el modo de operación en la opción **Dinamómetro**, para que funcione como freno.
- En el software, abre la ventana "Dinamómetro/Fuente de alimentación", que se encuentra en el menú superior, y realiza las siguientes configuraciones:
	a) Ajusta en el parámetro **Función** la opción **Freno de par constante de dos cuadrantes**.
	b) Ajusta la relación de polea **24:24**.
	c) Asegúrate de que el parámetro **Control de Par** esté ajustado en **Perilla**. Esto permite controlar manualmente el par del freno de dos cuadrantes.
	d) Configura el parámetro **Par** en **0,0 N.m**.
	e) Arranca el **Freno de par constante de dos cuadrantes** ajustando el parámetro **Estado** en la opción **En marcha** o haciendo clic en el botón **Marcha/Parada**.
- Abre la ventana **Aparatos de medición** para calcular la tensión del inducido $E_A$ (E1) y la corriente del inducido $I_A$ (I1) del motor CC. Configura un medidor para la corriente de campo $I_f$ (I2) del motor CC.
- Abre la ventana **Tabla de datos**. Configura para registrar la velocidad de rotación $n$ y el par $T$ del motor CC, así como la tensión del inducido $E_A$, la corriente del inducido $I_A$ y la corriente de campo $I_f$ del motor CC.
- Enciende la **Fuente de alimentación**.
- En el Motor/generador ajusta la perilla Reóstato de campo de modo que la corriente de campo $I_f$ (I2) sea igual al valor de la tabla 1.

**Tabla 1.** Corriente de campo $I_f$

| Red eléctrica AC local — Tensión (V) | Frecuencia (Hz) | Corriente de campo $I_f$ (mA) |
| :---: | :---: | :---: |
| 120 | 60 | 200 |
| 220 | 50 | 125 |
| 240 | 50 | 140 |
| 220 | 60 | 125 |

- En la **Fuente de alimentación**, ajusta la perilla de control de tensión de 0% a 100% en etapas de 10%, con el fin de incrementar la tensión de inducido $E_A$ por etapas. Para cada configuración, espera hasta que se estabilice la velocidad del motor, luego registra la tensión del inducido $E_A$, la corriente del inducido $I_A$ y la corriente de campo $I_f$ del motor, así como la velocidad de rotación $n$ y el par $T$ en la Tabla 2.
- Cuando se hayan registrado todos los datos, detén el **Motor/generador CC** ajustando la perilla de control de tensión de 0% y apaga la **Fuente de alimentación**, pero deja la fuente de 24 V AC encendida.

**Tabla 2.** Tensión y corriente del inducido, corriente de campo, velocidad de rotación y par del motor cc con excitación independiente.

| Tensión del inducido $E_A$ (V) | Corriente del inducido $I_A$ (A) | Corriente de campo $I_f$ (A) | Velocidad $n$ de rotación (r/min) | Par $T$ motor (N.m) |
| :---: | :---: | :---: | :---: | :---: |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

- En la ventana **Gráfico**, que se encuentra en el menú superior, realiza las configuraciones apropiadas para obtener un gráfico de la velocidad $n$ del motor CC en función de la tensión del inducido $E_A$. Titula el gráfico "Lab3", denomina el **eje x** "Tensión del inducido" y el **eje y** "Velocidad del motor". *(Escala sugerida: eje x de 0 a 300 V; eje y de 0 a 1750 r/min.)*
- Usa los puntos extremos para calcular la pendiente $K_1$ de la relación obtenida en el gráfico. Obtendrás los valores de esos puntos en la tabla 2.

$$K_1 = \frac{n_2 - n_1}{E_2 - E_1} = \frac{\underline{\quad\quad}}{\underline{\quad\quad}} = \underline{\quad\quad}\ \frac{\text{r/min}}{\text{V}}$$

- Compara el gráfico y la constante $K_1$ obtenidos en el ejercicio anterior. Describe el efecto que causa la disminución de la corriente de campo $I_f$ en las características de la relación entre la velocidad y la tensión y en la constante $K_1$ de un motor CC con excitación independiente.
- Luego, enciende la **Fuente de alimentación** nuevamente y el dinamómetro, asegúrate que el **Par** esté en 0,0 N.m.
- En el **Motor/generador CC**, reajusta levemente la perilla **Reóstato de campo**, si es necesario, de modo que la corriente de campo $I_f$ (indicado en el medidor I2) siga siendo igual a la corriente de la tabla 1.
- En la **Fuente de alimentación**, ajusta la perilla de control de tensión de modo que la velocidad de rotación $n$ del motor sea **1500 r/min**. Observa y registra el valor de la tensión del inducido $E_A$ (medidor E1) del motor.

$$\text{Tensión del inducido } E_A\ (n = 1500\ \text{r/min}) = \underline{\quad\quad}\ \text{V.} \quad (1)$$

- Observa y registra el valor del par motor $T$.

$$\text{Par motor } T\ (\text{nominal}) = \underline{\quad\quad}\ \text{N.m.}$$

- Con el valor del par mínimo obtenido anteriormente registra en la Tabla de datos la velocidad de rotación $n$ y el par $T$ del motor, así como la tensión del inducido $E_A$, la corriente del inducido $I_A$ y la corriente de campo $I_f$ del motor.
- Incrementa el parámetro **Par** del valor mínimo a unos **1,5 N.m** en etapas de **0,2 N.m**. Para cada configuración de par, vuelve a ajustar la perilla de control de tensión de la **Fuente de alimentación** de modo que la tensión del inducido $E_A$ siga siendo igual al valor calculado en (1) y luego registra en la **Tabla de datos** la velocidad de rotación $n$ y el par $T$, así como la tensión del inducido $E_A$, y las corrientes de inducido $I_A$ y de campo $I_f$ del motor.
- Luego de los registros, apaga la fuente de alimentación y deja encendida la tensión de 24 V en AC.
- Llena la tabla 3, como se muestra:

**Tabla 3.** Tensión y corriente del inducido, corriente de campo, velocidad de rotación y par del motor cc con excitación independiente.

| Tensión del inducido $E_A$ (V) | Corriente del inducido $I_A$ (A) | Corriente de campo $I_f$ (A) | Velocidad $n$ de rotación (r/min) | Par $T$ motor (N.m) |
| :---: | :---: | :---: | :---: | :---: |
| 0.1 |  |  |  |  |
| 0.3 |  |  |  |  |
| 0.5 |  |  |  |  |
| 0.7 |  |  |  |  |
| 0.9 |  |  |  |  |
| 1.1 |  |  |  |  |
| 1.3 |  |  |  |  |
| 1.5 |  |  |  |  |

> [!note] Sobre la columna "Tensión del inducido $E_A$" de la Tabla 3
> En la guía original la primera columna de la Tabla 3 aparece con los valores 0.1, 0.3, … 1.5; corresponden a los escalones de **Par $T$ (N.m)** que se van fijando (de 0,1 a 1,5 N.m en pasos de 0,2). Para cada escalón se reajusta la tensión de manera que $E_A$ se mantenga en el valor calculado en (1).

- En la ventana **Gráfico**, realiza las configuraciones apropiadas para obtener un gráfico del par $T$ del motor cc en función de la corriente del inducido $I_A$. Denomina los ejes según se indica en la gráfica. *(Escala sugerida: eje x — corriente del inducido $I_A$ de 0,0 a 1,8 A; eje y — Par $T$ motor de 0,0 a 1,6 N.m.)*
- Usa los puntos extremos para calcular la pendiente $K_2$ de la relación obtenida en el gráfico. Los valores de esos puntos se indican en la tabla 3.

$$K_2 = \frac{T_2 - T_1}{I_2 - I_1} = \frac{\underline{\quad\quad}}{\underline{\quad\quad}} = \underline{\quad\quad}\ \frac{\text{N.m}}{\text{A}}$$

- Compara el gráfico y la constante $K_2$ obtenidos en el ejercicio anterior. Describe el efecto que causa la disminución de la corriente de campo $I_f$ en las características de la relación entre el par y la corriente y en la constante $K_2$ de un motor CC con excitación independiente.

---

## Entregables

**Carátula:** incluye tu nombre, apellidos y código.

**Conexión eléctrica tipo independiente del motor CC:**

- Presenta el diagrama de la conexión realizada según las indicaciones.

**Velocidad vs. Tensión:**

- Presenta la tabla 2 con los datos obtenidos.
- Presenta el gráfico de velocidad-tensión.
- Presenta la resolución de la ecuación de $K_1$, paso por paso.
- Comparación del gráfico y la constante $K_1$: Compara y describe el efecto que causa la disminución de la corriente de campo $I_f$ en las características de la relación entre la velocidad y la tensión y en la constante $K_1$ de un motor CC con excitación independiente.

**Torque vs. Corriente:**

- Presenta la tabla 3 con los datos obtenidos.
- Presenta el gráfico de torque-corriente.
- Presenta la resolución de la ecuación de $K_2$, paso por paso.
- Comparación del gráfico y la constante $K_2$: Compara y describe el efecto que causa la disminución de la corriente de campo $I_f$ en las características de la relación entre la velocidad y la tensión y en la constante $K_2$ de un motor CC con excitación independiente.

**Conclusiones:** Redacta por lo menos 4 conclusiones de la experiencia y los resultados obtenidos.

---

## Fuentes de información complementaria

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5a. Ed.). McGraw-Hill Interamericana.
- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6a. Ed.). McGraw-Hill Interamericana.
- LabVolt Series (2013). Relaciones de tensiones y corrientes. En *Electricidad y Nuevas Energías – Transformadores de potencia monofásicos* (pp. 8-21). Québec, Canadá: Festo Didactic, ISBN 978-2-89640-664-7.
- LabVolt Series (2013). Apéndices. En *Electricidad y Nuevas Energías – Circuitos ca monofásicos* (pp. 121-131). Québec, Canadá: Festo Didactic, ISBN 978-2-89640-664-7.
