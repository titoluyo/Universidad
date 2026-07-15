---
title: "Ejercicio resuelto - Ecuación de potencia"
curso: "[[Motores MOC]]"
unidad: 4
semana: 16
orden: 4
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/flujo-de-potencia
  - tema/potencia-en-el-entrehierro
  - tema/eficiencia
date: 2026-07-06
---

> [!info] Material original
> Ejercicio en video del docente ([YouTube](https://www.youtube.com/watch?v=ONIuPwUrT90)). Guion (transcripción): [S16-Guion-Ejercicio-ecuacion-de-potencia.pdf](attachments/S16-Guion-Ejercicio-ecuacion-de-potencia.pdf) (UTP, Semana 16).

## Enunciado

A un **motor de inducción trifásico** de $480\ \text{V}$, $60\ \text{Hz}$ y $50\ \text{hp}$ se le suministran $60\ \text{A}$ con un factor de potencia de $0{,}85$ **en retraso**. Se conocen las siguientes pérdidas:

- Pérdidas en el cobre del estator: $2\ \text{kW}$.
- Pérdidas en el cobre del rotor: $700\ \text{W}$.
- Pérdidas por fricción y rozamiento con el aire: $600\ \text{W}$.
- Pérdidas en el núcleo: $1800\ \text{W}$.
- Pérdidas misceláneas: **despreciables**.

Se pide calcular:

- **a)** Potencia en el entrehierro.
- **b)** Potencia convertida.
- **c)** Potencia de salida.
- **d)** Eficiencia del motor.

## Datos

| Magnitud | Símbolo | Valor |
| --- | --- | --- |
| Tensión de línea | $V_L$ | $480\ \text{V}$ |
| Frecuencia | $f_e$ | $60\ \text{Hz}$ |
| Potencia nominal | — | $50\ \text{hp}$ |
| Corriente de línea | $I_L$ | $60\ \text{A}$ |
| Factor de potencia | $\cos\varphi$ | $0{,}85$ en retraso |
| Pérdidas cobre estator | $P_{PCE}$ | $2\ \text{kW}$ |
| Pérdidas cobre rotor | $P_{PCR}$ | $700\ \text{W}$ |
| Pérdidas fricción y rozamiento | $P_{FyR}$ | $600\ \text{W}$ |
| Pérdidas en el núcleo | $P_{núcleo}$ | $1800\ \text{W}$ |
| Pérdidas misceláneas | $P_{misc}$ | $0\ \text{W}$ |

La estrategia consiste en recorrer el **diagrama de flujo de potencia** del [[S16-3 Tema 03 - Potencia y par en los motores de inducción|motor de inducción]] de arriba hacia abajo, restando en cada escalón las pérdidas correspondientes.

## Potencia de entrada

La potencia de entrada de un sistema trifásico se calcula a partir de las magnitudes de línea:

$$P_{entr} = \sqrt{3}\,V_L\,I_L\,\cos\varphi$$

- $V_L$ = tensión de línea; $I_L$ = corriente de línea.
- $\cos\varphi$ = factor de potencia.

Reemplazando los datos:

$$P_{entr} = \sqrt{3}\,(480)(60)(0{,}85) = 42\,400{,}6\ \text{W} \approx 42{,}4\ \text{kW}$$

## a) Potencia en el entrehierro

La potencia en el entrehierro es la potencia de entrada **menos** las primeras pérdidas del recorrido: las del **cobre del estator** y las del **núcleo**.

$$P_{EH} = P_{entr} - P_{PCE} - P_{núcleo}$$

$$P_{EH} = 42{,}4 - 2 - 1{,}8 = 38{,}6\ \text{kW}$$

$$\boxed{P_{EH} = 38{,}6\ \text{kW}}$$

## b) Potencia convertida

Una vez la potencia cruza el entrehierro, el rotor consume sus propias pérdidas $I^2R$ y **el resto se convierte** de forma eléctrica a mecánica:

$$P_{conv} = P_{EH} - P_{PCR}$$

$$P_{conv} = 38{,}6\ \text{kW} - 0{,}7\ \text{kW} = 37{,}9\ \text{kW}$$

$$\boxed{P_{conv} = 37{,}9\ \text{kW}}$$

## c) Potencia de salida

Del lado mecánico aún deben descontarse las pérdidas por **fricción y rozamiento con el aire** y las **misceláneas**:

$$P_{sal} = P_{conv} - P_{FyR} - P_{misc}$$

$$P_{sal} = 37{,}9\ \text{kW} - 0{,}6\ \text{kW} - 0\ \text{kW} = 37{,}3\ \text{kW}$$

$$\boxed{P_{sal} = 37{,}3\ \text{kW}}$$

## d) Eficiencia del motor

La eficiencia es el cociente entre la potencia que sale por el eje y la que entra por los bornes:

$$\eta = \frac{P_{sal}}{P_{entr}} \times 100\ \%$$

$$\eta = \frac{37{,}3\ \text{kW}}{42{,}4\ \text{kW}} \times 100\ \% = 87{,}97\ \% \approx 88\ \%$$

$$\boxed{\eta \approx 88\ \%}$$

> [!note] Dato inconsistente
> En el video, al calcular la eficiencia se lee la potencia de entrada como $42{,}2\ \text{kW}$, mientras que el valor obtenido al inicio —y confirmado por $\sqrt{3}(480)(60)(0{,}85) = 42\,400{,}6\ \text{W}$— es $42{,}4\ \text{kW}$. Se trata de un lapsus de lectura sin consecuencias: con $42{,}4\ \text{kW}$ resulta $\eta = 87{,}97\ \%$ y con $42{,}2\ \text{kW}$ resulta $\eta = 88{,}4\ \%$; ambos **redondean a $88\ \%$**. Aquí se conserva $42{,}4\ \text{kW}$ por coherencia con el resto del desarrollo.

> [!success] Resultados
> | Inciso | Magnitud | Resultado |
> | --- | --- | --- |
> | a) | Potencia en el entrehierro | $P_{EH} = 38{,}6\ \text{kW}$ |
> | b) | Potencia convertida | $P_{conv} = 37{,}9\ \text{kW}$ |
> | c) | Potencia de salida | $P_{sal} = 37{,}3\ \text{kW}$ |
> | d) | Eficiencia | $\eta \approx 88\ \%$ |
>
> El ejercicio es una aplicación directa del **diagrama de flujo de potencia**: basta ir restando cada pérdida en el orden en que aparece ($P_{entr} \to P_{PCE},\,P_{núcleo} \to P_{EH} \to P_{PCR} \to P_{conv} \to P_{FyR},\,P_{misc} \to P_{sal}$), sin necesidad de resolver el circuito equivalente.

> [!tip] Verificación de coherencia
> Las pérdidas totales suman $2 + 1{,}8 + 0{,}7 + 0{,}6 = 5{,}1\ \text{kW}$, y en efecto $42{,}4 - 5{,}1 = 37{,}3\ \text{kW} = P_{sal}$. Además, $P_{sal} = 37{,}3\ \text{kW} \approx 50{,}0\ \text{hp}$ (con $1\ \text{hp} = 746\ \text{W}$), lo que confirma que el motor está operando **a su potencia nominal de $50\ \text{hp}$**.

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
- Pretel Díaz, Ch. H. (2026). *Ejercicio de ecuación de potencia* [Video – Guion]. UTP+class.
