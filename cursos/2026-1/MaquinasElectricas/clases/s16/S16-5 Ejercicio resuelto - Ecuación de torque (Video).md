---
title: "Ejercicio resuelto - Ecuación de torque"
curso: "[[Motores MOC]]"
unidad: 4
semana: 16
orden: 5
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/par-inducido
  - tema/circuito-equivalente
  - tema/deslizamiento
  - tema/eficiencia
date: 2026-07-06
---

> [!info] Material original
> Ejercicio en video del docente ([YouTube](https://www.youtube.com/watch?v=l-YJ5Zo1MUE)). Guion (transcripción): [S16-Guion-Ejercicio-ecuacion-de-torque.pdf](attachments/S16-Guion-Ejercicio-ecuacion-de-torque.pdf) (UTP, Semana 16).

## Enunciado

Un **motor de inducción de cuatro polos**, $460\ \text{V}$, $25\ \text{hp}$, $60\ \text{Hz}$, **conectado en Y**, tiene las siguientes impedancias en ohms **por fase referidas al circuito del estator**:

$$R_1 = 0{,}641\ \Omega \qquad R_2 = 0{,}332\ \Omega$$
$$X_1 = 1{,}106\ \Omega \qquad X_2 = 0{,}464\ \Omega \qquad X_M = 26{,}3\ \Omega$$

Las **pérdidas por rotación totales** son de $1100\ \text{W}$ y se suponen **constantes**. Las **pérdidas en el núcleo se agrupan con las pérdidas por rotación**. Para un **deslizamiento del rotor de $2{,}2\ \%$** a voltaje y frecuencia nominales, calcular:

- **a)** Velocidad.
- **b)** Corriente del estator.
- **c)** Factor de potencia.
- **d)** Potencia convertida y potencia de salida.
- **e)** Torque inducido y torque de carga.
- **f)** Eficiencia.

## Datos y consideración previa

| Magnitud | Símbolo | Valor |
| --- | --- | --- |
| Tensión de línea (nominal) | $V_L$ | $460\ \text{V}$ |
| Frecuencia | $f_e$ | $60\ \text{Hz}$ |
| Número de polos | $P$ | $4$ |
| Conexión | — | Y (estrella) |
| Resistencia del estator | $R_1$ | $0{,}641\ \Omega$ |
| Resistencia del rotor referida | $R_2$ | $0{,}332\ \Omega$ |
| Reactancia de dispersión del estator | $X_1$ | $1{,}106\ \Omega$ |
| Reactancia del rotor referida | $X_2$ | $0{,}464\ \Omega$ |
| Reactancia de magnetización | $X_M$ | $26{,}3\ \Omega$ |
| Pérdidas por rotación | $P_{rot}$ | $1100\ \text{W}$ |
| Deslizamiento | $s$ | $0{,}022$ |

> [!important] Tratamiento de las pérdidas en el núcleo
> Puesto que las **pérdidas en el núcleo están agrupadas** con las de fricción, rozamiento con el aire y misceláneas, se tratarán **como pérdidas mecánicas** y se restarán **de la potencia convertida** en el diagrama de flujo de potencia. Consecuencia práctica: en este problema **no aparece la rama $G_C$** en el circuito equivalente (solo $jX_M$), y la potencia en el entrehierro se obtiene restando **únicamente** $P_{PCE}$ a la potencia de entrada.

## a) Velocidad

La **velocidad síncrona** del campo giratorio (ver [[S16-1 Tema 01 - Principio de funcionamiento de las máquinas asíncronas trifásicas|principio de funcionamiento de las máquinas asíncronas]]) es:

$$n_{sinc} = \frac{120\,f_e}{P}$$

- $P$ = **número de polos** (no el número de pares de polos).

$$n_{sinc} = \frac{120\,(60)}{4} = 1800\ \text{rpm}$$

En velocidad angular:

$$\omega_{sinc} = n_{sinc}\left(\frac{2\pi}{60}\right) = 1800\left(\frac{2\pi}{60}\right) = 188{,}5\ \text{rad/s}$$

La **velocidad mecánica del eje del rotor** se obtiene a partir del deslizamiento:

$$n_m = (1 - s)\,n_{sinc}$$

- $s$ = deslizamiento; $n_m$ = velocidad mecánica del rotor.

$$n_m = (1 - 0{,}022)(1800) = 1760\ \text{rpm}$$

Y su equivalente angular:

$$\omega_m = (1 - s)\,\omega_{sinc} = (1 - 0{,}022)(188{,}5) = 184{,}4\ \text{rad/s}$$

$$\boxed{n_m = 1760\ \text{rpm} \qquad \omega_m = 184{,}4\ \text{rad/s}}$$

## b) Corriente del estator

