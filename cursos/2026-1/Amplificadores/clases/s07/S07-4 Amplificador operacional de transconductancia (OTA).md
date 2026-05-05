---
title: "Amplificador operacional de transconductancia (OTA)"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 7
orden: 4
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/ota
  - tema/transconductancia
  - tema/amplificador-controlable
  - tema/vca
  - tema/filtros-sintonizables
date: 2026-05-04
---

> [!info] Op-amps especiales
> Despues de revisar las aplicaciones lineales y no lineales del op-amp **convencional**, el profesor introduce los **op-amps especiales**: el primero es el **OTA** (Operational Transconductance Amplifier).

## Definicion

El **OTA** (Operational Transconductance Amplifier) es un amplificador diferencial cuya salida es una **corriente** proporcional al voltaje diferencial de entrada, en contraste con el op-amp convencional que entrega un **voltaje** a la salida.

| Parametro | Op-amp convencional | OTA |
| --------- | ------------------- | --- |
| Magnitud de salida | Voltaje $V_o$ | Corriente $I_o$ |
| Impedancia de salida | Muy baja (~0 $\Omega$) | Muy alta (M$\Omega$ - G$\Omega$) |
| Modelo basico | $V_o = A_{ol}(V_+ - V_-)$ | $I_o = g_m(V_+ - V_-)$ |
| Parametro principal | Ganancia de voltaje $A_{ol}$ | **Transconductancia** $g_m$ |
| Control externo | No (salvo realim.) | **Si** — via $I_{ABC}$ (corriente de polarizacion) |

> [!important] Idea central del OTA
> La transconductancia $g_m$ del OTA es **ajustable externamente** mediante una corriente de polarizacion $I_{ABC}$ (Amplifier Bias Current). Esto permite construir **amplificadores con ganancia controlable por voltaje/corriente** — base de VCAs, multiplicadores, filtros sintonizables, sintetizadores de musica, etc.

## Modelo del OTA

```
                       I_ABC (control externo)
                          |
                         (modulador de g_m)
                          |
         (+)\ ──────┐     |
             \      |     |
              + ────+─────+────── I_o (salida en corriente)
             /      |     |
         (-)/ ──────┘     |
                          |
                       Tierra
```

Ecuaciones del modelo:

$$\boxed{g_m = K \cdot I_{ABC}}$$

donde $K$ es una **constante caracteristica del IC** (no depende del usuario).

$$I_o = g_m \cdot V_d = g_m (V_+ - V_-)$$

## Fundamento fisico de $K$

> [!info] Derivacion de la transconductancia
> Para un par diferencial bipolar polarizado con corriente de cola $I_{ABC}$, el analisis de pequena senal da:
>
> $$g_m = \frac{I_{ABC}}{2 V_T}$$
>
> donde $V_T = kT/q \approx 26$ mV a 25°C. Sustituyendo:
>
> $$g_m = \frac{I_{ABC}}{2 \times 26\,\text{mV}} = \frac{I_{ABC}}{52\,\text{mV}}$$
>
> → $g_m / I_{ABC} \approx 19.2$ mS/mA $= 19.2\,\mu$S/$\mu$A (valor teorico ideal).

> [!note] Valor practico segun el profesor
> $$K \approx 16\,\mu\text{S}/\mu\text{A}$$
>
> El valor practico (16 vs 19.2 teorico) refleja factores de no idealidad: linealizacion interna por diodos (LM13700 tiene pins de linealizacion que reducen $g_m$ pero aumentan rango de senal), perdida en la cola, etc. Es el valor a usar en problemas de esta clase.

## Carga del OTA: por que se necesita $R_L$

Como la salida del OTA es **alta impedancia** (idealmente fuente de corriente), el voltaje de salida solo aparece al conectar una **carga** $R_L$. La conversion corriente → voltaje es:

$$V_o = I_o \cdot R_L$$

Sustituyendo $I_o = g_m V_d$:

$$V_o = g_m \cdot R_L \cdot V_d$$

