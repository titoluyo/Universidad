---
title: "Construcción del diagrama de Bode por factores"
curso: "[[Amplificadores MOC]]"
unidad: 3
semana: 14
orden: 5
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/diagrama-de-bode
  - tema/funcion-de-transferencia
  - tema/respuesta-en-frecuencia
  - tema/primer-orden
  - tema/segundo-orden
date: 2026-06-22
---

## Contexto

El [[S14-4 Tema 14 - Filtros de primer orden y diagrama de Bode|diagrama de Bode]] de una función de transferencia complicada **no se calcula de golpe**: se **descompone** $H(jw)$ en **factores elementales** y se **suman** sus aportes. Esto funciona porque, en escala logarítmica, el logaritmo de un producto es la **suma** de los logaritmos:

$$20\log\big|H_1\cdot H_2\cdots\big| = 20\log|H_1| + 20\log|H_2| + \cdots \qquad \angle(H_1H_2\cdots)=\angle H_1+\angle H_2+\cdots$$

Por eso basta conocer el Bode de **unos pocos factores tipo** y graficarlos sumando asíntotas. Esta nota recoge ese "diccionario de factores" tal como aparece en el material del curso.

> [!quote] Material complementario — diapositivas "Filtros Activos" (Diagrama de Bode)
> Factor **derivada** $(jw/w_0)$ y factor **integral** $(jw/w_0)^{-1}$; factores de **1.er orden** $(1+jw/w_0)^{\pm1}$ y factores de **2.º orden** $\big(1+2a\,jw/w_0+(jw/w_0)^2\big)^{\pm1}$.

> [!info] Toma de notas en clase
> Semana 14. **Construcción del diagrama de Bode por factores:** los bloques elementales (constante, derivada, integral, 1.er y 2.º orden), su pendiente en dB/década y su fase, y cómo se suman para armar el Bode completo de cualquier filtro.

---

## 1. La idea: sumar asíntotas

Cualquier $H(jw)$ de un filtro se escribe como **producto** de factores básicos. Sobre el Bode:

- **Magnitud (dB):** se **suman** las rectas asintóticas de cada factor.
- **Fase:** se **suman** las fases de cada factor.

Así, dibujar el Bode = identificar los factores → dibujar el aporte de cada uno → sumarlos.

## 2. Factor derivada $(jw/w_0)$ y factor integral $(jw/w_0)^{-1}$

Son los bloques de un **cero** y un **polo en el origen**.

### 2.1 Factor derivada $(jw/w_0)$ — un cero en el origen

$$G_{\text{dB}} = 20\log\left|\,j\dfrac{w}{w_0}\,\right| \qquad \varphi(w)=\arctan\!\big[(jw)\big]=+\dfrac{\pi}{2}$$

- **Magnitud:** recta de **$+20\ \text{dB/década}$** que cruza $0\ \text{dB}$ en $w=w_0$.
- **Fase:** constante en **$+90^\circ$** ($+\pi/2$).

### 2.2 Factor integral $(jw/w_0)^{-1}$ — un polo en el origen

$$G_{\text{dB}} = 20\log\left|\dfrac{1}{\,j\frac{w}{w_0}\,}\right| = -20\log\left|\,j\dfrac{w}{w_0}\,\right| \qquad \varphi(w)=-\arctan\!\big[(jw)\big]=-\dfrac{\pi}{2}$$

- **Magnitud:** recta de **$-20\ \text{dB/década}$** que cruza $0\ \text{dB}$ en $w=w_0$.
- **Fase:** constante en **$-90^\circ$** ($-\pi/2$).

> [!note] Son espejo uno del otro
> El factor integral es el inverso del derivada: misma recta pero con pendiente **opuesta** y fase opuesta. Por eso integrar "atrasa" $90^\circ$ y derivar "adelanta" $90^\circ$.

## 3. Factores de 1.er orden $(1+jw/w_0)^{\pm1}$

A diferencia de los anteriores, tienen un **codo** (cambio de pendiente) en $w_0$.

### 3.1 $(1+jw/w_0)$ — cero de 1.er orden

- $w \ll w_0$: asíntota **horizontal en $0\ \text{dB}$**.
- $w \gg w_0$: asíntota de **$+20\ \text{dB/década}$**.
- Fase: de $0^\circ$ a $+90^\circ$ (pasa por $+45^\circ$ en $w_0$).

### 3.2 $(1+jw/w_0)^{-1}$ — polo de 1.er orden (¡el pasabajo!)

