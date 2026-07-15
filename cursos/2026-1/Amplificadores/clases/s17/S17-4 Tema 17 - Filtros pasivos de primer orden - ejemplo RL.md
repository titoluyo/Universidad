---
title: "Filtros pasivos de primer orden: ejemplo RL"
curso: "[[Amplificadores MOC]]"
unidad: 4
semana: 17
orden: 4
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/primer-orden
  - tema/filtro-rl
  - tema/bobina
  - tema/filtros-pasivos
  - tema/respuesta-en-frecuencia
date: 2026-07-14
---

## Contexto

Segundo ejemplo de la idea "**cada elemento reactivo aporta un orden**": aquí el reactivo es una **bobina $L$**, no un condensador. Es el filtro pasivo de 1.er orden en versión **RL**, el gemelo del **RC** ya visto en [[S14-4 Tema 14 - Filtros de primer orden y diagrama de Bode|S14-4]]. Confirma lo que señaló el profesor y quedó en [[S17-2 Tema 17 - Filtros de primer y segundo orden - comparacion|S17-2]]: **una sola bobina → filtro de primer orden**, con caída de $-20\ \text{dB/década}$.

> [!info] De un vistazo
> $L$ en serie, salida sobre $R$ → **pasa bajo** de 1.er orden con corte $\;\omega_0 = \dfrac{R}{L}$.

---

## 1. Teoría: filtro pasivo de 1.er orden

Un filtro **pasivo** usa solo $R$, $L$, $C$ (sin amplificador). Es de **primer orden** cuando tiene **un** elemento reactivo → **un** polo → denominador de grado 1:

$$H(j\omega) = \frac{K}{1 + \dfrac{j\omega}{\omega_0}}$$

- Pendiente asintótica: $-20\ \text{dB/década}$.
- Fase: de $0^\circ$ a $\mp 90^\circ$.
- Corte en $-3\ \text{dB}$ cuando la reactancia iguala a $R$.
- **Ganancia $K \le 1$**: al ser pasivo, atenúa, nunca amplifica.

El reactivo puede ser un **$C$** (caso $RC$, [[S14-4 Tema 14 - Filtros de primer orden y diagrama de Bode|S14-4]]) **o** una **$L$** (caso $RL$, esta nota).

## 2. Ejemplo L-R (pasa bajo)

Circuito del pizarrón: bobina $L$ **en serie** desde $V_i$, y salida $V_o$ tomada **sobre $R$** (a tierra).

### 2.1 Divisor de tensión

La bobina tiene impedancia $Z_L = j\omega L$ (su reactancia es $X_L = \omega L$). Por divisor de tensión entre $Z_L$ y $R$:

$$V_o = \frac{R}{R + Z_L}\,V_i = \frac{R}{R + j\omega L}\,V_i$$

$$\boxed{\ H(j\omega) = \frac{V_o}{V_i} = \frac{R}{R + j\omega L}\ }$$

> [!note] Nota de notación
> En el pizarrón aparece $V_o = \dfrac{V_i\,R}{R + X_L}$. Ahí $X_L = \omega L$ es solo el **módulo** de la reactancia; la impedancia completa lleva la unidad imaginaria, $Z_L = j\omega L$. Para el álgebra compleja (y para separar módulo y fase) hay que conservar la $j$: $\;R + j\omega L$.

### 2.2 Frecuencia de corte

Llevamos $H$ a la forma canónica dividiendo entre $R$:

$$H(j\omega) = \frac{1}{1 + \dfrac{j\omega L}{R}} = \frac{1}{1 + \dfrac{j\omega}{\omega_0}} \qquad\Longrightarrow\qquad \boxed{\ \omega_0 = \frac{R}{L}\ }$$

$$f_0 = \frac{\omega_0}{2\pi} = \frac{R}{2\pi L}$$

Esto coincide con el criterio de $-3\ \text{dB}$: el corte ocurre cuando la **reactancia iguala a la resistencia**, $X_L = R \Rightarrow \omega L = R \Rightarrow \omega_0 = R/L$.

