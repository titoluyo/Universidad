---
title: "Tema 04 - Principio de funcionamiento como generador"
curso: "[[Motores MOC]]"
unidad: 4
semana: 17
orden: 5
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/generador-sincrono
  - tema/circuito-de-campo
  - tema/excitador-sin-escobillas
  - tema/velocidad-de-sincronismo
date: 2026-07-13
---

> [!info] Material original
> Manual del docente: [S17-Manual-Principio-funcionamiento-como-generador.pdf](attachments/S17-Manual-Principio-funcionamiento-como-generador.pdf) (UTP, Semana 17).

## Principio de funcionamiento como generador

Los **generadores síncronos** o **alternadores** son máquinas síncronas empleadas para transformar **potencia mecánica en potencia eléctrica de corriente alterna**.

En un generador síncrono, se genera un campo magnético en el **rotor** de dos formas posibles:

- Usando un **imán permanente**, o
- Aplicando **corriente continua** a su devanado para formar un **electroimán**.

Luego, el rotor gira gracias a un **motor primario**, creando un **campo magnético giratorio** en la máquina. Este campo magnético induce un **conjunto de voltajes trifásicos** en los devanados del **estator** del generador.

> [!note] Relación con el motor síncrono
> El principio es el mismo que el estudiado en la [[S17-4 Tema 03 - Máquina síncrona trifásica|máquina síncrona trifásica]], operando en sentido inverso: allí la red impone $V_\phi$ y la máquina entrega par mecánico; aquí el motor primario impone la velocidad y la máquina entrega potencia eléctrica. De hecho, el circuito equivalente es **idéntico** salvo por la dirección de referencia de la corriente de armadura $I_A$.

## Construcción del rotor y alimentación del circuito de campo

Debido a la **variación de los campos magnéticos** en el rotor, este se construye con **láminas delgadas** para minimizar las **pérdidas por corrientes parásitas**. El circuito de campo del rotor se alimenta con **corriente continua**.

Dado que el rotor está **en movimiento**, se necesita un método especial para proporcionar la potencia de corriente continua a los devanados del campo. Hay **dos formas comunes** de suministrar esta potencia continua:

1. Suministrar la potencia de corriente continua al rotor **desde una fuente externa**, mediante **anillos rozantes y escobillas**.
2. Proveer la potencia **directamente desde una fuente de corriente continua montada en el eje** del generador síncrono.

### Excitadores sin escobillas

En **generadores y motores de gran tamaño** se emplean **excitadores sin escobillas** para alimentar la corriente de campo continua. Estos excitadores consisten en **pequeños generadores de corriente alterna** con:

- Un **circuito de campo en el estator**, y
- Un **circuito de armadura acoplado al eje del rotor**.

Los excitadores sin escobillas, al **carecer de contacto mecánico** entre el rotor y el estator, necesitan **considerablemente menos mantenimiento** en comparación con los sistemas que emplean anillos rozantes y escobillas.

## La velocidad de rotación de un generador síncrono

Los generadores síncronos son **inherentemente síncronos**, lo que implica que la **frecuencia eléctrica está sincronizada con la velocidad de rotación** del generador. Su rotor, equipado con un electroimán alimentado con corriente continua, genera un campo magnético que **sigue la rotación del rotor**.

La velocidad de rotación de los campos magnéticos en la máquina está vinculada a la frecuencia eléctrica del estator mediante la ecuación:

$$f_e = \frac{n_m\,p}{120}$$

- $f_e$ = frecuencia eléctrica generada en el estator ($\text{Hz}$).
- $n_m$ = velocidad mecánica de rotación del rotor ($\text{rpm}$), igual a la velocidad del campo magnético.
- $p$ = número de polos de la máquina.

Esta ecuación vincula la velocidad de rotación del rotor con la frecuencia eléctrica resultante, **ya que el rotor gira a la misma velocidad que el campo magnético**.

Dado que la potencia eléctrica se genera a **50 o 60 Hz**, la velocidad de rotación del generador debe ser **constante** y depende del **número de polos** de la máquina. Por ejemplo:

| Frecuencia | Polos | Velocidad requerida |
| --- | --- | --- |
| $60\ \text{Hz}$ | $2$ | $3600\ \text{rpm}$ |
| $50\ \text{Hz}$ | $4$ | $1500\ \text{rpm}$ |

Es decir, para generar $60\ \text{Hz}$ con **dos polos** el rotor debe girar a $3600\ \text{rpm}$, mientras que para generar $50\ \text{Hz}$ con **cuatro polos** debe girar a $1500\ \text{rpm}$.

> [!summary] Idea central
> El generador síncrono (alternador) convierte **potencia mecánica en eléctrica trifásica**: el rotor, excitado en **corriente continua** (o con imán permanente), es arrastrado por un **motor primario** y su campo giratorio induce las tensiones en el estator. La CC llega al campo mediante **anillos rozantes y escobillas** o, en máquinas grandes, con **excitadores sin escobillas** (menos mantenimiento). La ligadura fundamental es $f_e = n_m\,p/120$: como la red exige $50$ o $60\ \text{Hz}$, la **velocidad queda fija** por el número de polos —$3600\ \text{rpm}$ para $60\ \text{Hz}$ con 2 polos, $1500\ \text{rpm}$ para $50\ \text{Hz}$ con 4 polos—. Es la misma relación que fija la velocidad del motor síncrono, leída al revés.

## Bibliografía

- Chapman, S. J. (2012). *Máquinas eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
