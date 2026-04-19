---
title: "Eficiencia de los amplificadores y circuitos resonantes"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 4
orden: 2
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/eficiencia
  - tema/amplificador-clase-a
  - tema/amplificador-clase-b
  - tema/amplificador-clase-c
  - tema/distorsion-armonica
  - tema/circuito-resonante
  - tema/factor-de-calidad
date: 2026-04-13
---

## Transmisor de AM (saberes previos)

Un transmisor de AM se compone de tres bloques principales:

**Portadora:**
1. RF carrier oscillator
2. Buffer amplifier
3. Carrier drive

**Audio:**
1. Modulating signal source
2. Band pass filter
3. Preamplifier
4. Modulating signal driver

**Amplificador de RF:**
1. Modulador
2. Band Pass filter
3. Linear Intermediate P.A.
4. Linear P.A.
5. Band Pass filter
6. Coupling Network
7. Antena

## Amplificadores de radiofrecuencia

El objetivo del amplificador es amplificar la senal del oscilador hasta niveles necesarios para ser considerada una senal de portadora suficiente para modular un transmisor. Importa mucho la **eficiencia** del amplificador, la cual es una relacion entre la potencia de RF y la potencia de polarizacion:

$$\eta = \frac{P_{RF}}{P_{CC}}$$

Donde:
- $P_{RF}$ = potencia de salida en RF (entregada a la carga $R_L$)
- $P_{CC}$ = potencia suministrada por la fuente DC
- $P_{eRF}$ = potencia de entrada RF
- $P_{perd}$ = potencia de perdidas (disipacion)

### Buffer amplifier

El amplificador de senal de RF se modela con impedancias de entrada $Z_e$, salida $Z_s$ y carga $Z_L$.

**Concepto de ganancia de potencia:**

$$p_e = (i_{e_{ef}})^2 \cdot \text{Re}[Z_e]$$

$$p_s = (i_{s_{ef}})^2 \cdot \text{Re}[Z_L]$$

$$G_p = \frac{p_s}{p_e}$$

### Clasificacion por angulo de conduccion

Hay varias clases de amplificadores (A, B, AB, C) definidos por el tipo de polarizacion y la region de operacion del transistor:

| Clase | Angulo de conduccion | Eficiencia maxima |
| ----- | -------------------- | ----------------- |
| A     | 360°                 | < 50%             |
| AB    | 180° - 360°          | < 60%             |
| B     | 180°                 | < 78.5%           |
| C     | < 180°               | < 100%            |
| D     | Conmutacion          | = 100%            |

### Eficiencia

Un amplificador es eficiente cuando toda la potencia continua se transforma en potencia alterna. Eficiencia quiere decir que el amplificador de RF disipe muy poco calor.

$$\text{Eficiencia} = \frac{P_{OUT}}{P_{IN}} \times 100\%$$

## Amplificador Clase A

El amplificador de clase A conduce **360 grados**. El punto "Q" esta activo y siempre hay corriente de colector aunque no se aplique senal, lo que representa una perdida continua de potencia.

La potencia de un amplificador la suministra la fuente $V_{CC}$. Cuando no hay senal de entrada, el consumo de corriente DC es la corriente de polarizacion de colector $I_{CQ}$, por lo tanto la potencia que consume el amplificador es:

$$P_{DC} = V_{CC} \times I_{CQ}$$

### Eficiencia maxima del clase A

La maxima potencia de salida esta dada por el valor de la tension y corriente eficaz de salida comparado con la potencia $P_{DC}$ continua aplicada:

$$P_{out} = V_{rms} \cdot I_{rms} = \frac{\hat{V}}{\sqrt{2}} \cdot \frac{\hat{I}}{\sqrt{2}} = 0.5 \, V_{CEQ} \, I_{CQ}$$

$$P_{DC} = V_{CC} \times I_{CQ} = 2 \, V_{CEQ} \, I_{CQ}$$

El rendimiento maximo es entonces:

$$\%\eta(\text{max}) = \frac{P_{out}}{P_{DC}} \times 100\% = \frac{0.5 \, V_{CEQ} \, I_{CQ}}{2 \, V_{CEQ} \, I_{CQ}} \times 100\% = 25\%$$

