---
title: Formulario - Motores Electricos Estaticos y Rotativos
curso: "[[Motores MOC]]"
tipo: formulario
tags:
  - curso/motores
  - tipo/formulario
date: 2026-03-28
---
# Formulario: Motores Eléctricos Estáticos y Rotativos

Este documento contiene las fórmulas y conceptos fundamentales desarrollados durante las primeras sesiones del curso.

## 1. Producción del Campo Magnético
Fuente: [[S01-1 Tema 01 - Como se produce un campo magnético|S01-1 Como se produce un campo magnetico]]

### Ley de Ampère
Establece la relación entre la corriente eléctrica y la intensidad del campo magnético.
$$\oint \vec{H} \cdot d\vec{l} = I_{\text{neta}}$$

Para un núcleo ferromagnético con longitud media $l_n$ y bobina de $N$ vueltas:
$$H \cdot l_n = N \cdot i$$

### Densidad de Flujo Magnético ($B$)
Relación con la intensidad de campo ($H$):
$$B = \mu H$$

Donde:
- $\mu = \mu_0 \mu_r$ (Permeabilidad del material)
- $\mu_0 = 4\pi \times 10^{-7} \, \mathrm{H/m}$ (Vacío)
- $\mu_r = \frac{\mu}{\mu_0}$ (Permeabilidad relativa)

### Flujo Magnético ($\phi$)
$$\phi = \int_A B \, dA$$
Si $B$ es constante y perpendicular al área $A$:
$$\phi = B \cdot A = \frac{\mu N i A}{l_n}$$

---

## 2. Circuitos Magnéticos
Fuente: [[S01-2 Tema 01 - Los circuitos magnéticos|S01-2 Los circuitos magneticos]]

### Ley de Hopkinson (Análoga a la Ley de Ohm)
$$\phi = \frac{F}{\mathcal{R}}$$

### Fuerza Magnetomotriz (FMM)
$$F = N \cdot i$$

### Reluctancia ($\mathcal{R}$)
Oposición al flujo magnético. Para un núcleo uniforme:
$$\mathcal{R} = \frac{l_n}{\mu \cdot A}$$

**Asociación de Reluctancias:**
- **Serie:** $\mathcal{R}_{eq} = \mathcal{R}_1 + \mathcal{R}_2 + \dots$
- **Paralelo:** $\frac{1}{\mathcal{R}_{eq}} = \frac{1}{\mathcal{R}_1} + \frac{1}{\mathcal{R}_2} + \dots$

### Permeancia ($\mathcal{P}$)
Inverso de la reluctancia:
$$\mathcal{P} = \frac{1}{\mathcal{R}} \implies \phi = F \cdot \mathcal{P}$$

---

## 3. Leyes del Electromagnetismo
Fuente: [[S01-3 Tema 02 - Las leyes del electromagnetismo|S01-3 Las leyes del electromagnetismo]]

### Ley de Faraday-Lenz
Inducción de fuerza electromotriz (fem).
$$E = -N \cdot \frac{d\phi}{dt}$$
*El signo negativo indica que la fem se opone a la variación del flujo (Ley de Lenz).*

### Ley de Coulomb
Fuerza entre cargas eléctricas:
$$F = \frac{k \cdot q_1 \cdot q_2}{r^2}$$

### Fuerza de Lorentz
Fuerza total sobre una carga en movimiento dentro de campos eléctricos y magnéticos:
$$\vec{F} = q\vec{E} + q(\vec{v} \times \vec{B})$$

### Ley de Biot-Savart
Campo generado por un elemento de corriente:
$$d\vec{B} = \frac{\mu_0}{4\pi} \frac{I \cdot d\vec{s} \times \hat{r}}{r^2}$$

---

## 4. Casos Específicos
Fuente: [[S01-5 Tema 04 - Campo magnetico de un toroide|S01-5 Campo magnetico de un toroide]]

### Campo en un Toroide
En el interior de un toroide de radio medio $r$:
$$B = \frac{\mu_0 NI}{2\pi r}$$

### Magnetización en Materiales
Fuente: [[S01-7 Tema 05 - Obtencion de la curva de magnetizacion|S01-7 Obtencion de la curva de magnetizacion]]

