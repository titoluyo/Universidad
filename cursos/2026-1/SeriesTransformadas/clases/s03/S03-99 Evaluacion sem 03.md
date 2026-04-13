---
title: Evaluacion semana 03
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 3
orden: 99
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/cauchy-riemann
  - tema/derivada-compleja
date: 2026-04-12
---

## Ejercicio 1

**Pregunta:** Identifica las componentes $u$ y $v$. Aplica la definición de las ecuaciones de Cauchy-Riemann. Aplica las propiedades de las derivadas. Indique si la función $f(z) = z^2$ es diferenciable en todas partes.

**Opciones:**
- a) Sí es diferenciable en todas partes.
- b) No es diferenciable en todas partes.
- c) Faltan datos para indicar si es diferenciable en todas partes.

### Desarrollo

Para verificar si $f(z) = z^2$ es diferenciable en todas partes, aplicamos las [[S03-1 Tema 03 - Derivada de una funcion compleja#Ecuacion de Cauchy-Riemann|ecuaciones de Cauchy-Riemann]].

#### Paso 1: Sustituir $z = x + iy$

$$f(z) = (x + iy)^2 = x^2 + 2ixy + i^2y^2 = x^2 - y^2 + 2ixy$$

#### Paso 2: Identificar componentes $u$ y $v$

$$f(z) = \underbrace{(x^2 - y^2)}_{u(x,y)} + i\underbrace{(2xy)}_{v(x,y)}$$

Donde:
- $u(x,y) = x^2 - y^2$
- $v(x,y) = 2xy$

#### Paso 3: Verificar ecuación (1) de Cauchy-Riemann

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$

Calculamos:

$$\frac{\partial u}{\partial x} = 2x$$

$$\frac{\partial v}{\partial y} = 2x$$

$$2x = 2x \quad \checkmark$$

#### Paso 4: Verificar ecuación (2) de Cauchy-Riemann

$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

Calculamos:

$$\frac{\partial u}{\partial y} = -2y$$

$$-\frac{\partial v}{\partial x} = -(2y) = -2y$$

$$-2y = -2y \quad \checkmark$$

#### Conclusión

Ambas ecuaciones de Cauchy-Riemann se satisfacen para **todo** $(x, y) \in \mathbb{R}^2$, y las derivadas parciales son continuas en todas partes (son polinomios). Por lo tanto, $f(z) = z^2$ es diferenciable en todo punto $z$.

> [!success] Respuesta
> **a) Sí es diferenciable en todas partes.**

**Referencia:** [[S03-1 Tema 03 - Derivada de una funcion compleja#Ecuacion de Cauchy-Riemann]] y [[S03-4 Tema 03 - Ejercicio 3 (SyT)]] (ejercicio análogo con $f(z) = z^2 + 5iz + 3 - i$)

---

## Ejercicio 2

**Pregunta:** Identifica las componentes $u$ y $v$. Aplica la definición de las ecuaciones de Cauchy-Riemann. Aplica las propiedades de las derivadas. Indique si la función $f(z) = |z|^2$ satisface las ecuaciones de Cauchy-Riemann.

**Opciones:**
- a) Sí satisface las ecuaciones de Cauchy-Riemann.
- b) No satisface las ecuaciones de Cauchy-Riemann, salvo si $x = y = 0$.
- c) No satisface las ecuaciones de Cauchy-Riemann.

### Desarrollo

