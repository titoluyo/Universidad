---
title: "Análisis del oscilador puente de Wien"
curso: "[[Amplificadores MOC]]"
unidad: 2
semana: 11
orden: 2
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/osciladores
  - tema/oscilador-rc
  - tema/puente-de-wien
  - tema/criterio-de-barkhausen
date: 2026-06-02
---

## Contexto

El **puente de Wien** es el oscilador $RC$ por excelencia para **bajas frecuencias** (audio, $\sim 5\ \text{Hz}$ a $\sim 1\ \text{MHz}$), donde —como se justificó en [[S09-2 Osciladores]]— el uso de bobinas $LC$ es inviable por su tamaño y bajo $Q$. Esta nota desarrolla el **análisis completo**: la red de realimentación, la aplicación del criterio de Barkhausen, la frecuencia de oscilación, la condición de ganancia y el problema (clave) de la **estabilización de amplitud**.

> [!info] Enfoque de la nota
> Análisis basado en conocimientos generales de electrónica y fuentes confiables, no en el material del curso. Todas las expresiones se derivan paso a paso.

---

## 1. Topología del circuito

El oscilador combina un **amplificador no inversor** (con un OPAM) y una **red de Wien** ($RC$ serie + $RC$ paralelo) que cierra el lazo de realimentación positiva.

```
                       ┌──────────────────┐
                       │        ┌────|>──── Vout
              ┌────────┤(+)     │
              │        │  OPAM ─┤
   Red de     │   ┌────┤(−)     │
   Wien (β) ──┘   │    └────────┘
                  │         │
                 [ ] Rf     │
                  │         │  ← amplificador NO inversor: A = 1 + Rf/Rg
                 [ ] Rg     │
                  │         │
                 GND       Vout

   Red de Wien (rama de realimentación positiva, de Vout a (+)):

        Vout ──[ R1 ]──┬──[ C1 ]──┐
                       │          │      ← rama SERIE:  Zs = R1 + 1/(sC1)
                      [ ] R2     ═╪═ C2  ← rama PARALELO: Zp = R2 ‖ 1/(sC2)
                       │          │
                       └────┬─────┘
                            │
                          V(+)  (β·Vout)
                            │
                           GND
```

El sistema es un **lazo realimentado** $A\beta$, con:

- $A$ = ganancia del amplificador no inversor $= 1 + \dfrac{R_f}{R_g}$ (red de realimentación **negativa**, fija la ganancia).
- $\beta$ = factor de la **red de Wien** (realimentación **positiva**, fija la frecuencia).

---

## 2. La red de Wien: cálculo de $\beta$

Definimos las dos impedancias de la red:

$$
Z_s = R_1 + \frac{1}{j\omega C_1}
\qquad\qquad
Z_p = R_2 \parallel \frac{1}{j\omega C_2} = \frac{R_2}{1 + j\omega R_2 C_2}
$$

El factor de realimentación es un **divisor de tensión** entre $Z_s$ y $Z_p$:

$$
\beta(j\omega) = \frac{V_{(+)}}{V_{out}} = \frac{Z_p}{Z_s + Z_p}
$$

Sustituyendo y simplificando (multiplicando por $j\omega C_1$ y agrupando), se llega a la forma canónica:

$$
\beta(j\omega) = \frac{1}{\left(1 + \dfrac{C_2}{C_1} + \dfrac{R_1}{R_2}\right) + j\left(\omega R_1 C_2 - \dfrac{1}{\omega R_2 C_1}\right)}
$$

### Caso simétrico $R_1 = R_2 = R$ y $C_1 = C_2 = C$

Es el diseño habitual. La expresión colapsa a:

$$
\boxed{\;\beta(j\omega) = \frac{1}{3 + j\left(\omega RC - \dfrac{1}{\omega RC}\right)}\;}
$$

> [!note] Lectura del resultado
> El término real vale **3** y el término imaginario depende de la frecuencia. El comportamiento del oscilador queda determinado por cuándo ese término imaginario **se anula**.

---

## 3. Aplicación del criterio de Barkhausen

Para una oscilación senoidal sostenida, la **ganancia de lazo** debe cumplir (ver [[S09-1 Amplificadores con realimentacion positiva y osciladores]]):

$$
A\beta(j\omega_0) = 1
\quad\Longleftrightarrow\quad
\begin{cases} |A\beta| = 1 & \text{(condición de magnitud)} \\[4pt] \angle A\beta = 0^\circ & \text{(condición de fase)} \end{cases}
$$

### 3.1. Condición de fase → frecuencia de oscilación

La fase total es $0°$ cuando la parte imaginaria de $\beta$ se anula (el amplificador no inversor ya aporta $0°$):

$$
\omega_0 RC - \frac{1}{\omega_0 RC} = 0
\quad\Rightarrow\quad
\omega_0^2 = \frac{1}{(RC)^2}
$$

$$
\boxed{\;\omega_0 = \frac{1}{RC} \qquad f_0 = \frac{1}{2\pi RC}\;}
$$

Donde:

- $f_0$ = frecuencia de oscilación [Hz]
- $R$ = resistencia de cada rama de la red de Wien [$\Omega$]
- $C$ = capacitancia de cada rama [F]

### 3.2. Condición de magnitud → ganancia mínima

En $\omega = \omega_0$ el término imaginario es cero, así que $\beta(j\omega_0) = \dfrac{1}{3}$. Imponiendo $|A\beta| = 1$:

$$
A \cdot \frac{1}{3} = 1 \quad\Rightarrow\quad \boxed{A = 3}
$$

Como el amplificador no inversor tiene $A = 1 + R_f/R_g$:

$$
1 + \frac{R_f}{R_g} = 3 \quad\Rightarrow\quad \boxed{R_f = 2\,R_g}
$$

> [!important] Síntesis del diseño
> La **red de Wien fija la frecuencia** ($f_0 = 1/2\pi RC$) y exige que el amplificador entregue **ganancia exactamente 3**. Por eso la rama de realimentación negativa se diseña con $R_f = 2R_g$.

---

## 4. El problema crítico: estabilización de amplitud

Una ganancia de **exactamente** $A = 3$ es imposible de mantener en la práctica (tolerancias, temperatura, envejecimiento). Por eso se juega con la **dinámica de arranque** y un control no lineal:

- Si $A < 3$ → $|A\beta| < 1$ → la oscilación **se extingue** (polos en el semiplano izquierdo).
- Si $A = 3$ → $|A\beta| = 1$ → amplitud **constante** (polos sobre el eje imaginario).
- Si $A > 3$ → $|A\beta| > 1$ → la oscilación **crece** hasta **recortar (clipping)** contra las fuentes, distorsionándose.

> [!warning] El dilema
> Para que el oscilador **arranque solo** desde el ruido térmico se necesita $A$ ligeramente **mayor** que 3. Pero si se queda así, la señal crece y se distorsiona. Hace falta un mecanismo que **reduzca automáticamente la ganancia hasta 3 exacto** cuando la amplitud llega al nivel deseado.

### Mecanismos de control de amplitud (AGC no lineal)

1. **Lámpara incandescente clásica (diseño original de Hewlett, 1939):** se coloca como $R_g$. Al aumentar la amplitud, sube su temperatura y su resistencia, lo que **baja la ganancia** $1 + R_f/R_g$ hasta estabilizarla en 3. Es un control térmico lento pero de muy baja distorsión.
2. **Diodos en antiparalelo sobre $R_f$:** al crecer la señal, los diodos conducen en los picos y reducen la resistencia efectiva de realimentación, recortando suavemente la ganancia. Más simple, algo más de distorsión.
3. **JFET como resistencia controlada por tensión:** un lazo que rectifica la salida ajusta $R_{DS}$ del JFET (haciendo de $R_g$), regulando la ganancia con baja distorsión.

> [!tip] Conexión con el plano $s$
> Este es el mismo mecanismo descrito en [[S09-2 Osciladores]]: el sistema **arranca con polos en el semiplano derecho** ($A>3$) y, al actuar la no linealidad, los polos **migran hasta el eje imaginario** ($A=3$), estacionando la amplitud.

---

## 5. Ventajas y limitaciones

| Ventajas                                            | Limitaciones                                              |
| --------------------------------------------------- | -------------------------------------------------------- |
| Onda senoidal de muy baja distorsión (THD bajo)     | Limitado a baja/media frecuencia (RC grande arriba de MHz) |
| Frecuencia fácil de sintonizar (variar $R$ o $C$)   | Requiere control de amplitud para arrancar sin distorsión |
| Topología simple, un solo OPAM                      | Estabilidad de frecuencia inferior a la del cuarzo        |
| Solo necesita componentes $RC$ (sin bobinas)        | Sensible a tolerancias de $R$ y $C$                       |

> [!note] Wien vs. cristal de cuarzo
> El puente de Wien es la opción para **generar audio senoidal sintonizable de baja distorsión**, pero su estabilidad ($\sim 10^{-3}$) no compite con la de un resonador de cuarzo ($\sim 10^{-6}$). Cuando lo que importa es una **referencia de frecuencia ultraestable**, se usa cristal (ver [[S11-2 Osciladores de cristal de cuarzo]]).

---

## 6. Aplicaciones

- **Generadores de funciones / audio:** fuente de tono senoidal puro en instrumentos de laboratorio. El primer producto de Hewlett-Packard (HP200A) fue un oscilador de puente de Wien.
- **Pruebas de respuesta en frecuencia** de amplificadores y filtros de audio.
- **Calibración** y caracterización de equipos en banda de audio.
- **Demostración didáctica** del criterio de Barkhausen y del control de amplitud no lineal.

---

## Bibliografía

- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*. Pearson. (Oscilador de puente de Wien y desplazamiento de fase.)
- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press. (Osciladores RC y estabilización de amplitud.)
- Franco, S. *Design with Operational Amplifiers and Analog Integrated Circuits*. McGraw-Hill. (Oscilador de Wien con control de amplitud.)
