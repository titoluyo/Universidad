---
title: "Qué son los espejos de corriente"
curso: "[[Amplificadores MOC]]"
unidad: 2
semana: 13
orden: 1
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/espejo-de-corriente
  - tema/fuente-de-corriente
  - tema/carga-activa
  - tema/efecto-early
  - tema/transistor-bjt
date: 2026-06-15
---

## Contexto

Un **espejo de corriente** (*current mirror*) es un circuito que **copia** la corriente que circula por una rama de referencia hacia otra rama de salida, manteniéndola constante sin importar la carga conectada. El nombre viene de que la corriente de salida es un **reflejo** (una réplica) de la corriente de referencia.

Es el bloque básico para construir **fuentes de corriente** y **cargas activas** dentro de los circuitos integrados, donde no se pueden usar resistencias precisas ni de valor alto. Aparece en casi todo amplificador integrado: polariza las etapas y, como carga activa, eleva enormemente la ganancia.

> [!info] Toma de notas en clase
> Semana 13 — Sesión 25. Introducción a las **Fuentes de Corriente y cargas activas**: qué es un espejo de corriente, el espejo bipolar simple, su error por $\beta$ finita y la resistencia de salida (efecto Early). El espejo FET, la fuente Widlar y la fuente independiente de polarización se desarrollan en notas siguientes.

---

## 1. ¿Qué es un espejo de corriente?

Es un circuito de **dos transistores apareados** (idénticos, fabricados juntos) en el que:

1. Una corriente de **referencia** $I_{REF}$ se fija en la primera rama (con una resistencia o por otro medio).
2. La segunda rama entrega una corriente de **salida** $I_O$ que es **igual** (o un múltiplo conocido) de $I_{REF}$.

$$\boxed{\,I_O \approx I_{REF}\,}$$

La clave es que, al ser transistores apareados que **comparten la misma tensión base-emisor** $V_{BE}$, conducen la misma corriente de colector. La salida "espeja" lo que ocurre en la referencia.

> [!note] Idea central
> No se copia un *voltaje*, se copia una *corriente*. La salida se comporta como una **fuente de corriente** casi ideal: entrega $I_O$ constante aunque cambie la tensión sobre la carga.

## 2. ¿Por qué se usan? (en circuitos integrados)

> [!tip] Motivación
> En un **circuito integrado** las resistencias ocupan mucha área, son imprecisas y dependen de la temperatura. En cambio, dos transistores fabricados lado a lado salen prácticamente **idénticos**. El espejo aprovecha ese apareamiento para distribuir corrientes de polarización estables a partir de **una sola** corriente de referencia.

Dos usos principales:

- **Fuente de corriente / polarización:** generar corrientes de bias estables para varias etapas a partir de un único $I_{REF}$.
- **Carga activa:** sustituir la resistencia de colector $R_C$ por la salida de un espejo. Como su resistencia de salida $r_o$ es altísima, la ganancia $A_v \approx -g_m R_{out}$ crece muchísimo respecto a usar una resistencia física.

## 3. Espejo de corriente bipolar básico

Dos transistores NPN apareados $Q_1$ y $Q_2$ con las **bases unidas** y los **emisores a tierra**. $Q_1$ está **conectado como diodo** (colector unido a la base). La referencia $I_{REF}$ entra por el colector de $Q_1$; la salida $I_O$ se toma del colector de $Q_2$.

```
 V_CC
  │
  R            ┌────────── I_O (salida, a la carga)
  │            │
  ├───┐        │
  │   │C      C│
 I_REF│  Q1   Q2
  │   ├───────┤  (bases unidas)
  │   │B     B│
  └───┘        │
   E│         E│
  ─┴─        ─┴─   (emisores a tierra)
```

### 3.1 El transistor de referencia está "diodo-conectado"

En $Q_1$, colector y base están unidos, así que $V_{CB1}=0$ y el transistor queda en la **región activa** (justo en el borde), comportándose como un diodo base-emisor. Esto fija la tensión común de bases:

$$V_{BE} = V_{BE1}$$

### 3.2 Igualdad de corrientes (mismo $V_{BE}$)

La corriente de colector de un BJT en activa sigue la relación exponencial:

$$I_C = I_S\, e^{\,V_{BE}/V_T}$$

