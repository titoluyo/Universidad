---
title: Funciones complejas elementales
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 5
orden: 1
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/funcion-exponencial-compleja
  - tema/funcion-logaritmica-compleja
  - tema/funcion-exponente-complejo
  - tema/funcion-potencia-compleja
  - tema/funcion-trigonometrica-compleja
  - tema/funcion-hiperbolica-compleja
date: 2026-04-26
---

## Introduccion

Las **funciones complejas elementales** son un conjunto de funciones especiales que operan en numeros complejos. Son herramientas fundamentales en el estudio del analisis complejo y tienen aplicaciones en diversos campos de las matematicas y la fisica.

Estas funciones (exponencial, logaritmica, exponente/potencia complejo, trigonometricas e hiperbolicas) tienen propiedades unicas y permiten comprender mejor la estructura y comportamiento de los numeros complejos.

> [!summary] Contenido de la sesion
> 1. **Funcion exponencial** $e^z$ — holomorfa en todo $\mathbb{C}$, periodica de periodo $2\pi i$
> 2. **Funcion logaritmica** $\ln z$ — multivaluada (infinitos valores)
> 3. **Funcion exponente complejo** $\beta^z$ y **funcion potencia** $z^\lambda$
> 4. **Funciones trigonometricas e hiperbolicas** definidas a partir de la exponencial

Material de estudio (manual PDF de la semana): [[Semana05_Man.pdf]]

## 1. Funcion exponencial

La funcion exponencial compleja es **holomorfa en todo el plano cartesiano**.

Sea $z = x + iy$:

$$e^z = e^{x+iy} = e^x \cdot e^{iy} = e^x(\cos y + i\,\text{sen}\,y)$$

Donde:

- $|e^z| = e^x$
- $\arg(e^z) = y + 2k\pi$ para $k = 0, \pm 1, \pm 2, \ldots$

Es ademas **periodica de periodo $2\pi i$**:

$$e^z = e^{z + 2\pi i}$$

> [!note] Conexion con [[S01-1 Tema 01 - Funciones en el plano complejo|forma exponencial de un complejo]]
> La forma exponencial $z = |z|\,e^{i\theta}$ es un caso particular: cualquier complejo se puede escribir asi gracias a la formula de Euler $e^{i\theta} = \cos\theta + i\,\text{sen}\,\theta$.

## 2. Funcion logaritmica

Para $z \in \mathbb{C}$, $z \neq 0$, definimos:

$$\ln z = \{w \in \mathbb{C}\ /\ e^w = z\}$$

Es una **funcion multivaluada**: para un valor determinado de $z$ hay infinitos valores de $w$.

Si $z = r\,e^{i\theta}$, entonces:

$$\ln z = \ln r + i\theta, \quad \theta = \arg(z),\ r = |z|$$

$$\ln z = \ln|z| + i\,\arg(z)$$

Considerando todas las ramas (la indeterminacion del argumento por multiplos de $2\pi$):

$$\ln z = \ln|z| + i(\arg(z) + 2k\pi), \quad k = 0, \pm 1, \pm 2, \ldots$$

Donde:

- $\ln|z|$ es el logaritmo natural real del modulo
- $k = 0$ corresponde a la **rama principal** (valor principal del logaritmo)
- Cada vuelta completa ($k$) genera un valor distinto

## 3. Funcion exponente complejo

Tenemos dos casos segun donde este la variable compleja:

**Funcion exponente** (base $\beta$ constante, exponente variable $z$):

$$\beta^z = e^{z\,\ln\beta}, \quad \beta \neq 0$$

**Funcion potencia** (base variable $z$, exponente $\lambda$ constante):

$$z^\lambda = e^{\lambda\,\ln z}, \quad z \neq 0$$

> [!warning] Multivaluacion heredada
> Como $\ln z$ es multivaluada, ambas funciones $\beta^z$ y $z^\lambda$ tambien son multivaluadas. Para un valor concreto se elige la rama principal salvo indicacion contraria.

## 4. Funciones trigonometricas e hiperbolicas

A partir de la exponencial, se definen:

**Trigonometricas:**

$$\text{sen}\,z = \frac{e^{iz} - e^{-iz}}{2i}, \qquad \cos z = \frac{e^{iz} + e^{-iz}}{2}$$

**Hiperbolicas:**

$$\text{senh}\,z = \frac{e^z - e^{-z}}{2}, \qquad \cosh z = \frac{e^z + e^{-z}}{2}$$

Estas formulas son la generalizacion al plano complejo de las definiciones reales y mantienen las mismas identidades estructurales (e.g. $\text{sen}^2 z + \cos^2 z = 1$, ver [[S05-5 Tema 05 - Ejercicio 4 (SyT)|Ejercicio 4]]).

## Bibliografia

- Churchill, R., & Ward, J. (2004). *Variable Compleja y Aplicaciones* (7ma ed). McGraw-Hill.
- Murray, S., Seymour, Lipschutz, & Dennis, S. (2011). *Variable compleja* (2da ed.). McGraw-Hill Interamericana de Espana S.L.
- Suarez Bueno, V. (1998). *Introduccion a la Variable Compleja* (1a ed.). Instituto Politecnico Nacional.
