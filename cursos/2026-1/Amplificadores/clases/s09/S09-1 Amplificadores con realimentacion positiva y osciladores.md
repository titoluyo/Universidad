---
title: "Amplificadores con realimentación positiva y osciladores"
curso: "[[Amplificadores MOC]]"
unidad: 3
semana: 9
orden: 1
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/realimentacion-positiva
  - tema/osciladores
  - tema/criterio-de-barkhausen
date: 2026-05-18
---

## Contexto

Hasta la semana 8 estudiamos la **realimentación negativa**, que estabiliza la ganancia, amplía el ancho de banda y reduce la distorsión. En esta sesión cruzamos la frontera al caso opuesto: cuando la red de realimentación **suma en fase** con la entrada, el sistema puede dejar de comportarse como amplificador y convertirse en un **generador autónomo de señal**: un **oscilador**.

Un oscilador, en sentido estricto, es un amplificador que produce una señal periódica **sin necesidad de entrada externa**, aprovechando el ruido propio del circuito como semilla y una red selectiva en frecuencia que la sostiene.

## Marco general

### De realimentación negativa a positiva

La ganancia de un sistema realimentado se expresa como:

$$
A_f = \frac{A}{1 - A\beta}
$$

- $A$ = ganancia del amplificador en lazo abierto.
- $\beta$ = factor de la red de realimentación.
- $A\beta$ = **ganancia de lazo** (loop gain).

> [!info] Signo del lazo
> - Si $A\beta < 0$ → realimentación **negativa**: $|A_f| < |A|$, estabiliza.
> - Si $0 < A\beta < 1$ → realimentación **positiva** pero acotada: amplifica más que $A$, sin oscilar todavía.
> - Si $A\beta \to 1$ → $A_f \to \infty$: el sistema produce salida **sin entrada**. Es la condición de oscilación.

### Criterio de Barkhausen

Para oscilación sostenida y senoidal, la ganancia de lazo a la frecuencia de oscilación $f_0$ debe cumplir simultáneamente dos condiciones:

$$
\boxed{|A\beta| = 1 \quad \text{y} \quad \angle A\beta = 0° \;(\text{o múltiplo de } 360°)}
$$

Donde:

- $|A\beta| = 1$ → **condición de magnitud**: la energía perdida por ciclo es exactamente repuesta por el amplificador.
- $\angle A\beta = 0°$ → **condición de fase**: la señal regresa a la entrada en fase para reforzarse a sí misma.

> [!warning] En la práctica
> El diseño se hace con $|A\beta|$ **ligeramente mayor que 1** para garantizar el arranque del oscilador desde el ruido. Una vez en régimen, un mecanismo de **limitación no lineal** (saturación del activo, AGC, lámpara/termistor, diodos de recorte) lleva $|A\beta|$ a 1 efectivo. Sin este mecanismo la amplitud crecería hasta recortar bruscamente, distorsionando la senoide.

### Arranque y régimen permanente

1. **Arranque:** el ruido térmico del circuito contiene componentes en todas las frecuencias. La red selectiva deja pasar solo $f_0$.
2. **Crecimiento exponencial:** mientras $|A\beta| > 1$, la amplitud crece ciclo a ciclo.
3. **Limitación:** un no-linealidad reduce la ganancia efectiva al aumentar la amplitud.
4. **Régimen estable:** $|A\beta|_{\text{efectivo}} = 1$, amplitud constante.

## Familias de osciladores

| Familia          | Red selectiva                       | Rango típico      | Ejemplos                                       |
| ---------------- | ----------------------------------- | ----------------- | ---------------------------------------------- |
| **RC**           | Redes resistivas-capacitivas        | Hz – cientos kHz  | Puente de Wien, desplazamiento de fase, doble T |
| **LC**           | Tanque resonante L-C                | 100 kHz – cientos MHz | Hartley, Colpitts, Clapp, Armstrong          |
| **Cristal**      | Cristal de cuarzo piezoeléctrico    | 10 kHz – cientos MHz | Pierce, Miller, Colpitts con cristal         |
| **Relajación**   | Carga/descarga no lineal            | DC – decenas MHz  | Astable con 555, multivibradores              |

> [!note] Senoidal vs relajación
> Los **osciladores senoidales** (RC, LC, cristal) trabajan en régimen lineal con Barkhausen. Los **osciladores de relajación** son inherentemente no lineales (basados en la histéresis del [[S07-1 Comparadores y Schmitt trigger - ejercicios resueltos|Schmitt trigger]] o en disparos por umbral) y producen ondas cuadradas o triangulares.