$$\%\eta(\text{disipacion}) = 75\% \quad \text{(calor)}$$

> [!important] Conclusion Clase A
> El amplificador clase A solo tiene una eficiencia del 25%. El 75% es calor del 100% de energia suministrada por la fuente. Solo se obtiene 25% de potencia util.

### Ejercicio: Eficiencia clase A

Calcular la eficiencia del amplificador que utiliza una fuente de poder DC de 12 VDC, el transistor es un 2N2222, siendo $R_L = 1k$, $R_E = 200$, $R_1 = 500K$, $R_2 = 1M$.

**Solucion:**

$$P_{out} = V_{rms} \cdot I_{rms} = 0.5 \times \frac{12}{2} \times \frac{12mA}{2} = 18 \text{ mW}$$

$$P_{DC} = V_{CC} \times I_C = 12 \times 12\text{mA} = 144 \text{ mW}$$

$$\%\eta(\text{max}) = \frac{18}{144} \times 100\% = 12.5\%$$

## Amplificador Clase B

El amplificador clase B se caracteriza porque cada transistor se encarga de amplificar la senal en la mitad de su periodo (**180°**). En la etapa de salida ambas mitades de la onda de senal se combinan juntas para producir la forma de onda completa.

Su eficiencia es mucho mayor que la del amplificador de clase A. Sin embargo, tiene la desventaja en la linealidad: produce **distorsion de onda**, la cual se corrige con los diodos en serie.

### Eficiencia maxima:

$$100\% - 78.54\% = 21.46\% \text{ es calor disipado}$$

### Analisis de la eficiencia del clase B

La corriente de salida se expresa por:

$$I_{out(rms)} = \frac{I_{out(peak)}}{\sqrt{2}} = \frac{I_C/2}{\sqrt{2}} \quad,\quad V_{out(rms)} = \frac{V_{out(peak)}}{\sqrt{2}} = \frac{V_{CC}/2}{\sqrt{2}}$$

$$P_{out} = I_{out(rms)} \cdot V_{out(rms)} = \frac{I_C/2}{\sqrt{2}} \cdot \frac{V_{CC}/2}{\sqrt{2}} = \frac{I_C \, V_{CC}}{8} = 0.25 \, I_C \, V_{CC}$$

**$I_{CEQ}$** es la corriente media que se obtiene de integrar una onda completa (igual al de un rectificador de media onda, que conduce solo medio periodo):

$$I_{CC} = \frac{I_{CEQ}}{\pi} = \frac{I_C / 2}{\pi}$$

**Potencia DC:**

$$P_{DC} = I_{CC} \cdot V_{CC} = \frac{I_C \, V_{CC}}{2\pi}$$

**Eficiencia maxima:**

$$\%\eta(\text{max}) = \frac{P_{out}}{P_{DC}} \times 100 = \frac{0.25 \, I_C \, V_{CC}}{\frac{I_C \, V_{CC}}{2\pi}} \times 100 = 78.54\%$$

### Ejercicio: Eficiencia clase B con 2N3055

Calcular la eficiencia del amplificador que usa el transistor de potencia 2N3055.

Datos del datasheet: $V_{CE(sat)} < 1.1$ V, $h_{FE} = 20$ a $70$, $V_{CC} = +20$ V, $R_L = 8\Omega$, $R_1 = R_2 = 470\Omega$.

**Solucion:**

Potencia DC:

$$P_{DC} = \frac{I_C \, V_{CC}}{2\pi} = \frac{(V_{CC})^2}{2\pi R_L} = \frac{(20)^2}{2\pi \cdot 8} = 31.83 \text{ W}$$

Potencia AC (considerando $V_{CE(sat)}$):

$$V_{out(rms)} = \frac{V_{CC}}{2} - V_{CE(sat)} = \frac{20}{2} - 1.1 = 8.9 \text{ V}$$

$$P_{out} = \frac{(V_{out(rms)})^2}{R_L} = \frac{(8.9)^2}{8} = 9.9 \text{ W}$$

$$\%\eta(\text{max}) = \frac{9.9}{31.83} \times 100 = 31\%$$

### Correccion de distorsion: Amplificador clase B