- $w \ll w_0$: asíntota **horizontal en $0\ \text{dB}$**.
- $w \gg w_0$: asíntota de **$-20\ \text{dB/década}$**.
- Fase: de $0^\circ$ a $-90^\circ$ (pasa por $-45^\circ$ en $w_0$).

Este es exactamente el pasabajo de [[S14-4 Tema 14 - Filtros de primer orden y diagrama de Bode|S14-4]]: $F(jw)=\dfrac{K}{1+jw/w_0}$ = factor constante $K$ **+** factor $(1+jw/w_0)^{-1}$.

## 4. Factores de 2.º orden $\big(1+2a\,jw/w_0+(jw/w_0)^2\big)^{\pm1}$

Cambian de pendiente al **doble**: $\pm 40\ \text{dB/década}$ tras $w_0$.

$$D(jw) = 1 + 2a\,\dfrac{jw}{w_0} + \left(\dfrac{jw}{w_0}\right)^2$$

- $\big(1+2a\,jw/w_0+(jw/w_0)^2\big)$: 0 dB hasta $w_0$, luego **$+40\ \text{dB/década}$**; fase $0^\circ\to+180^\circ$.
- Su inverso $(\cdots)^{-1}$ (el **pasabajo de 2.º orden**): 0 dB hasta $w_0$, luego **$-40\ \text{dB/década}$**; fase $0^\circ\to-180^\circ$.

> [!note] El coeficiente $a$ es el amortiguamiento
> Comparando con la forma canónica de [[S14-3 Tema 14 - Funcion de transferencia de filtros - polos y ceros|S14-3]] $\;s^2+\frac{w_0}{Q}s+w_0^2$ (normalizada): $\;2a = \dfrac{1}{Q}\;\Rightarrow\; a=\dfrac{1}{2Q}=\zeta$ (factor de amortiguamiento). Si $a$ es pequeño ($Q$ alto), la curva **real** se separa de la asíntota con un **pico de resonancia** en $w_0$ (ver la gráfica de $Q$ en [[S14-3 Tema 14 - Funcion de transferencia de filtros - polos y ceros|S14-3]]); la asíntota de $\pm40\ \text{dB/déc}$ no cambia.

## 5. Tabla resumen de factores

| Factor | Pendiente (tras $w_0$) | Fase | Qué es |
|--------|------------------------|------|--------|
| $K$ (constante) | $0$ (recta en $20\log K$) | $0^\circ$ | ganancia |
| $(jw/w_0)$ | $+20\ \text{dB/déc}$ | $+90^\circ$ | cero en el origen (derivada) |
| $(jw/w_0)^{-1}$ | $-20\ \text{dB/déc}$ | $-90^\circ$ | polo en el origen (integral) |
| $(1+jw/w_0)$ | $0 \to +20\ \text{dB/déc}$ | $0^\circ\to+90^\circ$ | cero de 1.er orden |
| $(1+jw/w_0)^{-1}$ | $0 \to -20\ \text{dB/déc}$ | $0^\circ\to-90^\circ$ | polo de 1.er orden (pasabajo) |
| $(1+2a\,jw/w_0+(jw/w_0)^2)$ | $0 \to +40\ \text{dB/déc}$ | $0^\circ\to+180^\circ$ | par de ceros |
| $(\cdots)^{-1}$ | $0 \to -40\ \text{dB/déc}$ | $0^\circ\to-180^\circ$ | par de polos (pasabajo 2.º orden) |

> [!tip] Receta para armar un Bode
> 1. Escribir $H(jw)$ como producto de factores de esta tabla.
> 2. Dibujar la asíntota de cada factor (todas parten de su contribución y cambian de pendiente en su $w_0$).
> 3. **Sumar** las pendientes tramo a tramo (y las fases).
> 4. Corregir en los codos: $-3\ \text{dB}$ por cada factor de 1.er orden en su $w_0$; pico/valle según $a$ en los de 2.º orden.

## 6. Gráfica

Asíntotas de magnitud de los factores elementales (todos con $w_0=1\ \text{kHz}$): los de pendiente constante (derivada $+20$, integral $-20$) y los de codo (1.er orden $\pm20$, 2.º orden $\pm40$).

![[bode_factores.png]]

Script: [`plot_bode_factores.py`](plot_bode_factores.py) — ejecutar con `uv run --with matplotlib --with numpy python plot_bode_factores.py`.

---

## Bibliografía

- Material del curso — diapositivas "Filtros Activos" (Diagrama de Bode: factores de 1.er y 2.º orden).
- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*. Pearson — diagramas de Bode.
- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press — respuesta en frecuencia por factores.
- Ogata, K. *Ingeniería de Control Moderna*. Pearson — construcción de diagramas de Bode por factores asintóticos.
