---
title: "Comparadores y Schmitt trigger - ejercicios resueltos"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 7
orden: 1
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tipo/ejercicio
  - tema/comparador
  - tema/schmitt-trigger
  - tema/histeresis
  - tema/diseno-de-circuitos
date: 2026-05-04
---

> [!info] Continuacion de la clase
> Esta nota desarrolla problemas de **diseno y analisis** de comparadores y Schmitt triggers. La teoria correspondiente esta en [[S06-1 Amplificadores lineales y no lineales#Parte II: Aplicaciones no lineales|S06-1]] secciones 1 y 2.

## Resumen rapido de formulas

| Configuracion | Umbrales | Histeresis $\Delta V_H$ |
| ------------- | -------- | ----------------------- |
| Comparador simple (sin realim.) | $V_{REF}$ unico | 0 |
| Schmitt **inversor** ($V_{in}$ a (-)) | $V_{UT,LT} = \pm V_{sat}\dfrac{R_1}{R_1+R_2}$ | $2V_{sat}\dfrac{R_1}{R_1+R_2}$ |
| Schmitt **no inversor** ($V_{in}$ a (+)) | $V_{UT,LT} = \mp V_{sat}\dfrac{R_1}{R_2}$ | $2V_{sat}\dfrac{R_1}{R_2}$ |
| Schmitt inversor con $V_{REF}$ | $V_{UT,LT} = V_{REF}\dfrac{R_2}{R_1+R_2} \pm V_{sat}\dfrac{R_1}{R_1+R_2}$ | $2V_{sat}\dfrac{R_1}{R_1+R_2}$ |

> [!note] Convencion
> En esta seccion $V_{sat} \approx V_{cc} - 1.5$ V para op-amps tipo 741 (saturacion ~$\pm 13.5$ V con $\pm 15$ V de alimentacion). Para op-amps **rail-to-rail** $V_{sat} \approx V_{cc}$.

---

## Ejercicio 1: Diseno de Schmitt trigger inversor

**Enunciado.** Disenar un Schmitt trigger inversor que conmute con umbrales $V_{UT} = +2$ V y $V_{LT} = -2$ V. La alimentacion es $\pm 15$ V con un op-amp 741 ($V_{sat} = \pm 13.5$ V). Calcular $R_1$ y $R_2$.

### Datos

- $V_{UT} = +2$ V
- $V_{LT} = -2$ V
- $V_{sat} = 13.5$ V
- Asumir $R_1 + R_2 = 100$ k$\Omega$ como criterio de diseno (impedancia razonable, baja corriente de polarizacion del op-amp).

### Topologia

```
              R2
       +----[===]----+
       |             |
       |        (-) \|
  Vin -+-------------+
                      >----- Vo
                 (+) /|
                      |
                     R1
                      |
                     GND
```

### Desarrollo

Para la configuracion inversora con realimentacion positiva al terminal (+):

$$V_+ = V_o \cdot \frac{R_1}{R_1 + R_2}$$

Cuando $V_o = +V_{sat}$, el umbral en (+) es $V_{UT}$; cuando $V_o = -V_{sat}$, el umbral es $V_{LT}$:

$$V_{UT} = V_{sat} \cdot \frac{R_1}{R_1 + R_2}$$

Despejando la relacion:

$$\frac{R_1}{R_1 + R_2} = \frac{V_{UT}}{V_{sat}} = \frac{2}{13.5} = 0.1481$$

Imponiendo $R_1 + R_2 = 100$ k$\Omega$:

$$R_1 = 0.1481 \times 100\,\text{k}\Omega = 14.81\,\text{k}\Omega \approx 15\,\text{k}\Omega$$

$$R_2 = 100 - 14.81 = 85.19\,\text{k}\Omega \approx 82\,\text{k}\Omega \text{ (valor estandar E12)}$$

### Verificacion con valores estandar ($R_1 = 15$ k, $R_2 = 82$ k)

$$\beta = \frac{R_1}{R_1 + R_2} = \frac{15}{97} = 0.1546$$

$$V_{UT} = 13.5 \times 0.1546 = 2.087\,\text{V}, \quad V_{LT} = -2.087\,\text{V}$$

$$\Delta V_H = V_{UT} - V_{LT} = 4.17\,\text{V}$$

> [!success] Resultado
> $R_1 = 15$ k$\Omega$, $R_2 = 82$ k$\Omega$. Umbrales reales: $\pm 2.09$ V (error +4.5% respecto a la especificacion, aceptable con tolerancia 5% de los resistores).

### Forma de onda esperada

```
  Vin (entrada con ruido)              Vo (salida limpia)
       |                                    |
   +5V |     ___                       +Vsat|________
       |    /   \                           |        |____
       |   /     \                          |        |    
   +2V-|-+-------+----+--------- t          |        |    +Vsat
       |/         \    \                    |________|____|____
   -2V-|-----------+----+----+---            |             |
       |            \    \   /                |             |
       |             \    \_/             -Vsat|             |________
   -5V |              \___/                    |
```

> [!important] Por que la histeresis elimina ruido
> Si $V_{in}$ tiene ruido de $\pm 100$ mV alrededor del umbral, sin histeresis el comparador conmuta varias veces (chattering). Con $\Delta V_H = 4$ V, una vez que conmuto a $+V_{sat}$, $V_{in}$ debe caer mas de 4 V para volver a conmutar — el ruido de 100 mV ya no afecta.

---

## Ejercicio 2: Schmitt trigger no inversor con $V_{REF} \neq 0$

**Enunciado.** En el circuito de la figura, $V_{REF} = +3$ V, $R_1 = 10$ k$\Omega$, $R_2 = 47$ k$\Omega$, $V_{sat} = \pm 13.5$ V. Calcular $V_{UT}$, $V_{LT}$ y $\Delta V_H$. Trazar la curva de transferencia.

### Topologia

```
       R1            R2
  Vin-[===]-+--[===]-+
            |        |
            |   (-) \|
            |        +
            |        >---- Vo
        +---|--(+) /
        |   |
        |  Vref
       Vref
```

### Desarrollo

En la version no inversora, la condicion de conmutacion se obtiene aplicando superposicion en el nodo (+):

$$V_+ = V_{in}\cdot\frac{R_2}{R_1+R_2} + V_o\cdot\frac{R_1}{R_1+R_2}$$

La conmutacion ocurre cuando $V_+ = V_{REF}$:

$$V_{in,th} = V_{REF}\cdot\frac{R_1+R_2}{R_2} - V_o\cdot\frac{R_1}{R_2}$$

Sustituyendo $V_o = \pm V_{sat}$:

$$V_{UT} = V_{REF}\cdot\frac{R_1+R_2}{R_2} + V_{sat}\cdot\frac{R_1}{R_2}$$

(transicion $V_o: -V_{sat} \to +V_{sat}$, ocurre cuando $V_{in}$ **sube** lo suficiente)

$$V_{LT} = V_{REF}\cdot\frac{R_1+R_2}{R_2} - V_{sat}\cdot\frac{R_1}{R_2}$$

> [!warning] Signos en Schmitt no inversor
> En la version no inversora, **al subir** $V_{in}$ por encima de $V_{UT}$ la salida pasa de $-V_{sat}$ a $+V_{sat}$ (no al reves como en el inversor).

### Calculos numericos

$$\frac{R_1+R_2}{R_2} = \frac{57}{47} = 1.2128, \quad \frac{R_1}{R_2} = \frac{10}{47} = 0.2128$$

$$V_{UT} = 3 \times 1.2128 + 13.5 \times 0.2128 = 3.638 + 2.872 = 6.51\,\text{V}$$

$$V_{LT} = 3 \times 1.2128 - 13.5 \times 0.2128 = 3.638 - 2.872 = 0.766\,\text{V}$$

$$\Delta V_H = V_{UT} - V_{LT} = 5.74\,\text{V}$$

> [!success] Resultado
> $V_{UT} = 6.51$ V, $V_{LT} = 0.77$ V, ancho de histeresis $\approx 5.74$ V. Util como detector de bateria semi-cargada: dispara alarma cuando bateria sube de 6.5 V (carga) y la libera solo si baja de 0.77 V.

### Curva de transferencia

```
           Vo
            |
      +Vsat |              +-----+
            |              |     |
            |              |     |
      ------+--------------+--+--+----- Vin
            |              |  |  |
            |              |  |  |
            |              |  |  |
      -Vsat +--+-----------+
                            |
                          VLT  VUT
                          0.77 6.51
```

---

## Ejercicio 3: Detector de cruce por cero con histeresis para senal con ruido

**Enunciado.** Una senal senoidal $V_{in}(t) = 5\sin(2\pi 60 t)$ V tiene ruido superpuesto de $\pm 80$ mV pico-pico cerca del cruce por cero. Disenar un detector de cruce por cero con histeresis que entregue una salida cuadrada limpia (sin chattering). Determinar $R_1$ y $R_2$ para garantizar inmunidad al ruido. Op-amp 741 con $\pm 15$ V, $V_{sat} = \pm 13.5$ V.

### Criterio de diseno

La histeresis debe ser **mayor** al ruido pico-pico para evitar conmutaciones espurias. Margen de seguridad x3:

$$\Delta V_H \geq 3 \times V_{ruido,pp} = 3 \times 0.16 = 0.48\,\text{V}$$

Eligiendo $\Delta V_H = 0.5$ V (centrada en cero, $V_{REF} = 0$):

$$\Delta V_H = 2 V_{sat} \cdot \frac{R_1}{R_1+R_2}$$

$$\frac{R_1}{R_1+R_2} = \frac{0.5}{2 \times 13.5} = 0.01852$$

Eligiendo $R_2 = 100$ k$\Omega$ (estandar):

$$R_1 = R_2 \cdot \frac{0.01852}{1 - 0.01852} = 100 \times 0.01887 = 1.89\,\text{k}\Omega$$

Valor estandar E12: $R_1 = 1.8$ k$\Omega$.

### Verificacion

$$\beta = \frac{1.8}{101.8} = 0.01768, \quad \Delta V_H = 2 \times 13.5 \times 0.01768 = 0.477\,\text{V}$$

$$V_{UT} = +0.239\,\text{V}, \quad V_{LT} = -0.239\,\text{V}$$

> [!success] Resultado
> $R_1 = 1.8$ k$\Omega$, $R_2 = 100$ k$\Omega$. Umbrales $\pm 0.24$ V — el ruido de $\pm 80$ mV no alcanza para hacer conmutar erroneamente.

### Implicancia en la senal de salida

La salida cuadrada conmuta:
- **Subida positiva:** cuando $V_{in}$ cruza $+0.24$ V — un poco antes del cruce por cero real
- **Bajada negativa:** cuando $V_{in}$ cruza $-0.24$ V

Esto introduce un **error de fase** en el detector. Para senoidal con $A = 5$ V:

$$\phi_{error} = \arcsin\left(\frac{0.24}{5}\right) = 2.75°$$

A 60 Hz, eso equivale a $\Delta t = 2.75/360 \times 16.67\,\text{ms} = 127\,\mu s$. Despreciable para mediciones de frecuencia, pero relevante en aplicaciones de PLL de alta precision donde se usa un comparador rapido **sin** histeresis (LM311) y filtrado pasa-bajos previo al ruido.

---

## Ejercicio 4: Comparador de ventana

**Enunciado.** Disenar un **detector de ventana** que active una alarma cuando $V_{in}$ esta **fuera** del rango $[2\,\text{V}, 4\,\text{V}]$. La salida $V_o$ debe ser:
- $V_o = 0$ V (LOW) cuando $2 \leq V_{in} \leq 4$ V (dentro de ventana, OK)
- $V_o = +5$ V (HIGH) cuando $V_{in} < 2$ V o $V_{in} > 4$ V (fuera, ALARMA)

### Solucion: dos comparadores con salida combinada (OR-cableado)

Se usan **dos op-amps** configurados como comparadores con salida en **colector abierto** (LM311 o LM393, no 741) y un pull-up:

```
   +5V
    |
   [Rp]
    |
    +------------------+----- Vo (alarma)
    |                  |
    |    +Vcc          |    +Vcc
    |     |            |     |
   (+)\   |           (+)\   |
       \  |               \  |
        +-+ U1: Vin > 4    +-+ U2: Vin < 2
       /  |               /  |
   (-)/   |           (-)/   |
    | 4V  |            | 2V  |
    |    -Vcc          |    -Vcc
   Vin ---+--------------+
```

- **U1 (comparador alto):** $V_+ = V_{in}$, $V_- = +4$ V. Si $V_{in} > 4$ V, salida = abierto (HIGH via pull-up); si $V_{in} \leq 4$ V, salida = LOW (saturada a tierra).
- **U2 (comparador bajo):** $V_+ = +2$ V, $V_- = V_{in}$. Si $V_{in} < 2$ V, salida = abierto (HIGH); si $V_{in} \geq 2$ V, salida = LOW.
- **OR-cableado:** ambas salidas a colector abierto en el mismo nodo: si **cualquiera** esta LOW, $V_o = $ LOW. Solo cuando ambas estan HIGH (ambas dentro de ventana → ambas saturadas... ¡esperamos!) — ¡hay que invertir la logica!

> [!warning] Logica correcta del detector de ventana
> El analisis anterior tiene un error de signo. La logica correcta:
>
> - U1 con $V_{REF,1} = 4$ V en (-), $V_{in}$ en (+). Salida $= 1$ si $V_{in} > 4$ V.
> - U2 con $V_{REF,2} = 2$ V en (+), $V_{in}$ en (-). Salida $= 1$ si $V_{in} < 2$ V.
> - $V_o = U_1 \lor U_2$ (OR logico). Con colector abierto y pull-up, el nodo se hace **HIGH si cualquiera esta abierto** (pulled up); LOW solo si los dos comparadores estan saturados (ambos $= 0$ → ambos transistores conducen → tirando a GND). Esto implementa **OR de las salidas no-saturadas**.

### Generacion de los voltajes de referencia

Con un divisor desde $+5$ V usando 3 resistencias en serie:

$$V_{REF,2} = 5 \cdot \frac{R_a}{R_a + R_b + R_c} = 2\,\text{V}$$

$$V_{REF,1} = 5 \cdot \frac{R_a + R_b}{R_a + R_b + R_c} = 4\,\text{V}$$

Eligiendo $R_a + R_b + R_c = 50$ k$\Omega$ (corriente del divisor = 100 $\mu$A):

$$R_a = \frac{2}{5} \times 50 = 20\,\text{k}\Omega$$

$$R_a + R_b = \frac{4}{5} \times 50 = 40\,\text{k}\Omega \Rightarrow R_b = 20\,\text{k}\Omega$$

$$R_c = 50 - 40 = 10\,\text{k}\Omega$$

### Verificacion con tabla de verdad

| $V_{in}$ | U1 (alto) | U2 (bajo) | $V_o$ | Estado |
| -------- | --------- | --------- | ----- | ------ |
| 1 V      | 0 (sat)   | 1 (open)  | HIGH  | ALARMA inferior |
| 2 V      | 0 (sat)   | 0 (sat)   | LOW   | OK (limite) |
| 3 V      | 0 (sat)   | 0 (sat)   | LOW   | OK |
| 4 V      | 0 (sat)   | 0 (sat)   | LOW   | OK (limite) |
| 5 V      | 1 (open)  | 0 (sat)   | HIGH  | ALARMA superior |

> [!success] Resultado
> Componentes: 2 comparadores LM393, divisor de referencia ($R_a = R_b = 20$ k$\Omega$, $R_c = 10$ k$\Omega$), pull-up $R_p = 10$ k$\Omega$. Aplicacion tipica: monitor de fuente de alimentacion (alarma si $V_{cc}$ sale del rango 2-4 V de tolerancia para un sensor 0-5 V).

> [!example] Aplicacion: monitor de tension de bateria
> Para una bateria de auto (12 V nominal), un detector de ventana con limites 11.5 V (descargada) y 14.5 V (sobrecarga del alternador) protege la electronica. Solo se necesita escalar $V_{in}$ con un divisor previo para entrar en el rango del LM393.

---

## Resumen del flujo de diseno

```
1. Especificar VUT, VLT (umbrales deseados) o ΔVH minimo (criterio de ruido)
   ↓
2. Elegir topologia (inversora si Vin va a (-), no inversora si va a (+))
   ↓
3. Aplicar formula del divisor:
   - Inversor:  R1/(R1+R2) = VUT/Vsat
   - No inversor:  R1/R2 = VUT/Vsat
   ↓
4. Imponer impedancia total (10-100 kΩ tipico) y resolver R1, R2
   ↓
5. Aproximar a valores estandar E12 y verificar tolerancia
   ↓
6. Si se requiere bias VREF != 0, anadir divisor en el otro terminal
```

## Bibliografia

- Sedra, A. & Smith, K. *Microelectronic Circuits* (7a ed.). Oxford University Press. Cap. 18, secs. 18.5-18.6.
- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos* (10a ed.). Pearson. Cap. 14, sec. 14.5.
- Coughlin, R. & Driscoll, F. *Operational Amplifiers and Linear Integrated Circuits* (6a ed.). Prentice Hall. Cap. 4 (comparadores), Cap. 5 (Schmitt).
- Universidad de Cantabria. *Electronica Basica - Hoja de problemas A.IV*. OCW. https://ocw.unican.es/
