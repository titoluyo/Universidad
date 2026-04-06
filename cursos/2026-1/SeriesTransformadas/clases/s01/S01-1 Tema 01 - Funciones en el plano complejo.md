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
- $i$ = unidad imaginaria, donde $i^2 = -1$

### Igualdad de numeros complejos

Dos numeros complejos $z_1 = a_1 + b_1 i$ y $z_2 = a_2 + b_2 i$ son iguales si y solo si:

- $a_1 = a_2$ (partes reales iguales)
- $b_1 = b_2$ (partes imaginarias iguales)

### Numero imaginario puro

Es cualquier numero complejo $z = a + bi$ en el cual $a = 0$ y $b \neq 0$, es decir, de la forma $z = bi$.

## Representacion de un numero complejo

### Forma binomica

Consideremos $\mathbb{C}$ como un espacio vectorial isomorfo a $\mathbb{R}^2$ y $z = a + ib$. Graficamente podemos representar $\mathbb{R}^2$ ($\mathbb{C}$) como un plano, donde el eje horizontal es el eje real ($\text{Re}$) y el eje vertical es el eje imaginario ($\text{Im}$).

**Modulo** de un numero complejo: se define como el modulo del vector que lo representa:

$$|z| = \sqrt{a^2 + b^2}$$

**Conjugado** de un numero complejo: es el simetrico al eje real, representado por $\bar{z}$:

$$z = a + ib$$

$$\bar{z} = a - ib$$

### Propiedades del conjugado

Si $z_1$ y $z_2$ son numeros complejos, se cumplen:

- $\overline{z_1 + z_2} = \bar{z}_1 + \bar{z}_2$
- $\overline{z_1 - z_2} = \bar{z}_1 - \bar{z}_2$
- $\overline{z_1 \cdot z_2} = \bar{z}_1 \cdot \bar{z}_2$
- $\overline{z_1 / z_2} = \bar{z}_1 / \bar{z}_2$, si $z_2 \neq 0$

Ademas, para cualquier numero complejo $z = a + ib$:

- $z \cdot \bar{z} = |z|^2$
- $z + \bar{z} = 2a = 2\,\text{Re}(z)$
- $z - \bar{z} = 2bi = 2i\,\text{Im}(z)$
- $\text{Re}(z) = \dfrac{z + \bar{z}}{2}$
- $\text{Im}(z) = \dfrac{z - \bar{z}}{2i}$

### Propiedades del modulo

Si $z_1, z_2, \ldots, z_m$ son numeros complejos:

- $|z_1 \cdot z_2| = |z_1| \cdot |z_2|$, en general $|z_1 z_2 \cdots z_m| = |z_1||z_2| \cdots |z_m|$
- $\left|\dfrac{z_1}{z_2}\right| = \dfrac{|z_1|}{|z_2|}$, si $z_2 \neq 0$
- $|z_1 + z_2| \leq |z_1| + |z_2|$ (**desigualdad triangular**)
- $|z_1 \pm z_2| \geq \big||z_1| - |z_2|\big|$
- $z \cdot \bar{z} = |z|^2$
- $|z| = |\bar{z}|$

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

**Formula del argumento principal** $\text{Arg}(z)$ (unico valor en $(-\pi, \pi]$):

$$\text{Arg}(z) = \begin{cases} \arctan\left(\dfrac{b}{a}\right) & \text{si } a > 0 \\ \arctan\left(\dfrac{b}{a}\right) + \pi & \text{si } b \geq 0,\ a < 0 \\ \arctan\left(\dfrac{b}{a}\right) - \pi & \text{si } b < 0,\ a < 0 \\ +\dfrac{\pi}{2} & \text{si } b > 0,\ a = 0 \\ -\dfrac{\pi}{2} & \text{si } b < 0,\ a = 0 \end{cases}$$

### Interpretacion geometrica

- $|z|$ = distancia del origen al punto $z$ en el plano complejo
- $\arg(z)$ = angulo desde el eje real positivo hasta el vector $z$
- $|z_1 - z_2|$ = distancia entre los puntos $z_1$ y $z_2$ en el plano complejo

### Forma exponencial de Euler

Una variante de la forma polar se obtiene al considerar la **formula de Euler**:

$$e^{i\theta} = \cos\theta + i\,\text{sen}\,\theta$$

Esta formula permite escribir un numero complejo de la siguiente forma:

$$z = |z|\,e^{i\theta}$$

**Formula general:**

$$z = |z|\,e^{i\arg(z)} = |z|\,e^{i(\theta_0 + 2k\pi)}, \quad k \in \mathbb{Z}$$

## Operaciones con numeros complejos

> [!abstract] Propiedades axiomaticas
> Los numeros complejos forman un **campo** $(\mathbb{C}, +, \cdot)$ que satisface:
> 1. **Cerradura:** $z_1 + z_2 \in \mathbb{C}$ y $z_1 \cdot z_2 \in \mathbb{C}$
> 2. **Conmutativa:** $z_1 + z_2 = z_2 + z_1$, $z_1 \cdot z_2 = z_2 \cdot z_1$
> 3. **Asociativa:** $(z_1 + z_2) + z_3 = z_1 + (z_2 + z_3)$
> 4. **Elemento neutro:** $z + 0 = z$, $z \cdot 1 = z$
> 5. **Elemento inverso:** $z + (-z) = 0$, $z \cdot z^{-1} = 1$ (si $z \neq 0$)
> 6. **Distributiva:** $z_1(z_2 + z_3) = z_1 z_2 + z_1 z_3$

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

