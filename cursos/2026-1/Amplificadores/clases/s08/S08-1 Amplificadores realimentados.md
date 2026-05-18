---
title: "Amplificadores realimentados"
curso: "[[Amplificadores MOC]]"
unidad: 2
semana: 8
orden: 1
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/realimentacion
  - tema/realimentacion-negativa
  - tema/topologias-feedback
  - tema/lazo-cerrado
  - tema/estabilidad
date: 2026-05-11
---

> [!info] Contexto
> Hasta la semana 7 se trabajo el op-amp asumiendo que la **realimentacion negativa** "simplemente funciona": al cerrar el lazo entre la salida y la entrada inversora, la ganancia queda fijada por las resistencias externas y no por el $A_{ol}$ del chip. Esta semana se generaliza ese principio a cualquier amplificador (op-amp, transistor, etapa multietapa) y se estudian las **cuatro topologias canonicas** de realimentacion.

## Que es la realimentacion

La **realimentacion** (feedback) consiste en tomar una porcion de la senal de salida de un amplificador y devolverla a la entrada combinada con la senal original. El amplificador deja de operar en **lazo abierto** (open-loop) y pasa a operar en **lazo cerrado** (closed-loop).

```
              +---------+
   x_s ---+--→|    A    |---+--→ x_o
          |   +---------+   |
          ↑                 |
          |   +---------+   |
          +---|    β    |←--+
              +---------+
```

- $x_s$ = senal de fuente (entrada al sistema completo)
- $x_i = x_s - x_f$ = senal a la entrada del amplificador (error)
- $x_o$ = senal de salida
- $x_f = \beta \cdot x_o$ = senal realimentada
- $A$ = ganancia **directa** del amplificador (sin realimentar)
- $\beta$ = factor de la red de realimentacion (sample → feedback)

> [!important] Convencion de signos
> Cuando la senal realimentada **se resta** de la senal de entrada se habla de **realimentacion negativa** (degenerativa). Cuando se **suma** se habla de **realimentacion positiva** (regenerativa), util para osciladores y comparadores con histeresis pero indeseable en amplificadores lineales.

## Ecuacion fundamental

Partiendo del diagrama de bloques con resta en la entrada, escribimos las dos ecuaciones del lazo:

$$x_i = x_s - x_f = x_s - \beta x_o \quad\quad\text{(1) — resta en la entrada}$$
$$x_o = A \cdot x_i \quad\quad\text{(2) — salida = ganancia} \times \text{error}$$

Sustituyendo (1) en (2):

$$x_o = A(x_s - \beta x_o)$$

**Paso 1 — distribuir $A$:**

$$x_o = A x_s - A\beta x_o$$

**Paso 2 — pasar el termino con $x_o$ al lado izquierdo:**

$$x_o + A\beta x_o = A x_s$$

**Paso 3 — factorizar $x_o$:**

$$x_o(1 + A\beta) = A x_s$$

**Paso 4 — despejar $x_o/x_s$:**

$$\boxed{A_f \;\equiv\; \frac{x_o}{x_s} \;=\; \frac{A}{1 + A\beta}}$$

Donde:

- $A_f$ = **ganancia de lazo cerrado** (closed-loop gain)
- $A$ = **ganancia de lazo abierto** (open-loop gain)
- $A\beta$ = **ganancia de lazo** (loop gain), adimensional
- $1 + A\beta$ = **factor de desensibilizacion** o **factor de sacrificio** ($S$)

> [!info] Por que aparece el factor $(1+A\beta)$
> El factor $(1+A\beta)$ no es arbitrario: surge **porque $x_o$ aparece en ambos lados de la ecuacion** — eso es justamente lo que significa "lazo cerrado". Para resolver una ecuacion donde la incognita aparece dos veces hay que **agruparla** y factorizarla. El "1" viene del $x_o$ original del lado izquierdo; el "$A\beta$" viene del $x_o$ que se cuela en el lado derecho via la red de realimentacion.
>
> **Analogia algebraica**: resolver $y = 3(10 - y) \Rightarrow y = 30 - 3y \Rightarrow y(1+3) = 30 \Rightarrow y = 7.5$. El "$1+3$" sale por el mismo motivo que el "$1+A\beta$".

### Aproximacion de alta ganancia

Cuando $A\beta \gg 1$ (caso tipico con op-amps donde $A \sim 10^5$):

$$A_f \approx \frac{A}{A\beta} = \frac{1}{\beta}$$

> [!example] Op-amp no inversor
> En el amplificador no inversor visto en S04, $\beta = R_1/(R_1+R_f)$ y la ganancia queda $A_f = 1 + R_f/R_1 = 1/\beta$. **Toda la formula** $A_f = 1/\beta$ es un caso particular de la ecuacion fundamental.

## Por que conviene realimentar

> [!important] Objetivo de la realimentacion negativa
> **Sacrificar ganancia bruta** (que sobra en op-amps y etapas multietapa) **para obtener un amplificador con:**
>
> - ganancia **estable** y predecible (insensible a temperatura, lote y envejecimiento),
> - menor **distorsion no lineal**,
> - menor **ruido interno** y derivas termicas,
> - mayor **ancho de banda**,
> - **impedancias** de entrada y salida controlables segun la topologia.
>
> **Todas las mejoras se pagan por el mismo factor $(1+A\beta)$** — el "precio" en ganancia se convierte en mejora repartida entre las demas caracteristicas.

