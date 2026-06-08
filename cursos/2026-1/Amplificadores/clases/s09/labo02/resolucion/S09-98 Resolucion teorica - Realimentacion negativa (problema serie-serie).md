---
title: "Resolución teórica - Realimentación negativa (teoría + problema serie-serie)"
curso: "[[Amplificadores MOC]]"
unidad: 3
semana: 9
orden: 98
tipo: ejercicio
tags:
  - curso/amplificadores
  - tipo/ejercicio
  - tema/realimentacion-negativa
  - tema/realimentacion-serie-serie
  - tema/transconductancia
  - tema/cuadripolos
  - tema/parametros-z
date: 2026-05-19
---

> [!warning] Importante: estas capturas NO resuelven el circuito de la guía LE2
> El laboratorio [[S09-99 Laboratorio - LE2 Realimentacion negativa|LE2]] es un **amplificador de transresistencia (shunt-shunt)** con un solo BJT 2N2222 ($+12\,\text{V}$, $R_C=1\,\text{k}$, $R_E=100\,\Omega$, $R_3=R_4=5.6\,\text{k}$, entrada en **corriente** $I_g$).
>
> El problema resuelto en estas fotos es **otro circuito distinto**: un **amplificador de transconductancia (serie-serie)** formado por **OPAMP + BJT** ($+18\,\text{V}$, $R_s=50\,\Omega$, $R_1=1.1\,\text{k}$, $R_f=2.2\,\text{k}$, $R_C=6.8\,\text{k}$, $R_E=3.3\,\text{k}$, $\beta=200$, entrada en **tensión** $V_s$).
>
> Es decir, estas hojas son **apuntes de teoría de realimentación + un problema-tipo resuelto** (probablemente un ejemplo de clase o de práctica). Sirven como base conceptual para el informe del LE2, pero **el procedimiento numérico no se aplica tal cual** al circuito de la guía. Lo conservo y reviso igual porque la metodología es la misma.

Capturas originales: ![[WhatsApp Image 2026-05-19 at 11.05.30 PM.jpeg]] ![[WhatsApp Image 2026-05-19 at 11.05.44 PM.jpeg]] ![[WhatsApp Image 2026-05-19 at 11.06.21 PM.jpeg]] ![[WhatsApp Image 2026-05-19 at 11.07.24 PM.jpeg]]

---

## Parte 1 — Teoría de la realimentación negativa

### Ventajas y desventajas

| Ventajas | Desventajas |
| -------- | ----------- |
| ↓ Sensibilidad a variaciones de los parámetros | ↓ Ganancia |
| ↓ Distorsión no lineal | Peligro de inestabilidad (oscilaciones no deseadas) |
| ↑ BW (ancho de banda) | |
| Ajuste de impedancias ($Z_e$ y $Z_o$) | |
| ↓ Ruido | |

> [!note]
> Sin realimentación se "pierde" estabilidad y aparecen ruido y distorsión; al cerrar el lazo, $V_o$ alimenta osciladores y comparadores en histéresis cuando la realimentación es **positiva** (contraste con [[S09-1 Amplificadores con realimentacion positiva y osciladores]]).

### Diagrama de bloques

```
Fuente externa ─Ws─►(Σ)─Wi─►[ Amplificador sin realimentar (A) ]─Wo─►[ Carga externa ]
                     ▲                                              │
                     └──────Wf──[ Circuito de realimentación  β ]◄──┘
```

- $\beta \to$ **factor de realimentación**.

### Ganancias

$$A_f = \frac{A}{1 + A\beta}$$

- **Ganancia de lazo abierto:** $A = A_{OL} = \dfrac{W_o}{W_i}$
- **Ganancia de lazo cerrado:** $A_f = A_{CL} = \dfrac{W_o}{W_s}$
- **Ganancia de realimentación:** $\beta = \dfrac{W_f}{W_o}$
- **Ganancia de lazo:** $L = A\beta$
- **Factor de mérito / mejora:** $F = 1 + A\beta$

### Mezcla y muestreo

- **Mezcla** (entrada): `I → paralelo (shunt)`, `V → serie`.
- **Muestreo** (salida): `I → serie`, `V → paralelo (shunt)`.

### Las 4 topologías

