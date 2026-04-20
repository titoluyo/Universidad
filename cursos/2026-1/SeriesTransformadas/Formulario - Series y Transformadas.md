---
title: Formulario - Series y Transformadas
curso: "[[SeriesTransformadas MOC]]"
tipo: formulario
tags:
  - curso/series-transformadas
  - tipo/formulario
date: 2026-03-29
---

## Numeros complejos

Fuente: [[S01-1 Tema 01 - Funciones en el plano complejo]]

### Representacion

| Forma | Expresion |
| ----- | --------- |
| Binomica | $z = a + bi$ |
| Polar | $z = \|z\|(\cos\theta + i\,\text{sen}\,\theta)$ |
| Exponencial (Euler) | $z = \|z\|\,e^{i\theta}$ |

### Modulo y conjugado

$$|z| = \sqrt{a^2 + b^2}$$

$$\bar{z} = a - ib$$

### Formula de Euler

$$e^{i\theta} = \cos\theta + i\,\text{sen}\,\theta$$

### Argumento

$$\arg(z) = \{\theta_0 + 2k\pi,\ k \in \mathbb{Z}\}$$

Donde $\theta_0$ es el argumento principal con $-\pi < \theta_0 < \pi$.

### Operaciones en forma binomica

Sean $z_1 = (a_1, b_1)$ y $z_2 = (a_2, b_2)$:

$$z_1 + z_2 = (a_1 + a_2,\ b_1 + b_2)$$

$$z_1 \cdot z_2 = (a_1 a_2 - b_1 b_2,\ b_1 a_2 + a_1 b_2)$$

$$\frac{z_1}{z_2} = \left(\frac{a_1 a_2 + b_1 b_2}{a_2^2 + b_2^2},\ \frac{b_1 a_2 - a_1 b_2}{a_2^2 + b_2^2}\right), \quad z_2 \neq 0$$

### Operaciones en forma polar-exponencial

Sean $z_1 = |z_1|\,e^{i\theta_1}$ y $z_2 = |z_2|\,e^{i\theta_2}$:

$$z_1 \cdot z_2 = |z_1|\,|z_2|\,e^{i(\theta_1 + \theta_2)}$$

$$\frac{z_1}{z_2} = \frac{|z_1|}{|z_2|}\,e^{i(\theta_1 - \theta_2)}$$

$$z^n = |z|^n\,e^{in\theta}$$

### Raices n-esimas

$$w_k = \sqrt[m]{|z|}\,e^{i\left(\frac{\theta_0 + 2k\pi}{m}\right)}, \quad k = 0, 1, \ldots, m-1$$

### Funciones de variable compleja

$$w = f(z) = u(x, y) + iv(x, y)$$

Donde:
- $u(x, y)$ = parte real de $f(z)$
- $v(x, y)$ = parte imaginaria de $f(z)$

## Derivada de una funcion compleja

Fuente: [[S03-1 Tema 03 - Derivada de una funcion compleja]]

### Definicion

$$f'(z) = \lim_{\Delta z \to 0} \frac{f(z + \Delta z) - f(z)}{\Delta z}$$

### Diferencial

$$dw = f'(z)\,dz$$

### Propiedades

| Propiedad | Formula |
| --- | --- |
| Suma | $\frac{d}{dz}\{f(z) + g(z)\} = f'(z) + g'(z)$ |
| Resta | $\frac{d}{dz}\{f(z) - g(z)\} = f'(z) - g'(z)$ |
| Producto | $\frac{d}{dz}\{f(z) \cdot g(z)\} = f(z)\,g'(z) + g(z)\,f'(z)$ |
| Cociente | $\frac{d}{dz}\left\{\frac{f(z)}{g(z)}\right\} = \frac{g(z)\,f'(z) - f(z)\,g'(z)}{g(z)^2}$ |

## Ecuaciones de Cauchy-Riemann

Fuente: [[S03-1 Tema 03 - Derivada de una funcion compleja]]

### Forma cartesiana

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$

### Forma polar

$$\frac{\partial u}{\partial r} = \frac{1}{r}\frac{\partial v}{\partial \theta} \qquad \frac{1}{r}\frac{\partial u}{\partial \theta} = -\frac{\partial v}{\partial r}$$

## Funciones analiticas, holomorfas y armonicas

Fuente: [[S04-1 Tema 04 - Funciones analiticas, holomorfas y armonicas]]

### Clasificacion

| Tipo | Definicion |
| --- | --- |
| Analitica en $S$ abierto | Tiene derivada en todo punto de $S$ y satisface Cauchy-Riemann |
| Holomorfa en $S$ abierto | Tiene derivada en todo punto de $S$ (equivalente a analitica) |
| Singularidad | Punto donde $f$ no es holomorfa |
| Armonica en $D$ | Satisface $\nabla^2 \varphi = 0$ con derivadas continuas de segundo orden |
| Armonica conjugada | $u,v$ armonicas que cumplen Cauchy-Riemann; $v$ es armonica conjugada de $u$ |

### Ecuacion de Laplace (condicion de armonicidad)

Si $f(z) = u(x,y) + i\,v(x,y)$ es analitica en un dominio $D$, entonces $u$ y $v$ son armonicas:

$$\nabla^2 u = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$

$$\nabla^2 v = \frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} = 0$$

### Conjuntos en el plano complejo

| Concepto | Criterio |
| --- | --- |
| Cerrado | Contiene a todos sus puntos limites (ej. $\|z\| \leq 1$) |
| Abierto | Solo contiene puntos interiores (ej. $\|z\| < 1$) |
| Conexo | Todo par de puntos se une por camino poligonal contenido en $S$ |
| Dominio | Conjunto abierto y conexo |
| Vecindad (disco abierto) | $\|z - z_0\| < \rho$ |
| Anillo circular abierto | $\rho_1 < \|z - z_0\| < \rho_2$ |

### Derivada de una funcion analitica

Si $f(z) = u + iv$ es analitica:

$$f'(z) = \frac{\partial u}{\partial x} + i\frac{\partial v}{\partial x} = \frac{\partial v}{\partial y} - i\frac{\partial u}{\partial y}$$

### Metodo para construir la conjugada armonica

Dada $u(x,y)$ armonica en un dominio simplemente conexo:

1. De $u_x = v_y$, integrar respecto a $y$:
$$v(x,y) = \int u_x\, dy + g(x)$$
2. De $u_y = -v_x$, derivar la expresion anterior respecto a $x$ y despejar $g'(x)$.
3. Integrar $g'(x)$ para obtener $g(x)$ (salvo constante).

### Metodo alternativo (integral de linea)

$$v(x,y) = \int_{(x_0, y_0)}^{(x, y)}\left(-u_y\, dx + u_x\, dy\right) + C$$

### Propiedades clave de funciones armonicas

| Propiedad | Enunciado |
| --- | --- |
| Principio del maximo | $u$ armonica no constante en $D$ conexa no alcanza max/min en el interior |
| Unicidad | $u$ armonica en $D$ queda determinada por sus valores en $\partial D$ |
| Valor medio | $u(\text{centro del disco}) = $ promedio de $u$ sobre la circunferencia |
| Ortogonalidad | Si $f = u+iv$ analitica, las curvas $u = c_1$ y $v = c_2$ son ortogonales: $\nabla u \cdot \nabla v = 0$ |
