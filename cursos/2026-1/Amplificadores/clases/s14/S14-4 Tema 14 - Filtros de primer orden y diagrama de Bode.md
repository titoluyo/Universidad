---
title: "Filtros de primer orden (pasivos y activos) y diagrama de Bode"
curso: "[[Amplificadores MOC]]"
unidad: 3
semana: 14
orden: 4
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/filtros-activos
  - tema/filtros-pasivos
  - tema/primer-orden
  - tema/diagrama-de-bode
  - tema/frecuencia-de-corte
  - tema/funcion-de-transferencia
date: 2026-06-22
---

## Contexto

El **filtro de primer orden** es el caso más simple: **un solo elemento reactivo** ($C$) y, por tanto, **un solo polo**. Su [[S14-3 Tema 14 - Funcion de transferencia de filtros - polos y ceros|función de transferencia]] tiene grado 1 en el denominador, una caída de $-20\ \text{dB/década}$ y un corte en $f_c=\frac{1}{2\pi RC}$.

Esta nota compara la versión **pasiva** ($RC$ solo) con la **activa** (con op-amp), y presenta la herramienta para representarlas: el **diagrama de Bode**, que es justo lo que pedía el pizarrón de la [[S14-1 Tema 14 - Funcion de transferencia|función de transferencia]] (entra $f$, sale la ganancia $G$ en dB y la fase).

> [!info] Toma de notas en clase
> Semana 14. **Filtros de primer orden:** pasivos ($RC$) vs. activos (con amplificador operacional), su función de transferencia y frecuencia de corte, y cómo se dibuja el **diagrama de Bode** (asíntotas de magnitud y de fase, regla de la década).

---

## 0. Forma general (notación del profesor)

> [!quote] Material complementario — diapositivas "Filtros Activos"
> Son aquellos filtros en donde el **denominador** de la FDT (función de transferencia) es un polinomio de **1.er orden** de la forma general $\left(1 + j\dfrac{w}{w_0}\right)$.

$$\boxed{\,F(jw) = \dfrac{N(jw)}{1 + j\dfrac{w}{w_0}}\,}$$

- $w_0 = 2\pi f_c$ = **pulsación de corte** (rad/s).
- $\tau = \dfrac{1}{w_0}$ = **constante de tiempo**.
- $K$ = **ganancia**.

**Según el numerador** se obtiene un tipo distinto de filtro (mismo denominador):

| Numerador | Tipo |
|-----------|------|
| $K$ | **Pasobajo** |
| $K\left(j\dfrac{w}{w_0}\right)$ | **Pasoalto** |

Forma del **pasabajo** (slide):

$$F(jw) = \dfrac{K}{1 + j\dfrac{w}{w_0}}$$

> [!note] Equivalencia con la notación de estas notas
> Es la misma $H(s)$ de [[S14-3 Tema 14 - Funcion de transferencia de filtros - polos y ceros|S14-3 §4.1]] con $s=jw$ y $w_0=2\pi f_c$. El criterio "según el numerador" es exactamente el de la tabla de ceros: numerador constante → pasa bajo; numerador con un $jw$ (un cero en el origen) → pasa alto.

## 1. Filtros pasivos de primer orden ($RC$)

Solo $R$ y $C$. **No tienen ganancia** ($|H|\le 1$): a lo sumo dejan pasar la señal, nunca la amplifican.

### 1.1 Pasa bajo $RC$

```
 Vin ──[ R ]──┬──► Vout
              │
            [ C ]
              │
             GND
```

$$H(s)=\dfrac{1/sC}{R+1/sC}=\dfrac{1}{1+sRC}\qquad |H(f)|=\dfrac{1}{\sqrt{1+(f/f_c)^2}}$$

### 1.2 Pasa alto $RC$ (se intercambian $R$ y $C$)

```
 Vin ──[ C ]──┬──► Vout
              │
            [ R ]
              │
             GND
```

$$H(s)=\dfrac{R}{R+1/sC}=\dfrac{sRC}{1+sRC}$$