> [!info] Contexto historico
> La realimentacion negativa fue inventada por **Harold S. Black** en 1927 (Bell Labs, patente US 2,102,671 de 1937) para resolver el problema de **dispersion de ganancia entre tubos de vacio** en los amplificadores repetidores de las primeras lineas telefonicas transcontinentales. El problema no era el ancho de banda sino la **estabilidad de ganancia**: cada tubo tenia parametros distintos y al cabo de cientos de repetidores en serie la senal se degradaba impredeciblemente. Black demostro que **sacrificando ganancia por un factor $(1+A\beta)$** se obtenia un amplificador cuya ganancia dependia solo de **componentes pasivos** (resistencias) y no de los tubos. Los textos clasicos (Sedra-Smith cap. 10, Boylestad cap. 14, Razavi cap. 8, Jaeger-Blalock cap. 17) desarrollan el mismo marco teorico que esta nota.

Aunque la realimentacion **reduce la ganancia** por un factor $(1+A\beta)$, **mejora todas las demas caracteristicas del amplificador** en el mismo factor:

| Caracteristica | Sin realimentacion | Con realimentacion negativa |
| -------------- | ------------------ | --------------------------- |
| Ganancia | $A$ (alta, imprecisa) | $A_f = A/(1+A\beta)$ (baja, precisa) |
| Sensibilidad a $\Delta A$ | $\Delta A_f/A_f = \Delta A/A$ | $\Delta A_f/A_f = (\Delta A/A)/(1+A\beta)$ |
| Ancho de banda | $BW$ | $BW \cdot (1+A\beta)$ |
| Distorsion armonica | $D$ | $D/(1+A\beta)$ |
| Ruido (no termico) | $N$ | $N/(1+A\beta)$ |
| Impedancia entrada | $Z_i$ | $Z_i \cdot (1+A\beta)$ o $Z_i/(1+A\beta)$ segun topologia |
| Impedancia salida | $Z_o$ | $Z_o/(1+A\beta)$ o $Z_o \cdot (1+A\beta)$ segun topologia |

El detalle de cada mejora se desarrolla en las secciones siguientes: insensibilidad (estabilidad de la amplificacion), ancho de banda y efectos sobre impedancias (estos ultimos en la seccion de topologias).

### Insensibilidad — estabilidad de la amplificacion

La ganancia de lazo abierto $A$ de un amplificador real **varia** por temperatura, envejecimiento, dispersion entre lotes o reemplazo del chip. Interesa cuantificar cuanto de esa variacion se traslada a $A_f$.

**Paso 1 — derivar $A_f$ respecto a $A$** usando la regla del cociente $(u/v)' = (u'v - uv')/v^2$ con $u = A$, $u' = 1$, $v = 1+A\beta$, $v' = \beta$ (asumiendo $\beta$ constante: la red de realimentacion es pasiva):

$$\frac{dA_f}{dA} = \frac{(1)(1+A\beta) - (A)(\beta)}{(1+A\beta)^2} = \frac{1 + A\beta - A\beta}{(1+A\beta)^2}$$

$$\boxed{\;\frac{dA_f}{dA} = \frac{1}{(1+A\beta)^2}\;}$$

Una variacion **absoluta** $dA$ en la ganancia de lazo abierto produce una variacion $dA_f = dA/(1+A\beta)^2$ en la ganancia de lazo cerrado — atenuada por el **cuadrado** del factor de desensibilizacion.

**Paso 2 — pasar a variacion relativa** (lo util en la practica) dividiendo $dA_f$ entre $A_f = A/(1+A\beta)$:

$$\frac{dA_f}{A_f} = \frac{dA/(1+A\beta)^2}{A/(1+A\beta)} = \frac{dA}{A(1+A\beta)}$$

$$\boxed{\;\frac{dA_f}{A_f} = \frac{1}{1+A\beta}\cdot\frac{dA}{A}\;}$$

**Paso 3 — definir la sensibilidad** $S^{A_f}_A$ como el cociente entre variaciones relativas:

$$S^{A_f}_A \;\equiv\; \frac{dA_f/A_f}{dA/A} \;=\; \frac{1}{1+A\beta}$$

> [!important] Lectura fisica
> $S^{A_f}_A$ dice "que fraccion del error relativo en $A$ se traslada a $A_f$". La realimentacion negativa **divide el error porcentual entre $(1+A\beta)$**. Con $A\beta = 99$, una variacion del **10%** en $A$ se ve reducida a una variacion del **0.1%** en $A_f$.

### Ejemplo numerico

Op-amp con $A_{ol} = 10^5$, red de realimentacion $\beta = 0.01$ → $A\beta = 1000$, $A_f \approx 99.9$.

| Variacion en $A$ | $\Delta A/A$ | $\Delta A_f/A_f$ | $\Delta A_f$ resultante |
| ---------------- | ------------ | ----------------- | ----------------------- |
| $A: 10^5 \to 0.5\times10^5$ | 50% | $50\%/1001 \approx 0.05\%$ | $\approx 0.05$ |
| $A: 10^5 \to 2\times10^5$ | 100% | $100\%/1001 \approx 0.1\%$ | $\approx 0.1$ |
| $A: 10^5 \to 10^4$ (chip degradado) | 90% | $90\%/101 \approx 0.9\%$ | $\approx 0.9$ |