## Conceptos clave a desarrollar en clase

> [!todo] Por completar mientras dicta el profesor
> - [ ] Definición operativa que da el profesor de "realimentación positiva"
> - [ ] Deducción/justificación del criterio de Barkhausen
> - [ ] Ejemplo de oscilador desarrollado en pizarra (topología, frecuencia, condición de oscilación)
> - [ ] Mecanismo de limitación de amplitud propuesto
> - [ ] Comentarios sobre estabilidad de frecuencia, deriva térmica, factor Q
> - [ ] Aplicaciones mencionadas (radiofrecuencia, relojes digitales, instrumentación, etc.)

## Desarrollo de la clase

### Criterio de oscilación (criterio de Barkhausen)

Formulado por **Heinrich Barkhausen** en 1921, es la condición clásica que debe cumplir un amplificador realimentado para sostener una oscilación **senoidal** de amplitud constante.

#### Deducción desde el lazo realimentado

Partimos del diagrama estándar de realimentación: una entrada $X_s$, un amplificador de ganancia $A(j\omega)$, y una red de realimentación $\beta(j\omega)$ que toma la salida $X_o$ y la inyecta de regreso a la entrada. La ecuación de transferencia es:

$$
\frac{X_o}{X_s} = A_f(j\omega) = \frac{A(j\omega)}{1 - A(j\omega)\,\beta(j\omega)}
$$

Para que el circuito produzca **salida sin entrada** ($X_s \to 0$ pero $X_o \neq 0$), el denominador debe anularse:

$$
1 - A(j\omega)\beta(j\omega) = 0 \quad\Longleftrightarrow\quad \boxed{A(j\omega)\,\beta(j\omega) = 1}
$$

Esta es la **ecuación característica del oscilador**. Como $A\beta$ es una cantidad compleja, la igualdad a 1 implica dos condiciones simultáneas:

#### Las dos condiciones de Barkhausen

> [!important] Enunciado
> A la frecuencia de oscilación $\omega_0$, la ganancia de lazo $T(j\omega) = A(j\omega)\beta(j\omega)$ debe satisfacer:
>
> 1. **Condición de magnitud:** $\;|A(j\omega_0)\,\beta(j\omega_0)| = 1$
> 2. **Condición de fase:** $\;\angle A(j\omega_0)\beta(j\omega_0) = 0°$ (o múltiplo entero de $360°$, equivalente a $2\pi n$ rad).

Interpretación física:

- La **condición de fase** selecciona **una sola frecuencia** $\omega_0$: aquella en la que la señal, tras recorrer amplificador y red de realimentación, vuelve a la entrada **exactamente en fase** para reforzarse. Es la condición que **fija** la frecuencia de oscilación.
- La **condición de magnitud** asegura que la energía aportada por el amplificador en cada ciclo **iguala** las pérdidas de la red selectiva y del propio amplificador. Sin esto, la oscilación se extingue ($|A\beta|<1$) o crece sin control ($|A\beta|>1$).

#### Aclaración importante: $1 - A\beta$ vs $1 + A\beta$

Es muy común encontrar la condición de oscilación escrita de **dos formas que parecen contradictorias**:

- $|A\beta| = 1$ con fase $0°$ (lo que se dedujo arriba).
- $|1 + A\beta| = 0$ (o equivalentemente $A\beta = -1$), que aparece en muchos textos.

**No son fórmulas distintas: son la misma condición escrita con distintas convenciones de signo en el sumador del lazo.**

##### Origen de la ambigüedad

La ecuación general del realimentado es:

$$
A_f = \frac{A}{1 \,\square\, A\beta}
$$

donde el signo $\square$ depende de **cómo se dibuje el sumador de la entrada**:

| Convención del sumador                                                | Función de transferencia              | Condición de oscilación ($A_f \to \infty$)         |
| --------------------------------------------------------------------- | ------------------------------------- | -------------------------------------------------- |
| **Resta:** $X_i = X_s - \beta X_o$ (Sedra/Smith — realimentación negativa por defecto) | $A_f = \dfrac{A}{1 + A\beta}$         | $1 + A\beta = 0 \;\Rightarrow\; A\beta = -1$      |
| **Suma:** $X_i = X_s + \beta X_o$ (Schilling/Belove y textos de osciladores — realimentación positiva por defecto) | $A_f = \dfrac{A}{1 - A\beta}$         | $1 - A\beta = 0 \;\Rightarrow\; A\beta = +1$      |

