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

## Funciones complejas elementales

Fuente: [[S05-1 Tema 05 - Funciones complejas elementales]]

### Funcion exponencial

Para $z = x + iy$:

$$e^z = e^x(\cos y + i\,\text{sen}\,y)$$

- $|e^z| = e^x$
- $\arg(e^z) = y + 2k\pi$, $k \in \mathbb{Z}$
- Holomorfa en todo $\mathbb{C}$
- Periodica de periodo $2\pi i$: $e^z = e^{z + 2\pi i}$

### Funcion logaritmica (multivaluada)

$$\ln z = \ln|z| + i(\arg(z) + 2k\pi), \quad k = 0, \pm 1, \pm 2, \ldots$$

- Rama principal: $k = 0$
- Cada vuelta ($k$) da un valor distinto

### Exponente y potencia complejos

| Tipo                                                   | Definicion                              |
| ------------------------------------------------------ | --------------------------------------- |
| **Exponente** (base $\beta$ fija, $z$ variable)        | $\beta^z = e^{z\,\ln \beta},\ \beta \neq 0$ |
| **Potencia** (base $z$ variable, $\lambda$ constante)  | $z^\lambda = e^{\lambda\,\ln z},\ z \neq 0$ |

Ambas heredan la multivaluacion de $\ln$.

### Funciones trigonometricas complejas

$$\text{sen}\,z = \frac{e^{iz} - e^{-iz}}{2i}, \qquad \cos z = \frac{e^{iz} + e^{-iz}}{2}$$

Identidad pitagorica (ver [[S05-5 Tema 05 - Ejercicio 4 (SyT)|demostracion]]):

$$\text{sen}^2 z + \cos^2 z = 1$$

### Funciones hiperbolicas complejas

$$\text{senh}\,z = \frac{e^z - e^{-z}}{2}, \qquad \cosh z = \frac{e^z + e^{-z}}{2}$$

## Integrales de contorno

Fuente: [[S06-1 Tema 06 - Integral de contorno en funciones complejas]]

### Definicion

Si $f(z)$ es continua sobre la curva $C$ desde $A$ hasta $B$:

$$\int_{A}^{B} f(z)\,dz = \lim_{n \to \infty} \sum_{k=1}^{n} f(z_k)\,\Delta z_k$$

### Descomposicion en partes real e imaginaria

Si $f(z) = u(x,y) + i\,v(x,y)$ y $dz = dx + i\,dy$:

$$\int_{C} f(z)\,dz = \int_{C}(u\,dx - v\,dy) + i\int_{C}(v\,dx + u\,dy)$$

### Cambio de variable a parametro $\theta$

Para curvas parametrizadas $z = z(\theta)$:

$$\int_{A}^{B} f(z)\,dz = \int_{\theta_A}^{\theta_B} f(z(\theta))\,\frac{dz}{d\theta}\,d\theta$$

### Casos canonicos

| Curva $C$         | $z(\theta)$              | $dz/d\theta$         |
| ----------------- | ------------------------ | -------------------- |
| $\|z\| = 1$       | $\cos\theta + i\,\text{sen}\,\theta$ | $-\text{sen}\,\theta + i\,\cos\theta$ |
| $\|z\| = r$       | $r\,e^{i\theta}$         | $i\,r\,e^{i\theta}$  |
| Camino horizontal $y = y_0$ | $x + iy_0$, $x: a \to b$ | $dx$ (con $dy = 0$) |
| Camino vertical $x = x_0$   | $x_0 + iy$, $y: a \to b$ | $i\,dy$ (con $dx = 0$) |

### Resultado fundamental

$$\boxed{\oint_{|z|=r} \frac{dz}{z} = 2\pi i}$$

(independiente de $r > 0$, demostrado en [[S06-1 Tema 06 - Integral de contorno en funciones complejas|sesión]] por dos métodos).

## Teorema de Cauchy

Fuente: [[S06-3 Tema 06 - Teorema de Cauchy]]

### Teorema de Green (cálculo vectorial)

$$\oint_{C}\bigl(P\,dx + Q\,dy\bigr) = \iint_{\mathcal{R}}\left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)dx\,dy$$

### Teorema de Cauchy

> Si $f$ es **analítica** en un dominio $\mathcal{R}$ simplemente conexo y $f'$ es continua, entonces para toda trayectoria simple cerrada $C \subset \mathcal{R}$:
>
> $$\oint_{C} f(z)\,dz = 0$$

### Forma integral via Green (derivacion)

$$\int f(z)\,dz = \iint\left(-\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right)dx\,dy + i\iint\left(\frac{\partial u}{\partial x} - \frac{\partial v}{\partial y}\right)dx\,dy$$

Ambos integrandos se anulan por las ecuaciones de Cauchy-Riemann ($u_x = v_y$, $u_y = -v_x$) → $\oint f(z)\,dz = 0$.

### Consecuencias

| Propiedad | Enunciado |
| --- | --- |
| Independencia del camino | $\int_A^B f\,dz$ depende solo de $A, B$ si $f$ analítica |
| Existencia de antiderivada | $\int_A^B f\,dz = F(B) - F(A)$ con $F' = f$ |
| Singularidades | Si $C$ encierra un punto donde $f$ no es analítica, el teorema **no aplica** |

## Teorema de extension de Cauchy

Fuente: [[S06-6 Tema 06 - Teorema de extension de Cauchy]]

### Singularidad

$z_0$ es singularidad de $f$ si $f$ no es analítica en $z_0$ pero sí en al menos un punto de todo entorno de $z_0$.

### Deformacion de contornos

> Si $f$ es analítica en una región y $C_1, C_2$ son dos contornos cerrados simples tales que **$C_1$ se puede deformar continuamente en $C_2$ sin cruzar singularidades**, entonces:
>
> $$\oint_{C_1} f(z)\,dz = \oint_{C_2} f(z)\,dz$$

### Aplicacion: integral de $1/z$ alrededor del origen

Para **cualquier** contorno $C$ que rodee $z = 0$ una vez en sentido antihorario:

$$\oint_{C} \frac{dz}{z} = 2\pi i$$