Para encontrar la corriente del estator hay que obtener la **impedancia equivalente del circuito**. El procedimiento tiene dos pasos:

1. Combinar la **impedancia referida del rotor en paralelo con la rama de magnetización**.
2. **Añadir en serie** la impedancia del estator a esa combinación.

### Impedancia referida del rotor

$$Z_2 = \frac{R_2}{s} + jX_2$$

$$Z_2 = \frac{0{,}332}{0{,}022} + j\,0{,}464 = 15{,}09 + j\,0{,}464\ \Omega$$

$$Z_2 = 15{,}10\ \angle\ 1{,}76°\ \Omega$$

> [!note] Lectura del resultado
> $R_2/s = 15{,}09\ \Omega$ frente a $X_2 = 0{,}464\ \Omega$: con un deslizamiento tan pequeño, la rama del rotor es **casi puramente resistiva** ($1{,}76°$). Es el reflejo de que a baja carga la corriente del rotor está prácticamente en fase con $E_{R0}$.

### Impedancia del paralelo (rama de magnetización + rotor)

$$Z_f = \cfrac{1}{\cfrac{1}{jX_M} + \cfrac{1}{Z_2}}$$

$$Z_f = \cfrac{1}{-j\,0{,}038 + 0{,}0662\ \angle\ {-1{,}76°}}$$

$$\boxed{Z_f = 12{,}94\ \angle\ 31{,}1°\ \Omega}$$

### Impedancia total

$$Z_{tot} = Z_1 + Z_f = (R_1 + jX_1) + Z_f$$

$$Z_{tot} = 0{,}641 + j\,1{,}106 + 12{,}94\ \angle\ 31{,}1°$$

$$Z_{tot} = 14{,}07\ \angle\ 33{,}6°\ \Omega$$

### Tensión de fase y corriente

Al estar el motor **conectado en Y**, la tensión de fase es la de línea dividida entre $\sqrt{3}$:

$$V_\phi = \frac{V_L}{\sqrt{3}} = \frac{460}{\sqrt{3}} = 266\ \text{V}$$

$$I_1 = \frac{V_\phi}{Z_{tot}} = \frac{266\ \angle\ 0°}{14{,}07\ \angle\ 33{,}6°}$$

$$\boxed{I_1 = 18{,}88\ \angle\ {-33{,}6°}\ \text{A}}$$

## c) Factor de potencia

El factor de potencia es el coseno del ángulo de la corriente respecto de la tensión:

$$FP = \cos\theta = \cos(33{,}6°) = 0{,}833$$

$$\boxed{FP = 0{,}833\ \text{en retraso}}$$

Es **en retraso** porque la corriente está desfasada $-33{,}6°$ respecto de la tensión, consecuencia del carácter inductivo del motor.

## d) Potencia convertida y potencia de salida

### Potencia de entrada

$$P_{entr} = \sqrt{3}\,V_L\,I_L\,\cos\theta$$

$$P_{entr} = \sqrt{3}\,(460)(18{,}88)(0{,}833) = 12\,530\ \text{W}$$

### Pérdidas en el cobre del estator

$$P_{PCE} = 3\,I_1^2\,R_1$$

$$P_{PCE} = 3\,(18{,}88)^2\,(0{,}641) = 685\ \text{W}$$

### Potencia en el entrehierro

Como las pérdidas en el núcleo se agruparon con las mecánicas, aquí **solo** se resta $P_{PCE}$:

$$P_{EH} = P_{entr} - P_{PCE} = 12\,530 - 685 = 11\,845\ \text{W}$$

### Potencia convertida

$$P_{conv} = (1 - s)\,P_{EH} = (1 - 0{,}022)(11\,845) = 11\,584\ \text{W}$$

$$\boxed{P_{conv} = 11\,584\ \text{W}}$$

### Potencia de salida

$$P_{sal} = P_{conv} - P_{rot}$$

- $P_{rot}$ = pérdidas por rotación (incluye fricción, rozamiento con el aire, misceláneas **y núcleo**).

$$P_{sal} = 11\,584 - 1100 = 10\,484\ \text{W} \approx 10\,485\ \text{W}$$

Expresada en caballos de fuerza, con $1\ \text{hp} = 746\ \text{W}$:

$$P_{sal} = \frac{10\,485\ \text{W}}{746\ \text{W/hp}} = 14{,}1\ \text{hp}$$

$$\boxed{P_{sal} \approx 10\,485\ \text{W} = 14{,}1\ \text{hp}}$$