##### Lo que **sí** es invariante

Sin importar la convención, la oscilación exige que el denominador se anule. Eso da siempre:

$$
\boxed{\,|A\beta| = 1\,}
$$

La **condición de magnitud es la misma en ambas convenciones**. Lo único que cambia es la fase de referencia de $A\beta$:

| Convención              | $\angle A\beta$ en oscilación | Razón                                                                |
| ----------------------- | ----------------------------- | -------------------------------------------------------------------- |
| Sumador con **resta**   | $180°$                        | La inversión del sumador aporta $180°$; el resto del lazo aporta otros $180°$ → total $360°$. |
| Sumador con **suma**    | $0°$                          | El sumador no invierte; el resto del lazo aporta $0°$ (o $360°$) directamente. |

##### La regla física que zanja todo

> [!important] Lo único que importa físicamente
> Para oscilar, la señal debe volver al punto de partida **con la misma fase y la misma amplitud** que tenía. Es decir:
> - **Fase total alrededor del lazo cerrado** $=360°$ (equivalente a $0°$).
> - **Ganancia total alrededor del lazo** $=1$.
>
> Si se cuenta la fase del **lazo completo** (amplificador + red de realimentación + sumador), el resultado siempre es $360°$. La diferencia entre las dos convenciones es solo **dónde se contabilizan los $180°$ del sumador**: dentro de $A\beta$ (convención "suma", fase $=0°$) o fuera (convención "resta", fase $=180°$). Es contabilidad de signos, no física distinta.

##### Cómo reconocer cada caso

- Si se escribe $A_f = \dfrac{A}{1 + A\beta}$ y la oscilación se enuncia como "$1 + A\beta = 0$" → convención de **resta**. Pide $A\beta = -1$, equivalente a $|A\beta|=1$ con fase $180°$.
- Si se escribe $A_f = \dfrac{A}{1 - A\beta}$ y la oscilación se enuncia como "$A\beta = 1$" → convención de **suma**. Pide $|A\beta|=1$ con fase $0°$.

Ambas describen el mismo circuito. Cambiar de una a otra es simplemente redefinir $\beta \to -\beta$ (absorbiendo el signo del sumador en la red de realimentación).

#### Procedimiento de aplicación

Para analizar o diseñar un oscilador con Barkhausen:

1. **Abrir el lazo** mentalmente en un punto conveniente y obtener la expresión simbólica de $A\beta(j\omega)$.
2. **Imponer la condición de fase:** $\angle A\beta = 0$. Resolver para $\omega$ → se obtiene la **frecuencia de oscilación** $\omega_0$.
3. **Sustituir $\omega_0$** en $|A\beta|$ e imponer $|A\beta|=1$. Despejar la **relación entre componentes** (típicamente la ganancia mínima del amplificador) que sostiene la oscilación.

> [!example] Aplicación al puente de Wien (preview)
> En el oscilador de Wien, la red RC tiene $\angle\beta = 0°$ únicamente a $\omega_0 = 1/RC$ y allí $|\beta| = 1/3$. Por tanto el amplificador debe tener $A \geq 3$ para arrancar. Este es el resultado directo de aplicar el procedimiento anterior.

#### Arranque y control de amplitud

> [!warning] $|A\beta| = 1$ es una condición de equilibrio inestable
> En un diseño real **no se ajusta $|A\beta|$ exactamente a 1**: las tolerancias de los componentes, la temperatura y el envejecimiento moverían la ganancia de lazo y la oscilación se apagaría o saturaría.

La práctica es:

1. **Diseñar con $|A\beta|$ ligeramente mayor que 1** (típicamente 5–20 % de margen) para garantizar el arranque desde el ruido térmico.
2. **Incorporar un mecanismo no lineal** que reduzca la ganancia efectiva al crecer la amplitud, hasta llevar $|A\beta|$ a 1:
   - Saturación natural del activo (la onda se distorsiona).
   - **AGC** (control automático de ganancia) con detector y elemento variable.
   - Componentes con resistencia dependiente de la temperatura: **termistor PTC** o **lámpara incandescente** (clásico en el Wien de HP-200A de Bill Hewlett).
   - Diodos de recorte en la red de realimentación (limitan la excursión sin saturar el activo).

#### Limitaciones y matices

