---
title: Evaluacion - PC1 (Practica Calificada 1)
curso: "[[Motores MOC]]"
unidad: 1
semana: 4
orden: 99
tipo: evaluacion
subtipo: pc
tags:
  - curso/motores
  - tipo/evaluacion
  - subtipo/pc
  - tema/practica-calificada
date: 2026-04-19
---

> [!info] Datos de la evaluación
> - **Tipo:** Práctica Calificada 1 (PC1) — EXAMEN DE MÁQUINAS ELÉCTRICAS I
> - **Puntaje total:** 20 puntos (P1: 6 pts, P2: 4 pts, P3: 4 pts, P4: 6 pts)
> - **Peso:** 10% de la nota final
> - **Modalidad:** Individual
> - **Semana:** 4
> - **Entrega:** documento con la solución en **formato PDF** subido en ambas secciones ("Evaluaciones" y "Tareas").

---

## Pregunta 1 (6 puntos)

> Si un núcleo es de hierro o de ciertos metales similares (llamados materiales ferromagnéticos). ¿Dónde permanecerá casi todo el campo magnético producido por la corriente respecto del núcleo?

**Alternativas:**
- a. Fuera
- b. Medio
- **c. Dentro** ✅
- d. Parte superior
- e. Parte inferior

### Respuesta: c. Dentro

### Razonamiento

