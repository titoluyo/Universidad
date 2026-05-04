---
title: "Amplificadores lineales y no lineales"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 6
orden: 1
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/opamp
  - tema/aplicaciones-lineales
  - tema/aplicaciones-no-lineales
  - tema/caracteristica-de-transferencia
  - tema/comparador-con-histeresis
  - tema/schmitt-trigger
  - tema/limitador
  - tema/amplificador-logaritmico
  - tema/amplificador-antilogaritmico
  - tema/generador-de-funcion
  - tema/fuente-de-corriente
date: 2026-04-27
---

## Caracteristica de transferencia del op-amp

La curva $V_o$ vs $V_d = V_+ - V_-$ del op-amp tiene **tres regiones**:

```
        Vo
         |
  +Vsat  |________
         |       /
         |      /  zona lineal
         |     /   (pendiente Aol)
         |    /
  -------+---/--------- Vd
         |  /
         | /
         |/
  -Vsat  |________
```

| Region | Condicion | Comportamiento |
| ------ | --------- | -------------- |
| Saturacion negativa | $V_d < -V_{sat}/A_{ol}$ | $V_o = V^- + V_{sat^-}$ |
| Lineal | $|V_d| < V_{sat}/A_{ol}$ | $V_o = A_{ol} \cdot V_d$ |
| Saturacion positiva | $V_d > V_{sat}/A_{ol}$ | $V_o = V^+ - V_{sat^+}$ |