La disposicion de diodos divisores de tension ($D_1$, $D_2$) corrigen la alinealidad del amplificador. Los diodos estan en conduccion constante por accion de $V_{CC}$.

> [!warning] Distorsion por cruce (Crossover distortion)
> Al conectar una resistencia en paralelo con los diodos $D_1$, $D_2$ aparece la distorsion por cruce. Al desconectar esta resistencia, la distorsion desaparece.

### Ejercicio: Eficiencia clase B con carga 1 kOhm

Determinar la eficiencia del amplificador para una carga de 1 kOhm (simulacion con Multisim).

La corriente media $I_{CEQ}$ se determina midiendo con un osciloscopio conectado a $R_1$:

$$I_{CEQ} = \frac{V_{R_1}}{R_1} = \frac{20\text{mV}}{5} = 4 \text{ mA}$$

$$I_{CC} = \frac{I_{CEQ}}{\pi} = \frac{4}{\pi} = 1.27 \text{ mA}$$

$$P_{DC} = I_{CC} \cdot V_{CC} = 1.27 \times 10^{-3} \times 36 = 45.72 \text{ mW}$$

La potencia alterna en carga ($R_9 = R_L$), midiendo el voltaje eficaz:

$$P_{out} = \frac{(V_{out(rms)})^2}{R_L} = \frac{(2.644)^2}{1k} = 6.99 \text{ mW}$$

$$\%\eta(\text{max}) = \frac{6.99}{45.72} \times 100 = 15\%$$

## Amplificador Darlington

Usando el par NPN Darlington como ejemplo, los colectores de dos transistores estan conectados entre si, y el emisor de TR1 impulsa la base de TR2. Esta configuracion logra la multiplicacion $\beta$ porque para una corriente base $I_B$, la corriente del colector es $\beta \cdot I_B$ donde la ganancia de corriente es mayor que la unidad:

$$I_C = I_{C1} + I_{C2}$$

$$I_C = \beta_1 \cdot I_B + \beta_2 \cdot I_{B2}$$

Como el emisor de TR1 esta conectado a la base de TR2:

$$I_{B2} = I_{E1} = I_{C1} + I_B = \beta_1 \cdot I_B + I_B = (\beta_1 + 1) \cdot I_B$$

Sustituyendo:

$$I_C = \beta_1 \cdot I_B + \beta_2 \cdot (\beta_1 + 1) \cdot I_B$$

$$I_C = \left(\beta_1 + \beta_2 \cdot \beta_1 + \beta_2\right) \cdot I_B$$

### Mejora de eficiencia: Clase B Darlington

$$I_{CEQ} = \frac{V_{R_1}}{R_1} = \frac{62\text{mV}}{5} = 12.4 \text{ mA}$$

$$I_{CC} = \frac{I_{CEQ}}{\pi} = \frac{12.4}{\pi} = 3.94 \text{ mA}$$

$$P_{DC} = I_{CC} \cdot V_{CC} = 3.94 \times 10^{-3} \times 36 = 142.08 \text{ mW}$$

$$P_{out} = \frac{(V_{out(rms)})^2}{R_L} = \frac{(7.196)^2}{1k} = 51.78 \text{ mW}$$

$$\%\eta(\text{max}) = \frac{51.78}{142.08} \times 100 = 36\%$$

> [!tip] Tarea
> Simular el mismo circuito y mejorar la eficiencia.

## Distorsion armonica THD

El amplificador clase B tiene la desventaja de generar ondas con contenido armonico debido a la distorsion por cruce. La distorsion por cruce se debe a la suma de la resultante de la onda fundamental y la armonica de tercer orden.

### Distorsion Armonica Total (THD)

La **THD** es una medida de cuanto se «distorsiona» o se cambia la forma de onda del voltaje o de la corriente de su forma de onda sinusoidal convencional. La THD es el porcentaje acumulado de distorsion para todos los tipos de armonicos en relacion a la potencia total.

$$THD = \frac{\sqrt{V_2^2 + V_3^2 + V_4^2 + \ldots + V_n^2}}{V_s}$$

Donde:
- $V_s$ = amplitud de la senal (RMS Volts)
- $V_2$ = amplitud de la 2da armonica (RMS Volts)
- $V_n$ = amplitud de la n-esima armonica (RMS Volts)

