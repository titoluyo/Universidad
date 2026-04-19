---
title: "Amplificador Operacional - Fundamentos"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 3
orden: 2
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/opamp
  - tema/amplificador-operacional
  - tema/laplace
  - tema/funcion-de-transferencia
date: 2026-04-07
---

## ¿Que es un amplificador operacional?

El amplificador operacional (op-amp) es un **amplificador de voltaje diferencial de alta ganancia** con entrada diferencial y salida single-ended. Se llama "operacional" porque originalmente se diseño para realizar **operaciones matematicas** (suma, resta, integracion, derivacion) en computadoras analogicas.

> [!info] Componente fundamental
> El op-amp es el bloque de construccion mas importante de la electronica analogica moderna. Un solo circuito integrado como el LM741 contiene ~20 transistores, resistencias y capacitores internos.

## Simbolo y terminales

```
        V+
        |
  V1 (+)|\ 
        | \
        |  >---- Vo (salida)
        | /
  V2 (-)|/
        |
        V-
```

| Terminal | Nombre | Descripcion |
| -------- | ------ | ----------- |
| $V_1$ (+) | Entrada no inversora | La salida esta **en fase** con esta entrada |
| $V_2$ (-) | Entrada inversora | La salida esta en **contrafase** con esta entrada |
| $V_o$ | Salida | Voltaje amplificado |
| $V^+$ | Alimentacion positiva | Tipicamente +15V, +12V o +5V |
| $V^-$ | Alimentacion negativa | Tipicamente -15V, -12V o GND |

> [!warning] Signo + y - en las entradas
> Los signos (+) y (-) **no** indican polaridad de voltaje. Indican la **relacion de fase** con la salida. No confundir con las terminales de alimentacion $V^+$ y $V^-$.

## Estructura interna

Como se vio en [[S03-1 Amplificador diferencial con BJT PNP|la nota anterior]], el op-amp esta compuesto por tres etapas en cascada:

| Etapa | Funcion | Caracteristica clave |
| ----- | ------- | -------------------- |
| **Diferencial** (entrada) | Amplifica $V_1 - V_2$ | Alta $Z_{in}$, alto CMRR |
| **Ganancia** (intermedia) | Aumenta la ganancia total | Ganancia de voltaje muy alta |
| **Salida** (push-pull) | Entrega corriente a la carga | Baja $Z_{out}$ |

---

## Op-amp ideal vs real

### Tabla comparativa

| Parametro | Simbolo | Ideal | Real (LM741) | Unidad |
| --------- | ------- | ----- | ------------- | ------ |
| Ganancia de lazo abierto | $A_{OL}$ | $\infty$ | $200{,}000$ ($106\,dB$) | V/V |
| Impedancia de entrada | $Z_{in}$ | $\infty$ | $2\,M\Omega$ | $\Omega$ |
| Impedancia de salida | $Z_{out}$ | $0$ | $75\,\Omega$ | $\Omega$ |
| Ancho de banda | $BW$ | $\infty$ | $\sim 5\,Hz$ (lazo abierto) | Hz |
| GBW | | $\infty$ | $1\,MHz$ | Hz |
| Slew Rate | $SR$ | $\infty$ | $0.5$ | $V/\mu s$ |
| Offset de entrada | $V_{OS}$ | $0$ | $\pm 1\,mV$ | V |
| Corriente de bias | $I_B$ | $0$ | $80\,nA$ | A |
| CMRR | | $\infty$ | $90\,dB$ | dB |
| PSRR | | $\infty$ | $90\,dB$ | dB |

### Impedancia de entrada ($Z_{in}$)

Es la resistencia que ve la fuente de senal entre las terminales (+) y (-):

```
  Fuente ──── Z_in ──── Op-Amp
  (V_s, R_s)   ↑
            corriente I_in
```

$$V_{id} = V_s \cdot \frac{Z_{in}}{Z_{in} + R_s}$$

- **Ideal ($Z_{in} = \infty$):** $I_{in} = 0$, no carga la fuente → $V_{id} = V_s$ (toda la senal llega al op-amp)
- **Real ($Z_{in}$ finita):** forma un divisor de voltaje con $R_s$. Si $R_s \ll Z_{in}$, el efecto es despreciable

