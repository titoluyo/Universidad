---
title: "Tema 02 - Función de energía y coenergía"
curso: "[[Motores MOC]]"
unidad: 3
semana: 10
orden: 2
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/energia-magnetica
  - tema/coenergia-magnetica
  - tema/conversion-electromecanica
  - tema/curva-magnetizacion
date: 2026-05-25
---

![[s10-t2-banner.png]]

## Idea central

Las **máquinas eléctricas retienen parte de la energía eléctrica suministrada en forma de campos electromagnéticos**. Al graficar el **flujo magnético** en la bobina frente a la **corriente** en una máquina eléctrica (por ejemplo un **electroimán**), podemos observar una **curva característica** $\lambda$ vs $i$ (no lineal cuando el hierro se satura).

Si mantenemos una **distancia constante $x$** entre el electroimán y su objetivo —por ejemplo una pieza de hierro, según se muestra en la **Figura 1**— el sistema almacena energía magnética que se relaciona con el área bajo (o sobre) esta curva.

![[s10-t2-fig1-conversion-energia.png]]
*Figura 1. Conversión de energía eléctrica. Electroimán con bobina alimentada por $v_1, i_1$ y enlace de flujo $\lambda_1$. La fuerza electromecánica $F_e$ actúa sobre la pieza de hierro a distancia $x$ del núcleo en forma de "C".*

## Energía y coenergía en el campo

![[s10-t2-fig2-energia-coenergia.png]]
*Figura 2. Energía y coenergía en el campo, representadas sobre la curva de magnetización $\Phi$ vs $\mathcal{F}$.*

La gráfica de la **Figura 2** muestra el área correspondiente a la **energía** y a la **coenergía** en el campo:

- La **energía** $W_c$ es el **área en la parte superior** de la curva (entre la curva y el eje $\lambda$).
- La **coenergía** $W'_c$ es el **área de la parte inferior** de la curva (entre la curva y el eje de corriente $i$ o fuerza magnetomotriz $\mathcal{F}$).

> [!important] Distinción clave
> - **Energía $W_c$:** tiene **sentido físico** real — representa la energía magnética efectivamente almacenada en el campo.
> - **Coenergía $W'_c$:** es una **construcción matemática auxiliar** (sin sentido físico directo), pero **fundamental para calcular fuerzas y pares electromagnéticos** sin tener que invertir explícitamente la relación $\lambda(i,x)$.

## Definiciones formales

La **energía almacenada en el campo** se representa con la siguiente ecuación:

$$W_c = \int_{\lambda(0)}^{\lambda(t)} i(\lambda, x)\, d\lambda$$

La **coenergía** (sin sentido físico) se define mediante la siguiente ecuación:

$$W'_c = \int_{i(0)}^{i(t)} \lambda(i, x)\, di$$

Donde:
- $W_c$ = energía magnética almacenada en el campo
- $W'_c$ = coenergía magnética (función auxiliar)
- $\lambda$ = enlace de flujo magnético (Wb·vuelta)
- $i$ = corriente que circula por la bobina (A)
- $x$ = distancia / variable de posición mecánica (m)

> [!note] Lectura geométrica
> Como las dos áreas son complementarias bajo la curva $\lambda$–$i$, se cumple:
>
> $$W_c + W'_c = \lambda \cdot i$$
>
> Esto se observa directamente en la Figura 3: las áreas $W_c$ (sombreada, sobre la curva) y $W'_c$ (debajo de la curva) llenan juntas el rectángulo $\lambda_1 \times i_1$.

![[s10-t2-fig3-energia-coenergia.png]]
*Figura 3. Energía $W_c$ (área sombreada, sobre la curva) y coenergía $W'_c$ (área bajo la curva) en el plano $\lambda$ vs $i$, para una posición $x$ fija. El punto de operación es $(i_1, \lambda_1)$.*

## Caso lineal vs no lineal

> [!success] Caso lineal (sin saturación)
> Si el material es **lineal** (sin saturación), $\lambda = L(x)\cdot i$ y la curva $\lambda$–$i$ es una **recta**. En ese caso las dos áreas son **iguales**:
>
> $$W_c = W'_c = \tfrac{1}{2}\,L(x)\,i^2 = \tfrac{1}{2}\,\frac{\lambda^2}{L(x)}$$

> [!warning] Caso no lineal (con saturación)
> Cuando el hierro **se satura** (curva cóncava hacia el eje $i$), la coenergía $W'_c$ es **mayor** que la energía $W_c$. El cálculo de fuerza/par exige integrar a lo largo de la curva real de magnetización o usar la **derivada de la coenergía respecto a $x$ a corriente constante**:
>
> $$F_e = \left.\frac{\partial W'_c(i, x)}{\partial x}\right|_{i\text{ cte}}$$
>
> (Análogamente, $F_e = -\,\partial W_c(\lambda, x)/\partial x|_{\lambda\text{ cte}}$.)

## Conexión con la semana

- En el [[S10-1 Tema 01 - Conversión de energía electromecánica|Tema 01]] vimos el principio físico (fuerza de Lorentz). La función energía/coenergía es el **aparato matemático** que cuantifica ese principio en sistemas con campo magnético almacenado.
- En el [[S10-3 Ejercicio resuelto - Función de energía y coenergía (Video)|ejercicio resuelto]] aplicaremos estas integrales a un caso concreto.

## Bibliografía

- Ramos, G. (2019). *Energía y coenergía magnética* [Archivo PDF]. Recuperado de [https://es.scribd.com/document/433164934/Energia-y-Coenergia-Magnetica](https://es.scribd.com/document/433164934/Energia-y-Coenergia-Magnetica)
- Pretel Díaz, Ch. H. (2026). *Función de energía y coenergía* [Material de estudio – Contenido personalizado]. UTP+class.
