---
title: Laboratorio LC1 - Circuito magnetico con nucleo ferromagnetico
curso: "[[Motores MOC]]"
unidad: 1
semana: 5
orden: 99
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/evaluacion
  - tema/laboratorio
  - tema/circuito-magnetico
  - tema/transformador
date: 2026-04-26
---

> [!info] Datos del laboratorio
> - **Tipo:** Laboratorio Calificado 1 (LC1) — Guía de laboratorio Nº 1
> - **Tema:** Circuito magnético con núcleo ferromagnético
> - **Peso:** 10% de la nota final
> - **Modalidad:** Evaluación flexible (individual o grupal)
> - **Semana:** 5
> - **Software:** LVSIM (LabVolt)
> - **Indicaciones y rúbrica:** [[S05-98 Indicaciones y Rubrica - LC1 Laboratorio|S05-98 Indicaciones y Rúbrica LC1]]

---

## Logro general de la unidad de aprendizaje

Al finalizar la unidad, el estudiante explica las leyes fundamentales del electromagnetismo en circuitos magnéticos.

## Objetivos específicos de la práctica

- Identificar los requerimientos y parámetros del circuito magnético con núcleo ferromagnético y devanado.
- Elaborar el esquema del circuito magnético con núcleo ferromagnético y devanado con los parámetros identificados.
- Analizar los parámetros medidos en el esquema final del circuito magnético.

## Materiales y equipos a utilizar en el software

| Descripción                                          | Cantidad |
| ---------------------------------------------------- | -------- |
| Puesto de trabajo (software LVSIM)                   | 1        |
| Transformador (8353)                                 | 1        |
| Multímetro (amperímetro, voltímetro y ohmímetro)     | 4        |
| Interfaz de adquisición de datos y de control (9063) | 1        |
| Cables de conexión                                   | 1        |
| Fuente de alimentación (8221)                        | 1        |

---

## Fundamento

### 1. Ecuación de la tensión inducida

La ecuación de la tensión inducida en un reactor de núcleo de un transformador está determinada por la relación entre el flujo magnético variable en el tiempo y el número de vueltas del devanado.

Según la **Ley de Faraday**, la variación del flujo magnético a través de un circuito cerrado induce una fuerza electromotriz (fem) en el mismo. Esta fem inducida es proporcional a la tasa de cambio del flujo magnético a lo largo del tiempo y al número de vueltas del devanado:

$$e = -N \cdot \frac{d\phi}{dt}$$

Donde:
- $e$ = fuerza electromotriz inducida $[\text{V}]$
- $N$ = número de vueltas del devanado
- $\dfrac{d\phi}{dt}$ = tasa de cambio del flujo magnético $[\text{Wb/s}]$

Esta ecuación muestra cómo la fem inducida en el devanado del transformador depende de la tasa de cambio del flujo magnético a lo largo del tiempo y del número de vueltas del devanado. Es fundamental para comprender el comportamiento del transformador en diferentes condiciones de operación y su relación con la tensión inducida en el devanado.

### 2. Pérdidas del núcleo

Las pérdidas del núcleo de hierro en un transformador son causadas por varios factores, como la resistencia en los circuitos magnéticos y eléctricos del transformador. Estas pérdidas se producen debido al **efecto Joule** en el conductor cuando circula una corriente eléctrica, lo que se transforma en energía térmica.

Las pérdidas en el núcleo de hierro se dividen en dos categorías principales:
- **Pérdidas fijas** en el hierro en vacío.
- **Pérdidas variables** en el cobre cuando el transformador está en carga.

Las pérdidas en el núcleo de hierro también pueden ser causadas por la magnetización, el origen dieléctrico y las corrientes parásitas asociadas. Estas pérdidas deben tenerse en cuenta al diseñar y operar un transformador, ya que afectan su eficiencia y rendimiento.

A su vez, las pérdidas en el núcleo de hierro se dividen en dos tipos principales:

> [!info] Tipos de pérdidas en el núcleo
> - **Pérdidas por histéresis:** se producen debido a la inversión continua del campo magnético en el núcleo del transformador. Dependen del volumen y la calidad del hierro, la frecuencia de las inversiones magnéticas y el valor de la densidad de flujo.
> - **Pérdidas por corrientes parásitas (Foucault):** se deben al flujo de corriente dentro del núcleo debido a los campos magnéticos cambiantes. Estas corrientes parásitas generan calor y contribuyen a las pérdidas totales del transformador.

Ver desarrollo completo en [[S05-1 Tema 01 - Perdidas magneticas en el nucleo|S05-1 Pérdidas magnéticas en el núcleo]].

### 3. Circuito equivalente del reactor con núcleo de hierro

La **Ley de Hopkinson** se expresa por la ecuación:

$$\phi = \frac{\mathcal{F}}{\mathcal{R}}$$

Donde:
- $\phi$ = flujo magnético
- $\mathcal{F}$ = fuerza magnetomotriz (f.m.m.)
- $\mathcal{R}$ = reluctancia

Al aplicar una tensión de alimentación de **c.c.** a la bobina, se producirá, de acuerdo con la **Ley de Ohm**, una corriente:

$$I = \frac{V}{R}$$

Que dará lugar a una f.m.m. $\mathcal{F} = N \cdot i$, y que según sea el valor de la reluctancia del circuito magnético determinará el flujo resultante $\phi = \dfrac{\mathcal{F}}{\mathcal{R}}$.

#### Excitación con tensión c.a. senoidal

Supóngase ahora que la bobina se alimenta con una tensión de c.a. senoidal:

$$v(t) = \sqrt{2} \cdot V \cdot \cos \omega t$$

Donde:
- $V$ = valor eficaz de la tensión alterna aplicada
- $\omega = 2\pi f$ = pulsación

![[s05-lab-fig1-bobina-nucleo-hierro.png]]
*Figura 1. Bobina con núcleo de hierro.*

Se producirá una corriente de circulación $i(t)$ que provocará un flujo $\phi(t)$ en el núcleo. Este flujo variable dará lugar a una f.e.m. inducida en la bobina. Aplicando el segundo lema de Kirchhoff al circuito eléctrico:

$$v = R \cdot i + N \cdot \frac{d\phi}{dt}$$

Suponiendo que la caída de tensión en la resistencia de la bobina es pequeña en comparación con la f.e.m. inducida:

$$v \approx N \cdot \frac{d\phi}{dt}$$

De donde se deduce el valor del flujo $\phi(t)$:

$$\phi(t) = \frac{1}{N} \int v \cdot dt = \frac{\sqrt{2}}{N \cdot \omega} \cdot V \, \text{sen} \, \omega t$$

Donde el flujo máximo:

$$\phi_m = \frac{\sqrt{2} \cdot V}{N \cdot \omega}$$

Y teniendo en cuenta que $\omega = 2\pi f$:

$$\boxed{V = \frac{2\pi}{\sqrt{2}} \cdot f \cdot N \cdot \phi_m = 4{,}44 \cdot f \cdot N \cdot \phi_m}$$

> [!tip] Ecuación fundamental del transformador
> La fórmula $V = 4{,}44 \cdot f \cdot N \cdot \phi_m$ es la **ecuación fundamental** que vincula la tensión eficaz, la frecuencia, el número de espiras y el flujo máximo. Es la base para el diseño y análisis de transformadores.

---

## Procedimiento del laboratorio

### Paso 1 — Configuración inicial

Ingresa a **LVSIM** con tu código de acceso. Configura el programa para tensión nominal de **220 voltios** y frecuencia de **50 Hz**.

### Paso 2 — Selección de módulos

Selecciona los módulos a utilizar y colócalos en la estación de trabajo:
- a. Fuente de alimentación (8221)
- b. Transformador (8353)
- c. Interfaz de adquisición de datos y de control

### Paso 3 — Identificación de parámetros

Identifica los parámetros de los módulos seleccionados y completa la **Tabla 1**:

- **Parámetros de la fuente de alimentación:** tensión alterna variable.
- **Parámetros del transformador:** número de vueltas del devanado primario, la resistencia de la bobina primaria del transformador (con un ohmímetro) y tensión nominal.

#### Tabla 1 — Parámetros del esquema 1

