---
title: "Series de Maclaurin y Laurent — definición y procedimiento"
curso: "[[SeriesTransformadas MOC]]"
unidad: 2
semana: 10
orden: 0
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/series-de-maclaurin
  - tema/series-de-laurent
  - tema/anillo-de-convergencia
date: 2026-05-25
---

## Idea central

La semana 10 cierra el bloque de series con dos representaciones:

- La **serie de Maclaurin** es el caso particular de la [[S09-0 Tema 01 - Series de Taylor en numeros complejos|serie de Taylor]] con centro $z_0 = 0$. Sirve cuando $f$ es **analítica** en un disco alrededor del origen.
- La **serie de Laurent** generaliza a Taylor para funciones que **no son analíticas** en el centro: admite **potencias negativas** $(z - z_0)^{-n}$ y representa a $f$ en un **anillo** $R_1 < |z - z_0| < R_2$ alrededor de una singularidad.

Al finalizar la semana se aplican ambas series para **resolver integrales de contorno** de funciones complejas, conectando con la [[S07-0 Tema 01 - Relacion del teorema de Cauchy y una integral|fórmula integral de Cauchy]] de la semana 7.

Fuente: [[Semana10-Manual-Maclaurin-Laurent.pdf|Manual — Aplicación de las series de Maclaurin y Laurent]].

## 1. Serie de Maclaurin

Partiendo de la serie de Taylor:

$$f(z) = f(z_0) + \frac{f'(z_0)}{1!}(z - z_0) + \frac{f''(z_0)}{2!}(z - z_0)^2 + \cdots + \frac{f^{(n)}(z_0)}{n!}(z - z_0)^n$$

Si $z_0 = 0$ se reduce a la **serie de Maclaurin**:

> [!summary] Serie de Maclaurin
> $$f(z) = \sum_{n=0}^{\infty} \frac{f^{(n)}(0)}{n!}\,z^n \qquad (|z| < R_0)$$

Donde:
- $f^{(n)}(0)$ = $n$-ésima derivada evaluada en el origen.
- $R_0$ = radio de convergencia (distancia del origen a la singularidad más cercana de $f$).

> [!tip] Atajo: serie geométrica
> Cuando $f$ es una función racional simple, suele ser más rápido reescribirla como serie geométrica $\dfrac{1}{1-w} = \sum_{n=0}^\infty w^n$ (con $|w|<1$) que derivar $n$ veces. Ver [[S10-1 Tema 01 - Maclaurin Ej1 - z sobre (z+9)|Ej 1]].

## 2. Serie de Laurent

### Motivación

Sean $C_1$ y $C_2$ círculos concéntricos de radios $R_1$ y $R_2$ ($R_1 < R_2$) con centro en $z_0$. Si $f(z)$ es **unívoca y analítica** sobre $C_1$, $C_2$ y en la región anular $C$ (el **anillo**) entre ambos, pero **no necesariamente en $z_0$**, entonces no se puede aplicar Taylor en $z_0$ — pero sí existe una representación en serie que contiene **potencias positivas y negativas** de $(z - z_0)$.

> [!summary] Teorema de Laurent
> Si $f$ es analítica en el dominio anular $R_1 < |z - z_0| < R_2$ y $C$ es cualquier contorno cerrado simple orientado positivamente en torno de $z_0$ contenido en ese dominio, entonces:
> $$f(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n + \sum_{n=1}^{\infty} \frac{b_n}{(z - z_0)^n} \qquad (R_1 < |z - z_0| < R_2)$$
> con
> $$a_n = \frac{1}{2\pi i}\oint_C \frac{f(z)\,dz}{(z - z_0)^{n+1}}, \qquad b_n = \frac{1}{2\pi i}\oint_C \frac{f(z)\,dz}{(z - z_0)^{-n+1}}$$

### Forma compacta

Reuniendo ambas sumas en un solo índice $n$ que recorre los enteros:

$$f(z) = \sum_{n=-\infty}^{\infty} c_n (z - z_0)^n \qquad (R_1 < |z - z_0| < R_2)$$

$$c_n = \frac{1}{2\pi i}\oint_C \frac{f(z)\,dz}{(z - z_0)^{n+1}}, \qquad n = 0, \pm 1, \pm 2, \ldots$$

- La parte $\sum a_n (z-z_0)^n$ se llama **parte analítica** (potencias $\geq 0$).
- La parte $\sum b_n (z-z_0)^{-n}$ se llama **parte principal** (potencias negativas) — es la que delata la singularidad.

> [!note] Las regiones que define una función
> Cada singularidad parte el plano en anillos distintos. Para $f$ con singularidades en $|z|=1$ y $|z|=2$ centrada en $0$, hay tres regiones: $|z|<1$, $1<|z|<2$ y $|z|>2$. **La serie de Laurent vive en el anillo** (la región intermedia). Ver [[S10-2 Tema 01 - Laurent Ej2 - region anular -1 sobre (z-1)(z-2)|Ej 2]].

## 3. Conexión con integrales de contorno

El coeficiente $c_{-1}$ (es decir $b_1$, el término en $(z-z_0)^{-1}$) es el **residuo** de $f$ en $z_0$. De la fórmula del coeficiente con $n = -1$:

$$c_{-1} = \frac{1}{2\pi i}\oint_C f(z)\,dz \qquad \Longrightarrow \qquad \boxed{\;\oint_C f(z)\,dz = 2\pi i\,c_{-1}\;}$$

> [!success] Regla operativa para integrales
> Al integrar una serie de Laurent sobre un contorno cerrado que rodea $z_0$, **solo sobrevive el término** $(z - z_0)^{-1}$ (los demás se anulan, pues $\oint (z-z_0)^k\,dz = 0$ para $k \neq -1$). Por tanto, basta hallar el coeficiente de $(z - z_0)^{-1}$ en la expansión de Laurent y multiplicarlo por $2\pi i$.

Si el contorno encierra **varias** singularidades, se suman las contribuciones de cada una. Ver [[S10-3 Tema 01 - Integral Ej3 - 5z-2 sobre z(z-1)|Ej 3]] y [[S10-4 Tema 01 - Integral Ej4 - (z+1) sobre (z2-2z)|Ej 4]].

## Procedimiento operativo (Laurent en un anillo)

1. **Identificar las singularidades** del denominador ($h(z) = 0$).
2. **Graficar** los círculos de singularidad y elegir el **anillo** de trabajo (la región pedida).
3. **Descomponer en fracciones parciales** si hay varios factores en el denominador.
4. Para cada fracción, **forzar la forma de serie geométrica** $\dfrac{1}{1 - w}$, usando la condición del anillo para decidir si se factoriza $z$ (cuando $|z|>r$, parte principal) o la constante (cuando $|z|<r$, parte analítica).
5. **Expandir** cada término y reunir potencias positivas y negativas.
6. Si se pide una **integral**, quedarse con el coeficiente de $(z - z_0)^{-1}$ y multiplicar por $2\pi i$ (sumando singularidades interiores).

## Bibliografía

- Churchill, R. V., & Brown, J. W. (2014). *Variable compleja y aplicaciones* (9.ª ed.). McGraw-Hill — §66–68 (Series de Laurent), §62 (Maclaurin).
- Spiegel, M. R. (2009). *Variable compleja* (Schaum). McGraw-Hill — Cap. 6 (series de Taylor y Laurent).
- Material del curso: [[Semana10-Manual-Maclaurin-Laurent.pdf|Manual — Aplicación de las series de Maclaurin y Laurent]].
