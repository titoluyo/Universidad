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
Fuente: [[S05-1 Tema 01 - Perdidas magneticas en el nucleo|S05-1 Perdidas magneticas en el nucleo]]

### Energía del Ciclo de Histéresis
$$dE = S \cdot L_m \cdot H \cdot dB$$

Donde:
- $S$ = sección transversal del núcleo
- $L_m$ = longitud magnética

### Energía absorbida y devuelta en una rama del ciclo

Energía absorbida (tramo $-B_r \rightarrow B_m$, abc):
$$W_{ac} = vol \int_{-B_r}^{B_m} H \cdot dB = vol \cdot w_1$$

Energía devuelta a la red (tramo $B_m \rightarrow B_r$, ce):
$$W_{ce} = vol \int_{B_m}^{B_r} H \cdot dB = vol \cdot w_2$$

Energía total disipada por ciclo (área del lazo):
$$W_H = (vol) \oint H \cdot dB$$

Potencia disipada por histéresis (con frecuencia $f$):
$$P_H = f \cdot W_H = f \cdot (vol) \oint H \cdot dB = f \cdot (vol) \cdot (\text{área del ciclo})$$

### Fórmula de Steinmetz (Pérdidas por Histéresis)
$$P_H = k_H \cdot f \cdot (vol) \cdot B_m^{\alpha}$$

Forma alternativa por unidad de masa:
$$P_H = K_H \cdot f \cdot B^{2}_{\max} \quad \left[\frac{\text{W}}{\text{kg}}\right]$$

Donde:
- $k_H$ = coeficiente de Steinmetz (depende del material)
- $\alpha$ = exponente de Steinmetz, entre 1,5 y 2,5 (valor frecuente $\alpha = 1{,}6$)
- Para acero al silicio: $k_H$ entre 100 y 200
- $f$ = frecuencia $[\text{Hz}]$
- $B_m = B_{\max}$ = inducción máxima $[\text{T}]$

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

---

## 13. Pérdidas por Corrientes de Foucault y Pérdidas Totales en el Hierro
Fuente: [[S05-1 Tema 01 - Perdidas magneticas en el nucleo|S05-1 Perdidas magneticas en el nucleo]]

### Inducción alterna en el núcleo
$$B_z = B_z \cos \omega t$$

### Flujo en la espira sombreada (chapa)
$$\phi = 2 b y B_m \cos \omega t$$

### F.E.M. inducida (Ley de Faraday)
$$e = 2 \omega b y B_m \, \text{sen} \, \omega t$$

### Resistencia de la espira
$$R = \frac{2b}{\sigma \cdot dy}$$

Donde:
- $\sigma$ = conductividad del material
- $y$ = espesor de la chapa magnética, varía entre $0$ y $\frac{a}{2}$
- $a$ = espesor total de la chapa
- $b$ = ancho de la chapa

### Potencia instantánea en la espira
$$dP_F = R \cdot i^2 = \frac{e^2}{R} = \frac{4 \omega^2 \cdot b^2 \cdot y^2 \cdot B_m^2 \cdot \sigma \cdot \text{sen}^2 \omega t \cdot dy}{2b}$$

### Potencia media diferencial
$$dP_F = \omega^2 \cdot b \cdot y^2 \cdot B_m^2 \cdot \sigma \cdot dy$$

### Potencia disipada total (integrando)
$$P_F = \int_0^{a/2} \omega^2 B_m^2 b \sigma y^2 \, dy = \frac{\omega^2}{24} B_m^2 \cdot a^3 \cdot b \cdot \sigma$$

### Pérdidas por corrientes de Foucault por unidad de volumen
$$\frac{P_F}{vol} = \pi^2 f^2 B_m^2 a^2 \frac{\sigma}{6} = k_F \cdot f^2 \cdot B_m^2 \cdot a^2 \cdot \sigma$$

> [!info] A mayor frecuencia, chapas más delgadas
> Las pérdidas por Foucault crecen con $f^2$ y con $a^2$. Para frecuencias elevadas se requieren chapas magnéticas de menor espesor.

### Pérdidas totales en el hierro (histéresis + Foucault)
$$P_{Fe} = P_H + P_F = k_H \cdot f \cdot B_m^{\alpha} + k_F \cdot f^2 \cdot B_m^2 \cdot a^2 \cdot \sigma$$

El fabricante del material magnético suministra las curvas de pérdidas totales en función de $B$ a frecuencia constante.