- **Magnetización ($M$):** $M = \chi_m H$
- **Relación de Inducción:** $B = \mu_0(H + M) = \mu_0 H (1 + \chi_m) = \mu_0 \mu_r H = \mu H$
- **Permeabilidad Relativa:** $\mu_r = 1 + \chi_m$
  *Donde $\chi_m$ es la susceptibilidad magnética.*

### Clasificación de Materiales por $\chi_m$
- Diamagnéticos: $\mu_r \leq 1$, $\chi_m \sim -10^{-5}$
- Paramagnéticos: $\mu_r \geq 1$, $\chi_m \sim 10^{-3}$
- Ferromagnéticos: $\mu_r \gg 1$, $\chi_m$ elevado

---

## 5. Tabla de Unidades SI
Fuente: [[S01-4 Tema 03 - Sistema de unidades|S01-4 Sistema de unidades]]

| Magnitud | Símbolo | Unidad |
| :--- | :---: | :--- |
| Flujo Magnético | $\phi$ | Weber (Wb) |
| Densidad de Flujo (Inducción) | $B$ | Tesla (T) |
| Intensidad de Campo Magnético | $H$ | A-vuelta/m |
| Fuerza Magnetomotriz | $F$ | A-vuelta |
| Reluctancia | $\mathcal{R}$ | A-vuelta/Wb |
| Permeabilidad | $\mu$ | Henry/m (H/m) |
| Potencial Eléctrico | $V, E$ | Voltio (V) |
| Corriente Eléctrica | $I, i$ | Amperio (A) |

---

## 6. Circuito Magnético Excitado con Corriente Continua
Fuente: [[S02-1 Tema 01 - Circuito magnetico excitado con corriente continua|S02-1 Circuito magnetico excitado con CC]]

### Inducción Magnética en un Anillo de Rowland
$$B = \mu_a \cdot \frac{N \cdot i}{l}$$

### Relación General
$$B = \mu_0 \cdot \mu_r \cdot H$$

### Flujo Magnético a partir de FMM y Reluctancia
$$\phi = B \cdot S = \frac{N \cdot i}{\dfrac{l}{\mu_r \cdot \mu_0 \cdot S}} = \frac{F}{\mathcal{R}}$$

### Permeabilidad Relativa (desde curva B-H)
$$\mu_r = \frac{B}{\mu_0 \cdot H}$$

### Método Directo — Circuito con Núcleo de Hierro

Inducción en el hierro:
$$B_{fe} = \frac{\phi}{S_{fe}}$$

Amper-vueltas del hierro (con $H_{fe}$ obtenido de la curva $B = f(H)$):
$$H_{fe} \cdot l_{fe} = (N \cdot i)_{fe}$$

### Sección Efectiva (Núcleo Laminado)
$$S_{fe} = K_{fe} \cdot S$$

Donde:
- $K_{fe}$ = factor de laminación (típicamente 0,90 a 0,95)

### Método Directo — Entrehierro

Sección ideal del entrehierro:
$$S_\delta = (a + \delta)(b + \delta)$$

Inducción en el entrehierro:
$$B_\delta = \frac{\phi}{S_\delta}$$

Intensidad de campo en el aire ($\mu_r = 1$):
$$H_\delta = \frac{B_\delta}{\mu_0}$$

Amper-vueltas del entrehierro:
$$H_\delta \cdot \delta = (N \cdot i)_\delta$$

### Circuito Magnético Completo (Hierro + Entrehierro)
$$H_{fe} \cdot l_{fe} + H_\delta \cdot l_\delta = (N \cdot i)_{fe} + (N \cdot i)_\delta = N \cdot i$$

Corriente necesaria:
$$i = I = \frac{N \cdot i}{N}$$

---

## 7. Permeabilidad Magnética y Entrehierro
Fuente: [[S02-3 Tema 02 - Caracteristicas para crear un campo magnetico|S02-3 Caracteristicas para crear un campo magnetico]]

### Permeabilidad Relativa
$$\mu_r = \frac{\mu}{\mu_0}$$

### Susceptibilidad Magnética
$$\chi_m = \mu_r - 1$$

### Permeabilidad Absoluta
$$\mu = \mu_r \cdot \mu_0$$

### Clasificación de Materiales por $\mu_r$