Considerando la senal de ruido:

$$THD + N = \frac{\sqrt{V_2^2 + V_3^2 + V_4^2 + \ldots + V_n^2 + V_{noise}^2}}{V_s}$$

### Ejemplo: THD de senal de 60 Hz con clase B

Para una senal de 60 Hz amplificada con un clase B, aparecen las componentes de frecuencia:

| n | $f_n$ (Hz) | $V_n$ |
| - | ---------- | ----- |
| 1 | 60         | 127.3 |
| 2 | 180        | 42.4  |
| 5 | 300        | 25.4  |
| 7 | 420        | 18.2  |
| 9 | 540        | 14.1  |

$$THD = \frac{\sqrt{42.4^2 + 25.4^2 + 18.2^2 + 14.1^2}}{127.3} = \frac{54.52}{127.3} \times 100 = 42.83\%$$

> [!warning] La distorsion armonica total (THD) es bastante elevada: 42.83%

## Amplificador Clase C

El amplificador clase C conduce un angulo **menor que 180°**. Este amplificador es polarizado por debajo del punto de corte con una tension negativa $V_{BB}$.

### Circuito tanque

Para producir onda completa de salida, al amplificador clase C se usa un **circuito tanque paralelo sintonizado**. La frecuencia de resonancia esta dada por:

$$f_r = \frac{1}{2\pi\sqrt{LC}}$$

### Potencia maxima de salida

El voltaje a traves del circuito tanque tiene un pico a pico de aproximadamente $2V_{CC}$. La maxima potencia de salida es:

$$P_{out} = \frac{V_{rms}^2}{R_C} = \frac{(0.707 \, V_{CC})^2}{R_C} = \frac{0.5 \, V_{CC}^2}{R_C}$$

### Potencia de disipacion

La potencia de disipacion del transistor es:

$$P_{D(on)} = I_{C(sat)} \cdot V_{CE(sat)}$$

La potencia promedio de disipacion considerando el tiempo de conduccion comparado con un ciclo completo (duty cycle) es:

$$P_{D(avg)} = \left(\frac{t_{on}}{T}\right) P_{D(on)} = \left(\frac{t_{on}}{T}\right) I_{C(sat)} \cdot V_{CE(sat)}$$

La potencia total y eficiencia:

$$P_T = P_{out} + P_{D(avg)}$$

$$\eta = \frac{P_{out}}{P_{out} + P_{D(avg)}}$$

### Eficiencia del clase C

De las ecuaciones anteriores:

$$\eta = \frac{P_{out}}{P_{out} + P_d} = \frac{1}{1 + \frac{P_d}{P_{out}}}$$

$$\frac{P_{D(avg)}}{P_{out}} = \frac{\frac{t_{on}}{T} \cdot I_{C(sat)} \cdot V_{CE(sat)}}{\frac{0.5 \, V_{CC}^2}{R_C}} \Rightarrow \eta \leq 100\%$$

> [!important] Eficiencia del clase C
> Si la tension de saturacion del transistor es muy pequena y el tiempo de conduccion de la corriente de colector es lo mas corto posible, la eficiencia puede aproximarse al 100%. Usualmente alcanza el 99%. Son los amplificadores mas eficientes, pero con la linealidad mas pobre.

### Ejemplo: Amplificador sintonizado clase C

Amplificador de frecuencia de oscilacion:

$$f_o = \frac{1}{2\pi\sqrt{LC}} = \frac{1}{2\pi\sqrt{(0.25 \times 10^{-6})(0.25 \times 10^{-6})}} = 636.618 \text{ kHz}$$

Datos: $V_{CC} = 15$ VDC, $V_1 = -1.5$ VDC, $V_p = 3$ Vca senal de generador, Ganancia $= \frac{30}{5} = 6$.

### Circuito sintonizado ajustado por nucleo de ferrita

Los circuitos sintonizados se pueden ajustar fisicamente mediante un nucleo de ferrita (ferrite tuning slug) que se inserta en la bobina, modificando la inductancia y por tanto la frecuencia de resonancia.

## Circuitos resonantes LC serie

