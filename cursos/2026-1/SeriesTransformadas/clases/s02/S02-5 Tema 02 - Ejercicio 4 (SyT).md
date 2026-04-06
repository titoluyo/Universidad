---
title: Ejercicio 4 - Limites por trayectorias, polares, infinito y continuidad
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 2
orden: 5
tipo: ejercicio
tags:
  - curso/series-transformadas
  - tipo/ejercicio
  - tema/limites-complejos
  - tema/continuidad-complejas
  - tema/trayectorias
  - tema/coordenadas-polares
date: 2026-04-05
---

## Ejercicio 4a: Limite de un polinomio (sustitucion directa)

Calcular $\displaystyle\lim_{z \to 2+i} (z^2 - 3z + 2)$.

### Desarrollo

Como $f(z) = z^2 - 3z + 2$ es un polinomio, es [[S02-1 Tema 02 - Limites y continuidad de funciones complejas#Propiedades de la continuidad|continua en todo]] $\mathbb{C}$, por lo que evaluamos directamente:

$$f(2+i) = (2+i)^2 - 3(2+i) + 2$$

$$= (4 + 4i + i^2) - 6 - 3i + 2$$

$$= 4 + 4i - 1 - 6 - 3i + 2$$

$$= -1 + i$$

> [!success] Resultado
> $$\lim_{z \to 2+i} (z^2 - 3z + 2) = -1 + i$$

## Ejercicio 4b: Limite que no existe (analisis por trayectorias)

Determinar si existe $\displaystyle\lim_{z \to 0} \frac{z}{\bar{z}}$.

### Desarrollo

Sea $f(z) = \dfrac{z}{\bar{z}}$ para $z \neq 0$. Analizamos por [[S02-1 Tema 02 - Limites y continuidad de funciones complejas#Analisis por trayectorias|trayectorias]].

**En coordenadas polares:** $z = re^{i\theta}$

$$f(z) = \frac{re^{i\theta}}{re^{-i\theta}} = e^{2i\theta}$$

El valor de $f(z)$ depende **solo de $\theta$**, no de $r$:

| Trayectoria | $\theta$ | $f(z) = e^{2i\theta}$ |
| --- | --- | --- |
| Eje real positivo | $0$ | $e^0 = 1$ |
| Recta $y = x$ | $\pi/4$ | $e^{i\pi/2} = i$ |
| Eje imaginario | $\pi/2$ | $e^{i\pi} = -1$ |

Como obtenemos valores distintos segun la direccion de aproximacion, el limite no existe.

> [!fail] Resultado
> El limite $\displaystyle\lim_{z \to 0} \frac{z}{\bar{z}}$ **no existe**.

## Ejercicio 4c: Limite por coordenadas polares

Determinar si existe $\displaystyle\lim_{z \to 0} \frac{z^2}{\bar{z}}$.

### Desarrollo

Usamos [[S02-1 Tema 02 - Limites y continuidad de funciones complejas#Coordenadas polares|coordenadas polares]] con $z = re^{i\theta}$:

$$f(z) = \frac{z^2}{\bar{z}} = \frac{r^2 e^{i2\theta}}{re^{-i\theta}} = r\,e^{i3\theta}$$

Tomamos el modulo:

$$|f(z)| = |r\,e^{i3\theta}| = r$$

Cuando $r \to 0$: $|f(z)| = r \to 0$, independientemente de $\theta$.

> [!success] Resultado
> $$\lim_{z \to 0} \frac{z^2}{\bar{z}} = 0$$

## Ejercicio 4d: Limite que no existe ($\text{Re}(z)/|z|$)

Determinar si existe $\displaystyle\lim_{z \to 0} \frac{\text{Re}(z)}{|z|}$.

### Desarrollo

Con $z = x + iy$: $f(z) = \dfrac{x}{\sqrt{x^2 + y^2}}$

**Por el eje real positivo** ($y = 0$, $x \to 0^+$):

$$f(x) = \frac{x}{|x|} = \frac{x}{x} = 1$$

**Por el eje real negativo** ($y = 0$, $x \to 0^-$):

$$f(x) = \frac{x}{|x|} = \frac{x}{-x} = -1$$

Como $1 \neq -1$:

> [!fail] Resultado
> El limite $\displaystyle\lim_{z \to 0} \frac{\text{Re}(z)}{|z|}$ **no existe**.

## Ejercicio 4e: Limite en el infinito

Calcular $\displaystyle\lim_{z \to \infty} \frac{2z + 1}{z - 3}$.

### Desarrollo

Usamos las [[S02-1 Tema 02 - Limites y continuidad de funciones complejas#Limites y el punto infinito|propiedades de limites en el infinito]]. Dividimos numerador y denominador por $z$:

$$\frac{2z + 1}{z - 3} = \frac{2 + 1/z}{1 - 3/z}$$

Cuando $|z| \to \infty$: $1/z \to 0$ y $3/z \to 0$.

> [!success] Resultado
> $$\lim_{z \to \infty} \frac{2z + 1}{z - 3} = \frac{2}{1} = 2$$

## Ejercicio 4f: Limite infinito

Estudiar $\displaystyle\lim_{z \to 2} \frac{1}{(z - 2)^2}$.

### Desarrollo

Cuando $z \to 2$: $(z - 2) \to 0$, entonces $(z-2)^2 \to 0$ y $\left|\dfrac{1}{(z-2)^2}\right| \to \infty$.

Formalmente: dado $M > 0$, tomamos $\delta = 1/\sqrt{M}$. Si $0 < |z - 2| < \delta$:

$$\left|\frac{1}{(z-2)^2}\right| = \frac{1}{|z-2|^2} > \frac{1}{\delta^2} = M$$

> [!success] Resultado
> $$\lim_{z \to 2} \frac{1}{(z-2)^2} = \infty$$

## Ejercicio 4g: Continuidad de $f(z) = |z|^2$

Estudiar la continuidad de $f(z) = |z|^2$.

### Desarrollo

Descomponemos en [[S02-1 Tema 02 - Limites y continuidad de funciones complejas#Teorema continuidad por componentes|componentes reales]]:

$$f(z) = |z|^2 = x^2 + y^2$$

Donde:
- $u(x,y) = x^2 + y^2$ (continua en $\mathbb{R}^2$)
- $v(x,y) = 0$ (continua en $\mathbb{R}^2$)

Como ambas componentes son continuas:

> [!success] Resultado
> $f(z) = |z|^2$ es **continua en todo** $\mathbb{C}$.

## Ejercicio 4h: Continuidad de funcion definida por casos

Estudiar la continuidad de:

$$f(z) = \begin{cases} \dfrac{z^2}{|z|}, & z \neq 0 \\ 0, & z = 0 \end{cases}$$

### Desarrollo

**Para $z \neq 0$:** $f$ es cociente de funciones continuas con denominador no nulo, por lo tanto es continua.

**En $z = 0$:** verificamos si $\displaystyle\lim_{z \to 0} f(z) = f(0) = 0$.

$$|f(z) - f(0)| = \left|\frac{z^2}{|z|}\right| = \frac{|z|^2}{|z|} = |z|$$

Dado $\varepsilon > 0$, tomamos $\delta = \varepsilon$. Si $|z| < \delta$:

$$|f(z) - f(0)| = |z| < \delta = \varepsilon$$

> [!success] Resultado
> $f$ es **continua en todo** $\mathbb{C}$ (incluido $z = 0$).

## Ejercicio 4i: Singularidad removible

Sea $f(z) = \dfrac{z^4 - 1}{z^2 + 1}$. Determinar puntos de discontinuidad y $\displaystyle\lim_{z \to i} f(z)$.

### Desarrollo

Factorizamos el numerador:

$$z^4 - 1 = (z^2 - 1)(z^2 + 1)$$

Para $z^2 + 1 \neq 0$ (es decir, $z \neq \pm i$):

$$f(z) = \frac{(z^2 - 1)(z^2 + 1)}{z^2 + 1} = z^2 - 1$$

$f$ no esta definida en $z = \pm i$ (denominador se anula), pero el limite existe:

$$\lim_{z \to i} f(z) = \lim_{z \to i} (z^2 - 1) = i^2 - 1 = -1 - 1 = -2$$

> [!info] Singularidad removible
> En $z = \pm i$, $f$ tiene **singularidades removibles**: el limite existe pero $f$ no esta definida. Se puede extender $f$ definiendo $f(\pm i) = -2$.

> [!success] Resultado
> - $f$ es discontinua en $z = \pm i$ (no esta definida)
> - $\displaystyle\lim_{z \to i} f(z) = -2$