> [!note] Dato inconsistente
> En el video se enuncia la potencia de salida como "*la potencia convertida menos la potencia del rotor*"; lo correcto es **menos las pérdidas por rotación** $P_{rot}$ (que aquí engloban también las del núcleo). Las pérdidas en el cobre del rotor ya fueron descontadas al aplicar $P_{conv} = (1-s)P_{EH}$; restarlas otra vez sería un doble conteo. El cálculo del video es correcto ($11\,584 - 1100$), solo la denominación es imprecisa.

> [!note] Dato inconsistente
> El video arrastra $11\,585\ \text{W}$ para $P_{conv}$ en este paso, aunque un renglón antes había obtenido $11\,584\ \text{W}$. La diferencia de $1\ \text{W}$ es puro redondeo y no altera ningún resultado ($10\,484$ vs. $10\,485\ \text{W}$).

## e) Torque inducido y torque de carga

El **par inducido** se calcula con la potencia en el entrehierro y la velocidad **síncrona**:

$$\tau_{ind} = \frac{P_{EH}}{\omega_{sinc}}$$

$$\tau_{ind} = \frac{11\,845\ \text{W}}{188{,}5\ \text{rad/s}} = 62{,}8\ \text{N}\cdot\text{m}$$

$$\boxed{\tau_{ind} = 62{,}8\ \text{N}\cdot\text{m}}$$

El **par de carga** (o par en la salida) se calcula con la potencia de salida y la velocidad **mecánica** del rotor:

$$\tau_{carga} = \frac{P_{sal}}{\omega_m}$$

$$\tau_{carga} = \frac{10\,485\ \text{W}}{184{,}4\ \text{rad/s}} = 56{,}9\ \text{N}\cdot\text{m}$$

$$\boxed{\tau_{carga} = 56{,}9\ \text{N}\cdot\text{m}}$$

> [!tip] Por qué $\tau_{ind} > \tau_{carga}$
> El par inducido es el generado por la **conversión interna** de energía; el par de carga es el realmente **disponible en el eje**. La diferencia ($62{,}8 - 56{,}9 = 5{,}9\ \text{N}\cdot\text{m}$) es el par consumido por las pérdidas por rotación. Nótese además que **cada par se divide entre su velocidad correspondiente**: $\tau_{ind}$ entre $\omega_{sinc}$ (por la cancelación del factor $(1-s)$) y $\tau_{carga}$ entre $\omega_m$.

## f) Eficiencia

$$\eta = \frac{P_{sal}}{P_{entr}} \times 100\ \%$$

$$\eta = \frac{10\,485\ \text{W}}{12\,530\ \text{W}} \times 100\ \% = 83{,}7\ \%$$

$$\boxed{\eta = 83{,}7\ \%}$$

> [!success] Resultados
> | Inciso | Magnitud | Resultado |
> | --- | --- | --- |
> | a) | Velocidad síncrona / mecánica | $n_{sinc} = 1800\ \text{rpm}$; $n_m = 1760\ \text{rpm}$ ($\omega_m = 184{,}4\ \text{rad/s}$) |
> | b) | Corriente del estator | $I_1 = 18{,}88\ \angle\ {-33{,}6°}\ \text{A}$ |
> | c) | Factor de potencia | $FP = 0{,}833$ en retraso |
> | d) | Potencia convertida / de salida | $P_{conv} = 11\,584\ \text{W}$; $P_{sal} = 10\,485\ \text{W} = 14{,}1\ \text{hp}$ |
> | e) | Torque inducido / de carga | $\tau_{ind} = 62{,}8\ \text{N}\cdot\text{m}$; $\tau_{carga} = 56{,}9\ \text{N}\cdot\text{m}$ |
> | f) | Eficiencia | $\eta = 83{,}7\ \%$ |
>
> El ejercicio recorre la cadena completa: se resuelve el [[S16-2 Tema 02 - Circuito equivalente de un motor de inducción|circuito equivalente por fase]] para hallar $I_1$, y con ella se alimenta el [[S16-3 Tema 03 - Potencia y par en los motores de inducción|balance de potencia]] hasta llegar al par. La clave operativa es $\tau_{ind} = P_{EH}/\omega_{sinc}$, que evita tener que pasar por $P_{conv}$ y $\omega_m$.

> [!tip] Lectura del punto de operación
> El motor es de $25\ \text{hp}$ nominales pero entrega $14{,}1\ \text{hp}$: está operando **a poco más de la mitad de su carga nominal**, lo cual es consistente con el deslizamiento pequeño ($2{,}2\ \%$) y con un factor de potencia modesto ($0{,}833$) — a carga parcial, la corriente de magnetización pesa relativamente más y el $FP$ se degrada.

## Bibliografía

- Chapman, S. J. (2012). *Máquinas Eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
- Pretel Díaz, Ch. H. (2026). *Ejercicio de ecuación de torque* [Video – Guion]. UTP+class.