### 2.3 Comportamiento en los extremos

| Frecuencia | La bobina se comporta como… | $V_o$ |
| --- | --- | --- |
| $\omega \to 0$ (DC) | cortocircuito ($X_L = \omega L \to 0$) | $V_o \cong V_i$ (**pasa**) |
| $\omega \to \infty$ | circuito abierto ($X_L \to \infty$) | $V_o \to 0$ (**bloquea**) |

Deja pasar lo **bajo** y bloquea lo **alto** → **pasa bajo**. (La bobina hace lo **opuesto** al condensador: en el $RC$ pasa bajo, el $C$ va en la rama de salida a tierra; aquí es $L$ el que va en serie.)

### 2.4 Completar el pizarrón: módulo y fase paso a paso

El profesor deja la derivación en $V_o = \dfrac{V_i R}{R + jwL}$. Para **terminarla** hay que separar $H$ en **módulo** y **fase**. Se **racionaliza** multiplicando por el conjugado del denominador:

$$H = \frac{R}{R + j\omega L}\cdot\frac{R - j\omega L}{R - j\omega L} = \frac{R(R - j\omega L)}{R^2 + (\omega L)^2} = \underbrace{\frac{R^2}{R^2+(\omega L)^2}}_{\Re(H)} - j\,\underbrace{\frac{R\,\omega L}{R^2+(\omega L)^2}}_{-\Im(H)}$$

De ahí salen las dos curvas que definen el filtro:

$$\boxed{\ |H(\omega)| = \frac{R}{\sqrt{R^2 + (\omega L)^2}} = \frac{1}{\sqrt{1+\left(\omega/\omega_0\right)^2}}\ }$$

$$\boxed{\ \varphi(\omega) = -\arctan\!\left(\frac{\omega L}{R}\right) = -\arctan\!\left(\frac{\omega}{\omega_0}\right)\ }$$

| $\omega$ | $|H|$ | $|H|_{\text{dB}}$ | Fase $\varphi$ |
| --- | --- | --- | --- |
| $\ll \omega_0$ | $\to 1$ | $0\ \text{dB}$ | $\to 0^\circ$ |
| $=\omega_0$ | $1/\sqrt2 \approx 0{,}707$ | $-3\ \text{dB}$ | $-45^\circ$ |
| $\gg \omega_0$ | $\to \omega_0/\omega$ | $-20\ \text{dB/déc}$ | $\to -90^\circ$ |

En $\omega_0$: parte real e imaginaria se **igualan** ($R^2 = (\omega L)^2$), de ahí el módulo $1/\sqrt2$ y la fase exacta de $-45^\circ$.

### 2.5 Ejemplo numérico L-R

Tomemos $R = 1\ \text{k}\Omega$ y $L = 10\ \text{mH}$:

$$\omega_0 = \frac{R}{L} = \frac{1000}{0{,}01} = 10^{5}\ \text{rad/s} \qquad\Longrightarrow\qquad f_0 = \frac{\omega_0}{2\pi} \approx 15{,}9\ \text{kHz}$$

Evaluando en una década por debajo, en el corte y una década por encima:

| $f$ | $\omega/\omega_0$ | $|H|$ | dB | Fase |
| --- | --- | --- | --- | --- |
| $1{,}59\ \text{kHz}$ | $0{,}1$ | $0{,}995$ | $-0{,}04\ \text{dB}$ | $-5{,}7^\circ$ |
| $15{,}9\ \text{kHz}$ ($=f_0$) | $1$ | $0{,}707$ | $-3{,}0\ \text{dB}$ | $-45^\circ$ |
| $159\ \text{kHz}$ | $10$ | $0{,}0995$ | $-20{,}0\ \text{dB}$ | $-84{,}3^\circ$ |

Se ve la firma del 1.er orden: **casi sin atenuación** una década antes, **$-3\ \text{dB}$** justo en $f_0$, y **$-20\ \text{dB}$** (factor $\times 10$) una década después.

## 3. Complemento: constante de tiempo y dominio del tiempo