- $I_C$ = corriente de colector
- $I_S$ = corriente de saturación inversa (depende del tamaño del transistor)
- $V_{BE}$ = tensión base-emisor
- $V_T$ = tensión térmica ($\approx 26\ \text{mV}$ a temperatura ambiente)

Como $Q_1$ y $Q_2$ están **apareados** ($I_{S1}=I_{S2}$) y comparten **el mismo $V_{BE}$**, conducen la misma corriente de colector:

$$\boxed{\,I_{C2} = I_{C1}\,}$$

Esa es la esencia del espejo: igual $V_{BE}$ → igual $I_C$.

### 3.3 Corriente de referencia

$I_{REF}$ la fija la resistencia $R$ entre $V_{CC}$ y el nodo diodo-conectado:

$$\boxed{\,I_{REF} = \dfrac{V_{CC} - V_{BE}}{R}\,}$$

- $V_{CC}$ = tensión de alimentación
- $V_{BE}$ = caída base-emisor del transistor diodo-conectado ($\approx 0.7\ \text{V}$)
- $R$ = resistencia que fija la referencia

> [!quote] Material complementario — diapositivas del profesor
> "$V_{CC}$ se conecta en serie con una $R_x$ en el **colector del transistor que se utiliza para conectarse con la base** (el diodo-conectado). Los emisores van conectados a tierra." Con la notación de la diapositiva ($I_x \equiv I_{REF}$, $R_x \equiv R$):
> $$I_x = \dfrac{V_{CC} - V_{BE}}{R_x}$$

### Desarrollo en clase (manuscrito sobre la diapositiva)

En clase el docente resolvió el ejemplo a mano y, con él, **demostró la propiedad del espejo**: que la corriente de salida $I$ es una copia de la de referencia $I_x$. La incógnita planteada sobre la rama derecha del circuito es justamente "$I = ?$".

**1. Ley de Ohm** sobre la resistencia de referencia:

$$V = IR \;\Rightarrow\; I_x = \dfrac{V}{R}$$

**2. La tensión sobre $R_x$** es $V_{CC}$ menos la caída base-emisor del transistor diodo-conectado:

$$I_x = \dfrac{V_{CC} - V_{BE}}{R_x}$$

**3. Sustituir valores** ($V_{CC}=10\ \text{V}$, $V_{BE}\approx 0.7\ \text{V}$, $R_x=1\ \text{k}\Omega$):

$$I_x = \dfrac{10 - V_{BE}}{1\text{k}} = \dfrac{10 - 0.7}{1\text{k}} = \dfrac{9.3\ \text{V}}{1\,000\ \Omega} = 0{,}0093\ \text{A} = \boxed{9.3\ \text{mA}}$$

**4. Conclusión** — la corriente de salida espeja a la de referencia:

$$\boxed{\,I_x \simeq I\,}\quad\checkmark$$

Es decir, la rama de salida entrega $I \approx 9.3\ \text{mA}$ **sin importar la carga**: eso es lo que el desarrollo quería demostrar.

> [!note] Por qué $\simeq$ y no $=$
> El docente usa $\simeq$ a propósito. Por la corriente de base finita, la copia no es exacta: $I = \dfrac{\beta_F}{\beta_F+2}\,I_x \approx I_x$. Con $\beta_F=100$, $I \approx 0.98\times 9.3 \approx 9.1\ \text{mA}$ (un 2 % menos). Este es el resultado de la *Demostración de $I_Q=(\beta_F+2)I_{B1}$* y de la sección *Error por $\beta$ finita* (§3.4), más abajo.

### 3.4 Error por $\beta$ finita

En el caso ideal $I_O = I_{REF}$, pero las **corrientes de base** introducen un pequeño error. La referencia debe alimentar el colector de $Q_1$ **más** las dos bases:

$$I_{REF} = I_{C1} + I_{B1} + I_{B2}$$

Con transistores idénticos $I_{C1}=I_{C2}=I_C$ e $I_B = I_C/\beta$:

$$I_{REF} = I_C + 2\frac{I_C}{\beta} = I_C\left(1 + \frac{2}{\beta}\right)$$

Como la salida es $I_O = I_C$, despejando:

$$\boxed{\,\dfrac{I_O}{I_{REF}} = \dfrac{1}{1 + \dfrac{2}{\beta}}\,}$$