Incluso un colapso de $A$ a un decimo de su valor solo desplaza $A_f$ en menos de un 1%. **Esa es la razon por la que se acepta sacrificar ganancia bruta por realimentacion**: la ganancia del chip se vuelve **irrelevante** mientras siga siendo "suficientemente grande", y el comportamiento queda determinado por la red pasiva $\beta$ (resistencias de tolerancia 1% o menos).

### Ancho de banda y producto ganancia-ancho de banda

#### Que es el ancho de banda

El **ancho de banda** (bandwidth, $BW$) es el **rango de frecuencias** en el que un amplificador funciona "como debe": entrega aproximadamente la misma ganancia para todas las senales dentro de ese rango. Ningun amplificador real amplifica por igual a 1 Hz que a 100 MHz — capacitancias internas, condensadores de compensacion, parasitas del layout y acoplamientos limitan la respuesta en frecuencia.

```
   |A| (dB)
    │
A_0 │      ╭──────────────────────╮
    │     ╱│         BW           │╲
A_0-3dB ──╱─│─────────────────────│─╲────
    │   ╱   │                     │  ╲
    │  ╱    │                     │   ╲
    └─╱─────┼─────────────────────┼────╲────→ f (log)
          f_L                    f_H
       (corte inferior)      (corte superior)
```

**Definicion operativa**: el ancho de banda se delimita por las frecuencias donde la ganancia cae **3 dB** (factor $1/\sqrt{2} \approx 0.707$) respecto a la zona plana $A_0$. Estas frecuencias se llaman **frecuencias de corte** o **frecuencias de $-3$ dB**.

> [!info] Por que $-3$ dB
> En la frecuencia de corte la **potencia** de la senal cae a la mitad ($|A|^2$ pasa de $A_0^2$ a $A_0^2/2$, lo que en dB son exactamente $10\log_{10}(2) \approx 3$ dB). Es la frontera convencional entre "el amplificador aun sirve" y "el amplificador ya no responde".

#### Corte superior $f_H$ — filtros pasa-bajos parasitos

El **corte superior $f_H$** existe **siempre** (no se puede evitar). Lo causan capacitancias **en paralelo** con las trayectorias de senal, que a alta frecuencia cortocircuitan la senal a tierra:

1. **Capacitancias internas del transistor**: $C_{be}$, $C_{bc}$ en BJT; $C_{gs}$, $C_{gd}$ en MOSFET.
2. **Efecto Miller**: $C_{bc}$ (o $C_{gd}$) entre entrada y salida se ve amplificada por la ganancia → $C_M = C_{bc}(1 + |A_v|)$ → polo de entrada muy bajo.
3. **Capacitancias parasitas** del layout, cableado y pistas del PCB.
4. **Condensador de compensacion interna** del op-amp (e.g. los 30 pF del 741), agregado a proposito para garantizar estabilidad.
5. **Capacitancia de la carga** ($C_L$): cable largo, sonda de osciloscopio, etapa de entrada FET de otro circuito.

Cada uno forma con su resistencia equivalente un **filtro pasa-bajos** de corte $f = 1/(2\pi RC)$. El $f_H$ del amplificador es el **menor** de todos esos (el polo dominante a alta frecuencia).

#### Corte inferior $f_L$ — filtros pasa-altos parasitos

El **corte inferior $f_L$** **solo existe** si hay elementos reactivos **en serie** que bloquean DC:

1. **Condensadores de acoplo** entre etapas (separan el bias DC de una etapa al pasar a la siguiente).
2. **Condensador de desacoplo de emisor** ($C_E$) — a baja frecuencia su impedancia crece y la ganancia colapsa.
3. **Condensador de acoplo a la entrada** y **a la salida** del amplificador.
4. **Transformadores** (no transmiten DC).

Cada uno forma con su resistencia equivalente un **filtro pasa-altos** de corte $f = 1/(2\pi RC)$. El $f_L$ del amplificador es el **mayor** de todos esos.

> [!example] Etapa BJT clasica con tres condensadores
> Una etapa emisor comun "de libro" tiene $C_{in}$ (acoplo entrada), $C_E$ (desacoplo emisor) y $C_{out}$ (acoplo salida). Cada uno introduce su propio $f_L$; el dominante (el mayor) marca el corte. Tipicamente $C_E$ es el dominante porque la resistencia de emisor reflejada es pequena.

#### Amplificadores DC-coupled vs AC-coupled

| Tipo de amplificador | $f_L$ | $f_H$ | $BW$ |
| -------------------- | ----- | ----- | ---- |
| **Op-amp** (DC-coupled) | **0 Hz** (no hay) | $f_H$ | $f_H$ |
| Etapa BJT acoplada por C | $f_L > 0$ | $f_H$ | $f_H - f_L$ |
| Amplificador de audio HiFi | $\sim 20$ Hz | $\sim 20$ kHz | $\sim 20$ kHz |
| Amplificador de RF sintonizado | $f_0 - \Delta/2$ | $f_0 + \Delta/2$ | $\Delta$ (estrecho, intencional) |