---

## 14. Reactor con Núcleo de Hierro (Sección Cruciforme)
Fuente: [[S06-1 Tema 01 - El reactor con núcleo de hierro|S06-1 El reactor con núcleo de hierro]]

### Sección cruciforme de tres escalones
Área real de hierro:
$$S = b^2 + 2ac - 2bc$$

Relación geométrica de la sección inscrita en el círculo de diámetro $d$:
$$d^2 = a^2 + c^2 \hspace{0.5cm};\hspace{0.5cm} d^2 = 2b^2$$

Expresión despejando $c$:
$$S = \frac{d^2}{2} + 2a\sqrt{d^2 - a^2} - d\sqrt{2(d^2 - a^2)}$$

### Dimensiones óptimas (3 escalones)
Para máximo aprovechamiento del espacio interno del devanado:
$$a = 0{,}906 \cdot d \hspace{0.5cm};\hspace{0.5cm} b = 0{,}707 \cdot d \hspace{0.5cm};\hspace{0.5cm} c = 0{,}423 \cdot d$$

Donde:
- $d$ = diámetro de la circunferencia que circunscribe al núcleo
- $a$, $b$, $c$ = anchos de las láminas (escalón externo, intermedio e interno)
- $S$ = área real de hierro del núcleo cruciforme

---

## 15. Transformador Monofásico Ideal
Fuente: [[S06-4 Tema 02 - El transformador monofásico ideal|S06-4 El transformador monofásico ideal]]

### Relación de transformación
$$\frac{V_P(t)}{V_S(t)} = \frac{N_P}{N_S} = a$$

### Relación de corrientes (Ley de Ampere aplicada al núcleo)
$$N_P \cdot i_P(t) = N_S \cdot i_S(t) \hspace{0.5cm} \Longrightarrow \hspace{0.5cm} \frac{i_P(t)}{i_S(t)} = \frac{1}{a}$$

### Forma fasorial
$$\frac{V_P}{V_S} = a \hspace{0.5cm};\hspace{0.5cm} \frac{I_P}{I_S} = \frac{1}{a}$$

### Potencia activa
$$P_{in} = V_P \cdot I_P \cdot \cos \theta_P \hspace{0.5cm};\hspace{0.5cm} P_{out} = V_S \cdot I_S \cdot \cos \theta_S$$

En el transformador ideal $\theta_S = \theta_P = \theta$, y por tanto:
$$P_{in} = P_{out}$$

### Conservación de potencias reactiva y aparente
$$Q_{in} = V_P \cdot I_P \cdot \sin\theta = V_S \cdot I_S \cdot \sin\theta = Q_{out}$$
$$S_{in} = V_P \cdot I_P = V_S \cdot I_S = S_{out}$$

---

## 16. Polaridad e Impedancia Reflejada
Fuente: [[S06-6 Tema 02 - Polaridad y conversión de impedancias|S06-6 Polaridad y conversión de impedancias]]

### Impedancia de la carga
$$\mathbf{Z}_L = \frac{\mathbf{V}_S}{\mathbf{I}_S}$$

### Impedancia aparente vista desde el primario
$$\mathbf{Z}_L^{\prime} = \frac{\mathbf{V}_P}{\mathbf{I}_P} = \frac{a\,\mathbf{V}_S}{\dfrac{\mathbf{I}_S}{a}} = a^2 \cdot \mathbf{Z}_L$$

> [!info] Regla de los puntos (dot convention)
> - Polaridad de voltaje: el extremo marcado del primario y el extremo marcado del secundario son positivos en simultáneo.
> - Corriente: si entra al punto del primario, **sale** por el punto del secundario.

---

## 17. Transformador Real — Circuito Equivalente
Fuente: [[S07-1 Tema 01 - Circuito equivalente exacto y aproximado del transformador real|S07-1 Circuito equivalente exacto y aproximado del trafo real]]

### Flujos totales y flujos de dispersión
$$\Phi_1 = \Phi + \Phi_{d1} \hspace{0.5cm};\hspace{0.5cm} \Phi_2 = \Phi + \Phi_{d2}$$

### Coeficientes de autoinducción de dispersión
$$L_{d1} = N_1 \, \frac{d\Phi_{d1}}{di_1} \hspace{0.5cm};\hspace{0.5cm} L_{d2} = N_2 \, \frac{d\Phi_{d2}}{di_2}$$

