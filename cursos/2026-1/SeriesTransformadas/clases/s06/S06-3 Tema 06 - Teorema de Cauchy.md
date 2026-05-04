---
title: Teorema de Cauchy
curso: "[[SeriesTransformadas MOC]]"
unidad: 1
semana: 6
orden: 3
tipo: clase
tags:
  - curso/series-transformadas
  - tipo/clase
  - tema/teorema-de-cauchy
  - tema/teorema-de-green
  - tema/funcion-analitica
date: 2026-05-03
---

## Introduccion

El **Teorema de Cauchy** es uno de los pilares del análisis complejo: relaciona la **analiticidad** de una función con el valor de su integral sobre contornos cerrados. Su demostración se apoya en el **Teorema de Green** del cálculo vectorial.

Material de estudio (manual PDF de la semana): [[Semana06_TeoremaCauchy.pdf]]

## Definiciones previas

> [!definition] Trayectoria simple cerrada
> Trayectoria cerrada que no se toca a sí misma (no se cruza).

> [!definition] Dominio simplemente conexo $D$
> Dominio del plano complejo tal que toda trayectoria simple cerrada en $D$ contiene solo puntos de $D$. Intuitivamente: "no tiene huecos".

## Teorema de Green

Sean $P(x, y)$ y $Q(x, y)$ funciones continuas con derivadas parciales en una región $\mathcal{R}$ y sobre su frontera $C$. El **Teorema de Green** establece:

$$\oint_{C}\bigl(P(x,y)\,dx + Q(x,y)\,dy\bigr) = \iint_{\mathcal{R}}\left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\,dx\,dy \tag{1}$$

El teorema es válido para regiones simples y multiplemente conexas.

## Teorema de Cauchy

Recordemos que la **integral compleja** se puede expresar como:

$$\int f(z)\,dz = \int(u\,dx - v\,dy) + i\int(v\,dx + u\,dy) \tag{2}$$

Aplicando el Teorema de Green (1) a (2), tenemos:

$$\int f(z)\,dz = \iint\left(-\frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}\right)\,dx\,dy + i\iint\left(\frac{\partial u}{\partial x} - \frac{\partial v}{\partial y}\right)\,dx\,dy \tag{3}$$

Aplicando las ecuaciones de **Cauchy-Riemann** (cuando $f$ es analítica):

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x} \tag{4}$$

Sustituyendo (4) en (3), ambos integrandos se anulan:

$$\int f(z)\,dz = \iint\left(\frac{\partial u}{\partial y} - \frac{\partial u}{\partial y}\right)\,dx\,dy + i\iint\left(\frac{\partial u}{\partial x} - \frac{\partial u}{\partial x}\right)\,dx\,dy = 0 \tag{5}$$

> [!success] Teorema de Cauchy
> Si $f(z)$ es **analítica** en una región $\mathcal{R}$ simplemente conexa y su derivada $f'$ es **continua** en $\mathcal{R}$, entonces:
>
> $$\boxed{\oint_{C} f(z)\,dz = 0} \tag{6}$$
>
> para toda trayectoria simple cerrada $C$ contenida en $\mathcal{R}$.

## Implicaciones

1. **Independencia del camino:** si $f$ es analítica en un dominio simplemente conexo, $\int_A^B f(z)\,dz$ depende solo de los puntos extremos $A$ y $B$, no del camino.
2. **Existencia de antiderivada:** $f$ admite una primitiva $F(z)$ en el dominio, y $\int_A^B f(z)\,dz = F(B) - F(A)$.
3. **Singularidades importan:** si $f$ tiene una singularidad encerrada por $C$ (e.g. $f(z) = 1/z$ en $|z|=1$), el teorema **no aplica** y la integral puede ser distinta de cero (ver [[S06-1 Tema 06 - Integral de contorno en funciones complejas#Ejercicio resuelto: $\oint \dfrac{dz}{z} = 2\pi i$ con $C: |z|=1$|el ejercicio ∮dz/z = 2πi]]).

Ver [[S06-6 Tema 06 - Teorema de extension de Cauchy|Teorema de extensión]] para el manejo de dominios multiplemente conexos y singularidades.

## Ejercicios

- [[S06-4 Tema 06 - Cauchy Ejercicio 1 - contorno triangular|Ej1 — Comprobar ∮z dz = 0 en contorno triangular]] (video)
- [[S06-5 Tema 06 - Cauchy Ejercicio 2 - circle via Green|Ej2 — Comprobar ∫f(z)dz = 0 con f(z)=z, |z|=1, vía Green]] (paso a paso)

## Bibliografia

- Churchill, R., & Ward, J. (2004). *Variable Compleja y Aplicaciones* (7ma ed). McGraw-Hill.
- Murray, S., Seymour, Lipschutz, & Dennis, S. (2011). *Variable compleja* (2da ed.). McGraw-Hill Interamericana.
- Suarez Bueno, V. (1998). *Introduccion a la Variable Compleja* (1a ed.). Instituto Politecnico Nacional.