Aplicamos las [[S03-1 Tema 03 - Derivada de una funcion compleja#Ecuacion de Cauchy-Riemann|ecuaciones de Cauchy-Riemann]] para determinar dónde $f(z) = |z|^2$ las satisface.

#### Paso 1: Sustituir $z = x + iy$

$$f(z) = |z|^2 = |x + iy|^2 = x^2 + y^2$$

Notemos que $f(z)$ es una función puramente real (no tiene parte imaginaria).

#### Paso 2: Identificar componentes $u$ y $v$

$$f(z) = \underbrace{(x^2 + y^2)}_{u(x,y)} + i\underbrace{(0)}_{v(x,y)}$$

Donde:
- $u(x,y) = x^2 + y^2$
- $v(x,y) = 0$

#### Paso 3: Verificar ecuación (1) de Cauchy-Riemann

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$

Calculamos:

$$\frac{\partial u}{\partial x} = 2x$$

$$\frac{\partial v}{\partial y} = 0$$

$$2x = 0 \implies \text{solo se cumple si } x = 0$$

#### Paso 4: Verificar ecuación (2) de Cauchy-Riemann

$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

Calculamos:

$$\frac{\partial u}{\partial y} = 2y$$

$$-\frac{\partial v}{\partial x} = 0$$

$$2y = 0 \implies \text{solo se cumple si } y = 0$$

#### Conclusión

Las ecuaciones de Cauchy-Riemann se satisfacen **únicamente** cuando $x = 0$ **y** $y = 0$ simultáneamente, es decir, solo en el origen $z = 0$. En cualquier otro punto del plano complejo, al menos una de las ecuaciones falla.

> [!success] Respuesta
> **b) No satisface las ecuaciones de Cauchy-Riemann, salvo si $x = y = 0$.**

**Referencia:** [[S03-1 Tema 03 - Derivada de una funcion compleja#Ecuacion de Cauchy-Riemann]]

---

## Ejercicio 3

**Pregunta:** Identifica las componentes $u$ y $v$. Aplica la definición de las condiciones del segundo teorema. Aplica las propiedades de las derivadas. Sea la función $f(z) = \frac{1}{z}$, verifique si cumple las condiciones del segundo teorema.

**Opciones:**
- a) Sí cumple las condiciones del segundo teorema.
- b) No cumple las condiciones del segundo teorema.
- c) Faltan datos para verificar las condiciones del segundo teorema.

### Desarrollo

El [[S03-1 Tema 03 - Derivada de una funcion compleja#Teorema 2 Forma polar|segundo teorema (forma polar)]] establece las ecuaciones de Cauchy-Riemann en coordenadas polares. Para $f(z) = 1/z$ conviene usar la forma polar.

#### Paso 1: Expresar $f(z)$ en forma polar

Con $z = re^{i\theta}$:

$$f(z) = \frac{1}{z} = \frac{1}{re^{i\theta}} = \frac{1}{r}e^{-i\theta} = \frac{1}{r}(\cos\theta - i\operatorname{sen}\theta)$$

#### Paso 2: Identificar componentes $u$ y $v$

$$f(z) = \underbrace{\frac{\cos\theta}{r}}_{u(r,\theta)} + i\underbrace{\left(-\frac{\operatorname{sen}\theta}{r}\right)}_{v(r,\theta)}$$

Donde:
- $u(r,\theta) = \dfrac{\cos\theta}{r}$
- $v(r,\theta) = -\dfrac{\operatorname{sen}\theta}{r}$

#### Paso 3: Verificar ecuación (10) de Cauchy-Riemann polar

$$\frac{\partial u}{\partial r} = \frac{1}{r}\frac{\partial v}{\partial \theta}$$

Calculamos:

$$\frac{\partial u}{\partial r} = -\frac{\cos\theta}{r^2}$$

$$\frac{1}{r}\frac{\partial v}{\partial \theta} = \frac{1}{r} \cdot \left(-\frac{\cos\theta}{r}\right) = -\frac{\cos\theta}{r^2}$$

$$-\frac{\cos\theta}{r^2} = -\frac{\cos\theta}{r^2} \quad \checkmark$$

#### Paso 4: Verificar ecuación (11) de Cauchy-Riemann polar

$$\frac{1}{r}\frac{\partial u}{\partial \theta} = -\frac{\partial v}{\partial r}$$

Calculamos:

$$\frac{1}{r}\frac{\partial u}{\partial \theta} = \frac{1}{r} \cdot \left(-\frac{\operatorname{sen}\theta}{r}\right) = -\frac{\operatorname{sen}\theta}{r^2}$$

$$-\frac{\partial v}{\partial r} = -\left(\frac{\operatorname{sen}\theta}{r^2}\right) = -\frac{\operatorname{sen}\theta}{r^2}$$

$$-\frac{\operatorname{sen}\theta}{r^2} = -\frac{\operatorname{sen}\theta}{r^2} \quad \checkmark$$

#### Conclusión

Ambas ecuaciones de Cauchy-Riemann en forma polar se satisfacen para todo $r \neq 0$, y las derivadas parciales son continuas en todo punto donde $r \neq 0$. Por lo tanto, $f(z) = 1/z$ cumple las condiciones del segundo teorema en todo punto $z \neq 0$.

> [!success] Respuesta
> **a) Sí cumple las condiciones del segundo teorema.**

**Referencia:** [[S03-1 Tema 03 - Derivada de una funcion compleja#Teorema 2 Forma polar]]

---

## Ejercicio 4

**Pregunta:** Identifica las componentes $u$ y $v$. Aplica la definición de las ecuaciones de Cauchy-Riemann. Aplica las propiedades de las derivadas. Determinar si existe $f'(z)$ en todas partes y calcule su valor si $f(z) = \frac{1}{z}$.

**Opciones:**
- a) No existe $f'(z)$; pero, aproximando, su valor es de $-\frac{1}{z^2}$.
- b) Sí existe $f'(z)$ y su valor es de $-\frac{1}{z^2}$.
- c) No existe $f'(z)$; por lo tanto, no se puede calcular la derivada.

