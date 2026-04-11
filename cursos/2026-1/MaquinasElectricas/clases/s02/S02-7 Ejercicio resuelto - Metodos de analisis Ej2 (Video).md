---
title: Ejercicio resuelto - Metodos de analisis Ej2 (Video)
curso: "[[Motores MOC]]"
unidad: 1
semana: 2
orden: 7
tipo: ejercicio
tags:
  - curso/motores
  - tipo/ejercicio
  - tema/circuito-magnetico
  - tema/metodo-ensayo-error
  - tema/metodo-grafico
  - tema/dos-materiales
date: 2026-04-11
---

> [!info] Fuente
> Video: [Semana 2 - Desarrollo de ejercicios de circuitos ferromagnéticos - Ejercicio 2](https://www.youtube.com/watch?v=m1t3v6XouXk) — Aprendizaje Virtual UTP (30:21)

## Enunciado

Para el circuito magnético de la figura con **dos fuentes** y **dos materiales distintos**, determinar el flujo $\phi$ total presente en el núcleo teniendo en cuenta:

- **a)** Que los sentidos del número de devanados por la corriente son **distintos** (opuestos)
- **b)** Que los sentidos del número de devanados por la corriente son **coincidentes**

![[video3-datos.png]]
**Figura 1.** Circuito magnético con dos fuentes y dos materiales

### Datos

- $N_1 \cdot I_1 = 1000 \, \text{A.v}$
- $N_2 \cdot I_2 = 2000 \, \text{A.v}$
- $S_1 = S_2 = 0{,}2 \, \text{m}^2$
- $l_1 = 1 \, \text{m}$
- $l_2 = 1{,}2 \, \text{m}$

---

## Caso A: Sentidos opuestos

### Ecuación fundamental

Cuando los sentidos de $NI$ son **opuestos**, aplicando [[S01-2 Tema 01 - Los circuitos magnéticos|Kirchhoff para circuitos magnéticos]]:

$$N_2 I_2 - N_1 I_1 = H_1 \cdot l_1 + H_2 \cdot l_2$$

$$2000 - 1000 = H_1 \cdot l_1 + H_2 \cdot l_2 = 1000 \, \text{A.v}$$

### Método de ensayo y error

Como $S_1 = S_2$, entonces $B_1 = B_2 = B = \frac{\phi}{S}$

![[video3-tabla-materiales.png]]
**Figura 2.** Cálculo de $B$ a partir de $\phi$ asumido

#### Iteración 1: $\phi = 0{,}1$ Wb

$$B = \frac{0{,}1}{0{,}2} = 0{,}5 \, \text{T}$$

De las tablas de materiales:
- $H_1 = 55 \, \text{A.v/m}$
- $H_2 = 145 \, \text{A.v/m}$

$$H_1 \cdot l_1 + H_2 \cdot l_2 = 55 \times 1 + 145 \times 1{,}2 = 229 \, \text{A.v}$$

$229 \neq 1000$ → flujo demasiado bajo, **aumentar**.

#### Iteración 2: $\phi = 0{,}2$ Wb

$$B = \frac{0{,}2}{0{,}2} = 1{,}0 \, \text{T}$$

- $H_1 = 120 \, \text{A.v/m}$
- $H_2 = 667 \, \text{A.v/m}$

$$H_1 \cdot l_1 + H_2 \cdot l_2 = 120 \times 1 + 667 \times 1{,}2 = 920 \, \text{A.v}$$

$920 \neq 1000$ → se acerca, **aumentar levemente**.

#### Iteración 3: $\phi = 0{,}21$ Wb

$$B = \frac{0{,}21}{0{,}2} = 1{,}05 \, \text{T}$$

- $H_1 = 140 \, \text{A.v/m}$
- $H_2 = 778 \, \text{A.v/m}$

$$H_1 \cdot l_1 + H_2 \cdot l_2 = 140 \times 1 + 778 \times 1{,}2 = 1074 \, \text{A.v}$$

$1074 > 1000$ → pasamos, **reducir levemente**.

#### Iteración 4: $\phi = 0{,}205$ Wb

$$B = \frac{0{,}205}{0{,}2} = 1{,}025 \, \text{T}$$