> [!success] Ganancia de voltaje del OTA
> $$\boxed{A_v = \frac{V_o}{V_d} = g_m \cdot R_L = K \cdot I_{ABC} \cdot R_L}$$
>
> La ganancia es **directamente proporcional a $I_{ABC}$**. Cambiando $I_{ABC}$ se cambia $A_v$ — un VCA (Voltage-Controlled Amplifier) usa exactamente este principio.

### Verificacion paso a paso (justificacion del profesor)

$$g_m = K \cdot I_{ABC}$$
$$I_{sal} = g_m \cdot V_{ent}$$
$$V_{sal} = I_{sal} \cdot R_L$$

Combinando:

$$\frac{V_{sal}}{V_{ent}} = \frac{I_{sal}}{V_{ent}} \cdot R_L = g_m \cdot R_L$$

$$\Rightarrow A_v = g_m \cdot R_L \checkmark$$

## ICs comerciales

| IC | Fabricante | $K$ tipico | $I_{ABC}$ rango | BW | Comentario |
| -- | ---------- | ---------- | --------------- | -- | ---------- |
| CA3080 | RCA / Intersil | 19.2 $\mu$S/$\mu$A | 0.1-2000 $\mu$A | 2 MHz | OTA "clasico", obsoleto |
| LM13600 | National | 19.2 $\mu$S/$\mu$A | 0.1-2000 $\mu$A | 2 MHz | Doble OTA con linealizacion |
| LM13700 | TI | 19.2 $\mu$S/$\mu$A (lineal) | 0.1-2000 $\mu$A | 2 MHz | Reemplazo del LM13600, todavia disponible |
| MAX435 | Maxim | --- | --- | 275 MHz | OTA de banda ancha |
| OPA860 | TI | $g_m \approx 95$ mS fija | --- | 470 MHz | Wideband, $g_m$ no ajustable |

## Polarizacion practica del LM13700

Para fijar $I_{ABC}$ se conecta un resistor entre una fuente positiva y el pin de bias del IC. En el LM13700 el pin de $I_{ABC}$ esta a **dos $V_{BE}$ por encima de $-V$** (~1.4 V) porque internamente hay un espejo de corriente con dos diodos.

```
   +V_cc
     |
    [R_pol]
     |
     ●─── pin I_ABC
     |
   (cae 2·V_BE ≈ 1.4 V)
     |
    -V
```

Voltaje a traves de $R_{pol}$:

$$V_{R_{pol}} = V_{cc} - (-V) - 2 V_{BE} = V_{cc} + |{-V}| - 1.4\,\text{V}$$

$$\boxed{I_{ABC} = \frac{V_{cc} - (-V) - 1.4\,\text{V}}{R_{pol}}}$$

> [!note] Por que 1.4 V
> Los dos diodos en serie del espejo de corriente caen $\approx 2 \times 0.7 = 1.4$ V. Si la fuente positiva fuera $V_{control}$ distinto de $V_{cc}$, se reemplaza en la formula. Esto es lo que permite controlar $I_{ABC}$ con un voltaje variable y construir un VCA.

## Ejemplo numerico 1: OTA basico con $I_{ABC}$ fija

**Enunciado.** Un OTA con $K = 16\,\mu$S/$\mu$A se polariza con $I_{ABC} = 100\,\mu$A. La carga es $R_L = 10\,\text{k}\Omega$. Calcular $g_m$, $I_o$ para $V_d = 5$ mV, $V_o$ y la ganancia $A_v$.

### Solucion

$$g_m = K \cdot I_{ABC} = 16\,\mu\text{S}/\mu\text{A} \times 100\,\mu\text{A} = 1600\,\mu\text{S} = 1.6\,\text{mS}$$

$$I_o = g_m \cdot V_d = 1.6\,\text{mS} \times 5\,\text{mV} = 8\,\mu\text{A}$$

$$V_o = I_o \cdot R_L = 8\,\mu\text{A} \times 10\,\text{k}\Omega = 80\,\text{mV}$$

$$A_v = g_m \cdot R_L = 1.6\,\text{mS} \times 10\,\text{k}\Omega = 16$$