En ambos:

$$\boxed{\,f_c=\dfrac{1}{2\pi RC}\,}$$

> [!warning] Limitación de los pasivos
> La salida depende de la **carga** conectada (la carga "ve" la impedancia del filtro y desplaza $f_c$). Y al **encadenar** dos etapas $RC$, la segunda carga a la primera y la respuesta se deforma. Eso es justo lo que resuelve la versión activa.

## 2. Filtros activos de primer orden (op-amp)

Se agrega un **amplificador operacional**. Ventajas frente al pasivo (ya vistas en [[S14-2 Tema 14 - Filtros activos - introduccion y clasificacion|S14-2]]): **ganancia** $>1$, **alta $Z_{in}$ / baja $Z_{out}$** (aísla la carga) y **encadenado** sin interacción. La frecuencia de corte la fija el par $RC$ del lazo.

### 2.1 Pasa bajo activo (inversor)

$R_1$ a la entrada; en el lazo, $R_f$ **en paralelo** con $C_f$:

```
            ┌──[ Rf ]──┐
            │          │
            ├──[ Cf ]──┤
            │          │
 Vin ─[ R1 ]┴──┤−\     │
               │  >────┴──► Vout
        GND ───┤+/
```

$$\boxed{\,H(s)=-\dfrac{R_f}{R_1}\cdot\dfrac{1}{1+sR_fC_f}\,}$$

- Ganancia en banda de paso: $A_0=-\dfrac{R_f}{R_1}$.
- Frecuencia de corte: $f_c=\dfrac{1}{2\pi R_f C_f}$.

> [!note] Lectura
> A baja frecuencia $C_f$ es un circuito abierto → amplificador inversor de ganancia $-R_f/R_1$. A alta frecuencia $C_f$ cortocircuita a $R_f$ → la ganancia cae ($-20\ \text{dB/déc}$). Es un inversor con "techo" en $f_c$.

### 2.2 Pasa alto activo (inversor)

A la entrada, $R_1$ **en serie** con $C_1$; en el lazo, $R_f$:

```
              ┌──[ Rf ]──┐
              │          │
 Vin─[C1]─[R1]┴──┤−\     │
                 │  >────┴──► Vout
          GND ───┤+/
```

$$H(s)=-\dfrac{R_f}{R_1}\cdot\dfrac{sR_1C_1}{1+sR_1C_1}\qquad f_c=\dfrac{1}{2\pi R_1C_1}$$

## 3. Diagrama de Bode

Es la forma estándar de representar la [[S14-1 Tema 14 - Funcion de transferencia|función de transferencia]]: dos gráficas frente a la frecuencia en **escala logarítmica**.

- **Magnitud:** $G_{\text{dB}}=20\log_{10}|H(f)|$ en el eje $y$, $\log f$ en el eje $x$.
- **Fase:** $\phi(f)=\angle H(f)$ en grados.

### 3.1 Asíntotas de magnitud (pasa bajo de 1.er orden)

El Bode se dibuja con **rectas asintóticas** que se cortan en $f_c$:

| Región | Magnitud | Asíntota |
|--------|----------|----------|
| $f \ll f_c$ | $\approx A_0$ | recta **horizontal** en $20\log A_0$ |
| $f = f_c$ | $A_0 - 3\ \text{dB}$ | el codo (error máx. $3\ \text{dB}$) |
| $f \gg f_c$ | cae | recta de **$-20\ \text{dB/década}$** |

> [!tip] Regla de la década
> Cada vez que la frecuencia se multiplica por **10** (una década), la magnitud baja **20 dB** en un filtro de 1.er orden. Equivale a $-6\ \text{dB/octava}$ (al duplicar $f$).

### 3.2 Asíntotas de fase

| Frecuencia | Fase (pasa bajo) |
|-----------|------------------|
| $f \le f_c/10$ | $0^\circ$ |
| $f = f_c$ | $-45^\circ$ |
| $f \ge 10f_c$ | $-90^\circ$ |

