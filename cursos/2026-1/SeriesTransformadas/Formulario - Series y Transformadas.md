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

## Formula integral de Cauchy

Fuente: [[S07-0 Tema 01 - Relacion del teorema de Cauchy y una integral]]

### Formula simple (singularidad de orden 1)

Sea $f(z)$ analítica dentro y sobre el contorno cerrado simple $C$, y sea $z_0$ un punto interior a $C$:

$$\oint_C \frac{f(z)}{z - z_0}\,dz = 2\pi i\,f(z_0)$$

### Formula generalizada (derivadas de funciones analiticas)

Para singularidades de orden $n+1$ (polo de orden $n+1$):

$$\oint_C \frac{f(z)}{(z - z_0)^{n+1}}\,dz = \frac{2\pi i}{n!}\,f^{(n)}(z_0), \quad n = 0, 1, 2, \ldots$$

Donde:
- $n$ es el orden de la derivada de $f$.
- $f^{(n)}(z_0)$ es la derivada $n$-ésima evaluada en $z_0$.
- Para $n = 0$ se recupera la fórmula simple.

### Procedimiento operativo

1. Identificar singularidades: $h(z) = 0$ (denominador).
2. Verificar cuáles están dentro de $C$ (las de fuera no contribuyen — Teorema de Cauchy puro).
3. Aislar el factor $(z - z_0)^{n+1}$ → leer $f(z)$ del resto del integrando y deducir $n$.
4. Calcular $f^{(n)}(z_0)$ y aplicar la fórmula.
5. Sumar contribuciones si hay varias singularidades interiores.

### Truco: factor lineal con coeficiente

Si el factor es $(az + b)$ con $a \neq 1$:

$$az + b = a\left(z + \tfrac{b}{a}\right) = a\left(z - z_0\right), \quad z_0 = -\tfrac{b}{a}$$

Sacar el $1/a$ al integrando antes de aplicar la fórmula.

Fuente: [[S07-1 Tema 01 - Aplicacion Caso 1 - integral con factor lineal]]

### Truco: fracciones parciales para varias singularidades simples

$$\frac{1}{(z - z_1)(z - z_2)} = \frac{1}{z_1 - z_2}\left(\frac{1}{z - z_1} - \frac{1}{z - z_2}\right)$$

Fuente: [[S07-3 Tema 01 - Aplicacion Caso 3 - fracciones parciales]]

### Derivadas utiles para la formula generalizada

Para $f(z) = e^{az}$: $f^{(n)}(z) = a^n e^{az}$.

Fuente: [[S07-4 Tema 01 - Aplicacion Caso 4 - formula generalizada e2z]]

## Series de potencias en complejos

Fuente: [[S08-0 Tema 01 - Series de potencias en complejos]]

### Forma general

$$y = \sum_{n=0}^{\infty} a_n\,(z - z_0)^n$$

Donde $a_n \in \mathbb{C}$ son los coeficientes y $z_0$ es el centro de la serie.

### Convergencia absoluta

Si $\sum_{n=1}^\infty |u_n|$ converge, entonces $\sum_{n=1}^\infty u_n$ converge. La implicación inversa no se cumple en general.

### Criterio del cociente (D'Alembert)

$$L = \lim_{n \to \infty}\left|\frac{u_{n+1}}{u_n}\right|$$

- $L < 1$ → converge absolutamente
- $L > 1$ → diverge
- $L = 1$ → no decide

### Radio de convergencia

Para $\sum a_n (z - z_0)^n$, separando $|z - z_0|$ del límite:

$$\lambda = \lim_{n \to \infty}\left|\frac{a_{n+1}}{a_n}\right| \qquad \Longrightarrow \qquad \boxed{R = \frac{1}{\lambda}}$$

Converge en el disco abierto $|z - z_0| < R$.

| $\lambda$ | $R$ | Región |
| --------- | --- | ------ |
| $0$ | $\infty$ | Todo $\mathbb{C}$ |
| Finito $> 0$ | $1/\lambda$ | Disco $\|z - z_0\| < R$ |
| $\infty$ | $0$ | Solo $z = z_0$ |

### Series notables (radio de convergencia $\infty$)

| Función | Serie de Maclaurin | Fuente |
| ------- | ------------------ | ------ |
| $e^z$ | $\sum_{n=0}^\infty \dfrac{z^n}{n!}$ | — |
| $\sin z$ | $\sum_{n=1}^\infty \dfrac{(-1)^{n-1}\,z^{2n-1}}{(2n-1)!}$ | [[S08-2 Tema 01 - Convergencia Ej2 - serie del seno]] |
| $\cos z$ | $\sum_{n=0}^\infty \dfrac{(-1)^n\,z^{2n}}{(2n)!}$ | — |