Un circuito resonante (serie o paralelo) debe tener un elemento inductivo y uno capacitivo. Siempre estara presente el elemento resistivo debido a la resistencia interna de la fuente y la resistencia interna del inductor ($R$).

Los dispositivos reactivos almacenan energia:

$$E_L = \frac{1}{2} L \, I^2 \qquad \text{(inductancia)}$$

$$E_C = \frac{1}{2} C \, V^2 \qquad \text{(condensador)}$$

Los dispositivos pasivos como la resistencia consumen potencia y la liberan en forma de calor.

### Impedancia del circuito serie

$$Z_T = R + j(X_L + X_C)$$

En resonancia $X_L = -X_C$, por lo tanto:

$$Z_T = R$$

La frecuencia de resonancia serie:

$$f_s = \frac{1}{2\pi\sqrt{LC}}$$

La corriente en funcion de la frecuencia:

$$I = \frac{V}{Z_T} = \frac{V}{\sqrt{R^2 + (X_L - X_C)^2}}$$

Cuando se produce la resonancia, la corriente es maxima:

$$I_{max} = \frac{V}{R}$$

### Factor de calidad Q

El factor de calidad $Q$ de un circuito resonante serie se define como la proporcion de la potencia reactiva del inductor o el capacitor entre la potencia promedio del resistor en la resonancia:

$$Q_S = \frac{\text{potencia reactiva}}{\text{potencia promedio}}$$

$$Q_S = \frac{I^2 X_L}{I^2 R} = \frac{\omega_S L}{R} = \frac{1}{\sqrt{LC}} \cdot \frac{L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}$$

Donde: $\omega_s = \frac{1}{\sqrt{LC}}$

En los circuitos resonantes en serie utilizados en sistemas de comunicacion, $Q_S$ es mayor que 1. Aplicando la regla divisora de voltaje:

$$Q_S = \frac{X_L}{R} \quad \therefore \quad X_L = R \cdot Q_S$$

En resonancia: $V_S = IR$

$$V_{LS} = I \cdot X_L = I \cdot R \cdot Q_S = V_S \cdot Q_S$$

$$V_{CS} = I \cdot X_C = I \cdot R \cdot Q_S = V_S \cdot Q_S$$

> [!warning] El voltaje que pasa a traves del capacitor o inductor podria ser considerablemente mayor que el voltaje de entrada, debido al almacenamiento de energia. En varios casos $Q_S$ es tan grande que la evaluacion de un circuito serie LC debe ser cuidadosa.

### Selectividad

Si trazamos la magnitud de la corriente $I = V/Z_T$ en funcion de la frecuencia, obtenemos la curva de selectividad:

En resonancia ($f = f_s$):

$$I_{(f=f_s)} = I_{max} \quad \therefore \quad \text{dB} = 10\log\frac{I_{max}}{I_{(f=f_s)}} = 10\log 1 = 0$$

En las frecuencias de corte ($f = f_1$ o $f = f_2$):

$$I_{(f=f_1, f=f_2)} = \frac{I_{max}}{2} \quad \therefore \quad \text{dB} = 10\log\frac{I_{max}/2}{I_{max}} = 10\log\frac{1}{2} = -3$$

### Ancho de banda

**Curva de selectividad:** significa que debemos ser selectivos al seleccionar una frecuencia, de modo que quede en el ancho de banda. Cuanto menor sea el ancho de banda, mas alta sera la selectividad. Las frecuencias pertenecientes al factor 0.707 de la maxima corriente se llaman **frecuencias de corte** ($f_1$ y $f_2$). El intervalo de frecuencias entre las dos se conoce como **ancho de banda** (BW).

a) Relacion con el factor de calidad:

$$BW = \frac{f_r}{Q_S} \qquad Q_S = \frac{X_L}{R}$$

b) Ancho de banda fraccionario:

$$\frac{f_2 - f_1}{f_r} = \frac{1}{Q_S}$$

c) Media geometrica de la banda de frecuencias:

$$f_s = \sqrt{f_1 \times f_2}$$

> [!info] Efecto de la resistencia
> A menor R, mayor $Q_S$ y menor ancho de banda (mayor selectividad). A mayor R, menor $Q_S$ y mayor ancho de banda (menor selectividad).

