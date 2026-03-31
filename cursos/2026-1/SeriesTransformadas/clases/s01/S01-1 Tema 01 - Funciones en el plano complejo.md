---
title: Numeros complejos y funciones en el plano complejo
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 1
orden: 1
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/numeros-complejos
  - tema/plano-complejo
  - tema/funciones-complejas
date: 2026-03-29
---

## Numeros complejos

### Definicion

Los numeros complejos son un par ordenado de numeros reales $z = (a, b)$, cuyo conjunto se denota por:

$$\mathbb{C} = \{(a, b) \in \mathbb{R}e \mid a \in \mathbb{R}e,\ b \in \mathbb{R}e\}$$

Donde $z$ es representado por una **parte real** ($x = \text{Re}(z)$) y una **parte imaginaria** ($y = \text{Im}(z)$):

$$z = a + bi$$

Donde:
- $a$ = parte real
- $b$ = parte imaginaria
- $i$ = unidad imaginaria

## Representacion de un numero complejo

### Forma binomica

Consideremos $\mathbb{C}$ como un espacio vectorial isomorfo a $\mathbb{R}^2$ y $z = a + ib$. Graficamente podemos representar $\mathbb{R}^2$ ($\mathbb{C}$) como un plano, donde el eje horizontal es el eje real ($\text{Re}$) y el eje vertical es el eje imaginario ($\text{Im}$).

**Modulo** de un numero complejo: se define como el modulo del vector que lo representa:

$$|z| = \sqrt{a^2 + b^2}$$

**Conjugado** de un numero complejo: es el simetrico al eje real, representado por $\bar{z}$:

$$z = a + ib$$

$$\bar{z} = a - ib$$

### Forma polar

Todo numero complejo tambien puede ser representado en forma polar:

$$z = |z|(\cos\theta + i\,\text{sen}\,\theta)$$

Donde:
- $|z| = r$ = modulo
- $a = |z|\cos\theta$ y $b = |z|i\,\text{sen}\,\theta$
- $\theta = \arg(z)$, con $-\pi < \theta < \pi$ (llamado **argumento principal**)

> [!info] Nota
> Un numero complejo tiene infinitos argumentos. Si $\theta_0$ es un valor particular del argumento de $z$, entonces:
> $$\arg(z) = \{\theta_0 + 2k\pi,\ k \in \mathbb{Z}\}$$

### Forma exponencial de Euler

Una variante de la forma polar se obtiene al considerar la **formula de Euler**:

$$e^{i\theta} = \cos\theta + i\,\text{sen}\,\theta$$

Esta formula permite escribir un numero complejo de la siguiente forma:

$$z = |z|\,e^{i\theta}$$

**Formula general:**

$$z = |z|\,e^{i\arg(z)} = |z|\,e^{i(\theta_0 + 2k\pi)}, \quad k \in \mathbb{Z}$$

## Operaciones con numeros complejos

### Forma binomica

Sean $z_1 = (a_1, b_1)$ y $z_2 = (a_2, b_2)$:

**1. Suma y resta binómica:**

$$z_1 + z_2 = (a_1 + a_2,\ b_1 + b_2)$$

**2. Multiplicacion binómica:**

$$z_1 \cdot z_2 = (a_1 a_2 - b_1 b_2,\ b_1 a_2 + a_1 b_2)$$

**3. Division binómica** (con $z_2 \neq 0$):

$$\frac{z_1}{z_2} = \left(\frac{a_1 a_2 + b_1 b_2}{a_2^2 + b_2^2},\ \frac{b_1 a_2 - a_1 b_2}{a_2^2 + b_2^2}\right)$$

### Forma polar-exponencial

Sean $z_1 = |z_1|\,e^{i\theta_1}$ y $z_2 = |z_2|\,e^{i\theta_2}$:

**4. Producto polar-exponencial:**

- $z_1 = |z_1|\left(\cos(\theta_1) + i\,\text{sen}(\theta_1)\right) = |z_1|\,e^{i\theta_1}$
- $z_2 = |z_2|\left(\cos(\theta_2) + i\,\text{sen}(\theta_2)\right) = |z_2|\,e^{i\theta_2}$
$$z_1 \cdot z_2 = |z_1|\,|z_2|\left(\cos(\theta_1 + \theta_2) + i\,\text{sen}(\theta_1 + \theta_2)\right)$$

$$z_1 \cdot z_2 = |z_1|\,|z_2|\,e^{i(\theta_1 + \theta_2)}$$

Generalizacion:

$$z_1 \cdot z_2 \cdots z_n = |z_1|\,|z_2| \cdots |z_n|\,e^{i(\theta_1 + \theta_2 + \cdots + \theta_n)}$$

**5. Potencia polar-exponencial** (sea $n > 0$):

$$z^n = |z|^n\,e^{in\theta} = |z|^n\left(\cos(n\theta) + i\,\text{sen}(n\theta)\right)$$

**6. Cociente polar-exponencial:**

$$\frac{z_1}{z_2} = \frac{|z_1|}{|z_2|}\,e^{i(\theta_1 - \theta_2)} = \frac{|z_1|}{|z_2|}\left(\cos(\theta_1 - \theta_2) + i\,\text{sen}(\theta_1 - \theta_2)\right)$$

**7. Raíces n-esimas polar-exponencial:**

Dado que $z = |z|\,e^{i(\theta_0 + 2k\pi)}$ y definimos $w$ como la raíz $m$ de $z$:

$$w = \sqrt[m]{z} = z^{1/m}, \quad m \in \mathbb{N}$$

Así: $z = w^m$ y $w = |w|\,e^{i\varphi}$, entonces:

$$|z|\,e^{i(\theta_0 + 2k\pi)} = |w|^m\,e^{im\varphi}, \quad \varphi = \frac{\theta_0 + 2k\pi}{m}$$

De la igualdad obtenemos que el numero complejo tiene siempre $m$ raíces m-ésimas:

$$w_k = \sqrt[m]{|z|}\,e^{i\left(\frac{\theta_0 + 2k\pi}{m}\right)}$$

## Funciones de variable compleja

### Definición

Sea $S$ un conjunto de números complejos y una función $f$ definida sobre $S$. Es una regla que asigna a cada $z$ de $S$ un numero del conjunto $w$, tal que:

$$w = f(z) = u(x, y) + iv(x, y)$$

Donde:
- $z$ = variable independiente (dominio)
- $w$ = variable dependiente (rango)
- $u(x, y)$ = parte real de $f(z)$
- $v(x, y)$ = parte imaginaria de $f(z)$

> [!example] Ejemplo
> Sea $w = 2xy - 4 + 2xyi$, se puede representar en funcion de $u(x,y)$ y $iv(x,y)$:
> $$u(x,y) = 2xy - 4$$
> $$v(x,y) = 2xy$$

### Funcion univoca y multivocas

- **Funcion univoca:** si a cada $z$ le corresponde un solo valor de $w$
- **Funcion multivoca:** si a cada $z$ le corresponde mas de un valor de $w$

## Bibliografia

- Churchill, R., & Ward, J. (2004). *Variable Compleja y Aplicaciones* (7ma ed). McGraw-Hill.
- Murray, S., Seymour, Lipschutz, & Dennis, S. (2011). *Variable compleja* (2nd ed). McGraw-Hill Interamericana de Espana S.L.
- Suarez Bueno, V. (1998). *Introduccion a la Variable Compleja* (1a. ed.). Instituto Politecnico Nacional.
