---
title: "Presentación PC2 - Práctica Calificada 2"
curso: "[[Motores MOC]]"
unidad: 2
semana: 9
orden: 101
tipo: evaluacion
subtipo: pc
tags:
  - curso/motores
  - tipo/evaluacion
  - subtipo/pc
  - tema/transformador-real
  - tema/ensayos
  - tema/transformador-trifasico
date: 2026-05-24
---

# Examen — Máquinas Eléctricas II (PC2)

**Estudiante:** Tito Luyo Murata · **Código:** U23210744
**Fecha:** 24 de mayo de 2026

---


1. ¿Cuál de los siguientes materiales magnéticos se utilizaría si se quisiera fabricar un transformador de alta frecuencia?

Rpta.: c) Núcleos de Ferrita

Las ferritas tienen resistividad eléctrica muy alta ($10^{\,5}$–$10^{\,8}\ \Omega\cdot$m), lo que elimina las pérdidas por corrientes de Foucault a alta frecuencia.

2. ¿Cuáles son los ensayos esenciales empleados en la práctica para establecer los parámetros del circuito de un transformador?

Rpta.: a) Ensayo de vacío y ensayo de cortocircuito

El ensayo de vacío entrega los parámetros de la rama de excitación ($R_{Fe}$, $X_\mu$) y el de cortocircuito entrega la impedancia serie equivalente ($R_{eq}$, $X_{eq}$).


3. ¿Cuál es la opción de conexión incorrecta en un banco de un transformador trifásico?

Rpta.: d) Ye – Ye – Ye

Un banco trifásico tiene dos lados (primario y secundario); la notación Y–Y–Y describe tres devanados, propia de un transformador de tres devanados.


4. Se va a probar un transformador de 15 kVA y 2300 V / 230 V para determinar los componentes de la rama de excitación, sus impedancias en serie y su regulación de voltaje. Se obtuvieron los siguientes datos de las pruebas:

| Prueba en vacío | Prueba en cortocircuito (medido en el primario) |
| --------------- | ----------------------------------------------- |
| $V_0 = 230$ V   | $V_{cc} = 47$ V   |
| $I_0 = 2{,}1$ A | $I_{cc} = 6$ A    |
| $P_0 = 50$ W    | $P_{cc} = 160$ W  |

a) Circuito equivalente referido al lado de alto voltaje.
b) Circuito equivalente referido al lado de bajo voltaje.

### Datos previos

$$a = \frac{V_{1n}}{V_{2n}} = \frac{2300}{230} = 10$$

$$I_{1n} = \frac{S_n}{V_{1n}} = \frac{15{,}000}{2300} = 6{,}52\ \text{A} \hspace{1cm} I_{2n} = \frac{S_n}{V_{2n}} = \frac{15{,}000}{230} = 65{,}22\ \text{A}$$

### Ensayo en cortocircuito (en el primario → referido a AT)

$$Z_{eq1} = \frac{V_{cc}}{I_{cc}} = \frac{47}{6} = 7{,}833\ \Omega$$

$$R_{eq1} = \frac{P_{cc}}{I_{cc}^{\,2}} = \frac{160}{36} = 4{,}444\ \Omega$$

$$X_{eq1} = \sqrt{Z_{eq1}^{\,2} - R_{eq1}^{\,2}} = \sqrt{7{,}833^{\,2} - 4{,}444^{\,2}} = 6{,}451\ \Omega$$

### Ensayo en vacío (en el secundario → referido a BT)

$$\cos\varphi_0 = \frac{P_0}{V_0\,I_0} = \frac{50}{230 \times 2{,}1} = 0{,}1035 \hspace{1cm} \sin\varphi_0 = 0{,}9946$$

$$I_{Fe} = I_0\cos\varphi_0 = 2{,}1 \times 0{,}1035 = 0{,}2174\ \text{A} \hspace{1cm} I_\mu = I_0\sin\varphi_0 = 2{,}0887\ \text{A}$$

$$R_{Fe}^{(BT)} = \frac{V_0}{I_{Fe}} = \frac{230}{0{,}2174} = 1058\ \Omega \hspace{1cm} X_\mu^{(BT)} = \frac{V_0}{I_\mu} = \frac{230}{2{,}0887} = 110{,}1\ \Omega$$

### a) Circuito equivalente referido a AT

La impedancia serie ya está en AT; la rama de excitación se refiere de BT a AT multiplicando por $a^{\,2} = 100$:

$$R_{Fe}^{(AT)} = a^{\,2} \cdot R_{Fe}^{(BT)} = 100 \times 1058 = 105{,}8\ \text{k}\Omega$$

$$X_\mu^{(AT)} = a^{\,2} \cdot X_\mu^{(BT)} = 100 \times 110{,}1 = 11{,}01\ \text{k}\Omega$$

| Elemento | Valor |
| -------- | ----- |
| $R_{eq1} = R_1 + R'_2$ | $4{,}444\ \Omega$ |
| $X_{eq1} = X_1 + X'_2$ | $6{,}451\ \Omega$ |
| $R_{Fe}$ | $105{,}8\ \text{k}\Omega$ |
| $X_\mu$  | $11{,}01\ \text{k}\Omega$ |

### b) Circuito equivalente referido a BT

La rama de excitación ya está en BT; la impedancia serie se refiere de AT a BT dividiendo por $a^{\,2} = 100$:

$$R_{eq2} = \frac{R_{eq1}}{a^{\,2}} = \frac{4{,}444}{100} = 0{,}04444\ \Omega \hspace{1cm} X_{eq2} = \frac{X_{eq1}}{a^{\,2}} = \frac{6{,}451}{100} = 0{,}06451\ \Omega$$

| Elemento | Valor |
| -------- | ----- |
| $R_{eq2} = R'_1 + R_2$ | $0{,}04444\ \Omega$ |
| $X_{eq2} = X'_1 + X_2$ | $0{,}06451\ \Omega$ |
| $R_{Fe}$ | $1058\ \Omega$ |
| $X_\mu$  | $110{,}1\ \Omega$ |