> [!example] Tamaño del error
> Con $\beta = 100$:
> $$\frac{I_O}{I_{REF}} = \frac{1}{1 + 2/100} = \frac{1}{1.02} \approx 0.980$$
> El espejo entrega un **2 % menos** de lo ideal. Cuanto mayor sea $\beta$, más fiel es la copia: con $\beta \to \infty$, $I_O \to I_{REF}$.

### Demostración de $I_Q = (\beta_F + 2)\,I_{B1}$

> [!note] Notación de la diapositiva
> El docente llama $I_Q$ a la corriente de referencia ($\equiv I_{REF}$) y $\beta_F$ a la ganancia de corriente. El transistor **2** es el de referencia (*diodo-conectado*, por donde entra $I_Q$) y el **1** es el de salida ($I_O = I_{C1}$). El resultado es idéntico al de arriba: $\frac{\beta_F}{\beta_F+2} = \frac{1}{1+2/\beta}$.

**1. KCL en el colector de 2.** El colector de 2 está unido a su propia base **y** a la base de 1. A ese nodo entra $I_Q$ y salen tres ramas: $I_{C2}$ (al colector de 2), $I_{B2}$ (a la base de 2) e $I_{B1}$ (a la base de 1):

$$I_Q = I_{C2} + I_{B2} + I_{B1}$$

**2. Transistores iguales.** Comparten el mismo $V_{BE}$ (mismo nodo de base, emisores a tierra). Como $I_C = I_S e^{V_{BE}/V_T}$ y están apareados:

$$V_{BE1}=V_{BE2}\;\Rightarrow\; I_{B1}=I_{B2}\quad\text{y}\quad I_{C1}=I_{C2}$$

**3. Expresar el colector en función de la base.** En activa $I_C=\beta_F I_B$, y como $I_{B2}=I_{B1}$:

$$I_{C2} = \beta_F\,I_{B2} = \beta_F\,I_{B1}$$

**4. Sustituir y factorizar.** Reemplazando $I_{C2}=\beta_F I_{B1}$ e $I_{B2}=I_{B1}$ en la KCL:

$$I_Q = \underbrace{\beta_F\,I_{B1}}_{I_{C2}} + \underbrace{I_{B1}}_{I_{B2}} + \underbrace{I_{B1}}_{I_{B1}} = (\beta_F + 1 + 1)\,I_{B1}$$

$$\boxed{\,I_Q = (\beta_F + 2)\,I_{B1}\,}$$

> [!tip] De dónde sale el "+2"
> El $\beta_F$ viene del **colector** de 2 ($I_{C2}=\beta_F I_{B1}$); cada **+1** es una de las **dos corrientes de base** ($I_{B1}=I_{B2}$). Son los dos transistores "robándole" corriente de base a la referencia.

**5. Cierre.** Despejando $I_{B1}$ y usando $I_O = I_{C1} = \beta_F I_{B1}$:

$$I_{B1}=\frac{I_Q}{\beta_F+2} \;\Rightarrow\; I_O=\beta_F\,I_{B1}=\frac{\beta_F}{\beta_F+2}\,I_Q \approx I_Q$$

### ¿Por qué $\dfrac{\beta_F}{\beta_F+2} \approx 1$?

Porque **$\beta_F$ es grande** (típicamente $100$–$300$ en un BJT), así que sumarle $2$ casi no cambia el denominador. Se ve mejor dividiendo numerador y denominador entre $\beta_F$:

$$\frac{\beta_F}{\beta_F + 2} = \frac{1}{1 + \dfrac{2}{\beta_F}}$$

El término que estorba es $\dfrac{2}{\beta_F}$, y como $\beta_F \gg 2$ resulta diminuto:

$$\beta_F \gg 2 \;\Rightarrow\; \frac{2}{\beta_F} \approx 0 \;\Rightarrow\; \frac{1}{1+\frac{2}{\beta_F}} \approx 1$$

| $\beta_F$ | $\dfrac{2}{\beta_F}$ | $\dfrac{\beta_F}{\beta_F+2}$ | Error |
|-----------|----------------------|------------------------------|-------|
| 50        | 0.040                | $50/52 = 0.9615$             | 3.8 % |
| 100       | 0.020                | $100/102 = 0.9804$           | 2.0 % |
| 200       | 0.010                | $200/202 = 0.9901$           | 1.0 % |
| 300       | 0.0067               | $300/302 = 0.9934$           | 0.7 % |