| Topología | Mezcla–Muestreo | Amplificador | Magnitud estabilizada |
| --------- | --------------- | ------------ | --------------------- |
| **Serie–paralelo** | Tensión–Tensión | Tensión $A_v = V_o/V_i$ | $A_{vf}=V_o/V_i$ |
| **Paralelo–serie** | Corriente–Corriente | Corriente $A_i = I_o/I_i$ | $A_{if}=I_o/I_i$ |
| **Paralelo–paralelo** | Corriente–Tensión | Transresistencia $A_z = V_o/I_i$ | $A_{zf}=V_o/I_i$ |
| **Serie–serie** | Tensión–Corriente | Transconductancia $A_y = I_o/V_i$ | $A_{yf}=I_o/V_i$ |

### Efecto sobre las impedancias

| Mezcla/Muestreo | Impedancia de **salida** $R_{of}$ | Impedancia de **entrada** $R_{if}$ |
| --------------- | --------------------------------- | ---------------------------------- |
| **Serie** | $R_{of} = R_o(1 + A\beta)$ | $R_{if} = R_i(1 + A\beta)$ |
| **Paralelo** | $R_{of} = \dfrac{R_o}{1 + A\beta}$ | $R_{if} = \dfrac{R_i}{1 + A\beta}$ |

> Regla mnemónica: **serie ⇒ ×(1+Aβ)** (sube la impedancia), **paralelo ⇒ ÷(1+Aβ)** (baja la impedancia). Aplica por separado al lado de entrada (mezcla) y al de salida (muestreo).

### Parámetros de cuadripolo para la red de realimentación

Se representa $A$ y $\beta$ con 4 variables y 2 ecuaciones. Cada juego de parámetros "privilegia" una topología:

| Parámetros | Ecuaciones | $R_{11}$ | $R_{22}$ | $\beta$ | Privilegia |
| ---------- | ---------- | -------- | -------- | ------- | ---------- |
| **H** | $V_1=h_{11}I_1+h_{12}V_2$; $I_2=h_{21}I_1+h_{22}V_2$ | $h_{11}=\frac{V_1}{I_1}\big|_{V_2=0}$ | $\frac{1}{h_{22}}=\frac{V_2}{I_2}\big|_{I_1=0}$ | $h_{12}=\frac{V_1}{V_2}\big|_{I_1=0}$ | $A_v$ (serie–paralelo) |
| **G** | $I_1=g_{11}V_1+g_{12}I_2$; $V_2=g_{21}V_1+g_{22}I_2$ | $\frac{1}{g_{11}}=\frac{V_1}{I_1}\big|_{I_2=0}$ | $g_{22}=\frac{V_2}{I_2}\big|_{V_1=0}$ | $g_{12}=\frac{I_1}{I_2}\big|_{V_1=0}$ | $A_i$ (paralelo–serie) |
| **Y** | $I_1=y_{11}V_1+y_{12}V_2$; $I_2=y_{21}V_1+y_{22}V_2$ | $\frac{1}{y_{11}}=\frac{V_1}{I_1}\big|_{V_2=0}$ | $\frac{1}{y_{22}}=\frac{V_2}{I_2}\big|_{V_1=0}$ | $y_{12}=\frac{I_1}{V_2}\big|_{V_1=0}$ | $A_z$ (paralelo–paralelo) |
| **Z** | $V_1=z_{11}I_1+z_{12}I_2$; $V_2=z_{21}I_1+z_{22}I_2$ | $z_{11}=\frac{V_1}{I_1}\big|_{I_2=0}$ | $z_{22}=\frac{V_2}{I_2}\big|_{I_1=0}$ | $z_{12}=\frac{V_1}{I_2}\big|_{I_1=0}$ | $A_y$ (serie–serie) |

---

## Parte 2 — Problema resuelto (amplificador de transconductancia, serie–serie)

### Enunciado

En el amplificador se pide:

1. Identificar $A$ y $\beta$, el tipo de amplificador y la topología.
2. Dibujar el circuito equivalente en pequeña señal a frecuencias medias.
3. Reconocer por qué existe realimentación negativa.
4. Reconocer los parámetros privilegiados, $V_1$, $V_2$ y el valor de $\beta$.
5. Circuito equivalente de la red $A'$ y valor de $A'$.
6. Calcular $A_f$, $Z_{if}$, $Z_{of}$ y la ganancia $V_o/V_s$.