### Desarrollo

Aplicamos las [[S03-1 Tema 03 - Derivada de una funcion compleja#Ecuacion de Cauchy-Riemann|ecuaciones de Cauchy-Riemann]] en forma cartesiana para verificar la existencia de $f'(z)$ y luego calculamos su valor.

#### Paso 1: Sustituir $z = x + iy$

$$f(z) = \frac{1}{z} = \frac{1}{x + iy} = \frac{x - iy}{(x + iy)(x - iy)} = \frac{x - iy}{x^2 + y^2}$$

#### Paso 2: Identificar componentes $u$ y $v$

$$f(z) = \underbrace{\frac{x}{x^2 + y^2}}_{u(x,y)} + i\underbrace{\left(-\frac{y}{x^2 + y^2}\right)}_{v(x,y)}$$

Donde:
- $u(x,y) = \dfrac{x}{x^2 + y^2}$
- $v(x,y) = -\dfrac{y}{x^2 + y^2}$

#### Paso 3: Verificar ecuación (7) de Cauchy-Riemann

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$$

Calculamos $\frac{\partial u}{\partial x}$ usando la regla del cociente:

$$\frac{\partial u}{\partial x} = \frac{(x^2 + y^2) - x \cdot 2x}{(x^2 + y^2)^2} = \frac{y^2 - x^2}{(x^2 + y^2)^2}$$

Calculamos $\frac{\partial v}{\partial y}$:

$$\frac{\partial v}{\partial y} = -\frac{(x^2 + y^2) - y \cdot 2y}{(x^2 + y^2)^2} = -\frac{x^2 - y^2}{(x^2 + y^2)^2} = \frac{y^2 - x^2}{(x^2 + y^2)^2}$$

$$\frac{y^2 - x^2}{(x^2 + y^2)^2} = \frac{y^2 - x^2}{(x^2 + y^2)^2} \quad \checkmark$$

#### Paso 4: Verificar ecuación (8) de Cauchy-Riemann

$$\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

Calculamos $\frac{\partial u}{\partial y}$:

$$\frac{\partial u}{\partial y} = \frac{0 - x \cdot 2y}{(x^2 + y^2)^2} = -\frac{2xy}{(x^2 + y^2)^2}$$

Calculamos $-\frac{\partial v}{\partial x}$:

$$\frac{\partial v}{\partial x} = -\frac{0 - y \cdot 2x}{(x^2 + y^2)^2} = \frac{2xy}{(x^2 + y^2)^2}$$

$$-\frac{\partial v}{\partial x} = -\frac{2xy}{(x^2 + y^2)^2}$$

$$-\frac{2xy}{(x^2 + y^2)^2} = -\frac{2xy}{(x^2 + y^2)^2} \quad \checkmark$$

Las ecuaciones de Cauchy-Riemann se cumplen para todo $z \neq 0$, y las derivadas parciales son continuas. Por tanto, $f'(z)$ **existe**.

#### Paso 5: Calcular $f'(z)$

Usando la fórmula $f'(z) = \frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x}$:

$$f'(z) = \frac{y^2 - x^2}{(x^2 + y^2)^2} + i\frac{2xy}{(x^2 + y^2)^2} = \frac{y^2 - x^2 + 2ixy}{(x^2 + y^2)^2}$$

Notemos que el numerador es $-(x - iy)^2 = -\bar{z}^2$ y el denominador es $(z\bar{z})^2$:

$$f'(z) = \frac{-\bar{z}^2}{(z\bar{z})^2} = \frac{-\bar{z}^2}{\bar{z}^2 z^2} = -\frac{1}{z^2}$$

#### Conclusión

La derivada $f'(z)$ existe para todo $z \neq 0$ y su valor es:

$$\boxed{f'(z) = -\frac{1}{z^2}}$$

> [!success] Respuesta
> **b) Sí existe $f'(z)$ y su valor es de $-\frac{1}{z^2}$.**

**Referencia:** [[S03-1 Tema 03 - Derivada de una funcion compleja#Ecuacion de Cauchy-Riemann]] y [[S03-1 Tema 03 - Derivada de una funcion compleja#Propiedad 4 Derivada del cociente]]

---

## Ejercicio 5

**Pregunta:** Aplica las propiedades de las derivadas. Determinar la derivada de $f(z) = \frac{z - 1}{2z + 1}$ si $z \neq \frac{1}{2}$.

**Opciones:**
- a) $\dfrac{3}{(2z - 1)^2}$
- b) $-\dfrac{3}{(2z + 1)^2}$
- c) $\dfrac{3}{(2z + 1)^2}$

### Desarrollo

Aplicamos la [[S03-1 Tema 03 - Derivada de una funcion compleja#Propiedad 4 Derivada del cociente|propiedad de la derivada del cociente]].

#### Paso 1: Identificar las funciones

$$f(z) = \frac{h(z)}{g(z)}$$

Donde:
- $h(z) = z - 1 \implies h'(z) = 1$
- $g(z) = 2z + 1 \implies g'(z) = 2$

#### Paso 2: Aplicar la fórmula del cociente

$$f'(z) = \frac{g(z) \cdot h'(z) - h(z) \cdot g'(z)}{[g(z)]^2}$$

$$f'(z) = \frac{(2z + 1)(1) - (z - 1)(2)}{(2z + 1)^2}$$

#### Paso 3: Desarrollar el numerador

$$= \frac{2z + 1 - 2z + 2}{(2z + 1)^2} = \frac{3}{(2z + 1)^2}$$

#### Resultado

$$\boxed{f'(z) = \frac{3}{(2z + 1)^2}}$$

> [!success] Respuesta
> **c) $\dfrac{3}{(2z + 1)^2}$**

**Referencia:** [[S03-1 Tema 03 - Derivada de una funcion compleja#Propiedad 4 Derivada del cociente]] y [[S03-2 Tema 03 - Ejercicio 1 (SyT)]] (ejercicio análogo de derivada de cociente)