Los **op-amps** se fabrican con pares diferenciales y espejos de corriente integrados — sin condensadores en serie. Responden hasta **DC** (0 Hz). Si se necesita bloquear DC, se agrega **externamente** un condensador de acoplo; el $f_L$ resultante no es un defecto del op-amp sino una decision del disenador.

#### Modelo de polo dominante

La mayoria de op-amps se modelan con un **unico polo dominante**:

$$A(j\omega) = \frac{A_0}{1 + j(\omega/\omega_p)}$$

Donde $\omega_p = 2\pi f_p$ es la frecuencia del polo. En esa frecuencia:

$$|A(j\omega_p)| = \frac{A_0}{\sqrt{1+1}} = \frac{A_0}{\sqrt{2}}$$

Es decir: **el polo dominante coincide con la frecuencia de corte superior**: $f_H = f_p$.

#### Producto ganancia-ancho de banda (GBW)

Para un amplificador con polo dominante, **el producto ganancia × ancho de banda es constante**:

$$\boxed{\;GBW \;=\; A \cdot BW \;=\; A_0 \cdot f_p \;=\; \text{constante}\;}$$

El chip "vende" siempre la misma cantidad de Hz·V/V — el disenador decide como distribuirla via la red de realimentacion.

**Demostracion de la conservacion bajo realimentacion**: si en lazo abierto el polo esta en $\omega_p$, en lazo cerrado pasa a $\omega_p(1+A_0\beta)$ y la ganancia DC baja por el mismo factor:

$$A_{f,0} = \frac{A_0}{1+A_0\beta}, \quad\quad \omega_{p,f} = \omega_p(1+A_0\beta)$$

Multiplicando:

$$A_{f,0} \cdot \omega_{p,f} = \frac{A_0}{1+A_0\beta} \cdot \omega_p(1+A_0\beta) = A_0 \cdot \omega_p = GBW$$

**Lo que se pierde de ganancia se gana de ancho de banda — exactamente.**

#### Efecto de la realimentacion sobre $f_L$ y $f_H$

La realimentacion negativa **mueve ambas frecuencias de corte en sentido favorable** (expande el ancho de banda por ambos extremos):

$$\boxed{f_{H,f} = f_H \cdot (1 + A_0\beta) \quad\quad\text{(corte superior sube)}}$$

$$\boxed{f_{L,f} = \frac{f_L}{1 + A_0\beta} \quad\quad\text{(corte inferior baja)}}$$

Para amplificadores DC-coupled solo importa $f_{H,f}$; para amplificadores acoplados por C, ambos se desplazan.

#### Ejemplos numericos

**Op-amp 741** con $A_0 = 2 \times 10^5$, $f_p \approx 5$ Hz → $GBW = A_0 \cdot f_p = 10^6$ Hz = **1 MHz**:

| Ganancia de lazo cerrado $A_f$ | Ancho de banda resultante | Aplicacion tipica |
| ------------------------------ | ------------------------- | ----------------- |
| 1000 × | 1 MHz / 1000 = **1 kHz** | sensor de bajo nivel |
| 100 × | 1 MHz / 100 = **10 kHz** | audio mediano |
| 10 × | 1 MHz / 10 = **100 kHz** | audio completo |
| 1 × (buffer) | **1 MHz** | seguidor de tension rapido |

**Etapa BJT** con $f_L = 100$ Hz, $f_H = 10$ kHz, $A_0 = 200$. Realimentando con $\beta = 0.05$ → $1+A_0\beta = 11$:

- $A_f = 200/11 \approx 18$
- $f_{L,f} = 100/11 \approx 9$ Hz
- $f_{H,f} = 10\text{k} \times 11 = 110$ kHz
- $BW_f \approx 110$ kHz (la ganancia bajo $\times 11$, el BW subio $\times 11$, el GBW se mantiene).

> [!warning] El GBW limita la eleccion del op-amp
> Para amplificar a 10 MHz con ganancia 10 se necesita $GBW \geq 100$ MHz. El 741 (1 MHz) no llega; se requiere un op-amp de banda ancha como el OPA847 ($GBW \approx 4$ GHz). El GBW es **la metrica principal** al elegir op-amp para una aplicacion especifica.

#### Diagrama de Bode con varias ganancias de lazo cerrado

```
   |A| (dB)
    │
100 dB ────╲  A_ol (lazo abierto, A_0 = 10^5)
    │       ╲
 80 dB      ╲
    │   ────╲╲─  A_f = 100 (closed-loop)
    │        ╲╲
 40 dB ──────╲╲─────╲─  A_f = 10
    │         ╲╲    ╲
 20 dB          ╲   ╲╲─────╲─ buffer (A_f = 1)
    │            ╲   ╲      ╲
  0 dB ───────────╲───╲──────╲──── GBW = 1 MHz
    │              ╲   ╲      ╲
    └────────────────────────────────→ f (log)
       5Hz  50Hz  500Hz  5kHz  100kHz  1MHz
```

Todas las curvas de lazo cerrado se "estrellan" contra la misma asintota de lazo abierto en $f = GBW$ (el "techo" del chip).

### Caracteristica de transferencia (VTC)

La **VTC** (Voltage Transfer Characteristic, caracteristica de transferencia de voltaje) es la grafica de $V_{out}$ vs $V_{in}$ en **regimen estatico** (DC). Es el complemento DC del diagrama de Bode: mientras este describe la respuesta en frecuencia, la VTC describe el comportamiento punto a punto en amplitud.

