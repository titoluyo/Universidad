---
title: "Aplicaciones lineales del amplificador operacional"
curso: "[[Amplificadores MOC]]"
unidad: 1
semana: 4
orden: 1
tipo: clase
tags:
  - curso/amplificadores
  - tipo/clase
  - tema/amplificador-operacional
  - tema/aplicaciones-lineales
  - tema/inversor
  - tema/no-inversor
  - tema/sumador
  - tema/integrador
  - tema/derivador
date: 2026-04-07
---

## Op-amp ideal: suposiciones

En todas las configuraciones se asume el amplificador operacional **ideal**:

- Ganancia de lazo abierto $A \to \infty$
- Impedancia de entrada $Z_{in} \to \infty$ → no entra corriente por las entradas
- Impedancia de salida $Z_{out} = 0$

Consecuencias:
- $V^+ = V^-$ (cortocircuito virtual)
- $I^+ = I^- = 0$

---

## 1. Amplificador inversor

La entrada se aplica por $V^-$ a traves de $R_1$, con realimentacion por $R_f$.

$$\boxed{A_v = \frac{V_o}{V_i} = -\frac{R_f}{R_1}}$$

- Invierte la fase (signo negativo)
- Impedancia de entrada: $Z_{in} = R_1$ (relativamente baja)

---

## 2. Amplificador no inversor

La entrada se aplica por $V^+$, con $R_1$ y $R_f$ en la realimentacion.

$$\boxed{A_v = \frac{V_o}{V_i} = 1 + \frac{R_f}{R_1}}$$

- No invierte la fase
- Impedancia de entrada: $Z_{in} \to \infty$ (la entrada va directo a $V^+$)
- Ganancia minima = 1 (cuando $R_f = 0$ o $R_1 \to \infty$)

---

## 3. Seguidor de voltaje (buffer)

Caso especial del no inversor con $R_f = 0$ y $R_1 \to \infty$ (realimentacion unitaria directa).

$$\boxed{A_v = 1 \implies V_o = V_i}$$

- **Adaptador de impedancia**: entrada muy alta, salida muy baja
- Conecta una fuente de alta impedancia a una carga de baja impedancia sin perder senal

---

## 4. Sumador inversor

Multiples entradas a traves de resistencias individuales hacia $V^-$.

$$\boxed{V_o = -R_f\left(\frac{V_1}{R_1} + \frac{V_2}{R_2} + \frac{V_3}{R_3} + \cdots\right)}$$

Si $R_1 = R_2 = R_3 = R$:

$$V_o = -\frac{R_f}{R}(V_1 + V_2 + V_3)$$

- Usado en mezcladoras de audio, conversores DAC

---

## 5. Restador (diferencial)

Combina las configuraciones inversora y no inversora.

$$\boxed{V_o = \frac{R_f}{R_1}(V_2 - V_1)} \quad \text{(si } R_1 = R_2 \text{ y } R_f = R_3\text{)}$$

Caso general con 4 resistencias:

$$V_o = -\frac{R_f}{R_1}V_1 + \frac{R_f}{R_2}\left(1 + \frac{R_1}{R_f}\right)\frac{R_4}{R_3 + R_4}V_2$$

- Cuando $R_1 = R_2$ y $R_3 = R_4 = R_f$: resta pura
- Base de los amplificadores de instrumentacion

---

## 6. Integrador

Reemplaza $R_f$ por un condensador $C$.

$$\boxed{V_o = -\frac{1}{R_1 C}\int_0^t V_i \, dt}$$

- Entrada constante → salida **rampa**
- Onda cuadrada → **onda triangular**
- Usado en generadores de formas de onda, filtros y controladores PID

---

## 7. Derivador

Reemplaza $R_1$ por un condensador $C$.

$$\boxed{V_o = -R_f C \frac{dV_i}{dt}}$$

- Responde a la **velocidad de cambio** de la entrada
- Rampa → salida **constante**
- Onda triangular → **onda cuadrada**

> [!warning] Sensibilidad al ruido
> El derivador amplifica el ruido de alta frecuencia. En la practica se agrega una resistencia en serie con $C$ para limitar la ganancia a frecuencias altas.

---

## 8. Convertidor corriente a voltaje (transimpedancia)

$$\boxed{V_o = -I_{in} \cdot R_f}$$

- La corriente de entrada fluye por $R_f$ directamente
- Usado con fotodiodos y sensores que generan corriente

---

## 9. Fuente de corriente controlada por voltaje

$$\boxed{I_L = \frac{V_i}{R}}$$

- La corriente en la carga es independiente de $R_L$
- Util para excitar cargas que requieren corriente constante (LEDs, sensores)

---

## Resumen

| Aplicacion | Formula clave | Uso tipico |
| ---------- | ------------- | ---------- |
| Inversor | $-R_f / R_1$ | Amplificacion con inversion |
| No inversor | $1 + R_f / R_1$ | Amplificacion sin inversion |
| Seguidor | $A_v = 1$ | Adaptador de impedancia |
| Sumador | $-R_f \sum V_i/R_i$ | Mezcla de senales, DAC |
| Restador | $\frac{R_f}{R_1}(V_2 - V_1)$ | Medicion diferencial |
| Integrador | $-\frac{1}{RC}\int V_i\,dt$ | Formas de onda, filtros, PID |
| Derivador | $-RC \cdot dV_i/dt$ | Deteccion de cambios |
| I→V | $-I_{in} \cdot R_f$ | Sensores de corriente |

## Bibliografia

- Boylestad, R. & Nashelsky, L. *Electronica: Teoria de Circuitos y Dispositivos Electronicos*. Pearson.
- Gonzalez de la Rosa, J. J. *Circuitos electronicos aplicados con amplificadores operacionales*. Universidad de Cadiz.