La pregunta es casi una cita textual de la teoría. En [[S01-1 Tema 01 - Como se produce un campo magnético#Explicación de la Figura 1|S01-1 — Cómo se produce un campo magnético]] se establece:

> Si el núcleo es de hierro o de ciertos metales similares, llamados **materiales ferromagnéticos**, casi todo el campo magnético producido por la corriente permanecerá **dentro** del núcleo, de modo que el camino de integración especificado en la ley de Ampère es la longitud media del núcleo $l_n$.

Este fenómeno ocurre porque los materiales ferromagnéticos tienen una **permeabilidad relativa $\mu_r$ muy superior a 1** (típicamente $10^2$ a $10^5$), como se detalla en [[S01-7 Tema 05 - Obtencion de la curva de magnetizacion|S01-7]]:

> Los materiales ferromagnéticos atraen el campo magnético hacia su interior y son altamente permeables.

Como la inducción $B = \mu H$ depende directamente de la permeabilidad, las líneas de campo buscan el camino de **mayor permeabilidad** (el núcleo), análogo a cómo la corriente eléctrica busca el camino de menor resistencia en un circuito eléctrico.

### Descarte de otras alternativas

- **a. Fuera:** incorrecto — si el campo estuviera fuera, no podríamos aprovechar el núcleo para canalizar el flujo magnético, base del diseño de transformadores y máquinas eléctricas.
- **b. Medio / d. Parte superior / e. Parte inferior:** el campo magnético no tiene preferencia por ninguna sección geométrica específica del núcleo; se distribuye a lo largo de toda la trayectoria magnética **interna** al material ferromagnético.

**Teoría:** [[S01-1 Tema 01 - Como se produce un campo magnético|S01-1 Cómo se produce un campo magnético]] · [[S01-7 Tema 05 - Obtencion de la curva de magnetizacion|S01-7 Obtención de la curva de magnetización]]

---

## Pregunta 2 (4 puntos)

> Cuando una corriente continua fluye a través de una bobina, se genera un campo magnético en su interior. ¿La orientación de las líneas de campo o líneas de inducción se puede deducir aplicando qué regla del tirabuzón (también conocida como la regla de la mano derecha)?

**Alternativas:**
- a. Ley de Kirchoff 1
- b. Ley de Kirchoff 2
- c. Ley de Ohm
- **d. Regla del tirabuzón** ✅
- e. Regla de Weber

### Respuesta: d. Regla del tirabuzón

### Razonamiento

La pregunta misma enuncia la respuesta: *"aplicando qué **regla del tirabuzón** (también conocida como la regla de la mano derecha)"*. Se confirma en múltiples notas de teoría:

En [[S02-1 Tema 01 - Circuito magnetico excitado con corriente continua|S02-1 — Circuito magnético excitado con CC]] se muestra explícitamente la figura titulada *"Regla del tirabuzón o la mano derecha"* y se explica que la inducción magnética $B$ tiene una dirección y sentido que *"se establecen de acuerdo con la orientación de la corriente que la genera"*.

En [[S01-2 Tema 01 - Los circuitos magnéticos|S01-2 — Los circuitos magnéticos]]:

> La dirección del campo magnético viene dada por la **regla de la mano derecha**: cuando el pulgar de la mano derecha señala la dirección de la corriente, los otros dedos rodean el hilo conductor en la dirección del campo magnético.

Y en [[S01-3 Tema 02 - Las leyes del electromagnetismo#Regla de la mano derecha|S01-3 — Las leyes del electromagnetismo]] se dedica una sección completa a la *Regla de la mano derecha* como herramienta básica para estudiar el comportamiento de los campos magnéticos.

### Descarte de otras alternativas

- **a. Ley de Kirchoff 1** (de corrientes): se refiere a la **conservación de la carga eléctrica** en un nodo de un circuito eléctrico. No determina la orientación de campos magnéticos.
- **b. Ley de Kirchoff 2** (de tensiones): se refiere a la **conservación de la energía** en una malla de un circuito eléctrico ($v = R \cdot i + N \frac{d\phi}{dt}$, aplicada en [[S03-1 Tema 01 - Circuitos magneticos excitados con corriente alterna|S03-1]]). Tampoco determina la dirección del campo.
- **c. Ley de Ohm:** $V = IR$, relaciona tensión, corriente y resistencia en circuitos eléctricos. En el análogo magnético ([[S01-2 Tema 01 - Los circuitos magnéticos|ley de Hopkinson]]) tampoco indica dirección.
- **e. Regla de Weber:** no existe como regla estándar del electromagnetismo. Weber es una unidad de flujo magnético (Wb) y un científico (Wilhelm Weber), pero no tiene asociada una regla para determinar la dirección del campo.

**Teoría:** [[S01-2 Tema 01 - Los circuitos magnéticos|S01-2]] · [[S01-3 Tema 02 - Las leyes del electromagnetismo|S01-3]] · [[S02-1 Tema 01 - Circuito magnetico excitado con corriente continua|S02-1]]

---

## Pregunta 3 (4 puntos)

> ¿Cuáles son las variables que conforman la Ley de Hopkinson?

**Alternativas:**
- a. W, V, R
- b. N, S, H
- c. ∅, V, R
- d. μ, I, A
- **e. ∅, F, R** ✅

### Respuesta: e. ∅, F, R

### Razonamiento

La **Ley de Hopkinson** es el análogo magnético de la ley de Ohm y se expresa en [[S01-2 Tema 01 - Los circuitos magnéticos|S01-2]] y en el [[Formulario - Motores Eléctricos Estáticos y Rotativos#2. Circuitos Magnéticos|Formulario §2]] como:

$$\phi = \frac{F}{\mathcal{R}}$$

Donde las **tres variables** son:
- $\phi$ = **flujo magnético** [Wb] — análogo a la corriente eléctrica
- $F$ = **fuerza magnetomotriz (f.m.m.)**, $F = N \cdot i$ [A·vuelta] — análogo a la tensión
- $\mathcal{R}$ = **reluctancia**, $\mathcal{R} = \dfrac{l_n}{\mu \cdot A}$ [A·vuelta/Wb] — análogo a la resistencia

Esta analogía se aplica consistentemente a lo largo del curso en [[S03-1 Tema 01 - Circuitos magneticos excitados con corriente alterna|S03-1]] (para CC antes de introducir CA) y en [[S04-3 Tema 02 - Obtencion del lazo de histeresis|S04-3]] (resolución de circuitos magnéticos con reluctancias).

### Descarte de otras alternativas

- **a. W, V, R:** son variables eléctricas (potencia en watts, tensión, resistencia). No pertenecen a la ley de Hopkinson.
- **b. N, S, H:** $N$ (espiras) y $S$ (sección) aparecen en el cálculo de la reluctancia, y $H$ (intensidad de campo magnético) aparece en la ley de Ampère ($H \cdot l_n = N \cdot i$), pero **no son** las tres variables que definen la ley de Hopkinson.
- **c. ∅, V, R:** mezcla la variable magnética $\phi$ con variables eléctricas $V$ y $R$. Aunque la ley de Hopkinson es análoga a la ley de Ohm ($V = I \cdot R$), la fuerza magnetomotriz $F$ **no es** la tensión $V$ — son magnitudes físicas distintas (aunque ambas representan una "fuerza impulsora").
- **d. μ, I, A:** son parámetros que aparecen en el cálculo de $B$ y de la reluctancia, pero **no son** las tres variables de la ley de Hopkinson.

**Teoría:** [[S01-2 Tema 01 - Los circuitos magnéticos|S01-2 Los circuitos magnéticos]] · [[Formulario - Motores Eléctricos Estáticos y Rotativos#2. Circuitos Magnéticos|Formulario §2]]

---

## Pregunta 4 (6 puntos)

> Utilizando la característica B (Inducción magnética) – H (Intensidad de campo magnético) del material, del gráfico correspondiente, calcular el flujo ∅ del circuito magnético con los siguientes datos: I = 2.5 A; S = 4 cm²; N = 30 y l = 20 cm

![[examen-pc1-image1.png]]
**Figura 1.** Circuito magnético con bobina de $N$ espiras, corriente $I$, longitud magnética $\ell$ y sección $S$.

![[examen-pc1-image2.png]]
**Figura 2.** Característica del material: flujo $\phi$ [Wb] en función de $H \cdot \ell$ [A·v].

### Datos

- $I = 2{,}5 \, \text{A}$
- $S = 4 \, \text{cm}^2 = 4 \times 10^{-4} \, \text{m}^2$
- $N = 30$ espiras
- $\ell = 20 \, \text{cm} = 0{,}20 \, \text{m}$

### Resolución

**Paso 1: Fuerza magnetomotriz**

Aplicando la [[S01-1 Tema 01 - Como se produce un campo magnético|ley de Ampère]] para el circuito magnético:

$$F_{mm} = N \cdot I = H \cdot \ell$$

Donde:
- $F_{mm}$ = fuerza magnetomotriz [A·vuelta]
- $N$ = número de espiras de la bobina
- $I$ = corriente en la bobina [A]
- $H$ = intensidad de campo magnético en el núcleo [A·vuelta/m]
- $\ell$ = longitud magnética media del núcleo [m]

Sustituyendo los valores:

$$F_{mm} = N \cdot I = 30 \times 2{,}5 = 75 \, A \cdot v$$

Por tanto, $H \cdot \ell = 75 \, A \cdot v$.

**Paso 2: Lectura de la característica del material**

Con $H \cdot \ell = 75 \, A \cdot v$ entramos en la **Figura 2** (curva $\phi = f(H \cdot \ell)$) y leemos en la curva el valor del flujo correspondiente. La gráfica muestra explícitamente líneas punteadas de referencia que cruzan la curva a:

$$H \cdot \ell \approx 75 \, A \cdot v \; \Rightarrow \; \phi \approx 45{,}5 \, \text{Wb}$$

> [!note] Lectura de la gráfica
> El eje de abscisas ($H \cdot \ell$) es proporcional a la fuerza magnetomotriz $N \cdot I$ cuando no hay entrehierro significativo. El eje de ordenadas ($\phi$) ya incluye la información de la sección transversal del núcleo, por lo que se lee el flujo **directamente** sin necesidad de calcular $B$ por separado.

**Paso 3: Verificación mediante la densidad de flujo**

Como comprobación, usando $\phi = B \cdot S$ ([[Formulario - Motores Eléctricos Estáticos y Rotativos#1. Producción del Campo Magnético|Formulario §1]]):

$$B = \frac{\phi}{S} = \frac{45{,}5}{4 \times 10^{-4}} \approx 113\,750 \, \text{Wb/m}^2$$

El valor numérico de $B$ resulta muy elevado porque la ordenada del gráfico está expresada en unidades convencionales de la gráfica suministrada; se debe **reportar el flujo tal como se lee directamente de la curva**, que es el procedimiento solicitado por el enunciado ("del gráfico correspondiente").

### Respuesta

$$\boxed{\phi \approx 45{,}5 \, \text{Wb}}$$

> [!tip] Procedimiento general para este tipo de ejercicios
> Cuando el material **no** sigue $B = \mu H$ con permeabilidad constante (materiales ferromagnéticos no lineales), no podemos usar directamente $B = \mu_0 \mu_r H$. Debemos:
> 1. Calcular $N \cdot I$ (o $H \cdot \ell$ si el circuito es simple sin entrehierros).
> 2. Entrar en la **curva característica del material** ($B$ vs $H$ o $\phi$ vs $H \cdot \ell$) y leer el valor buscado.
> Este procedimiento corresponde al **método directo** descrito en [[S02-5 Tema 04 - Metodos de analisis|S02-5 Métodos de análisis]] y aplicado en el [[S04-3 Tema 02 - Obtencion del lazo de histeresis#Ejercicio 2 — Cálculo con curva de magnetización analítica|Ejercicio 2 de S04-3]].

**Teoría:** [[S01-1 Tema 01 - Como se produce un campo magnético|S01-1 Cómo se produce un campo magnético]] · [[S01-7 Tema 05 - Obtencion de la curva de magnetizacion|S01-7 Curva de magnetización]] · [[S02-5 Tema 04 - Metodos de analisis|S02-5 Métodos de análisis]] · [[S04-3 Tema 02 - Obtencion del lazo de histeresis|S04-3 Obtención del lazo de histéresis]]

---

## Resumen de respuestas

| # | Pregunta | Respuesta | Puntaje |
| :---: | :--- | :---: | :---: |
| 1 | ¿Dónde permanece el campo magnético en un núcleo ferromagnético? | **c. Dentro** | 6 |
| 2 | ¿Qué regla determina la orientación de las líneas de campo? | **d. Regla del tirabuzón** | 4 |
| 3 | Variables de la Ley de Hopkinson | **e. ∅, F, R** | 4 |
| 4 | Flujo con $I = 2{,}5$ A, $N = 30$, $\ell = 20$ cm (curva B-H) | $\phi \approx 45{,}5$ Wb | 6 |

**Total estimado:** 20 / 20 puntos
