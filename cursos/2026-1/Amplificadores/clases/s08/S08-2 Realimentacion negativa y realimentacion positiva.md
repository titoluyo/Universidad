---
title: "Realimentacion negativa y realimentacion positiva"
curso: "[[Amplificadores MOC]]"
unidad: 2
semana: 8
orden: 2
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/realimentacion-negativa
  - tema/realimentacion-positiva
  - tema/barkhausen
  - tema/osciladores
  - tema/histeresis
  - tema/estabilidad
date: 2026-05-11
---

> [!info] Contexto
> En [[S08-1 Amplificadores realimentados]] se dedujo la ecuacion fundamental $A_f = A/(1+A\beta)$ asumiendo que la senal realimentada **se resta** de la entrada. Esa convencion corresponde a la **realimentacion negativa**. Esta nota muestra que la realimentacion puede tambien **sumar** (realimentacion positiva), y que el **signo de $A\beta$** transforma por completo el comportamiento del circuito: de amplificador estable a oscilador o comparador con histeresis.

## Origen del signo: la ecuacion general

Partiendo del lazo cerrado donde la senal de error es $x_i = x_s \pm x_f$:

$$x_o = A(x_s \pm \beta x_o) \;\Rightarrow\; A_f = \frac{x_o}{x_s} = \frac{A}{1 \mp A\beta}$$

El **signo del denominador** define el tipo de realimentacion:

| Signo en la entrada | Denominador | Tipo de realimentacion | Sinonimo |
| ------------------- | ----------- | ---------------------- | -------- |
| $x_i = x_s - x_f$ (resta) | $1 + A\beta$ | **Negativa** | Degenerativa |
| $x_i = x_s + x_f$ (suma) | $1 - A\beta$ | **Positiva** | Regenerativa |

> [!important] Convencion practica
> En la literatura se suele escribir **siempre** $A_f = A/(1+A\beta)$ y absorber el signo en $\beta$: $\beta > 0$ → negativa; $\beta < 0$ → positiva. El comportamiento del circuito depende entonces del **signo y magnitud de $A\beta$**, no del simbolo $\pm$ del diagrama.

## Realimentacion negativa (degenerativa)

Cuando $A\beta > 0$ (y especialmente cuando $A\beta \gg 1$):

$$A_f = \frac{A}{1+A\beta} < A \;\;\;\;\text{(la ganancia DISMINUYE)}$$

### Caracteristicas

- $|A_f| < |A|$: la senal realimentada **resta**, opone, **corrige** el error.
- $A_f$ se estabiliza en $1/\beta$ → depende solo de la red pasiva de realimentacion.
- Aumenta el **ancho de banda** por el factor $(1+A\beta)$.
- Reduce **distorsion**, **ruido interno** y **deriva termica** por el mismo factor.
- Modifica las impedancias de entrada/salida segun la topologia (ver [[S08-1 Amplificadores realimentados]]).

### Donde aparece

- **Cualquier amplificador lineal**: op-amps en configuracion inversora/no inversora, etapas a transistor con resistor de emisor sin desacoplar, etapas multietapa con lazo global.
- Sistemas de control: termostatos, reguladores de voltaje, PLL, lazos de servocontrol.
- **Cualquier circuito que necesite predecibilidad** > ganancia bruta.

> [!example] Ilustracion numerica
> Op-amp con $A = 10^5$ y red $\beta = 0.01$ (no inversor con $R_f = 99 R_1$):
> - $A_f = 10^5/(1 + 10^5 \cdot 0.01) = 10^5/1001 \approx 99.9$.
> - Si $A$ varia un 50% (e.g. otro chip de la misma referencia con $A = 5 \times 10^4$): $A_f = 5\times10^4/501 \approx 99.8$. **Variacion < 0.1%** a pesar del 50% de tolerancia en $A$.

## Realimentacion positiva (regenerativa)

Cuando $A\beta > 0$ pero **con signo opuesto al de la mezcla** (i.e. la senal realimentada **suma** en vez de restar):

$$A_f = \frac{A}{1-A\beta}$$

Aparecen **tres regimenes** segun el valor de $A\beta$:

| Condicion | Comportamiento |
| --------- | -------------- |
| $0 < A\beta < 1$ | $A_f > A$: la ganancia **aumenta** pero el circuito sigue siendo estable. Util ocasionalmente para "boost" de ganancia o linealizacion. |
| $A\beta = 1$ | $A_f \to \infty$: ganancia infinita. Una perturbacion infinitesimal a la entrada produce salida finita → **oscilacion sostenida**. |
| $A\beta > 1$ | El sistema es **inestable**: la salida crece hasta saturar contra los rieles de alimentacion. Util para **circuitos biestables** (latch, Schmitt trigger). |