Como $A_{ol} \approx 10^5$, la zona lineal es **extremadamente angosta** (uV). Por eso un op-amp sin realimentacion solo es util como [[S04-1 Aplicaciones lineales del amplificador operacional#1. Comparador de voltaje (lazo abierto)|comparador]]: cualquier diferencia minima entre entradas lo lleva a saturacion.

> [!important] Lineal vs no lineal
> - **Aplicacion lineal:** el op-amp opera en la zona lineal mediante **realimentacion negativa**. La salida es proporcional (lineal) a la entrada en algun rango.
> - **Aplicacion no lineal:** el op-amp opera en saturacion (lazo abierto o realimentacion positiva), o usa elementos no lineales (diodos, transistores) en la realimentacion para producir una funcion no lineal.

---

## Parte I: Aplicaciones lineales (profundizacion)

Las configuraciones basicas (inversor, no inversor, sumador, restador, derivador, integrador, buffer) ya fueron analizadas en [[S04-1 Aplicaciones lineales del amplificador operacional]]. En esta seccion se profundiza en aplicaciones especiales.

### Adaptador de impedancia

El **buffer (seguidor)** es el adaptador de impedancia por excelencia: convierte una fuente de alta impedancia en una de baja impedancia sin alterar la senal.

```
   Sensor             Buffer              Carga
   Zfuente alta       Zin altisima        Zout casi 0
   --------       --------       --------
   |      |--->---|+     |---->-|       |
   | Vin  |       |  op  |      |  RL  |
   |      |       |  amp |      |       |
   --------       |      |---<--|       |
                  |-     |       --------
                  --------
```

**Aplicaciones:**

- Acoplar sensores piezoelectricos, fotodiodos o pH-metros a un ADC
- Aislar etapas para evitar carga (loading) entre ellas
- Convertir senales de instrumentacion de alta Z a baja Z para transmision por cable

### Convertidores de impedancia

Generalizacion del adaptador. Permiten **transformar la naturaleza** de la senal:

| Convertidor | Entrada | Salida | Configuracion | Formula |
| ----------- | ------- | ------ | ------------- | ------- |
| V → V (buffer) | Voltaje | Voltaje | Seguidor | $V_o = V_{in}$ |
| I → V (transimpedancia) | Corriente | Voltaje | Inversor con $I_{in}$ a tierra virtual | $V_o = -I_{in} R_f$ |
| V → I (transconductancia) | Voltaje | Corriente | Howland / inversor con carga flotante | $I_L = V_{in}/R$ |
| I → I | Corriente | Corriente | Espejo activo | $I_o = k \cdot I_{in}$ |

### Fuente de tension de referencia

Genera un voltaje DC estable, independiente de la carga:

```
              Rf
   +Vref ---[===]---+----- Vo (estable)
                    |
              R1    |
   +Vz ----[===]---+
                    |
               (-) \|
                    >----- Vo
               (+) /
                    |
                   GND
```

Usa un **diodo Zener** ($V_z$) como referencia primaria. El op-amp en configuracion no inversora amplifica $V_z$ a la salida deseada y aisla la corriente de carga del Zener (que necesita corriente estable para mantener su voltaje):

$$V_o = V_z \left(1 + \frac{R_f}{R_1}\right)$$

> [!tip] Por que no usar el Zener directamente
> El Zener varia su voltaje con la corriente de carga (regulacion limitada). El op-amp absorbe la corriente de carga y mantiene el Zener en su punto optimo de polarizacion.

### Fuente de corriente controlada por voltaje (Howland)

Entrega corriente proporcional al voltaje de entrada, **independiente de la carga**:

```
          R1         R2
  V1 ---[===]---+---[===]---+
                |           |
           (-) \|           |
                >-----------+---- IL
           (+) /            |
                |          [RL]
          R3    |           |
  V2 ---[===]---+           |
                |           |
               R4           |
                |           |
               GND          |
                            +---- (retorna)
```

Cuando se cumple $R_1 R_4 = R_2 R_3$:

$$\boxed{I_L = \frac{V_2 - V_1}{R_1}}$$

La corriente en la carga **no depende de $R_L$**, solo de la diferencia de voltaje y $R_1$.

**Aplicaciones:**

- Excitar LEDs con corriente constante (brillo estable)
- Polarizar sensores resistivos (RTD, termopares)
- Generadores de senal de corriente (4-20 mA en instrumentacion industrial)

---

## Parte II: Aplicaciones no lineales

En las aplicaciones no lineales el op-amp **no opera en zona lineal** o tiene elementos no lineales en la red de realimentacion. La salida ya no es proporcional a la entrada.

### 1. Comparador no inversor (basico)

Configuracion mas simple del op-amp como elemento no lineal: la senal va a la terminal **no inversora** (+) y un voltaje de referencia $V_{REF}$ a la **inversora** (-). El op-amp opera en **lazo abierto** (sin realimentacion).

```
                +---- +Vcc
                |
   Vin -----(+)\|
                >---- Vo
  Vref -----(-)/|
                |
                +---- -Vee
```

#### Comportamiento

Por la ecuacion del op-amp en lazo abierto $V_o = A_{ol}(V_+ - V_-)$ con $V_+ = V_{in}$ y $V_- = V_{REF}$:

$$V_o = A_{ol}(V_{in} - V_{REF})$$

Como $A_{ol} \approx 10^5$, cualquier diferencia minima ($\mu V$) entre $V_{in}$ y $V_{REF}$ satura la salida:

$$\boxed{V_o = \begin{cases} +V_{sat} & \text{si } V_{in} > V_{REF} \\ -V_{sat} & \text{si } V_{in} < V_{REF} \end{cases}}$$

> [!note] Por que "no inversor"
> La salida **sigue el sentido** de la entrada: cuando $V_{in}$ sube por encima del umbral, la salida va a $+V_{sat}$. La fase es la misma.
> En el **comparador inversor** (signal a (-), $V_{REF}$ a (+)) la logica se invierte: $V_{in} > V_{REF}$ → $V_o = -V_{sat}$.

#### Caracteristica de transferencia

```
       Vo
        |
  +Vsat |          ___________
        |         |
        |         |
  ------+---------+--------- Vin
        |        Vref
        |         |
        |_________|
  -Vsat
```

Es una funcion **escalon** centrada en $V_{REF}$. La transicion idealmente es instantanea (en la practica esta limitada por el **slew rate** del op-amp).

#### Diagrama temporal

Para una entrada senoidal $V_{in} = A\sin(\omega t)$ con $V_{REF} > 0$:

```
   Vin
    |          ___
    |        /     \                  /
  A_|_______/       \_________________/
    |      /         \               /
  Vref-----+----------+--------------+----- t
    |    /             \            /
    |  /                \         /
  --+-------------------------------------> t
    |                    \      /
    |                     \    /
   -A|____________________ \__/

   Vo
    |    ___              ___
+Vsat    |  |              |  |
    |    |  |              |  |
  --+----+--+--------------+--+--+----- t
    |       |              |     |
    |       |              |     |
-Vsat       |______________|     
```

#### Aplicaciones

- **Detector de nivel:** dispara una alarma cuando una senal (temperatura, presion, voltaje de bateria) supera un umbral
- **Detector de cruce por cero:** con $V_{REF} = 0$, convierte una senoidal en cuadrada en fase con la entrada
- **Generador de pulsos** sincronizados con una senal analogica
- **Cuantizacion de 1 bit** (etapa basica de un ADC flash)

#### Ejemplo: detector de cruce por cero

```
                +---- +12V
                |
  Vin ------(+)\|
                >---- Vo (cuadrada en fase con Vin)
  GND ------(-)/|
                |
                +---- -12V
```

Como $V_{REF} = 0$:

| Intervalo | $V_{in}$ | $V_o$ |
| --------- | -------- | ----- |
| $0 < t < T/2$ | Positivo | $+V_{sat}$ |
| $T/2 < t < T$ | Negativo | $-V_{sat}$ |

La salida es una **onda cuadrada** sincronizada con los cruces por cero de la entrada. Util para extraer la frecuencia o la fase de una senal analogica (sincronizacion de PLL, contadores de frecuencia).

#### Ejemplo: detector de nivel con $V_{REF}$ generado por divisor

```
   +Vcc
     |
    [R1]
     |
     +-------(-)\
                 \      +---- +Vcc
    [R2]          \    |
     |        Vin-(+)\|
    GND              >---- Vo
                 (-)/|
                    |
                    +---- -Vee
```

$$V_{REF} = V_{cc} \cdot \frac{R_2}{R_1 + R_2}$$

Ajustando la relacion $R_1/R_2$ se fija el umbral de disparo.

> [!warning] Limitaciones del comparador con op-amp
> 1. **Velocidad:** un op-amp generico (741) tarda decenas de $\mu s$ en conmutar. Para senales rapidas se usan **comparadores dedicados** (LM311, LM339, LM393) con tiempos de propagacion de cientos de ns y salida en colector abierto.
> 2. **Sensibilidad al ruido:** sin histeresis, el ruido cerca del umbral causa **multiples conmutaciones** indeseadas. Solucion → [[#2. Comparador con histeresis (Schmitt trigger)|Schmitt trigger]].
> 3. **Saturacion asimetrica:** en op-amps reales $V_{sat^+} \neq V_{sat^-}$, especialmente con alimentacion unica. Para salidas digitales limpias usar diodos Zener limitadores en la salida.
> 4. **Sin proteccion:** transitorios rapidos en la entrada pueden danar las terminales. Anadir resistencias serie y diodos de clamp.

---

### 2. Comparador con histeresis (Schmitt trigger)

El [[#1. Comparador no inversor (basico)|comparador simple]] tiene un problema: si la senal de entrada tiene **ruido** alrededor del umbral, la salida conmuta multiples veces.

```
  Vin con ruido          Comparador simple → salida con multiples conmutaciones
                         (oscilaciones rapidas indeseadas)
```

**Solucion:** agregar **realimentacion positiva** para crear dos umbrales distintos (histeresis).

#### Schmitt trigger inversor

```
              R2
       +-----[===]-----+
       |               |
       |          (-) \|
  Vin -+---------------+
                       >----- Vo
                  (+) /|
                       |
                      R1
                       |
                      GND  (o Vref)
```

Por divisor entre $R_1$ y $R_2$ desde la salida hacia la entrada (+):

$$V_+ = V_o \cdot \frac{R_1}{R_1 + R_2}$$

Como $V_o$ solo toma dos valores ($\pm V_{sat}$), aparecen **dos umbrales**:

$$V_{UT} = +V_{sat} \cdot \frac{R_1}{R_1 + R_2} \quad \text{(umbral superior)}$$

$$V_{LT} = -V_{sat} \cdot \frac{R_1}{R_1 + R_2} \quad \text{(umbral inferior)}$$

El **ancho de la histeresis** es:

$$\boxed{\Delta V_H = V_{UT} - V_{LT} = 2V_{sat} \cdot \frac{R_1}{R_1 + R_2}}$$

#### Curva de transferencia (con histeresis)

```
       Vo
        |
  +Vsat |+++++++++++
        |          |
        |          |     <-- baja desde +Vsat solo cuando Vin > VUT
  ------+----------+----- Vin
       VLT       VUT
        |          |
        |          |     <-- sube desde -Vsat solo cuando Vin < VLT
  -Vsat |__________|
```

> [!important] Funcionamiento
> - Si $V_o = +V_{sat}$, conmuta a $-V_{sat}$ solo cuando $V_{in} > V_{UT}$
> - Si $V_o = -V_{sat}$, conmuta a $+V_{sat}$ solo cuando $V_{in} < V_{LT}$
> - Entre $V_{LT}$ y $V_{UT}$ la salida **mantiene su estado anterior** (memoria)

#### Schmitt trigger no inversor

```
       R1            R2
  Vin-[===]-+--[===]-+
            |        |
            |   (-) \|
            |        +
            |        >---- Vo
            +--(+) /
                    |
                   GND
```

Umbrales:

$$V_{UT} = +V_{sat} \cdot \frac{R_1}{R_2}, \quad V_{LT} = -V_{sat} \cdot \frac{R_1}{R_2}$$

#### Aplicaciones

- **Recuperacion de senal digital** sobre canales con ruido
- **Detectores de nivel** robustos
- **Generadores de onda cuadrada** (junto con un integrador, ver mas adelante)
- **Eliminacion de rebote** (debounce) en interruptores mecanicos

---

### 3. Limitadores (recortadores)

Recortan la senal a un nivel maximo y/o minimo. Se construyen colocando **diodos en la realimentacion** o en serie con la entrada.

#### Limitador positivo (con diodo en realimentacion)

```
          R1          D
  Vin ---[===]---+---|>|--- Vo
                 |        |
                 +--[===]-+
                 |    Rf
            (-) \|
                 >---- Vo
            (+) /
                 |
                GND
```

- Si $V_o < V_\gamma$: el diodo no conduce, $V_o = -V_{in} R_f / R_1$ (inversor normal)
- Si $V_o \geq V_\gamma$: el diodo conduce, fija $V_o \approx V_\gamma$ (clamp)

#### Limitador con Zener (limitador de doble nivel)

```
                  Z1   Z2
            +----|<|--|>|----+
            |                |
          R1|       Rf       |
  Vin ---[===]---+---[===]---+
                 |
            (-) \|
                 >---- Vo
            (+) /
                 |
                GND
```

Dos Zeners espalda-con-espalda limitan la salida a:

$$-(V_{Z2} + V_\gamma) \leq V_o \leq +(V_{Z1} + V_\gamma)$$

Util para **proteger** entradas de ADC o convertir cualquier forma de onda en cuadrada con amplitud controlada.

#### Rectificador de precision (super diodo)

Un diodo simple tiene caida de $0.7$ V que arruina senales pequenas. Colocando el diodo dentro del lazo de realimentacion del op-amp, la caida se "divide" entre $A_{ol}$:

```
                 D
             +--|>|--+
             |       |
  Vin --(+) \|       |
             >-------+---- Vo
        (-) /        |
             +---<---+
```

La caida efectiva es $V_\gamma / A_{ol} \approx 7$ uV. Permite rectificar senales de **mV**.

---

### 4. Generadores de funcion

Combinan integrador + Schmitt trigger para generar formas de onda **sin entrada de senal**.

#### Multivibrador astable (onda cuadrada)

Un op-amp con realimentacion positiva (Schmitt) y una red RC en la entrada inversora oscila libremente:

```
             R              Rf
       +---[===]---+    +--[===]--+
       |           |    |         |
       |       (-) +----+         |
       |            \             |
       |             >----+------ Vo (cuadrada)
       |            /     |
       |       (+) +------+
       |           |      |
       +---||------+     R1
            C       |     |
           GND     GND   GND
```

El capacitor se carga/descarga a traves de $R$ entre los umbrales del Schmitt. La frecuencia es:

$$f = \frac{1}{2RC \cdot \ln\left(\frac{1 + \beta}{1 - \beta}\right)}, \quad \beta = \frac{R_1}{R_1 + R_f}$$

Si $R_1 = R_f$ (β = 0.5): $f \approx \frac{1}{2.2 \, RC}$

#### Generador de onda triangular

Conectar la salida cuadrada del astable a un [[S04-1 Aplicaciones lineales del amplificador operacional#8. Amplificador integrador|integrador]]: la integral de una cuadrada es triangular.

```
   Schmitt trigger ----+---- Vo (cuadrada)
                       |
                       v
                    Integrador ----- Vo' (triangular)
```

La amplitud de la triangular es:

$$V_{tri} = \frac{V_{sat} \cdot T}{4 R_i C_i}$$

#### Generador de onda senoidal

Mas complejo: usa **realimentacion positiva con red selectiva de frecuencia** (puente de Wien, oscilador de corrimiento de fase). Se ve a profundidad en [[Unidad 2]].

---

### 5. Amplificador logaritmico

Produce una salida proporcional al **logaritmo natural** de la entrada. Es la base para realizar **operaciones matematicas analogicas** (multiplicacion, division, potencias) y para **comprimir** rangos dinamicos amplios (ej. señales que varian en varias decadas).

#### Fundamento fisico: ecuacion de Shockley

> [!info] Derivacion completa
> La derivacion paso a paso desde la **distribucion de Maxwell-Boltzmann** hasta $V_f = (kT/q)\ln(I_f/I_R)$ esta en [[Ecuacion del diodo - derivacion desde Boltzmann]].

La corriente en una union PN polarizada en directa esta dada por:

$$I_D = I_s\left(e^{V_D / V_T} - 1\right)$$

Para $V_D \gg V_T$ (~26 mV) la unidad es despreciable:

$$I_D \approx I_s \, e^{V_D / V_T}$$

Donde:
- $I_s$ = corriente de saturacion inversa ($10^{-12}$ a $10^{-15}$ A para diodos de silicio)
- $V_T = kT/q \approx 26$ mV a 25°C ($k$ = Boltzmann, $T$ = temperatura absoluta, $q$ = carga del electron)
- $V_D$ = voltaje directo del diodo

Despejando $V_D$ en funcion de $I_D$:

$$V_D = V_T \ln\left(\frac{I_D}{I_s}\right)$$

→ El voltaje a traves del diodo **es el logaritmo natural** de la corriente que lo atraviesa. Este es el principio que aprovecha el log-amp.

#### Configuracion con diodo

```
          R              D
  Vin ---[===]---+------|>|------+
                 |               |
            (-) \|               |
                 +---------------+ Vo
            (+) /
                 |
                GND
```

#### Derivacion

Por tierra virtual ($V_- = V_+ = 0$), la corriente que entra por $R$ pasa integramente por el diodo (corriente de entrada del op-amp despreciable):

$$I_R = I_D \quad \Rightarrow \quad \frac{V_{in}}{R} = I_s \, e^{V_D / V_T}$$

El voltaje del diodo es $V_D = 0 - V_o = -V_o$ (anodo a tierra virtual, catodo a la salida):

$$\frac{V_{in}}{R} = I_s \, e^{-V_o / V_T}$$

Despejando $V_o$:

$$\boxed{V_o = -V_T \ln\left(\frac{V_{in}}{R \cdot I_s}\right)}$$

#### Caracteristica de transferencia

Reescribiendo la formula:

$$V_o = -V_T \ln(V_{in}) + V_T \ln(R \cdot I_s)$$

→ **$V_o$ vs $\ln(V_{in})$ es una recta** con pendiente $-V_T \approx -26$ mV/unidad-de-ln.

En base decimal (mas usada en la practica):

$$V_o \approx -V_T \ln(10) \cdot \log_{10}\left(\frac{V_{in}}{R \cdot I_s}\right) \approx -60 \text{ mV} \cdot \log_{10}\left(\frac{V_{in}}{R \cdot I_s}\right)$$

→ La salida cae **~60 mV por cada decada** de aumento en $V_{in}$.

```
       Vo
        |
   0    |----.
        |     '----.
  -60mV |           '----. <- decada 1 (Vin x10)
        |                 '----.
  -120mV|                       '----. <- decada 2 (x100)
        |                              '----.
  -180mV|                                    '----. <- decada 3 (x1000)
        |
        +----+--------+--------+--------+----- log(Vin)
            Vref    10·Vref  100·Vref 1000·Vref
```

#### Ejemplo numerico

Sea $R = 10\,\text{k}\Omega$, $I_s = 10^{-12}$ A, $V_T = 26$ mV. Calcular $V_o$ para varios $V_{in}$:

| $V_{in}$ | $\dfrac{V_{in}}{R \cdot I_s}$ | $\ln(\cdot)$ | $V_o = -V_T \ln(\cdot)$ |
| -------- | ----------------------------- | ------------ | ------------------------ |
| 1 mV     | $10^{5}$  | 11.51 | $-299$ mV |
| 10 mV    | $10^{6}$  | 13.82 | $-359$ mV |
| 100 mV   | $10^{7}$  | 16.12 | $-419$ mV |
| 1 V      | $10^{8}$  | 18.42 | $-479$ mV |
| 10 V     | $10^{9}$  | 20.72 | $-539$ mV |

Diferencia entre decadas: $\Delta V_o \approx 60$ mV ✓ — confirma la pendiente teorica.

> [!example] Comprime 4 decadas en 240 mV
> Mientras $V_{in}$ varia en un rango de 10000:1 (1 mV a 10 V), $V_o$ apenas varia 240 mV. Esto permite procesar señales con enorme rango dinamico (ej. luz solar vs luz de luna en un fotodiodo).

#### Configuracion con transistor BJT (mas estable)

Reemplazando el diodo por un BJT con la base a tierra virtual y el emisor en la trayectoria de realimentacion, la relacion logaritmica mejora notablemente:

```
                              C
                              |
                             [Q]   <- BJT NPN, base a GND, colector recibe corriente
                              |
                              E ----+
                              |     |
          R                   |     |
  Vin ---[===]---+------------+     |  (corriente de Vin pasa por C-E)
                 |                  |
            (-) \|                  |
                 +------------------+ Vo
            (+) /
                 |
                GND
```

La ecuacion del BJT en region activa es:

$$I_C = I_s \, e^{V_{BE} / V_T}$$

Aplicando el mismo analisis (con $V_{BE} = -V_o$ porque emisor en $V_o$ y base en GND):

$$\boxed{V_o = -V_T \ln\left(\frac{V_{in}}{R \cdot I_s}\right)}$$

> [!tip] Por que el BJT es mejor que el diodo
> 1. **Linealidad logaritmica:** mantiene $I_C = I_s e^{V_{BE}/V_T}$ con alta precision durante **8-10 decadas** (vs 4-6 decadas del diodo)
> 2. **Sin resistencia serie significativa:** el diodo tiene resistencia interna de la region neutra que distorsiona la respuesta a corrientes altas
> 3. **Factor de idealidad $\eta = 1$:** la union B-E del BJT no tiene recombinacion en la zona de carga espacial (en el diodo $\eta \in [1,2]$)
> 4. **Pares monoliticos disponibles:** se consiguen pares de transistores apareados en un solo chip (ej. LM394, MAT01)

#### Compensacion de temperatura

Sin compensacion el log-amp es **inutil** en aplicaciones serias:

- $V_T = kT/q$ varia $+0.33\%/°C$ → afecta la pendiente
- $I_s$ se **duplica cada 10°C aprox.** → causa una deriva de cero gigantesca (~7 mV/°C)

**Solucion:** **par diferencial de transistores apareados** termicamente (mismo chip o encapsulado). Un segundo BJT identico, polarizado con una corriente de referencia $I_{REF}$, cancela $I_s$:

```
   Vin/R                I_REF
     |                    |
     E1                   E2
    [Q1]               [Q2]   <- par apareado, misma temperatura
     B1=GND             B2=GND
     C1                   C2
     |                    |
     V_BE1                V_BE2
     |                    |
     +---->[op-amp resta]<+
                |
                Vo
```

Calculando los $V_{BE}$ de cada transistor:

$$V_{BE1} = V_T \ln\left(\frac{V_{in}/R}{I_s}\right), \quad V_{BE2} = V_T \ln\left(\frac{I_{REF}}{I_s}\right)$$

Restando con un op-amp diferencial:

$$\boxed{V_o = V_{BE2} - V_{BE1} = V_T \ln\left(\frac{I_{REF} \cdot R}{V_{in}}\right)}$$

→ **$I_s$ cancelado**. Solo queda la dependencia con $V_T$, que se compensa con un resistor de coeficiente de temperatura positivo (PTC) o con circuiteria interna en ICs dedicados.

#### ICs comerciales

| IC | Decadas | Banda | Aplicacion tipica |
| -- | ------- | ----- | ----------------- |
| LOG101 / LOG102 (TI) | 6 | DC | Instrumentacion analitica |
| AD8304 (Analog Devices) | 8 | 5 MHz | Fotometria, fibra optica |
| LOG112 (TI) | 7.5 | DC | Sensores quimicos, pH |
| LOG114 (TI) | 7 | DC | Multiplicacion analogica |

#### Compensacion en frecuencia

> [!warning] Tendencia a oscilar
> La ganancia de pequena senal del log-amp **aumenta** cuando $V_{in}$ disminuye:
>
> $$g_m = \frac{\partial I_C}{\partial V_{BE}} = \frac{I_C}{V_T}$$
>
> $$A_v(\text{small-signal}) \approx \frac{1}{g_m R} = \frac{V_T}{V_{in}}$$
>
> Para $V_{in}$ pequeno la ganancia se dispara y el op-amp puede oscilar. **Solucion:** agregar resistencia $R_E$ en serie con el emisor del BJT y un capacitor $C_C$ en paralelo:
>
> ```
>     E
>     |
>    [RE]====[CC]   <- limita ganancia de alta frecuencia
>     |
>     Vo
> ```

#### Limitaciones generales

| Limitacion | Descripcion | Mitigacion |
| ---------- | ----------- | ---------- |
| Polaridad | $V_{in}$ debe ser positivo (diodo/BJT solo conduce en directa) | Rectificador de precision previo |
| Cero | Si $V_{in} \to 0$, $V_o \to +\infty$ (no fisico) | Offset y $I_b$ del op-amp definen el limite inferior practico |
| Saturacion | Para $V_{in}$ muy alto el op-amp satura (limite superior) | Atenuador previo |
| Temperatura | Deriva grande sin compensacion | Par apareado + resistor PTC |
| Velocidad | Respuesta lenta a $V_{in}$ pequeno ($\tau = r_d \cdot C \uparrow$) | IC dedicado con compensacion activa |

---

### 6. Amplificador antilogaritmico (exponencial)

Es la **operacion inversa** del logaritmico: la salida es proporcional a $e^{V_{in}}$. Se obtiene **intercambiando** las posiciones de $R$ y el diodo (o BJT) en la configuracion log.

#### Configuracion con diodo

```
                       R
                  +---[===]---+
                  |           |
            D     |           |
  Vin -----|>|----+-----------+ Vo
                  |
             (-) \|
                  +---- Vo
             (+) /
                  |
                 GND
```

#### Derivacion

El anodo del diodo esta en $V_{in}$ y el catodo en tierra virtual ($V_- = 0$). El voltaje del diodo es $V_D = V_{in}$:

$$I_D = I_s \, e^{V_{in}/V_T}$$

Esta corriente fluye por $R$ desde $V_o$ hacia tierra virtual:

$$V_o - 0 = -I_D \cdot R$$

$$\boxed{V_o = -R \cdot I_s \, e^{V_{in}/V_T}}$$

#### Caracteristica de transferencia

Como $\ln(10) \cdot V_T \approx 60$ mV, **cada 60 mV de aumento en $V_{in}$ multiplica $|V_o|$ por 10**:

| $V_{in}$ | $e^{V_{in}/V_T}$ | $|V_o|/(R \cdot I_s)$ |
| -------- | ---------------- | --------------------- |
| 0    | 1     | 1 |
| 60 mV  | 10  | 10 |
| 120 mV | 100 | 100 |
| 180 mV | 1000 | 1000 |
| 240 mV | $10^4$ | $10^4$ |

```
       |Vo|
        |                                   .__
        |                              .---'
        |                         .---'
        |                    .---'
        |               .---'
        |__________.---'
        +----+----+----+----+----+----+----- Vin
        0   60  120  180  240  300  360 mV
              (cada +60 mV → x10)
```

#### Ejemplo numerico

Sea $R = 10\,\text{k}\Omega$, $I_s = 10^{-12}$ A. Calcular $V_o$ para varios $V_{in}$:

| $V_{in}$ | $V_{in}/V_T$ | $e^{V_{in}/V_T}$ | $V_o = -R I_s e^{V_{in}/V_T}$ |
| -------- | ------------ | ---------------- | ------------------------------ |
| 0 mV     | 0       | 1                  | $-10$ nV    |
| 240 mV   | 9.23    | $1.0 \times 10^4$  | $-100\,\mu$V |
| 480 mV   | 18.46   | $1.0 \times 10^8$  | $-1.0$ mV   |
| 600 mV   | 23.08   | $1.1 \times 10^{10}$ | $-110$ mV  |
| 660 mV   | 25.38   | $1.1 \times 10^{11}$ | $-1.1$ V   |
| 720 mV   | 27.69   | $1.1 \times 10^{12}$ | $-11$ V (saturado) |

→ Para $V_{in} \gtrsim 0.7$ V el op-amp **satura**. El antilog opera tipicamente con $V_{in}$ entre **0 y 600 mV**.

#### Configuracion con transistor BJT

```
                        R
                  +----[===]----+
                  |             |
                  C             |
                  |             |
                 [Q]            |   <- BJT NPN, base a Vin, colector recibe corriente
                  |             |
                  E ------------+ (a tierra virtual)
  Vin --[B]-------+
                                |
                             (-)\|
                                 +---- Vo
                             (+)/
                                |
                               GND
```

Con $V_{BE} = V_{in}$ (emisor a tierra virtual) y $I_C = I_s e^{V_{in}/V_T}$:

$$V_o = -R \cdot I_s \, e^{V_{in}/V_T}$$

#### Compensacion de temperatura

Mismo principio que el log-amp: **par apareado** con $I_{REF}$:

$$\boxed{V_o = -R \cdot I_{REF} \cdot e^{V_{in}/V_T}}$$

→ $I_s$ cancelado. Es la formula que se usa en la practica con ICs como **AD8304** (operando como antilog) o **LOG114** configurado como exponencial.

#### Limitaciones del antilog

> [!warning] Restricciones practicas
> - $V_{in}$ tipicamente entre **0 y ~600 mV** (limitado por saturacion del op-amp y rotura B-E del transistor a $V_{BE} > 0.7$ V)
> - $V_o$ siempre del mismo signo (negativo en esta topologia)
> - Si se requiere $V_{in}$ negativo o mayor a 600 mV: usar **escalado previo** (atenuador / divisor) para mantener $V_{BE}$ en rango seguro
> - Misma sensibilidad termica que el log-amp → **siempre** compensar con par apareado

#### Ejemplo de escalado

Si la entrada disponible es 0-10 V y se necesita $V_{in,BE}$ en 0-600 mV:

```
              Atenuador    Antilog
              R1=10k       (con BJT)
   +10V ---[===]---+--------+----- ... 
                   |
                  [R2=600]   --> V_BE = 600 mV cuando entrada = 10V
                   |
                  GND
```

---

### 7. Aplicaciones del log/antilog

Combinando log y antilog se realizan **operaciones matematicas analogicas**:

#### Multiplicador analogico

$$\ln(V_1) + \ln(V_2) = \ln(V_1 V_2)$$

```
  V1 ---[log]---+
                +--[suma]---[antilog]--- V_o = k V1 V2
  V2 ---[log]---+
```

#### Divisor analogico

$$\ln(V_1) - \ln(V_2) = \ln(V_1/V_2)$$

#### Compresor / expansor de senal

En audio profesional, el **companding** (compress + expand) reduce el ruido:

- En grabacion: comprimir (log) la senal para reducir rango dinamico
- En reproduccion: expandir (antilog) para recuperar la senal original

> [!example] Aplicacion clasica: Dolby
> Los sistemas Dolby B/C/SR para cassettes usaban log/antilog amps para comprimir la senal antes de grabar y expandirla al reproducir, mejorando el SNR en 10-20 dB.

---

## Resumen comparativo: lineales vs no lineales

| Caracteristica | Lineales | No lineales |
| -------------- | -------- | ----------- |
| Realimentacion | Negativa | Positiva o no lineal (diodos) |
| Region de operacion | Lineal | Saturacion o curva no lineal |
| Salida vs entrada | Proporcional ($V_o = kV_{in}$) | No proporcional |
| Ejemplos | Inversor, no inversor, sumador, restador, integrador | Comparador, Schmitt, limitador, log, antilog |
| Aplicaciones | Amplificacion, filtrado, acondicionamiento | Conmutacion, deteccion, operaciones matematicas |

## Bibliografia

- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson. Cap. 14.
- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press. Cap. 18.
- Gonzalez de la Rosa, J. J. *Circuitos electronicos aplicados con amplificadores operacionales*. Universidad de Cadiz. Cap. 5-6.
- Coughlin, R. & Driscoll, F. *Operational Amplifiers and Linear Integrated Circuits*. Prentice Hall. Cap. 4-7.