De la VTC se leen directamente:

- **Ganancia DC** $A_v$ = pendiente $dV_{out}/dV_{in}$ en la zona lineal.
- **Rango de salida** = entre $+V_{sat}$ y $-V_{sat}$ (rieles de saturacion).
- **Umbrales de conmutacion** (puntos donde la curva cambia de regimen).
- **Histeresis** (si la curva depende de la direccion del barrido).

#### VTC del op-amp en lazo abierto

```
    V_out
      ↑
 +V_sat ─────────╮
                 │
               ╱ │  ← pendiente A_ol ≈ 10^5 (casi vertical)
              ╱  │     ventana lineal de solo ~100 µV
   ───────────╱──┼──→ V_d = V+ − V−
              │
              │
 -V_sat ──────╯
```

La pendiente $A_{ol}$ es tan grande que la zona lineal es **practicamente invisible** (unas decenas de microvoltios). Cualquier desbalance real entre $V_+$ y $V_-$ satura la salida. **Esta VTC justifica graficamente la necesidad de la realimentacion**: sin ella, el op-amp no es un amplificador lineal util.

#### VTC del op-amp con realimentacion negativa

```
    V_out
      ↑
 +V_sat ───────────╮
                   │
                 ╱ │  ← pendiente A_f = 1/β (mucho menor)
                ╱  │     zona lineal ANCHA, util
   ────────────╱───┼──→ V_in
              ╱    │
             ╱     │
 -V_sat ────╯
```

La realimentacion negativa **endereza la VTC**: reduce la pendiente al valor predecible $A_f = 1/\beta$ y, simultaneamente, **expande la zona lineal** hasta casi ocupar todo el rango entre rieles. La saturacion ya no la decide el chip sino la combinacion $A_f \cdot V_{in,max} = V_{sat}$.

> [!important] Conexion con la insensibilidad
> En lazo abierto, una variacion del 50% en $A_{ol}$ inclina la VTC drasticamente. En lazo cerrado, la misma variacion practicamente no cambia la pendiente. **La realimentacion fija la pendiente de la VTC** a un valor que solo depende de la red $\beta$ — exactamente lo cuantificado en la formula de sensibilidad $S^{A_f}_A = 1/(1+A\beta)$.

#### VTC del comparador (sin realimentacion, saturando)

```
    V_out
      ↑
 +V_sat ─────────╮
                 │
                 │
                 │
   ──────────────┼─────────→ V_in
                 │     V_ref
                 │
                 │
 -V_sat ─────────╯
```

Escalon ideal con pendiente "infinita" en $V_{in} = V_{ref}$. Util para decisiones binarias pero **vulnerable al ruido**: pequenas oscilaciones cerca del umbral producen conmutaciones espurias.

#### VTC del Schmitt trigger (realimentacion positiva)

```
    V_out
      ↑
 +V_sat ─────╮       ╭───────
             │       │
             │←──────┤   ← HISTERESIS: la curva
             │       │      depende de la direccion
             │       │      del barrido de V_in
             │       │
   ──────────┼───────┼──→ V_in
             │       │
        V_TL │       │ V_TH
 -V_sat ─────╯       ╰───────
```

VTC con **dos curvas distintas** segun si $V_{in}$ esta subiendo (umbral $V_{TH}$) o bajando (umbral $V_{TL}$). La separacion $V_{TH} - V_{TL}$ es el **ancho de histeresis** y da inmunidad al ruido. Es la **firma grafica de la realimentacion positiva** (ver [[S07-1 Comparadores y Schmitt trigger - ejercicios resueltos]] y [[S08-2 Realimentacion negativa y realimentacion positiva]]).

#### Sintesis: como la realimentacion modifica la VTC

| Tipo de realimentacion | Efecto sobre la VTC | Resultado |
| ---------------------- | ------------------- | --------- |
| **Ninguna** (lazo abierto) | Pendiente $A_{ol}$ extrema, zona lineal microscopica | Op-amp saturado, comparador crudo |
| **Negativa** | Pendiente reducida a $1/\beta$, zona lineal expandida, curva enderezada | Amplificador lineal estable |
| **Positiva** | Curva con histeresis, dos umbrales distintos | Biestable, Schmitt, latch |

> [!info] VTC y Bode son complementarios
> - **VTC**: que pasa **a una entrada dada** (amplitud, saturacion, linealidad). Eje: $V_{in}$.
> - **Bode**: que pasa **a una frecuencia dada** (ganancia, fase, BW). Eje: $\omega$.
>
> Juntos describen completamente un amplificador lineal. Para amplificadores **no lineales** (comparadores, Schmitt, logaritmico) la VTC es la herramienta principal porque la respuesta en frecuencia depende de en que punto de la VTC se este operando.

## Clasificacion de las topologias

La red de realimentacion puede conectarse al amplificador de **cuatro formas distintas**, segun:

1. **Que magnitud muestrea a la salida**: tension (en paralelo con $R_L$) o corriente (en serie con $R_L$).
2. **Como mezcla a la entrada**: en serie (suma de tensiones, KVL) o en paralelo (suma de corrientes, KCL).

Las $2 \times 2 = 4$ combinaciones dan las **cuatro topologias canonicas**:

| Topologia (mezcla–muestreo) | Tipo de amplificador | Senal entrada | Senal salida | Ganancia $A$ |
| --------------------------- | -------------------- | ------------- | ------------ | ------------ |
| **Serie–paralelo** (V–V) | Amplificador de **tension** | Tension | Tension | $A_v$ [V/V] |
| **Serie–serie** (V–I) | **Transconductancia** | Tension | Corriente | $G_m$ [A/V] = S |
| **Paralelo–paralelo** (I–V) | **Transresistencia** | Corriente | Tension | $R_m$ [V/A] = $\Omega$ |
| **Paralelo–serie** (I–I) | Amplificador de **corriente** | Corriente | Corriente | $A_i$ [A/A] |

> [!important] Regla mnemotecnica
> - **Muestreo en paralelo** (de tension) → la red lee $V_o$ → **estabiliza** $V_o$ → $Z_{out}$ **baja**.
> - **Muestreo en serie** (de corriente) → la red lee $I_o$ → **estabiliza** $I_o$ → $Z_{out}$ **sube**.
> - **Mezcla en serie** (de tension) → la red **suma tensiones** en la malla de entrada → $Z_{in}$ **sube**.
> - **Mezcla en paralelo** (de corriente) → la red **suma corrientes** en el nudo de entrada → $Z_{in}$ **baja**.

### Efecto sobre impedancias — tabla completa

| Topologia | $Z_{in,f}$ | $Z_{out,f}$ | Convierte fuente en... |
| --------- | ---------- | ----------- | ---------------------- |
| Serie–paralelo | $Z_{in}(1+A\beta)$ | $Z_{out}/(1+A\beta)$ | Fuente de **tension** ideal |
| Serie–serie | $Z_{in}(1+A\beta)$ | $Z_{out}(1+A\beta)$ | Fuente de **corriente** controlada por **tension** |
| Paralelo–paralelo | $Z_{in}/(1+A\beta)$ | $Z_{out}/(1+A\beta)$ | Fuente de **tension** controlada por **corriente** |
| Paralelo–serie | $Z_{in}/(1+A\beta)$ | $Z_{out}(1+A\beta)$ | Fuente de **corriente** ideal |

## Las cuatro topologias en detalle

### 1. Serie–paralelo (amplificador de tension)

Tambien llamada **voltage-series** o **shunt-shunt feedback** segun la fuente. Es la topologia mas comun en op-amps.

```
            +-----------+
   v_s --→ ( - )        |
            |     A_v   |---+---→ v_o
       +--→ ( + )       |   |
       |    +-----------+   |
       |       Z_o ↓        |
       |    +-----------+   |
       +----|     β     |←--+
            +-----------+
```

- **Muestrea $v_o$** (en paralelo con la carga, "lee el voltaje sin perturbar").
- **Realimenta $v_f = \beta v_o$** en serie con $v_s$ a la entrada.
- KVL en la malla de entrada: $v_i = v_s - v_f$.

**Resultado**: $Z_{in,f} = Z_{in}(1+A\beta)$ (muy alta) y $Z_{out,f} = Z_{out}/(1+A\beta)$ (muy baja) → **fuente de tension casi ideal**.

> [!example] Ejemplo canonico
> El **op-amp no inversor**: $\beta = R_1/(R_1+R_f)$, $A_v = 1+R_f/R_1$, $Z_{in} \to \infty$, $Z_{out} \to 0$. Ideal para acoplar fuentes de alta impedancia a cargas de baja impedancia (buffer de voltaje cuando $R_f = 0$ y $R_1 = \infty$).

### 2. Serie–serie (transconductancia)

```
            +-----------+        I_o
   v_s --→ ( - )        |--------↓---→ a R_L
            |     G_m   |        |
       +--→ ( + )       |    +---+ (sense)
       |    +-----------+    |
       |    +-----------+    |
       +----|     β     |←---+
            +-----------+
```

- **Muestrea $i_o$** (en serie con la carga, "lee la corriente que circula").
- **Realimenta $v_f = \beta i_o$** (la $\beta$ tiene unidades de **resistencia**, $\Omega$) en serie con $v_s$.
- La ganancia directa es **transconductancia**: $G_m = i_o/v_i$ en S.

**Resultado**: $Z_{in,f}$ alta, $Z_{out,f}$ alta → **fuente de corriente controlada por tension** (VCCS).

> [!example] Aplicaciones
> Etapas con resistencia de emisor sin desacoplar ($R_E$ sin condensador), fuentes de corriente Howland con op-amp, drivers de LEDs/diodos laser donde se desea controlar la corriente independientemente de las variaciones de la carga.

### 3. Paralelo–paralelo (transresistencia)

```
                R_f
            +---/\/\/\----+
            |             |
   i_s ----+→ ( - )        +---→ v_o
                |    R_m    |
                ( + )       |
                +-----------+
```

- **Muestrea $v_o$** (en paralelo con la carga).
- **Realimenta $i_f = \beta v_o$** (la $\beta$ tiene unidades de **conductancia**, S) en paralelo con $i_s$.
- KCL en el nudo de entrada: $i_i = i_s - i_f$.
- La ganancia directa es **transresistencia**: $R_m = v_o/i_i$ en $\Omega$.

