---
title: Ejercicio resuelto - Circuito ferromagnetico (Video)
curso: "[[Motores MOC]]"
unidad: 1
semana: 2
orden: 2
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/circuito-magnetico
  - tema/corriente-continua
  - tema/curva-imanacion
date: 2026-04-11
---

> [!info] Fuente
> Video: [Semana 2 - Resolución de ejercicio de circuitos ferromagnéticos](https://www.youtube.com/watch?v=OulhnFBPBcQ) — Aprendizaje Virtual UTP (4:56)

## Enunciado

En el núcleo de material magnético de la figura se desea establecer un flujo $\phi = 0{,}1 \times 10^{-3}$ Wb. Se nos pide calcular la corriente $I$ que debe circular por la bobina.

![[video-ej-formula-B.png]]
**Figura 1.** Núcleo de material magnético del problema 1

### Datos

- Longitud promedio: $l = 0{,}25$ m
- $N = 500$ vueltas
- $A = 0{,}2 \times 10^{-3} \, \text{m}^2$
- $\phi = 0{,}1 \times 10^{-3} \, \text{Wb}$
- Material: hierro fundido (curva $B = f(H)$ dada)

---

## Resolución

### Paso 1: Calcular la densidad de flujo magnético $B$

Aplicamos la fórmula:

$$B = \frac{\phi}{A}$$

Reemplazando los datos:

$$B = \frac{0{,}1 \times 10^{-3} \, \text{Wb}}{0{,}2 \times 10^{-3} \, \text{m}^2} = 0{,}5 \, \text{T}$$

### Paso 2: Obtener $H$ de la curva de imanación

Con $B = 0{,}5$ T, entramos a la gráfica de densidad de flujo magnético vs intensidad de campo magnético para hierro fundido.

![[video-ej-grafica-BH.png]]
**Figura 2.** Curva $B = f(H)$ — Hierro fundido

De la gráfica, para $B = 0{,}5$ T se obtiene:

$$H \approx 1550 \, \text{A} \cdot \text{v/m}$$

> [!warning] Recordar
> La longitud debe estar expresada en **metros**.

### Paso 3: Aplicar la [[S01-1 Tema 01 - Como se produce un campo magnético|Ley de Ampère]]

Tomando en cuenta que solo hay una bobina y una sección de núcleo con un ancho de 0,25 m:

$$N \cdot I = H \cdot l$$

Reemplazando:

$$N \cdot I = 1550 \times 0{,}25 = 387{,}5 \, \text{A} \cdot \text{v}$$

![[video-ej-resultado.png]]
**Figura 3.** Cálculo final de la corriente

### Paso 4: Calcular la corriente $I$

$$I = \frac{N \cdot I}{N} = \frac{387{,}5}{500} = 0{,}78 \, \text{A}$$

---

## Resultado

$$\boxed{I = 0{,}78 \, \text{A}}$$

La corriente que debe circular por la bobina de 500 vueltas para establecer un flujo de $0{,}1 \times 10^{-3}$ Wb en el núcleo de hierro fundido es de **0,78 amperios**.