> [!success] Verificacion cruzada
> $A_v \cdot V_d = 16 \times 5\,\text{mV} = 80\,\text{mV} = V_o$ ✓

### Cambio de ganancia variando $I_{ABC}$

Manteniendo $R_L = 10\,\text{k}\Omega$ y variando $I_{ABC}$:

| $I_{ABC}$ ($\mu$A) | $g_m$ (mS) | $A_v$ |
| ------------------ | ---------- | ----- |
| 1     | 0.016 | 0.16   |
| 10    | 0.16  | 1.6    |
| 100   | 1.6   | 16     |
| 1000  | 16    | 160    |

→ Variar $I_{ABC}$ en 3 decadas mueve $A_v$ en 3 decadas (60 dB de control de ganancia).

## Ejemplo numerico 2: LM13700 polarizado con $\pm 12$ V

**Enunciado.** Calcular la ganancia de voltaje $A_v$ de un LM13700 con los siguientes datos:

- Alimentacion simetrica: $V_{cc} = +12$ V, $-V = -12$ V
- $R_{pol} = 35\,\text{k}\Omega$ (entre $+V_{cc}$ y el pin $I_{ABC}$)
- $R_L = 15\,\text{k}\Omega$
- $K = 15\,\mu$S/$\mu$A

### Paso 1: corriente de polarizacion

Voltaje sobre $R_{pol}$:

$$V_{R_{pol}} = V_{cc} - (-V) - 1.4\,\text{V} = 12 - (-12) - 1.4 = 22.6\,\text{V}$$

Corriente:

$$I_{ABC} = \frac{V_{R_{pol}}}{R_{pol}} = \frac{22.6\,\text{V}}{35\,\text{k}\Omega} = 645.7\,\mu\text{A} \approx 646\,\mu\text{A}$$

### Paso 2: transconductancia

$$g_m = K \cdot I_{ABC} = 15\,\frac{\mu\text{S}}{\mu\text{A}} \times 645.7\,\mu\text{A} = 9686\,\mu\text{S} = 9.686\,\text{mS}$$

> [!warning] Cuidado con las unidades
> $K$ tiene unidades $\mu$S/$\mu$A. Al multiplicar por $I_{ABC}$ en $\mu$A, las "$\mu$A" se cancelan dejando $\mu$S. **No olvidar la unidad** en el resultado: $g_m = 9686\,\mu$S (no es un numero adimensional).

### Paso 3: ganancia de voltaje

$$A_v = g_m \cdot R_L = 9.686\,\text{mS} \times 15\,\text{k}\Omega$$

Conversion: $\text{mS} \times \text{k}\Omega = 10^{-3}\,\text{S} \times 10^3\,\Omega = 1$ (las unidades dan adimensional → ganancia).

$$\boxed{A_v = 9.686 \times 15 = 145.3 \quad (\equiv 43.2\,\text{dB})}$$

### Verificacion cruzada en una formula

$$A_v = K \cdot I_{ABC} \cdot R_L = K \cdot \frac{V_{R_{pol}}}{R_{pol}} \cdot R_L = 15 \cdot \frac{22.6}{35\,\text{k}} \cdot 15\,\text{k} = 15 \cdot 0.6457 \cdot 15 = 145.3 \checkmark$$

### Comprobacion del rango lineal

Para que el OTA opere en zona lineal, $|V_d| \ll V_T = 26$ mV. Con $A_v = 145$, la salida $V_o$ alcanzara $\pm 12$ V (saturacion del op-amp interno) cuando:

$$V_{d,max} = \frac{V_{sat}}{A_v} = \frac{12}{145} = 82.8\,\text{mV}$$

Pero **el OTA pierde linealidad** mucho antes (a partir de $\sim 50$ mV diferenciales por la funcion $\tanh$). Sin diodos de linealizacion, este OTA solo procesa senales de hasta $\sim 30$ mV pico sin distorsion notable. El LM13700 tiene los **diodos de linealizacion** (pines 2 y 15) que se activan polarizandolos con corriente externa para extender el rango a $\sim 100$ mV.

