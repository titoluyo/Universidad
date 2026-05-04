---
title: Ejercicio resuelto - Perdidas en el hierro y exponente de Steinmetz
curso: "[[Motores MOC]]"
unidad: 1
semana: 5
orden: 2
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/perdidas-nucleo
  - tema/perdidas-histeresis
  - tema/corrientes-foucault
  - tema/exponente-steinmetz
date: 2026-04-26
---

> [!info] Fuente
> Video y guion del aula virtual UTP (Semana 5 — Ejercicio de pérdida de campo magnético en el núcleo).

## Enunciado

Un material ferromagnético se ha sometido a tres ensayos con diferentes frecuencias e inducciones, dando lugar a las pérdidas totales en el hierro mostradas en la siguiente tabla:

| Ensayo | $f$ [Hz] | $B_m$ [T] | $P_{Fe}$ [W/kg] |
| ------ | -------- | --------- | --------------- |
| 1      | 50       | 1,0       | 2               |
| 2      | 50       | 1,5       | 4               |
| 3      | 100      | 1,0       | 5               |

**Se pide:**
1. Pérdidas por histéresis ($P_H$) y por corrientes de Foucault ($P_F$) en cada ensayo.
2. Valor del exponente de Steinmetz ($\alpha$).

## Marco teórico

De [[S05-1 Tema 01 - Perdidas magneticas en el nucleo|S05-1 Pérdidas magnéticas en el núcleo]], las pérdidas totales en el hierro son la suma de las pérdidas por histéresis y por corrientes de Foucault:

$$P_{Fe} = P_H + P_F$$

$$P_H = k_1 \cdot f \cdot B_m^{\alpha}$$

$$P_F = k_2 \cdot f^2 \cdot B_m^2$$

Donde $k_1$, $k_2$ son constantes del material y $\alpha$ es el exponente de Steinmetz.

## Desarrollo

### Paso 1 — Plantear el sistema (ecuaciones "a")

Aplicando $P_{Fe} = P_H + P_F$ a cada ensayo:

$$
\begin{cases}
P_{H1} + P_{F1} = 2 \\
P_{H2} + P_{F2} = 4 \\
P_{H3} + P_{F3} = 5
\end{cases} \tag{a}
$$

### Paso 2 — Plantear las relaciones entre ensayos (ecuaciones "b")

Como $k_1$ y $k_2$ son constantes del material, los cocientes entre ensayos eliminan estas constantes y dejan solo las razones de $f$ y $B_m$.

**Comparando ensayos 1 y 2** (misma frecuencia, distinta inducción):

$$\frac{P_{H1}}{P_{H2}} = \left(\frac{1}{1{,}5}\right)^{\alpha}$$

$$\frac{P_{F1}}{P_{F2}} = \left(\frac{1}{1{,}5}\right)^{2}$$

**Comparando ensayos 1 y 3** (misma inducción, distinta frecuencia):

$$\frac{P_{H1}}{P_{H3}} = \frac{50}{100} = \frac{1}{2}$$

$$\frac{P_{F1}}{P_{F3}} = \left(\frac{50}{100}\right)^2 = \frac{1}{4}$$

A este conjunto lo llamaremos ecuaciones (b).

### Paso 3 — Resolver $P_{H1}$ y $P_{F1}$

De las relaciones (b) entre los ensayos 1 y 3:

$$P_{H3} = 2 \cdot P_{H1} \qquad P_{F3} = 4 \cdot P_{F1}$$

Sustituyendo en la primera y tercera ecuación de (a):

$$
\begin{cases}
P_{H1} + P_{F1} = 2 \\
2 P_{H1} + 4 P_{F1} = 5
\end{cases}
$$

Multiplicando la primera por 2 y restándola de la segunda:

$$2 P_{F1} = 1 \;\Rightarrow\; \boxed{P_{F1} = 0{,}5 \;\text{W/kg}}$$

$$P_{H1} = 2 - 0{,}5 \;\Rightarrow\; \boxed{P_{H1} = 1{,}5 \;\text{W/kg}}$$

### Paso 4 — Calcular $P_{H3}$ y $P_{F3}$

$$\boxed{P_{H3} = 2 \cdot 1{,}5 = 3 \;\text{W/kg}}$$

$$\boxed{P_{F3} = 4 \cdot 0{,}5 = 2 \;\text{W/kg}}$$

### Paso 5 — Calcular $P_{H2}$ y $P_{F2}$

De las relaciones (b) entre los ensayos 1 y 2:

$$P_{F2} = 1{,}5^2 \cdot P_{F1} = 2{,}25 \cdot 0{,}5$$

$$\boxed{P_{F2} = 1{,}125 \;\text{W/kg}}$$

De la segunda ecuación de (a):

$$P_{H2} = 4 - P_{F2} = 4 - 1{,}125$$

$$\boxed{P_{H2} = 2{,}875 \;\text{W/kg}}$$

### Paso 6 — Calcular el exponente de Steinmetz $\alpha$

Aplicando la primera relación de (b) con los valores ya conocidos:

$$\frac{P_{H1}}{P_{H2}} = \frac{1{,}5}{2{,}875} = \left(\frac{1}{1{,}5}\right)^{\alpha}$$

Tomando logaritmos:

$$\alpha = \frac{\ln(P_{H2}/P_{H1})}{\ln(1{,}5)} = \frac{\ln(2{,}875/1{,}5)}{\ln(1{,}5)} = \frac{\ln(1{,}9167)}{\ln(1{,}5)}$$

$$\alpha \approx \frac{0{,}6506}{0{,}4055} \approx 1{,}605$$

$$\boxed{\alpha \approx 1{,}6}$$

## Resumen de resultados

| Ensayo | $f$ [Hz] | $B_m$ [T] | $P_H$ [W/kg] | $P_F$ [W/kg] | $P_{Fe}$ [W/kg] |
| ------ | -------- | --------- | ------------ | ------------ | --------------- |
| 1      | 50       | 1,0       | **1,500**    | **0,500**    | 2               |
| 2      | 50       | 1,5       | **2,875**    | **1,125**    | 4               |
| 3      | 100      | 1,0       | **3,000**    | **2,000**    | 5               |

**Exponente de Steinmetz:** $\alpha \approx 1{,}6$

> [!note] Verificación
> El valor $\alpha \approx 1{,}6$ es coincidente con el valor frecuente para acero al silicio mencionado en la teoría ($\alpha$ entre 1,5 y 2,5).

## Bibliografía

- Fraile Mora, J. (2008). *Máquinas Eléctricas* (6ta. ed.). McGraw-Hill Interamericana.
