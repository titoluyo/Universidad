---
title: "Filtro pasivo RLC de segundo orden y resonancia física"
curso: "[[Amplificadores MOC]]"
unidad: 4
semana: 17
orden: 3
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/segundo-orden
  - tema/filtro-rlc
  - tema/resonancia
  - tema/factor-q
  - tema/bobina
date: 2026-07-14
---

## Contexto

En [[S17-2 Tema 17 - Filtros de primer y segundo orden - comparacion|S17-2]] vimos que el **orden** lo fija el número de **elementos reactivos independientes** ($C$ **o** $L$), tal como señaló el profesor. Allí trabajamos con filtros **activos** (solo $R$ y $C$). Aquí aterrizamos el caso donde la **bobina aparece de verdad**: el **filtro pasivo RLC**, el ejemplo más limpio de un 2.º orden porque **se ve físicamente de dónde sale la resonancia** — del intercambio de energía entre $L$ y $C$.

> [!info] Por qué es de 2.º orden
> Tiene **dos** elementos que almacenan energía: la bobina $L$ (campo magnético) y el condensador $C$ (campo eléctrico). Dos reactivos independientes → **dos polos** → orden 2 → caída de $-40\ \text{dB/década}$.

---

## 1. El circuito: RLC serie

Una malla con $R$, $L$ y $C$ en serie, excitada por $V_{in}$. Según **dónde tomemos la salida**, obtenemos los tres tipos básicos:

| Salida sobre… | Tipo de filtro |
| --- | --- |
| el **condensador** $C$ | **Pasa bajo** |
| la **bobina** $L$ | **Pasa alto** |
| la **resistencia** $R$ | **Pasa banda** |

Es el mismo denominador para los tres (los **polos** son comunes); cambia el numerador (los **ceros**), igual que se explicó en [[S14-3 Tema 14 - Funcion de transferencia de filtros - polos y ceros|S14-3]].

## 2. Función de transferencia (salida sobre $C$ → pasa bajo)

Por divisor de tensión, con $Z_L = j\omega L$, $Z_C = \dfrac{1}{j\omega C}$:

$$H(s) = \frac{V_C}{V_{in}} = \frac{\dfrac{1}{sC}}{R + sL + \dfrac{1}{sC}} = \frac{1}{s^2 LC + sRC + 1}$$

Dividiendo numerador y denominador entre $LC$ para llevarlo a la **forma canónica** de 2.º orden:

$$\boxed{\ H(s) = \frac{\dfrac{1}{LC}}{\,s^2 + \dfrac{R}{L}\,s + \dfrac{1}{LC}\,} \;=\; \frac{\omega_0^2}{s^2 + \dfrac{\omega_0}{Q}\,s + \omega_0^2}\ }$$

Comparando término a término con la forma estándar de [[S14-3 Tema 14 - Funcion de transferencia de filtros - polos y ceros|S14-3]]:

$$\boxed{\ \omega_0 = \frac{1}{\sqrt{LC}}\ } \qquad\qquad \boxed{\ Q = \frac{\omega_0 L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}\ }$$

> [!note] Donde
> - $\;\omega_0 = 2\pi f_0$ = frecuencia de resonancia $[\text{rad/s}]$
> - $\;Q$ = factor de calidad (adimensional)
> - $\;R,\ L,\ C$ = resistencia, inductancia y capacitancia de la malla

## 3. De dónde sale la resonancia (lo físico)

En la resonancia, las **reactancias de $L$ y $C$ se igualan y se cancelan**:

$$X_L = X_C \;\Longrightarrow\; \omega_0 L = \frac{1}{\omega_0 C} \;\Longrightarrow\; \omega_0^2 = \frac{1}{LC} \;\Longrightarrow\; \boxed{f_0 = \frac{1}{2\pi\sqrt{LC}}}$$

Físicamente, en $\omega_0$ la energía **oscila de ida y vuelta** entre los dos campos:

- La bobina la guarda en su **campo magnético** ($\tfrac12 L i^2$).
- El condensador la guarda en su **campo eléctrico** ($\tfrac12 C v^2$).