## Modulacion: $I_{ABC}$ variable en el tiempo

Si en lugar de conectar $R_{pol}$ a $V_{cc}$ fija, se conecta a una **senal moduladora** $V_{MOD}(t)$, la corriente de polarizacion deja de ser constante y se vuelve **funcion del tiempo**:

$$I_{ABC}(t) = \frac{V_{MOD}(t) - (-V) - 1.4\,\text{V}}{R_{pol}}$$

Como $g_m = K \cdot I_{ABC}$ y $A_v = g_m R_L$, **la ganancia del OTA tambien varia en el tiempo** siguiendo a $V_{MOD}$. Esto convierte al OTA en un **multiplicador analogico**: la salida es el producto de la senal de entrada (en pines diferenciales) por la senal moduladora (en el pin de bias).

### Limites de excursion de $I_{ABC}$

Si $V_{MOD}$ oscila entre un maximo $V_{MOD,max}$ y un minimo $V_{MOD,min}$:

$$\boxed{I_{ABC,max} = \frac{V_{MOD,max} - (-V) - 1.4\,\text{V}}{R_{pol}}}$$

$$\boxed{I_{ABC,min} = \frac{V_{MOD,min} - (-V) - 1.4\,\text{V}}{R_{pol}}}$$

```
         V_MOD(t) (senal moduladora)
            |
           [R_pol]
            |
            ●─── pin I_ABC del LM13700
            |  I_ABC(t) = K1 · V_MOD(t) + K0
           (cae 1.4 V)
            |
           -V

          ┌───────────────────────┐
          │ V_MOD →  I_ABC →  g_m  │  →  A_v(t)
          │ (control)  ↑           │
          └────────────│───────────┘
                       │
                  V_x  →  V_o = A_v(t) · V_x = K_total · V_MOD(t) · V_x(t)
                   (entrada de senal)              ↑
                                          producto de dos senales
```

> [!important] Restriccion fisica
> Para que la corriente fluya correctamente, **$V_{MOD,min}$ debe quedar por encima de $-V + 1.4$ V**. De lo contrario $I_{ABC}$ se hace negativo o cero y el OTA se apaga (corte). Por seguridad: $V_{MOD,min} \geq -V + 2$ V.

### Variacion de la ganancia con $V_{MOD}$

Sustituyendo en $A_v = K \cdot I_{ABC} \cdot R_L$:

$$A_v(t) = \frac{K \cdot R_L}{R_{pol}}\cdot\big[V_{MOD}(t) - (-V) - 1.4\big]$$

→ La ganancia es **lineal** en $V_{MOD}$, lo que es la base de un VCA con curva de control lineal (no logaritmica como un fader de audio comun, pero sirve para muchas aplicaciones).

## Ejemplo numerico 3: Rango de $I_{ABC}$ en un VCA

**Enunciado.** Para el LM13700 del Ejemplo 2 ($V_{cc} = +12$ V, $-V = -12$ V, $R_{pol} = 35\,\text{k}\Omega$, $R_L = 15\,\text{k}\Omega$, $K = 15\,\mu$S/$\mu$A), se reemplaza la conexion fija $R_{pol} \to V_{cc}$ por una senal moduladora que varia entre $V_{MOD,min} = 0$ V y $V_{MOD,max} = +12$ V. Calcular el rango de $I_{ABC}$, $g_m$ y $A_v$.

### Calculo en los extremos

**Maximo ($V_{MOD} = +12$ V):**

$$I_{ABC,max} = \frac{12 - (-12) - 1.4}{35\,\text{k}\Omega} = \frac{22.6}{35\,\text{k}\Omega} = 645.7\,\mu\text{A}$$

$$g_{m,max} = 15 \times 645.7 = 9686\,\mu\text{S}, \quad A_{v,max} = 9.686 \times 15 = 145.3$$

**Minimo ($V_{MOD} = 0$ V):**

