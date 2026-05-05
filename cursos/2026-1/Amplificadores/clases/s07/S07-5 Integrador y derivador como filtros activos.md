---
title: "Integrador y derivador como filtros activos"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 7
orden: 5
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/integrador
  - tema/derivador
  - tema/filtro-pasa-bajos
  - tema/filtro-pasa-altos
  - tema/respuesta-en-frecuencia
  - tema/diagrama-de-bode
date: 2026-05-04
---

> [!info] Doble identidad
> Las configuraciones **integrador** y **derivador** del op-amp ya fueron analizadas en el dominio temporal en [[S04-1 Aplicaciones lineales del amplificador operacional#7. Amplificador derivador|S04-1 secs. 7-8]]. En esta nota se las revisita en el **dominio frecuencial**: alli se ven como **filtros activos** de primer orden.

## Respuesta corta

> [!success] Equivalencia
> | Operacion en tiempo | Equivalente en frecuencia |
> | ------------------- | ------------------------- |
> | **Integrador** $V_o = -\dfrac{1}{RC}\int V_{in}\,dt$ | **Filtro pasa-bajos** activo de 1er orden |
> | **Derivador** $V_o = -RC\,\dfrac{dV_{in}}{dt}$ | **Filtro pasa-altos** activo de 1er orden |

La razon es la dualidad entre derivada/integral en tiempo y multiplicacion/division por $j\omega$ en frecuencia:

$$\frac{d}{dt} \longleftrightarrow j\omega \quad \text{(amplifica altas)}$$

$$\int dt \longleftrightarrow \frac{1}{j\omega} \quad \text{(amplifica bajas)}$$

---

## 1. Integrador = filtro pasa-bajos

### Topologia ideal

```
          R              C
  Vin ---[===]---+------||------+
                 |               |
            (-) \|               |
                 +---------------+ Vo
            (+) /
                 |
                GND
```

### Funcion de transferencia

Por la impedancia de entrada $Z_R = R$ y de realimentacion $Z_C = 1/(sC)$:

$$H(s) = \frac{V_o(s)}{V_{in}(s)} = -\frac{Z_C}{Z_R} = -\frac{1}{sRC}$$

### Respuesta en frecuencia

$$|H(j\omega)| = \frac{1}{\omega RC}$$

$$\angle H(j\omega) = -180° + 90° = -90° \text{ (constante)}$$

### Diagrama de Bode (ideal)

```
   |H(jω)| dB
       |
   +20 |───\
       |    \  -20 dB/dec (pasa-bajos)
     0 |─────\─
       |      \
   -20 |       \
       |        \
   -40 |─────────\─
       +─────+────+─────+────+─── ω (log)
           0.1 ωc  ωc  10ωc 100ωc
       
       ωc = 1/RC (frecuencia donde |H|=1)
```

> [!warning] Problema del integrador puro
> A $\omega = 0$ (DC), $|H| \to \infty$. Cualquier offset DC del op-amp se integra indefinidamente y satura la salida. Por eso el integrador **puro** no es practico.

### Topologia practica (Miller integrator) = filtro pasa-bajos real

Se agrega $R_f$ en paralelo con $C$ para limitar la ganancia DC:

```
          R              C
  Vin ---[===]---+------||------+
                 |       Rf      |
                 +-----[===]-----+
                 |               |
            (-) \|               |
                 +---------------+ Vo
            (+) /
                 |
                GND
```

Funcion de transferencia:

$$H(s) = -\frac{R_f}{R}\cdot\frac{1}{1 + sR_fC}$$

→ **Filtro pasa-bajos** de 1er orden:

$$\boxed{\text{Ganancia DC: } A_0 = -\frac{R_f}{R}, \quad \omega_c = \frac{1}{R_f C}}$$

```
   |H(jω)| dB
       |
   +A0 |─────\
       |  banda \  
       |  pasante \  -20 dB/dec
       |          \
       0 |───────────\─
       +─────────+──+──+──── ω (log)
                 ωc  10ωc
       
       Por debajo de ωc: ganancia constante = A0 (banda pasante)
       Por encima de ωc: caida 20 dB/dec (rechazo)
```

> [!important] Equivalencia exacta
> El **integrador con $R_f$** ES un **filtro pasa-bajos activo** — no es analogia, es la misma cosa con dos nombres:
> - Si $\omega \ll \omega_c$ → comportamiento de **amplificador inversor** ($A = -R_f/R$)
> - Si $\omega \gg \omega_c$ → comportamiento de **integrador** ($A = -1/(sRC)$)
> - En la transicion → 1er orden pasa-bajos clasico

### Ejemplo: filtro pasa-bajos de audio

Diseno: cortar el ruido por encima de 5 kHz manteniendo ganancia 10 (20 dB) en banda audible.

- Ganancia $A_0 = 10$ → $R_f / R = 10$
- $\omega_c = 2\pi \times 5\,\text{kHz} = 31416$ rad/s
- Eligiendo $C = 10$ nF: $R_f = 1/(\omega_c C) = 1/(31416 \times 10^{-8}) = 3.18\,\text{k}\Omega \approx 3.3\,\text{k}\Omega$
- $R = R_f / 10 = 330\,\Omega$

$$f_c = \frac{1}{2\pi R_f C} = \frac{1}{2\pi \times 3.3\text{k} \times 10\text{n}} = 4.82\,\text{kHz} \checkmark$$

---

## 2. Derivador = filtro pasa-altos

### Topologia ideal

```
          C              R
  Vin ---||---+--------[===]---+
              |                 |
         (-) \|                 |
              +-----------------+ Vo
         (+) /
              |
             GND
```

### Funcion de transferencia

$$H(s) = -\frac{Z_R}{Z_C} = -sRC$$

### Respuesta en frecuencia

$$|H(j\omega)| = \omega RC$$

$$\angle H(j\omega) = -180° - 90° = -270° \equiv +90°$$

### Diagrama de Bode (ideal)

```
   |H(jω)| dB
       |
       |          /
   +40 |        /
       |      / +20 dB/dec
   +20 |    /  (pasa-altos)
       |  /
     0 |/______
       +────+────+─────+────+─── ω (log)
        ωc/100  ωc/10   ωc  10ωc
       
       ωc = 1/RC
```

> [!warning] Problema del derivador puro
> A $\omega \to \infty$, $|H| \to \infty$. **Amplifica todo el ruido de alta frecuencia** (un ruido blanco se vuelve ilimitado). Ademas tiene tendencia a oscilar por el cero en $s=0$ que da +90° de fase.

### Topologia practica = filtro pasa-altos de 1er orden

Se agrega $R_1$ en serie con $C$ para limitar la ganancia a alta frecuencia:

```
       R1     C              R
  Vin-[===]--||---+--------[===]---+
                  |                 |
             (-) \|                 |
                  +-----------------+ Vo
             (+) /
                  |
                 GND
```

Funcion de transferencia:

$$H(s) = -\frac{R}{R_1}\cdot\frac{sR_1 C}{1 + sR_1 C}$$

→ **Filtro pasa-altos** de 1er orden:

$$\boxed{\text{Ganancia HF: } A_\infty = -\frac{R}{R_1}, \quad \omega_c = \frac{1}{R_1 C}}$$

```
   |H(jω)| dB
       |               
   +A∞ |        ___________________
       |       /  banda pasante
       |      / +20 dB/dec
       |     /
     0 |____/_____________________
       +───+──+──────+──────+──── ω (log)
        ωc/10 ωc   10ωc
       
       Por debajo de ωc: caida 20 dB/dec (rechazo)
       Por encima de ωc: ganancia constante = A∞
```

> [!important] Equivalencia exacta
> El **derivador con $R_1$** ES un **filtro pasa-altos activo**:
> - Si $\omega \ll \omega_c$ → comportamiento de **derivador** ($A = -sRC$)
> - Si $\omega \gg \omega_c$ → comportamiento de **amplificador inversor** ($A = -R/R_1$)

### Ejemplo: detector de cambios rapidos en sensor

Diseno: detectar cambios en una senal de presion con frecuencias > 100 Hz, rechazar derivas DC y bajas frecuencias.

- Ganancia HF $A_\infty = 5$ → $R/R_1 = 5$
- $\omega_c = 2\pi \times 100\,\text{Hz} = 628$ rad/s
- Eligiendo $C = 100$ nF: $R_1 = 1/(\omega_c C) = 15.9\,\text{k}\Omega \approx 16\,\text{k}\Omega$
- $R = 5 R_1 = 80\,\text{k}\Omega \approx 82\,\text{k}\Omega$

$$f_c = \frac{1}{2\pi \times 16\text{k} \times 100\text{n}} = 99.5\,\text{Hz} \checkmark$$

---

## 3. Comparacion lado a lado

| Aspecto | Integrador (LPF) | Derivador (HPF) |
| ------- | ---------------- | --------------- |
| Topologia | $R$ entrada, $C$ realim. | $C$ entrada, $R$ realim. |
| $H(s)$ ideal | $-1/(sRC)$ | $-sRC$ |
| Pendiente Bode | $-20$ dB/dec | $+20$ dB/dec |
| Fase | $+90°$ (lead inv.) | $-90°$ (lag inv.) |
| Problema ideal | Satura por offset DC | Amplifica ruido HF |
| Solucion practica | $R_f \parallel C$ (= LPF) | $R_1$ serie $C$ (= HPF) |
| Frecuencia caracteristica | $\omega_c = 1/(R_f C)$ | $\omega_c = 1/(R_1 C)$ |
| Ganancia maxima | DC ($A_0 = -R_f/R$) | HF ($A_\infty = -R/R_1$) |

---

## 4. Vision integrada: posicion del polo y cero

| Configuracion | Polos | Ceros |
| ------------- | ----- | ----- |
| Integrador ideal | $s = 0$ (en origen) | --- |
| LPF (integrador con $R_f$) | $s = -1/(R_fC)$ | --- |
| Derivador ideal | --- | $s = 0$ (en origen) |
| HPF (derivador con $R_1$) | $s = -1/(R_1C)$ | $s = 0$ |

> [!summary] Por que la equivalencia es **exacta** y no analogia
> En el plano $s$:
> - Un cero en el origen $\Rightarrow$ deriva la senal
> - Un cero en el origen + un polo a la izquierda $\Rightarrow$ deriva en banda pasante, satura ganancia HF $\Rightarrow$ pasa-altos
> - Un polo en el origen $\Rightarrow$ integra la senal
> - Polo en el origen reemplazado por polo a la izquierda $\Rightarrow$ integra solo a altas frecuencias, ganancia DC finita $\Rightarrow$ pasa-bajos
>
> No hay ninguna diferencia conceptual entre "integrador real" y "filtro pasa-bajos de 1er orden" — son nombres distintos para la **misma funcion de transferencia**.

---

## 5. Filtros de orden superior (preview)

Los integrador/derivador de **1er orden** rechazan a 20 dB/dec, lo que puede ser insuficiente. Cascadeando dos op-amps se obtienen filtros de **2do orden** con 40 dB/dec:

- **Sallen-Key:** topologia simple, no inversora, polos complejos conjugados
- **Multiple-feedback (MFB):** topologia inversora, mas robusta a tolerancias

→ Tema completo en filtros activos (Unidad 2 del curso). Por ahora basta saber que el "integrador con $R_f$" es el bloque mas simple, equivalente a un Sallen-Key sin la red Q.

## Resumen final

> [!success] Mini-tabla mnemonica
> ```
>      Tiempo                 Frecuencia
>      ──────                 ──────────
>      derivar (d/dt)    →    pasa-altos (HPF)
>      integrar (∫dt)    →    pasa-bajos (LPF)
> ```
>
> Ambas configuraciones tienen el problema de ganancia ilimitada (al limite del rango de frecuencias correspondiente) y se "domestican" agregando un componente extra:
> - Integrador → agregar $R_f$ paralelo a $C$ → filtro **pasa-bajos**
> - Derivador → agregar $R_1$ serie con $C$ → filtro **pasa-altos**

## Bibliografia

- Sedra, A. & Smith, K. *Microelectronic Circuits* (7a ed.). Oxford University Press. Cap. 16 (filtros activos).
- Coughlin, R. & Driscoll, F. *Operational Amplifiers and Linear Integrated Circuits* (6a ed.). Prentice Hall. Cap. 11.
- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos* (10a ed.). Pearson. Cap. 14.
- Mancini, R. *Op Amps for Everyone*. Texas Instruments / Newnes (3a ed.). Cap. 16 (active filter design).