### Datos

- $V_{BE}=0.7\,\text{V}$, $I_{CQ}=1.8\,\text{mA}$, $\beta=200$, $V_T=25\,\text{mV}$, $r_o\to\infty$
- **OPAMP:** $A_v=2\times10^{5}\,\text{V/V}$, $R_i=1\,\text{M}\Omega$ *(ver nota)*, $R_o=130\,\Omega$
- $R_s=50\,\Omega$, $R_1=1.1\,\text{k}\Omega$, $R_f=2.2\,\text{k}\Omega$, $R_C=6.8\,\text{k}\Omega$, $R_E=3.3\,\text{k}\Omega$
- Alimentación $+18\,\text{V}$.

> [!note] Duda de lectura
> El valor de $R_i$ del OPAMP en la foto no es legible con certeza (parece $1\,\text{M}\Omega$). Lo asumo $1\,\text{M}\Omega$; afecta sobre todo a $Z_{if}$. **A confirmar con el original.**

### Circuito y topología

OPAMP en configuración no inversora cuya salida ataca la base de $Q_1$; la corriente de salida $I_o$ (colector) se sensa en el emisor a través de $R_E$ y se realimenta por $R_f$ al nudo inversor (con $R_1$ a tierra).

- **Tipo:** amplificador de **transconductancia** → $A_y = \dfrac{I_o}{V_s}$
- **Topología:** **Serie–Serie (S–S)** = mezcla en tensión, muestreo en corriente.
- Parámetros privilegiados: **Z** (se modela la red $\beta$ con parámetros $z$).

### Red de realimentación — parámetros $z$ (lo desarrollado en la foto)

$$z_{11}=R_{11}=\frac{V_1}{I_1}\bigg|_{I_2=0}=R_1\parallel(R_f+R_E)=1.1\text{k}\parallel(2.2\text{k}+3.3\text{k})$$
$$\boxed{R_{11}=1.1\text{k}\parallel5.5\text{k}=0.92\,\text{k}\Omega}$$

$$z_{22}=R_{22}=\frac{V_2}{I_2}\bigg|_{I_1=0}=R_E\parallel(R_1+R_f)=3.3\text{k}\parallel(1.1\text{k}+2.2\text{k})$$
$$\boxed{R_{22}=3.3\text{k}\parallel3.3\text{k}=1.65\,\text{k}\Omega}$$

$$\beta=z_{12}=\frac{V_1}{I_2}\bigg|_{I_1=0}=\frac{R_E\,R_1}{R_1+R_f+R_E}=\frac{3.3\text{k}\cdot1.1\text{k}}{1.1\text{k}+2.2\text{k}+3.3\text{k}}$$
$$\boxed{\beta=0.55\,\text{k}\Omega\ \ [\text{V/A}]}$$

---

## Parte 3 — Revisión de la solución

### ✅ Lo que está correcto

| Resultado | En la foto | Verificación | Estado |
| --------- | ---------- | ------------ | ------ |
| Tipo / topología | Transconductancia, S–S, $A_y=I_o/V_s$ | El $R_f$ sensa corriente de emisor y la devuelve en serie al nudo inversor → serie–serie ✔ | ✔ |
| Parámetros privilegiados | Z | Serie–serie ⇒ parámetros $z$ ✔ | ✔ |
| $z_{11}=R_{11}$ | $0.92\,\text{k}\Omega$ | $1.1\parallel5.5=\frac{1.1\cdot5.5}{6.6}=0.917\,\text{k}$ ✔ | ✔ |
| $z_{22}=R_{22}$ | $1.65\,\text{k}\Omega$ | $3.3\parallel3.3=1.65\,\text{k}$ ✔ | ✔ |
| $\beta=z_{12}$ | $0.55\,\text{k}\Omega$ | $\frac{3.3\cdot1.1}{6.6}=0.55\,\text{k}$ ✔ | ✔ |

**Toda la caracterización de la red de realimentación es correcta.**

### ⚠️ Lo que falta (la solución está incompleta)

El enunciado pide $A_f$, $Z_{if}$, $Z_{of}$ y $V_o/V_s$, pero las fotos **terminan en el cálculo de la red $\beta$**. Faltan el amplificador básico $A$, la ganancia de lazo $A\beta$ y los resultados finales. Los completo abajo.