La misma red $RL$ tiene una **constante de tiempo** $\tau$ que la conecta con su respuesta temporal:

$$\boxed{\ \tau = \frac{L}{R}\ } \qquad\Longrightarrow\qquad \omega_0 = \frac{R}{L} = \frac{1}{\tau}$$

> [!important] Frecuencia y tiempo son la misma información
> El corte $\omega_0 = 1/\tau$ dice que un filtro que **reacciona lento** en el tiempo (τ grande) **corta bajo** en frecuencia, y viceversa. En el ejemplo, $\tau = L/R = 10\ \mu\text{s}$ → $\omega_0 = 1/\tau = 10^5\ \text{rad/s}$, exactamente el corte de arriba.

**Respuesta al escalón** (entrada $V_i$ que salta de $0$ a $V$): la bobina se **opone a los cambios bruscos de corriente**, así que la salida sobre $R$ **no** salta de golpe, sino que crece exponencialmente:

$$v_o(t) = V\left(1 - e^{-t/\tau}\right)$$

Alcanza el $63\%$ en $t=\tau$ y prácticamente el $100\%$ en $5\tau$. Es el reflejo temporal del pasa bajo: **suaviza los flancos** (recorta lo rápido = lo de alta frecuencia). Al no tener elementos que resuenen (es de 1.er orden), **nunca** hay sobrepico — sube monótono, igual que dijimos en [[S17-2 Tema 17 - Filtros de primer y segundo orden - comparacion|S17-2]].

> [!note] Por qué la bobina "inercia" la corriente
> $v_L = L\,\dfrac{di}{dt}$: para cambiar la corriente al instante haría falta $v_L$ infinito. La bobina es a la corriente lo que la masa a la velocidad: se resiste a cambiar. Por eso filtra lo rápido (alta frecuencia) y deja pasar lo lento (baja frecuencia).

## 4. Variante: RL pasa alto (salida sobre $L$)

Si se **intercambian** los elementos —$R$ en serie y salida sobre la **bobina**— se obtiene un **pasa alto**:

$$H(j\omega) = \frac{j\omega L}{R + j\omega L} = \frac{j\omega/\omega_0}{1 + j\omega/\omega_0}, \qquad \omega_0 = \frac{R}{L}$$

Misma frecuencia de corte, pero ahora **bloquea lo bajo y pasa lo alto** (en DC la bobina es un corto → $V_o=0$).

## 5. Dualidad RC ↔ RL

Los dos filtros de 1.er orden dan la **misma forma** $\dfrac{1}{1+j\omega/\omega_0}$; solo cambia **cómo** se arma $\omega_0$:

| | $RC$ pasa bajo | $RL$ pasa bajo |
| --- | --- | --- |
| Reactivo | condensador $C$ | bobina $L$ |
| Salida sobre | $C$ | $R$ |
| Frecuencia de corte | $\omega_0 = \dfrac{1}{RC}$ | $\omega_0 = \dfrac{R}{L}$ |
| Reactancia | $X_C = \dfrac{1}{\omega C}$ | $X_L = \omega L$ |
| Pendiente | $-20\ \text{dB/déc}$ | $-20\ \text{dB/déc}$ |

> [!tip] Por qué en la práctica se prefiere el RC
> Ambos filtran igual, pero la **bobina** es voluminosa, cara, con resistencia parásita y capta interferencia magnética (lo mismo que se dijo en [[S17-2 Tema 17 - Filtros de primer y segundo orden - comparacion|S17-2]] y [[S17-3 Tema 17 - Filtro pasivo RLC de segundo orden y resonancia|S17-3]]). Por eso en baja frecuencia domina el $RC$; el $RL$ aparece sobre todo en **RF** y en etapas de potencia, donde las bobinas son pequeñas y eficientes.

## Bibliografía

- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos* (filtros $RL$/$RC$ de primer orden, frecuencia de corte). Pearson.
- Sedra, A. & Smith, K. *Microelectronic Circuits* (single-time-constant $RL$/$RC$ networks). Oxford University Press.
