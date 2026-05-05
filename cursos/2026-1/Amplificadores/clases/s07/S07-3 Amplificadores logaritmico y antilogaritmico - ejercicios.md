---
title: "Amplificadores logaritmico y antilogaritmico - ejercicios resueltos"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 7
orden: 3
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tipo/ejercicio
  - tema/amplificador-logaritmico
  - tema/amplificador-antilogaritmico
  - tema/multiplicador-analogico
  - tema/companding
  - tema/diseno-de-circuitos
date: 2026-05-04
---

> [!info] Continuacion
> Esta nota desarrolla problemas de **diseno y analisis** de log-amps y antilog-amps. La teoria correspondiente esta en [[S06-1 Amplificadores lineales y no lineales#5. Amplificador logaritmico|S06-1 sec. 5]] y [[S06-1 Amplificadores lineales y no lineales#6. Amplificador antilogaritmico (exponencial)|sec. 6]].

## Resumen rapido de formulas

### Log-amp con BJT (configuracion basica)

$$V_o = -V_T \ln\left(\frac{V_{in}}{R \cdot I_s}\right) = -V_T\,\ln(10)\cdot\log_{10}\left(\frac{V_{in}}{R \cdot I_s}\right)$$

Pendiente: $-V_T \ln(10) \approx -60$ mV/decada a 25°C.

### Log-amp con compensacion (par BJT apareado + $I_{REF}$)

$$\boxed{V_o = V_T \ln\left(\frac{I_{REF} \cdot R}{V_{in}}\right)}$$

→ $I_s$ cancelado. Solo queda dependencia con $V_T = kT/q$.

### Antilog-amp con BJT y compensacion

$$\boxed{V_o = -R \cdot I_{REF} \cdot e^{V_{in}/V_T}}$$

→ Por cada $V_T \ln 10 \approx 60$ mV de aumento en $V_{in}$, $|V_o|$ se multiplica por 10.

### Constantes utiles

| Constante | Valor a 25°C |
| --------- | ------------ |
| $V_T = kT/q$ | $25.9 \approx 26$ mV |
| $V_T \ln 10$ | $59.6$ mV |
| $I_s$ (BJT pequena senal, ej. 2N3904) | ~$2 \times 10^{-15}$ A |
| $I_s$ (diodo Si 1N4148) | ~$2.5 \times 10^{-9}$ A |

---

## Ejercicio 1: Calculo de $V_o$ del log-amp basico

**Enunciado.** Para el circuito log-amp con diodo de la figura, calcular $V_o$ cuando $V_{in}$ vale: $1$ mV, $10$ mV, $100$ mV, $1$ V, $10$ V. Datos: $R = 10$ k$\Omega$, $I_s = 10^{-12}$ A, $V_T = 26$ mV. Op-amp con $V_{cc} = \pm 15$ V.

```
          R = 10k          D
  Vin ---[===]---+--------|>|--------+
                 |                   |
            (-) \|                   |
                 +-------------------+ Vo
            (+) /
                 |
                GND
```

### Formula

$$V_o = -V_T \ln\left(\frac{V_{in}}{R \cdot I_s}\right)$$

### Tabla de calculos

$R \cdot I_s = 10\,\text{k}\Omega \times 10^{-12}\,\text{A} = 10^{-8}$ V (referencia interna).

| $V_{in}$ | $V_{in}/(RI_s)$ | $\ln(\cdot)$ | $V_o = -V_T \ln(\cdot)$ |
| -------- | --------------- | ------------ | ----------------------- |
| 1 mV     | $10^5$  | 11.51 | $\bf -299$ mV |
| 10 mV    | $10^6$  | 13.82 | $\bf -359$ mV |
| 100 mV   | $10^7$  | 16.12 | $\bf -419$ mV |
| 1 V      | $10^8$  | 18.42 | $\bf -479$ mV |
| 10 V     | $10^9$  | 20.72 | $\bf -539$ mV |

### Verificacion de la pendiente

$$\Delta V_o / \text{decada} = -60\,\text{mV} \approx -V_T \ln 10$$

| Decada | $\Delta V_o$ |
| ------ | ------------ |
| 1 mV → 10 mV | $-60$ mV ✓ |
| 10 mV → 100 mV | $-60$ mV ✓ |
| 100 mV → 1 V | $-60$ mV ✓ |
| 1 V → 10 V | $-60$ mV ✓ |

> [!success] Resultado
> Para 4 decadas de variacion en $V_{in}$ (1 mV → 10 V, factor $10^4$), $V_o$ varia solo $240$ mV. Este es el principio del log-amp: **comprime un rango dinamico amplio en una salida pequena**.

> [!example] Aplicacion: medicion de luz solar
> Un fotodiodo expuesto a luz puede generar corrientes desde 1 nA (luna) hasta 100 $\mu$A (sol directo) — un rango de **5 decadas**. Un log-amp comprime esta corriente a una salida lineal en dB/decadas, facilmente leida por un ADC de 12 bits.

---

## Ejercicio 2: Diseno de log-amp para sensor con rango dinamico amplio

**Enunciado.** Disenar un log-amp con BJT para procesar la salida de un fotodiodo que entrega corrientes entre $I_{min} = 10$ nA y $I_{max} = 1$ mA (5 decadas). La salida debe estar en el rango $0$ a $-300$ mV (compatible con un ADC unipolar). Usar par BJT apareado (LM394 o similar) con $I_{REF} = 1$ mA.

### Topologia (corriente directa, sin $R$ de entrada)

```
   I_in (fotodiodo)              I_REF
         |                         |
         E1                        E2
        [Q1]                     [Q2]    <- LM394 (par apareado)
         B1=GND                   B2=GND
         |                         |
        VBE1                     VBE2
         +---->[op-amp resta]<----+
                       |
                      Vo
```

### Formula con par apareado

Con corriente directa al emisor (sin $R$), la formula simplifica a:

$$V_o = V_T \ln\left(\frac{I_{REF}}{I_{in}}\right)$$

### Calculos

| $I_{in}$ | $I_{REF}/I_{in}$ | $\ln(\cdot)$ | $V_o$ |
| -------- | ---------------- | ------------ | ----- |
| 10 nA    | $10^5$ | 11.51 | $\bf +299$ mV |
| 100 nA   | $10^4$ | 9.21  | $\bf +239$ mV |
| 1 $\mu$A | $10^3$ | 6.91  | $\bf +180$ mV |
| 10 $\mu$A | $10^2$ | 4.61 | $\bf +120$ mV |
| 100 $\mu$A | $10^1$ | 2.30 | $\bf +60$ mV |
| 1 mA     | $1$    | 0     | $\bf 0$ V |

> [!success] Resultado
> Para $I_{in}$ desde 10 nA hasta 1 mA (5 decadas), $V_o$ varia de 0 a +299 mV → exactamente $60$ mV/decada. Cumple con la especificacion del ADC.

### Conversion a logaritmo decimal (escala de dB)

$$V_o = V_T \ln(10) \cdot \log_{10}(I_{REF}/I_{in}) = 60\,\text{mV/dec} \times \log_{10}(I_{REF}/I_{in})$$

Para hacer la salida en **dB optico** (10 log para potencia, 20 log para amplitud), basta amplificar con un op-amp en configuracion no inversora con ganancia adecuada.

---

## Ejercicio 3: Compensacion de temperatura

**Enunciado.** El log-amp del Ejercicio 1 (sin compensacion, con un solo diodo) opera a $T = 25°$C. Estimar el error de la salida si la temperatura aumenta a $T = 70°$C. Comparar con la version compensada.

### Variacion de los parametros con T

A $T = 70°$C:

$$V_T(70°\text{C}) = \frac{k \times 343.15}{q} = \frac{1.381\times 10^{-23} \times 343.15}{1.602\times 10^{-19}} = 29.6\,\text{mV}$$

→ aumento de $V_T$: $(29.6 - 26)/26 = +13.8\%$.

$I_s$ se duplica aprox. cada $10°$C → entre 25°C y 70°C ($\Delta T = 45°$C), aumenta:

$$I_s(70°\text{C}) = I_s(25°\text{C}) \times 2^{4.5} \approx 22.6 \times I_s(25°\text{C})$$

### Sin compensacion ($V_o = -V_T \ln(V_{in}/(R I_s))$)

Para $V_{in} = 1$ V, $R = 10$ k$\Omega$, $I_s$ a 25°C $= 10^{-12}$ A.

A 25°C: $V_o = -26 \times \ln(10^8) = -479$ mV (calculado en Ej. 1).

A 70°C:
- $I_s = 22.6 \times 10^{-12}$ A
- $RI_s = 2.26 \times 10^{-7}$
- $V_{in}/(RI_s) = 4.42 \times 10^6$
- $\ln(\cdot) = 15.30$
- $V_o = -29.6 \times 15.30 = -453$ mV

**Error:** $\Delta V_o = -453 - (-479) = +26$ mV → desviacion de **5.4%** sobre la lectura.

> [!warning] Significado en aplicaciones reales
> Para un sensor que entrega 0-300 mV de salida en un rango de 5 decadas (60 mV/decada), un error de 26 mV equivale a **0.43 decadas o un factor 2.7 en la entrada**. Inaceptable para instrumentacion.

### Con compensacion (par apareado, mismo chip)

Si los dos transistores estan en el **mismo encapsulado** (ej. LM394) o en chip monolitico, $I_s$ se cancela perfectamente:

$$V_o = V_T \ln(I_{REF}/I_{in})$$

→ Solo queda la dependencia con $V_T$ ($+13.8\%$ en escala). Esta dependencia se compensa con un **resistor de coeficiente termico positivo** (PTC) en la red de salida, o con un divisor con thermistor que escale la ganancia $\propto 1/T$.

> [!success] Mejora con compensacion completa
> Con par apareado + ganancia compensada en T:
> - Sin compensacion: error 5.4% en 45°C
> - Solo par apareado: error 13.8% (solo $V_T$)
> - Par apareado + PTC: < 0.5% en todo el rango industrial (-40 a +85°C)

### ICs comerciales con compensacion completa

| IC | Compensacion | Decadas utiles |
| -- | ------------ | -------------- |
| LOG101 | Par apareado interno + escala compensada | 6 |
| LOG114 | Par + ganancia y bias compensados | 7 |
| AD8304 | Compensacion total + amplificador buffer | 8 |

---

## Ejercicio 4: Antilog-amp y caracteristica exponencial

**Enunciado.** Para el antilog-amp con BJT compensado, calcular $V_o$ para $V_{in} = 0, 60$ mV, $120$ mV, $240$ mV, $480$ mV, $600$ mV. Datos: $R = 10$ k$\Omega$, $I_{REF} = 100\,\mu$A, $V_T = 26$ mV. Verificar el rango lineal del op-amp ($V_{sat} = -13.5$ V).

### Formula

$$V_o = -R \cdot I_{REF} \cdot e^{V_{in}/V_T}$$

$R \cdot I_{REF} = 10\,\text{k}\Omega \times 100\,\mu\text{A} = 1$ V.

### Tabla de calculos

| $V_{in}$ | $V_{in}/V_T$ | $e^{V_{in}/V_T}$ | $V_o = -1 \cdot e^{V_{in}/V_T}$ V |
| -------- | ------------ | ---------------- | --------------------------------- |
| 0        | 0      | 1     | $\bf -1.000$ V |
| 60 mV    | 2.31   | 10.04 | $\bf -10.04$ V |
| 120 mV   | 4.62   | 101.0 | $\bf -101$ V (saturacion!) |
| 240 mV   | 9.23   | $1.02 \times 10^4$ | satura |
| 480 mV   | 18.46  | $1.04 \times 10^8$ | satura |
| 600 mV   | 23.08  | $1.06 \times 10^{10}$ | satura |

> [!warning] Limite practico
> Con esta combinacion ($R \cdot I_{REF} = 1$ V), el op-amp satura para $V_{in} > 70$ mV aprox. ($V_o = -13.5$ V):
>
> $$V_{in,max} = V_T \ln(13.5) = 26 \times 2.603 = 67.7\,\text{mV}$$
>
> El antilog **comprime el rango de entrada** drasticamente — la salida cubre 1 decada por cada 60 mV de entrada.

### Diseno corregido (rango util mas amplio)

Para que el antilog opere de $V_{in} = 0$ hasta $600$ mV con $V_o$ en $\pm 12$ V:

Si queremos $V_o(600\,\text{mV}) = -12$ V:

$$12 = R\,I_{REF}\,e^{0.6/0.026} = R\,I_{REF}\times 1.06\times 10^{10}$$

$$R\,I_{REF} = 1.13 \times 10^{-9}\,\text{V}$$

Eligiendo $R = 1$ k$\Omega$:

$$I_{REF} = 1.13 \times 10^{-12}\,\text{A} = 1.13\,\text{pA}$$

Es muy pequena pero generable con un divisor de alta impedancia (10 G$\Omega$) o usando otro espejo de corriente.

| $V_{in}$ | $V_o$ |
| -------- | ----- |
| 0        | $-1.13$ pV |
| 120 mV   | $-114$ nV |
| 240 mV   | $-11.5\,\mu$V |
| 360 mV   | $-1.16$ mV |
| 480 mV   | $-117$ mV |
| 600 mV   | $-11.8$ V (cerca de saturacion) |

> [!note] Usar log/antilog para multiplicar
> En la practica los antilogs **no se usan solos** — son la etapa final de un multiplicador analogico (ver Ejercicio 5). En esa configuracion los rangos se ajustan automaticamente.

---

## Ejercicio 5: Multiplicador analogico log + log + antilog

**Enunciado.** Disenar un multiplicador analogico de dos voltajes: $V_o = K \cdot V_1 V_2$ usando dos log-amps y un antilog-amp. Calcular $K$ y verificar para $V_1 = 1$ V, $V_2 = 2$ V. Asumir todos los log/antilog amps con BJT apareado, mismos $R$ y $I_{REF}$.

### Idea

```
   V1 ---[log-amp]----- V_a = K1 ln(V1)
                              \
                               +-- V_a + V_b ---[antilog]---- V_o = K2 e^(V_a + V_b) = K2 V1*V2*K1
   V2 ---[log-amp]----- V_b = K1 ln(V2)
                              /
                       (suma con un sumador inversor, omitido aqui)
```

Cada log-amp produce: $V_x = -V_T \ln(V_x/(R I_s))$ (con un solo BJT, sin compensacion). Sumando:

$$V_a + V_b = -V_T[\ln(V_1/(RI_s)) + \ln(V_2/(RI_s))] = -V_T \ln\left(\frac{V_1 V_2}{(RI_s)^2}\right)$$

Pasando por el antilog ($V_o = -RI_s e^{-(V_a+V_b)/V_T}$, signo invertido por la sustraccion):

$$V_o = -R I_s \cdot \frac{V_1 V_2}{(R I_s)^2} = -\frac{V_1 V_2}{R I_s}$$

### Calibracion

Eligiendo $R = 100$ k$\Omega$ y $I_s = 10^{-13}$ A → $R I_s = 10^{-8}$. Entonces:

$$V_o = -\frac{V_1 V_2}{10^{-8}} \to \text{satura inmediatamente}$$

Necesitamos un **escalado** en la suma. La forma estandar es escalar por una constante de referencia $V_{ref} = 10$ V para que $V_o = V_1 V_2 / V_{ref}$:

$$V_o = \frac{V_1 \cdot V_2}{V_{ref}}, \quad V_{ref} = 10\,\text{V}$$

### Verificacion

Para $V_1 = 1$ V, $V_2 = 2$ V:

$$V_o = \frac{1 \times 2}{10} = 0.2\,\text{V}$$

Con $V_1 = 5$ V, $V_2 = 4$ V:

$$V_o = \frac{5 \times 4}{10} = 2\,\text{V}$$

Con $V_1 = 10$ V, $V_2 = 10$ V:

$$V_o = \frac{100}{10} = 10\,\text{V} \quad \text{(maximo del rango)}$$

> [!success] Multiplicador analogico
> Con $V_{ref} = 10$ V, el multiplicador acepta $V_1, V_2 \in [0, 10]$ V y produce $V_o \in [0, 10]$ V. La precision tipica con BJTs apareados es de ~1% para entradas > 100 mV.

### Aplicaciones tipicas del multiplicador analogico

1. **Modulacion AM:** $V_o(t) = V_{portadora}(t) \cdot V_{moduladora}(t)$
2. **Mezcladores RF:** producto de dos senoidales → suma y diferencia de frecuencias
3. **Calculo de potencia instantanea:** $P(t) = V(t) \cdot I(t)$ con un sensor de corriente y un multiplicador
4. **Conversor cuadratico (RMS):** elevar al cuadrado con $V_1 = V_2 = V_{in}$
5. **Control automatico de ganancia (AGC):** $V_{salida} = V_{senal} \times V_{control}$
6. **Calculo vectorial:** $|V|^2 = V_x^2 + V_y^2$ (multiples multiplicadores)

### IC comercial: AD633

El **AD633** (Analog Devices) es un multiplicador analogico de 4 cuadrantes en un solo chip:

$$V_o = \frac{(X_1 - X_2)(Y_1 - Y_2)}{10\,\text{V}} + Z$$

Con precision $\pm 2\%$, BW de 1 MHz, ideal para senales de audio, instrumentacion y RF de baja frecuencia.

---

## Ejercicio 6: Aplicacion - Companding (compresion + expansion)

**Enunciado.** En un sistema de telefonia de larga distancia, las senales de audio (variables en 60 dB) se transmiten por un canal con SNR limitado. Para mejorar la inteligibilidad de las senales debiles, se usa **companding $\mu$-law**: comprimir antes de transmitir y expandir despues.

### Compresion $\mu$-law

$$F(x) = \text{sgn}(x) \cdot \frac{\ln(1 + \mu|x|)}{\ln(1 + \mu)}, \quad |x| \leq 1$$

con $\mu = 255$ (estandar US/Japon, T1) o $A$-law $A = 87.6$ (estandar europeo, E1).

Para $\mu = 255$:

| $|x|$ (entrada) | $F(x)$ (salida comprimida) | Ganancia $F(x)/x$ |
| ---- | -------- | ----------------- |
| 0.001 | 0.0468  | 47   (senales pequenas amplificadas 33 dB) |
| 0.01 | 0.179  | 17.9 |
| 0.1  | 0.481  | 4.81 |
| 0.5  | 0.876  | 1.75 |
| 1.0  | 1.000  | 1.00 (sin amplificar) |

> [!important] Que hace el compander
> Las senales **debiles** se amplifican mucho antes de transmitir; las **fuertes** se mantienen. Despues, el receptor expande con la curva inversa, restaurando la senal original. El ruido del canal **se amplifica solo cuando las senales son grandes** — donde es enmascarado por la propia senal. Resultado: SNR efectivo mejora ~10-20 dB.

### Implementacion analogica

Una version simplificada del compresor usa un log-amp con ganancia ajustada:

$$V_{out} = K \log_{10}(1 + V_{in}/V_{ref})$$

Con $V_{ref}$ seleccionado para igualar $\mu = 255$. La curva real $F(x)$ se aproxima por tramos lineales en implementaciones digitales (PCM) — pero en la era analogica (telefonia analogica) se realizaba con log-amps reales.

### IC clasico: NE570/571 (Compander)

El **NE570** de Signetics/Phillips integra dos compander cells (cada una con un log-amp + buffer + multiplicador). Ampliamente usado en:

- **Sistemas Dolby B/C/SR** para cassettes
- **Telefonia inalambrica** (cordless 50 MHz)
- **Walkie-talkies** comerciales
- **CB radio** mejorado

> [!example] Resultados medidos
> En una cinta cassette grabada a -20 dB de nivel maximo:
> - Sin Dolby: SNR = 56 dB (cinta de cromo BASF a 4.76 cm/s)
> - Con Dolby B: SNR = 65 dB (mejora 9 dB en altas frecuencias)
> - Con Dolby C: SNR = 70 dB (mejora 14 dB)

---

## Ejercicio 7: Limite del log-amp por offset y bias

**Enunciado.** Un log-amp con OP07 (offset $V_{os} = 30\,\mu$V, $I_{bias} = 1.5$ nA) y $R = 10$ k$\Omega$, $I_s = 10^{-13}$ A. Calcular el **menor $V_{in}$ medible** con error inferior al 1% en la salida.

### Analisis

El error principal en log-amps a $V_{in}$ pequeno proviene de:

1. **Voltaje offset $V_{os}$:** se suma directamente a $V_{in}$ → "piso" de entrada $\approx V_{os}$
2. **Bias $I_{bias}$:** se suma a la corriente del diodo → "piso" de corriente $\approx I_{bias} \cdot R$ en terminos de Vin equivalente

### Calculo del piso por bias

$$V_{in,piso} = I_{bias} \cdot R = 1.5\,\text{nA} \times 10\,\text{k}\Omega = 15\,\mu\text{V}$$

Por offset: $V_{in,piso}^{(offset)} = V_{os} = 30\,\mu$V (el offset se ve directamente como un sumando a $V_{in}$).

**Error total:** se suma cuadraticamente para incertidumbres independientes, pero como ambos tienen la misma signo nominal puede ser tan alto como su suma:

$$V_{in,piso,total} \approx 45\,\mu\text{V}$$

### Para error < 1%

Para que el error relativo en $V_{in}$ sea menor al 1%:

$$V_{in} > 100 \times V_{in,piso} = 4.5\,\text{mV}$$

Pero el **error en la salida** de un log-amp es diferente porque:

$$\frac{\partial V_o}{\partial V_{in}} = -\frac{V_T}{V_{in}}$$

Entonces:

$$\Delta V_o = -V_T \cdot \frac{\Delta V_{in}}{V_{in}}$$

Para $\Delta V_o < 1\,\text{mV}$ (1% de la salida tipica):

$$\frac{\Delta V_{in}}{V_{in}} < \frac{1\,\text{mV}}{26\,\text{mV}} = 3.85\%$$

→ El error relativo en $V_{in}$ permitido es 3.85%, que se traduce a:

$$V_{in,min} = \frac{V_{in,piso}}{0.0385} = \frac{45\,\mu\text{V}}{0.0385} = 1.17\,\text{mV}$$

> [!success] Resultado
> Con OP07: $V_{in,min} \approx 1$ mV. Para medir corrientes mas pequenas usar:
> - Op-amp con offset menor (OPA192: $V_{os} = 5\,\mu$V, $I_{bias} = 50$ pA)
> - Tecnica de **chopper-stabilized** (ICL7650): $V_{os} = 0.5\,\mu$V

---

## Resumen de aplicaciones log/antilog en sistemas reales

| Aplicacion | Log o antilog | Razon |
| ---------- | ------------- | ----- |
| Vumetros (medidor de audio en dB) | Log | Comprimir dinamica |
| Densitometros (cuantos dB de absorbancia tiene una pelicula) | Log | $\text{Densidad} = \log(I_o/I)$ |
| pH-metros | Log | $\text{pH} = -\log[H^+]$ |
| Espectrofotometros | Log + sensor | Concentracion = $\log_{10}(I_0/I)$ |
| Fotometros (fotografia) | Log | EV = $\log_2$ de luminancia |
| Modulacion AM | Multiplicador (log-suma-antilog) | Producto $V_p \cdot V_m$ |
| Mezcladores RF | Multiplicador | Heterodinaje |
| AGC en radios | Multiplicador con $V_{control}$ | Ganancia ajustable |
| Calculo RMS | Multiplicador (cuadrado + raiz) | $\sqrt{\text{avg}(V^2)}$ |
| Companding (Dolby, $\mu$-law) | Log + antilog (cancelados) | Mejorar SNR |

## Bibliografia

- Sedra, A. & Smith, K. *Microelectronic Circuits* (7a ed.). Oxford University Press. Cap. 18, secs. 18.7-18.8.
- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos* (10a ed.). Pearson. Cap. 14, sec. 14.7.
- Coughlin, R. & Driscoll, F. *Operational Amplifiers and Linear Integrated Circuits* (6a ed.). Prentice Hall. Cap. 7 (log-amps y multiplicadores).
- Texas Instruments. *LOG114 Datasheet*. https://www.ti.com/product/LOG114
- Analog Devices. *AD633 Datasheet - Low Cost Analog Multiplier*. https://www.analog.com/en/products/ad633.html
- ITU-T Recommendation G.711, *Pulse code modulation (PCM) of voice frequencies*. International Telecommunication Union.