### Serie geométrica (radio de convergencia $1$)

$$\sum_{n=0}^\infty z^n = \frac{1}{1 - z}, \quad |z| < 1$$

Derivadas útiles:

$$\sum_{n=1}^\infty n\,z^{n-1} = \frac{1}{(1-z)^2}, \quad \sum_{n=1}^\infty n(n+1)\,z^n = \frac{2z}{(1-z)^3}$$

Fuente: [[S08-4 Tema 01 - Convergencia Ej4 - polinomial n(n+1)]]

### Procedimiento operativo

1. Escribir $C_n$ del término general.
2. Construir $C_{n+1}$ sustituyendo $n \mapsto n+1$.
3. Formar el cociente $|C_{n+1}/C_n|$ y simplificar (cancelando factoriales y potencias).
4. Sacar $|z - z_0|^k$ fuera del límite (no depende de $n$).
5. Calcular $\lambda$ (límite del cociente de coeficientes solamente).
6. $R = 1/\lambda$ define la región de convergencia.

## Series de Taylor en números complejos

Fuente: [[S09-0 Tema 01 - Series de Taylor en numeros complejos]]

### Fórmula de Taylor

Si $f(z)$ es analítica en el disco $|z - z_0| < R$:

$$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(z_0)}{n!}\,(z - z_0)^n$$

### Serie de Maclaurin (caso $z_0 = 0$)

$$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}\,z^n$$

### Series de Maclaurin notables

| Función | Serie | $R$ |
| ------- | ----- | --- |
| $e^z$ | $\displaystyle\sum_{n=0}^\infty \frac{z^n}{n!}$ | $\infty$ |
| $\sin z$ | $\displaystyle\sum_{n=1}^\infty \frac{(-1)^{n-1}\,z^{2n-1}}{(2n-1)!}$ | $\infty$ |
| $\cos z$ | $\displaystyle\sum_{n=0}^\infty \frac{(-1)^n\,z^{2n}}{(2n)!}$ | $\infty$ |
| $\dfrac{1}{1 - z}$ | $\displaystyle\sum_{n=0}^\infty z^n$ | $1$ |
| $\ln(1 + z)$ | $\displaystyle\sum_{n=1}^\infty \frac{(-1)^{n-1}\,z^n}{n}$ | $1$ |
| $\ln(1 - z)$ | $\displaystyle -\sum_{n=1}^\infty \frac{z^n}{n}$ | $1$ |
| $\ln\!\left(\dfrac{1+z}{1-z}\right) = 2\,\text{arctanh}\,z$ | $\displaystyle 2\sum_{n=1}^\infty \frac{z^{2n-1}}{2n-1}$ | $1$ |

Fuentes: [[S09-1 Tema 01 - Taylor Ej1 - logaritmo neperiano de (1+z)]], [[S09-2 Tema 01 - Taylor Ej2 - logaritmo de (1+z) sobre (1-z)]]

### Identidades para reordenar series

- $\ln\!\left(\dfrac{a}{b}\right) = \ln a - \ln b$ → permite reducir series compuestas a partes conocidas.
- $\ln(1 - z) = \ln(1 + (-z))$ → sustitución $z \mapsto -z$ en la serie de $\ln(1+z)$.
- $\sin(a + b) = \sin a \cos b + \cos a \sin b$ → atajo para Taylor de $\sin z$ alrededor de $z_0 = a$.

### Patrones cíclicos de derivadas

Para funciones trigonométricas las derivadas se repiten con período 4:

| $f$ | $f'$ | $f''$ | $f'''$ | $f^{(4)}$ |
| --- | ---- | ----- | ------ | --------- |
| $\sin z$ | $\cos z$ | $-\sin z$ | $-\cos z$ | $\sin z$ |
| $\cos z$ | $-\sin z$ | $-\cos z$ | $\sin z$ | $\cos z$ |

Fuente: [[S09-3 Tema 01 - Taylor Ej3 - sen(z) alrededor de pi cuartos]]

### Procedimiento Taylor

1. Identificar $f(z)$ y centro $z_0$.
2. Calcular derivadas sucesivas y evaluarlas en $z_0$.
3. Construir $a_n = f^{(n)}(z_0)/n!$ y simplificar.
4. Identificar patrón (signos, factoriales que se cancelan) y escribir sumatoria compacta.
5. Calcular $R$ (distancia desde $z_0$ a la singularidad más cercana).

