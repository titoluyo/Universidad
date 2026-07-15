---
title: "Filtros de primer y segundo orden: comparación"
curso: "[[Amplificadores MOC]]"
unidad: 4
semana: 17
orden: 2
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/filtros-activos
  - tema/primer-orden
  - tema/segundo-orden
  - tema/factor-q
  - tema/respuesta-en-frecuencia
date: 2026-07-14
---

## Contexto

Recapitulación comparativa de los dos bloques con los que se construye **cualquier** filtro activo. El detalle de cada uno ya está desarrollado:

- **1.er orden** → [[S14-4 Tema 14 - Filtros de primer orden y diagrama de Bode|S14-4]] (pasivos/activos, $f_c$, Bode).
- **2.º orden** (forma canónica, polos, $Q$) → [[S14-3 Tema 14 - Funcion de transferencia de filtros - polos y ceros|S14-3]].
- Ambos como **factores** del Bode → [[S14-5 Tema 14 - Diagrama de Bode por factores|S14-5]].

Aquí los ponemos **lado a lado**: qué los diferencia, por qué el 2.º orden puede resonar y el 1.er orden no, y cuándo conviene cada uno.

> [!info] Idea de una línea
> El **orden** = número de polos = número de **elementos reactivos independientes** (condensadores $C$ **y/o** bobinas $L$). Cada polo suma $-20\ \text{dB/década}$ de caída y hasta $-90^\circ$ de fase.

---

## 1. ¿Qué fija el "orden"?

El orden $n$ es el **grado del denominador** de la [[S14-1 Tema 14 - Funcion de transferencia|función de transferencia]] $H(s)$, e igual al **número de elementos reactivos independientes** del circuito:

$$H(s) = \frac{N(s)}{D(s)}, \qquad n = \operatorname{grado}\big(D(s)\big) = \text{n.º de polos}$$

Cuanto mayor el orden, **más se parece la respuesta al filtro ideal** (corte vertical), a costa de más componentes y más desfase.

> [!important] Elementos reactivos: condensadores **y** bobinas
> Lo que suma "orden" es **cualquier** elemento que almacena energía, no solo el condensador: cada **$C$** (energía en el campo eléctrico) **o** cada **$L$** (energía en el campo magnético) **independiente** aporta un polo. Por eso un $L$ tiene reactancia $X_L = \omega L$ y un $C$ tiene $X_C = 1/\omega C$: ambos introducen dependencia con la frecuencia.
>
> En estas notas hablamos de **$C$** porque en los **filtros activos con op-amp** casi nunca se usan bobinas: a bajas frecuencias son **grandes, caras, con resistencia parásita y captan interferencia**. El op-amp permite lograr el mismo efecto (incluso resonancia y $Q$ alto) **solo con R y C**. En **filtros pasivos RLC** y en **RF**, en cambio, las bobinas sí se usan y **cuentan igual** para el orden. Así que la frase del profesor es la **general y correcta**; "solo $C$" es el caso particular del filtro activo.

## 2. Filtro de primer orden ($n=1$)

**Un** condensador → **un** polo. Forma canónica (pasa bajo):

$$H(j\omega) = \frac{K}{1 + \dfrac{j\omega}{\omega_0}} \qquad\Longrightarrow\qquad f_c = f_0 = \frac{1}{2\pi RC}$$

- **Pendiente asintótica:** $-20\ \text{dB/década}$ ($= -6\ \text{dB/octava}$).
- **Fase:** de $0^\circ$ a $-90^\circ$ (pasa por $-45^\circ$ en $f_c$).
- **En $f_c$:** caída de $-3\ \text{dB}$ ($|H| = 1/\sqrt2 \approx 0{,}707$).
- **No puede resonar:** con un solo polo real **no existe pico**; no se define $Q$. La respuesta siempre es monótona.

> [!note] Donde
> - $\;K$ = ganancia en la banda de paso
> - $\;\omega_0 = 2\pi f_0$ = frecuencia de corte $[\text{rad/s}]$

## 3. Filtro de segundo orden ($n=2$)

**Dos** elementos reactivos → **dos** polos. Forma canónica (pasa bajo), la misma que en [[S14-3 Tema 14 - Funcion de transferencia de filtros - polos y ceros|S14-3]]:

$$H(j\omega) = \frac{K}{\;1 + \dfrac{1}{Q}\dfrac{j\omega}{\omega_0} + \left(\dfrac{j\omega}{\omega_0}\right)^{2}\;}$$

- **Pendiente asintótica:** $-40\ \text{dB/década}$ (el doble de selectivo).
- **Fase:** de $0^\circ$ a $-180^\circ$ ($-90^\circ$ en $f_0$).
- **Sí puede resonar:** el **factor de calidad $Q$** controla el pico cerca de $\omega_0$.

El término central $\dfrac{1}{Q}$ es el mismo factor $2a$ de [[S14-5 Tema 14 - Diagrama de Bode por factores|S14-5]] con $2a = \dfrac{1}{Q}$, y equivale al **amortiguamiento** $\zeta$:

$$\zeta = \frac{1}{2Q} \qquad (a = \zeta)$$

### 3.1 El papel de $Q$