Cada semiciclo, $L$ le "pasa" su energía a $C$ y viceversa — un péndulo eléctrico. La **única** pérdida es la que disipa $R$. Por eso:

> [!important] $Q$ mide cuánto "resuena" el circuito
> $$Q = 2\pi\,\frac{\text{energía almacenada}}{\text{energía disipada por ciclo}}$$
> - **$R$ pequeña** → poca pérdida → $Q$ **alto** → pico de resonancia agudo, la energía oscila muchos ciclos antes de apagarse.
> - **$R$ grande** → mucha pérdida → $Q$ **bajo** → sin pico, respuesta amortiguada.
>
> Aquí se ve **físico** lo que en el filtro activo era abstracto: el $Q$ de la [[S17-2 Tema 17 - Filtros de primer y segundo orden - comparacion|S17-2]] es literalmente qué tan poco amortigua $R$ el vaivén $L\leftrightarrow C$.

## 4. Amortiguamiento y comportamiento

El coeficiente de amortiguamiento $\zeta$ (el $a$ de [[S14-5 Tema 14 - Diagrama de Bode por factores|S14-5]], con $2\zeta = 1/Q$):

$$\zeta = \frac{1}{2Q} = \frac{R}{2}\sqrt{\frac{C}{L}}$$

| Condición | $\zeta$ / $Q$ | Respuesta al escalón |
| --- | --- | --- |
| Sobreamortiguado | $\zeta>1$ ($Q<0{,}5$) | Lento, sin oscilar (dos polos reales) |
| Crítico | $\zeta=1$ ($Q=0{,}5$) | Lo más rápido posible sin sobrepico |
| Subamortiguado | $\zeta<1$ ($Q>0{,}5$) | **Sobrepico y *ringing*** (polos complejos) |
| Butterworth | $\zeta=0{,}707$ ($Q=0{,}707$) | Banda plana, sin pico en frecuencia |
| Sin pérdidas | $\zeta=0$ ($R=0$, $Q\to\infty$) | Oscila para siempre → **oscilador** ideal |

> [!tip] Puente con la S17-1
> Con $R\to 0$ ($Q\to\infty$) los polos caen sobre el eje $j\omega$ y el RLC **oscila indefinidamente**: el mismo límite que persigue el [[S17-1 Tema 17 - Oscilador puente de Wien - analisis y criterio de Barkhausen|oscilador puente de Wien]]. La diferencia es que un $LC$ real siempre tiene algo de $R$ y se apaga; el oscilador **repone** esa energía con el amplificador (Barkhausen) para mantener la senoide viva.

## 5. RLC pasivo vs. 2.º orden activo (Sallen-Key)

Ambos producen **la misma $H(s)$** de 2.º orden; la diferencia es **cómo** consiguen la resonancia:

| | RLC pasivo | 2.º orden activo (Sallen-Key) |
| --- | --- | --- |
| Reactivos | $L$ **y** $C$ | dos $C$ (sin bobina) |
| Origen de la resonancia | **Física:** vaivén $L\leftrightarrow C$ | **Sintetizada** por realimentación del op-amp |
| $Q$ lo fija | la relación $R,L,C$ (limitado por $R$ parásita de $L$) | la ganancia y los $R$ del op-amp (ajustable, $Q$ alto fácil) |
| Ganancia | $\le 1$ (pasivo, atenúa) | $>1$ posible (activo, amplifica) |
| Problema práctico | bobina grande, cara, con pérdidas a baja $f$ | necesita alimentación y un op-amp |

Por eso a **baja frecuencia** (audio, instrumentación) se prefiere el **activo sin bobina**, y el **RLC** reina en **RF** y potencia, donde las bobinas son pequeñas y eficientes.

## Bibliografía

- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos* (resonancia serie/paralelo, factor $Q$). Pearson.
- Sedra, A. & Smith, K. *Microelectronic Circuits* (second-order transfer functions, RLC resonance, $\omega_0$ y $Q$). Oxford University Press.