### Radio de convergencia y singularidades

> El radio de convergencia $R$ de una serie de Taylor centrada en $z_0$ es la distancia desde $z_0$ a la **singularidad más cercana** de $f$.

Ejemplos:
- $\ln(1+z)$ centrada en $0$ → singular en $z = -1$ → $R = 1$.
- $\dfrac{1}{1-z}$ centrada en $0$ → singular en $z = 1$ → $R = 1$.
- $\sin z$, $\cos z$, $e^z$ → enteras → $R = \infty$ para cualquier $z_0$.

## Series de Laurent

Fuente: [[S10-0 Tema 01 - Series de Maclaurin y Laurent]]

### Teorema de Laurent

Si $f$ es analítica en el anillo $R_1 < |z - z_0| < R_2$ (pero no necesariamente en $z_0$) y $C$ es un contorno cerrado simple orientado positivamente en torno de $z_0$ dentro del anillo:

$$f(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n + \sum_{n=1}^{\infty} \frac{b_n}{(z - z_0)^n} \qquad (R_1 < |z - z_0| < R_2)$$

$$a_n = \frac{1}{2\pi i}\oint_C \frac{f(z)\,dz}{(z - z_0)^{n+1}}, \qquad b_n = \frac{1}{2\pi i}\oint_C \frac{f(z)\,dz}{(z - z_0)^{-n+1}}$$

- Parte analítica: $\sum a_n (z-z_0)^n$ (potencias $\geq 0$).
- Parte principal: $\sum b_n (z-z_0)^{-n}$ (potencias negativas; delata la singularidad).

### Forma compacta

$$f(z) = \sum_{n=-\infty}^{\infty} c_n (z - z_0)^n, \qquad c_n = \frac{1}{2\pi i}\oint_C \frac{f(z)\,dz}{(z - z_0)^{n+1}}, \quad n = 0, \pm 1, \pm 2, \ldots$$

### Serie geométrica como herramienta de expansión

$$\frac{1}{1 - w} = \sum_{n=0}^{\infty} w^n, \quad |w| < 1$$

Según el anillo, se elige qué factorizar:

| Condición del anillo | Reescritura | Tipo de potencias |
| -------------------- | ----------- | ----------------- |
| $\|z\| > r$ (exterior de $\|z\|=r$) | $\dfrac{1}{z-r}=\dfrac1z\cdot\dfrac{1}{1-r/z}$ (factorizar $z$) | negativas (parte principal) |
| $\|z\| < r$ (interior de $\|z\|=r$) | $\dfrac{1}{z-r}=-\dfrac1r\cdot\dfrac{1}{1-z/r}$ (factorizar $r$) | positivas (parte analítica) |

Fuente: [[S10-2 Tema 01 - Laurent Ej2 - region anular -1 sobre (z-1)(z-2)]]

### Integrales de contorno vía Laurent (residuo)

El coeficiente $c_{-1}$ (término en $(z-z_0)^{-1}$) es el **residuo** de $f$ en $z_0$. Como $\oint_C (z-z_0)^k\,dz = 0$ para $k \neq -1$ y $\oint_C \dfrac{dz}{z-z_0} = 2\pi i$:

$$\boxed{\oint_C f(z)\,dz = 2\pi i\,c_{-1} = 2\pi i\sum_{\text{polos interiores}}\operatorname{Res}_{z_k} f}$$

Residuo en un polo simple:

$$\operatorname{Res}_{z_0} f = \lim_{z \to z_0}(z - z_0)\,f(z)$$

Solo contribuyen las singularidades **dentro** del contorno (las de fuera dan integral nula).

Fuentes: [[S10-3 Tema 01 - Integral Ej3 - 5z-2 sobre z(z-1)]], [[S10-4 Tema 01 - Integral Ej4 - (z+1) sobre (z2-2z)]]

### Procedimiento Laurent

1. Identificar singularidades ($h(z)=0$) y graficar los círculos.
2. Elegir el **anillo** de trabajo (región pedida).
3. Descomponer en fracciones parciales si hay varios factores.
4. Forzar la forma $\dfrac{1}{1-w}$ en cada término según la condición del anillo.
5. Expandir y reunir potencias positivas y negativas.
6. Para integrales: quedarse con el coeficiente de $(z-z_0)^{-1}$ y multiplicar por $2\pi i$ (sumando singularidades interiores).

## Señales periódicas, pares e impares

Fuente: [[S11-0 Tema 01 - Senales periodicas, pares e impares]]

### Periodicidad

$$f(t) = f(t + T) \qquad (T = \text{periodo mínimo})$$

Para una **suma de armónicos**, el periodo total es el menor $T$ múltiplo entero simultáneo de cada periodo individual.

### Paridad

| Tipo | Condición | Simetría | Ejemplo |
| ---- | --------- | -------- | ------- |
| Par | $f(-t) = f(t)$ | eje vertical | $\cos$ |
| Impar | $f(-t) = -f(t)$ | origen | $\sin$ |

### Propiedades

- par × par = par; impar × impar = par; **par × impar = impar**.
- Toda $f(t)$ se descompone en una parte par y una impar.
- Integral en intervalo simétrico:

$$\int_{-a}^{a} f(t)\,dt = 2\int_0^a f(t)\,dt \;\;(f\text{ par}); \qquad \int_{-a}^{a} f(t)\,dt = 0 \;\;(f\text{ impar})$$

## Series de Fourier

Fuente: [[S11-2 Tema 02 - Series de Fourier]]

### Serie trigonométrica

$$f(t) = \frac{1}{2}a_0 + \sum_{n=1}^{\infty}\bigl(a_n\cos n\omega t + b_n\sin n\omega t\bigr), \qquad \omega = \frac{2\pi}{T}$$

### Coeficientes (vía ortogonalidad)

$$a_0 = \frac{2}{T}\int_{-T/2}^{T/2} f(t)\,dt$$

$$a_n = \frac{2}{T}\int_{-T/2}^{T/2} f(t)\cos(n\omega t)\,dt, \qquad n = 0, 1, 2, \ldots$$

$$b_n = \frac{2}{T}\int_{-T/2}^{T/2} f(t)\sin(n\omega t)\,dt, \qquad n = 1, 2, 3, \ldots$$

- $\tfrac{1}{2}a_0$ = valor promedio (componente DC) de la señal.
- $\omega = 2\pi/T$ = frecuencia angular fundamental.

### Atajo por paridad

| Si $f$ es… | Se anula | Serie resultante |
| ---------- | -------- | ---------------- |
| **par** | $b_n = 0$ | solo cosenos |
| **impar** | $a_0 = a_n = 0$ | solo senos |

### Relaciones de ortogonalidad ($\omega = 2\pi/T$)

$$\int_{-T/2}^{T/2}\cos(m\omega t)\cos(n\omega t)\,dt = \int_{-T/2}^{T/2}\sin(m\omega t)\sin(n\omega t)\,dt = \begin{cases}0, & m\neq n\\ T/2, & m=n\end{cases}$$

$$\int_{-T/2}^{T/2}\sin(m\omega t)\cos(n\omega t)\,dt = 0 \quad \forall\, m,n$$

### Resultados notables

| Señal (impar, periodo $T$) | Coeficiente | Serie | Fuente |
| -------------------------- | ----------- | ----- | ------ |
| Onda cuadrada ($\pm1$) | $b_n = \dfrac{2}{n\pi}(1-(-1)^n) = \dfrac{4}{n\pi}$ (impares) | $\dfrac{4}{\pi}\sum_{n\,\text{impar}}\dfrac{1}{n}\sin n\omega t$ | [[S11-3 Tema 02 - Series de Fourier Ejercicio 1 - onda cuadrada]] |
| Onda triangular (altura $k$) | $b_n = \dfrac{8k}{(n\pi)^2}\sin\dfrac{n\pi}{2}$ | $\dfrac{8k}{\pi^2}\left(\sin\tfrac{\pi}{L}t - \tfrac{1}{9}\sin\tfrac{3\pi}{L}t + \cdots\right)$ | [[S11-4 Tema 02 - Series de Fourier Ejercicio 2 - onda triangular]] |

> Las amplitudes decaen como $1/n$ (señal discontinua: cuadrada) o $1/n^2$ (señal continua: triangular): a mayor suavidad, decaimiento más rápido.

## Series de Fourier de medio rango

Fuente: [[S12-0 Tema 01 - Analisis de las series de Fourier]]

Para una función definida solo en $(0, \tau)$, se extiende a periodo $T = 2\tau$ y se desarrolla con **solo senos** o **solo cosenos**:

| Extensión | Serie | Coeficiente |
| --------- | ----- | ----------- |
| **Par** (cosenos) | $f(t) = \dfrac{1}{2}a_0 + \sum_{n=1}^{\infty} a_n\cos\dfrac{n\pi t}{\tau}$ | $a_n = \dfrac{2}{\tau}\displaystyle\int_0^{\tau} f(t)\cos\dfrac{n\pi t}{\tau}\,dt$ |
| **Impar** (senos) | $f(t) = \sum_{n=1}^{\infty} b_n\sin\dfrac{n\pi t}{\tau}$ | $b_n = \dfrac{2}{\tau}\displaystyle\int_0^{\tau} f(t)\sin\dfrac{n\pi t}{\tau}\,dt$ |

Fuente del ejercicio en cosenos: [[S12-1 Tema 01 - Ejercicio 1 - serie por expansion del coseno]]

## Error cuadrático medio (aproximaciones finitas)

Fuente: [[S12-0 Tema 01 - Analisis de las series de Fourier]]

**Suma parcial** ($2k+1$ términos):

$$S_k = \frac{1}{2}a_0 + \sum_{n=1}^{k}\bigl(a_n\cos n\omega t + b_n\sin n\omega t\bigr)$$

**Error** $\varepsilon_k(t) = f(t) - S_k(t)$, y el **error cuadrático medio**:

$$E_k = \frac{1}{T}\int_{-T/2}^{T/2}\bigl[f(t) - S_k(t)\bigr]^2 dt$$

> [!success] Forma reducida (Parseval truncada)
> $$E_k = \frac{1}{T}\int_{-T/2}^{T/2}\bigl[f(t)\bigr]^2 dt - \frac{a_0^2}{4} - \frac{1}{2}\sum_{n=1}^{k}\bigl(a_n^2 + b_n^2\bigr)$$

- $\frac{1}{T}\int[f(t)]^2 dt$ = potencia media (valor cuadrático medio) de la señal.
- El término sustraído = potencia capturada por los $k$ armónicos. $E_k$ = potencia residual.

| Señal | $E_5$ | Comentario |
| ----- | ----- | ---------- |
| $f(t)=t$ en $(-\pi,\pi)$ (discontinua) | $\approx 0.363$ | converge lento (Gibbs) |
| $A\lvert\sin\omega_0 t\rvert$ (continua) | $\approx 1.22\times10^{-4}A^2$ | converge muy rápido |

Fuentes: [[S12-2 Tema 01 - Ejercicio 2 - error cuadratico de f(t) = t]], [[S12-3 Tema 01 - Ejercicio 3 - error cuadratico seno rectificado]]

### Fenómeno de Gibbs

Sobreoscilación (≈ 9 % del salto) cerca de una **discontinuidad** al usar sumas parciales; persiste sin importar el número de términos (se comprime hacia la discontinuidad), pero su energía (error cuadrático) tiende a cero. Solo aparece en señales **discontinuas**.

## Teorema de Parseval

Fuente: [[S13-0 Tema 01 - Teorema de Parseval]]

> [!summary] Identidad de Parseval (señales periódicas)
> $$\frac{1}{T}\int_{-T/2}^{T/2}\bigl[f(t)\bigr]^2 dt = \frac{a_0^2}{4} + \frac{1}{2}\sum_{n=1}^{\infty}\bigl(a_n^2 + b_n^2\bigr)$$

- Lado izquierdo = **potencia promedio** (valor cuadrático medio) de la señal.
- $\dfrac{a_0^2}{4}$ = potencia DC; $\dfrac{1}{2}(a_n^2+b_n^2)$ = potencia del $n$-ésimo armónico.
- Se deduce del error cuadrático medio: como $E_k \geq 0$ es no creciente y $\lim E_k = 0$, queda la igualdad.

### Aplicación: sumar series numéricas

Expandir $f$ en Fourier (usar paridad) → aplicar Parseval → calcular $\frac{1}{T}\int[f]^2 dt$ y despejar.

| Función (periodo) | Serie probada | Valor |
| ----------------- | ------------- | ----- |
| $f(x)=x$, $(-\pi,\pi)$ (impar) | $\displaystyle\sum_{n=1}^\infty \dfrac{1}{n^2}$ | $\dfrac{\pi^2}{6}$ |
| $f(x)=1+\lvert x\rvert$, $(-1,1)$ (par) | $\displaystyle\sum_{n=1}^\infty \dfrac{1}{(2n-1)^4}$ | $\dfrac{\pi^4}{96}$ |

Fuentes: [[S13-1 Tema 01 - Ejercicio 1 - Parseval prueba suma 1 sobre n cuadrado]], [[S13-2 Tema 01 - Ejercicio 2 - Parseval convergencia 1 sobre (2n-1) cuarta]]