> [!note] Barkhausen es necesario pero **no estrictamente suficiente**
> El criterio garantiza la **existencia** de una oscilación de amplitud constante a $\omega_0$, pero no asegura que **arranque** desde condiciones iniciales nulas ni que **sea estable** ante perturbaciones. Para un análisis riguroso de estabilidad se usa el **criterio de Nyquist**: la oscilación es estable si el lugar de $A\beta(j\omega)$ encierra al punto $(1,0)$ del plano complejo de la manera adecuada.
> En la práctica, para los osciladores senoidales clásicos (Wien, desplazamiento de fase, LC, cristal), Barkhausen y Nyquist coinciden y el primero basta para el diseño.

#### Resumen visual

| Condición            | Expresión                         | Determina                       |
| -------------------- | --------------------------------- | ------------------------------- |
| Fase                 | $\angle A\beta(j\omega_0) = 0°$   | **Frecuencia** de oscilación    |
| Magnitud             | $\lvert A\beta(j\omega_0)\rvert = 1$ | **Ganancia mínima** del amplificador |

### Tipos de osciladores según rango de frecuencia

La clasificación práctica más útil agrupa los osciladores **senoidales** por el rango de frecuencias donde son eficientes y por el tipo de red selectiva que usan:

| Rango                       | Familia                       | Red selectiva                              | Topologías típicas                  |
| --------------------------- | ----------------------------- | ------------------------------------------ | ----------------------------------- |
| **Baja frecuencia**         | RC                            | Redes resistivas-capacitivas               | Wien, desplazamiento de fase, doble T |
| **Alta frecuencia, variable** | LC                          | Tanque resonante $L$-$C$                   | Colpitts, Hartley, Clapp, Armstrong |
| **Alta frecuencia, fija (precisión)** | Cristal               | Cristal de cuarzo piezoeléctrico           | Pierce, Miller, Colpitts a cristal  |

> [!info] ¿Por qué este corte?
> A **baja frecuencia** un inductor de valor útil sería físicamente enorme y caro: por debajo de ~100 kHz dominan las redes **RC**. En **radiofrecuencia** los inductores se hacen pequeños y prácticos, y el tanque **LC** ofrece alto $Q$ y sintonía variable. Cuando se necesita una **frecuencia muy precisa y estable** (relojes, comunicaciones, microcontroladores), se reemplaza el $LC$ por un **cristal de cuarzo**, que se comporta como un resonador con $Q$ varios órdenes de magnitud mayor.

#### Baja frecuencia: osciladores RC

Operan típicamente desde fracciones de Hz hasta ~1 MHz. La red de realimentación está hecha solo de resistencias y capacitores; la frecuencia se fija porque a $f_0$ la red presenta **fase $0°$** (o $180°$, según la convención) y atenuación conocida.

##### Oscilador del puente de Wien

Red: dos ramas $RC$ — una serie y una paralelo — que forman un divisor selectivo en frecuencia, montadas en un puente con dos resistencias del amplificador.

$$
f_0 = \frac{1}{2\pi R C}
$$

A esa frecuencia $\beta = \dfrac{1}{3}$ y $\angle\beta = 0°$. Por Barkhausen, el amplificador debe tener:

$$
A \;\geq\; 3
$$

Donde:

- $R, C$ = componentes iguales de las dos ramas del puente.
- $A$ = ganancia del amplificador no inversor.

> [!note] Control de amplitud clásico
> El histórico **HP-200A** (primer producto comercial de Hewlett-Packard, 1939) usaba una **lámpara incandescente** en la rama negativa del divisor de ganancia: al crecer la amplitud, la lámpara se calienta, su resistencia aumenta y la ganancia baja hasta $A=3$ exacto. Es un AGC pasivo y elegante.

##### Oscilador por desplazamiento de fase (phase-shift)

Red: **tres celdas $RC$ en cascada**, cada una aportando hasta $60°$ de desfase. La salida del amplificador es inversora ($180°$); las tres celdas deben aportar otros $180°$ a la frecuencia de oscilación para completar los $360°$ del lazo.

$$
f_0 = \frac{1}{2\pi RC\sqrt{6}}, \qquad A \;\geq\; 29
$$

Donde:

- $R, C$ = elementos iguales de las tres celdas.
- La atenuación de la red a $f_0$ es $1/29$, por eso la ganancia mínima es alta.

##### Oscilador doble T (notch)

Red: una **red doble T** (notch) en realimentación negativa que **rechaza** una frecuencia; al combinarse con una realimentación positiva débil, el sistema sostiene oscilación justo en la frecuencia de rechazo. Da formas de onda muy puras pero es sensible al ajuste de componentes.

