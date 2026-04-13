---
title: Evaluación - PA1
curso: "[[Motores MOC]]"
unidad: 1
semana: 3
orden: 99
tipo: clase
tags:
  - curso/motores
  - tipo/clase
  - tema/evaluacion
date: 2026-04-12
---

## Pregunta 1

> Son máquinas estáticas, n (velocidad) = 0, constituidas por dos devanados, inductor e inducido. El devanado inductor se conecta a una fuente de c.a. de frecuencia f1 y se denomina primario.

**Alternativas:**
- **a. Transformadores** ✅
- b. Motores síncronos
- c. Motores asíncronos
- d. Núcleo magnético
- e. Campo magnético

### Respuesta: a. Transformadores

### Razonamiento

La pregunta describe máquinas con las siguientes características:
1. **Estáticas** ($n = 0$, sin movimiento)
2. **Dos devanados**: inductor (primario) e inducido (secundario)
3. **Alimentación en c.a.** a frecuencia $f_1$

Según lo visto en [[S03-0 Ideas clave - Semana 03]], la idea clave 4 establece:

> Si no existen órganos móviles ($n = 0$), lo que indica que $f_1 = f_2$, entonces coinciden las frecuencias del inductor e inducido, resultando las llamadas **máquinas estáticas**.

En [[S03-3 Tema 03 - Ecuacion de tension inducida#Caso 1 Inducido fijo. Flujo variable.]], se analiza el caso donde $\Omega = 0$ (inducido fijo), y la f.e.m. inducida resulta:

$$E_2 = 4{,}44 \cdot N_2 \cdot f_1 \cdot \phi_m$$

La nota explícitamente indica:

> Esta expresión se empleará en el estudio de los **transformadores**.

### Descarte de otras alternativas

- **b. Motores síncronos**: Son máquinas **rotativas** ($n \neq 0$) donde $f_2 = \frac{n \cdot p}{60}$, como se demuestra en [[S03-3 Tema 03 - Ecuacion de tension inducida#Caso 2 Inducido móvil. Flujo constante.]]
- **c. Motores asíncronos**: También son máquinas **rotativas** ($n \neq 0$), corresponden al caso general $f_2 = f_1 \pm \frac{n \cdot p}{60}$, como se indica en [[S03-0 Ideas clave - Semana 03]] idea clave 5.
- **d. Núcleo magnético**: Es un componente físico de las máquinas, no un tipo de máquina eléctrica. Se estudia en [[S03-2 Tema 02 - Nucleo ferromagnetico excitado con CA sinusoidal]].
- **e. Campo magnético**: Es un fenómeno físico, no un tipo de máquina. Se introduce en [[S01-1 Tema 01 - Como se produce un campo magnético]].

---

## Pregunta 2

> ¿Cuál es la ley que establece que en una bobina de alambre conductor se generará un voltaje proporcional a la tasa de cambio del flujo que la atraviesa con respecto al tiempo?

**Alternativas:**
- **a. Ley de Faraday** ✅
- b. Ley de Hopkins
- c. Ley de Ohm
- d. Ley de Ampere
- e. Ley de magnetomotriz

### Respuesta: a. Ley de Faraday

### Razonamiento

La pregunta describe exactamente la **ley de inducción de Faraday**: una f.e.m. (voltaje) inducida proporcional a la tasa de cambio del flujo magnético en el tiempo.

Según [[S01-3 Tema 02 - Las leyes del electromagnetismo#Ley de Faraday]]:

> "La ley de la inducción de Faraday-Lenz dice que la fuerza electromotriz inducida en un circuito es igual al valor negativo de la rapidez con la cual está cambiando el flujo que atraviesa el circuito."

La ecuación que la define es:

$$E = -N \cdot \frac{d\phi}{dt}$$

Donde la f.e.m. inducida es **proporcional** al número de espiras $N$ y a la **rapidez de variación del flujo** $\frac{d\phi}{dt}$.

Esta ley también se aplica en [[S03-3 Tema 03 - Ecuacion de tension inducida]] para deducir la f.e.m. inducida en máquinas eléctricas.

### Descarte de otras alternativas

- **b. Ley de Hopkins**: Relaciona flujo, f.m.m. y reluctancia ($\phi = \frac{F}{\mathcal{R}}$), es la "ley de Ohm magnética". Ver [[S03-1 Tema 01 - Circuitos magneticos excitados con corriente alterna]].
- **c. Ley de Ohm**: Relaciona voltaje, corriente y resistencia ($V = I \cdot R$) en circuitos eléctricos, no involucra flujo magnético.
- **d. Ley de Ampere**: Relaciona la corriente eléctrica con el campo magnético que produce. Se estudia en [[S01-5 Tema 04 - Campo magnetico de un toroide]].
- **e. Ley de magnetomotriz**: La f.m.m. ($F = N \cdot I$) es una magnitud que impulsa el flujo en un circuito magnético, no describe la inducción de voltaje por cambio de flujo.

---

## Pregunta 3

> Una bobina con 100 espiras se conecta a una fuente de 480 V, 60 Hz. Calcular el valor pico del flujo magnético.

**Alternativas:**
- **a. 18 mWb** ✅
- b. 48 mWb
- c. 28 mWb
- d. 38 mWb

### Respuesta: a. 18 mWb

### Razonamiento

Usamos la ecuación de tensión inducida vista en [[S03-1 Tema 01 - Circuitos magneticos excitados con corriente alterna]] y [[S03-3 Tema 03 - Ecuacion de tension inducida#Caso 1 Inducido fijo. Flujo variable.]]:

$$V = 4{,}44 \cdot f \cdot N \cdot \phi_m$$

**Datos:**
- $V = 480 \text{ V}$
- $f = 60 \text{ Hz}$
- $N = 100 \text{ espiras}$

**Despejando** $\phi_m$:

$$\phi_m = \frac{V}{4{,}44 \cdot f \cdot N}$$

$$\phi_m = \frac{480}{4{,}44 \cdot 60 \cdot 100}$$

$$\phi_m = \frac{480}{26\,640}$$

$$\boxed{\phi_m = 0{,}01802 \text{ Wb} \approx 18 \text{ mWb}}$$

### Verificación con las otras alternativas

- Si $\phi_m = 48 \text{ mWb}$: $V = 4{,}44 \cdot 60 \cdot 100 \cdot 0{,}048 = 1\,278{,}7 \text{ V}$ ✗
- Si $\phi_m = 28 \text{ mWb}$: $V = 4{,}44 \cdot 60 \cdot 100 \cdot 0{,}028 = 745{,}9 \text{ V}$ ✗
- Si $\phi_m = 38 \text{ mWb}$: $V = 4{,}44 \cdot 60 \cdot 100 \cdot 0{,}038 = 1\,012{,}3 \text{ V}$ ✗

Solo $\phi_m = 18 \text{ mWb}$ produce el voltaje dado de 480 V.

---

## Pregunta 4

> Se tiene una bobina con 7200 espiras que eslabona un flujo magnético de corriente alterna que tiene un valor pico de flujo magnético de 0.25 mWb. Si la frecuencia es de 60 Hz, calcular el valor del voltaje inducido.

**Alternativas:**
- **a. 479,52 V** ✅
- b. 549,92 V
- c. 749,25 V
- d. 954752 V

### Respuesta: a. 479,52 V

### Razonamiento

Aplicamos la misma ecuación de tensión inducida de [[S03-1 Tema 01 - Circuitos magneticos excitados con corriente alterna]] y [[S03-3 Tema 03 - Ecuacion de tension inducida#Caso 1 Inducido fijo. Flujo variable.]]:

$$V = 4{,}44 \cdot f \cdot N \cdot \phi_m$$

**Datos:**
- $N = 7200 \text{ espiras}$
- $\phi_m = 0{,}25 \text{ mWb} = 0{,}00025 \text{ Wb}$
- $f = 60 \text{ Hz}$

**Cálculo:**

$$V = 4{,}44 \cdot 60 \cdot 7200 \cdot 0{,}00025$$

$$V = 4{,}44 \cdot 60 \cdot 1{,}8$$

$$V = 4{,}44 \cdot 108$$

$$\boxed{V = 479{,}52 \text{ V}}$$

### Verificación con las otras alternativas

- **b. 549,92 V**: Requeriría $\phi_m = \frac{549{,}92}{4{,}44 \cdot 60 \cdot 7200} = 0{,}000287 \text{ Wb}$ ✗
- **c. 749,25 V**: Requeriría $\phi_m = \frac{749{,}25}{4{,}44 \cdot 60 \cdot 7200} = 0{,}000391 \text{ Wb}$ ✗
- **d. 954752 V**: Valor absurdamente alto, sin sentido físico ✗

---

## Pregunta 5

> Una bobina con 4600 vueltas y un voltaje de 240 V a 3.65 mWb. Calcular la frecuencia.

**Alternativas:**
- **a. 3,21 Hz** ✅
- b. 2,31 Hz
- c. 1,23 Hz
- d. 0,23 Hz

### Respuesta: a. 3,21 Hz

### Razonamiento

Despejamos $f$ de la ecuación de [[S03-1 Tema 01 - Circuitos magneticos excitados con corriente alterna]]:

$$V = 4{,}44 \cdot f \cdot N \cdot \phi_m \quad \Rightarrow \quad f = \frac{V}{4{,}44 \cdot N \cdot \phi_m}$$

**Datos:**
- $V = 240 \text{ V}$
- $N = 4600 \text{ espiras}$
- $\phi_m = 3{,}65 \text{ mWb} = 0{,}00365 \text{ Wb}$

**Cálculo:**

$$f = \frac{240}{4{,}44 \cdot 4600 \cdot 0{,}00365}$$

$$f = \frac{240}{4{,}44 \cdot 16{,}79}$$

$$f = \frac{240}{74{,}55}$$

$$\boxed{f \approx 3{,}22 \text{ Hz} \approx 3{,}21 \text{ Hz}}$$

### Verificación con las otras alternativas

- Si $f = 2{,}31$ Hz: $V = 4{,}44 \cdot 2{,}31 \cdot 4600 \cdot 0{,}00365 = 172{,}4$ V ✗
- Si $f = 1{,}23$ Hz: $V = 4{,}44 \cdot 1{,}23 \cdot 4600 \cdot 0{,}00365 = 91{,}7$ V ✗
- Si $f = 0{,}23$ Hz: $V = 4{,}44 \cdot 0{,}23 \cdot 4600 \cdot 0{,}00365 = 17{,}1$ V ✗