### Ejercicio en clase (examen final)

Graficar la curva de resonancia serie para: $L = 10$ mH, resistencia del inductor $= 1\Omega$, $C = 100\mu$F, tension aplicada $= 24$ VCA. Determinar la corriente en resonancia y al 50%.

$$f_s = \frac{1}{2\pi\sqrt{LC}} = 159.23 \text{ Hz}$$

$$I_{max} = \frac{V}{R} = \frac{24}{1} = 24 \text{ A}$$

| f (Hz)  | i (A)  | dB   |
| ------- | ------ | ---- |
| 159.23  | 24.00  | 0    |
| 173.53  | 12.02  | 3    |
| 170.00  | 14.49  | 2.2  |
| 180.00  | 9.01   | 4.25 |
| 190.00  | 6.48   | 5.68 |

Frecuencias de corte y ancho de banda:
- $f_{\text{corte superior}} = 173.53$ Hz
- $f_{\text{corte inferior}} = 144.93$ Hz
- **Ancho de banda = 28.6 Hz**

### Ejercicio 1

El ancho de banda de un circuito resonante es de 400 Hz, con frecuencia de resonancia de 4000 Hz.
a) Factor de calidad Q
b) Si $R = 10\Omega$, valor de $X_L$ en resonancia
c) Determinar la inductancia y la capacitancia del circuito

**Solucion:**

a) $Q_S = \frac{f_r}{BW} = \frac{4000}{400} = 10$

b) $X_L = R \cdot Q_S = 10 \times 10 = 100\Omega$

c) $X_L = \omega_S L = 2\pi f L \quad \therefore \quad L = \frac{X_L}{2\pi f} = \frac{100}{2\pi \cdot 4000} = 3.98$ mH

$C = \frac{1}{2\pi f X_C} = \frac{1}{2\pi \cdot 2000 \cdot 100} = 0.398 \; \mu$F

### Ejercicio 2

Un circuito RLC en serie tiene una frecuencia de resonancia serie en 1200 Hz.
a) Si $R = 5\Omega$ y en resonancia $X_L = 300\Omega$, determinar el ancho de banda
b) Determinar las frecuencias de corte

**Solucion:**

a) $Q_S = \frac{X_L}{R} = \frac{300}{5} = 60$

$BW = \frac{f_r}{Q_S} = \frac{1200}{60} = 200$ Hz

b) Como $Q_S \geq 10$, el ancho de banda es simetrico:

$$f_1 = f_r + \frac{BW}{2} = 1200 + \frac{200}{2} = 1300 \text{ Hz}$$

$$f_2 = f_r - \frac{BW}{2} = 1200 - \frac{200}{2} = 1100 \text{ Hz}$$

### Ejercicio examen ELEC A_B

El ancho de banda de un circuito resonante es de 40 Hz, con frecuencia de resonancia de 10 kHz.
a) Factor de calidad Q
b) Si $R = 4\Omega$, valor de $X_L$ en resonancia
c) Determinar la inductancia y la capacitancia del circuito
d) Realizar la simulacion

**Solucion:**

a) $Q_S = \frac{f_r}{BW} = \frac{10000}{40} = 250$

b) $X_L = R \cdot Q_S = 4 \times 250 = 1000\Omega$

c) $L = \frac{X_L}{2\pi f} = \frac{1000}{2\pi \cdot 10000} = 15.91$ mH

$C = \frac{1}{2\pi f X_C} = \frac{1}{2\pi \cdot 10000 \cdot 1000} = 15.91$ nF

## Tareas

> [!todo] Tarea 1
> Calcular la distorsion por cruce de un amplificador clase B. Determinar la serie de Fourier de la funcion: $f(t) = \cos(t)$

> [!todo] Tarea 2
> - Experimentar los amplificadores clase B (20 kHz)
> - Para el amplificador clase C, amplificar una senal de 450 kHz
> - Mediante software (Proteus, Matlab u otro), analizar el circuito serie RLC y dibujar la curva de selectividad. Determinar el ancho de banda. Graficar: dB = f(frec). Realizar otro grafico para diferentes R y dar conclusiones ($Q_S = X_L / R$)
