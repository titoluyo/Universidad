---
title: "Tema 02 - Análisis de la placa de característica del motor asíncrono"
curso: "[[Motores MOC]]"
unidad: 4
semana: 17
orden: 3
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/placa-de-caracteristicas
  - tema/motor-de-induccion
  - tema/clase-nema
  - tema/valores-nominales
date: 2026-07-13
---

> [!info] Material original
> Infografía del portal UTP: [S17-Infografia-Placa-caracteristica.pdf](attachments/S17-Infografia-Placa-caracteristica.pdf) (UTP, Semana 17).

La **placa de características** (*nameplate*) es la ficha de identidad del motor: resume los valores nominales bajo los cuales el fabricante garantiza su operación. Saber leerla permite verificar si un motor es apto para una carga determinada, cómo debe conectarse y qué comportamiento tendrá en el arranque.

## Valores nominales de la placa

En la Figura 1 se muestra la placa de características de un típico **motor de inducción** de tamaño pequeño a medio y de **alta eficiencia**. Los valores nominales más importantes que se presentan en ella son:

1. **Potencia de salida** (caballos de fuerza en Estados Unidos y kilowatts en el resto del mundo).
2. **Voltaje**.
3. **Corriente**.
4. **Factor de potencia**.
5. **Velocidad**.
6. **Eficiencia nominal**.
7. **Clase NEMA de diseño**.

### Figura 1. Placa de un motor de inducción de alta eficiencia

Placa del fabricante **Louis Allis** (Litton, Milwaukee, Wisconsin 53201), modelo *SPARTAN MOTOR*. Sus campos y valores son:

| Campo de la placa | Valor | Significado |
| --- | --- | --- |
| MODEL | 27987J-X | Modelo del fabricante |
| TYPE | CJ4B | Tipo constructivo |
| FRAME | 324TS | Carcasa normalizada NEMA |
| VOLTS | 230/460 | Tensión nominal (doble tensión) |
| °C AMB. / INS. CL. | 40 / B | Temperatura ambiente máxima y clase de aislamiento |
| SERV. FACT. | 1.0 | Factor de servicio |
| 1ST BRG / 2ND BRG | 210 SF / 312 SF | Rodamientos delantero y trasero |
| PHASE | 3 | Número de fases |
| HZ | 60 | Frecuencia nominal |
| CODE | G | Letra de código NEMA de arranque (ver Tabla 1) |
| WDGS. | 1 | Devanados |
| OPER. INSTR. | C-517 | Instrucciones de operación |
| H.P. | 40 | Potencia de salida nominal |
| R.P.M. | 3565 | Velocidad nominal a plena carga |
| AMPS | 97 / 48.5 | Corriente nominal (a 230 V / a 460 V) |
| NEMA NOM. EFF. | .936 | Eficiencia nominal NEMA (93.6 %) |
| NOM. P.F. | .827 | Factor de potencia nominal (0.827) |
| DUTY | Cont | Régimen de trabajo continuo |
| NEMA DESIGN | B | Clase NEMA de diseño |

La placa incluye además las **tablas de conexión** de los terminales ($T_1$ a $T_9$), que indican cómo agrupar y unir las bobinas según se trabaje con **devanado completo** (*full winding*, en baja o alta tensión) o con **devanado parcial** (*part winding*, solo en baja tensión), señalando en cada caso las conexiones del arrancador (*starter*), del contactor de arranque y del contactor de marcha, y las líneas $L_1$, $L_2$, $L_3$ que se conectan a cada terminal.

> [!tip] Doble tensión y corriente nominal
> Los valores `VOLTS 230/460` y `AMPS 97/48.5` van emparejados: al **duplicar** la tensión de alimentación, la corriente nominal se **reduce a la mitad** para la misma potencia de salida (40 HP). La tabla de conexiones de la placa indica el reagrupamiento de bobinas necesario para cada tensión.

> **Figura 1.** Placa de características de un típico motor de inducción de alta eficiencia.

## Tabla 1. Letras de código NEMA

A continuación se presentan algunas imágenes importantes que permiten analizar a mayor detalle la placa característica del motor asíncrono.

La **letra de código NEMA** indica los **kVA/hp de arranque nominales** del motor, es decir, la potencia aparente que demanda con el **rotor bloqueado** por cada caballo de fuerza nominal. Cada letra de código se extiende **hasta, pero no incluye**, el límite inferior de la siguiente clase superior.

