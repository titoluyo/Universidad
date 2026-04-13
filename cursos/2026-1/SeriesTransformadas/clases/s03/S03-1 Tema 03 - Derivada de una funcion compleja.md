---
title: Derivada de una funcion compleja
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 3
orden: 1
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/derivada-compleja
  - tema/cauchy-riemann
date: 2026-04-12
---

## Definicion de la derivada de una funcion compleja

- Sea $f$ una funcion univoca en alguna region $\mathbb{R}$ del plano $z$, la derivada de $f(z)$ se define como:

$$f'(z) = \lim_{\Delta z \to 0} \frac{f(z + \Delta z) - f(z)}{\Delta z} \quad (1)$$

- Si el limite existe independientemente de la manera como $\Delta z \to 0$, en tal caso decimos que $f(z)$ es diferenciable en $z$.

## Diferenciales

- Si $\Delta z = dz$ un incremento dado a $z$. Entonces:

$$\Delta w = f(z + \Delta z) - f(z) \quad (2)$$

- Es llamado el incremento en $w = f(z)$.

Si $f(z)$ es continua y su primera derivada es continua, entonces:

$$dw = f'(z)\,dz$$

> [!info] Relacion entre (1) y (2)
> Debido a la definicion (1) y (2), podemos escribir:
> $$\frac{dw}{dz} = f'(z) = \lim_{\Delta z \to 0} \frac{f(z + \Delta z) - f(z)}{\Delta z} \quad (3)$$

## Propiedades de las derivadas de una funcion compleja

### Propiedad 1: Derivada de la suma

$$\frac{d}{dz}\{f(z) + g(z)\} = \frac{d}{dz}f(z) + \frac{d}{dz}g(z) = f'(z) + g'(z)$$

> [!example] Ejemplo
> Sea $f(z) = 1 + z^2$ y $g(z) = 1 - z$. Determinar la $\frac{d}{dz}\{f(z) + g(z)\}$.
>
> $$\frac{d}{dz}\{f(z) + g(z)\} = f'(z) + g'(z) = (2z) + (-1) = 2z - 1$$

### Propiedad 2: Derivada de la resta

$$\frac{d}{dz}\{f(z) - g(z)\} = \frac{d}{dz}f(z) - \frac{d}{dz}g(z) = f'(z) - g'(z)$$

> [!example] Ejemplo
> Sea $f(z) = 1 + z^2$ y $g(z) = 1 - z$. Determinar la $\frac{d}{dz}\{f(z) - g(z)\}$.
>
> $$\frac{d}{dz}\{f(z) - g(z)\} = f'(z) - g'(z) = (2z) + (-1) = 2z + 1$$

### Propiedad 3: Derivada del producto

$$\frac{d}{dz}\{f(z) \cdot g(z)\} = f(z) \cdot \frac{d}{dz}g(z) + g(z) \cdot \frac{d}{dz}f(z) = f(z)\,g'(z) + g(z)\,f'(z)$$

> [!example] Ejemplo
> Sea $f(z) = 1 + z^2$ y $g(z) = 1 - z$. Determinar la $\frac{d}{dz}\{f(z) \cdot g(z)\}$.
>
> $$\frac{d}{dz}\{f(z) \cdot g(z)\} = f(z)\,g'(z) + g(z)\,f'(z)$$
> $$= (1 + z^2)(-1) + (1 - z)(2z) = -1 + z^2 + 2z - 2z^2$$
> $$= -z^2 + 2z - 1$$

### Propiedad 4: Derivada del cociente

$$\frac{d}{dz}\left\{\frac{f(z)}{g(z)}\right\} = \frac{g(z) \cdot \frac{d}{dz}f(z) - f(z) \cdot \frac{d}{dz}g(z)}{g(z)^2} = \frac{g(z)\,f'(z) - f(z)\,g'(z)}{g(z)^2}$$