| $Q$ | Comportamiento | Nombre / uso |
| --- | --- | --- |
| $Q < 0{,}5$ | Sobreamortiguado (polos reales) | Se parece a dos de 1.er orden en cascada |
| $Q = 0{,}5$ | Amortiguamiento crítico | Transición sin pico |
| $Q = 0{,}707$ | Máxima planicie en banda de paso | **Butterworth** (el más usado) |
| $Q > 0{,}707$ | Aparece **pico** de resonancia en $\approx\omega_0$ | Chebyshev / resonadores |
| $Q \to \infty$ | Polos sobre el eje $j\omega$ | **Oscilador** ([[S17-1 Tema 17 - Oscilador puente de Wien - analisis y criterio de Barkhausen|puente de Wien]]) |

> [!tip] Puente con la S17-1
> Un oscilador es el **límite** de un filtro de 2.º orden con $Q\to\infty$: los polos llegan al eje imaginario y el sistema sostiene una senoide por sí mismo. Es el mismo álgebra de polos, llevada al borde de la estabilidad.

## 4. Comparación directa

| Característica | 1.er orden | 2.º orden |
| --- | --- | --- |
| Polos / condensadores | 1 | 2 |
| Pendiente de caída | $-20\ \text{dB/déc}$ | $-40\ \text{dB/déc}$ |
| Fase total | $0^\circ \to -90^\circ$ | $0^\circ \to -180^\circ$ |
| Parámetros | solo $\omega_0$ | $\omega_0$ **y** $Q$ |
| ¿Pico de resonancia? | **No** (siempre monótono) | **Sí** si $Q>0{,}707$ |
| Selectividad | Baja | Alta |
| Topología típica (activo) | Op-amp con 1 $C$ | **Sallen-Key**, MFB |

## 5. Dos de 1.er orden en cascada ≠ un 2.º orden real

Conectar en cascada dos secciones de 1.er orden **sí** da $-40\ \text{dB/déc}$, pero con **polos reales** → equivale a $Q \le 0{,}5$: nunca hay pico ni respuesta plana óptima. Para lograr $Q = 0{,}707$ (Butterworth) o mayor hace falta un **verdadero 2.º orden** con realimentación (Sallen-Key), donde el op-amp "acerca" los polos al eje $j\omega$ y fija $Q$ libremente.

## 6. Diferencias en la práctica

La teoría dice "un polo más"; en el laboratorio la diferencia se siente en **cuánto limpias la señal** frente a **qué problemas te trae hacerlo**.

### 6.1 Rechazo: lo que ganas con el 2.º orden

Una **década** por encima del corte ($10\,f_c$):

- **1.er orden** ($-20\ \text{dB/déc}$): atenúa **×10** en tensión → el ruido queda al **10 %**.
- **2.º orden** ($-40\ \text{dB/déc}$): atenúa **×100** en tensión → el ruido queda al **1 %**.

Por eso para **antialiasing antes de un ADC**, **ripple de fuente conmutada** o **crossovers de audio**, el de 1.er orden "no limpia lo suficiente" y se salta a 2.º orden o más.

### 6.2 Lo que cuesta: inconvenientes del 2.º orden

| En la práctica | 1.er orden | 2.º orden |
| --- | --- | --- |
| Componentes / costo | Mínimo ($R$, $C$, a veces sin op-amp) | Op-amp $+$ 2 $R$ $+$ 2 $C$, más ajuste |
| **Sobrepico / *ringing*** | **Nunca** (respuesta limpia al escalón) | **Sí** si $Q>0{,}707$: oscila antes de asentarse |
| Sensibilidad / deriva | Muy tolerante | $Q$ depende de la precisión de $R$ y $C$; se descalibra |
| Retardo de grupo | Suave y predecible | Puede deformar la onda cerca de $f_c$ |

> [!warning] El *ringing* es el precio temporal
> Ante un **escalón o pulso**, un 2.º orden con $Q$ alto responde con **sobrepico y oscilación amortiguada** antes de estabilizarse. En audio se oye como resonancia; en un sensor o en datos digitales, **deforma el pulso**. El de 1.er orden **jamás** hace esto: sube y baja de forma monótona.

### 6.3 El compromiso de fondo

> [!success] Selectividad ↔ comportamiento temporal
> Más orden = **mejor selectividad** (corte más ideal) pero **peor comportamiento en el tiempo** (más fase, más retardo, riesgo de sobrepico) y **más costo/sensibilidad**. Filtrar mejor en frecuencia se paga en el dominio del tiempo. Por eso $Q=0{,}707$ (**Butterworth**) es el default: banda de paso lo más plana posible **sin** sobrepico.

### 6.4 Regla de decisión

- **1.er orden:** basta una atenuación suave y se prioriza **sencillez y fase mínima** (acoplamientos, desacoplo, filtrado suave de un sensor DC, antialiasing burdo).
- **2.º orden:** se necesita **corte marcado**, **banda de paso plana** o **rechazar algo cercano en frecuencia** (antialiasing serio, fuentes, comunicaciones, audio Hi-Fi).
- **Orden alto (4.º, 6.º…):** no se diseña de una pieza → se **encadenan secciones de 2.º orden** (Sallen-Key), más **una de 1.er orden si $n$ es impar**. El de 1.er orden es el "comodín" para volver impar un diseño.

## Bibliografía

- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos* (filtros activos, orden y pendiente). Pearson.
- Sedra, A. & Smith, K. *Microelectronic Circuits* (second-order filter functions, $Q$ y $\omega_0$, Sallen-Key). Oxford University Press.