**Resultado**: $Z_{in,f}$ baja, $Z_{out,f}$ baja → **fuente de tension controlada por corriente** (CCVS).

> [!example] Ejemplo canonico
> El **op-amp inversor** visto como amplificador de transresistencia: la entrada inversora es un **nudo virtual de tierra** ($Z_{in} \to 0$), la salida es una tension ($Z_{out} \to 0$), y la ganancia $v_o/i_{in} = -R_f$. Tambien los **convertidores I-V** para fotodiodos.

### 4. Paralelo–serie (amplificador de corriente)

```
                                I_o
   i_s ----+→ ( - )            ↓---→ a R_L
            |     A_i          |
            ( + )              |
            +----+         +---+ (sense)
                 |         |
                 +--[ β ]--+
```

- **Muestrea $i_o$** (en serie con la carga).
- **Realimenta $i_f = \beta i_o$** (la $\beta$ es adimensional, A/A) en paralelo con $i_s$.
- La ganancia directa es **corriente**: $A_i = i_o/i_i$ adimensional.

**Resultado**: $Z_{in,f}$ baja, $Z_{out,f}$ alta → **fuente de corriente casi ideal** (espejo "mejorado" por realimentacion).

> [!example] Aplicaciones
> Espejos de corriente con realimentacion (Wilson, cascode), etapas de amplificacion de corriente en colector comun con resistor sensor.

## Sintesis: cuadro unificado de topologias y magnitudes

Las cuatro topologias canonicas y las cuatro **magnitudes constitutivas** ($R$, $G$, $r_m$, $g_m$ — vistas en [[S07-4 Amplificador operacional de transconductancia (OTA)]]) no son cuadros independientes: comparten una estructura $2\times2$ subyacente. La conexion es que **las unidades de la ganancia de cada topologia coinciden con las cuatro relaciones V/I posibles entre dos terminales**.

Un amplificador es, en esencia, una "magnitud constitutiva **activa**" — un dispositivo que mantiene esa relacion V/I de forma controlada y con energia añadida.

### Cuadro $2 \times 2$ unificado

Las filas son **tipo de variable de entrada** (que se mezcla) y las columnas **tipo de variable de salida** (que se muestrea):

| Mezcla ↓ \ Muestreo → | **Paralelo** → muestrea $V_o$ | **Serie** → muestrea $I_o$ |
| --------------------- | ----------------------------- | -------------------------- |
| **Serie** → mezcla $V_{in}$ | **Serie–paralelo**<br>Amp. de **voltaje**<br>Ganancia $A_v$ — V/V (adimensional)<br>$Z_{in}\uparrow$, $Z_{out}\downarrow$<br>*Ej: op-amp no inversor* | **Serie–serie**<br>Amp. de **transconductancia**<br>Ganancia $G_m$ — **S (A/V)**<br>**↔ $g_m$**<br>$Z_{in}\uparrow$, $Z_{out}\uparrow$<br>*Ej: OTA, etapa con $R_E$* |
| **Paralelo** → mezcla $I_{in}$ | **Paralelo–paralelo**<br>Amp. de **transresistencia**<br>Ganancia $R_m$ — **$\Omega$ (V/A)**<br>**↔ $r_m$**<br>$Z_{in}\downarrow$, $Z_{out}\downarrow$<br>*Ej: op-amp inversor, conv. I-V* | **Paralelo–serie**<br>Amp. de **corriente**<br>Ganancia $A_i$ — A/A (adimensional)<br>$Z_{in}\downarrow$, $Z_{out}\uparrow$<br>*Ej: espejos Wilson/cascode* |

### Lectura cruzada

- **Diagonal principal** (V→V, I→I): amplificadores **adimensionales** (sin dimension fisica propia).
- **Antidiagonal** (V→I, I→V): amplificadores con dimension, "trans-" → exactamente las magnitudes $g_m$ y $r_m$.

Las cuatro topologias son las **cuatro posibilidades de elegir variable de entrada y variable de salida** entre $\{V, I\}$. No hay quinta ni sexta — el cuadro es **exhaustivo por construccion**.

### Regla mnemotecnica unificada

- **Mezcla en serie** (KVL en la malla de entrada) → entrada en **voltaje** → $Z_{in}$ **sube**.
- **Mezcla en paralelo** (KCL en el nodo de entrada) → entrada en **corriente** → $Z_{in}$ **baja**.
- **Muestreo en paralelo** (la red lee voltaje sin perturbar) → salida en **voltaje** → $Z_{out}$ **baja**.
- **Muestreo en serie** (la red lee corriente que circula) → salida en **corriente** → $Z_{out}$ **sube**.

> [!important] Para que sirve esto
> Una vez internalizado el cuadro, **no hace falta memorizar las cuatro topologias por separado**. Se identifica que tipo de variable se quiere a la entrada y a la salida → la celda dice topologia, unidad de ganancia, efecto sobre impedancias y ejemplo canonico. Es el "mapa de Karnaugh" de los amplificadores realimentados.

### Limitaciones de la analogia

La unificacion **no es perfecta**. Conviene tener claras dos diferencias conceptuales:

1. **Pasivo vs activo**. Las magnitudes $R$, $G$, $r_m$, $g_m$ son **relaciones constitutivas pasivas** — no requieren energia, existen en una resistencia, capacitor o transistor "estatico". Las cuatro ganancias de amplificador son **funciones de transferencia activas** — requieren energia de alimentacion y son **unidireccionales** entrada→salida (un amplificador no funciona "al reves").