> [!example] Ejemplo
> Sea $f(z) = 1 + z^2$ y $g(z) = 1 - z$. Determinar la $\frac{d}{dz}\left\{\frac{f(z)}{g(z)}\right\}$.
>
> $$\frac{d}{dz}\left\{\frac{f(z)}{g(z)}\right\} = \frac{g(z)\,f'(z) - f(z)\,g'(z)}{g(z)^2} = \frac{(1 - z)(2z) - (1 + z^2)(-1)}{(1 - z)^2}$$
> $$= \frac{2z - z^2 + 1 - z^2}{(1 - z)^2} = \frac{-2z^2 + 2z + 1}{(1 - z)^2}$$

## Tabla de derivadas fundamentales

> [!note] Nota
> $u$ y $v$ representan, cada una, una expresion en funcion de $x$.

### Propiedades basicas

| Propiedad | Propiedad |
| --- | --- |
| $y = ku \implies y' = ku', \; k \in \mathbb{R}$ | $y = u \pm v \implies y' = u' \pm v'$ |
| $y = u \cdot v \implies y' = u'v + uv'$ | $y = \dfrac{u}{v} \implies y' = \dfrac{u'v - v'u}{v^2}$ |

### Constante e identidad

| Funcion | Derivada | Ejemplo | Ejemplo derivada |
| --- | --- | --- | --- |
| $y = k$ | $y' = 0$ | $y = 5$ | $y' = 0$ |
| $y = x$ | $y' = 1$ | $y = 4x$ | $y' = 4$ |

### Potenciales

| Funcion | Derivada | Ejemplo | Ejemplo derivada |
| --- | --- | --- | --- |
| $y = u^n$ | $y' = nu^{n-1}u'$ | $y = (2x+7)^4$ | $y' = 8(2x+7)^3$ |
| $y = \sqrt{u}$ | $y' = \dfrac{u'}{2\sqrt{u}}$ | $y = \sqrt{3x}$ | $y' = \dfrac{3}{2\sqrt{3x}}$ |
| $y = \sqrt[n]{u}$ | $y' = \dfrac{u'}{n\sqrt[n]{u^{n-1}}}$ | $y = \sqrt[4]{7x}$ | $y' = \dfrac{7}{4\sqrt[4]{(7x)^3}}$ |

### Exponenciales

| Funcion | Derivada | Ejemplo | Ejemplo derivada |
| --- | --- | --- | --- |
| $y = e^u$ | $y' = u'e^u$ | $y = e^{4x+5}$ | $y' = 4e^{4x+5}$ |
| $y = a^u$ | $y' = u'a^u \ln a$ | $y = 3^{7x-5}$ | $y' = 7 \cdot 3^{7x-5} \ln 3$ |

### Logaritmicas

| Funcion | Derivada | Ejemplo | Ejemplo derivada |
| --- | --- | --- | --- |
| $y = \ln u$ | $y' = \dfrac{u'}{u}$ | $y = \ln(2x+7)$ | $y' = \dfrac{2}{2x+7}$ |
| $y = \log_a u$ | $y' = \dfrac{u'}{u} \log_a e = \dfrac{u'}{u \ln a}$ | $y = \log_2(3x+4)$ | $y' = \dfrac{3}{3x+4} \cdot \dfrac{1}{\ln 2}$ |

### Trigonometricas

| Funcion | Derivada |
| --- | --- |
| $y = \operatorname{sen} u$ | $y' = u' \cos u$ |
| $y = \cos u$ | $y' = -u' \operatorname{sen} u$ |
| $y = \operatorname{tg} u$ | $y' = \dfrac{u'}{\cos^2 u} = u'(1 + \operatorname{tg}^2 u)$ |
| $y = \operatorname{cotg} u$ | $y' = -\dfrac{u'}{\operatorname{sen}^2 u} = -u'(1 + \operatorname{cotg}^2 u)$ |
| $y = \sec u$ | $y' = u' \sec u \operatorname{tg} u$ |
| $y = \csc u$ | $y' = -u' \csc u \operatorname{cotg} u$ |

### Trigonometricas inversas

| Funcion | Derivada |
| --- | --- |
| $y = \arcsin u$ | $y' = \dfrac{u'}{\sqrt{1 - u^2}}$ |
| $y = \arccos u$ | $y' = -\dfrac{u'}{\sqrt{1 - u^2}}$ |
| $y = \operatorname{arctg} u$ | $y' = \dfrac{u'}{1 + u^2}$ |

