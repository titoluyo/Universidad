---
title: "Ejercicio resuelto - Regulación de velocidad de motor de inducción"
curso: "[[Motores MOC]]"
unidad: 4
semana: 17
orden: 2
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/motor-asincrono
  - tema/equivalente-de-thevenin
  - tema/par-maximo
  - tema/rotor-devanado
date: 2026-07-13
---

> [!info] Material original
> Ejercicio en video del docente ([YouTube](https://www.youtube.com/watch?v=UGMOhCPKpf0)). Guion (transcripción): [S17-Guion-Ejercicio-curvas-caracteristicas.pdf](attachments/S17-Guion-Ejercicio-curvas-caracteristicas.pdf) (UTP, Semana 17).

> [!warning] El título del ítem en el portal está mal puesto
> El ítem del portal se titula *"…curvas características del motor **síncrono**"*, pero el guion del video se titula internamente **"Guion – Ejercicio de regulación de velocidad"** y resuelve un **motor de inducción con rotor devanado** (asíncrono). Esta nota sigue el contenido real del video y aplica la teoría de [[S17-1 Tema 01 - Curvas características del motor asíncrono y regulación de velocidad|curvas características y regulación de velocidad]].

## Enunciado

Un **motor de inducción con rotor devanado** de $460\ \text{V}$, $25\ \text{hp}$, $60\ \text{Hz}$, **cuatro polos**, conectado en **estrella (Y)**, tiene las siguientes impedancias en ohmios **por fase**, referidas al circuito del estator:

$$R_1 = 0{,}641\ \Omega \qquad R_2 = 0{,}332\ \Omega$$
$$X_1 = 1{,}106\ \Omega \qquad X_2 = 0{,}464\ \Omega \qquad X_M = 26{,}3\ \Omega$$

Se pide responder:

- **a)** ¿Cuál es el **par máximo** de este motor? ¿A qué **velocidad** y **deslizamiento** se presenta?
- **b)** ¿Cuál es el **par de arranque** del motor?
- **c)** Si se **duplica la resistencia del rotor**, ¿cuál es la velocidad a la que se presenta ahora el par máximo? ¿Y cuál es el nuevo par de arranque?

## Datos de partida

| Magnitud | Símbolo | Valor |
| --- | --- | --- |
| Tensión de línea | $V_L$ | $460\ \text{V}$ |
| Potencia nominal | $P_{nom}$ | $25\ \text{hp}$ |
| Frecuencia | $f_e$ | $60\ \text{Hz}$ |
| Número de polos | $P$ | $4$ |
| Conexión | — | Estrella (Y) |
| Resistencia del estator | $R_1$ | $0{,}641\ \Omega$ |
| Resistencia del rotor (referida) | $R_2$ | $0{,}332\ \Omega$ |
| Reactancia de dispersión del estator | $X_1$ | $1{,}106\ \Omega$ |
| Reactancia de dispersión del rotor (referida) | $X_2$ | $0{,}464\ \Omega$ |
| Reactancia de magnetización | $X_M$ | $26{,}3\ \Omega$ |

Al estar conectado en estrella, la **tensión de fase** es:

$$V_\phi = \frac{V_L}{\sqrt{3}} = \frac{460}{\sqrt{3}} = 265{,}6 \approx 266\ \text{V}$$

Y las velocidades de sincronismo:

$$n_{sinc} = \frac{120\,f_e}{P} = \frac{120 \times 60}{4} = 1800\ \text{rpm}$$

$$\omega_{sinc} = n_{sinc}\,\frac{2\pi}{60} = 1800 \times \frac{2\pi}{60} = 188{,}5\ \text{rad/s}$$

## Paso 1: Equivalente de Thevenin del circuito de entrada

### Voltaje de Thevenin

$$V_{TH} = V_\phi\,\frac{X_M}{\sqrt{R_1^{2} + (X_1 + X_M)^{2}}}$$

$$V_{TH} = 266 \times \frac{26{,}3}{\sqrt{(0{,}641)^{2} + (1{,}106 + 26{,}3)^{2}}} = 266 \times \frac{26{,}3}{\sqrt{0{,}411 + 751{,}09}}$$

$$V_{TH} = 266 \times \frac{26{,}3}{27{,}41} = 255{,}2\ \text{V}$$

### Resistencia de Thevenin

$$R_{TH} \approx R_1\left(\frac{X_M}{X_1 + X_M}\right)^{2} = 0{,}641\left(\frac{26{,}3}{1{,}106 + 26{,}3}\right)^{2} = 0{,}641\,(0{,}9596)^{2}$$

$$R_{TH} = 0{,}590\ \Omega$$

### Reactancia de Thevenin

$$X_{TH} \approx X_1 = 1{,}106\ \Omega$$

## Paso 2 — a) Par máximo, deslizamiento y velocidad

El **deslizamiento al cual ocurre el par máximo** es:

$$s_{máx} = \frac{R_2}{\sqrt{R_{TH}^{2} + (X_{TH} + X_2)^{2}}}$$

$$s_{máx} = \frac{0{,}332}{\sqrt{(0{,}590)^{2} + (1{,}106 + 0{,}464)^{2}}} = \frac{0{,}332}{\sqrt{0{,}348 + 2{,}465}} = \frac{0{,}332}{1{,}677}$$

$$\boxed{s_{máx} = 0{,}198}$$

La **velocidad mecánica** correspondiente:

$$n_m = (1 - s_{máx})\,n_{sinc} = (1 - 0{,}198)(1800) = 1443{,}6$$

$$\boxed{n_m \approx 1444\ \text{rpm}}$$

El **par a esta velocidad** es el par máximo:

$$\tau_{máx} = \frac{3\,V_{TH}^{2}}{2\,\omega_{sinc}\left[R_{TH} + \sqrt{R_{TH}^{2} + (X_{TH} + X_2)^{2}}\right]}$$

$$\tau_{máx} = \frac{3\,(255{,}2)^{2}}{2\,(188{,}5)\left[0{,}590 + 1{,}677\right]} = \frac{195\,381}{(377)(2{,}267)} = \frac{195\,381}{854{,}7}$$

$$\boxed{\tau_{máx} \approx 229\ \text{N}\cdot\text{m}}$$

## Paso 3 — b) Par de arranque

El par de arranque se encuentra estableciendo el **deslizamiento $s = 1$** en la ecuación general del par:

$$\tau_{arr} = \frac{3\,V_{TH}^{2}\,\dfrac{R_2}{s}}{\omega_{sinc}\left[\left(R_{TH} + \dfrac{R_2}{s}\right)^{2} + (X_{TH} + X_2)^{2}\right]}$$

Con $s = 1$, $R_2/s = 0{,}332\ \Omega$:

$$\tau_{arr} = \frac{3\,(255{,}2)^{2}\,(0{,}332)}{188{,}5\left[(0{,}590 + 0{,}332)^{2} + (1{,}106 + 0{,}464)^{2}\right]}$$

$$\tau_{arr} = \frac{64\,866{,}5}{188{,}5\left[0{,}850 + 2{,}465\right]} = \frac{64\,866{,}5}{(188{,}5)(3{,}315)} = \frac{64\,866{,}5}{624{,}9}$$

$$\boxed{\tau_{arr} \approx 104\ \text{N}\cdot\text{m}}$$

## Paso 4 — c) Resistencia del rotor duplicada

Si se **duplica la resistencia del rotor**, $R_2' = 2\,(0{,}332) = 0{,}664\ \Omega$.

### Nuevo deslizamiento y velocidad del par máximo

Como $s_{máx}$ es **directamente proporcional a $R_2$** (véase la fórmula del Paso 2, donde $R_2$ aparece solo en el numerador), el deslizamiento también se duplica:

$$s_{máx}' = 2\,(0{,}198) = 0{,}396$$

$$n_m' = (1 - s_{máx}')\,n_{sinc} = (1 - 0{,}396)(1800) = 1087{,}2$$

$$\boxed{n_m' \approx 1087\ \text{rpm}}$$

### Par máximo (sin cambios)

La expresión de $\tau_{máx}$ **no contiene $R_2$**, por lo que el par máximo permanece igual:

$$\boxed{\tau_{máx}' = 229\ \text{N}\cdot\text{m}}$$

### Nuevo par de arranque

Nuevamente con $s = 1$, ahora $R_2'/s = 0{,}664\ \Omega$:

$$\tau_{arr}' = \frac{3\,(255{,}2)^{2}\,(0{,}664)}{188{,}5\left[(0{,}590 + 0{,}664)^{2} + (1{,}106 + 0{,}464)^{2}\right]}$$

$$\tau_{arr}' = \frac{129\,733}{188{,}5\left[1{,}573 + 2{,}465\right]} = \frac{129\,733}{(188{,}5)(4{,}037)} = \frac{129\,733}{761{,}1}$$

$$\boxed{\tau_{arr}' \approx 170\ \text{N}\cdot\text{m}}$$

> [!note] Sobre el redondeo de $V_\phi$
> El video calcula $V_{TH} = 255{,}2\ \text{V}$ usando $V_\phi \approx 266\ \text{V}$. Partiendo del valor exacto $V_\phi = 460/\sqrt{3} = 265{,}58\ \text{V}$ se obtiene $V_{TH} = 254{,}79\ \text{V}$ y, en consecuencia, $\tau_{máx} = 227{,}8\ \text{N}\cdot\text{m}$, $\tau_{arr} = 103{,}5\ \text{N}\cdot\text{m}$ y $\tau_{arr}' = 169{,}9\ \text{N}\cdot\text{m}$. La diferencia (< 0,6 %) es solo de redondeo; se conservan los valores del video, que coinciden con los del texto de Chapman.

> [!success] Resultados
> | Pregunta | Resultado |
> | --- | --- |
> | Equivalente de Thevenin | $V_{TH} = 255{,}2\ \text{V}$, $R_{TH} = 0{,}590\ \Omega$, $X_{TH} = 1{,}106\ \Omega$ |
> | a) Par máximo | $\tau_{máx} = 229\ \text{N}\cdot\text{m}$ en $s_{máx} = 0{,}198$, $n_m = 1444\ \text{rpm}$ |
> | b) Par de arranque | $\tau_{arr} = 104\ \text{N}\cdot\text{m}$ |
> | c) Con $R_2$ duplicada | $s_{máx}' = 0{,}396$, $n_m' = 1087\ \text{rpm}$, $\tau_{máx}' = 229\ \text{N}\cdot\text{m}$, $\tau_{arr}' = 170\ \text{N}\cdot\text{m}$ |
>
> El ejercicio confirma la propiedad clave del **rotor devanado**: al duplicar $R_2$, el par máximo **no cambia** pero se desplaza a menor velocidad, y el **par de arranque crece** de $104$ a $170\ \text{N}\cdot\text{m}$ (+63 %). Esa es justamente la razón de insertar resistencia rotórica durante el arranque.

## Bibliografía

- Chapman, S. J. (2012). *Máquinas eléctricas* (5.ª ed.). McGraw-Hill Interamericana.
- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
- Pretel Díaz, Ch. H. (2026). *Desarrollo de un ejercicio de curvas características del motor síncrono* [Video – Guion]. UTP+class.