### Caracteristicas

- La senal realimentada **refuerza** el error → el sistema **amplifica su propia salida**.
- No corrige distorsion, **la amplifica**.
- La impedancia de entrada puede crecer mas alla de $Z_{in}(1+A\beta)$, o incluso volverse **negativa** (efecto Miller invertido).
- **No es deseable en amplificadores**, pero es **indispensable** en:
    - **Osciladores** (Wien, Colpitts, Hartley, cristal, RC con desplazamiento de fase).
    - **Comparadores con histeresis** (Schmitt trigger, visto en S07-1).
    - **Multivibradores** (astable, monoestable, biestable / flip-flop).
    - **Generadores de onda no senoidal** (triangular, cuadrada, diente de sierra).

> [!example] Comparador con histeresis (Schmitt trigger)
> En el comparador de S07, una pequena fraccion de $v_o$ se devuelve a la entrada **no inversora** via un divisor resistivo: $\beta = R_1/(R_1+R_2)$. Como $A_{ol}$ del op-amp es muy grande, $A\beta \gg 1$ y el circuito tiene **dos estados estables** ($+V_{sat}$ y $-V_{sat}$). La salida solo conmuta cuando la entrada cruza los **umbrales** $\pm \beta V_{sat}$, dando inmunidad al ruido.

## Criterio de Barkhausen (condicion de oscilacion)

Un circuito con realimentacion oscila **sostenidamente y de forma senoidal** cuando, a alguna frecuencia $\omega_0$, se cumplen simultaneamente las dos condiciones de Barkhausen:

$$\boxed{|A(\omega_0)\,\beta(\omega_0)| = 1}$$

$$\boxed{\angle\,[A(\omega_0)\,\beta(\omega_0)] = 0° \;\text{(o multiplo de}\; 360°)}$$

Es decir: la **ganancia de lazo** tiene magnitud unitaria y fase cero. La senal recorre el lazo y vuelve **identica** a si misma, autoregenerandose.

### Interpretacion fisica

- Si $|A\beta| > 1$ a la frecuencia donde la fase es $0°$: la amplitud crece exponencialmente hasta que **la no linealidad** (saturacion) reduce la ganancia efectiva. Es por eso que los osciladores reales **arrancan con $|A\beta|$ ligeramente > 1** y se estabilizan en $|A\beta|=1$ por saturacion suave.
- Si $|A\beta| < 1$: cualquier oscilacion decae exponencialmente → no hay oscilacion sostenida.
- Si $|A\beta| = 1$ exacto: oscilacion sostenida ideal (utopia matematica, dificil de mantener sin AGC).

### Aplicacion practica al diseno

En un **amplificador** con realimentacion negativa, hay que **garantizar** que la condicion de Barkhausen **NO se cumpla** dentro del ancho de banda util. Si la fase del lazo llega a $-180°$ (que sumado al $180°$ de la resta da $0°$ total, **realimentacion positiva efectiva**) antes de que $|A\beta|$ caiga por debajo de 1, el amplificador oscila.

> [!important] Margen de fase y margen de ganancia
> El **margen de fase** ($\phi_m$) es cuanto le falta a la fase del lazo para llegar a $-180°$ cuando $|A\beta| = 1$. El **margen de ganancia** ($G_m$, en dB) es cuanto le falta a la magnitud para llegar a $1$ cuando la fase llega a $-180°$. Reglas tipicas: $\phi_m > 45°$ (idealmente $60°$) y $G_m > 6$ dB.

> [!warning] Por que los op-amps llevan compensacion interna
> El 741 y la mayoria de op-amps "compensados" tienen un **condensador interno** ($C_c \approx 30$ pF) que introduce un polo dominante a baja frecuencia. Esto **fuerza** que $|A\beta|$ caiga a 20 dB/decada en toda la banda util, garantizando margen de fase $\geq 45°$ para cualquier $\beta \leq 1$. Por eso un op-amp 741 "se puede usar con cualquier red de realimentacion sin oscilar", a costa de un GBW modesto.

## Comparacion lado a lado