### Reactancias de dispersión
$$X_1 = L_{d1} \, \omega \hspace{0.5cm};\hspace{0.5cm} X_2 = L_{d2} \, \omega$$

### Ecuaciones de Kirchhoff (fasoriales)
$$\mathbf{V}_1 = \mathbf{E}_1 + R_1 \, \mathbf{I}_1 + jX_1 \, \mathbf{I}_1$$
$$\mathbf{V}_2 = \mathbf{E}_2 - R_2 \, \mathbf{I}_2 - jX_2 \, \mathbf{I}_2$$

### F.e.m. inducidas (valores eficaces)
$$E_1 = 4{,}44 \cdot f \cdot N_1 \cdot \Phi_m \hspace{0.5cm};\hspace{0.5cm} E_2 = 4{,}44 \cdot f \cdot N_2 \cdot \Phi_m$$

### Reducción al primario (transformador equivalente con $N'_2 = N_1$)
| Magnitud | Real | Equivalente |
| -------- | ---- | ----------- |
| Voltaje  | $E_2$, $V_2$ | $E'_2 = a \cdot E_2$, $V'_2 = a \cdot V_2$ |
| Corriente | $I_2$ | $I'_2 = I_2 / a$ |
| Resistencia | $R_2$ | $R'_2 = a^2 \cdot R_2$ |
| Reactancia | $X_2$ | $X'_2 = a^2 \cdot X_2$ |
| Impedancia | $Z_L$ | $\mathbf{Z}'_L = a^2 \cdot \mathbf{Z}_L$ |

### Impedancia de cortocircuito (circuito equivalente aproximado)
$$\boxed{R_{cc} = R_1 + R'_2 \hspace{0.4cm};\hspace{0.4cm} X_{cc} = X_1 + X'_2}$$

Para transformadores grandes ($X_{cc} \gg R_{cc}$) suele usarse solo $X_{cc}$.

---

## 18. Ensayo de Vacío
Fuente: [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real|S07-3 Ensayo de vacío y cortocircuito]]

### Condición de medida
Primario alimentado a $V_{1n}$, secundario en circuito abierto. Se miden $P_0$, $I_0$, $V_{20}$.

### Pérdidas en el hierro
$$P_0 \approx P_{Fe}$$

### Factor de potencia en vacío
$$P_0 = V_{1n} \cdot I_0 \cdot \cos\varphi_0$$

### Componentes de la corriente de vacío
$$I_{Fe} = I_0 \cos\varphi_0 \hspace{0.5cm};\hspace{0.5cm} I_\mu = I_0 \sin\varphi_0$$

### Parámetros de la rama paralela
$$R_{Fe} = \frac{V_1}{I_{Fe}} \hspace{0.5cm};\hspace{0.5cm} X_\mu = \frac{V_1}{I_\mu}$$

Forma alterna directa con $P_0$:
$$R_{Fe} = \frac{V_{1n}^2}{P_0}$$

### Relación de transformación
$$a = \frac{N_1}{N_2} = \frac{E_1}{E_2} = \frac{V_{1n}}{V_{20}}$$

---

## 19. Ensayo de Cortocircuito
Fuente: [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real|S07-3 Ensayo de vacío y cortocircuito]]

### Condición de medida
Secundario cortocircuitado, $V_1$ se eleva desde 0 hasta que $I_1 = I_{1n}$. Se miden $V_{1cc}$, $I_{1cc}=I_{1n}$, $P_{cc}$.

### Pérdidas en el cobre
$$P_{cc} \approx P_{Cu}$$

### Impedancia de cortocircuito
$$Z_{cc} = \frac{V_{1cc}}{I_{1n}}$$

### Resistencia de cortocircuito
$$R_{cc} = \frac{P_{cc}}{I_{1n}^{\,2}}$$

### Reactancia de cortocircuito
$$X_{cc} = \sqrt{Z_{cc}^{\,2} - R_{cc}^{\,2}}$$

### Factor de potencia en cortocircuito
$$\cos\varphi_{cc} = \frac{P_{cc}}{V_{1cc} \cdot I_{1n}}$$

### Caídas de tensión (diagrama vectorial)
$$V_{R_{cc}} = R_{cc} \, I_{1n} = V_{1cc} \cos\varphi_{cc}$$
$$V_{X_{cc}} = X_{cc} \, I_{1n} = V_{1cc} \sin\varphi_{cc}$$

