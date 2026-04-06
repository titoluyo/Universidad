---
title: Limites y continuidad de funciones complejas
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 2
orden: 1
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/limites-complejos
  - tema/continuidad-complejas
date: 2026-04-05
---

## Limite de una funcion compleja

### Definicion

Sea una funcion definida en todos los puntos $z$ de un entorno punteado de $z_0$. Definimos el limite de $f(z)$, cuando $z$ tiende a $z_0$, resulta un numero $w_0$, definido por:

$$\lim_{z \to z_0} f(z) = w_0 \quad (1)$$

Si (1) es correcto, significa que, para cada numero $\varepsilon$, existe un numero positivo $\delta$ tal que:

$$|f(z) - w_0| < \varepsilon \text{ siempre que } 0 < |z - z_0| < \delta \quad (2)$$

Geometricamente, esta definicion nos dice que para cada $\varepsilon$ entorno punteado $|w - w_0| < \varepsilon$ de $w_0$, existe un $\delta$ entorno $0 < |z - z_0| < \delta$ de $z_0$ tal que todo punto $z$ en el tiene una imagen $w$ que esta en el entorno.

> [!info] Figura 1
> (a) valor de los puntos $z$ y (b) imagen de los puntos $z$ evaluados en $f(z)$

### Observaciones importantes

1. $z_0$ debe ser un **punto de acumulacion** del dominio $D$
2. No es necesario que $f$ este definida en $z_0$
3. El limite $w_0$, si existe, es **unico**
4. La definicion es analoga a la de funciones reales, pero usando el modulo complejo $|\cdot|$

### Teorema: limite por componentes

Sea $f(z) = u(x,y) + iv(x,y)$ donde $z = x + iy$. Entonces:

$$\lim_{z \to z_0} f(z) = L \iff \lim_{(x,y) \to (x_0,y_0)} u(x,y) = \text{Re}(L) \quad \text{y} \quad \lim_{(x,y) \to (x_0,y_0)} v(x,y) = \text{Im}(L)$$

Es decir, el limite de $f(z)$ existe si y solo si los limites de sus partes real e imaginaria existen por separado.

## Continuidad de una funcion compleja

### Definicion

Una funcion $f$ es continua en un punto $z_0$ si se satisfacen estas tres condiciones:

1. $\displaystyle\lim_{z \to z_0} f(z)$ existe
2. $f(z_0)$ existe
3. $\displaystyle\lim_{z \to z_0} f(z) = f(z_0)$

Una funcion de una variable compleja se dice que es continua en una region $R$, si cumple la continuidad en todos sus puntos.

### Teorema: continuidad por componentes

Sea $f(z) = u(x,y) + iv(x,y)$. Entonces $f$ es continua en $z_0 = x_0 + iy_0$ si y solo si $u$ y $v$ son continuas en $(x_0, y_0)$.

### Propiedades de la continuidad

Si $f$ y $g$ son continuas en $z_0$, entonces:

1. $f + g$ es continua en $z_0$
2. $f \cdot g$ es continua en $z_0$
3. $f / g$ es continua en $z_0$ (si $g(z_0) \neq 0$)
4. $cf$ es continua en $z_0$ ($c \in \mathbb{C}$ constante)

> [!abstract] Corolarios importantes
> 1. Los **polinomios** son continuos en todo $\mathbb{C}$
> 2. Las **funciones racionales** son continuas en todos los puntos donde el denominador no se anula

### Criterios de discontinuidad

Una funcion $f$ **no es continua** en $z_0$ si se cumple al menos una de:

1. $f$ no esta definida en $z_0$
2. $\displaystyle\lim_{z \to z_0} f(z)$ no existe
3. $\displaystyle\lim_{z \to z_0} f(z) \neq f(z_0)$

> [!example] Ejemplo
> Si $f(z) = \begin{cases} z^2, & z \neq i \\ z, & z = i \end{cases}$ entonces si evaluamos:
> - $\lim_{z \to i} f(z) = \lim_{z \to i} z^2 = (i)^2 = -1$
> - $f(z_0) = f(i) = i$
>
> Asi, $\lim_{z \to z_0} f(z) \neq f(z_0)$ y la funcion **no es continua**.