$$I_{ABC,min} = \frac{0 - (-12) - 1.4}{35\,\text{k}\Omega} = \frac{10.6}{35\,\text{k}\Omega} = 302.9\,\mu\text{A}$$

$$g_{m,min} = 15 \times 302.9 = 4543\,\mu\text{S}, \quad A_{v,min} = 4.543 \times 15 = 68.1$$

### Tabla resumen

| $V_{MOD}$ | $I_{ABC}$ ($\mu$A) | $g_m$ (mS) | $A_v$ |
| --------- | ------------------ | ---------- | ----- |
| 0 V       | 303 | 4.54 | **68.1** |
| +6 V (medio) | 474 | 7.11 | **107** |
| +12 V     | 646 | 9.69 | **145.3** |

### Profundidad de modulacion

$$\frac{A_{v,max}}{A_{v,min}} = \frac{145.3}{68.1} = 2.13 \quad (\equiv 6.6\,\text{dB})$$

→ Variando $V_{MOD}$ entre 0 y +12 V, la ganancia se modula en un factor 2.1 (o 6.6 dB) — utilidad limitada para AM profunda.

> [!tip] Como aumentar la profundidad de modulacion
> 1. **Permitir $V_{MOD}$ negativos:** si la moduladora baja hasta $V_{MOD,min} = -10$ V (sigue por encima de $-V + 1.4 = -10.6$), la corriente minima cae a $I_{ABC,min} = (−10 − (−12) − 1.4)/35\text{k} = 17\,\mu$A → $A_{v,min} = 3.8$ → relacion 38:1 (32 dB).
> 2. **Centrar la senal:** restar un nivel DC para que $V_{MOD,min}$ quede cerca de $-V + 1.4$ V (limite fisico).
> 3. **Espejos de corriente externos:** convertir un voltaje bipolar en una corriente que va a 0 cuando $V_{MOD} = -V_{ref}$, dando modulacion 100% (4 cuadrantes).

### Aplicaciones tipicas con $I_{ABC}$ modulada

- **Modulador AM:** $V_x = $ portadora RF, $V_{MOD} = $ senal de audio. La salida es la portadora con amplitud variable $\propto V_{MOD}$.
- **Compresor / limitador de audio:** $V_{MOD}$ proviene de un detector de envolvente (rectificador + filtro pasa-bajos) de la propia senal de entrada. Cuando la senal sube, $V_{MOD}$ baja y reduce la ganancia → compresion automatica.
- **Tremolo (efecto de musica):** $V_{MOD} = $ LFO senoidal de 5-10 Hz → la senal de audio de entrada sale con modulacion de amplitud audible como "tremolo".
- **VCA en sintetizadores analogicos (Moog, ARP, Roland):** $V_{MOD}$ es la salida de la envolvente ADSR. Al pulsar una tecla, $V_{MOD}$ sube (Attack), baja a sostenido (Decay-Sustain) y cae al soltar (Release). El OTA modula la amplitud de la nota siguiendo esa envolvente.
- **AGC (control automatico de ganancia):** $V_{MOD}$ se genera como $V_{ref} - V_{detectado}$ — si la senal recibida es debil, $V_{MOD}$ sube y aumenta la ganancia.

## Aplicaciones del OTA

### 1. VCA (Voltage-Controlled Amplifier)

```
                      I_ABC = (V_control - 0.6) / R_set
                            ↑ (genera I_ABC desde V_control)
                            |
   V_in --(+) [OTA] (-)--+--+
                         |
                        [R_L]
                         |
                         GND        Vo = K · I_ABC · R_L · V_in
```

Aplicaciones:
- **Sintetizadores de musica analogica** (envolventes ADSR, control de volumen modulado por LFO)
- **Procesadores de audio** (compresion, limitacion suave)
- **Mezcladores con fader logaritmico**

### 2. Multiplicador analogico de 4 cuadrantes

Si $I_{ABC}$ es proporcional a un voltaje $V_y$ y $V_d = V_x$:

$$V_o = K \cdot I_{ABC} \cdot R_L \cdot V_x = K \cdot \frac{V_y}{R_y} \cdot R_L \cdot V_x = \frac{K R_L}{R_y} \cdot V_x V_y$$

