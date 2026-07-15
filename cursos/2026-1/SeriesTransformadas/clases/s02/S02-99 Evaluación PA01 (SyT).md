---
title: Evaluacion PA01 - Series y Transformadas
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 2
orden: 99
tipo: evaluacion
subtipo: pa
tags:
  - curso/series-transformadas
  - tipo/evaluacion
  - subtipo/pa
  - tema/numeros-complejos
  - tema/raices-complejas
date: 2026-04-05
---

## Pregunta 1: Determinar los valores de $(-9)^{1/2}$

### Interpretacion

Se pide encontrar todas las raíces cuadradas del número complejo $z = -9$, es decir, los valores de $w$ tales que $w^2 = -9$.

### Desarrollo

#### Paso 1: Expresar $z = -9$ en [[S01-1 Tema 01 - Funciones en el plano complejo#Forma polar|forma polar]]

- Módulo: $|z| = |-9| = 9$
- Argumento principal: $\theta_0 = \pi$ (está sobre el eje real negativo)

$$z = -9 = 9\,e^{i\pi}$$

#### Paso 2: Aplicar la fórmula de [[S01-1 Tema 01 - Funciones en el plano complejo#Raíces n-esimas polar-exponencial|raíces n-ésimas]] con $m = 2$

Fuente: [[S01-1 Tema 01 - Funciones en el plano complejo#Raíces n-esimas polar-exponencial]] — Ejercicio análogo: [[S01-2 Tema 01 - Ejercicio 1 (SyT)#Ejercicio 1c Determinar los valores de $(-1)^{1/2}$]]

$$w_k = \sqrt[m]{|z|}\,e^{i\left(\frac{\theta_0 + 2k\pi}{m}\right)}, \quad k = 0, 1, \ldots, m-1$$

$$w_k = \sqrt[2]{9}\,e^{i\left(\frac{\pi + 2k\pi}{2}\right)} = 3\,e^{i\left(\frac{\pi + 2k\pi}{2}\right)}, \quad k = 0, 1$$

#### Paso 3: Calcular las 2 raíces

**Para $k = 0$:**

$$w_0 = 3\left(\cos\frac{\pi}{2} + i\,\text{sen}\frac{\pi}{2}\right) = 3(0 + i \cdot 1) = 3i$$

**Para $k = 1$:**

$$w_1 = 3\left(\cos\frac{3\pi}{2} + i\,\text{sen}\frac{3\pi}{2}\right) = 3(0 + i \cdot (-1)) = -3i$$

#### Verificación

$$w_0^2 = (3i)^2 = 9i^2 = 9(-1) = -9 \checkmark$$

$$w_1^2 = (-3i)^2 = 9i^2 = 9(-1) = -9 \checkmark$$

> [!success] Resultado
> Los valores de $(-9)^{1/2}$ son:
> $$w_0 = 3i \qquad \text{y} \qquad w_1 = -3i$$
> Ambas raíces están ubicadas sobre el circulo de radio 3, en los ángulos $\frac{\pi}{2}$ y $\frac{3\pi}{2}$ (eje imaginario).

## Pregunta 2: Expresar $3x + 2y = 6$ en coordenadas conjugadas

### Interpretacion

Se pide reescribir la ecuación lineal $3x + 2y = 6$ en términos de $z$ y $\bar{z}$, es decir, en coordenadas conjugadas.

### Desarrollo

Fuente: [[S01-1 Tema 01 - Funciones en el plano complejo#Propiedades del conjugado]] — Ejercicio análogo: [[S01-2 Tema 01 - Ejercicio 1 (SyT)#Ejercicio 1d Expresar $2x + y = 5$ en funcion de $z$ y $\bar{z}$]]

#### Paso 1: Expresar $x$ e $y$ en función de $z$ y $\bar{z}$

Sabemos que $z = x + iy$ y $\bar{z} = x - iy$. De las [[S01-1 Tema 01 - Funciones en el plano complejo#Propiedades del conjugado|propiedades del conjugado]]:

$$x = \frac{z + \bar{z}}{2}, \qquad y = \frac{z - \bar{z}}{2i}$$

#### Paso 2: Sustituir en la ecuación $3x + 2y = 6$

$$3\left(\frac{z + \bar{z}}{2}\right) + 2\left(\frac{z - \bar{z}}{2i}\right) = 6$$

$$\frac{3(z + \bar{z})}{2} + \frac{2(z - \bar{z})}{2i} = 6$$

#### Paso 3: Simplificar multiplicando todo por $2i$

$$2i \cdot \frac{3(z + \bar{z})}{2} + 2i \cdot \frac{2(z - \bar{z})}{2i} = 6 \cdot 2i$$

$$3i(z + \bar{z}) + 2(z - \bar{z}) = 12i$$

#### Paso 4: Expandir y agrupar por $z$ y $\bar{z}$

$$3iz + 3i\bar{z} + 2z - 2\bar{z} = 12i$$

$$z(3i + 2) + \bar{z}(3i - 2) = 12i$$

> [!success] Resultado
> La ecuación $3x + 2y = 6$ en coordenadas conjugadas es:
> $$(3i + 2)z + (3i - 2)\bar{z} = 12i$$

## Pregunta 3: Límite de $f(z) = \dfrac{\sqrt{z-9} - 3i}{z}$ cuando $z \to 0$

### Interpretacion

Se pide calcular $\displaystyle\lim_{z \to 0} \frac{\sqrt{z - 9} - 3i}{z}$. Hay un radical en el numerador, lo cual sugiere resolver por **racionalización**.

### Desarrollo

Fuente: [[S02-1 Tema 02 - Limites y continuidad de funciones complejas#Metodos para resolver limites]] — Ejercicio análogo: [[S02-2 Tema 02 - Ejercicio 1 (SyT)]]

#### Paso 1: Verificar la indeterminación

Evaluamos directamente en $z = 0$:

- Numerador: $\sqrt{0 - 9} - 3i = \sqrt{-9} - 3i = 3i - 3i = 0$
- Denominador: $0$

Donde $\sqrt{-9} = 3i$ porque $-9 = 9e^{i\pi}$, entonces $\sqrt{-9} = \sqrt{9}\,e^{i\pi/2} = 3i$ (ver [[S01-1 Tema 01 - Funciones en el plano complejo#Raíces n-esimas polar-exponencial|raíces n-ésimas]])

Obtenemos la indeterminación $\dfrac{0}{0}$, por lo que no podemos evaluar directamente.

#### Paso 2: Racionalizar

Multiplicamos numerador y denominador por el conjugado del numerador $(\sqrt{z - 9} + 3i)$:

$$\lim_{z \to 0} \frac{(\sqrt{z - 9} - 3i)(\sqrt{z - 9} + 3i)}{z(\sqrt{z - 9} + 3i)}$$

Aplicamos diferencia de cuadrados en el numerador:

$$\lim_{z \to 0} \frac{(\sqrt{z - 9})^2 - (3i)^2}{z(\sqrt{z - 9} + 3i)}$$

$$\lim_{z \to 0} \frac{(z - 9) - (9i^2)}{z(\sqrt{z - 9} + 3i)} = \lim_{z \to 0} \frac{(z - 9) - (-9)}{z(\sqrt{z - 9} + 3i)}$$

$$\lim_{z \to 0} \frac{z}{z(\sqrt{z - 9} + 3i)}$$

#### Paso 3: Simplificar $z$

$$\lim_{z \to 0} \frac{1}{\sqrt{z - 9} + 3i}$$

#### Paso 4: Evaluar el límite

$$\frac{1}{\sqrt{0 - 9} + 3i} = \frac{1}{3i + 3i} = \frac{1}{6i}$$

Racionalizamos multiplicando por $\dfrac{-6i}{-6i}$:

$$\frac{1}{6i} \cdot \frac{-6i}{-6i} = \frac{-i}{6}$$

> [!success] Resultado
> $$\lim_{z \to 0} \frac{\sqrt{z - 9} - 3i}{z} = -\frac{i}{6}$$

## Pregunta 4: Evaluar $\displaystyle\lim_{z \to 2i} \frac{z^2 + 1}{z^2 - 2iz - 1}$

### Interpretacion

Se pide evaluar el límite de una función racional compleja cuando $z \to 2i$.

### Desarrollo

Fuente: [[S02-1 Tema 02 - Limites y continuidad de funciones complejas#Propiedades de los limites]] — Método: [[S02-1 Tema 02 - Limites y continuidad de funciones complejas#Metodos para resolver limites]]

#### Paso 1: Verificar si hay indeterminación evaluando en $z = 2i$

**Numerador:**

$$z^2 + 1 = (2i)^2 + 1 = 4i^2 + 1 = -4 + 1 = -3$$

**Denominador:**

$$z^2 - 2iz - 1 = (2i)^2 - 2i(2i) - 1 = 4i^2 - 4i^2 - 1 = -4 - (-4) - 1 = -1$$

El denominador no se anula ($-1 \neq 0$), por lo tanto **no hay indeterminación** y podemos evaluar por [[S02-1 Tema 02 - Limites y continuidad de funciones complejas#Metodos para resolver limites|sustitución directa]].

#### Paso 2: Calcular el límite

$$\lim_{z \to 2i} \frac{z^2 + 1}{z^2 - 2iz - 1} = \frac{-3}{-1} = 3$$

> [!success] Resultado
> $$\lim_{z \to 2i} \frac{z^2 + 1}{z^2 - 2iz - 1} = 3$$

## Pregunta 5: Calcular $\displaystyle\lim_{x \to 1} \frac{x^4 - 1}{x - 1}$

### Interpretacion

Se pide calcular el límite de una función racional real cuando $x \to 1$. Al evaluar directamente se obtiene $\frac{0}{0}$, por lo que se resuelve por **factorización**.

### Desarrollo

Fuente: [[S02-1 Tema 02 - Limites y continuidad de funciones complejas#Metodos para resolver limites]] — Ejercicio análogo: [[S02-4 Tema 02 - Ejercicio 3 (SyT)]]

#### Paso 1: Verificar la indeterminación

$$\frac{1^4 - 1}{1 - 1} = \frac{0}{0}$$

Hay indeterminación, por lo que no podemos evaluar directamente.

#### Paso 2: Factorizar el numerador

Aplicamos diferencia de cuadrados sucesivamente:

$$x^4 - 1 = (x^2 - 1)(x^2 + 1) = (x - 1)(x + 1)(x^2 + 1)$$

#### Paso 3: Simplificar el factor común $(x - 1)$

$$\lim_{x \to 1} \frac{(x - 1)(x + 1)(x^2 + 1)}{x - 1} = \lim_{x \to 1} (x + 1)(x^2 + 1)$$

#### Paso 4: Evaluar el límite

$$(1 + 1)(1^2 + 1) = (2)(2) = 4$$

> [!success] Resultado
> $$\lim_{x \to 1} \frac{x^4 - 1}{x - 1} = 4$$