- $H_1 = 130 \, \text{A.v/m}$
- $H_2 = 722 \, \text{A.v/m}$

$$H_1 \cdot l_1 + H_2 \cdot l_2 = 130 \times 1 + 722 \times 1{,}2 = 996 \, \text{A.v}$$

$996 \approx 1000$ → error $\approx 0{,}4\%$

### Resultado Caso A

$$\boxed{\phi \approx 0{,}205 \, \text{Wb} \quad \text{(sentidos opuestos)}}$$

---

## Caso B: Sentidos coincidentes

### Ecuación fundamental

Cuando los sentidos de $NI$ **coinciden**:

$$N_2 I_2 + N_1 I_1 = H_1 \cdot l_1 + H_2 \cdot l_2$$

$$2000 + 1000 = H_1 \cdot l_1 + H_2 \cdot l_2 = 3000 \, \text{A.v}$$

### Método de ensayo y error

#### Iteración 1: $\phi = 0{,}3$ Wb

$$B = \frac{0{,}3}{0{,}2} = 1{,}5 \, \text{T}$$

- $H_1 = 1867 \, \text{A.v/m}$
- $H_2 = 2200 \, \text{A.v/m}$

$$H_1 \cdot l_1 + H_2 \cdot l_2 = 1867 \times 1 + 2200 \times 1{,}2 = 4507 \, \text{A.v}$$

$4507 \gg 3000$ → **disminuir**.

#### Iteración 2: $\phi = 0{,}25$ Wb

$$B = 1{,}25 \, \text{T}$$

- $H_1 = 325 \, \text{A.v/m}$
- $H_2 = 1323 \, \text{A.v/m}$

$$325 \times 1 + 1323 \times 1{,}2 = 1913 \, \text{A.v}$$

$1913 < 3000$ → **aumentar**.

#### Iteración 3: $\phi = 0{,}27$ Wb

$$B = 1{,}35 \, \text{T}$$

- $H_1 = 575 \, \text{A.v/m}$
- $H_2 = 1645 \, \text{A.v/m}$

$$575 \times 1 + 1645 \times 1{,}2 = 2549 \, \text{A.v}$$

$2549 < 3000$ → **aumentar**.

#### Iteración 4: $\phi = 0{,}28$ Wb

$$B = 1{,}4 \, \text{T}$$

- $H_1 = 867 \, \text{A.v/m}$
- $H_2 = 1806 \, \text{A.v/m}$

$$867 \times 1 + 1806 \times 1{,}2 = 3034 \, \text{A.v}$$

$3034 \approx 3000$ → cercano, **reducir levemente**.

#### Iteración 5: $\phi = 0{,}279$ Wb

$$B = 1{,}395 \, \text{T}$$

- $H_1 = 833 \, \text{A.v/m}$
- $H_2 = 1790 \, \text{A.v/m}$

$$833 \times 1 + 1790 \times 1{,}2 = 2981 \, \text{A.v}$$

$2981 \approx 3000$ → error $\approx 0{,}6\%$

### Resultado Caso B

$$\boxed{\phi \approx 0{,}279 \, \text{Wb} \quad \text{(sentidos coincidentes)}}$$

---

## Verificación por método gráfico

Ambos resultados se verifican con el [[S02-5 Tema 04 - Metodos de analisis|método gráfico]], graficando las curvas de los dos materiales:

![[video3-grafico-opuestos.png]]
**Figura 3.** Método gráfico — sentidos opuestos ($F_{mm} = 1000$ A.v → $\phi \approx 0{,}205$ Wb)

![[video3-grafico-coincidentes.png]]
**Figura 4.** Método gráfico — sentidos coincidentes ($F_{mm} = 3000$ A.v → $\phi \approx 0{,}271$ Wb)

Los valores obtenidos gráficamente son consistentes con los obtenidos por aproximación analítica.

---

## Resumen de resultados

| Caso | Ecuación | $F_{mm}$ | $\phi$ |
| :--- | :--- | :---: | :---: |
| Sentidos opuestos | $N_2 I_2 - N_1 I_1$ | 1000 A.v | 0,205 Wb |
| Sentidos coincidentes | $N_2 I_2 + N_1 I_1$ | 3000 A.v | 0,279 Wb |