### Reparto entre primario y secundario (referidos al primario)
$$R_1 = R'_2 = \frac{R_{cc}}{2} \hspace{0.5cm};\hspace{0.5cm} X_1 = X'_2 = \frac{X_{cc}}{2}$$

### Conversión a magnitudes nominales (si el ensayo no se hizo con $I_{1n}$)
$$V_{1cc} = V_{1corto} \cdot \frac{I_{1n}}{I_{1corto}} \hspace{0.4cm};\hspace{0.4cm} P_{cc} = P_{corto} \cdot \frac{I_{1n}^{\,2}}{I_{1corto}^{\,2}}$$

---

## 20. Tensión de Cortocircuito Porcentual y Corriente de Falta
Fuente: [[S07-3 Tema 02 - Ensayo de vacío y de cortocircuito de un transformador real|S07-3 Ensayo de vacío y cortocircuito]]

### Tensión relativa de cortocircuito
$$\boxed{\varepsilon_{cc} = \frac{V_{1cc}}{V_{1n}} \cdot 100}$$

### Componentes resistiva y reactiva
$$\varepsilon_{R_{cc}} = \frac{V_{R_{cc}}}{V_{1n}} \cdot 100 \hspace{0.5cm};\hspace{0.5cm} \varepsilon_{X_{cc}} = \frac{V_{X_{cc}}}{V_{1n}} \cdot 100$$

### Corriente de cortocircuito de falta (cortocircuito accidental con $V_{1n}$ aplicada)
$$I_{1falta} = \frac{V_{1n}}{Z_{cc}}$$

Expresión equivalente:
$$\boxed{I_{1falta} = \frac{100}{\varepsilon_{cc}} \cdot I_{1n}}$$

### Valores típicos de $\varepsilon_{cc}$
| Capacidad | $\varepsilon_{cc}$ |
| --------- | ------------------ |
| $< 1000\,\text{kVA}$ (distribución) | 1 % – 6 % |
| $> 1000\,\text{kVA}$ | 6 % – 13 % |

Por lo general $\varepsilon_{X_{cc}} > \varepsilon_{R_{cc}}$ porque $X_{cc} \gg R_{cc}$.

---

## 21. Admitancia de Excitación (Forma Chapman)
Fuente: [[S08-1 Tema 01 - Determinación de los parámetros del transformador|S08-1 Determinacion de los parametros del transformador]]

### Conductancia y susceptancia
$$G_{Fe} = \frac{1}{R_{Fe}} \hspace{0.5cm};\hspace{0.5cm} B_\mu = \frac{1}{X_\mu}$$

### Admitancia de excitación
$$\mathbf{Y}_E = G_{Fe} - jB_\mu = \frac{1}{R_{Fe}} - j\,\frac{1}{X_\mu}$$

### Cálculo desde el ensayo de vacío
$$|\mathbf{Y}_E| = \frac{I_0}{V_0} \hspace{0.5cm};\hspace{0.5cm} \angle\mathbf{Y}_E = -\cos^{-1}\!\left(\frac{P_0}{V_0 \cdot I_0}\right)$$

### Impedancia serie desde el ensayo de cortocircuito
$$|\mathbf{Z}_{serie}| = \frac{V_{cc}}{I_{cc}} \hspace{0.5cm};\hspace{0.5cm} \angle\mathbf{Z}_{serie} = +\cos^{-1}\!\left(\frac{P_{cc}}{V_{cc} \cdot I_{cc}}\right)$$

$$\mathbf{Z}_{serie} = R_{eq} + jX_{eq}$$

### Descomposición aproximada (criterio de Chapman)
$$\mathbf{Z}_{serie} = (R_1 + a^2 R_2) + j(X_1 + a^2 X_2)$$

Con reparto igualitario: $R_1 = a^2 R_2 = R_{eq}/2$, $X_1 = a^2 X_2 = X_{eq}/2$.

---

## 22. Regulación de Voltaje y Eficiencia
Fuente: [[S08-2 Tema 02 - Eficiencia y regulación del transformador real|S08-2 Eficiencia y regulacion del transformador real]]

### Regulación de voltaje (RV)
$$\boxed{RV = \frac{V_P/a - V_S}{V_S} \cdot 100\,\%}$$

Donde:
- $V_P/a$ = tensión que entregaría el secundario si el transformador fuera ideal.
- $V_S$ = tensión real en el secundario a plena carga.