## Propiedades de los limites

Sean $\lim_{z \to z_0} f(z)$ y $\lim_{z \to z_0} g(z)$ limites que existen:

1. **Suma:** $\displaystyle\lim_{z \to z_0} \{f(z) + g(z)\} = \lim_{z \to z_0} f(z) + \lim_{z \to z_0} g(z)$
2. **Resta:** $\displaystyle\lim_{z \to z_0} \{f(z) - g(z)\} = \lim_{z \to z_0} f(z) - \lim_{z \to z_0} g(z)$
3. **Producto:** $\displaystyle\lim_{z \to z_0} \{f(z) \cdot g(z)\} = \left\{ \lim_{z \to z_0} f(z) \right\} \left\{ \lim_{z \to z_0} g(z) \right\}$
4. **Cociente:** $\displaystyle\lim_{z \to z_0} \left( \frac{f(z)}{g(z)} \right) = \frac{\lim_{z \to z_0} f(z)}{\lim_{z \to z_0} g(z)}$, siempre que $\lim_{z \to z_0} g(z) \neq 0$
5. **Multiplo constante:** $\displaystyle\lim_{z \to z_0} c \cdot f(z) = c \cdot \lim_{z \to z_0} f(z)$, con $c \in \mathbb{C}$ constante

### Ejemplos de aplicacion

**Ejemplo 1:** Sea $\lim_{z \to z_0} f(z) = 2$ y $\lim_{z \to z_0} g(z) = 4$.

$$\lim_{z \to z_0} \{f(z) + g(z)\} = 2 + 4 = 6$$

**Ejemplo 2:** Sea $\lim_{z \to z_0} f(z) = 2$ y $\lim_{z \to z_0} g(z) = 6$.

$$\lim_{z \to z_0} \{f(z) - g(z)\} = 2 - 6 = -4$$

**Ejemplo 3:** Sea $\lim_{z \to z_0} f(z) = 4$ y $\lim_{z \to z_0} g(z) = 6$.

$$\lim_{z \to z_0} \{f(z) \cdot g(z)\} = 4 \cdot 6 = 24$$

**Ejemplo 4:** Sea $\lim_{z \to z_0} f(z) = 4$ y $\lim_{z \to z_0} g(z) = 6 \neq 0$.

$$\lim_{z \to z_0} \left\{ \frac{f(z)}{g(z)} \right\} = \frac{4}{6} = \frac{2}{3}$$

## Metodos para resolver limites

Cuando la evaluacion directa produce una indeterminacion, se pueden emplear distintos metodos:

| Metodo | Cuando usar |
| --- | --- |
| Sustitucion directa | Funciones continuas (polinomios, racionales sin polo) |
| Racionalizacion | Radicales en el numerador o denominador |
| [[S02-3 Tema 02 - Ejercicio 2 (SyT)\|Regla de L'Hospital]] | Indeterminacion $\frac{0}{0}$ o $\frac{\infty}{\infty}$ |
| Factorizacion | Factores comunes que se cancelan |
| Analisis por trayectorias | Para demostrar que un limite **no existe** |
| Coordenadas polares | Cuando hay simetria radial o involucra $\|z\|$, $\arg(z)$ |

### Analisis por trayectorias

Para demostrar que un limite **no existe**, basta encontrar dos trayectorias de aproximacion a $z_0$ que den resultados distintos.

**Trayectorias comunes:**
- Eje real: $y = 0$, $x \to x_0$
- Eje imaginario: $x = 0$, $y \to y_0$
- Rectas: $y = mx$
- Parabolas: $y = x^2$

> [!example] Ejemplo: $\lim_{z \to 0} \dfrac{\bar{z}}{z}$
> Con $z = x + iy$, $f(z) = \dfrac{x - iy}{x + iy}$
>
> **Por el eje real** ($y = 0$): $f(x) = \dfrac{x}{x} = 1$
>
> **Por el eje imaginario** ($x = 0$): $f(iy) = \dfrac{-iy}{iy} = -1$
>
> Como $1 \neq -1$, el **limite no existe**.

### Coordenadas polares

Con $z = re^{i\theta}$, se sustituye y se analiza el comportamiento cuando $r \to 0$. Si el resultado depende de $\theta$, el limite no existe.

> [!example] Ejemplo: $\lim_{z \to 0} \dfrac{z^2}{\bar{z}}$
> Con $z = re^{i\theta}$:
> $$f(z) = \frac{r^2 e^{i2\theta}}{re^{-i\theta}} = r\cos(2\theta)\,e^{i\theta} + ir\,\text{sen}(2\theta)\,e^{i\theta}$$
>
> Simplificando: $f(z) = r\cos(2\theta)\,e^{i\theta}$
>
> Cuando $r \to 0$: $f(z) \to 0$, independiente de $\theta$. Por lo tanto $\lim_{z \to 0} \dfrac{z^2}{\bar{z}} = 0$.

Ver los ejercicios resueltos:
- [[S02-2 Tema 02 - Ejercicio 1 (SyT)|Ejercicio 1 - Racionalizacion]]
- [[S02-3 Tema 02 - Ejercicio 2 (SyT)|Ejercicio 2 - Regla de L'Hospital]]
- [[S02-4 Tema 02 - Ejercicio 3 (SyT)|Ejercicio 3 - Factorizacion y continuidad]]
- [[S02-5 Tema 02 - Ejercicio 4 (SyT)|Ejercicio 4 - Trayectorias, polares, infinito y continuidad]]

## Limites y el punto infinito

### Propiedades fundamentales

Sea $f(z)$ una funcion de variable compleja:

**P1)** $\displaystyle\lim_{z \to z_0} f(z) = \infty$ si y solo si $\displaystyle\lim_{z \to z_0} \frac{1}{f(z)} = 0$

**P2)** $\displaystyle\lim_{z \to \infty} f(z) = w_0$ si y solo si $\displaystyle\lim_{z \to 0} f\left(\frac{1}{z}\right) = w_0$

**P3)** $\displaystyle\lim_{z \to \infty} f(z) = \infty$ si y solo si $\displaystyle\lim_{z \to 0} \frac{1}{f(1/z)} = 0$

### Definicion: limite cuando $z \to \infty$

$$\lim_{z \to \infty} f(z) = L$$

si para todo $\varepsilon > 0$, existe $M > 0$ tal que:

$$|z| > M \implies |f(z) - L| < \varepsilon$$

### Definicion: limite infinito

$$\lim_{z \to z_0} f(z) = \infty$$

si para todo $M > 0$, existe $\delta > 0$ tal que:

$$0 < |z - z_0| < \delta \implies |f(z)| > M$$

> [!example] Ejemplos
> **1)** $\displaystyle\lim_{z \to \infty} \frac{2z + 1}{z - 3} = \lim_{z \to \infty} \frac{2 + 1/z}{1 - 3/z} = \frac{2}{1} = 2$
>
> **2)** $\displaystyle\lim_{z \to 2} \frac{1}{(z - 2)^2} = \infty$, pues cuando $z \to 2$, $(z-2)^2 \to 0$ y $|f(z)| \to \infty$

## Teoremas importantes

### Caracterizacion secuencial del limite

$$\lim_{z \to z_0} f(z) = L \iff \text{para toda sucesion } \{z_n\} \text{ con } z_n \to z_0,\ z_n \neq z_0: f(z_n) \to L$$

### Conservacion de la continuidad

Si $f: D \to \mathbb{C}$ es continua y $K \subseteq D$ es **compacto**, entonces $f(K)$ es compacto.

### Teorema del valor extremo

Si $f: D \to \mathbb{C}$ es continua y $K \subseteq D$ es **compacto**, entonces $|f|$ alcanza su maximo y minimo en $K$.

## Bibliografia

- Churchill, R., & Ward, J. (2004). *Variable Compleja y Aplicaciones* (7ma ed). McGraw-Hill.
- Murray, S., Seymour, Lipschutz, & Dennis, S. (2011). *Variable compleja* (2nd ed). McGraw-Hill Interamericana de Espana S.L.
- Suarez Bueno, V. (1998). *Introduccion a la Variable Compleja* (1a. ed.). Instituto Politecnico Nacional.
