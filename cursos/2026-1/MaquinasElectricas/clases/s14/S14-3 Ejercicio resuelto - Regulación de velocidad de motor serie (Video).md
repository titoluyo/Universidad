---
title: "Ejercicio resuelto - Regulación de velocidad de un motor serie con saturación"
curso: "[[Motores MOC]]"
unidad: 3
semana: 14
orden: 3
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/motor-serie
  - tema/regulacion-de-velocidad
  - tema/curva-de-magnetizacion
date: 2026-06-22
---

> [!note] Fuente
> Desarrollado a partir del **video** "Semana 14 – Desarrollo de un ejercicio de regulación" (Guion del docente). Transcripción y figuras tomadas del video.

## Enunciado

La **figura 1** muestra un **motor de c.d. en serie de 250 V** con devanados de compensación y una resistencia total en serie $R_A + R_S = 0{,}08\ \Omega$. El campo en serie consta de **25 vueltas por polo** y tiene la **curva de magnetización** de la **figura 2** (levantada a $n_0 = 1200\ \text{rpm}$).

**Se pide:** hallar la **velocidad** $n$ y el **par inducido** $T$ del motor cuando la corriente del inducido es $I_i = 50\ \text{A}$.

![[Ej - Figura 1. Circuito equivalente motor serie DC.png]]
> **Figura 1.** Circuito equivalente de un motor de c.d. en serie. $\;I_A = I_S = I_L\;$ y $\;V_T = E_A + I_A(R_A + R_S)$.

![[Ej - Figura 2. Curva de magnetizacion a 1200 rpm.png]]
> **Figura 2.** Curva de magnetización del ejercicio, levantada a $n_m = 1200\ \text{rpm}$ (voltaje interno generado $E_A$ vs. fuerza magnetomotriz $\mathcal{F}$ en A·vueltas).

## Datos y equivalencias

En el motor serie, todas las corrientes coinciden:

$$I_A = I_S = I_L = I_i = 50\ \text{A}$$

| Símbolo | Valor | Descripción |
| --- | --- | --- |
| $V$ ($=V_T$) | 250 V | Tensión en bornes |
| $R_i$ ($=R_A+R_S$) | 0,08 Ω | Resistencia total del inducido + serie |
| $N$ | 25 vueltas/polo | Espiras del campo serie |
| $n_0$ | 1200 rpm | Velocidad de la curva de magnetización |
| $I_i$ | 50 A | Corriente del inducido |

> [!info] Estrategia
> El motor serie trabaja **con saturación**, por lo que no vale suponer $\phi$ lineal: hay que **leer la f.e.m. en la curva de magnetización**. La curva está dada a 1200 rpm, así que la f.e.m. que se obtenga de ella es un valor de referencia $E_0$ a esa velocidad; la velocidad real se halla por **proporcionalidad** $E/E_0 = n/n_0$.

## Desarrollo

### 1) Fuerza contraelectromotriz a 50 A

De la ecuación del inducido $V = E + R_i I_i$:

$$E = V - R_i\,I_i = 250 - (50)(0{,}08) = \mathbf{246\ V}$$

### 2) Fuerza magnetomotriz y lectura en la curva

Con $I_i = 50\ \text{A}$ y $N = 25$ vueltas, la **fuerza magnetomotriz** del campo serie es:

$$\mathcal{F} = N\,I_i = (25)(50) = \mathbf{1250\ \text{A·vueltas}}$$

Entrando en la **curva de magnetización** (figura 2) con $\mathcal{F} = 1250\ \text{A·vueltas}$ se lee una f.e.m. de referencia (a 1200 rpm):

$$E_0 \approx 80\ \text{V}$$

### 3) Velocidad del motor

Como la f.e.m. es proporcional a la velocidad ($E = K_E\,n\,\phi$, con $\phi$ fijado por $\mathcal{F}$), se aplica:

$$\frac{E}{E_0} = \frac{n}{n_0} \quad\Longrightarrow\quad n = \frac{E}{E_0}\,n_0 = \frac{246}{80}\,(1200)$$

$$\boxed{n \approx 3690\ \text{rpm}}$$

### 4) Par inducido

El par desarrollado se obtiene de la potencia electromagnética $P = E\,I_i = T\,\omega$, con $\omega = \dfrac{2\pi n}{60}$:

$$T = \frac{E\,I_i}{\omega} = \frac{E\,I_i}{\dfrac{2\pi n}{60}} = \frac{(246)(50)}{\dfrac{2\pi (3690)}{60}} = \frac{12\,300}{386{,}4}$$

$$\boxed{T \approx 31{,}8\ \text{N·m}}$$

## Resumen

| Magnitud | Resultado |
| --- | --- |
| f.c.e.m. $E$ | 246 V |
| FMM $\mathcal{F}$ | 1250 A·vueltas |
| f.e.m. de referencia $E_0$ (a 1200 rpm) | ≈ 80 V |
| Velocidad $n$ | ≈ 3690 rpm |
| Par inducido $T$ | ≈ 31,8 N·m |

> [!success] Interpretación
> Con la carga dada ($I_i = 50\ \text{A}$) el motor gira muy por encima de la velocidad base (3690 vs. 1200 rpm): es el comportamiento típico del **motor serie**, cuya velocidad **se dispara a baja carga** porque $\phi$ disminuye con $I_i$. El procedimiento clave es **leer la f.e.m. en la curva de magnetización** (zona saturada) en vez de suponer flujo lineal. Sustenta la [[S14-2 Tema 02 - Regulación de velocidad de un motor de corriente continua|regulación de velocidad del motor serie]].

## Bibliografía

- Chapman, S. J. (2012). *Máquinas eléctricas* (5.ª ed.). McGraw-Hill.
- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6.ª ed.). McGraw-Hill Interamericana.