### Completando la solución

**Parámetros de pequeña señal del BJT:**
$$g_m=\frac{I_{CQ}}{V_T}=\frac{1.8\,\text{mA}}{25\,\text{mV}}=72\,\text{mS}\qquad r_\pi=\frac{\beta}{g_m}=\frac{200}{0.072}=2.78\,\text{k}\Omega$$

**Amplificador básico $A=I_o/V_i$** (con la carga de la red: $z_{11}$ en la entrada, $z_{22}$ en el emisor; $V_{id}\approx V_i$ porque $R_i\gg R_s+z_{11}$):
$$i_b=\frac{A_v\,V_i}{R_o+r_\pi+(\beta+1)z_{22}}=\frac{2\times10^5\,V_i}{130+2780+201\cdot1650}$$
$$A=\frac{I_o}{V_i}=\frac{\beta\,i_b}{V_i}=\frac{200\cdot2\times10^5}{334\,560}\approx1.20\times10^{2}\ \text{S}$$

**Ganancia de lazo y factor de mérito:**
$$A\beta=119.6\times550\approx6.6\times10^{4}\gg1\qquad F=1+A\beta\approx6.6\times10^{4}$$

**Transconductancia de lazo cerrado:**
$$A_f=A_{yf}=\frac{I_o}{V_s}=\frac{A}{1+A\beta}\approx\frac{1}{\beta}=\frac{1}{0.55\,\text{k}\Omega}\approx1.82\,\text{mA/V}$$

(Como $A\beta\gg1$, la transconductancia queda fijada por la red de realimentación, $A_f\approx1/\beta$ — el sello de la realimentación negativa fuerte.)

**Ganancia de tensión total:**
$$\frac{V_o}{V_s}=-A_f\,R_C=-1.82\,\text{mA/V}\times6.8\,\text{k}\Omega\approx-12.4\ \text{V/V}$$

**Impedancias (ambas en *serie* ⇒ se multiplican por $F$):**
$$Z_{if}=Z_i(1+A\beta)\ \to\ \text{muy grande (dominada por }R_i\text{; }\to\infty\text{ ideal})$$
$$Z_{of}=Z_o(1+A\beta)\ \to\ \infty\quad(\text{ya que }r_o\to\infty\Rightarrow\text{fuente de corriente casi ideal})$$

> [!check] Conclusión de la revisión
> Lo escrito (topología + red de realimentación $z_{11}, z_{22}, \beta$) está **bien calculado**. Falta cerrar el problema: $A\approx120\,\text{S}$, $A\beta\approx6.6\times10^4$, $A_f\approx1/\beta\approx1.82\,\text{mS}$, $V_o/V_s\approx-12.4$, y $Z_{if}, Z_{of}$ muy grandes (mezcla y muestreo en serie). Conviene confirmar el valor de $R_i$ del OPAMP en el original para afinar $Z_{if}$.

---

## Cómo aplicar esto al laboratorio LE2 (que sí es shunt–shunt)

El **método** es idéntico, pero cambian dos cosas clave por ser el LE2 de tipo **paralelo–paralelo (transresistencia)**:

1. Se usan parámetros **Y** (no Z): $\;y_{11}=\frac1{R_1}+\frac1{R_f}$, etc., con $R_f=R_3+R_4=11.2\,\text{k}\Omega$.
2. Las impedancias van **divididas** por $(1+A\beta)$ (mezcla y muestreo en **paralelo**): $Z_{if}=\dfrac{Z_i}{1+A\beta}$, $Z_{of}=\dfrac{Z_o}{1+A\beta}$ → **bajan** (al revés que aquí).
3. La magnitud estabilizada es la **transresistencia** $R_{mf}=V_o/I_g\approx 1/\beta=-R_f$, coherente con lo anotado en [[S09-99 Laboratorio - LE2 Realimentacion negativa|la guía LE2]].

---

## Bibliografía

- Sedra, A. & Smith, K. *Microelectronic Circuits*, cap. *Feedback* (método de las 4 topologías y carga por parámetros de cuadripolo).
- Boylestad, R. & Nashelsky, L. *Electrónica: Teoría de Circuitos y Dispositivos Electrónicos*. Pearson.