→ multiplicacion analogica con un solo OTA. Aplicacion clasica: **modulador AM**, **multiplicador en mezcladores RF**.

### 3. Filtros sintonizables

Combinando dos OTAs y dos capacitores se construye un **filtro pasa-bajos de 2do orden** cuya **frecuencia de corte se ajusta** con $I_{ABC}$:

$$\omega_c = \frac{g_m}{C} = \frac{K I_{ABC}}{C}$$

Aplicaciones:
- **Filtros adaptativos** (tracking de senal)
- **Filtros barridos** (sweep) en analizadores de espectro
- **VCFs** (Voltage-Controlled Filters) en sintetizadores Moog/ARP

### 4. Comparador de alta velocidad

Sin realimentacion, el OTA satura rapidamente porque su pequenisima corriente de salida se amplifica en cualquier impedancia alta. BW > 100 MHz tipico.

### 5. Generador de impedancia simulada (giradores)

Dos OTAs cascadeados con un capacitor pueden simular una **inductancia** (girador). Util para implementar inductancias grandes en circuitos integrados sin usar bobinas (que son enormes en silicio).

## Limitaciones del OTA

> [!warning] Aspectos a tener en cuenta
> 1. **Linealidad limitada:** la relacion $I_o = g_m V_d$ solo vale para $|V_d| \ll V_T$ (mV). Para $V_d > 50$ mV, la salida sigue $\tanh(V_d/2V_T)$ — comprime la senal. Por eso el OTA es ideal para senales pequenas o requiere **linealizacion** (diodos del LM13700).
> 2. **Ruido:** la baja corriente de polarizacion implica $g_m$ baja → ruido relativo alto en $g_m R_L$ pequenas.
> 3. **Slew rate variable:** depende de $I_{ABC}$. A baja $I_{ABC}$, el OTA es lento.
> 4. **Buffer de salida necesario:** la salida es alta impedancia → cualquier carga la afecta. Casi siempre se sigue de un buffer (op-amp en seguidor o transistor en seguidor de emisor).

## Comparacion: op-amp vs OTA

```
   Op-amp tradicional               OTA
   ──────────────────               ───
   Vd ──[A]── Vo                    Vd ──[gm]── Io ──[RL]── Vo
        ↑ ganancia FIJA                  ↑ gm AJUSTABLE
        (a menos que se use              via I_ABC externo
        realimentacion)
        
   Vo solo depende de Vd            Vo depende de Vd Y de I_ABC
                                    → multiplicador inherente
```

## Resumen

> [!summary] Cuatro formulas que recordar
> 1. $g_m = K \cdot I_{ABC}$ con $K \approx 16\,\mu$S/$\mu$A en este curso
> 2. $I_o = g_m \cdot V_d$ (definicion de OTA)
> 3. $V_o = I_o \cdot R_L$ (efecto de la carga)
> 4. $A_v = g_m \cdot R_L = K \cdot I_{ABC} \cdot R_L$ (ganancia controlable)

El OTA convierte el control de ganancia en un problema de **control de corriente**, no de resistencia. Esto es justo lo que se necesita para implementar ganancias **controladas por voltaje** en cualquier sistema analogico modulable.

## Bibliografia

- Sedra, A. & Smith, K. *Microelectronic Circuits* (7a ed.). Oxford University Press. Cap. 8 (par diferencial), Cap. 11 (OTAs en filtros).
- Coughlin, R. & Driscoll, F. *Operational Amplifiers and Linear Integrated Circuits* (6a ed.). Prentice Hall. Cap. 11 (OTAs).
- Texas Instruments. *LM13700 Dual Operational Transconductance Amplifier with Linearizing Diodes and Buffers*. Datasheet. https://www.ti.com/product/LM13700
- Geiger, R. & Sanchez-Sinencio, E. (1985). "Active Filter Design Using Operational Transconductance Amplifiers: A Tutorial". *IEEE Circuits and Devices Magazine*, 1(2), 20-32.