| Parámetro                                                  | Valor          |
| ---------------------------------------------------------- | -------------- |
| Tensión nominal a 60 Hz                                    | 24 voltios AC  |
| Número de vueltas del devanado primario del transformador  | 58             |
| Resistencia del cobre de la bobina primaria del transformador |                |
| Máxima tensión de la fuente variable                       |                |
| Frecuencia de la fuente variable                           |                |

### Paso 4 — Esquema 1 (transformador simple)

Elabora el esquema del circuito magnético con núcleo ferromagnético y devanado con los parámetros identificados.

> [!warning] Seguridad
> Por temas de seguridad, establece la tensión alterna variable de la fuente de alimentación a **0 V** antes de armar el circuito.

- a. Establece la tensión alterna variable de la fuente de alimentación a **0**.
- b. Selecciona el módulo de cables de conexión y **3 multímetros** (1 configurado como amperímetro y 2 como voltímetro) para armar el esquema del circuito y establecer la conexión entre la fuente de alimentación y el transformador, según lo mostrado en la **Imagen 3**.
- c. Establece la tensión alterna variable de la fuente de alimentación a **24 voltios** (tensión nominal del transformador).

![[s05-lab-img3-esquema-monofasico.png]]
*Imagen 3. Esquema de transformador monofásico.*

### Paso 5 — Cálculo de parámetros del esquema 1

Calcula los parámetros del circuito magnético:

- a. Obtén la corriente y voltaje con los multímetros correspondientes.
- b. A partir de los datos obtenidos y en base a las fórmulas correspondientes, calcula la **impedancia, reluctancia, flujo magnético máximo en el circuito, pérdidas en el núcleo y fuerza magnetomotriz**.
- c. A partir de las medidas de $E_1$ e $I_1$, configura en el software LVSIM un **vatímetro** para medir las pérdidas del núcleo. Para ello, dirígete al botón de "Aparatos de medición" en el menú superior. Selecciona en el medidor de potencia $E_1$, $I_1$.
- d. Registra los datos obtenidos en la **Tabla 2**.

#### Tabla 2 — Resultados del esquema 1

| Parámetro                          | Resultado/medición esquema 1 |
| ---------------------------------- | ---------------------------- |
| Corriente                          |                              |
| Voltaje                            |                              |
| Pérdidas en el núcleo              |                              |
| Impedancia                         |                              |
| Flujo magnético máximo en el circuito |                           |
| Fuerza magnetomotriz               |                              |
| Reluctancia                        |                              |

### Paso 6 — Esquema 2 (transformadores en serie)

Modifica el esquema diseñado, agregando otro transformador **en serie**, para recrear el esquema eléctrico de la **Imagen 4**.

- a. Por seguridad, asegúrate de colocar la fuente de corriente en **0 voltios** antes de diseñar el esquema.
- b. Luego, aumenta el voltaje de la fuente de corriente hasta llegar a la tensión nominal de **48 voltios**.

![[s05-lab-img4-esquema-serie.png]]
*Imagen 4. Esquema de transformador monofásico en serie.*

### Paso 7 — Cálculo de parámetros del esquema 2

Con el nuevo esquema implementado, realiza el mismo procedimiento.

- a. Con el ohmímetro, identifica los parámetros de la fuente de alimentación y de los transformadores del nuevo esquema y registra los resultados en la **Tabla 3**.

#### Tabla 3 — Parámetros del esquema 2

| Parámetro                                                  | Valor          |
| ---------------------------------------------------------- | -------------- |
| Tensión nominal a 60 Hz                                    | 48 voltios AC  |
| Número de vueltas del devanado primario del transformador  | 116            |
| Resistencia del cobre de la bobina primaria del transformador |             |
| Máxima tensión de la fuente variable                       |                |
| Frecuencia de la fuente variable                           |                |

- b. A partir de los datos obtenidos y en base a las fórmulas correspondientes, calcula la **impedancia, reluctancia, flujo magnético máximo en el circuito, pérdidas en el núcleo y fuerza magnetomotriz** en el esquema 2. Luego, registra los resultados en la **Tabla 4**.

#### Tabla 4 — Resultados del esquema 2