### Ecuación exacta (todo referido al secundario)
$$\frac{\mathbf{V}_P}{a} = \mathbf{V}_S + R_{eq}\,\mathbf{I}_S + jX_{eq}\,\mathbf{I}_S$$

### Eficiencia del transformador
$$\eta = \frac{P_{sal}}{P_{ent}} \cdot 100\,\% = \frac{P_{sal}}{P_{sal} + P_{perdida}} \cdot 100\,\%$$

$$\boxed{\eta = \frac{V_S \, I_S \, \cos\theta}{V_S \, I_S \, \cos\theta + P_{Cu} + P_{nucleo}} \cdot 100\,\%}$$

### Pérdidas
| Tipo | Origen | Se obtiene de |
| ---- | ------ | ------------- |
| $P_{Cu} = I^2 R$ | Resistencias del devanado | Ensayo cortocircuito ($P_{cc}$) |
| $P_{histeresis}$ | Ciclo $B$–$H$ del núcleo | Ensayo vacío ($P_0$) |
| $P_{Foucault}$ | Corrientes parásitas en chapas | Ensayo vacío ($P_0$) |

### Comportamiento de la RV según FP de la carga
| FP | $V_P/a$ vs $V_S$ | Signo de RV |
| -- | ---------------- | ----------- |
| Inductivo (retraso) | $V_P/a \gg V_S$ | Positiva grande |
| Resistivo (FP = 1) | $V_P/a > V_S$ | Positiva moderada |
| Capacitivo (adelanto) | $V_P/a \lessgtr V_S$ | Pequeña o **negativa** |

---

## 23. El Autotransformador
Fuente: [[S08-5 Tema 04 - El autotransformador|S08-5 El autotransformador]]

### Relación de espiras (devanado común y devanado serie)
$$\frac{V_C}{V_{SE}} = \frac{N_C}{N_{SE}} \hspace{0.5cm}\Longrightarrow\hspace{0.5cm} N_C \cdot I_C = N_{SE} \cdot I_{SE}$$

### Voltajes y corrientes terminales
| Lado | Voltaje | Corriente |
| ---- | ------- | --------- |
| Baja (L) | $V_L = V_C$ | $I_L = I_C + I_{SE}$ |
| Alta (H) | $V_H = V_C + V_{SE}$ | $I_H = I_{SE}$ |

Donde:
- $V_C$ = voltaje en el devanado común (aparece en ambos lados)
- $V_{SE}$ = voltaje en el devanado en serie
- $I_C$, $I_{SE}$ = corrientes en los devanados común y en serie

> [!info] Sin aislamiento galvánico
> A diferencia del transformador convencional, el autotransformador tiene **conexión eléctrica directa** entre primario y secundario. Es más compacto y económico, pero **no aísla** los dos lados.

---

## 24. Transformador Trifásico — Conexiones
Fuente: [[S09-1 Tema 01 - El transformador trifásico|S09-1 El transformador trifasico]]

### Potencia aparente trifásica
$$S = \sqrt{3} \cdot V_L \cdot I_L = 3 \cdot V_\phi \cdot I_\phi$$

### Relaciones entre fase y línea
| Conexión | $V_L$ vs $V_\phi$ | $I_L$ vs $I_\phi$ |
| -------- | ----------------- | ----------------- |
| **Y** (estrella) | $V_L = \sqrt{3}\,V_\phi$ | $I_L = I_\phi$ |
| **Δ** (triángulo) | $V_L = V_\phi$ | $I_L = \sqrt{3}\,I_\phi$ |

### Relación de transformación de línea según conexión
| Conexión | $V_{LP}/V_{LS}$ | Desfase |
| -------- | ---------------- | ------- |
| **Y–Y** | $a$ | 0° |
| **Y–Δ** | $\sqrt{3} \cdot a$ | 30° |
| **Δ–Y** | $a/\sqrt{3}$ | 30° |
| **Δ–Δ** | $a$ | 0° |

Donde $a = N_{\phi P}/N_{\phi S}$ es la **relación por fase**.

### Ventajas y desventajas
| Conexión | Ventajas | Desventajas |
| -------- | -------- | ----------- |
| Y–Y | Sencilla, ambos lados con neutro | Problemas con 3.er armónico y cargas desbalanceadas |
| Y–Δ | Robusta frente a armónicos y desbalances | Desfase 30°, sin neutro secundario |
| Δ–Y | Robusta + permite neutro secundario | Desfase 30° |
| Δ–Δ | Sin desfase, robusta | Sin neutro accesible |