| Tipo | $\mu_r$ | Ejemplo |
| :--- | :---: | :--- |
| Ferromagnético | $\mu_r \gg 1$ | Hierro, aleaciones |
| Paramagnético | $\mu_r \approx 1$ | Aluminio, aire |
| Diamagnético | $\mu_r < 1$ | Cobre, bismuto |

### Sección del Entrehierro (fórmula empírica)
$$S_\delta = (a + \delta)(b + \delta)$$

Donde:
- $a$, $b$ = lados de la sección del hierro
- $\delta$ = longitud del entrehierro

---

## 8. Lazo de Histéresis y Pérdidas Magnéticas
Fuente: [[S02-4 Tema 03 - Lazo de histeresis|S02-4 Lazo de histeresis]]
Fuente: [[S04-3 Tema 02 - Obtencion del lazo de histeresis|S04-3 Obtencion del lazo de histeresis]]

### Energía del Ciclo de Histéresis
$$dE = S \cdot L_m \cdot H \cdot dB$$

Donde:
- $S$ = sección transversal del núcleo
- $L_m$ = longitud magnética

### Fórmula de Steinmetz (Pérdidas por Histéresis)
$$P_H = K_H \cdot f \cdot B^{2}_{\max} \quad \left[\frac{\text{W}}{\text{kg}}\right]$$

Donde:
- $K_H$ = constante del tipo de chapa magnética
- $f$ = frecuencia $[\text{Hz}]$
- $B_{\max}$ = inducción máxima $[\text{T}]$

### Ecuación de Fröelich (curva de magnetización analítica)
$$B = \frac{a \cdot H}{1 + b \cdot H}$$

Donde:
- $a$, $b$ = constantes propias del material, elegidas para aproximar la curva real $B = f(H)$
- $B$ = inducción magnética $[\text{T}]$
- $H$ = intensidad de campo magnético $[A \cdot v/m]$

### Permeabilidad Variable (curva no lineal)
$$\mu = \frac{B}{H}$$

*La permeabilidad del material ferromagnético no es constante — depende del valor de $H$ en la curva de magnetización.*

### Parámetros característicos del ciclo de histéresis
- **Inducción remanente $B_r$:** valor de $B$ cuando $H = 0$ (magnetización permanente).
- **Campo coercitivo $H_c$:** valor de $H$ opuesto necesario para anular la magnetización remanente ($B = 0$).
- **Área del ciclo $\propto$ energía disipada por unidad de volumen por ciclo** (pérdidas por histéresis).

---

## 9. Métodos de Análisis de Circuitos Magnéticos
Fuente: [[S02-5 Tema 04 - Metodos de analisis|S02-5 Metodos de analisis]]

### Ley de Circuitación (circuito serie hierro + entrehierro)
$$F = Ni = H_{Fe} \cdot l_{Fe} + H_e \cdot l_e$$

### Recta de Carga (Método Gráfico)
$$H_{Fe} = \frac{Ni}{l_{Fe}} - \frac{B_{Fe} \cdot l_e}{\mu_0 \cdot l_{Fe}}$$

Donde:
- Intersección eje $B$: $B = \frac{Ni \cdot \mu_0}{l_e}$ (punto A)
- Intersección eje $H$: $H = \frac{Ni}{l_{Fe}}$ (punto B)
- El punto de operación es la intersección de la recta con la curva $B = f(H)$

---

## 10. Circuito Magnético Excitado con Corriente Alterna
Fuente: [[S03-1 Tema 01 - Circuitos magneticos excitados con corriente alterna|S03-1 Circuitos magneticos excitados con CA]]

### Tensión en Bobina con Núcleo de Hierro (Ley de Faraday)
$$v = R \cdot i + N \frac{d\phi}{dt}$$

Aproximación (despreciando resistencia):
$$v \approx N \frac{d\phi}{dt}$$

### Flujo en función de la tensión aplicada
$$\phi(t) = \frac{\sqrt{2}}{N \cdot \omega} \cdot V \cdot \text{sen} \, \omega t$$

### Flujo Máximo
$$\phi_m = \frac{\sqrt{2} \cdot V}{N \cdot \omega}$$

### Ecuación Fundamental del Transformador
$$V = 4{,}44 \cdot f \cdot N \cdot \phi_m$$