| Parámetro                          | Resultado esquema 2 |
| ---------------------------------- | ------------------- |
| Corriente                          |                     |
| Voltaje                            |                     |
| Pérdidas en el núcleo              |                     |
| Impedancia                         |                     |
| Flujo magnético máximo en el circuito |                  |
| Fuerza magnetomotriz               |                     |
| Reluctancia                        |                     |

### Paso 8 — Cierre seguro

Para finalizar con el procedimiento de manera segura, **apaga las fuentes de alimentación, desconecta los cables de conexión y coloca los módulos en sus lugares correspondientes**.

---

## Fórmulas a utilizar para el cálculo

> [!abstract] Resumen de fórmulas para los cálculos
> Ver [[Formulario - Motores Eléctricos Estáticos y Rotativos|Formulario]] para el desarrollo completo.
>
> - **Ecuación fundamental del transformador:** $V = 4{,}44 \cdot f \cdot N \cdot \phi_m$
> - **Flujo máximo:** $\phi_m = \dfrac{\sqrt{2} \cdot V}{N \cdot \omega} = \dfrac{V}{4{,}44 \cdot f \cdot N}$
> - **Impedancia:** $Z = \dfrac{V}{I}$
> - **Fuerza magnetomotriz:** $\mathcal{F} = N \cdot I$
> - **Ley de Hopkinson (reluctancia):** $\mathcal{R} = \dfrac{\mathcal{F}}{\phi_m} = \dfrac{N \cdot I}{\phi_m}$
> - **Pérdidas en el núcleo:** $P_{Fe}$ medido directamente con vatímetro $(E_1, I_1)$.

---

## Entregables

Elaborar el informe final en base a la siguiente estructura:

1. **Carátula:** incluye nombre, apellidos y código.

2. **Esquema 1:**
   - a. Parámetros de la fuente de alimentación y transformador del esquema 1: incluir la **Tabla 1** completada y una imagen de evidencia del procedimiento realizado.
   - b. Esquema del transformador monofásico: colocar una imagen del esquema elaborado, según lo especificado.
   - c. Parámetros del circuito del esquema 1: calcular los parámetros del circuito, incluir el desarrollo de las fórmulas correspondientes. Finalmente, presentar la **Tabla 2** completa con los valores obtenidos.

3. **Esquema 2:**
   - a. Parámetros de la fuente de alimentación y transformadores del esquema 2: incluir la **Tabla 3** completada y una imagen de evidencia del procedimiento realizado.
   - b. Esquema del transformador monofásico en serie: colocar una imagen del esquema elaborado, según lo especificado.
   - c. Parámetros del circuito del esquema 2: calcular los parámetros del circuito, incluir el desarrollo de las fórmulas correspondientes. Finalmente, presentar la **Tabla 4** completa con los valores obtenidos.

4. **Análisis de resultados:** De acuerdo a los resultados obtenidos, analizarlos en base a los valores teóricos en un texto de una extensión **mayor a 1 hoja**. Prestar especial atención a las diferencias de las variables calculadas y medidas de las **Tablas 2 y 4** para los dos esquemas.

5. **Conclusiones:** redactar **al menos 4 conclusiones** de la experiencia y los resultados obtenidos.

> [!tip] Indicaciones y rúbrica
> Las indicaciones específicas de entrega, formato del informe y la rúbrica detallada de calificación se encuentran en una nota separada: [[S05-98 Indicaciones y Rubrica - LC1 Laboratorio|S05-98 Indicaciones y Rúbrica LC1]].

---

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5ta. ed.). McGraw-Hill Interamericana.
- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6ta. ed.). McGraw-Hill Interamericana.
- LabVolt Series (2013). *Relaciones de tensiones y corrientes*. En *Electricidad y Nuevas Energías – Transformadores de potencia monofásicos* (pp. 8-21). Québec, Canadá: Festo Didactic. ISBN 978-2-89640-664-7.
- LabVolt Series (2013). *Apéndices*. En *Electricidad y Nuevas Energías – Circuitos ca monofásicos* (pp. 121-131). Québec, Canadá: Festo Didactic. ISBN 978-2-89640-664-7.