#### Alta frecuencia variable: osciladores LC

Operan típicamente entre ~100 kHz y cientos de MHz. La red selectiva es un **circuito tanque** $L$-$C$ paralelo (o serie) que resuena a:

$$
f_0 = \frac{1}{2\pi\sqrt{LC}}
$$

El amplificador repone las pérdidas resistivas del tanque para mantener la oscilación. La frecuencia se **varía** fácilmente cambiando $C$ (condensador variable) o $L$ (núcleo móvil) → de ahí su uso en sintonizadores de radio.

##### Oscilador Colpitts

Característica distintiva: **divisor capacitivo** en el tanque. Dos capacitores $C_1$ y $C_2$ en serie forman el resonador con un inductor $L$ en paralelo. El nodo intermedio entre $C_1$ y $C_2$ proporciona la realimentación al amplificador.

$$
f_0 = \frac{1}{2\pi\sqrt{L\,C_{eq}}}, \qquad C_{eq} = \frac{C_1\,C_2}{C_1+C_2}
$$

Condición de ganancia (forma aproximada, con $A_v$ ganancia del transistor en emisor común):

$$
A_v \;\geq\; \frac{C_2}{C_1}
$$

Donde:

- $C_{eq}$ = capacidad equivalente del divisor serie $C_1$-$C_2$.
- $C_2/C_1$ = factor de realimentación $\beta$.

Es **el más usado en RF discreta** por su simplicidad y porque las capacitancias parásitas del transistor se suman a $C_1$ y $C_2$ sin desestabilizar el circuito.

##### Oscilador Hartley

Es el **dual** del Colpitts: **divisor inductivo**. Dos inductores $L_1$ y $L_2$ en serie (o un inductor con toma central) forman el tanque con un capacitor $C$ en paralelo.

$$
f_0 = \frac{1}{2\pi\sqrt{L_{eq}\,C}}, \qquad L_{eq} = L_1 + L_2 + 2M
$$

Donde $M$ es la inductancia mutua si las dos bobinas están acopladas.

Condición de ganancia: $A_v \geq L_1/L_2$.

Ventaja: una sola bobina con derivación. Desventaja: el inductor con toma es más caro y delicado que dos capacitores; las inductancias parásitas son menos predecibles.

##### Oscilador Clapp

Es un **Colpitts mejorado**: se agrega un **tercer capacitor $C_3$ en serie con $L$**. La capacidad efectiva del tanque pasa a ser:

$$
\frac{1}{C_{tank}} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3}
$$

Si se elige $C_3 \ll C_1, C_2$, entonces $C_{tank} \approx C_3$ y:

$$
f_0 \;\approx\; \frac{1}{2\pi\sqrt{L\,C_3}}
$$

> [!tip] Ventaja del Clapp
> Como $C_3$ domina la frecuencia, las **capacitancias parásitas** del transistor (que entran sumadas a $C_1$ y $C_2$) **dejan de influir** sobre $f_0$. El resultado: mucha mayor **estabilidad de frecuencia** que el Colpitts puro, sin perder la simplicidad del divisor capacitivo.

##### Modelo unificado: configuración de tres impedancias (oscilador de tres puntos)

Hartley, Colpitts y Clapp **no son circuitos distintos**: son **el mismo esquema general** con tres impedancias $Z_1$, $Z_2$, $Z_3$ conectadas a los tres terminales del transistor (o amplificador). Lo único que cambia entre ellos es **qué se pone en cada $Z$**.

###### Topología generalizada

Se conecta una impedancia entre cada par de terminales del activo (base/colector/emisor en BJT, o gate/drain/source en FET):

```
              ┌──── Z3 ────┐
              │            │
        ┌─────┤            ├──────┐
        │     B            C     │
        │     │            │     │
       Z1     │   ─────    │    Z2
        │     │  │ TBJ │   │     │
        │     │   ─────    │     │
        │     │     │      │     │
        └─────┴─────E──────┴─────┘
                    │
                   GND
```

- $Z_1$ entre **base y emisor** (entrada).
- $Z_2$ entre **colector y emisor** (salida).
- $Z_3$ entre **base y colector** (realimentación).

###### Condición de oscilación

Sumando reactancias alrededor del lazo y aplicando Barkhausen, la frecuencia de oscilación cumple:

$$
\boxed{\,X_1 + X_2 + X_3 = 0\,}
$$

Y la condición de fase exige que **$Z_1$ y $Z_2$ tengan el mismo tipo de reactancia, y $Z_3$ el opuesto**:

> [!important] Regla del signo
> - Si $Z_1$ y $Z_2$ son **inductivos** ($X>0$), entonces $Z_3$ debe ser **capacitivo** ($X<0$).
> - Si $Z_1$ y $Z_2$ son **capacitivos** ($X<0$), entonces $Z_3$ debe ser **inductivo** ($X>0$).
>
> Esto garantiza que la red de realimentación aporte los $180°$ que faltan para completar el lazo en un amplificador inversor (emisor común / source común).

###### Tabla de configuraciones clásicas

| Configuración               | $Z_1$ (BE)                   | $Z_2$ (CE)                   | $Z_3$ (BC)                              | $f_0$                                                                                  |
| --------------------------- | ---------------------------- | ---------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------- |
| **Hartley**                 | $L_1$                        | $L_2$                        | $C$                                     | $\dfrac{1}{2\pi\sqrt{(L_1+L_2+2M)\,C}}$                                                |
| **Colpitts**                | $C_1$                        | $C_2$                        | $L$                                     | $\dfrac{1}{2\pi\sqrt{L\,\frac{C_1 C_2}{C_1+C_2}}}$                                     |
| **Clapp**                   | $C_1$                        | $C_2$                        | $L$ **en serie con** $C_3$              | $\dfrac{1}{2\pi\sqrt{L\,\left(\frac{1}{C_1}+\frac{1}{C_2}+\frac{1}{C_3}\right)^{-1}}}$ |
| **Sintonizado-sintonizado** | $L_1 \parallel C_1$ (tanque) | $L_2 \parallel C_2$ (tanque) | $C_M$ (Miller del transistor) o nada    | dos tanques en resonancia, acoplados por $C_M$                                         |
| **Armstrong**               | $L_1$                        | $L_2 \parallel C$ (tanque)   | acoplamiento mutuo $M$ (no es $Z$ pura) | $\dfrac{1}{2\pi\sqrt{L_2 C}}$                                                          |

> [!tip] Cómo leer la tabla
> - **Hartley** = L, L, C → divisor inductivo, realimentación capacitiva.
> - **Colpitts** = C, C, L → divisor capacitivo, realimentación inductiva.
> - **Clapp** = C, C, LC serie → Colpitts con un capacitor extra en serie con la bobina que **domina** la frecuencia.
>
> El nombre del oscilador queda determinado **únicamente por la naturaleza de $Z_1$, $Z_2$, $Z_3$**.

###### Por qué funciona la regla del signo

En un amplificador en emisor común, la salida en el colector está **invertida $180°$** respecto a la base. Para completar el lazo a $360°$ necesitamos que la red de tres impedancias **invierta otros $180°$** entre colector y base.

Eso ocurre solamente cuando $Z_1$ y $Z_2$ forman un **divisor** con tensiones de **signo opuesto** en sus extremos respecto al nodo común (emisor), lo cual exige que ambas sean reactancias del **mismo tipo** (las dos $L$ o las dos $C$) y que $Z_3$ sea del **tipo contrario** para cerrar el bucle resonante.

Si se viola esta regla (por ejemplo, dos capacitores y otro capacitor), la red no produce inversión y **no oscila** — solo atenúa.

##### Comparación rápida LC

| Topología | Tanque                           | $\beta$            | Pros                                | Contras                          |
| --------- | -------------------------------- | ------------------ | ----------------------------------- | -------------------------------- |
| Colpitts  | $L$ con divisor $C_1$-$C_2$      | $C_1/C_2$          | Fácil, parásitas absorbidas         | Frecuencia sensible al transistor |
| Hartley   | $C$ con divisor $L_1$-$L_2$      | $L_2/L_1$          | Una sola bobina con toma            | Inductores difíciles de ajustar  |
| Clapp     | Colpitts + $C_3$ en serie con $L$ | $C_1/C_2$         | Muy estable en frecuencia           | Sintonía menos amplia             |
| Armstrong | Bobina con devanado de realimentación | acoplo $M$    | Histórico, simple                   | Acoplo crítico, poco usado hoy   |

#### Alta frecuencia fija: osciladores a cristal

Cuando se necesita una frecuencia **muy estable y precisa** (relojes de microcontroladores, transmisores AM/FM, equipos de medida, GPS), el tanque $LC$ se reemplaza por un **cristal de cuarzo**.

##### Por qué el cristal es distinto