### Funcion univoca y multivoca

- **Funcion univoca:** si a cada $z$ le corresponde un solo valor de $w$
- **Funcion multivoca:** si a cada $z$ le corresponde mas de un valor de $w$

### Funciones complejas en coordenadas polares

Si $z = re^{i\theta}$, podemos escribir una funcion $f(z)$ en terminos de coordenadas polares:

$$f(z) = f(re^{i\theta}) = u(r, \theta) + iv(r, \theta)$$

> [!example] Ejemplos
> **1)** Si $f(z) = z^2$:
> $$f(re^{i\theta}) = r^2 e^{i2\theta} = r^2(\cos 2\theta + i\,\text{sen}\,2\theta)$$
> - $u(r, \theta) = r^2 \cos 2\theta$
> - $v(r, \theta) = r^2\,\text{sen}\,2\theta$
>
> **2)** Si $f(z) = 2z - \bar{z}$:
> $$f(re^{i\theta}) = 2re^{i\theta} - re^{-i\theta} = r\cos\theta + i(3r\,\text{sen}\,\theta)$$
> - $u(r, \theta) = r\cos\theta$
> - $v(r, \theta) = 3r\,\text{sen}\,\theta$

### Representacion grafica de una funcion compleja

Las funciones de variable compleja $f(z) = w$ no se pueden graficar directamente (contienen 4 variables reales). En su lugar, se representan como un **mapeo** entre dos planos:

- **Plano $z$** (dominio): se grafican los puntos $z = x + iy$
- **Plano $w$** (rango): se grafican los puntos $w = u + iv = f(z)$

> [!example] Ejemplo: mapeo de $f(z) = z^2$
> Sabemos que $f(x + iy) = (x^2 - y^2) + i(2xy)$. Ubicamos puntos del plano $z$ en el plano $w$:
> - $z_1 = -2 - i \rightarrow w_1 = 3 + 4i$
> - $z_2 = 1 - 2i \rightarrow w_2 = -3 - 4i$
> - $z_3 = 1 + i \rightarrow w_3 = 2i$
> - $z_4 = -1 \rightarrow w_4 = 1$

## Limites y continuidad

### Limite de una funcion compleja

$$\lim_{z \to z_0} f(z) = L$$

si para todo $\varepsilon > 0$, existe $\delta > 0$ tal que:

$$0 < |z - z_0| < \delta \implies |f(z) - L| < \varepsilon$$

### Continuidad

Una funcion $f(z)$ es **continua** en $z_0$ si se cumplen tres condiciones:

1. $f(z_0)$ esta definida
2. $\displaystyle\lim_{z \to z_0} f(z)$ existe
3. $\displaystyle\lim_{z \to z_0} f(z) = f(z_0)$

## Funciones elementales complejas

### Funcion exponencial

$$e^z = e^{x + iy} = e^x(\cos y + i\,\text{sen}\,y)$$

### Funciones trigonometricas

$$\text{sen}\,z = \frac{e^{iz} - e^{-iz}}{2i}, \qquad \cos z = \frac{e^{iz} + e^{-iz}}{2}$$

### Funcion logaritmica

$$\log z = \ln|z| + i(\arg z + 2k\pi), \quad k \in \mathbb{Z}$$

> [!info] Valor principal del logaritmo
> $$\text{Log}\,z = \ln|z| + i\,\text{Arg}(z)$$

## Transformaciones geometricas

Las funciones complejas pueden interpretarse como transformaciones del plano:

| Transformacion | Funcion | Efecto |
| --- | --- | --- |
| Traslacion | $f(z) = z + c$ | Desplaza por el vector $c$ |
| Rotacion | $f(z) = ze^{i\theta}$ | Rota un angulo $\theta$ |
| Escalamiento | $f(z) = rz$ | Escala por factor $r$ |
| Inversion | $f(z) = 1/z$ | Invierte respecto al circulo unitario |

## Regiones en el plano complejo

### Curvas

Una curva en el plano complejo se parametriza como:

$$z(t) = x(t) + iy(t), \quad a \leq t \leq b$$

### Tipos de regiones

- **Region abierta:** no contiene su frontera
- **Region cerrada:** contiene su frontera
- **Region conexa:** cualquier par de puntos puede conectarse por una curva contenida en la region
- **Region simplemente conexa:** no tiene "agujeros" (toda curva cerrada simple puede contraerse a un punto)

## Bibliografia

- Churchill, R., & Ward, J. (2004). *Variable Compleja y Aplicaciones* (7ma ed). McGraw-Hill.
- Murray, S., Seymour, Lipschutz, & Dennis, S. (2011). *Variable compleja* (2nd ed). McGraw-Hill Interamericana de Espana S.L.
- Suarez Bueno, V. (1998). *Introduccion a la Variable Compleja* (1a. ed.). Instituto Politecnico Nacional.