---

## 25. Circuito Equivalente Trifásico — Índice Horario
Fuente: [[S09-3 Tema 02 - Circuito equivalente aproximado del transformador trifásico|S09-3 Circuito equivalente aproximado e indice horario]]

### Análisis por fase (mismas fórmulas que el monofásico)
$$a = \frac{N_{\phi P}}{N_{\phi S}} = \frac{E_{\phi P}}{E_{\phi S}}$$

Cada fase es un transformador monofásico equivalente con los parámetros $R_{cc}$, $X_{cc}$, $R_{Fe}$, $X_\mu$ aplicables por fase.

### Reflexión de impedancia externa al primario (por fase)
$$\mathbf{Z}' = m^2 \cdot \mathbf{Z}$$

Con $m = V_{\phi P}/V_{\phi S}$.

### Caída relativa de tensión de cortocircuito (por fase)
$$\varepsilon_{cc} = \frac{Z_{cc} \cdot I_{\phi}}{V_{\phi}} \cdot 100\,\% \hspace{0.5cm};\hspace{0.5cm} \varepsilon_{X_{cc}} = \frac{X_{cc} \cdot I_{\phi}}{V_{\phi}} \cdot 100\,\%$$

Despejando los parámetros:
$$Z_{cc} = \frac{\varepsilon_{cc} \cdot V_{\phi}}{I_{\phi}} \hspace{0.5cm};\hspace{0.5cm} X_{cc} = \frac{\varepsilon_{X_{cc}} \cdot V_{\phi}}{I_{\phi}} \hspace{0.5cm};\hspace{0.5cm} R_{cc} = \sqrt{Z_{cc}^{\,2} - X_{cc}^{\,2}}$$

### Índice horario (grupo de conexión)
**Notación:** `Xy<n>` — primera letra = primario (mayúscula), segunda = secundario (minúscula), $n$ = desfase / 30°.

| Grupo | Símbolo | Desfase |
| ----- | ------- | ------- |
| 0 | Dd0, Yy0 | 0° |
| 5 | Dy5, Yd5 | 150° |
| 6 | Dd6, Yy6 | 180° |
| 11 | Dy11, Yd11 | 330° (= −30°) |

> [!info] Compatibilidad para puesta en paralelo
> Dos transformadores trifásicos en paralelo deben tener **el mismo índice horario** para no producir corrientes circulantes destructivas.