### Momento de Fuerza sobre una Espira
$$\tau = I \cdot B \cdot A$$

### Momento Magnético
$$\vec{\mu} = I \cdot \vec{A} \quad [\text{A} \cdot \text{m}^2]$$

### Momento de Fuerzas (general)
$$\vec{\tau} = \vec{\mu} \times \vec{B}$$

### Corrientes Trifásicas del Estator
$$i_{aa'}(t) = I_M \cdot \text{sen} \, \omega t$$
$$i_{bb'}(t) = I_M \cdot \text{sen} (\omega t - 120°)$$
$$i_{cc'}(t) = I_M \cdot \text{sen} (\omega t - 240°)$$

---

## 11. Núcleo Ferromagnético Excitado con CA Sinusoidal
Fuente: [[S03-2 Tema 02 - Nucleo ferromagnetico excitado con CA sinusoidal|S03-2 Nucleo ferromagnetico excitado con CA sinusoidal]]

### Autoinducción de Bobina con Núcleo (sin pérdidas)
$$L = \frac{\mu \cdot N^2 \cdot S}{l}$$

### Pérdidas en el Hierro
$$P_{Fe} = V \cdot I_{exc} \cdot \cos \phi_v$$

### Componentes de la Corriente de Excitación
$$I_{Fe} = I_{exc} \cdot \cos \phi_v \qquad I_\mu = I_{exc} \cdot \text{sen} \, \phi_v$$

$$\vec{I_{exc}} = \vec{I_{Fe}} + \vec{I_\mu} \qquad I_{exc} = \sqrt{I_{Fe}^2 + I_\mu^2}$$

### Factor de Potencia de Excitación
$$\cos \phi_v = \frac{I_{Fe}}{I_{exc}}$$

### Tensión en Inductancia
$$v = L \frac{di}{dt}$$

### Circuito Equivalente (con pérdidas)
$$R_{Fe} = \frac{V}{I_{Fe}} \qquad X_\mu = \frac{V}{I_\mu}$$

Donde:
- $R_{Fe}$ = resistencia equivalente de pérdidas en el hierro
- $X_\mu$ = reactancia magnetizante
- $I_{Fe}$ = componente de pérdidas
- $I_\mu$ = corriente magnetizante

---

## 12. Ecuación de Tensión Inducida
Fuente: [[S03-3 Tema 03 - Ecuacion de tension inducida|S03-3 Ecuacion de tension inducida]]

### Flujo en el Entrehierro
$$\phi_1 = \phi_m \cos \omega t \cos p\alpha$$

### F.E.M. Inducida (caso general)
$$e_2 = -N_2 \frac{d\phi}{dt}$$

### Pulsación de la F.E.M. Inducida
$$\omega_2 = \omega_1 \pm p\Omega$$

### Relación de Frecuencias (ecuación fundamental)
$$f_2 = f_1 \pm \frac{n \cdot p}{60}$$

Donde:
- $f_1$ = frecuencia del inductor
- $f_2$ = frecuencia del inducido
- $n$ = velocidad del rotor [rpm]
- $p$ = número de pares de polos
- $\omega_1 = 2\pi f_1$, $\omega_2 = 2\pi f_2$, $\Omega = \frac{2\pi n}{60}$

### Caso 1: Inducido Fijo — Transformador ($\Omega = 0$)

F.E.M. instantánea:
$$e_2 = N_2 \omega_1 \phi_m \, \text{sen} \, \omega_1 t \cos p\alpha$$

Valor eficaz:
$$E_2 = \frac{N_2 \omega_1 \phi_m}{\sqrt{2}} = 4{,}44 \cdot N_2 \cdot f_1 \cdot \phi_m$$

### Caso 2: Inducido Móvil — Máquina Síncrona ($\omega_1 = 0$)

F.E.M. instantánea:
$$e_2 = N_2 p\Omega \phi_m \, \text{sen} \, p\Omega t$$

Valor eficaz:
$$E_2 = \frac{N_2 p\Omega \phi_m}{\sqrt{2}} = 4{,}44 \cdot N_2 \cdot f_2 \cdot \phi_m$$

$$f_2 = \frac{n \cdot p}{60}$$
