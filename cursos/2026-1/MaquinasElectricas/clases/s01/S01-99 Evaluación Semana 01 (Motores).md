---
title: "Evaluación Semana 01 (Motores)"
curso: "[[Motores MOC]]"
unidad: 1
semana: 1
orden: 99
tipo: evaluacion
subtipo: cuestionario
tags:
  - curso/motores
  - tipo/evaluacion
  - subtipo/cuestionario
  - tema/permeabilidad-magnetica
  - tema/curva-de-magnetizacion
  - tema/histeresis
date: 2026-03-29
---

## 1. ¿Cuál será la permeabilidad relativa del material ferromagnético típico, cuya curva de magnetización se muestra en la siguiente figura cuando H = 50 A • espiras/m?

![[Pasted image 20260329185300.png]]

a. ur=3980
b. ur=5730
c. ur=2230

### Resolución

**Datos del gráfico:** Para $H = 50 \text{ A·espiras/m}$, la curva de magnetización muestra:

$$B \approx 0.25 \text{ T}$$

**Cálculo de la permeabilidad relativa:**

$$B = \mu_0 \cdot \mu_r \cdot H \implies \mu_r = \frac{B}{\mu_0 \cdot H}$$

$$\mu_r = \frac{0.25}{(4\pi \times 10^{-7})(50)} = \frac{0.25}{6.2832 \times 10^{-5}} \approx 3980$$

**Descarte de las otras opciones:** verificando qué $B$ implicaría cada una en $H = 50$:

- $\mu_r = 5730 \implies B = (4\pi \times 10^{-7})(5730)(50) = 0.36 \text{ T}$ — demasiado alto respecto a la curva
- $\mu_r = 2230 \implies B = (4\pi \times 10^{-7})(2230)(50) = 0.14 \text{ T}$ — demasiado bajo respecto a la curva

Solo $\mu_r = 3980$ produce $B \approx 0.25 \text{ T}$, consistente con la lectura del gráfico en $H = 50$.

**Teoría:** [[S01-7 Tema 05 - Obtencion de la curva de magnetizacion|Obtención de la curva de magnetización]] · [[S01-2 Tema 01 - Los circuitos magnéticos|Los circuitos magnéticos]]

> [!success] Respuesta: **a. $\mu_r = 3980$**

##   2. ¿Cuál será la permeabilidad relativa del material ferromagnético típico, cuya curva de magnetización se muestra en la siguiente figura cuando H = 100 A • espiras/m?

![[Pasted image 20260329190041.png]]

Selecciona 1 alternativa.

a. ur=5730
b. ur=3980
c. ur=2230

### Resolución

**Lectura del gráfico:** Para $H = 100 \text{ A·espiras/m}$, la curva de magnetización muestra:

$$B \approx 0.72 \text{ T}$$

**Fórmula:**

$$B = \mu_0 \cdot \mu_r \cdot H \implies \mu_r = \frac{B}{\mu_0 \cdot H}$$

**Cálculo:**

$$\mu_r = \frac{0.72}{(4\pi \times 10^{-7})(100)} = \frac{0.72}{1.2566 \times 10^{-4}} \approx 5730$$

**Verificación con todas las opciones** — calculando qué $B$ implicaría cada $\mu_r$ en $H = 100$:

| Opción | $\mu_r$ | $B = \mu_0 \cdot \mu_r \cdot H$ | ¿Consistente con la curva? |
| ------ | ------- | -------------------------------- | -------------------------- |
| a      | 5730    | $(4\pi \times 10^{-7})(5730)(100) = 0.72 \text{ T}$ | ✅ Sí, coincide con la lectura |
| b      | 3980    | $(4\pi \times 10^{-7})(3980)(100) = 0.50 \text{ T}$ | ❌ Bajo respecto a la curva |
| c      | 2230    | $(4\pi \times 10^{-7})(2230)(100) = 0.28 \text{ T}$ | ❌ Muy bajo respecto a la curva |

**Teoría:** [[S01-7 Tema 05 - Obtencion de la curva de magnetizacion|Obtención de la curva de magnetización]] · [[S01-2 Tema 01 - Los circuitos magnéticos|Los circuitos magnéticos]]

> [!success] Respuesta: **a. $\mu_r = 5730$**


## 3. ¿Cuál será la permeabilidad relativa del material ferromagnético típico, cuya curva de magnetización se muestra en la siguiente figura cuando H = 500 A • espiras/m?

![[Pasted image 20260329190408.png]]

Selecciona 1 alternativa.

a. ur=2230
b. ur=3980
c. ur=5730

### Resolución

**Lectura del gráfico:** Para $H = 500 \text{ A·espiras/m}$, la curva de magnetización muestra:

$$B \approx 1.40 \text{ T}$$

**Fórmula:**

$$\mu_r = \frac{B}{\mu_0 \cdot H}$$

**Cálculo:**

$$\mu_r = \frac{1.40}{(4\pi \times 10^{-7})(500)} = \frac{1.40}{6.2832 \times 10^{-4}} \approx 2228 \approx 2230$$

**Verificación con todas las opciones** — calculando qué $B$ implicaría cada $\mu_r$ en $H = 500$:

| Opción | $\mu_r$ | $B = \mu_0 \cdot \mu_r \cdot H$ | ¿Consistente con la curva? |
| ------ | ------- | -------------------------------- | -------------------------- |
| a      | 2230    | $(4\pi \times 10^{-7})(2230)(500) = 1.40 \text{ T}$ | ✅ Sí, coincide con la lectura |
| b      | 3980    | $(4\pi \times 10^{-7})(3980)(500) = 2.50 \text{ T}$ | ❌ Muy alto, supera la curva |
| c      | 5730    | $(4\pi \times 10^{-7})(5730)(500) = 3.60 \text{ T}$ | ❌ Imposible, fuera de escala |

**Teoría:** [[S01-7 Tema 05 - Obtencion de la curva de magnetizacion|Obtención de la curva de magnetización]] · [[S01-2 Tema 01 - Los circuitos magnéticos|Los circuitos magnéticos]]

> [!success] Respuesta: **a. $\mu_r = 2230$**

## 4. ¿Cómo es la permeabilidad de los materiales ferromagnéticos?

a. La permeabilidad relativa de los materiales ferromagnéticos es muy superior a 1.
b. La permeabilidad relativa de los materiales ferromagnéticos es aproximadamente 1.
c. Los materiales ferromagnéticos no tienen permeabilidad relativa.

### Resolución

Los materiales ferromagnéticos (hierro, cobalto, níquel y sus aleaciones) se caracterizan por tener una permeabilidad relativa $\mu_r$ muy superior a 1, típicamente en el rango de $10^2$ a $10^5$. Esto es lo que les permite concentrar líneas de campo magnético y ser utilizados en núcleos de transformadores, motores y otros dispositivos electromagnéticos.

Como se comprobó en las preguntas anteriores con la curva de magnetización:
- En $H = 50$: $\mu_r = 3980$
- En $H = 100$: $\mu_r = 5730$
- En $H = 500$: $\mu_r = 2230$

Todos valores muy superiores a 1.

**Descarte de otras opciones:**
- **b.** $\mu_r \approx 1$ corresponde a materiales paramagnéticos (aluminio, platino), no ferromagnéticos
- **c.** Todos los materiales tienen permeabilidad relativa; es una propiedad física inherente

**Teoría:** [[S01-1 Tema 01 - Como se produce un campo magnético|Cómo se produce un campo magnético]] · [[S01-2 Tema 01 - Los circuitos magnéticos|Los circuitos magnéticos]]

> [!success] Respuesta: **a. La permeabilidad relativa de los materiales ferromagnéticos es muy superior a 1.**

## 5. ¿Qué se entiende por histéresis?

Selecciona 1 alternativa.

a. Histéresis es la tendencia de un material a conservar una de sus propiedades en ausencia del estímulo que la ha generado.
b. Histéresis es la tendencia de un material a perder su capacidad magnética con el tiempo, volviéndose cada vez menos reactivo a los campos magnéticos externos.
c. Histéresis es la propiedad de algunos materiales de cambiar su temperatura interna de manera significativa cuando se exponen a campos magnéticos, lo que afecta directamente a su comportamiento magnético.

### Resolución

La histéresis magnética describe el fenómeno donde un material ferromagnético retiene magnetización ($B$ remanente) incluso después de retirar el campo magnético externo ($H = 0$). El material "recuerda" su estado magnético anterior — por eso el ciclo de histéresis no sigue el mismo camino al aumentar y disminuir $H$.

**Descarte de otras opciones:**
- **b.** Describe una degradación temporal que no corresponde a histéresis. Los materiales ferromagnéticos no pierden su capacidad magnética con el tiempo de esa manera
- **c.** Describe un efecto magnetocalórico, no histéresis. Si bien existen pérdidas por histéresis que generan calor, la definición fundamental es la retención de propiedades, no el cambio de temperatura

**Teoría:** [[S01-7 Tema 05 - Obtencion de la curva de magnetizacion|Obtención de la curva de magnetización]]

> [!success] Respuesta: **a. Histéresis es la tendencia de un material a conservar una de sus propiedades en ausencia del estímulo que la ha generado.**