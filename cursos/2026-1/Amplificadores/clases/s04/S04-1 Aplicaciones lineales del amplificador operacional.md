---
title: "Aplicaciones lineales del amplificador operacional"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 4
orden: 1
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/opamp
  - tema/comparador
  - tema/amplificador-inversor
  - tema/amplificador-no-inversor
  - tema/seguidor-de-voltaje
  - tema/sumador
  - tema/amplificador-diferencial
  - tema/derivador
  - tema/integrador
  - tema/aplicaciones-lineales
date: 2026-04-07
---

## Configuraciones fundamentales

Todas las configuraciones de lazo cerrado se analizan aplicando las [[S03-2 Amplificador Operacional - Fundamentos#Reglas de analisis (op-amp ideal con realimentacion negativa)|reglas del op-amp ideal]]:

1. **Cortocircuito virtual:** $V_+ = V_-$
2. **Corriente de entrada cero:** $I_+ = I_- = 0$

---

## 1. Comparador de voltaje (lazo abierto)

El op-amp opera **sin realimentacion**, aprovechando su ganancia enorme para determinar cual entrada es mayor.

```
  Vin ----(+)\
              >---- Vo
  Vref ---(-)/ 
```

### Comportamiento

$$V_o = \begin{cases} V^+ - V_{sat} & \text{si } V_{in} > V_{ref} \\ V^- + V_{sat} & \text{si } V_{in} < V_{ref} \end{cases}$$

La salida solo tiene **dos estados**: saturacion positiva o negativa. No hay zona lineal util.

> [!warning] Op-amp como comparador
> Aunque funciona, un op-amp convencional (741) es **lento** para conmutar. Para aplicaciones reales se usan comparadores dedicados como el **LM311** o **LM339**, que tienen salida en colector abierto y tiempos de conmutacion mucho menores.

### Aplicaciones

- Detector de nivel (umbral)
- Detector de cruce por cero ($V_{ref} = 0$)
- Conversion analogica a digital (1 bit)

---

## 2. Amplificador no inversor

La senal de entrada se aplica a la terminal **no inversora** (+). La realimentacion negativa va de la salida a la entrada inversora (-) a traves de un divisor resistivo.

```
              Rf
  Vo ---[===]---+---(-)\ 
                |       >---- Vo
  Vin -----(+) R1      /
                |
               GND
```

### Derivacion

Por cortocircuito virtual: $V_- = V_+ = V_{in}$

Por divisor de voltaje en la realimentacion:

$$V_- = V_o \cdot \frac{R_1}{R_1 + R_f}$$

Igualando:

$$V_{in} = V_o \cdot \frac{R_1}{R_1 + R_f}$$

$$\boxed{A_v = \frac{V_o}{V_{in}} = 1 + \frac{R_f}{R_1}}$$

Donde:
- $R_f$ = resistencia de realimentacion
- $R_1$ = resistencia a tierra
- $A_v$ = ganancia de voltaje (siempre $\geq 1$)

### Caracteristicas

| Parametro | Valor |
| --------- | ----- |
| Ganancia | $1 + R_f/R_1 \geq 1$ |
| Fase | $0°$ (en fase) |
| $Z_{in}$ | Muy alta ($\approx Z_{in_{OL}} \cdot A_{OL}/A_v$) |
| $Z_{out}$ | Muy baja |

> [!tip] Ganancia minima
> La ganancia nunca puede ser menor que 1. Si se necesita $A_v < 1$ se debe usar la configuracion inversora.

---

## 3. Amplificador inversor

La senal entra por la terminal **inversora** (-) a traves de $R_1$. La entrada no inversora (+) se conecta a tierra.

```
          R1          Rf
  Vin ---[===]---+---[===]--- Vo
                 |
            (-)  |
              \  |
               >---- Vo
              /
  GND ---(+)
```

### Derivacion

Por cortocircuito virtual: $V_- = V_+ = 0$ → la entrada inversora es una **tierra virtual**.

Por corriente de entrada cero, toda la corriente que entra por $R_1$ sale por $R_f$:

$$I_1 = I_f$$

$$\frac{V_{in} - 0}{R_1} = \frac{0 - V_o}{R_f}$$

$$\boxed{A_v = \frac{V_o}{V_{in}} = -\frac{R_f}{R_1}}$$

Donde:
- $R_f$ = resistencia de realimentacion
- $R_1$ = resistencia de entrada
- El signo negativo indica **inversion de fase** (180°)

### Caracteristicas

| Parametro | Valor |
| --------- | ----- |
| Ganancia | $-R_f/R_1$ (cualquier valor) |
| Fase | $180°$ (invertida) |
| $Z_{in}$ | $R_1$ (no la del op-amp) |
| $Z_{out}$ | Muy baja |

> [!note] Tierra virtual
> El nodo de la entrada inversora se mantiene a $0\,V$ por la accion de la realimentacion, aunque **no esta fisicamente conectado a tierra**. Esta es la "tierra virtual" y es un concepto clave para analizar circuitos con op-amps.

---

## 4. Seguidor de voltaje (buffer)

Caso especial del no inversor con $R_f = 0$ y $R_1 = \infty$ (realimentacion unitaria directa).

```
            +-------------------+
            |                   |
  Vin --(+) |                   |
             >---- Vo = Vin     |
        (-) |                   |
            +-------------------+
```

$$\boxed{A_v = 1}$$

La salida **copia exactamente** la entrada. No amplifica, pero **aisla** la fuente de la carga.

### ¿Para que sirve si no amplifica?

| Sin buffer | Con buffer |
| ---------- | ---------- |
| La carga "carga" a la fuente, reduciendo $V_{in}$ | La fuente no ve la carga |
| $Z_{in}$ baja (depende de la carga) | $Z_{in}$ altisima (la del op-amp) |
| $Z_{out}$ alta (la de la fuente) | $Z_{out} \approx 0$ |

> [!example] Aplicacion tipica
> Acoplar la salida de un sensor de alta impedancia (como un piezoelectrico o un pH-metro) a un ADC de baja impedancia, sin perder voltaje.

---

## 5. Sumador inversor

Extiende el amplificador inversor a **multiples entradas**. Cada entrada se conecta al nodo de tierra virtual a traves de su propia resistencia.

```
          R1
  V1 ---[===]---+
          R2    |     Rf
  V2 ---[===]---+---[===]--- Vo
          R3    |
  V3 ---[===]---+
                |
           (-) \|
                >---- Vo
           (+) /
               |
              GND
```

### Derivacion

En el nodo de tierra virtual ($V_- = 0$), por KCL:

$$I_1 + I_2 + I_3 = I_f$$

$$\frac{V_1}{R_1} + \frac{V_2}{R_2} + \frac{V_3}{R_3} = -\frac{V_o}{R_f}$$

$$\boxed{V_o = -R_f\left(\frac{V_1}{R_1} + \frac{V_2}{R_2} + \frac{V_3}{R_3}\right)}$$

**Caso especial** — si $R_1 = R_2 = R_3 = R$:

$$V_o = -\frac{R_f}{R}(V_1 + V_2 + V_3)$$

Si ademas $R_f = R$:

$$V_o = -(V_1 + V_2 + V_3)$$

→ suma pura (invertida) de las entradas.

### Aplicaciones

- Mezclador de audio (cada $R_i$ controla el volumen de un canal)
- Conversores digital-analogico (DAC tipo R-2R)
- Operaciones matematicas analogicas

---

## 6. Amplificador diferencial (restador)

Amplifica la **diferencia** entre dos senales, rechazando lo que tienen en comun. Combina las configuraciones inversora y no inversora en un solo circuito.

```
          R1          R2
  V1 ---[===]---+---[===]--- Vo
                |
           (-) \|
                >---- Vo
           (+) /|
                |
          R3    |
  V2 ---[===]---+
                |
               R4
                |
               GND
```

### Derivacion

Aplicando superposicion y las reglas del op-amp ideal:

$$\boxed{V_o = \frac{R_2}{R_1}(V_2 - V_1)} \quad \text{cuando } \frac{R_1}{R_2} = \frac{R_3}{R_4}$$

**Caso general** (sin restriccion de resistencias):

$$V_o = V_2 \cdot \frac{R_4}{R_3 + R_4} \cdot \left(1 + \frac{R_2}{R_1}\right) - V_1 \cdot \frac{R_2}{R_1}$$

> [!important] Condicion de balance
> Para que el circuito rechace eficazmente el modo comun, las resistencias deben cumplir:
> $$\frac{R_1}{R_2} = \frac{R_3}{R_4}$$
> Cualquier desbalance degrada el CMRR. Por eso en la practica se usan resistencias de **precision** (tolerancia 0.1% o mejor).

### Limitaciones

- $Z_{in}$ no es infinita (depende de $R_1$ y $R_3$)
- Dificil lograr alto CMRR con resistencias discretas
- Para mejor desempeno → usar **amplificador de instrumentacion** (3 op-amps)

---

## 7. Amplificador derivador

> [!info] Vision en frecuencia
> El derivador es equivalente a un **filtro pasa-altos** de 1er orden. Funcion de transferencia $H(s) = -sRC$ (ideal) o $H(s) = -sRC/(1 + sR_1C)$ (practico). Detalles, derivaciones y diagramas de Bode en [[S07-5 Integrador y derivador como filtros activos]].

Produce una salida proporcional a la **derivada** de la entrada. Se obtiene reemplazando $R_1$ por un capacitor en la configuracion inversora.

```
          C           R
  Vin ---||---+---[===]--- Vo
              |
         (-) \|
              >---- Vo
         (+) /
              |
             GND
```

### Derivacion

La corriente por el capacitor es:

$$I_C = C \frac{dV_{in}}{dt}$$

Esta corriente fluye por $R$ (tierra virtual):

$$V_o = -R \cdot I_C$$

$$\boxed{V_o = -RC\frac{dV_{in}}{dt}}$$

Donde:
- $R$ = resistencia de realimentacion
- $C$ = capacitor de entrada
- $RC$ = constante de tiempo

### Respuesta a senales tipicas

| Entrada $V_{in}$ | Salida $V_o$ |
| ----------------- | ------------ |
| Rampa ($kt$) | Constante ($-RCk$) |
| Senoidal ($\sin\omega t$) | Cosenoidal ($-RC\omega\cos\omega t$) |
| Escalon | Pulso (impulso ideal) |
| Constante (DC) | Cero |

> [!warning] Inestabilidad
> El derivador **amplifica el ruido** de alta frecuencia (ganancia crece con $\omega$). En la practica se agrega una resistencia en serie con $C$ para limitar la ganancia a frecuencias altas:
> ```
>       Rs     C           R
> Vin-[===]--||---+---[===]--- Vo
> ```
> La frecuencia maxima util queda limitada a $f_{max} = \frac{1}{2\pi R_s C}$.

---

## 8. Amplificador integrador

> [!info] Vision en frecuencia
> El integrador es equivalente a un **filtro pasa-bajos** de 1er orden. Funcion de transferencia $H(s) = -1/(sRC)$ (ideal) o $H(s) = -(R_f/R)/(1 + sR_fC)$ (practico, con $R_f$ paralelo a $C$). Detalles, derivaciones y diagramas de Bode en [[S07-5 Integrador y derivador como filtros activos]].

Produce una salida proporcional a la **integral** de la entrada. Se obtiene reemplazando $R_f$ por un capacitor en la configuracion inversora.

```
          R           C
  Vin ---[===]---+---||--- Vo
                 |
            (-) \|
                 >---- Vo
            (+) /
                 |
                GND
```

### Derivacion

La corriente por $R$ es:

$$I_R = \frac{V_{in}}{R}$$

Esta corriente carga el capacitor:

$$V_o = -\frac{1}{C}\int I_R \, dt$$

$$\boxed{V_o = -\frac{1}{RC}\int_0^t V_{in} \, dt + V_o(0)}$$

Donde:
- $R$ = resistencia de entrada
- $C$ = capacitor de realimentacion
- $RC$ = constante de tiempo
- $V_o(0)$ = condicion inicial (voltaje en $C$ en $t=0$)

### Respuesta a senales tipicas

| Entrada $V_{in}$ | Salida $V_o$ |
| ----------------- | ------------ |
| Constante ($V_{DC}$) | Rampa ($-\frac{V_{DC}}{RC}t$) |
| Senoidal ($\sin\omega t$) | Cosenoidal ($\frac{1}{RC\omega}\cos\omega t$) |
| Pulso cuadrado | Onda triangular |
| Impulso | Escalon |

> [!warning] Saturacion por offset
> Cualquier pequeno voltaje DC de offset se integra continuamente, causando que la salida derive lentamente hacia la saturacion. Solucion practica: agregar una resistencia $R_f$ en paralelo con $C$ para limitar la ganancia DC:
> ```
>               Rf
>          +--[===]--+
>          |         |
>   R      |    C    |
> --[===]--+---||----+--- Vo
> ```
> $R_f$ define la ganancia DC maxima como $-R_f/R$, evitando la saturacion.

---

## 9. Convertidor corriente a voltaje (transimpedancia)

Convierte una senal de corriente en voltaje proporcional. La corriente de entrada fluye directamente por $R_f$.

```
  Iin ---+---[===]--- Vo
         |     Rf
    (-) \|
         >---- Vo
    (+) /
         |
        GND
```

$$\boxed{V_o = -I_{in} \cdot R_f}$$

- Usado con **fotodiodos** y sensores que generan corriente
- $Z_{in} \approx 0$ (tierra virtual)

---

## 10. Fuente de corriente controlada por voltaje

La corriente en la carga es independiente de $R_L$:

$$\boxed{I_L = \frac{V_{in}}{R}}$$

- Util para excitar cargas que requieren corriente constante (LEDs, sensores)
- La carga "flota" (no referenciada a tierra) en la configuracion basica

---

## Resumen de configuraciones

| Configuracion | Formula de salida | Fase | $Z_{in}$ | Aplicacion principal |
| ------------- | ----------------- | ---- | --------- | -------------------- |
| Comparador | $\pm V_{sat}$ | — | Alta | Deteccion de nivel |
| No inversor | $V_{in}(1 + R_f/R_1)$ | 0° | Muy alta | Amplificacion sin inversion |
| Inversor | $-V_{in}(R_f/R_1)$ | 180° | $R_1$ | Amplificacion con inversion |
| Seguidor | $V_{in}$ | 0° | Muy alta | Buffer, aislamiento |
| Sumador inversor | $-R_f\sum V_i/R_i$ | 180° | $R_i$ | Mezcla de senales |
| Diferencial | $(R_2/R_1)(V_2 - V_1)$ | — | $R_1, R_3$ | Medicion diferencial |
| Derivador | $-RC \cdot dV/dt$ | 180° | $1/\omega C$ | Deteccion de cambios |
| Integrador | $-\frac{1}{RC}\int V \, dt$ | 180° | $R$ | Acumulacion, filtros |
| I→V | $-I_{in} \cdot R_f$ | 180° | $\approx 0$ | Sensores de corriente |
| V→I | $V_{in}/R$ | — | Alta | Corriente constante |

## Bibliografia

- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson.
- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press.
- Gonzalez de la Rosa, J. J. *Circuitos electronicos aplicados con amplificadores operacionales*. Universidad de Cadiz.