| Caracteristica | Realimentacion **negativa** | Realimentacion **positiva** |
| -------------- | ---------------------------- | ---------------------------- |
| Signo del lazo | $A\beta > 0$ con resta | $A\beta > 0$ con suma |
| Ecuacion | $A_f = A/(1+A\beta)$ | $A_f = A/(1-A\beta)$ |
| Efecto sobre ganancia | **Reduce** por $(1+A\beta)$ | **Aumenta** o **diverge** |
| Estabilidad | Estable (si margen de fase > 0) | Inestable o biestable |
| Ancho de banda | Aumenta por $(1+A\beta)$ | **Disminuye** o se concentra en $\omega_0$ |
| Distorsion | **Reduce** por $(1+A\beta)$ | **Amplifica** |
| Inmunidad al ruido | **Mejora** | **Empeora** (excepto en Schmitt) |
| Comportamiento temporal | Salida sigue a entrada | Salida tiende a saturar o oscilar |
| Aplicacion principal | **Amplificadores lineales** | **Osciladores y comparadores biestables** |
| Ejemplo canonico | Op-amp no inversor / inversor | Schmitt trigger / oscilador Wien |
| Modelo mental | "El circuito **corrige** su error" | "El circuito **refuerza** su error" |

## Cuando una realimentacion negativa se vuelve positiva

Todo amplificador real tiene **polos** que introducen desfase creciente con la frecuencia. La realimentacion **es negativa en DC** (donde la fase de $A$ es $0°$ o $180°$ controlado), pero a alta frecuencia el desfase adicional del propio amplificador puede llevar la fase total del lazo a $180°$ → lo que era resta se convierte en suma → **realimentacion positiva efectiva**.

Si en esa frecuencia $|A\beta| \geq 1$, el circuito **oscila espontaneamente** aunque haya sido diseñado como amplificador. Patologias comunes:

- Lineas de alimentacion mal desacopladas → realimentacion via $V_{CC}$.
- Capacitancias parasitas entre salida y entrada inversora.
- Cables largos con su inductancia / capacitancia distribuida.
- Carga capacitiva en la salida del op-amp (introduce un polo extra).

> [!example] Sintomas tipicos de oscilacion parasita
> - Onda senoidal limpia superpuesta a la salida deseada, frecuencia tipicamente entre 100 kHz y varios MHz.
> - Consumo de corriente anomalamente alto.
> - El amplificador "funciona bien con la sonda del osciloscopio" (la capacitancia de la sonda cambia los polos) y mal sin ella, o viceversa.
> - Remedios: condensador de compensacion adicional, snubber RC en la salida, mejor ruteo, perlas de ferrita en la alimentacion.

## Realimentacion positiva controlada en amplificadores

En algunos diseños se mezclan ambos tipos a proposito:

- **Bootstrap**: una pequena fraccion de realimentacion positiva eleva la impedancia de entrada de etapas a BJT mas alla de la que daria la realimentacion negativa sola.
- **Compensacion de carga**: en etapas de salida clase AB, una rama positiva compensa caidas de tension del seguidor.
- **Osciladores con AGC**: la ganancia se ajusta dinamicamente para mantener $|A\beta| = 1$ exacto y producir senoidal limpia (e.g. Wien con termistor o JFET como resistor variable).

La regla general: **realimentacion positiva ES util**, siempre que se mantenga $|A\beta| < 1$ a las frecuencias donde **no** se desea oscilar.

## Sintesis

- **Negativa** = el circuito **se opone** a su propia salida → amplificacion estable, predecible, lineal.
- **Positiva** = el circuito **refuerza** su propia salida → biestabilidad (Schmitt), oscilacion (osciladores) o saturacion (latch).
- Ambas comparten la misma ecuacion general; lo que cambia es el **signo de $A\beta$** (o equivalentemente, la fase del lazo).
- Barkhausen ($|A\beta|=1$, $\angle A\beta = 0°$) es la **frontera**: por debajo, amplificador; encima, oscilador.

## Bibliografia

- Sedra, A. & Smith, K. *Microelectronic Circuits* (7ma ed.), Cap. 10 — Feedback (secs. sobre estabilidad y oscilacion). Oxford University Press.
- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*, Cap. 14 — Realimentacion y circuitos osciladores (secs. 14.3-14.5). Pearson.
- Kuphaldt, T. *Lessons in Electric Circuits, Volume III — Semiconductors*, Cap. 8.12 — Positive Feedback. LibreTexts. [enlace](https://espanol.libretexts.org/Vocacional/Tecnologia_Electronica/Libro:_Circuitos_Electricos_III_-_Semiconductores_(Kuphaldt)/08:_Amplificadores_Operacionales/8.12:_Retroalimentaci%C3%B3n_positiva)
- Wikipedia. *Barkhausen stability criterion*. [enlace](https://en.wikipedia.org/wiki/Barkhausen_stability_criterion)
- Schmiegelow, C. T. (UBA). *Realimentacion positiva; comparadores y osciladores de relajacion*. [enlace](http://users.df.uba.ar/schmiegelow/materias/laboe_2019c2/guias/P3-RealimentacionPositiva.pdf)
- Sanchez, R. *Amplificador operacional con histeresis*. [enlace](http://rubensm.com/amplificador-operacional-con-histeresis/)