> [!tip] Regla practica
> Para que el error sea menor al 1%: $Z_{in} > 100 \cdot R_s$
>
> Con el LM741 ($Z_{in} = 2\,M\Omega$) esto se cumple para fuentes con $R_s < 20\,k\Omega$. Para fuentes de alta impedancia (sensores piezoelectricos, electrodos) se necesitan op-amps con entrada JFET o CMOS ($Z_{in} > 10^{12}\,\Omega$).

### Impedancia de salida ($Z_{out}$)

Es la resistencia interna en serie con la fuente de voltaje de salida:

```
                  Z_out
  A_OL·Vid ──[===]──+── Vo
                    |
                   R_L
                    |
                   GND
```

$$V_o = A_{OL} \cdot V_{id} \cdot \frac{R_L}{Z_{out} + R_L}$$

- **Ideal ($Z_{out} = 0$):** la salida entrega todo el voltaje a cualquier carga
- **Real ($Z_{out}$ finita):** con carga baja se pierde voltaje. Pero con realimentacion negativa, la impedancia de salida efectiva se reduce drasticamente:

$$Z_{out(CL)} = \frac{Z_{out}}{1 + A_{OL} \cdot \beta}$$

Donde $\beta$ = fraccion de realimentacion. Con el 741: $Z_{out(CL)} \approx \frac{75}{1 + 200{,}000 \cdot \beta} < 1\,\Omega$

> [!note] Efecto de la realimentacion
> La realimentacion negativa **mejora** tanto la impedancia de entrada (la sube) como la de salida (la baja), acercando el op-amp real al comportamiento ideal.

### Ganancia de lazo abierto ($A_{OL}$) y ganancia de lazo cerrado ($K$)

**Lazo abierto** — la ganancia intrinseca del op-amp, sin realimentacion:

$$V_o = A_{OL} \cdot V_{id}$$

Es enorme pero **inestable** (varia con temperatura, frecuencia, lote de fabricacion). No se usa directamente para amplificacion lineal.

**Lazo cerrado ($K$)** — la ganancia **util**, controlada por resistencias externas mediante realimentacion negativa:

$$\boxed{K = \frac{V_o}{V_{in}}}$$

La ganancia $K$ depende **solo de los componentes externos**, no de $A_{OL}$:

| Configuracion | Ganancia $K$ | Depende de |
| ------------- | ------------ | ---------- |
| [[S04-1 Aplicaciones lineales del amplificador operacional#3. Amplificador inversor\|Inversor]] | $K = -\dfrac{R_f}{R_1}$ | $R_f$, $R_1$ |
| [[S04-1 Aplicaciones lineales del amplificador operacional#2. Amplificador no inversor\|No inversor]] | $K = 1 + \dfrac{R_f}{R_1}$ | $R_f$, $R_1$ |
| [[S04-1 Aplicaciones lineales del amplificador operacional#4. Seguidor de voltaje (buffer)\|Seguidor]] | $K = 1$ | Ninguno |

> [!success] ¿Por que $K$ no depende de $A_{OL}$?
> Con $A_{OL} \to \infty$, cualquier cambio infinitesimal en $V_{id}$ produce el voltaje de salida necesario. La realimentacion "fuerza" $V_{id} \approx 0$, y la ganancia queda determinada **solo por la red de resistencias**. Esto es lo que hace al op-amp tan util: la ganancia es **precisa y predecible**.

### Relacion entre $K$ y $A_{OL}$ (formula exacta)

Para un amplificador no inversor con $A_{OL}$ finita:

$$K_{real} = \frac{A_{OL}}{1 + A_{OL} \cdot \beta}$$

Donde $\beta = \dfrac{R_1}{R_1 + R_f}$ es la fraccion de realimentacion.

Si $A_{OL} \cdot \beta \gg 1$ (siempre que $A_{OL}$ sea grande):

$$K_{real} \approx \frac{1}{\beta} = 1 + \frac{R_f}{R_1} = K_{ideal}$$

El **error** por ganancia finita es:

$$\text{Error} = \frac{K_{ideal} - K_{real}}{K_{ideal}} \approx \frac{1}{A_{OL} \cdot \beta}$$

> [!example] Ejemplo
> Amplificador no inversor con $R_f = 9\,k\Omega$, $R_1 = 1\,k\Omega$ → $K_{ideal} = 10$, $\beta = 0.1$
> - Con LM741 ($A_{OL} = 200{,}000$): Error $= \frac{1}{200{,}000 \times 0.1} = 0.005\%$ → despreciable
> - Con op-amp de $A_{OL} = 1{,}000$: Error $= \frac{1}{1{,}000 \times 0.1} = 1\%$ → puede importar

---

## Decibeles (dB)

El decibel es una escala **logaritmica** que permite expresar ganancias muy grandes o muy pequenas de forma compacta. Existen dos formulas segun la magnitud:

### Para voltaje o corriente (amplitudes)

$$\boxed{G_{dB} = 20\log\left(\frac{V_o}{V_i}\right)}$$

Se usa $20\log$ porque voltaje y corriente son magnitudes de **amplitud**. La potencia es proporcional al cuadrado de la amplitud ($P \propto V^2$), y $\log(x^2) = 2\log(x)$, de ahi el factor 20.

### Para potencia

$$\boxed{G_{dB} = 10\log\left(\frac{P_o}{P_i}\right)}$$

Se usa $10\log$ porque la potencia ya es una magnitud de **energia por tiempo** — no necesita el factor extra.

### ¿Por que son equivalentes?

$$10\log\left(\frac{P_o}{P_i}\right) = 10\log\left(\frac{V_o^2/R}{V_i^2/R}\right) = 10\log\left(\frac{V_o}{V_i}\right)^2 = 20\log\left(\frac{V_o}{V_i}\right)$$

> [!important] Regla para no confundirlas
> - **Voltaje, corriente, ganancia de voltaje, CMRR** → $20\log$
> - **Potencia, eficiencia, relacion senal/ruido en potencia** → $10\log$

### Valores de referencia utiles

| Ganancia lineal | dB (voltaje) | Significado |
| --------------- | ------------ | ----------- |
| $1$ | $0\,dB$ | Sin ganancia ni atenuacion |
| $2$ | $6\,dB$ | Duplica el voltaje |
| $10$ | $20\,dB$ | 10 veces el voltaje |
| $100$ | $40\,dB$ | 100 veces |
| $1{,}000$ | $60\,dB$ | 1000 veces |
| $100{,}000$ | $100\,dB$ | Ganancia tipica de un op-amp |
| $0.5$ | $-6\,dB$ | Mitad del voltaje |
| $0.707$ | $-3\,dB$ | Frecuencia de corte (potencia a la mitad) |

> [!tip] El punto de $-3\,dB$
> $-3\,dB$ en voltaje equivale a $\frac{1}{\sqrt{2}} \approx 0.707$ del voltaje, que corresponde a **la mitad de la potencia** ($10\log(0.5) = -3\,dB$). Es el criterio estandar para definir el **ancho de banda** de un amplificador.

---

## Variable compleja de Laplace ($s$)

En el analisis de circuitos con capacitores e inductores (filtros, integradores, derivadores, respuesta en frecuencia), se reemplaza el dominio del tiempo por el **dominio de la frecuencia compleja** usando la variable $s$:

$$\boxed{s = \sigma + j\omega}$$

Donde:
- $\sigma$ = parte real → describe el **crecimiento o decaimiento** exponencial de la senal
- $\omega = 2\pi f$ = frecuencia angular en $rad/s$
- $j = \sqrt{-1}$ = unidad imaginaria (en electronica se usa $j$ en vez de $i$ para no confundir con corriente)

### Caso senoidal permanente ($\sigma = 0$)

Para senales senoidales en estado estable, $\sigma = 0$ y la variable se reduce a:

$$\boxed{s = j\omega = j \cdot 2\pi f}$$

Esto es lo que se usa en la practica para calcular **ganancia y fase** a una frecuencia especifica.

### Impedancias en el dominio $s$

La variable $s$ simplifica el analisis de circuitos reactivos — capacitores e inductores se tratan como **resistencias** dependientes de la frecuencia:

| Componente | Impedancia en $s$ | Impedancia en $j\omega$ | Comportamiento |
| ---------- | ------------------ | ----------------------- | -------------- |
| Resistor | $Z_R = R$ | $R$ | Constante |
| Capacitor | $Z_C = \dfrac{1}{sC}$ | $\dfrac{1}{j\omega C}$ | Baja con la frecuencia |
| Inductor | $Z_L = sL$ | $j\omega L$ | Sube con la frecuencia |

> [!note] ¿Por que es util?
> Con estas impedancias, un circuito RC o RL se analiza **igual que un circuito puramente resistivo** usando divisores de voltaje y KVL/KCL. El resultado es la **funcion de transferencia** $H(s) = V_o(s)/V_i(s)$.

### Ejemplo: integrador con op-amp

El [[S04-1 Aplicaciones lineales del amplificador operacional#8. Amplificador integrador|integrador]] tiene $R$ en la entrada y $C$ en la realimentacion. Su funcion de transferencia es:

$$H(s) = -\frac{Z_f}{Z_1} = -\frac{1/sC}{R} = -\frac{1}{sRC}$$

Sustituyendo $s = j\omega$:

$$H(j\omega) = -\frac{1}{j\omega RC}$$

- **Magnitud:** $|H| = \dfrac{1}{\omega RC}$ → la ganancia **disminuye** con la frecuencia (filtro pasa-bajos)
- **Fase:** $\angle H = -90° - 180° = -270°$ (o equivalente $+90°$)

### Ejemplo: derivador con op-amp

El [[S04-1 Aplicaciones lineales del amplificador operacional#7. Amplificador derivador|derivador]] tiene $C$ en la entrada y $R$ en la realimentacion:

$$H(s) = -\frac{R}{1/sC} = -sRC$$

Sustituyendo $s = j\omega$:

$$H(j\omega) = -j\omega RC$$

- **Magnitud:** $|H| = \omega RC$ → la ganancia **crece** con la frecuencia (filtro pasa-altos)
- **Fase:** $\angle H = +90° - 180° = -90°$

> [!abstract] Resumen de correspondencias
>
> | Operacion en tiempo | Equivalente en $s$ |
> | ------------------- | ------------------ |
> | $\dfrac{d}{dt}$ (derivar) | Multiplicar por $s$ |
> | $\displaystyle\int dt$ (integrar) | Dividir por $s$ |
> | Senal constante (DC) | $s = 0$ |
> | Senal senoidal a frecuencia $f$ | $s = j \cdot 2\pi f$ |

---

## Parametros fundamentales del op-amp

### Ganancia de voltaje de lazo abierto ($A_{OL}$)

Es la ganancia **intrinseca** del op-amp, sin ningun circuito de realimentacion externo. Amplifica la diferencia entre las entradas:

$$\boxed{V_o = A_{OL}(V_1 - V_2) = A_{OL} \cdot V_{id}}$$

Donde:
- $V_o$ = voltaje de salida
- $A_{OL}$ = ganancia de lazo abierto (open loop), tipicamente $10^5$ a $10^6$
- $V_{id} = V_1 - V_2$ = [[S03-1 Amplificador diferencial con BJT PNP#Tensiones de entrada|tension diferencial de entrada]]

En decibeles:

$$A_{OL(dB)} = 20\log(A_{OL})$$

> [!tip] Consecuencia practica
> Como $A_{OL}$ es enorme (~$10^5$), basta una diferencia de **microvoltios** entre las entradas para que la salida se sature. Por eso el op-amp **casi nunca se usa en lazo abierto** para amplificacion lineal.

### Ganancia en modo comun ($A_{cm}$)

Es la ganancia que el op-amp aplica a la senal que aparece **igual en ambas entradas** (ruido, interferencia):

$$V_{o(cm)} = A_{cm} \cdot V_{ic}$$

Donde:
- $V_{ic} = \dfrac{V_1 + V_2}{2}$ = [[S03-1 Amplificador diferencial con BJT PNP#Tensiones de entrada|tension en modo comun]]
- $A_{cm}$ = ganancia en modo comun → idealmente **cero**

En un op-amp real, $A_{cm}$ no es cero debido a asimetrias internas en el [[S03-1 Amplificador diferencial con BJT PNP|par diferencial de entrada]] (diferencias en $\beta$, $R_C$, $V_{BE}$ entre los transistores).

### Salida total (considerando ambas ganancias)

$$\boxed{V_o = A_{OL} \cdot V_{id} + A_{cm} \cdot V_{ic}}$$

El primer termino es la **senal util** (lo que queremos amplificar). El segundo termino es **ruido/error** (lo que queremos rechazar).

---

### CMRR (Factor de Rechazo en Modo Comun)

Mide la capacidad del op-amp de **amplificar la senal diferencial** y **rechazar la senal comun**:

$$\boxed{CMRR = \frac{|A_{OL}|}{|A_{cm}|}}$$

En decibeles:

$$CMRR_{dB} = 20\log\left(\frac{|A_{OL}|}{|A_{cm}|}\right) = A_{OL(dB)} - A_{cm(dB)}$$

### ¿Que significa en la practica?

El CMRR indica cuanto se **atenua** una senal no deseada que aparece igual en ambas entradas:

| CMRR (dB) | Rechazo de modo comun | Calidad |
| ---------- | --------------------- | ------- |
| 60 dB | $1000:1$ | Minimo aceptable |
| 80 dB | $10{,}000:1$ | Bueno (LM741) |
| 100 dB | $100{,}000:1$ | Muy bueno |
| 120 dB | $1{,}000{,}000:1$ | Excelente (amp. de instrumentacion) |

> [!example] Ejemplo numerico
> Un op-amp con $CMRR = 80\,dB$ recibe una senal diferencial de $1\,mV$ y ruido en modo comun de $1\,V$:
> - Senal amplificada: $A_{OL} \cdot 1\,mV$ → la senal util
> - Ruido amplificado: $A_{cm} \cdot 1\,V = \frac{A_{OL}}{10{,}000} \cdot 1\,V$ → atenuado $10{,}000\times$
> 
> El ruido de $1\,V$ se reduce a la equivalencia de $0.1\,mV$ referido a la entrada, 10 veces menor que la senal.

### ¿Donde se aplica?

| Aplicacion | ¿Por que importa el CMRR? |
| ---------- | ------------------------- |
| **Instrumentacion medica** (ECG, EEG) | La senal biologica es de $\mu V$-$mV$, el ruido de 60Hz de la red electrica aparece igual en ambos electrodos |
| **Celdas de carga / strain gauges** | Variaciones de temperatura afectan ambos brazos del puente por igual |
| **Audio profesional** (lineas balanceadas) | El ruido electromagnetico captado por el cable aparece en modo comun |
| **Sensores industriales** | Lazos de tierra y EMI generan tensiones comunes en lineas de senal |
| **[[S04-1 Aplicaciones lineales del amplificador operacional#6. Amplificador diferencial (restador)|Amplificador diferencial con op-amp]]** | La condicion de balance $R_1/R_2 = R_3/R_4$ maximiza el CMRR del circuito |

> [!success] Regla general
> Mientras mas pequena sea la senal util comparada con el ruido comun, **mas alto debe ser el CMRR**. Por eso en instrumentacion medica se usan amplificadores de instrumentacion (3 op-amps) con $CMRR > 100\,dB$.

---

## Otros parametros del op-amp real

### Voltaje de offset de entrada ($V_{OS}$)

Es el pequeno voltaje diferencial que se debe aplicar en las entradas para que la salida sea **exactamente cero**. Existe porque los transistores del par diferencial interno no son perfectamente identicos.

$$V_o = A_{OL}(V_{id} + V_{OS})$$

- Tipico: $\pm 1\text{-}5\,mV$ (LM741), $\pm 5\text{-}25\,\mu V$ (op-amps de precision como OP07)
- Efecto: en un amplificador con ganancia $A_v$, el offset se amplifica → $V_{o(error)} = A_v \cdot V_{OS}$
- Solucion: pines de ajuste de offset (null), o capacitor de acople AC si la senal es solo alterna

### Corrientes de polarizacion de entrada ($I_B$)

Los transistores de entrada necesitan una pequena corriente de base para operar. Estas corrientes fluyen **hacia dentro** (NPN) o **hacia fuera** (PNP) de las terminales de entrada.

$$\boxed{I_B = \frac{I_{B+} + I_{B-}}{2}}$$

- Tipico: $80\,nA$ (LM741 con BJT), $< 1\,pA$ (op-amps con JFET o CMOS)
- Efecto: producen caidas de voltaje en las resistencias del circuito, generando errores en la salida

**Corriente de offset de entrada:**

$$\boxed{I_{OS} = |I_{B+} - I_{B-}|}$$

Es la **diferencia** entre las dos corrientes de polarizacion. Causa error incluso si se compensa $I_B$.

> [!tip] Compensacion de $I_B$
> Se agrega una resistencia $R_{comp} = R_1 \| R_f$ en la entrada no inversora (+) para que ambas corrientes de bias produzcan la **misma caida de voltaje**, cancelando su efecto. Solo queda el error por $I_{OS}$.

### Producto ganancia-ancho de banda (GBW)

En un op-amp con compensacion interna (como el 741), la ganancia cae $-20\,dB/dec$ desde el polo dominante. El producto de la ganancia por el ancho de banda es **constante**:

$$\boxed{GBW = A_v \cdot BW = \text{constante}}$$

$$BW = \frac{GBW}{A_v}$$

Donde:
- $GBW$ = producto ganancia-ancho de banda (tipico: $1\,MHz$ para LM741)
- $A_v$ = ganancia de lazo cerrado
- $BW$ = ancho de banda a $-3\,dB$

> [!example] Ejemplo
> Con un LM741 ($GBW = 1\,MHz$):
> - Si $A_v = 10$ → $BW = 100\,kHz$
> - Si $A_v = 100$ → $BW = 10\,kHz$
> - Si $A_v = 1$ (buffer) → $BW = 1\,MHz$
> 
> A mayor ganancia, menor ancho de banda. Es un **compromiso** inevitable.

### Slew Rate (SR)

Es la **maxima velocidad de cambio** de la salida, medida en $V/\mu s$:

$$\boxed{SR = \left(\frac{dV_o}{dt}\right)_{max}}$$

- Tipico: $0.5\,V/\mu s$ (LM741), $13\,V/\mu s$ (TL072)
- Limita la **frecuencia maxima** a la que el op-amp puede entregar una senal sinusoidal sin distorsion:

$$\boxed{f_{max} = \frac{SR}{2\pi \cdot V_{p}}}$$

Donde $V_p$ = amplitud pico de la salida.

> [!example] Ejemplo
> LM741 con $SR = 0.5\,V/\mu s$ y salida de $V_p = 10\,V$:
> $$f_{max} = \frac{0.5 \times 10^6}{2\pi \times 10} = 7.96\,kHz$$
> Por encima de esta frecuencia, la salida se **distorsiona** (se vuelve triangular en vez de sinusoidal). Esto se llama **slew rate limiting**.

### PSRR (Rechazo de fuente de alimentacion)

Mide cuanto afectan las variaciones de la fuente de alimentacion ($\Delta V_{CC}$) a la salida:

$$\boxed{PSRR = \frac{\Delta V_{CC}}{\Delta V_{OS}}}$$

En decibeles: $PSRR_{dB} = 20\log(PSRR)$

- Tipico: $90\,dB$ (LM741)
- Un alto PSRR significa que el ripple de la fuente **no afecta** la salida

---

## Modelo de circuito equivalente

El op-amp se puede modelar como un circuito con sus parametros reales:

```
                    Ro
  V1 (+)---+       +--[===]--+--- Vo
           |       |         |
          Zi    A_OL·Vid    |
           |    (fuente     |
  V2 (-)---+    dependiente)|
           |       |         |
          GND     GND       GND
```

### Modelo simplificado (3 elementos)

| Elemento | Simbolo | Funcion |
| -------- | ------- | ------- |
| Impedancia de entrada | $Z_i$ | Resistencia entre las terminales (+) y (-) |
| Fuente de voltaje dependiente | $A_{OL} \cdot V_{id}$ | Modela la amplificacion |
| Impedancia de salida | $R_o$ | Resistencia en serie con la salida |

La salida con carga:

$$V_o = A_{OL} \cdot V_{id} \cdot \frac{R_L}{R_o + R_L}$$

Con $R_o \ll R_L$ (casi siempre): $V_o \approx A_{OL} \cdot V_{id}$

### Modelo completo (incluye imperfecciones)

```
              Ro
  +---[Zi]---+--[===]--+--- Vo
  |          |         |
 V1(+)    A_OL·Vid    |
  |       A_cm·Vic    |
  |          |         |
  +--[Zi]---+         |
  |                    |
 V2(-)                |
  |                    |
  +--- Vos ---+       GND
  |           |
  +-- IB+ →  |
  |           |
  +-- IB- →  |
```

Este modelo agrega:
- $V_{OS}$: fuente de offset en serie con la entrada
- $I_{B+}$, $I_{B-}$: fuentes de corriente en las entradas
- $A_{cm} \cdot V_{ic}$: componente de ganancia en modo comun

> [!abstract] Resumen de parametros del op-amp real
>
> | Parametro | Simbolo | LM741 | Ideal |
> | --------- | ------- | ----- | ----- |
> | Ganancia lazo abierto | $A_{OL}$ | $200{,}000$ | $\infty$ |
> | Impedancia de entrada | $Z_i$ | $2\,M\Omega$ | $\infty$ |
> | Impedancia de salida | $R_o$ | $75\,\Omega$ | $0$ |
> | Offset de entrada | $V_{OS}$ | $\pm 1\,mV$ | $0$ |
> | Corriente de bias | $I_B$ | $80\,nA$ | $0$ |
> | CMRR | | $90\,dB$ | $\infty$ |
> | PSRR | | $90\,dB$ | $\infty$ |
> | GBW | | $1\,MHz$ | $\infty$ |
> | Slew Rate | $SR$ | $0.5\,V/\mu s$ | $\infty$ |

---

## Saturacion

La salida no puede exceder los voltajes de alimentacion:

$$V^- + V_{sat} \leq V_o \leq V^+ - V_{sat}$$

Donde $V_{sat} \approx 1\text{-}2\,V$ para op-amps convencionales (como el 741). En op-amps **rail-to-rail**, $V_{sat} \approx 0$.

```
Vo
 ^
 |         ___________  V+ - Vsat (saturacion positiva)
 |        /
 |       / ← pendiente = A_OL (muy grande)
 |      /
 |_____/______________ → Vd = V1 - V2
 |    /
 |   /
 |__/_______________   V- + Vsat (saturacion negativa)
```

---

## Reglas de analisis (op-amp ideal con realimentacion negativa)

Cuando el op-amp opera en **lazo cerrado** con realimentacion negativa, se aplican dos reglas fundamentales:

> [!success] Regla 1: Cortocircuito virtual
> $$V_1 = V_2$$
> La diferencia de voltaje entre las entradas es **cero** (porque $A_{OL} \to \infty$).

> [!success] Regla 2: Corriente de entrada cero
> $$I_+ = I_- = 0$$
> No entra corriente por ninguna terminal de entrada (porque $Z_{in} \to \infty$).

> [!warning] Condicion necesaria
> Estas reglas **solo son validas** cuando hay **realimentacion negativa** (la salida se conecta de vuelta a la entrada inversora). Sin realimentacion, el op-amp satura.

---

## Modos de operacion

| Modo | Realimentacion | Comportamiento | Aplicacion |
| ---- | -------------- | -------------- | ---------- |
| **Lazo abierto** | Ninguna | Saturacion (+/−) | Comparadores |
| **Lazo cerrado lineal** | Negativa | Amplificacion controlada | Amplificadores, filtros |
| **Lazo cerrado no lineal** | Positiva | Conmutacion, oscilacion | Schmitt trigger, osciladores |

---

## Alimentacion

### Fuente simetrica (dual supply)

```
     +Vcc (+15V)
       |
    [Op-Amp]
       |
     -Vcc (-15V)
```

- Permite senales positivas y negativas en la salida
- Uso tipico: circuitos de audio, instrumentacion

### Fuente simple (single supply)

```
     +Vcc (+5V)
       |
    [Op-Amp]
       |
      GND (0V)
```

- La salida solo puede ser positiva (entre GND y $V_{CC}$)
- Se debe **polarizar** la entrada a $V_{CC}/2$ para centrar la senal
- Uso tipico: circuitos digitales, microcontroladores

---

## Op-amps comunes

| Modelo | $A_{OL}$ (dB) | GBW | Slew Rate | Alimentacion | Nota |
| ------ | -------------- | --- | --------- | ------------ | ---- |
| LM741 | 106 | 1 MHz | 0.5 V/µs | ±15V | Clasico, educativo |
| LM358 | 100 | 1 MHz | 0.3 V/µs | 3-32V | Fuente simple, bajo costo |
| LM324 | 100 | 1 MHz | 0.5 V/µs | 3-32V | Cuadruple, entrada PNP |
| TL072 | 106 | 3 MHz | 13 V/µs | ±18V | JFET, alta $Z_{in}$ |
| OPA2134 | 120 | 8 MHz | 20 V/µs | ±18V | Audio de alta fidelidad |

## Bibliografia

- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson.
- Sedra, A. & Smith, K. *Microelectronic Circuits*. Oxford University Press.