Un cristal de cuarzo tallado y metalizado se comporta eléctricamente como un **resonador mecánico** por el **efecto piezoeléctrico**: una tensión aplicada lo deforma, y su vibración mecánica genera tensión. Su modelo eléctrico equivalente es:

```
       Cs       Ls        Rs
   ──┤├─────⌒⌒⌒⌒⌒───/\/\/─── (rama motional, serie)
                                            
         ────────╫────────       (Cp, capacidad de electrodos, en paralelo)
```

Donde:

- $L_s, C_s, R_s$ = rama **motional** (modela la masa, elasticidad y pérdidas mecánicas).
- $C_p$ = capacidad estática entre electrodos (rama paralela).

Este modelo tiene **dos resonancias muy próximas**:

- **Resonancia serie:** $f_s = \dfrac{1}{2\pi\sqrt{L_s C_s}}$ — impedancia mínima (resistiva, $\approx R_s$).
- **Resonancia paralelo:** $f_p = f_s\sqrt{1 + C_s/C_p}$ — impedancia máxima. Típicamente $f_p$ está unos cientos de ppm por encima de $f_s$.

> [!important] La clave: factor $Q$ enorme
> El cristal tiene $Q$ del orden de $10^4$ a $10^6$, frente a $10^2$–$10^3$ de un tanque $LC$ de buena factura. La estabilidad de frecuencia mejora en proporción: típicamente **1 a 100 ppm**, frente a **0.1 a 1 %** de un $LC$. Esa estabilidad es **mecánica**, intrínseca al material, no depende del circuito.

##### Topologías más usadas

| Topología                | Modo del cristal      | Característica                                                |
| ------------------------ | --------------------- | ------------------------------------------------------------- |
| **Pierce**               | Paralelo              | El más usado en microcontroladores (los dos pines $XTAL_1$/$XTAL_2$). Mínimos componentes externos: el cristal y dos capacitores a tierra. |
| **Miller**               | Paralelo              | Cristal entre puerta-drenador (o base-colector). Histórico.   |
| **Colpitts a cristal**   | Paralelo              | Igual al Colpitts $LC$ pero reemplazando el inductor por el cristal en modo inductivo (entre $f_s$ y $f_p$). |
| **Butler**               | Serie                 | Cristal en modo serie, baja impedancia. Para frecuencias altas (overtone). |

##### Por qué la frecuencia es **fija**

La resonancia del cristal viene determinada por **sus dimensiones físicas** (corte, espesor). No puede sintonizarse libremente. Sí admite un pequeño "pulling" de unos pocos ppm cambiando los capacitores de carga, suficiente para ajustar reloj o aplicar modulación de banda estrecha (FSK), pero no para barridos amplios.

> [!note] Aplicaciones
> - **Microcontroladores y SoCs:** cristal Pierce de 4–32 MHz como reloj principal.
> - **Relojes en tiempo real (RTC):** cristal de 32.768 kHz ($2^{15}$ Hz, divisible exactamente a 1 Hz).
> - **Comunicaciones:** referencias de PLL para sintetizadores de frecuencia.
> - **Equipos de medida:** referencias de tiempo/frecuencia (TCXO, OCXO).

### Osciladores de relajación

Son osciladores **no senoidales** que generan formas de onda periódicas (cuadradas, triangulares, dientes de sierra, pulsos) a partir de la **carga y descarga repetida de un elemento almacenador de energía** (típicamente un capacitor) entre dos niveles de umbral.

> [!info] Idea central
> A diferencia del oscilador senoidal (que vive en régimen **lineal** y obedece Barkhausen), el oscilador de relajación trabaja en régimen **no lineal**: el circuito conmuta abruptamente entre dos estados cuando la tensión del capacitor cruza un umbral. La frecuencia depende del **tiempo de carga RC** y de los **niveles de disparo**, no de una resonancia.

#### Principio de funcionamiento

1. Un capacitor se carga a través de una resistencia hacia una tensión objetivo.
2. Un elemento no lineal con **histéresis** (Schmitt trigger, comparador con realimentación positiva, UJT, lámpara de neón, diodo de avalancha) vigila la tensión del capacitor.
3. Al alcanzar el **umbral superior** $V_{TH}$, el elemento conmuta su salida y obliga al capacitor a descargarse (o cargarse en sentido contrario) hacia el **umbral inferior** $V_{TL}$.
4. Al alcanzar $V_{TL}$, conmuta de nuevo. El ciclo se repite indefinidamente.

La realimentación positiva acelera la conmutación (efecto regenerativo), produciendo flancos rápidos en la salida → forma de onda **cuadrada** o **rectangular**.