> [!note] Idea clave
> El "+2" son las dos corrientes de base que se "pierden". Frente a un colector que conduce $\beta_F$ veces esa base, esas 2 unidades son **despreciables**. En el límite $\beta_F \to \infty$, $\dfrac{\beta_F}{\beta_F+2} \to 1$ y $I_O = I_Q$ exactamente. Es el mismo argumento de "término despreciable" de la aproximación del rizado ($CR \gg T$) en [[S12-1 Tema 12 - Rectificador de pico y rizado|S12-1]].

## 4. Resistencia de salida y efecto Early

Un espejo ideal entregaría $I_O$ **perfectamente constante** para cualquier tensión de salida. En la práctica, el **efecto Early** (modulación del ancho de base) hace que $I_C$ aumente ligeramente con $V_{CE}$. Esto se modela con una **resistencia de salida finita**:

$$\boxed{\,r_o = \dfrac{V_A}{I_C}\,}$$

- $r_o$ = resistencia de salida del transistor de salida
- $V_A$ = tensión de Early (típica $50$–$100\ \text{V}$)
- $I_C$ = corriente de colector ($\approx I_O$)

> [!quote] Material complementario — notación de parámetros $h$ (diapositiva)
> La diapositiva escribe la resistencia de salida del espejo $R_Q$ como el **inverso del parámetro híbrido de salida** $h_{oe}$ del transistor de salida:
> $$R_Q = h_{oe,1}^{-1} \approx \dfrac{V_{AF,1}}{I_O}$$
> Es la **misma** $r_o$ de arriba: $h_{oe}$ es la admitancia de salida del modelo de parámetros $h$, así que $h_{oe}^{-1}$ es una resistencia, y $V_{AF}$ es la tensión de Early directa (*forward*). Por eso $R_Q = h_{oe,1}^{-1} \approx V_{AF,1}/I_O \equiv V_A/I_C$. El subíndice $1$ indica que es el transistor de **salida** (notación de la diapositiva, donde el de referencia es el $2$).

Incluyendo el efecto Early, la corriente de salida depende débilmente de su tensión:

$$I_O \approx I_{REF}\left(1 + \frac{V_{CE2} - V_{CE1}}{V_A}\right)$$

> [!note] Por qué importa para la ganancia
> Como **carga activa**, lo que interesa es que $r_o$ sea **grande**: cuanto más plana la característica $I_O$–$V_{CE}$, más se parece a una fuente ideal y mayor es la ganancia del amplificador. Un $V_A$ alto (curva casi horizontal) es lo deseable.

---

## 5. Variantes que veremos

El espejo simple es el punto de partida. La familia completa (sesión 25 del sílabo) incluye:

- **Espejo FET simple:** misma idea con MOSFET. Como la puerta no consume corriente DC ($I_G = 0$), **no hay error por $\beta$** — la copia depende de la relación de tamaños $W/L$.
- **Fuente Widlar:** agrega una resistencia en el emisor de $Q_2$ para obtener corrientes de salida **muy pequeñas** sin usar resistencias enormes.
- **Fuente independiente de polarización:** corriente de salida que **no depende** de $V_{CC}$.

## 6. Gráfica

Característica de salida del espejo bipolar ($I_{REF} = 1\ \text{mA}$, $V_A = 50\ \text{V}$). La fuente ideal sería una recta horizontal; la real tiene una pequeña pendiente $1/r_o$ debida al efecto Early, y cae a cero por debajo de $V_{CE,sat}$ (el transistor de salida entra en saturación y deja de espejar).

![[espejo_corriente.png]]

> [!example] Verificación numérica
> Con $V_A = 50\ \text{V}$ e $I_C = 1\ \text{mA}$:
> $$r_o = \frac{V_A}{I_C} = \frac{50\ \text{V}}{1\ \text{mA}} = 50\ \text{k}\Omega$$
> Entre $V_{CE} = 0.2\ \text{V}$ y $10\ \text{V}$ la salida sube de $\approx 1.00$ a $\approx 1.20\ \text{mA}$ (20 % en casi 10 V): una pendiente muy suave, coherente con la $r_o$ alta de la gráfica.

Script: [`plot_espejo_corriente.py`](plot_espejo_corriente.py) — ejecutar con `uv run --with matplotlib --with numpy python plot_espejo_corriente.py`.

---

## Bibliografía

- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press — cap. de fuentes de corriente y espejos.
- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*. Pearson.
- Jaeger, R. & Blalock, T. *Microelectronic Circuit Design*. McGraw-Hill.
