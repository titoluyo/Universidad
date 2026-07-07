# GUÍA N° 3: FILTRO ACTIVO PASA BAJO

| CURSO | AMBIENTE |
| --- | --- |
| CIRCUITOS ELECTRÓNICOS AMPLIFICADORES | LABORATORIO DE ELECTRÓNICA GENERAL |

| | |
| --- | --- |
| **ELABORADO POR** | ALBERTO ALVARADO |
| **APROBADO POR** | DDA INGENIERIAS ELECTRONICAS |
| **VERSIÓN** | 005 |
| **FECHA DE APROBACIÓN** | 24/10/2025 |

## 1. Logro general de la unidad de aprendizaje

Al finalizar la unidad, el estudiante desarrolla los diferentes modelos de filtros activos y la respuesta en frecuencia de amplificadores en casos prácticos.

## 2. Objetivos específicos de la práctica

Al final del laboratorio, el estudiante analiza e implementa el amplificador operacional como filtro activo pasa bajo y medición de su respuesta en frecuencia.

## 3. Materiales y equipos

- GENERADOR DE FUNCIONES 220 V
- MULTIMETRO DIGITAL CD 771
- PROTOBOARD 1660 PUNTOS
- OSCILOSCOPIO DIGITAL
- CABLE DE HILO DE COBRE PARA PROTOBOARD MACHO-MACHO
- CIRCUITO INTEGRADO LM741
- COMPONENTE ELECTRONICO CONDENSADOR ELECTROLITICO 0.1 UF / 25 V
- COMPONENTE ELECTRONICO RESISTENCIA 10 K OHM 1/2 W
- CABLE DE HILO DE COBRE PARA PROTOBOARD MACHO-HEMBRA
- FUENTE DE ALIMENTACION 2231A 30 V 3 A
- CABLE DE HILO DE COBRE PARA PROTOBOARD HEMBRA-HEMBRA

### Materiales que trae el alumno

- COMPONENTE ELECTRONICO RESISTENCIA 3.3K OHM - 1/2W

## 4. Pautas de seguridad

### 4.1. Recomendaciones de seguridad:

a. El laboratorio cuenta con señaléticas de prohibiciones, seguridad y emergencias, los cuales deben ser respetados.
b. Es responsabilidad del alumno o grupo de trabajo mantener el orden y limpieza.
c. Todos los equipos deben ser maniobrados bajo la estricta supervisión del docente del curso.
d. Todo el grupo de trabajo es responsable por la rotura y/o deterioro del material entregado y/o equipos del laboratorio durante el desarrollo de las prácticas.

### 4.2. Uso de EPP

a. Guardapolvo.

## 5. Fundamento

Los filtros activos se caracterizan por tener la posibilidad de tener una ganancia mayor que la unidad, además de seleccionar el rango de frecuencias.

El amplificador operacional permite explotar más fácilmente estas características, además de conseguirse un tamaño reducido del filtro. Con él, un método de diseño consiste en emplear simultáneamente realimentación negativa y positiva, manteniendo un comportamiento lineal, como es el caso del circuito de la experiencia.

> [!note] Circuito del fundamento (filtro activo pasa bajo Sallen-Key con LM741)
> - R2 = 10K (realimentación, terminal inversor — pin 2)
> - R1 = 10K (de inversor a tierra)
> - LM741: salida en pin 6, V+ en pin 3, V− en pin 2, alimentación +Vcc / −Vcc
> - R = 3K3 y C = 0.1uF en la red de entrada (rama no inversora) y en la rama de realimentación positiva
> - Vi: generador senoidal de entrada; Vo: salida

La tensión de salida la podemos hallar en función de V+ empleando la ecuación de ganancia del amplificador no inversor:

$$V_o = \left(1 + \frac{R_2}{R_1}\right) V^+ = A \cdot V^+$$

$$A = \left(1 + \frac{R_2}{R_1}\right)$$

A continuación, hallamos V en función de Vi y Vo:

**En el nudo V+:**

$$\frac{V^+ - V_i}{R} + sC\,(V^+ - V) = 0$$

**De aquí:**

$$V = \left[\frac{1 + RC\,s}{A\,RC\,s}\right] V_o - \frac{V_i}{RC\,s}$$

**En el nudo V−:**

$$(V - V^+)\,C\,s + V\,C\,s + \frac{V - V_o}{R} = 0$$

**De aquí:**

$$V\,(2RC\,s + 1) = (RC\,s)\,V^+ + V_o$$

Reemplazando V y despejando la función de transferencia:

$$H(s) = \frac{A\,(1 + 2RCS)}{R^2 C^2 S^2 + (3 - A)\,RCS + 1}$$

El denominador de la función de transferencia corresponde a la ecuación diferencial en el dominio del tiempo y poder identificar la frecuencia natural y el factor de atenuación:

- **Frecuencia natural:** $\omega_o = \dfrac{1}{RC}$
- **Factor de atenuación:** $\alpha = \dfrac{3 - A}{2RC}$
- **Factor de calidad:** $Q = \dfrac{\omega_o}{2\alpha} = \dfrac{1}{3 - A}$
- **Relación de amortiguación:** $\zeta = \dfrac{\alpha}{\omega_o} = \dfrac{3 - A}{2}$

Si queremos una respuesta sobre amortiguada con poco sobre impulso podemos elegir una relación de amortiguación cercana a 0.7, requeriremos de una ganancia de A = 1.6.

## 6. Procedimiento (desarrollo de la práctica)

1. Ensamble el siguiente circuito:

> [!note] Circuito a ensamblar
> - R2 = 10K (realimentación)
> - R1 = 10K
> - LM741: alimentación +12 V (pin 7) y −12 V (pin 4); salida pin 6; V+ pin 3; V− pin 2
> - R3 = 5.6K y C1 = 0.1uF en la rama de entrada
> - R3 = 5.6K y C2 = 0.1uF en la rama de realimentación positiva
> - Vi: generador senoidal; Vo: salida

2. Ponga especial cuidado al momento de conectar las tensiones de alimentación:

   **Pin 7: +12 Vdc, Pin 4: −12 Vdc**

3. Ajuste el voltaje del generador a Vi = 1 voltio pico, con frecuencia de 1KHz, onda sinusoidal.

4. Varíe la frecuencia del generador y mida el voltaje de salida en cada caso y anote los resultados en la tabla siguiente. También determine la ganancia de tensión para cada caso:

| F [Hz] | 50 | 100 | 150 | 200 | 250 | 300 | 350 | 400 | 450 | 500 | 1K | 2K | 5K | 10K |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Vo | | | | | | | | | | | | | | |
| Av | | | | | | | | | | | | | | |

## 7. Entregables

1. Haga una tabla comparando los valores teóricos con los experimentales y explique las razones de las diferencias que hubiere.
2. Halle los diagramas de Bode empleando MATLAB.
3. ¿Qué conclusiones saca de las mediciones efectuadas?
4. Presente el informe completo la siguiente clase práctica.

## 8. Fuentes de información complementaria

- FILTRO PASA BAJO — https://www.youtube.com/watch?v=zu3OpwCOJy4
