---
title: "Ejercicio resuelto - Máquina asíncrona trifásica"
curso: "[[Motores MOC]]"
unidad: 4
semana: 15
orden: 2
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/maquina-asincrona
  - tema/deslizamiento
  - tema/velocidad-de-sincronismo
  - tema/frecuencia-del-rotor
date: 2026-06-29
---

> [!info] Material original
> Ejercicio en video del docente ([YouTube](https://www.youtube.com/watch?v=1P2YMyj1dVA)). Guion (transcripción): [S15-Guion-Ejercicio-maquina-asincrona-trifasica.pdf](attachments/S15-Guion-Ejercicio-maquina-asincrona-trifasica.pdf) (UTP, Semana 15).

## Enunciado

Un **motor de inducción** de $208\ \text{V}$, $10\ \text{hp}$, **cuatro polos**, $60\ \text{Hz}$, **conectado en "Y"**, tiene un **deslizamiento a plena carga de** $5\ \%$. Calcular:

- **a)** ¿Cuál es la **velocidad síncrona** del motor?
- **b)** ¿Cuál es la **velocidad del rotor** con carga nominal?
- **c)** ¿Cuál es la **frecuencia del rotor** con carga nominal?

## Datos

| Dato | Valor |
| --- | --- |
| Tensión de línea | $208\ \text{V}$ |
| Potencia nominal | $10\ \text{hp}$ |
| Número de polos | $4$ → $p = 2$ pares de polos |
| Frecuencia del estator | $f_1 = 60\ \text{Hz}$ |
| Conexión | Estrella (Y) |
| Deslizamiento a plena carga | $s = 5\ \% = 0{,}05$ |

> [!tip] Datos que no se usan
> La tensión ($208\ \text{V}$), la potencia ($10\ \text{hp}$) y la conexión en **Y** **no intervienen** en ningún cálculo de este ejercicio: las tres preguntas dependen únicamente de $f_1$, del número de polos y del deslizamiento. Son datos de placa que servirían para el [[S16-2 Tema 02 - Circuito equivalente de un motor de inducción|circuito equivalente]] o para el balance de potencias, no para la cinemática del campo giratorio.

## a) Velocidad síncrona

La **velocidad de sincronismo** $n_1$ es la velocidad a la que gira el campo magnético creado por el devanado trifásico del estator:

$$n_1 = \frac{60\,f_1}{p}$$

- $n_1$ = velocidad de sincronismo (rpm).
- $f_1$ = frecuencia de alimentación del estator (Hz).
- $p$ = número de **pares** de polos.

Como el motor tiene **4 polos**, el número de **pares** de polos es $p = 4/2 = 2$:

$$n_1 = \frac{60 \times 60}{2} = \frac{3600}{2}$$

$$\boxed{n_1 = 1800\ \text{rpm}}$$

> [!warning] Polos vs. pares de polos
> El error más frecuente aquí es sustituir $p = 4$ y obtener $900\ \text{rpm}$. La fórmula $n_1 = 60f_1/p$ usa **pares de polos**, no polos. Con la variante en función del número de polos $P$ la expresión equivalente sería $n_1 = 120f_1/P = (120 \times 60)/4 = 1800\ \text{rpm}$ — mismo resultado.

## b) Velocidad del rotor con carga nominal

La velocidad del rotor $n_2$ se obtiene despejándola de la definición de deslizamiento $s = \dfrac{n_1 - n_2}{n_1}$:

$$n_2 = (1 - s)\,n_1$$

- $n_2$ = velocidad del rotor (rpm).
- $s$ = deslizamiento (en tanto por uno).
- $n_1$ = velocidad de sincronismo (rpm).

Sustituyendo $s = 0{,}05$ y $n_1 = 1800\ \text{rpm}$:

$$n_2 = (1 - 0{,}05)(1800) = (0{,}95)(1800)$$

$$\boxed{n_2 = 1710\ \text{rpm}}$$

> [!note] Dato inconsistente
> En el guion del video el docente enuncia el deslizamiento como *"el cinco por ciento, cero coma cinco"*. En tanto por uno, $5\ \% = 0{,}05$, **no** $0{,}5$ (que sería un 50 % de deslizamiento y daría $n_2 = 900\ \text{rpm}$). Se trata de un lapsus verbal: el cálculo del video sí utiliza $0{,}05$ y llega correctamente a $1710\ \text{rpm}$, valor que se sigue aquí.

El resultado es coherente con la teoría: el rotor gira **ligeramente por debajo** del sincronismo (90 rpm menos), que es la condición necesaria para que exista FEM inducida, corriente en el rotor y, por tanto, par.

## c) Frecuencia del rotor con carga nominal

La **frecuencia del rotor** es igual al deslizamiento multiplicado por la frecuencia del estator:

$$f_r = s \cdot f_e$$

- $f_r$ = frecuencia del rotor (Hz).
- $s$ = deslizamiento.
- $f_e$ = frecuencia del estator (Hz).

Sustituyendo:

$$f_r = (0{,}05)(60)$$

$$\boxed{f_r = 3\ \text{Hz}}$$

Se puede verificar con la identidad $f_2 = f_1 - \dfrac{n_2\,p}{60} = 60 - \dfrac{(1710)(2)}{60} = 60 - 57 = 3\ \text{Hz}$, y con $s = \dfrac{f_2}{f_1} = \dfrac{3}{60} = 0{,}05$ ✓.

> [!success] Resultados
> | Pregunta | Fórmula | Resultado |
> | --- | --- | --- |
> | a) Velocidad síncrona | $n_1 = \dfrac{60 f_1}{p}$ | $n_1 = 1800\ \text{rpm}$ |
> | b) Velocidad del rotor | $n_2 = (1-s)\,n_1$ | $n_2 = 1710\ \text{rpm}$ |
> | c) Frecuencia del rotor | $f_r = s\,f_e$ | $f_r = 3\ \text{Hz}$ |
>
> Las tres respuestas salen de las relaciones básicas de la [[S15-1 Tema 01 - Máquinas de corriente alterna|máquina asíncrona]]: el campo gira a $1800\ \text{rpm}$, el rotor lo persigue 90 rpm por detrás ($s = 5\ \%$) y las barras del rotor ven esa diferencia como una frecuencia de solo $3\ \text{Hz}$. La potencia y el par que entrega el motor en estas condiciones se calculan en [[S16-3 Tema 03 - Potencia y par en los motores de inducción]].

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
- Pretel Díaz, Ch. H. (2026). *Ejercicio de máquina asíncrona trifásica* [Video – Guion]. UTP+class.
