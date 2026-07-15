---
title: "Multivibrador astable y generador de onda triangular - ejercicios resueltos"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 7
orden: 2
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tipo/ejercicio
  - tema/multivibrador-astable
  - tema/generador-onda-triangular
  - tema/oscilador
  - tema/integrador
  - tema/diseno-de-circuitos
date: 2026-05-04
---

> [!info] Continuacion
> Esta nota desarrolla problemas de **diseno y analisis** de generadores de funcion sin entrada (osciladores RC con op-amp). Teoria correspondiente en [[S06-1 Amplificadores lineales y no lineales#4. Generadores de funcion|S06-1 sec. 4]].

## Resumen rapido de formulas

### Multivibrador astable simetrico

```
             R              Rf
       +---[===]---+    +--[===]--+
       |           |    |         |
       |       (-) +----+         |
       |            \             |
       |             >----+------ Vo
       |            /     |
       |       (+) +------+
       |           |      |
       +---||------+     R1
            C       |     |
           GND     GND   GND
```

Definiendo $\beta = \dfrac{R_1}{R_1+R_f}$ (factor de realimentacion positiva):

$$\boxed{T = 2RC \ln\left(\frac{1+\beta}{1-\beta}\right), \quad f = \frac{1}{T}}$$

Caso particular $R_1 = R_f$ ($\beta = 0.5$):

$$T = 2RC \ln(3) \approx 2.197\,RC, \quad f \approx \frac{1}{2.2\,RC}$$

### Generador de onda triangular (Schmitt + integrador)

```
   Schmitt no inversor      Integrador
  +Vsat / -Vsat              -1/(RC) integral
   ┌─────────┐               ┌─────────┐
   │   U1    │── Vs ──[R]───│   U2    │── Vo (triangular)
   │         │               │  C en  │
   └─────────┘               │  realim│
        ↑                    └─────────┘
        │                          │
        └──────────────────────────┘
            (realimentacion)
```

Frecuencia y amplitud de la triangular:

$$f = \frac{R_2}{4 R_1 R C}, \quad V_{tri,pp} = 2 V_{sat} \cdot \frac{R_1}{R_2}$$

donde $R_1, R_2$ son los resistores del Schmitt no inversor y $R, C$ los del integrador.

---

## Ejercicio 1 (Cantabria A.IV.5): Calcular f del multivibrador con 741

**Enunciado.** Calcular la frecuencia de oscilacion del multivibrador astable de la figura. Datos: $V_{cc} = 12$ V (entonces $V_{sat} \approx 10.5$ V), $R_1 = R_2 = 100$ k$\Omega$, $R = 120$ k$\Omega$, $C = 47$ nF.

```
              R2 = 100k
       +-----[===]-----+
       |               |
       |          (-) \|
  Vi --+---------------+
                       >---- Vo
                  (+) /|
                       |
                      R1 = 100k
                       |
   Vi -[R=120k]--+-----+
                |
               [C=47n]
                |
               GND
```

(Topologia inversora: $V_{in}$ se acopla al inversor por la red RC; el divisor $R_1, R_2$ va al no inversor.)

### Analisis

Cuando $V_o = +V_{sat}$:
- El nodo (+) tiene $V_+ = +V_{sat}\cdot \frac{R_1}{R_1+R_2} = +V_{sat}/2$ (porque $R_1 = R_2$)
- $C$ se carga a traves de $R$ buscando llegar a $+V_{sat}$
- Cuando $V_C$ alcanza $+V_{sat}/2$, el comparador conmuta a $-V_{sat}$

Por simetria, en el siguiente semiperiodo $V_C$ debe ir desde $+V_{sat}/2$ hasta $-V_{sat}/2$, manejado por el voltaje objetivo $-V_{sat}$.

### Calculo del periodo

La carga del capacitor desde un valor inicial $V_i$ hacia un valor final $V_f$ es:

$$V_C(t) = V_f + (V_i - V_f) e^{-t/RC}$$

Para el semiperiodo $T/2$ (transicion de $-\beta V_{sat}$ a $+\beta V_{sat}$ con $V_f = +V_{sat}$):

$$\beta V_{sat} = V_{sat} + (-\beta V_{sat} - V_{sat}) e^{-T/(2RC)}$$

Despejando:

$$e^{-T/(2RC)} = \frac{V_{sat}(1-\beta)}{V_{sat}(1+\beta)} = \frac{1-\beta}{1+\beta}$$

$$\frac{T}{2} = RC \ln\left(\frac{1+\beta}{1-\beta}\right) \Rightarrow T = 2RC\ln\left(\frac{1+\beta}{1-\beta}\right)$$

### Sustitucion numerica

Con $\beta = 0.5$:

$$T = 2 \times 120\,\text{k}\Omega \times 47\,\text{nF} \times \ln\left(\frac{1.5}{0.5}\right) = 2 \times 5.64\,\text{ms} \times \ln(3)$$

$$T = 11.28 \times 1.0986 = 12.39\,\text{ms}$$

$$\boxed{f = \frac{1}{T} = 80.7\,\text{Hz}}$$

### Verificacion con la formula simplificada ($R_1 = R_f$)

$$f = \frac{1}{2.2 \times RC} = \frac{1}{2.2 \times 120\text{k} \times 47\text{n}} = \frac{1}{0.01241} = 80.6\,\text{Hz} \checkmark$$

### Formas de onda (cualitativo)

```
   Vc (sobre el capacitor)              Vo (salida cuadrada)
    |                                     |
+βVsat|     ___    ___    ___       +Vsat |____    ____    ____
    |    /   \  /   \  /   \             |    |  |    |  |    |
    |   /     \/     \/     \            |    |  |    |  |    |
    +--+-------+------+------+--- t  ----+----+--+----+--+----+--- t
    |  /\     /\      /\                 |       |       |
    |     \  /  \    /                   |       |       |
-βVsat|     \/    \  /                  -Vsat    |_______|________
    |              \/
```

---

## Ejercicio 2: Diseno de un astable de 1 kHz

**Enunciado.** Disenar un multivibrador astable basado en op-amp 741 con:
- Frecuencia: $f = 1$ kHz
- Duty cycle: 50% (simetrico)
- Alimentacion $\pm 12$ V → $V_{sat} = \pm 10.5$ V
- Amplitud de salida: $\pm V_{sat}$

### Procedimiento

1. **Elegir $\beta$:** valores tipicos son $\beta = 0.5$ ($R_1 = R_f$) por simplicidad. Esto da $T = 2.2\,RC$.

2. **Calcular $RC$:**

$$RC = \frac{T}{2.2} = \frac{1\,\text{ms}}{2.2} = 454.5\,\mu\text{s}$$

3. **Elegir $C$ tipico:** $C$ entre $10$ nF y $1$ $\mu$F (capacitores ceramicos/film de bajo ESR). Eligiendo $C = 10$ nF:

$$R = \frac{454.5\,\mu\text{s}}{10\,\text{nF}} = 45.45\,\text{k}\Omega \approx 47\,\text{k}\Omega \text{ (E12)}$$

4. **Resistores del Schmitt:** $R_1 = R_f = 10$ k$\Omega$ (cualquier par igual sirve).

### Verificacion

$$f = \frac{1}{2.2 \times 47\text{k} \times 10\text{n}} = \frac{1}{1.034\,\text{ms}} = 967\,\text{Hz}$$

Error: 3.3% por aproximacion de $R$ a valor estandar. Aceptable.

> [!success] Componentes finales
> $C = 10$ nF, $R = 47$ k$\Omega$, $R_1 = R_f = 10$ k$\Omega$. Op-amp: 741 (con $\pm 12$ V).

> [!warning] Limitacion de slew rate del 741
> El 741 tiene slew rate $SR = 0.5$ V/$\mu$s. Para $V_o$ cuadrada que conmuta entre $\pm 10.5$ V (transicion total $\Delta V = 21$ V), el tiempo de subida es:
>
> $$t_r = \frac{\Delta V}{SR} = \frac{21}{0.5} = 42\,\mu\text{s}$$
>
> A 1 kHz ($T = 1$ ms), $t_r$ es el 4.2% del periodo → la onda se ve claramente cuadrada.
>
> Pero a **10 kHz** ($T = 100$ $\mu$s), $t_r$ seria casi la mitad del periodo → la onda se distorsiona en forma triangular. Para frecuencias > 5 kHz usar op-amps mas rapidos (TL081, $SR = 13$ V/$\mu$s).

---

## Ejercicio 3 (Cantabria A.IV.7): Astable con compensacion termica

**Enunciado.** En el multivibrador de la figura los **diodos $D_1$ y $D_2$** en la realimentacion fijan el umbral del Schmitt independiente de $V_{sat}$. Su voltaje varia con la temperatura segun $V_d(T) = V_{do} + TC(T - T_o)$ con $V_{do} = 0.7$ V, $TC = -2$ mV/$°$C, $T_o = 25°$C. Encontrar la expresion del periodo y calcular $f$ a $T = 0°, 25°, 50°, 100°$C. Datos: $V_{cc} = 12$ V, $R = 10$ k$\Omega$, $C = 0.1\,\mu$F.

```
        D1 (cathode hacia +)
   |---|<|---+
             |    R (realim. positiva)
             +---[===]----+
             |            |
        D2   |       (-) \|
   |---|>|---+            |
                          >---- Vo
                     (+) /|
                          |
                         [R]
                          |
        Vc ---+----+      |
              |    |     GND
            [R=10k][C]
              |    |
             GND  GND
```

(Los diodos en serie con la realimentacion limitan el voltaje del nodo (+) a $\pm V_d$ en lugar de $\pm V_{sat}$.)

### Modelo

Cuando $V_o = +V_{sat}$, el diodo $D_2$ conduce y fija $V_+ = +V_d$ (en lugar de $+\beta V_{sat}$). Cuando $V_o = -V_{sat}$, $D_1$ conduce y fija $V_- = -V_d$. Esto hace que **el umbral de conmutacion sea $\pm V_d$**.

El capacitor se carga a traves de $R$ desde $-V_d$ hasta $+V_d$, buscando $V_o = +V_{sat}$:

$$V_d = V_{sat} + (-V_d - V_{sat}) e^{-T/(2RC)}$$

$$\frac{T}{2} = RC\ln\left(\frac{V_{sat} + V_d}{V_{sat} - V_d}\right)$$

$$\boxed{T(V_d) = 2RC\ln\left(\frac{V_{sat} + V_d}{V_{sat} - V_d}\right)}$$

### Calculo a varias temperaturas

$RC = 10\,\text{k}\Omega \times 0.1\,\mu\text{F} = 1\,\text{ms}$, $V_{sat} = 10.5$ V.

$$V_d(T) = 0.7 + (-0.002)(T - 25) = 0.75 - 0.002\,T \text{ [V con T en °C]}$$

| $T$ ($°$C) | $V_d$ (V) | $\dfrac{V_{sat}+V_d}{V_{sat}-V_d}$ | $\ln(\cdot)$ | $T_{periodo}$ (ms) | $f$ (Hz) |
| ---------- | --------- | -------------- | ------------ | ------------------ | -------- |
| 0          | 0.750 | $\dfrac{11.25}{9.75} = 1.1538$ | 0.1431 | 0.286 | **3494** |
| 25         | 0.700 | $\dfrac{11.20}{9.80} = 1.1429$ | 0.1335 | 0.267 | **3744** |
| 50         | 0.650 | $\dfrac{11.15}{9.85} = 1.1320$ | 0.1240 | 0.248 | **4032** |
| 100        | 0.550 | $\dfrac{11.05}{9.95} = 1.1106$ | 0.1048 | 0.210 | **4768** |

> [!warning] Conclusion
> Aunque los diodos **estabilizan los umbrales contra variaciones de $V_{sat}$**, todavia introducen una sensibilidad termica via $V_d(T)$. La frecuencia varia 36% entre 0°C y 100°C — inaceptable para osciladores de precision.
>
> Para osciladores estables: usar **referencia de voltaje precisa** (Zener compensado) o **integrado dedicado** (NE555, ICL8038, XR2206).

### Comparacion con el caso "ideal" sin diodos ($\beta = 0.5$)

Sin diodos, $T = 2 RC \ln 3 = 2 \times 1\,\text{ms} \times 1.0986 = 2.197$ ms → $f = 455$ Hz, **independiente de $V_d$**.

→ Los diodos elevaron la frecuencia ~10x y la hicieron sensible a la temperatura. Es un trade-off: ganan precision en amplitud (umbrales fijos a $\pm 0.7$ V) pero pierden estabilidad en frecuencia.

---

## Ejercicio 4 (Cantabria A.IV.8): Generador de onda triangular

**Enunciado.** Calcular las tensiones $V_o$ (triangular) y $V_s$ (cuadrada) del generador de la figura. Datos: $R_1 = 50$ k$\Omega$, $R_2 = 100$ k$\Omega$, $R = 100$ k$\Omega$, $C = 10$ nF. Caso (a): alimentacion simetrica $V_{cc} = +15$ V, $V_{ee} = -15$ V → $V_{sat} = \pm 13.5$ V. Caso (b): asimetrica $V_{cc} = +15$ V, $V_{ee} = -10$ V → $V_{sat^+} = +13.5$ V, $V_{sat^-} = -8.5$ V.

```
   +-----+ R2=100k +-----+ R    +-----+ C
   |     |---[===]-+--[===]--+--||--+--+
   |     |         |         |      |  |
   |  U1 |         |         | U2  | |  |
   | (Schmitt   <-Vs->     | (integ-|  |
   |  no inv)  |          |  rador)|  |
   |     |     |          |        |  |
   +-----+     |          +--------+--+ Vo (triangular)
   |  ↑        |
   |  |R1=50k  |
   |  +--------+ (realim. positiva del Schmitt: nodo + recibe Vo)
   |
  GND
```

(Corregido: el Schmitt no inversor U1 toma $V_o$ del integrador como entrada al nodo (+) via $R_1$. La salida $V_s$ del Schmitt va al integrador U2.)

### Analisis del Schmitt no inversor (U1)

Umbrales del Schmitt no inversor (con $V_{REF}=0$):

$$V_{UT} = -V_{sat^-}\cdot\frac{R_1}{R_2}, \quad V_{LT} = -V_{sat^+}\cdot\frac{R_1}{R_2}$$

(en no inversor, $V_o$ del Schmitt cambia signo respecto al inversor: $V_{UT}$ ocurre cuando $V_s$ va de negativo a positivo, y la conmutacion al subir $V_o$ del integrador requiere $V_o > V_{UT}$.)

Reescribiendo con magnitudes:

- Si $V_s = +V_{sat^+}$, conmuta a $-V_{sat^-}$ cuando $V_o$ del integrador alcanza $V_{LT} = -V_{sat^+}\cdot R_1/R_2$
- Si $V_s = -V_{sat^-}$, conmuta a $+V_{sat^+}$ cuando $V_o$ del integrador alcanza $V_{UT} = +|V_{sat^-}|\cdot R_1/R_2$

### Caso (a): $\pm 15$ V, $V_{sat} = \pm 13.5$ V

$$V_{UT} = +13.5 \times \frac{50}{100} = +6.75\,\text{V}$$

$$V_{LT} = -13.5 \times \frac{50}{100} = -6.75\,\text{V}$$

$$V_{tri,pp} = 13.5\,\text{V}, \quad V_{tri,amp} = \pm 6.75\,\text{V}$$

**Periodo:**

El integrador con $V_s = +V_{sat}$ produce pendiente:

$$\frac{dV_o}{dt} = -\frac{V_s}{RC} = -\frac{13.5}{100\text{k} \times 10\text{n}} = -\frac{13.5}{1\,\text{ms}} = -13500\,\text{V/s}$$

Tiempo para ir de $V_{UT} = +6.75$ V a $V_{LT} = -6.75$ V (caida de 13.5 V):

$$t_{semi} = \frac{13.5}{13500} = 1\,\text{ms}$$

Por simetria, $T = 2 \times 1\,\text{ms} = 2$ ms → $f = 500$ Hz.

> [!success] Caso (a) — simetrico
> $V_o$ (triangular): $\pm 6.75$ V, frecuencia 500 Hz
> $V_s$ (cuadrada): $\pm 13.5$ V, mismo 500 Hz, **desfasada 90°** respecto a triangular

### Caso (b): asimetrico $V_{cc} = +15$ V, $V_{ee} = -10$ V

Con $V_{sat^+} = +13.5$ V y $V_{sat^-} = -8.5$ V:

$$V_{UT} = -V_{sat^-}\cdot\frac{R_1}{R_2} = +8.5 \times 0.5 = +4.25\,\text{V}$$

$$V_{LT} = -V_{sat^+}\cdot\frac{R_1}{R_2} = -13.5 \times 0.5 = -6.75\,\text{V}$$

→ La triangular es **asimetrica**: pico positivo $+4.25$ V, pico negativo $-6.75$ V.

**Pendientes (asimetricas):**

- Subiendo (cuando $V_s = -V_{sat^-} = -8.5$ V): pendiente $= -(-8.5)/RC = +8500$ V/s
- Bajando (cuando $V_s = +V_{sat^+} = +13.5$ V): pendiente $= -13.5/RC = -13500$ V/s

**Tiempos:**

- Subida (de $-6.75$ a $+4.25$, $\Delta V = 11$ V): $t_1 = 11/8500 = 1.294$ ms
- Bajada (de $+4.25$ a $-6.75$, $\Delta V = 11$ V): $t_2 = 11/13500 = 0.815$ ms

$$T = t_1 + t_2 = 2.108\,\text{ms} \Rightarrow f = 474\,\text{Hz}$$

**Duty cycle de la cuadrada $V_s$:**

$$D = \frac{t_1}{T} = \frac{1.294}{2.108} = 61.4\%$$

> [!warning] Caso (b) — asimetria
> $V_o$ (triangular): pico-pico $11$ V, no centrada en 0 (rango $-6.75$ a $+4.25$ V)
> $V_s$ (cuadrada): asimetrica, pulso positivo 0.815 ms, pulso negativo 1.294 ms (duty 38.6% / 61.4%)

### Diagrama temporal (caso a, simetrico)

```
       Vo (triangular, salida del integrador)
       |
  +6.75|       /\        /\        /\
       |      /  \      /  \      /  \
       |     /    \    /    \    /    \
   0   +----+------+--+------+--+------+----- t
       |   /        \/        \/        \
       |  /                              
  -6.75|/__________
       
       Vs (cuadrada, salida del Schmitt)
       |
  +13.5|________      ________      ____
       |        |    |        |    |
       |        |    |        |    |
   0   +--------+----+--------+----+----- t
       |        |    |        |    |
       |        |    |        |    |
  -13.5|        |____|        |____|
                  ↑         ↑
                  |         |
              (justo cuando Vo cruza el umbral, Vs conmuta)
```

> [!note] Relacion de fase
> La cuadrada $V_s$ conmuta **exactamente** cuando $V_o$ alcanza un pico (umbral del Schmitt). Por eso aparenta estar 90° adelantada — es un comportamiento clasico del par integrador-comparador.

---

## Ejercicio 5: Generador de onda triangular de frecuencia ajustable

**Enunciado.** Modificar el circuito del Ejercicio 4 para que la frecuencia sea ajustable entre 100 Hz y 1 kHz mediante un potenciometro $P$, manteniendo la amplitud constante.

### Estrategia

La frecuencia depende de $f = R_2 / (4 R_1 R C)$. La forma mas simple de hacerla ajustable sin afectar la amplitud (que depende solo de $R_1/R_2$) es **variar $R$** del integrador.

Rango: $f_{max}/f_{min} = 10$ → $R_{min}/R_{max} = 1/10$.

Con $C = 10$ nF, $R_1 = 50$ k, $R_2 = 100$ k, $V_{sat} = \pm 13.5$ V:

$$f = \frac{R_2}{4 R_1 R C} = \frac{100\text{k}}{4 \times 50\text{k} \times R \times 10\text{n}} = \frac{50}{R}\,\text{[con } R \text{ en } \Omega]$$

Para $f = 100$ Hz: $R = 500$ k$\Omega$
Para $f = 1000$ Hz: $R = 50$ k$\Omega$

### Implementacion: $P + R_{fija}$

Para evitar que $R \to 0$ (lo cual saturaria el integrador), poner $R_{fija} = 47$ k$\Omega$ en serie con un pot de $P_{max} = 470$ k$\Omega$:

- Pot al minimo: $R = 47$ k$\Omega$ → $f = 1064$ Hz
- Pot al maximo: $R = 47 + 470 = 517$ k$\Omega$ → $f = 96.7$ Hz

### Verificacion en los extremos

$$f_{max} = \frac{50}{47\text{k}} = 1.064\,\text{kHz} \approx 1\,\text{kHz} \checkmark$$

$$f_{min} = \frac{50}{517\text{k}} = 96.7\,\text{Hz} \approx 100\,\text{Hz} \checkmark$$

> [!success] Generador VCO simple
> Reemplazando el potenciometro por un transistor JFET o un MOSFET en region triodo (cuya $R_{DS,on}$ depende de $V_{GS}$), se obtiene un **VCO** (oscilador controlado por voltaje) — base de los moduladores FM y los sintetizadores de musica.

---

## Resumen comparativo de osciladores RC con op-amp

| Tipo | Forma de onda | Formula de f | Estabilidad |
| ---- | ------------- | ------------ | ----------- |
| Astable simetrico ($\beta = 0.5$) | Cuadrada | $f \approx 1/(2.2 RC)$ | Buena (depende solo de R, C) |
| Astable con diodos | Cuadrada | $f$ depende de $V_d(T)$ | Mala termicamente |
| Schmitt + integrador | Cuadrada + triangular | $f = R_2 / (4 R_1 R C)$ | Excelente (no depende de $V_{sat}$) |
| Wien-bridge + AGC | Senoidal | $f = 1/(2\pi RC)$ | Muy buena (con AGC) |
| Cristal de cuarzo | Senoidal | $f$ del cristal | Optima (1 ppm) |

## Bibliografia

- Coughlin, R. & Driscoll, F. *Operational Amplifiers and Linear Integrated Circuits* (6a ed.). Prentice Hall. Cap. 8 (osciladores).
- Sedra, A. & Smith, K. *Microelectronic Circuits* (7a ed.). Oxford University Press. Cap. 18, secs. 18.6-18.7.
- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos* (10a ed.). Pearson. Cap. 14, sec. 14.5-14.6.
- Universidad de Cantabria. *Electronica Basica - Hoja de problemas A.IV* (Probs A.IV.5, A.IV.7, A.IV.8). OCW. https://ocw.unican.es/