### Procedimiento general para problemas trifásicos
1. Calcular $m$ con voltajes **de fase** y corrientes **de fase**.
2. Pasar $\varepsilon_{cc}$, $\varepsilon_{X_{cc}}$ a Ω.
3. Reflejar impedancias externas (línea, carga) al primario con $m^2$.
4. Resolver el circuito **por una fase** como si fuera monofásico.
5. Convertir las tensiones de fase del primario al lado real del secundario:
   - **Secundario en Y:** $V_L = (V'_\phi / m) \cdot \sqrt{3}$
   - **Secundario en Δ:** $V_L = V'_\phi / m$

---

## 26. Conversión Electromecánica — Fuerza de Lorentz
Fuente: [[S10-1 Tema 01 - Conversión de energía electromecánica|S10-1 Conversion de energia electromecanica]]

Fuerza sobre una carga puntual $q$ en presencia de campos $\mathbf{E}$ y $\mathbf{B}$:

$$\mathbf{F} \;=\; q\,(\mathbf{E} + \mathbf{v} \times \mathbf{B})$$

- $q$ = carga puntual
- $\mathbf{E}$ = campo eléctrico
- $\mathbf{v}$ = velocidad de la partícula
- $\mathbf{B}$ = densidad de campo magnético

El término $q\,(\mathbf{v} \times \mathbf{B})$ es el responsable del **par electromagnético** en motores: integrado sobre los portadores de carga de un conductor con corriente en un campo magnético, da la fuerza neta sobre el conductor.

---

## 27. Energía y Coenergía Magnética
Fuente: [[S10-2 Tema 02 - Función de energía y coenergía|S10-2 Funcion de energia y coenergia]]

### Definiciones (sobre la curva $\lambda$–$i$ a posición $x$ fija)

**Energía magnética almacenada** (área entre la curva y el eje $\lambda$):

$$W_c(\lambda, x) \;=\; \int_{\lambda(0)}^{\lambda(t)} i(\lambda, x)\,d\lambda$$

**Coenergía magnética** — función auxiliar sin sentido físico (área bajo la curva, entre la curva y el eje $i$):

$$W'_c(i, x) \;=\; \int_{i(0)}^{i(t)} \lambda(i, x)\,di$$

### Relación complementaria

$$W_c + W'_c \;=\; \lambda \cdot i$$

### Balance de energía (dispositivo con bobina alimentada por $V, i$)

$$i\,d\lambda \;=\; dW_c \;+\; F_e\,dx$$

Si la pieza móvil se mantiene fija ($dx = 0$): $\;dW_c = i\,d\lambda$.

### Caso lineal (sin saturación) — $\lambda = L(x)\,i$

$$W_c \;=\; W'_c \;=\; \tfrac{1}{2}\,L(x)\,i^{2} \;=\; \tfrac{1}{2}\,\frac{\lambda^{2}}{L(x)}$$

### Fuerza electromagnética (caso general — útil con saturación)

$$F_e \;=\; \left.\frac{\partial W'_c(i, x)}{\partial x}\right|_{i\,\text{cte}} \;=\; -\left.\frac{\partial W_c(\lambda, x)}{\partial x}\right|_{\lambda\,\text{cte}}$$

> [!info] Aplicación
> Estas fórmulas son la base para calcular la **fuerza** en electroimanes/actuadores y el **par** en máquinas rotativas (Unidad 3, semanas 11–14).

---

## 28. Fuerza y Torque de Origen Electromagnético
Fuente: [[S11-1 Tema 01 - Fuerza electromagnética|S11-1 Fuerza electromagnetica]]
Fuente: [[S11-2 Tema 01 - Torques de origen electromagnético|S11-2 Torques de origen electromagnetico]]

### Fuerza electromagnética (componente magnética de Lorentz)
$$\vec{F} = q\,\vec{v} \times \vec{B}$$

### Torque neto sobre una espira rectangular
$$\vec{\tau} = -I\,A\,B\sin\theta\;\hat{i} \hspace{0.5cm}\text{con}\hspace{0.3cm} A = a\,b$$

### Momento dipolar magnético
$$\vec{\mu} = I\,A\,\hat{n} \hspace{0.5cm};\hspace{0.5cm} \vec{\mu} = N\,I\,A\,\hat{n} \quad [\text{A}\cdot\text{m}^2]$$

### Torque en función del momento dipolar
$$\boxed{\vec{\tau} = \vec{\mu} \times \vec{B}} \hspace{0.5cm}\Longrightarrow\hspace{0.5cm} \tau = \mu\,B\sin\theta$$

### Energía potencial del dipolo magnético
$$U = -\vec{\mu}\cdot\vec{B} = -\mu\,B\cos\theta$$

Donde:
- $\mu = I\cdot A$ = momento dipolar magnético (con $A = \pi r^2$ para un bucle circular)
- $\theta$ = ángulo entre $\vec{\mu}$ y $\vec{B}$
- $\tau$ máximo en $\theta = 90°$ (plano de la espira paralelo al campo); $U$ mínima en $\theta = 0°$ (alineación estable)

> [!example] Aplicación numérica
> Bucle circular $r = 2\,\text{cm}$, $I = 2\,\text{mA}$, $B = 0{,}5\,\text{T}$, $\theta = 30°$ → $\mu \approx 2{,}5\times10^{-6}\,\text{A}\cdot\text{m}^2$, $\tau \approx 6{,}3\times10^{-7}\,\text{N}\cdot\text{m}$, $U \approx -1{,}1\times10^{-6}\,\text{J}$. Desarrollo en [[S11-3 Ejercicio resuelto - Torque en un bucle de corriente (Video)|S11-3]].

---

## 29. Velocidad de Sincronismo (Motores AC)
Fuente: [[S11-4 Tema 01 - Aplicaciones del motor eléctrico|S11-4 Aplicaciones del motor electrico]]

### Velocidad de sincronismo
$$n = \frac{60 \cdot f}{P}$$

Donde:
- $n$ = velocidad de sincronismo [rpm]
- $f$ = frecuencia de la red [Hz]
- $P$ = número de **pares de polos** de la máquina

> [!info] Motor asíncrono
> El **motor asíncrono** gira a una velocidad **distinta** a la de sincronismo (existe deslizamiento). Se regula con **variadores de frecuencia**.