## Ecuacion de Cauchy-Riemann

### Definicion

Las ecuaciones de Cauchy-Riemann son un par de ecuaciones que deben satisfacer las primeras derivadas parciales de las funciones componentes $u$ y $v$ de una funcion.

Sea:

$$f(z) = u(x,y) + iv(x,y) \quad (4)$$

Evaluemos la derivada de $f(z)$ mediante limites, donde $z_0 = x_0 + iy_0$. Asi tenemos:

$$f'(z_0) = \frac{\partial}{\partial x}u(x_0, y_0) - i\frac{\partial}{\partial x}v(x_0, y_0) \quad (5)$$

$$f'(z_0) = i\frac{\partial}{\partial y}u(x_0, y_0) + \frac{\partial}{\partial y}v(x_0, y_0) \quad (6)$$

Igualando la parte real e imaginaria de (5) y (6), tenemos:

$$\frac{\partial}{\partial x}u(x_0, y_0) = \frac{\partial}{\partial y}v(x_0, y_0) \quad (7)$$

$$\frac{\partial}{\partial y}u(x_0, y_0) = -\frac{\partial}{\partial x}v(x_0, y_0) \quad (8)$$

Las ecuaciones (7) y (8) son las **ecuaciones de Cauchy-Riemann**, estas ecuaciones son condiciones necesarias para la existencia de la derivada de una funcion $f$ en el punto $z_0$.

Estas ecuaciones suelen utilizarse para localizar puntos en los que $f$ no admite derivada.

### Teorema 1: Forma cartesiana

Sea:

$$f(z) = u(x,y) + iv(x,y) \quad (4)$$

Definida en algun $\varepsilon$ entorno de un punto $z_0 = x_0 + iy_0$. Supongamos que las derivadas parciales de primer orden de las funciones $u$ y $v$ con respecto a $x$ e $y$ existen en todos los puntos de ese entorno y son continuas en $(x_0, y_0)$. Entonces, esas derivadas parciales satisfacen las ecuaciones de Cauchy-Riemann:

$$\frac{\partial}{\partial x}u(x_0, y_0) = \frac{\partial}{\partial y}v(x_0, y_0) \quad (7)$$

$$\frac{\partial}{\partial y}u(x_0, y_0) = -\frac{\partial}{\partial x}v(x_0, y_0) \quad (8)$$

En $(x_0, y_0)$ la derivada $f'(z_0)$ existe.

### Teorema 2: Forma polar

Sea:

$$f(z) = u(r, \theta) + iv(r, \theta) \quad (9)$$

Definida en algun $\varepsilon$ entorno de un punto no nulo $z_0 = r_0 \exp(i\theta)$. Supongamos que las primeras derivadas parciales de las funciones $u$ y $v$ con respecto a $r$ y $\theta$ existen en todos los puntos de ese entorno y son continuas en $(r_0, \theta_0)$. Entonces, si esas derivadas parciales satisfacen las ecuaciones de Cauchy-Riemann:

$$\frac{\partial}{\partial r}u(r_0, \theta_0) = \frac{1}{r}\frac{\partial}{\partial \theta}v(r_0, \theta_0) \quad (10)$$

$$\frac{1}{r}\frac{\partial}{\partial \theta}u(r_0, \theta_0) = -\frac{\partial}{\partial r}v(r_0, \theta_0) \quad (11)$$

En $(r_0, \theta_0)$ la derivada $f'(z_0)$ existe.

## Bibliografia

- Churchill, R., & Ward, J. (2004). *Variable Compleja y Aplicaciones* (7ma ed). McGraw-Hill.
- Murray, S., Seymour, Lipschutz, & Dennis, S. (2011). *Variable compleja* (2nd ed). McGraw-Hill Interamericana de Espana S.L.
- Suarez Bueno, V. (1998). *Introduccion a la Variable Compleja* (1a. ed.). Instituto Politecnico Nacional.
