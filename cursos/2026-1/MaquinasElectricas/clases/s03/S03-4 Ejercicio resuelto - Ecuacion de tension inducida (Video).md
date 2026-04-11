---
title: Ejercicio resuelto - Ecuacion de tension inducida (Video)
curso: "[[Motores MOC]]"
unidad: 1
semana: 3
orden: 4
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/fem-inducida
  - tema/transformador
date: 2026-04-11
---

> [!info] Fuente
> Video: [Semana 3 - Ejercicio de ecuación de tensión inducida](https://www.youtube.com/watch?v=m9mTGSs-VNk) — Aprendizaje Virtual UTP (5:36)

## Enunciado

Se tiene un **transformador monofásico** constituido por dos devanados (primario y secundario) colocados en un núcleo magnético de sección uniforme de 10 $\text{cm}^2$, como indica la figura. Los devanados primario y secundario tienen 400 y 639 espiras respectivamente. El primario se conecta a una red de 127 V a 60 Hz. En el supuesto de despreciar la caída de tensión del primario, se nos pide calcular:

1. La densidad del flujo máximo existente en el núcleo
2. La fuerza electromotriz inducida en el secundario

![[video4-datos-figura.png]]
**Figura 1.** Transformador monofásico con datos del problema

### Datos

- $N_1 = 400$ espiras (primario)
- $N_2 = 639$ espiras (secundario)
- $S = 10 \, \text{cm}^2 = 10 \times 10^{-4} \, \text{m}^2$
- $V_1 = 127 \, \text{V}$
- $f = 60 \, \text{Hz}$
- Caída de tensión en el primario despreciable

---

## Resolución

### Parte 1: Densidad de flujo máximo en el núcleo

Al despreciar la caída de tensión en el devanado primario:

$$V_1 \approx E_1$$

De acuerdo con la [[S03-3 Tema 03 - Ecuacion de tension inducida#Caso 1 Inducido fijo. Flujo variable.|ecuación de tensión inducida]] aplicada al primario:

$$E_1 = 4{,}44 \cdot N_1 \cdot f_1 \cdot \phi_m$$

Como $V_1 = E_1$:

$$V_1 = 4{,}44 \cdot N_1 \cdot f_1 \cdot \phi_m$$

![[video4-calculo-flujo.png]]
**Figura 2.** Cálculo del flujo máximo

Despejando el flujo máximo:

$$\phi_m = \frac{V_1}{4{,}44 \cdot N_1 \cdot f_1} = \frac{127}{4{,}44 \times 400 \times 60} = 1{,}19 \times 10^{-3} \, \text{Wb}$$

Teniendo en cuenta que $\phi_m = B_m \cdot S$:

$$B_m = \frac{\phi_m}{S} = \frac{1{,}19 \times 10^{-3}}{10 \times 10^{-4}}$$

$$\boxed{B_m = 1{,}19 \, \text{T}}$$

### Parte 2: Fuerza electromotriz inducida en el secundario

Aplicando la misma ecuación en el secundario:

$$E_2 = 4{,}44 \cdot N_2 \cdot f \cdot \phi_m$$

![[video4-resultado-e2.png]]
**Figura 3.** Cálculo completo con resultados

$$E_2 = 4{,}44 \times 639 \times 60 \times 1{,}19 \times 10^{-3}$$

$$\boxed{E_2 = 202{,}69 \, \text{V}}$$

---

## Resultados

| Magnitud | Valor |
| :--- | :---: |
| Flujo máximo $\phi_m$ | $1{,}19 \times 10^{-3}$ Wb |
| Densidad de flujo máximo $B_m$ | $1{,}19$ T |
| FEM inducida en secundario $E_2$ | $202{,}69$ V |

> [!tip] Principio del transformador
> Al aplicar la [[S03-1 Tema 01 - Circuitos magneticos excitados con corriente alterna#Circuito magnético alimentado con corriente alterna|ecuación $V = 4{,}44 \cdot f \cdot N \cdot \phi_m$]] en un núcleo con dos bobinas, tenemos el principio de funcionamiento del **transformador**.
