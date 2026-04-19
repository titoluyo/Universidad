---
title: Ejercicio resuelto - Circuito equivalente de excitacion (Video)
curso: "[[Motores MOC]]"
unidad: 1
semana: 4
orden: 2
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/corriente-excitacion
  - tema/circuito-equivalente
  - tema/reactancia-magnetizante
  - tema/perdidas-nucleo
date: 2026-04-19
---

> [!info] Fuente
> Video: [Semana 4 - Excitación de flujo sinusoidal de corriente alterna](https://www.youtube.com/watch?v=RFYg8INKmjw) — Aprendizaje Virtual UTP (11:25)

## Enunciado

Una bobina con núcleo de hierro tiene **500 espiras**, siendo su **resistencia despreciable**. La sección del núcleo es uniforme y vale **25 cm²**, siendo la longitud magnética media igual a **80 cm**. La curva de imanación del material es:

$$B = \frac{2H}{150 + H} \quad ; \quad B \text{ [Teslas]}; \quad H \left[\frac{A \cdot v}{m}\right]$$

![[video-s04-ej-enunciado.png]]
![[video-s04-ej-datos-completos.png]]
**Figura 1.** Enunciado del problema con la curva de imanación del material.

Si la tensión aplicada es alterna y de **220 V eficaces** y la frecuencia es de **60 Hz**, se pide calcular el **circuito equivalente de la excitación**.

Tengamos en cuenta que, por la información proporcionada por el constructor, se conoce que a la tensión nominal de 220 V las pérdidas en el núcleo son de **5 W/kg**. El peso específico del material es igual a **7,8 kg/dm³**.

![[video-s04-ej-pregunta.png]]
**Figura 2.** Datos adicionales: pérdidas específicas y peso específico del material.

### Datos

- $N = 500$ espiras
- $S = 25 \, \text{cm}^2 = 25 \times 10^{-4} \, \text{m}^2$
- $l = 80 \, \text{cm} = 0{,}80 \, \text{m}$
- $V = 220 \, \text{V}$ (valor eficaz)
- $f = 60 \, \text{Hz}$
- $P'_{Fe} = 5 \, \text{W/kg}$ (pérdidas específicas en el núcleo)
- $d = 7{,}8 \, \text{kg/dm}^3$ (densidad / peso específico del material)
- Resistencia del devanado despreciable
- Curva de imanación: $B = \dfrac{2H}{150 + H}$

---

## Resolución

### Paso 1: Cálculo de la masa del núcleo

La masa del núcleo se obtiene multiplicando la densidad por el volumen:

$$m = d \cdot V_{vol} = d \cdot l \cdot S$$

Donde:
- $m$ = masa del núcleo [kg]
- $d$ = densidad (peso específico) del material [kg/dm³]
- $V_{vol}$ = volumen del núcleo [dm³]
- $l$ = longitud magnética media [m]
- $S$ = sección transversal del núcleo [m²]

$$m = 7{,}8 \, \frac{\text{kg}}{\text{dm}^3} \times 0{,}80 \, \text{m} \times 25 \times 10^{-4} \, \text{m}^2$$

Convirtiendo el volumen a $\text{dm}^3$: $l \cdot S = 0{,}80 \times 25 \times 10^{-4} = 2 \times 10^{-3} \, \text{m}^3 = 2 \, \text{dm}^3$

$$\boxed{m = 15{,}6 \, \text{kg}}$$

### Paso 2: Pérdidas en el núcleo

Las pérdidas totales en el núcleo se obtienen como el producto de las pérdidas específicas por la masa:

$$P_{Fe} = P'_{Fe} \cdot m$$

Donde:
- $P_{Fe}$ = pérdidas totales en el núcleo de hierro [W]
- $P'_{Fe}$ = pérdidas específicas en el hierro [W/kg] (dato del constructor)
- $m$ = masa del núcleo [kg]

$$P_{Fe} = 5 \, \frac{W}{kg} \times 15{,}6 \, \text{kg}$$

$$\boxed{P_{Fe} = 78 \, \text{W}}$$

### Paso 3: Corriente en el núcleo $I_{Fe}$ (componente activa)

La corriente en el núcleo representa la componente activa de la corriente de excitación, responsable de las pérdidas. Aplicando la **ley de Watts**:

$$P_{Fe} = V \cdot I_{Fe}$$

Donde:
- $P_{Fe}$ = pérdidas en el núcleo [W]
- $V$ = tensión eficaz aplicada a la bobina [V]
- $I_{Fe}$ = corriente activa (de pérdidas en el hierro), en fase con $V$ [A]

$$I_{Fe} = \frac{P_{Fe}}{V} = \frac{78 \, \text{W}}{220 \, \text{V}}$$

$$\boxed{I_{Fe} = 0{,}354 \, \text{A}}$$

### Paso 4: Resistencia del núcleo $R_{Fe}$

$$R_{Fe} = \frac{V}{I_{Fe}}$$

Donde:
- $R_{Fe}$ = resistencia equivalente que modela las pérdidas en el hierro [Ω]
- $V$ = tensión aplicada [V]
- $I_{Fe}$ = corriente por la rama resistiva del circuito equivalente [A]

$$R_{Fe} = \frac{220 \, \text{V}}{0{,}354 \, \text{A}}$$

$$\boxed{R_{Fe} = 621{,}5 \, \Omega}$$

![[video-s04-ej-resistencia-nucleo.png]]
**Figura 3.** Cálculo de la masa, pérdidas, corriente del núcleo y resistencia $R_{Fe}$.

### Paso 5: Planteamiento de la reactancia magnetizante $X_\mu$

La reactancia magnetizante es igual al voltaje sobre la corriente magnetizante, que es la corriente que circula por la rama inductiva del circuito equivalente:

$$X_\mu = \frac{V}{I_\mu}$$

Donde:
- $X_\mu$ = reactancia magnetizante (rama inductiva del circuito equivalente) [Ω]
- $V$ = tensión aplicada a la bobina [V]
- $I_\mu$ = corriente magnetizante, retrasada 90° respecto a $V$ [A]

Para obtener $X_\mu$ necesitamos primero calcular $I_\mu$. Para ello partimos del flujo máximo en el núcleo, obtenemos la densidad de flujo $B_m$, aplicamos la curva de imanación para hallar $H_m$ y, finalmente, con la ley de Ampère despejamos $I_\mu$.

### Paso 6: Flujo máximo en el núcleo

Aplicando la [[S03-3 Tema 03 - Ecuacion de tension inducida|ecuación de tensión inducida]]:

$$V = 4{,}44 \cdot N \cdot f \cdot \phi_m$$

Donde:
- $V$ = valor eficaz de la tensión aplicada [V]
- $N$ = número de espiras del devanado
- $f$ = frecuencia de la tensión [Hz]
- $\phi_m$ = flujo magnético máximo en el núcleo [Wb]
- $4{,}44 = \pi \sqrt{2}$ (factor que aparece al relacionar valor eficaz y máximo de una onda sinusoidal)

Despejando el flujo máximo:

$$\phi_m = \frac{V}{4{,}44 \cdot N \cdot f} = \frac{220}{4{,}44 \times 500 \times 60}$$

$$\boxed{\phi_m = 1{,}65 \times 10^{-3} \, \text{Wb}}$$

### Paso 7: Densidad de flujo máximo $B_m$

$$B_m = \frac{\phi_m}{S}$$

Donde:
- $B_m$ = densidad de flujo magnético máxima (inducción máxima) [T = Wb/m²]
- $\phi_m$ = flujo magnético máximo [Wb]
- $S$ = sección transversal del núcleo [m²]

$$B_m = \frac{1{,}65 \times 10^{-3} \, \text{Wb}}{25 \times 10^{-4} \, \text{m}^2}$$

$$\boxed{B_m = 0{,}66 \, \text{T}}$$

![[video-s04-ej-flujo-maximo.png]]
**Figura 4.** Cálculo de la densidad de flujo máximo.

### Paso 8: Intensidad de campo magnético máxima $H_m$

Aplicando la curva de imanación con $B_m$:

$$B_m = \frac{2 H_m}{150 + H_m}$$

Donde:
- $B_m$ = densidad de flujo máxima en el núcleo [T]
- $H_m$ = intensidad de campo magnético máxima [A·vuelta/m]
- Los valores $2$ y $150$ son constantes propias de la curva de imanación del material dado

$$0{,}66 \, (150 + H_m) = 2 H_m$$

$$99 + 0{,}66 \, H_m = 2 \, H_m \Rightarrow 99 = 1{,}34 \, H_m$$

$$\boxed{H_m = 73{,}88 \, \frac{A \cdot v}{m}}$$

### Paso 9: Intensidad de campo magnético eficaz $H$

Para trabajar con la ley de Ampère en régimen sinusoidal, utilizamos el valor eficaz:

$$H = \frac{H_m}{\sqrt{2}}$$

Donde:
- $H$ = intensidad de campo magnético eficaz [A·vuelta/m]
- $H_m$ = intensidad de campo magnético máxima (pico) [A·vuelta/m]
- $\sqrt{2}$ = factor que relaciona el valor máximo con el eficaz de una onda sinusoidal

$$H = \frac{73{,}88}{\sqrt{2}}$$

$$\boxed{H = 52{,}24 \, \frac{A \cdot v}{m}}$$

![[video-s04-ej-h-campo.png]]
**Figura 5.** Aplicación de la curva de imanación para obtener $H_m$ y $H$ eficaz.

### Paso 10: Corriente magnetizante $I_\mu$

Por la [[S01-3 Tema 02 - Las leyes del electromagnetismo|ley de Ampère]] aplicada al circuito magnético:

$$F_{mm} = H \cdot l = N \cdot I_\mu$$

Donde:
- $F_{mm}$ = fuerza magnetomotriz [A·vuelta]
- $H$ = intensidad de campo magnético eficaz [A·vuelta/m]
- $l$ = longitud magnética media del núcleo [m]
- $N$ = número de espiras de la bobina
- $I_\mu$ = corriente magnetizante eficaz [A]

Despejando la corriente magnetizante:

$$I_\mu = \frac{H \cdot l}{N} = \frac{52{,}24 \times 0{,}80}{500}$$

$$\boxed{I_\mu = 0{,}0835 \, \text{A}}$$

### Paso 11: Reactancia magnetizante $X_\mu$ (cálculo numérico)

Reemplazando en la fórmula planteada en el Paso 5:

$$X_\mu = \frac{V}{I_\mu} = \frac{220 \, \text{V}}{0{,}0835 \, \text{A}}$$

$$\boxed{X_\mu \approx 2635 \, \Omega}$$

### Paso 12: Corriente de excitación $I_{exc}$

La corriente de excitación es la suma vectorial de la corriente del núcleo (activa, en fase con $V$) y la corriente magnetizante (reactiva, en cuadratura):

$$I_{exc} = \sqrt{I_{Fe}^2 + I_\mu^2}$$

Donde:
- $I_{exc}$ = corriente de excitación total absorbida por la bobina [A]
- $I_{Fe}$ = componente activa (en fase con $V$), asociada a las pérdidas [A]
- $I_\mu$ = componente reactiva (retrasada 90° respecto a $V$), asociada a la magnetización [A]

$$I_{exc} = \sqrt{(0{,}354)^2 + (0{,}0835)^2}$$

$$\boxed{I_{exc} = 0{,}363 \, \text{A}}$$

![[video-s04-ej-corriente-excitacion.png]]
**Figura 6.** Diagrama fasorial de las corrientes y cálculo de la corriente de excitación.

### Paso 13: Ángulo del vector $I_{exc}$

El ángulo del vector respecto a la tensión $V$ (equivalente a la componente $I_{Fe}$):

$$\theta_v = \arctan\left(\frac{I_\mu}{I_{Fe}}\right)$$

Donde:
- $\theta_v$ = ángulo de desfase entre $I_{exc}$ y $V$ [°]
- $I_\mu$ = corriente magnetizante (cateto opuesto en el triángulo de corrientes) [A]
- $I_{Fe}$ = corriente activa (cateto adyacente, en fase con $V$) [A]

$$\theta_v = \arctan\left(\frac{0{,}0835}{0{,}354}\right) \approx 13{,}28°$$

---

## Circuito equivalente

![[video-s04-ej-reactancia-magnetizante.png]]
**Figura 7.** Circuito equivalente de excitación y diagrama fasorial.

El circuito equivalente de la excitación consta de dos ramas en paralelo conectadas a la tensión $V$:

- **Rama activa (resistiva):** $R_{Fe}$ representa las pérdidas en el hierro. Por ella circula $I_{Fe}$, en fase con $V$.
- **Rama reactiva (inductiva):** $X_\mu = L\omega$ representa la magnetización del núcleo. Por ella circula $I_\mu$, retrasada 90° respecto a $V$.

$$I_{exc} = I_{Fe} + I_\mu \quad \text{(suma vectorial)}$$

## Resultados

| Magnitud | Símbolo | Valor |
| :--- | :---: | :---: |
| Masa del núcleo | $m$ | $15{,}6 \, \text{kg}$ |
| Pérdidas en el núcleo | $P_{Fe}$ | $78 \, \text{W}$ |
| Corriente del núcleo (activa) | $I_{Fe}$ | $0{,}354 \, \text{A}$ |
| Resistencia del núcleo | $R_{Fe}$ | $621{,}5 \, \Omega$ |
| Flujo máximo | $\phi_m$ | $1{,}65 \times 10^{-3} \, \text{Wb}$ |
| Densidad de flujo máxima | $B_m$ | $0{,}66 \, \text{T}$ |
| Intensidad de campo máxima | $H_m$ | $73{,}88 \, A \cdot v/m$ |
| Intensidad de campo eficaz | $H$ | $52{,}24 \, A \cdot v/m$ |
| Corriente magnetizante | $I_\mu$ | $0{,}0835 \, \text{A}$ |
| Reactancia magnetizante | $X_\mu$ | $\approx 2635 \, \Omega$ |
| Corriente de excitación | $I_{exc}$ | $0{,}363 \, \text{A}$ |
| Ángulo | $\theta_v$ | $\approx 13{,}28°$ |

> [!tip] Componentes de la corriente de excitación
> La corriente de excitación $I_{exc}$ que absorbe la bobina con núcleo ferromagnético tiene dos componentes:
> - **$I_{Fe}$** (activa, en fase con $V$): corresponde a las **pérdidas en el núcleo** (histéresis + corrientes parásitas).
> - **$I_\mu$** (reactiva, retrasada 90° respecto a $V$): corresponde a la **magnetización del núcleo** y crea el flujo sinusoidal.