2. **Solo la antidiagonal coincide en unidades**. El cuadro de magnitudes tiene dos celdas "no-trans" ($R$ y $G$ del **mismo** par de terminales) que **no tienen analogo directo** en el cuadro de topologias — las celdas equivalentes ($A_v$ y $A_i$) son **adimensionales**, no $\Omega$ ni S. La analogia exacta solo se da en la antidiagonal: $g_m \leftrightarrow G_m$ y $r_m \leftrightarrow R_m$. Es ahi donde la unidad fisica de la ganancia es **literalmente** la magnitud "trans-" correspondiente.

3. **Bonus — la realimentacion "tira hacia el ideal"**. En cada topologia, la realimentacion negativa empuja las impedancias hacia los valores **ideales del tipo de amplificador correspondiente**:
    - Amp. de voltaje ideal: $Z_{in} = \infty$, $Z_{out} = 0$ → serie-paralelo lo hace.
    - Amp. de corriente ideal: $Z_{in} = 0$, $Z_{out} = \infty$ → paralelo-serie lo hace.
    - Transconductancia ideal: $Z_{in} = \infty$, $Z_{out} = \infty$ → serie-serie lo hace.
    - Transresistencia ideal: $Z_{in} = 0$, $Z_{out} = 0$ → paralelo-paralelo lo hace.
    
    Es decir: **la topologia no es una eleccion arbitraria**, es la **unica** que convierte el amplificador real en una version mas cercana del tipo ideal deseado.

A pesar de estas limitaciones, el cuadro $2\times2$ captura lo esencial: las cuatro topologias son las cuatro combinaciones posibles de variable a la entrada y a la salida, y dos de ellas heredan directamente las unidades de las dos magnitudes "trans-".

## Ventajas y desventajas

### Ventajas de la realimentacion negativa

- **Ganancia controlada por elementos pasivos** ($R$, $C$): tolerancias del 1% son baratas; $A_{ol}$ del chip varia 30%.
- **Mayor ancho de banda** (a costa de ganancia, pero el GBW se conserva).
- **Menor distorsion no lineal** (la realimentacion "corrige" el error en cada instante).
- **Menor ruido y derivas** generadas internamente.
- **Impedancias ajustables** segun topologia (4 combinaciones posibles).
- **Inmunidad a variaciones** de temperatura, envejecimiento, dispersion.

### Desventajas

- **Perdida de ganancia** por un factor $(1+A\beta)$.
- **Posible inestabilidad**: si $A\beta$ alcanza fase $-180°$ con magnitud $\geq 1$, el denominador $1+A\beta \to 0$ y el sistema **oscila** (criterio de Barkhausen). Esto exige analisis de **margen de fase** y **margen de ganancia** (tema de la proxima sesion / curso de control).
- **Mayor complejidad** circuital: hay que diseñar la red $\beta$ y verificar que no introduzca polos adicionales.
- **Reduccion del rango dinamico** util en algunos casos (la salida tiene menos ganancia para amplificar entradas pequeñas).

> [!warning] Cuando la realimentacion negativa se vuelve positiva
> Todo amplificador real introduce **desfase** que aumenta con la frecuencia. Si a alguna frecuencia el desfase total del lazo llega a $180°$, la senal que originalmente se restaba ahora se **suma**: la realimentacion deja de ser correctora y pasa a ser regenerativa. Si ademas $|A\beta| \geq 1$ en esa frecuencia, el circuito oscila. La **compensacion en frecuencia** (e.g. el condensador interno del 741) busca garantizar que $|A\beta| < 1$ antes de llegar a $-180°$.

## Procedimiento de analisis (resumen)

Para analizar un amplificador realimentado real:

1. **Identificar la topologia** (mezcla y muestreo) observando como se conecta la red $\beta$.
2. **Separar la red $\beta$** del amplificador para obtener:
    - $A$: ganancia del amplificador **cargado** por la red $\beta$ (incluyendo $R_{in}$ y $R_{out}$ que la red presenta como carga).
    - $\beta$: factor de transferencia de la red sola (cortocircuitando entradas/salidas segun convenga).
3. **Calcular** $A_f = A/(1+A\beta)$, $Z_{in,f}$, $Z_{out,f}$ usando las formulas de la tabla segun topologia.
4. **Verificar estabilidad** con diagrama de Bode de $A\beta$ (margen de fase $> 45°$ ideal).

## Bibliografia

- Sedra, A. & Smith, K. *Microelectronic Circuits* (7ma ed.), Cap. 10/11 — Feedback. Oxford University Press.
- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*, Cap. 14 — Realimentacion y circuitos osciladores. Pearson.
- Miyara, F. (2005). *Amplificadores Realimentados* (2da ed.). Universidad Nacional de Rosario. [enlace](https://www.fceia.unr.edu.ar/enica3/realim.pdf)
- Fiore, J. *Operational Amplifiers and Linear Integrated Circuits — Theory and Application*, Cap. 3 — Negative Feedback. LibreTexts.
- Jaeger, R. & Blalock, T. *Microelectronic Circuit Design*, Cap. 17 — Feedback, Stability and Oscillators. McGraw-Hill.