La transición de fase ocurre en **dos décadas** (de $f_c/10$ a $10f_c$), con pendiente $\approx-45^\circ$/década. (En el pasa alto la fase va de $+90^\circ$ a $0^\circ$, pasando por $+45^\circ$ en $f_c$.)

> [!note] Por qué un solo polo da $-90^\circ$ como máximo
> Cada **polo** aporta hasta $-90^\circ$ de fase y $-20\ \text{dB/déc}$ de caída; cada **cero**, lo contrario. Un filtro de orden $n$ acumula hasta $n\times(-90^\circ)$ y $n\times(-20\ \text{dB/déc})$ — la base para leer estabilidad (márgenes de fase) en la semana 15.

### 3.3 Décadas y octavas

El eje de frecuencias del Bode es **logarítmico**, así que las distancias se miden en **décadas** y **octavas**, no en hertz.

> [!quote] Material complementario — diapositivas "Filtros Activos" (Décadas y Octavas)
> - Dos frecuencias están separadas una **DÉCADA** cuando una es **10 veces** la otra. En el eje: $1, 10, 100, 1000$.
> - Dos frecuencias están separadas una **OCTAVA** cuando una es el **doble** de la otra. En el eje: $1, 2, 4, 8$.

Cuántas décadas ($n$) u octavas ($x$) separan a $f_1$ y $f_2$:

$$\boxed{\,n = \log_{10}\dfrac{f_2}{f_1}\,}\qquad\qquad \boxed{\,x = \log_{2}\dfrac{f_2}{f_1}\,}$$

### 3.3.1 Conversión entre décadas y octavas

Igualando la razón de frecuencias expresada en ambas bases:

$$\dfrac{f_2}{f_1} = 10^{\,n} = 2^{\,x} \;\Rightarrow\; n = x\,\log_{10}2 \approx 0{,}3\,x$$

De ahí la equivalencia (cuadro de la diapositiva):

$$\boxed{\,1\ \text{octava} \cong 0{,}3\ \text{décadas}\,}\qquad \boxed{\,1\ \text{década} \cong 3{,}3\ \text{octavas}\,}$$

> [!note] Por qué importa para el Bode
> La pendiente de un filtro de 1.er orden es $-20\ \text{dB/década}$, que equivale a $-20\times0{,}3 = -6\ \text{dB/octava}$. Por eso se dice indistintamente "$-20\ \text{dB/déc}$" o "$-6\ \text{dB/oct}$" (y "$-40\ \text{dB/déc} = -12\ \text{dB/oct}$" para 2.º orden). Es la misma caída expresada en distinta unidad de frecuencia.

> [!example] Verificación rápida
> De $1\ \text{kHz}$ a $1\ \text{MHz}$ hay $\log_{10}(10^6/10^3)=3$ **décadas**, o $\log_2(1000)\approx 9{,}97$ **octavas** $\approx 3\times 3{,}3$. ✓

## 4. Gráfica

Diagrama de Bode de un pasa bajo de 1.er orden con $f_c=1\ \text{kHz}$ y $A_0=1$ (0 dB): magnitud y fase, curva **real** vs. **asíntotas**. Se ve el codo a $-3\ \text{dB}$ en $f_c$, la pendiente de $-20\ \text{dB/déc}$ y la fase pasando por $-45^\circ$ en $f_c$.

![[bode_primer_orden.png]]

Script: [`plot_bode_primer_orden.py`](plot_bode_primer_orden.py) — ejecutar con `uv run --with matplotlib --with numpy python plot_bode_primer_orden.py`.

---

## Bibliografía

- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*. Pearson — filtros $RC$, filtros activos y diagramas de Bode.
- Coughlin, R. & Driscoll, F. *Amplificadores Operacionales y Circuitos Integrados Lineales*. Pearson — filtros activos de primer orden con op-amp.
- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press — respuesta en frecuencia y diagramas de Bode.