| Letra código nominal | Rotor bloqueado, kVA/hp | Letra código nominal | Rotor bloqueado, kVA/hp |
| :---: | :---: | :---: | :---: |
| A | 0 - 3.15 | L | 9.00 - 10.00 |
| B | 3.15 - 3.55 | M | 10.00 - 11.00 |
| C | 3.55 - 4.00 | N | 11.20 - 12.50 |
| D | 4.00 - 4.50 | P | 12.50 - 14.00 |
| E | 4.50 - 5.00 | R | 14.00 - 16.00 |
| F | 5.00 - 5.60 | S | 16.00 - 18.00 |
| G | 5.60 - 6.30 | T | 18.00 - 20.00 |
| H | 6.30 - 7.10 | U | 20.00 - 22.40 |
| J | 7.10 - 8.00 | V | 22.40 y más |
| K | 8.00 - 9.00 | | |

> **Tabla 1.** Tabla de letras de código NEMA que indica los kVA/hp de arranque nominales de un motor. Cada letra de código se extiende hasta, pero no incluye, el límite inferior de la siguiente clase superior.

> [!example] Lectura del código de la Figura 1
> El motor de la Figura 1 tiene `CODE G` y `H.P. 40`. Según la Tabla 1, la letra **G** corresponde a **5.60 - 6.30 kVA/hp** con rotor bloqueado, de modo que la potencia aparente de arranque está entre $40 \times 5.60 = 224\ \text{kVA}$ y $40 \times 6.30 = 252\ \text{kVA}$. Con ese dato se estima la **corriente de arranque** y se dimensionan protecciones y arrancador.

## Figura 2. Placa de un motor síncrono grande

La Figura 2 muestra la placa de características típica de un **motor síncrono grande**, del fabricante **General Electric** (Schenectady, N.Y., *Made in U.S.A.*). Frente a la del motor de inducción, aparecen campos propios de la excitación del rotor:

| Campo de la placa | Valor | Significado |
| --- | --- | --- |
| RATED HP | 21,000 | Potencia nominal de salida |
| RPM | 1200 | Velocidad síncrona |
| PF | 1.0 | Factor de potencia nominal |
| VOLTS | 6600 | Tensión nominal del estator |
| PHASE | 3 | Número de fases |
| FREQ | 60 | Frecuencia nominal |
| CODE | B | Letra de código NEMA |
| AMP | 1404 | Corriente nominal del estator |
| FRAME | 9398 | Carcasa |
| TYPE | TS | Tipo constructivo |
| EXCITATION-VOLTS | 125 | Tensión de excitación del campo |
| AMP (excitación) | 5.2 | Corriente de excitación del campo |
| HP 21,000 CONT. | 80 °C RISE (estator, por RTD) / 105 °C RISE (rotor, por resistencia) | Elevación de temperatura admisible en régimen continuo |
| OUTLINE | B1GE357 | Plano de dimensiones |
| MODEL | 264×766 | Modelo |
| SER. NO. | 837405I | Número de serie |
| INSTRUCTIONS | GEK-42586 | Manual de instrucciones |
| CONN. DIAG. | 34A150850 | Diagrama de conexiones |

La placa advierte (*CAUTION*) que **antes de instalar u operar** el motor deben leerse las instrucciones y el diagrama de conexiones indicados, y que al pedir repuestos deben proporcionarse el **modelo** y el **número de serie**.

> **Figura 2.** Placa de características típica de un motor síncrono grande.

> [!summary] Idea central
> La placa de características condensa los **valores nominales** del motor: potencia de salida, voltaje, corriente, factor de potencia, velocidad, eficiencia nominal y clase NEMA de diseño. En un motor de inducción de doble tensión (`230/460 V`, `97/48.5 A`), tensión y corriente van emparejadas según la conexión de las bobinas. La **letra de código** (Tabla 1) traduce la placa en **kVA/hp con rotor bloqueado**, dato clave para estimar la corriente de arranque y dimensionar las protecciones. La placa de un [[S17-4 Tema 03 - Máquina síncrona trifásica|motor síncrono]] añade además los datos de **excitación** (tensión y corriente de campo) y las elevaciones de temperatura admisibles de estator y rotor.

## Bibliografía

- Chapman, S. J. (2012). *Máquinas eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