#### Forma de onda típica

- **Salida del comparador / Schmitt:** onda **cuadrada** entre $+V_{sat}$ y $-V_{sat}$ (o $V_{CC}$ y $0$).
- **Tensión en el capacitor:** **exponencial troceada** entre $V_{TH}$ y $V_{TL}$. Si la constante RC es mucho mayor que el período, los tramos parecen casi lineales → se aproxima a una **onda triangular**.

#### Topologías clásicas

| Topología                                    | Elemento de histéresis            | Salida                       |
| -------------------------------------------- | --------------------------------- | ---------------------------- |
| **Astable con OPAM** (multivibrador)         | OPAM en modo Schmitt              | Cuadrada + exp. en $C$        |
| **Temporizador 555 en modo astable**         | Dos comparadores + flip-flop SR  | Cuadrada asimétrica           |
| **Oscilador con UJT** (transistor uniunión)  | Resistencia diferencial negativa | Diente de sierra + pulsos    |
| **Oscilador de lámpara de neón / Pearson-Anson** | Ruptura de gas (~80 V)        | Diente de sierra              |
| **Multivibrador con BJT acoplado por RC**    | Saturación / corte de BJT        | Cuadrada                      |

#### Frecuencia de oscilación (caso astable con OPAM)

Para un Schmitt trigger inversor con divisor $R_1, R_2$ que fija los umbrales $V_{TH} = +\beta V_{sat}$ y $V_{TL} = -\beta V_{sat}$, con $\beta = R_2/(R_1+R_2)$, y red RC integradora:

$$
T = 2RC\,\ln\!\left(\frac{1+\beta}{1-\beta}\right) \quad\Rightarrow\quad f_0 = \frac{1}{T}
$$

Donde:

- $R, C$ = resistencia y capacitor de la red de temporización.
- $\beta$ = factor del divisor de realimentación positiva.
- $V_{sat}$ = tensión de saturación del OPAM (cancela en la fórmula).

> [!tip] Caso particular cómodo
> Si se elige $R_1 = R_2$ (es decir, $\beta = 1/2$):
> $$T = 2RC\,\ln(3) \approx 2.197\,RC$$

#### Diferencias frente al oscilador senoidal

| Característica          | Senoidal (RC, LC, cristal)            | Relajación                            |
| ----------------------- | ------------------------------------- | ------------------------------------- |
| Régimen de operación    | Lineal                                | No lineal (conmutación)               |
| Criterio de diseño      | Barkhausen ($|A\beta|=1$, $\angle=0$) | Umbrales de disparo + $RC$            |
| Forma de onda           | Senoidal                              | Cuadrada / triangular / diente sierra |
| Determinante de $f_0$   | Resonancia ($LC$, polos $RC$)         | Constante de tiempo y umbrales        |
| Pureza espectral        | Alta (un solo tono)                   | Baja (rica en armónicos impares)      |
| Estabilidad de frecuencia | Alta (cristal: ppm)                 | Moderada (depende de $V_{sat}$, deriva térmica de $R$, $C$) |

#### Aplicaciones

- **Generación de reloj** en sistemas digitales sencillos (donde no se requiere precisión de cristal).
- **Bases de tiempo** para osciloscopios analógicos (diente de sierra para barrido).
- **Modulación PWM**, control de motores, fuentes conmutadas.
- **Generadores de funciones** (combinando astable + integrador para obtener senoidal aproximada).
- **Convertidores tensión-frecuencia (VCO)** de baja precisión.

> [!note] Conexión con la sesión anterior
> El [[S07-2 Multivibrador astable y generador de onda triangular - ejercicios|astable con OPAM]] que viste en la semana 7 es exactamente un oscilador de relajación: la histéresis del Schmitt fija los umbrales, y la red $RC$ define la frecuencia.

## Bibliografía

- Sedra, A. & Smith, K. (2015). *Microelectronic Circuits* (7.ª ed.). Oxford University Press. — Capítulo de osciladores senoidales y criterio de Barkhausen.
- Boylestad, R. & Nashelsky, L. (2013). *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos* (11.ª ed.). Pearson. — Capítulo de osciladores.
- Schilling, D. & Belove, C. *Circuitos Electrónicos: Discretos e Integrados*. McGraw-Hill. — Tratamiento clásico del criterio de Barkhausen.
- Razavi, B. (2008). *Fundamentals of Microelectronics*. Wiley. — Análisis moderno de osciladores LC y de cristal.
